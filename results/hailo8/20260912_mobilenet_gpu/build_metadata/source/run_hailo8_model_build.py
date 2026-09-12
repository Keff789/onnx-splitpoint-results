#!/usr/bin/env python3
"""One private MobileNet Full Hailo8 GPU build; uses the installed DFC builder.

No install/download, no settings update, no inference/energy/bootstrap, no
publication to production model caches. Run --build explicitly to compile.
"""
from __future__ import annotations
import argparse
import contextlib
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import threading
import time
import traceback
import zipfile

HERE = Path(__file__).resolve().parent
SCHEMA = 'hailo8_mobilenet_private_build_r1'
MAX_FILE = 256 * 1024 * 1024
MAX_TOTAL = 512 * 1024 * 1024


def read_json(path: Path):
    if path.stat().st_size > 16 * 1024 * 1024:
        raise ValueError('metadata_over_16MiB:' + str(path))
    return json.loads(path.read_text(encoding='utf-8'))


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def remap_home(path: str, home: Path) -> Path:
    original = Path(path)
    try:
        return home / original.relative_to('/home/kmika')
    except ValueError:
        return original.expanduser().absolute()


def load_tool(root: Path, expectations=None):
    root = root.expanduser().resolve(strict=True)
    expectations = expectations or read_json(HERE / 'SOURCE_PROVENANCE.json')['guarded_production_files']
    checked = {}
    for rel, expected in expectations.items():
        path = root / rel
        if not path.is_file() or path.is_symlink() or digest(path) != expected:
            raise RuntimeError('unreviewed_tool_source:' + str(path) + '; no build started')
        checked[rel] = expected
    for path in (root / 'scripts', root, HERE):
        sys.path.insert(0, str(path))
    import onnx_splitpoint_tool as tool
    if not Path(tool.__file__).resolve().is_relative_to(root):
        raise RuntimeError('tool_imported_from_other_installation')
    return {'root': str(root), 'version': tool.__version__, 'python': sys.executable,
            'checked_files': checked}


@contextlib.contextmanager
def interlock():
    import fcntl
    from onnx_splitpoint_tool.workflow.run_control import platform_workflow_interlock_path
    path = platform_workflow_interlock_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_CREAT | os.O_RDWR | os.O_CLOEXEC | os.O_NOFOLLOW, 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError('workflow_or_platform_operation_active') from exc
        yield
    finally:
        os.close(fd)


def find_exact(candidates, sha, size=None):
    """Only explicit known paths; never scan model/cache trees or build a fallback."""
    seen, tried = set(), []
    for p in candidates:
        p = Path(p).expanduser().absolute()
        if str(p) in seen:
            continue
        seen.add(str(p))
        if not p.is_file():
            tried.append(str(p) + ': missing')
            continue
        if size is not None and p.stat().st_size != size:
            tried.append(str(p) + ': size_mismatch')
            continue
        if digest(p) == sha:
            return p
        tried.append(str(p) + ': digest_mismatch')
    raise FileNotFoundError('exact_original_asset_not_found; expected_sha256=' + sha + '; tried=' + repr(tried))


def prepare(args, out: Path):
    from h8_model_request import (prepare_request, file_identity, check_identity,
                                  validate_request, write_json)
    from onnx_splitpoint_tool.hailo_dependency_plan import child_library_environment
    from onnx_splitpoint_tool.hailo_backend import _load_valid_hailo_receipt
    baseline = read_json(HERE / 'inputs/baseline_inputs.json')
    gate = read_json(HERE / 'inputs/compute_gate.json')
    if gate['summary']['status'] != 'compute_pass' or gate['gpu_compute_result']['family'] != 'hailo8':
        raise ValueError('recorded_hailo8_compute_gate_not_passed')
    home = Path.home()
    original = baseline['cpu_build_receipt']
    overlay = args.overlay or remap_home(baseline['dependency_manifest']['path'], home)
    bound = {**baseline['dependency_manifest'], 'path': str(overlay)}
    check_identity(bound)
    venv_python = remap_home(baseline['venv_python'], home)
    # Metadata/filesystem only. Do not rerun the successful GPU compute checks.
    child_library_environment({}, family='hailo8', selected_python=str(venv_python), manifest_path=overlay)
    print('OVERLAY_PREFLIGHT=PASS; no download; no repeated compute smoke', flush=True)
    run = args.run_dir or remap_home(baseline['default_run_dir'], home)
    suite = run / 'models/mobilenet_v3_large/benchmark_set/legacy_suite'
    cpu_candidates = [args.cpu_hef] if args.cpu_hef else [suite / 'hailo/hailo8/full/compiled.hef']
    cpu = find_exact(cpu_candidates, original['hef_sha256'], original['hef_size_bytes'])
    receipt = _load_valid_hailo_receipt(cpu, source_onnx_sha256=original['source_onnx_sha256'],
                                       cache_key=original['cache_key'], expected_net_name='mobilenet_v3_large_full')
    if not receipt or receipt['hw_arch'] != 'hailo8' or receipt['cache_payload'] != original['cache_payload']:
        raise ValueError('baseline_not_the_recorded_productive_HAILO8_CPU_HEF')
    source = find_exact([remap_home(baseline['source_onnx']['path'], home)],
                        original['source_onnx_sha256'], baseline['source_onnx']['size_bytes'])
    filename = original['compiler_onnx_filename']
    known_old = home / 'Models/EvaluationRuns/biggerset_20260908_210306/models/mobilenet_v3_large/benchmark_set/legacy_suite'
    graphs = [args.compiler_onnx] if args.compiler_onnx else [
        suite / 'hailo/hailo8/full' / filename, cpu.resolve().parent / filename,
        known_old / 'hailo/hailo8/full' / filename,
        # Identical graph bytes are allowed, never the Hailo10 HEF/receipt.
        suite / 'hailo/hailo10/full' / filename,
        remap_home(baseline['compiler_onnx']['path'], home)]
    compiler = find_exact(graphs, original['compiler_onnx_sha256'], baseline['compiler_onnx']['size_bytes'])
    images = [{**r, 'path': str(remap_home(r['path'], home))} for r in baseline['images']]
    for r in images:
        check_identity(r)
    write_json(out / 'fixed16_images.json', images)
    cal_manifest = {**baseline['calibration_manifest'], 'path': str(remap_home(baseline['calibration_manifest']['path'], home))}
    check_identity(cal_manifest)
    print('MODEL_INPUTS=verified Hailo8 CPU-HEF + exact compiler ONNX; checking B500', flush=True)
    request = prepare_request(cpu_hef=cpu, source_onnx=source, compiler_onnx=compiler,
        calibration_dir=remap_home(baseline['calibration_dir'], home),
        images_json=out / 'fixed16_images.json', venv=venv_python,
        timeout_s=args.timeout_s, calibration_manifest=cal_manifest['path'])
    expected_cal = [{**r, 'path':str(remap_home(r['path'],home))} for r in baseline['calibration_records']]
    if request['calibration_records'] != expected_cal or request['images'] != images:
        raise ValueError('fixed_calibration_or_fixed16_differ_from_prior_diagnosis')
    request['dependency_manifest'] = file_identity(overlay)
    request['gpu_selector'] = gate['gpu_compute_result']['environment']['CUDA_VISIBLE_DEVICES']
    request['evidence_note'] = 'New Hailo8-only request; CPU baseline Hailo8. Calibration and fixed16 from previously opened diagnostic cohort.'
    validate_request(request)
    write_json(out / 'request.json', request)
    write_json(out / 'overlay_manifest.json', read_json(overlay))
    write_json(out / 'baseline_cpu_receipt.json', receipt)
    print('PREFLIGHT=PASS; B500 / Opt1 / Batch8 / relaxed; fixed16 reserved, inference not run', flush=True)
    return request


def configuration_state(home: Path, tool: Path):
    paths = [home/'.onnx_splitpoint_tool/run_modes.yaml',
             home/'.onnx_splitpoint_tool/hardware_setups.yaml',
             tool/'profiles/CompleteSetDev.yaml']
    return {str(p): {'sha256':digest(p),'size':p.stat().st_size} if p.is_file() else None for p in paths}


class ConsoleTail:
    def __init__(self, path: Path):
        self.path, self.stop_event = path, threading.Event()
        self.thread = threading.Thread(target=self.run, daemon=True)
    def __enter__(self):
        self.thread.start(); return self
    def run(self):
        position, start, heartbeat = 0, time.monotonic(), time.monotonic()
        while True:
            try:
                if self.path.is_file():
                    with self.path.open('rb') as f:
                        f.seek(position); data=f.read(256 * 1024); position=f.tell()
                    if data:
                        print(data.decode('utf-8', errors='replace'), end='', flush=True)
            except OSError:
                pass
            if self.stop_event.is_set():
                if not self.path.is_file() or position >= self.path.stat().st_size:
                    break
            now=time.monotonic()
            if now-heartbeat >= 15:
                print(f'HEARTBEAT=model_build elapsed_s={now-start:.0f}', flush=True); heartbeat=now
            self.stop_event.wait(0.2)
    def __exit__(self, *exc):
        self.stop_event.set(); self.thread.join(timeout=5)


def worker(request_file: Path, out: Path):
    from h8_model_request import validate_request, private_environment, builder_arguments, write_json
    from build_observation import GpuActivity, summarize_result
    request=read_json(request_file)
    validate_request(request)
    env=private_environment(request, out)
    # Selection is process-local. Never persist it to any GUI/run-mode registry.
    env['ONNX_SPLITPOINT_HAILO8_DEPENDENCY_MANIFEST']=request['dependency_manifest']['path']
    os.environ.clear(); os.environ.update(env)
    os.chdir(out)
    from onnx_splitpoint_tool.hailo_backend import hailo_build_hef_auto
    activity=GpuActivity(out)
    result=None
    try:
        activity.start()
        with (out/'compiler.log').open('w',encoding='utf-8') as log:
            def on_log(*parts):
                line=' '.join(str(part) for part in parts)
                log.write(line+'\n'); log.flush(); print(line,flush=True)
            kwargs=builder_arguments(request,out)
            if kwargs['hw_arch'] != 'hailo8' or kwargs['publish_artifacts'] is not False or kwargs['force'] is not True:
                raise RuntimeError('private_H8_build_arguments_invalid')
            write_json(out/'builder_arguments.json',kwargs)
            result=asdict(hailo_build_hef_auto(**kwargs,on_log=on_log))
            write_json(out/'build_result.json',result)
    except BaseException as exc:
        write_json(out/'primary_error.json',{'type':type(exc).__name__,'error':str(exc)})
        (out/'worker_traceback.log').write_text(traceback.format_exc(),encoding='utf-8')
        raise
    finally:
        activity.stop()
    summary=summarize_result(result,request,out,activity.samples)
    context=summary.get('compiler_context') or {}
    if context.get('family') != 'hailo8' or context.get('dependency_manifest') != request['dependency_manifest']['path']:
        summary.update(model_build_status='failed',error='effective_H8_dependency_context_not_verified')
    if summary.get('private_hef'):
        from onnx_splitpoint_tool.hailo_backend import _load_valid_hailo_receipt
        r=_load_valid_hailo_receipt(Path(summary['private_hef']['path']),allow_diagnostic=True)
        if not r or r.get('hw_arch') != 'hailo8' or r.get('publish_artifacts') is not False:
            summary.update(model_build_status='failed',error='private_receipt_family_or_nonpublishing_mismatch')
        if r:
            write_json(out/'private_hef_receipt.json',r)
    validate_request(request)
    summary.update(schema=SCHEMA, family='hailo8', frozen_inputs_unchanged=True,
                   runtime_status='not_run', quality_status='not_evaluated', model_acceptance='NOT_EVALUATED',
                   g3_status='incomplete_runtime_comparison_pending')
    write_json(out/'summary.json',summary)
    return 0 if summary.get('model_build_status') == 'pass' else 2


def finish_status(summary, process):
    summary=dict(summary)
    summary['supervision']=process
    bad=(process.get('returncode') != 0 or process.get('timed_out') or process.get('cancelled')
         or process.get('cleanup_complete') is not True or process.get('lingering_children_after_cli'))
    if bad:
        summary['model_build_status']='cancelled' if process.get('cancelled') else 'failed'
        summary.setdefault('error','supervised_model_build_failed_or_incomplete')
    if process.get('cancelled'):
        status='cancelled'; rc=130
    elif summary.get('model_build_status')=='pass' and not bad:
        status='build_and_gpu_pass' if summary.get('gpu_execution_status')=='pass' else 'build_pass_gpu_unproven'
        rc=0 if status=='build_and_gpu_pass' else 2
    else:
        status='failed'; rc=2
    summary.update(test_status=status,model_acceptance='NOT_EVALUATED',runtime_status='not_run',
                   quality_status='not_evaluated',g3_status='incomplete_runtime_comparison_pending')
    return summary,rc


def export_evidence(out: Path):
    """Explicit metadata/log allowlist. Atomic non-overwriting final archive."""
    archive=out.with_suffix('.zip')
    names=['launcher_summary.json','tool_source_check.json','configuration_before.json','configuration_after.json',
           'configuration_preservation.json','fixed16_images.json','request.json','overlay_manifest.json',
           'baseline_cpu_receipt.json','summary.json','build_result.json','primary_error.json','supervision.json',
           'gpu_activity.json','gpu_activity.log','compiler.log','worker.log','worker_traceback.log',
           'builder_arguments.json','private_hef_receipt.json','preflight_error.json',
           'build/hailo_build_phases.json','build/hailo_compiler_context.json']
    sources=[]
    for name in names:
        sources.append((out/name,name))
    metadata=out/'build/hailo_compiler_context.json'
    if metadata.is_file():
        try:
            ctx=read_json(metadata)
            trace=Path(ctx.get('ptxas_trace_path','')).resolve()
            if trace.is_relative_to(out.resolve()):
                sources.append((trace,'ptxas_invocations.jsonl'))
        except (OSError,ValueError,TypeError):
            pass
    for name in ('run_hailo8_model_build.py','h8_model_request.py','build_observation.py','SOURCE_PROVENANCE.json'):
        sources.append((HERE/name,'source/'+name))
    fd,tmp=tempfile.mkstemp(prefix=archive.name+'.tmp-',dir=out.parent)
    os.close(fd)
    rows=[]; total=0
    try:
        with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED,allowZip64=True) as z:
            for path,name in sources:
                if not path.is_file() or path.is_symlink():
                    rows.append({'path':name,'status':'not_present_or_symlink'});continue
                size=path.stat().st_size
                if size>MAX_FILE or total+size>MAX_TOTAL:
                    rows.append({'path':name,'status':'omitted_size_limit','size_bytes':size});continue
                z.write(path,name);total+=size
                rows.append({'path':name,'status':'included','size_bytes':size})
            z.writestr('collection_inventory.json',json.dumps({'schema':SCHEMA,'rows':rows,'source_payload_bytes':total,
                 'models_and_libraries_included':False,'complete_model_archive':False},indent=2))
        with zipfile.ZipFile(tmp) as z:
            bad=z.testzip()
            if bad: raise RuntimeError('zip_crc_failed:'+bad)
        with open(tmp,'rb') as f: os.fsync(f.fileno())
        os.link(tmp,archive)  # atomic and refuses to overwrite any existing evidence
        return archive
    finally:
        Path(tmp).unlink(missing_ok=True)


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    mode=p.add_mutually_exclusive_group()
    mode.add_argument('--build',action='store_true',help='prepare and execute exactly one private build')
    mode.add_argument('--prepare-only',action='store_true',help='validate inputs; no model build')
    p.add_argument('--tool',type=Path,default=Path(os.environ.get('ONNX_SPLITPOINT_TOOL_DIR',str(Path.home()/'ONNX-Splitpoint-Tool'))))
    p.add_argument('--run-dir',type=Path)
    p.add_argument('--cpu-hef',type=Path)
    p.add_argument('--compiler-onnx',type=Path)
    p.add_argument('--overlay',type=Path)
    p.add_argument('--timeout-s',type=int,default=7200)
    p.add_argument('--output-parent',type=Path,default=Path.home()/'Downloads')
    p.add_argument('--_worker',action='store_true',help=argparse.SUPPRESS)
    p.add_argument('--request',type=Path,help=argparse.SUPPRESS)
    p.add_argument('--work',type=Path,help=argparse.SUPPRESS)
    args=p.parse_args(argv)
    if not 600<=args.timeout_s<=86400: p.error('timeout-s must be 600..86400')
    try:
        tool_info=load_tool(args.tool)
    except Exception as exc:
        print('MODEL_BUILD_STARTED=NO\nERROR='+type(exc).__name__+': '+str(exc),flush=True);return 2
    if args._worker:
        return worker(args.request,args.work)
    from h8_model_request import write_json,validate_request
    from deepx_full_workflow_smoke_worker_v27930 import supervised_run
    out=None; summary={'schema':SCHEMA,'family':'hailo8','test_status':'not_started','model_build_status':'not_run',
                       'gpu_execution_status':'not_run','model_acceptance':'NOT_EVALUATED','runtime_status':'not_run',
                       'publication':'private_only','product_cache_publication_disabled':True}
    rc=2
    try:
        with interlock():
            args.output_parent.mkdir(parents=True,exist_ok=True)
            out=Path(tempfile.mkdtemp(prefix='hailo8_mobilenet_gpu_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'_',dir=args.output_parent))
            print('TEST_DIRECTORY='+str(out),flush=True)
            write_json(out/'tool_source_check.json',tool_info)
            before=configuration_state(Path.home(),args.tool)
            write_json(out/'configuration_before.json',before)
            try:
                # Read/test files only; do not change existing DFC installation.
                if shutil.disk_usage(out).free < 8*1024**3:
                    raise RuntimeError('insufficient_free_space: need at least 8 GiB plus builder own capacity preflight')
                request=prepare(args,out)
                if not args.build:
                    summary.update(test_status='prepared_only',model_build_status='not_run');rc=0
                else:
                    print('MODEL_BUILD_STARTED=YES\nMODEL=mobilenet_v3_large FAMILY=hailo8 ROLE=full',flush=True)
                    print('MODEL_BUILD_TIMEOUT_S='+str(args.timeout_s)+'\nPUBLICATION=private_only; force limited to this one diagnostic call',flush=True)
                    command=[sys.executable,'-I','-B',str(Path(__file__).resolve()),'--tool',str(args.tool),
                             '--_worker','--request',str(out/'request.json'),'--work',str(out)]
                    with ConsoleTail(out/'worker.log'):
                        process=supervised_run(command,cwd=out,log_path=out/'worker.log',timeout=args.timeout_s+90,grace=10)
                    write_json(out/'supervision.json',process)
                    if (out/'summary.json').is_file(): summary.update(read_json(out/'summary.json'))
                    if (out/'primary_error.json').is_file(): summary['primary_error']=read_json(out/'primary_error.json')
                    summary,rc=finish_status(summary,process)
                    validate_request(request)
                    summary['frozen_inputs_unchanged']=True
            except KeyboardInterrupt:
                summary.update(test_status='cancelled',model_build_status='cancelled');rc=130
            except Exception as exc:
                error={'type':type(exc).__name__,'error':str(exc)}
                write_json(out/'preflight_error.json',error)
                summary.update(test_status='failed',error=error);rc=2
            finally:
                after=configuration_state(Path.home(),args.tool)
                write_json(out/'configuration_after.json',after)
                preserved=before==after
                write_json(out/'configuration_preservation.json',{'checked_paths_unchanged':preserved})
                if not preserved:
                    summary.update(test_status='failed',configuration_changed_during_test=True);rc=2
                summary['checked_configuration_unchanged']=preserved
                write_json(out/'launcher_summary.json',summary)
                archive=export_evidence(out)
                print('\nHAILO8_MODEL_TEST_STATUS='+str(summary.get('test_status')),flush=True)
                print('MODEL_BUILD_STATUS='+str(summary.get('model_build_status')),flush=True)
                print('GPU_EXECUTION_STATUS='+str(summary.get('gpu_execution_status')),flush=True)
                if summary.get('error'): print('ERROR='+str(summary['error']),flush=True)
                print('RUNTIME_TEST=NOT_RUN\nMODEL_ACCEPTANCE=NOT_EVALUATED_BY_DIAGNOSTIC',flush=True)
                print('DIAGNOSTIC_ZIP='+str(archive)+'\nLOCAL_MODEL_OUTPUTS_KEPT='+str(out),flush=True)
    except Exception as exc:
        print(('MODEL_BUILD_STARTED=NO\n' if out is None else '')+'ERROR='+type(exc).__name__+': '+str(exc),flush=True)
        if out: print('RESULT_DIRECTORY_KEPT='+str(out),flush=True)
        return 2
    return rc


if __name__=='__main__':
    raise SystemExit(main())
