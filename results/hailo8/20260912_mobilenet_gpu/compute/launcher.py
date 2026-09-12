#!/usr/bin/env python3
"""Hailo8-only CUDA supplement + existing product compute test. No Tool patch.

Default: metadata-only plan. --prepare-and-test: show exact packages, ask for
consent, download ONLY missing pinned NVIDIA CUDA-12 wheels, stage with the
installed product planner, run the installed product compute collector. No
pip install, no frameworks replaced, no HEF build, no registry/cache changes.
"""
from __future__ import annotations
import argparse
import contextlib
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from types import SimpleNamespace
import zipfile

sys.dont_write_bytecode = True
TOKEN = 'HAILO8 GPU TEST'
LIBRARY_MANIFEST = 'ONNX_SPLITPOINT_HAILO8_DEPENDENCY_MANIFEST'


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)+'\n', encoding='utf-8')


def sha(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()


def checked_plan(plan: dict) -> dict:
    if plan.get('status') == 'BLOCKED':
        raise RuntimeError('dependency_plan_blocked: '+json.dumps(plan.get('conflicts', []),ensure_ascii=False))
    return plan


def choose_missing(proposals: list[dict]) -> list[str]:
    """Do not shadow an existing package. Fail before downloading on mismatch."""
    selected=[]
    for p in proposals:
        name, version = p['name'], p['version']
        if not re.fullmatch(r'nvidia-[a-z0-9-]+-cu12',name) or not re.fullmatch(r'[0-9]+(?:\.[0-9]+)+',version):
            raise ValueError('unexpected_cuda_package: '+str(p))
        if p.get('installed_version') is not None:
            if p['installed_version'] != version:
                raise RuntimeError(f'existing_package_version_conflict:{name}:installed={p["installed_version"]},requested={version}')
        else: selected.append(name)
    if not proposals: raise RuntimeError('no_explicit_tensorflow_cuda_requirements')
    return sorted(selected)


def pip_download_command(python: str, destination: Path, requirements: list[str]) -> list[str]:
    if not requirements or any(not re.fullmatch(r'nvidia-[a-z0-9-]+-cu12==[0-9]+(?:\.[0-9]+)+',r) for r in requirements):
        raise ValueError('download_requires_exact_cuda12_pins')
    return [python,'-I','-B','-m','pip','--isolated','--disable-pip-version-check','--no-cache-dir',
            'download','--no-deps','--only-binary=:all:','--index-url','https://pypi.org/simple',
            '--retries','2','--timeout','30','--dest',str(destination),*requirements]


def load_product(tool: Path):
    tool=tool.expanduser().resolve(strict=True)
    py=tool/'.venv/bin/python'
    if not py.is_file(): raise RuntimeError('tool_venv_missing:'+str(py))
    # Expected target interpreter: prevent running pip with another env's tags.
    if Path(sys.prefix).resolve() != (tool/'.venv').resolve():
        raise RuntimeError('run_with_tool_venv_python:'+str(py))
    sys.path.insert(0,str(tool))
    import onnx_splitpoint_tool as package
    if Path(package.__file__).resolve().parent != tool/'onnx_splitpoint_tool':
        raise RuntimeError('unexpected_tool_import_source')
    from onnx_splitpoint_tool import hailo_dependency_plan as hp
    cf=tool/'scripts/hailo_gpu_diagnostics/collect.py'
    spec=importlib.util.spec_from_file_location('hailo8_product_compute_collector',cf)
    if spec is None or spec.loader is None: raise RuntimeError('collector_unavailable')
    collector=importlib.util.module_from_spec(spec);spec.loader.exec_module(collector)
    return hp,collector,package


@contextlib.contextmanager
def compute_environment(manifest: Path | None):
    keys=[LIBRARY_MANIFEST,'TF_NUM_INTEROP_THREADS','TF_NUM_INTRAOP_THREADS','TF_FORCE_GPU_ALLOW_GROWTH']
    prior={k:os.environ.get(k) for k in keys}
    try:
        if manifest is not None: os.environ[LIBRARY_MANIFEST]=str(manifest)
        else: os.environ.pop(LIBRARY_MANIFEST,None)
        os.environ['TF_NUM_INTEROP_THREADS']='2'
        os.environ['TF_NUM_INTRAOP_THREADS']='2'
        os.environ['TF_FORCE_GPU_ALLOW_GROWTH']='true'
        yield
    finally:
        for k,v in prior.items():
            if v is None: os.environ.pop(k,None)
            else: os.environ[k]=v


def make_evidence(work: Path) -> Path:
    target=work.with_suffix('.zip')
    partial=target.with_suffix('.zip.partial')
    if target.exists() or partial.exists(): raise RuntimeError('archive_target_already_exists')
    with zipfile.ZipFile(partial,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(work.iterdir()):
            if p.is_file() and not p.is_symlink() and p.suffix in {'.json','.txt','.log','.py','.md'}:
                z.write(p,p.name)
        # Flatten the ORIGINAL collector's curated evidence, never crawl caches.
        for a in sorted((work/'compute').glob('*.zip')):
            with zipfile.ZipFile(a) as q:
                for item in q.infolist():
                    rel=Path(item.filename)
                    if item.is_dir(): continue
                    if rel.is_absolute() or '..' in rel.parts or rel.suffix not in {'.json','.jsonl','.log','.txt','.py','.sh','.md'}:
                        raise RuntimeError('unexpected_compute_evidence_member:'+item.filename)
                    z.writestr('compute/'+a.stem+'/'+item.filename,q.read(item))
        p=work/'download/console.log'
        if p.is_file() and not p.is_symlink():z.write(p,'download/console.log')
    with zipfile.ZipFile(partial) as z:
        if z.testzip() is not None:raise RuntimeError('evidence_crc_failed')
    # Unique run directory owns the name. No source is overwritten.
    os.link(partial,target);partial.unlink()
    return target


def execute(args, hp, collector, package_version: str, *, ask=input) -> int:
    h8=args.hailo8_venv.expanduser().absolute(); vendor_python=h8/'bin/python'
    out=args.output_parent.expanduser().absolute();out.mkdir(parents=True,exist_ok=True)
    # Fail visibly before expensive preparation; collector reacquires this same
    # lock immediately before its real GPU process. Never delete the lock file.
    with collector.interlock(collector.platform_interlock_path()): pass
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    work=Path(tempfile.mkdtemp(prefix='hailo8_gpu_test_'+stamp+'_',dir=out))
    target=h8.parent/('hailo8_cuda_'+work.name.removeprefix('hailo8_gpu_test_'))
    summary={'schema':'hailo8-private-gpu-test-v1','status':'running','tool_version':package_version,
             'family':'hailo8','model_build':'NOT_RUN','model_acceptance':'NOT_EVALUATED',
             'tool_source_patched':False,'vendor_packages_installed_or_replaced':False,
             'registry_modified':False,'production_model_cache_modified':False,
             'private_overlay':None,'network_requested':False,'compute_requested':False}
    rc=2
    print('TEST_DIRECTORY='+str(work),flush=True)
    Path(work/'launcher.py').write_bytes(Path(__file__).read_bytes())
    try:
        with collector.interlock(collector.platform_interlock_path()):
            inv=hp.collect_inventory(vendor_python)
            write_json(work/'inventory_before.json',inv)
            base=checked_plan(hp.build_plan(inv,target))
            write_json(work/'dependency_proposals.json',base)
            selected=choose_missing(base['proposals'])
            pins={p['name']:p['version'] for p in base['proposals']}
            print('HAILO8_PACKAGES_MISSING='+str(len(selected)),flush=True)
            for name in selected:print('  '+name+'=='+pins[name],flush=True)
            if args.overlay_manifest:
                manifest=args.overlay_manifest.expanduser().absolute()
                hp.validated_overlay_components(family='hailo8',selected_python=vendor_python,manifest_path=manifest)
                summary['private_overlay']=str(manifest)
                # An explicit existing overlay is not shadowed by a new one.
                selected=[]
            else:manifest=None
            preliminary=checked_plan(hp.build_plan(inv,target,packages=selected))
            write_json(work/'dependency_selection.json',preliminary)
            if not args.prepare_and_test:
                summary['status']='plan_only';rc=0
                return rc
            print('\nNur Hailo8: private CUDA-Ergaenzung und anschliessend GPU/XLA-Test.\n'
                  'Kein HEF-Build, kein pip install, keine Aenderung an Hailo10/DeepX/Profilen.\n'
                  'Pakete werden nur bei Bedarf in einen NEUEN separaten Ordner entpackt.',flush=True)
            print('PRIVATE_TARGET='+str(manifest.parent if manifest else target),flush=True)
            if selected and not args.wheel_dir:
                print('Download von PyPI erforderlich; bei bisherigem Bestand groessenordnung GB.\n'
                      'Der Download hat insgesamt hoechstens 30 Minuten Zeit.',flush=True)
            if ask('Zum Fortfahren exakt '+TOKEN+' eingeben: ').strip()!=TOKEN:
                summary['status']='not_authorized';rc=3;return rc
            if selected:
                # Deliberately generous space reserve; do not alter existing caches.
                for parent in {out, h8.parent}:
                    if shutil.disk_usage(parent).free < 8*1024**3:
                        raise RuntimeError('at_least_8_GiB_free_required:'+str(parent))
                if args.wheel_dir:
                    wheel_paths=sorted(args.wheel_dir.expanduser().absolute().glob('*.whl'))
                    if not wheel_paths:raise RuntimeError('local_wheel_directory_empty')
                else:
                    wheels=work/'wheels';wheels.mkdir()
                    dl=work/'download';dl.mkdir()
                    requirements=[n+'=='+pins[n] for n in selected]
                    command=pip_download_command(sys.executable,wheels,requirements)
                    write_json(work/'download_command.json',{'argv':command,'operation':'download_only'})
                    summary['network_requested']=True
                    env=dict(os.environ)
                    env['PYTHONDONTWRITEBYTECODE']='1';env['PIP_CONFIG_FILE']=os.devnull
                    env['TMPDIR']=str(dl)
                    proc=collector.run_command(command,dl,env,1800)
                    write_json(work/'download_process.json',proc)
                    if proc.get('returncode')!=0 or proc.get('timed_out') or not proc.get('cleanup_complete'):
                        raise RuntimeError('wheel_download_failed_see_download_console')
                    wheel_paths=sorted(wheels.glob('*.whl'))
                plan=checked_plan(hp.build_plan(inv,target,packages=selected,wheels=wheel_paths))
                pf=work/'reviewed_stage_plan.json';write_json(pf,plan)
                if plan['status']!='READY_FOR_EXPLICIT_OFFLINE_STAGE':
                    raise RuntimeError('private_overlay_plan_not_ready:'+plan['status'])
                total=0
                for wheel in wheel_paths:
                    with zipfile.ZipFile(wheel) as archive:total+=sum(i.file_size for i in archive.infolist())
                if shutil.disk_usage(h8.parent).free < total+1024**3:raise RuntimeError('overlay_uncompressed_space_insufficient')
                print('PRIVATE_STAGE_START: exakt gepruefte NVIDIA-Wheels; kein Paketresolver',flush=True)
                manifest=hp.stage_reviewed_plan(plan,expected_plan_sha256=sha(pf),plan_file=pf)
                hp.validated_overlay_components(family='hailo8',selected_python=vendor_python,manifest_path=manifest)
                summary['private_overlay']=str(manifest)
                write_json(work/'overlay_manifest.json',json.loads(manifest.read_text()))
            if hp.collect_inventory(vendor_python)!=inv:raise RuntimeError('vendor_metadata_changed_before_compute')
        # The product collector itself owns/rechecks the interlock and timeout.
        print('COMPUTE_ONLY=HAILO8; keine Wiederholung des Hailo10-Tests',flush=True)
        summary['compute_requested']=True
        compute_args=SimpleNamespace(families=['hailo8'],venv_hailo8=h8,
            venv_hailo10=h8.parent/'venv_hailo10',gpu=args.gpu,timeout=180,
            compiler_context=True,output_parent=work/'compute')
        with compute_environment(manifest):
            rc=int(collector.collect(compute_args))
        after=hp.collect_inventory(vendor_python);write_json(work/'inventory_after.json',after)
        summary['vendor_metadata_unchanged']=after==inv
        if after!=inv:raise RuntimeError('vendor_metadata_changed_during_compute')
        summary['status']='compute_pass' if rc==0 else 'compute_not_passed'
        return rc
    except KeyboardInterrupt:
        summary.update(status='cancelled',error='KeyboardInterrupt');rc=130;return rc
    except Exception as exc:
        summary.update(status='failed',error=type(exc).__name__+': '+str(exc))
        print('HAILO8_TEST_ERROR='+summary['error'],flush=True);rc=2;return rc
    finally:
        summary['returncode']=rc;write_json(work/'summary.json',summary)
        try:
            a=make_evidence(work)
            print('HAILO8_TEST_STATUS='+summary['status']+'\nMODEL_BUILD=NOT_RUN\nDIAGNOSTIC_ZIP='+str(a),flush=True)
        except Exception as exc:
            summary.update(status='evidence_archive_failed',evidence_error=repr(exc),returncode=2)
            write_json(work/'summary.json',summary)
            print('EVIDENCE_ARCHIVE_FAILED='+repr(exc)+'\nRESULT_DIRECTORY='+str(work),flush=True)
            raise RuntimeError('evidence_archive_failed:'+str(work)) from exc
        if 'manifest' in locals() and manifest is not None:
            print('PRIVATE_OVERLAY_KEPT='+str(manifest)+'\nNORMAL_GUI_CONFIGURATION_UNCHANGED=YES',flush=True)


def main(argv=None) -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--tool',type=Path,default=Path(os.environ.get('ONNX_SPLITPOINT_TOOL_DIR',str(Path.home()/'ONNX-Splitpoint-Tool'))))
    p.add_argument('--hailo8-venv',type=Path,default=Path.home()/'.onnx_splitpoint_tool/hailo/venv_hailo8')
    p.add_argument('--output-parent',type=Path,default=Path.home()/'Downloads')
    p.add_argument('--prepare-and-test',action='store_true')
    p.add_argument('--wheel-dir',type=Path,help='Optional already downloaded exact selected wheels; no network')
    p.add_argument('--overlay-manifest',type=Path,help='Explicit existing Hailo8 private overlay; no automatic discovery')
    p.add_argument('--gpu',default='0')
    a=p.parse_args(argv)
    if not re.fullmatch(r'[0-9]+|GPU-[A-Za-z0-9-]+',a.gpu):p.error('one GPU index or UUID required')
    if a.wheel_dir and a.overlay_manifest:p.error('--wheel-dir and --overlay-manifest are mutually exclusive')
    try:
        hp,col,pkg=load_product(a.tool)
        return execute(a,hp,col,str(getattr(pkg,'__version__','unknown')))
    except Exception as exc:
        if type(exc).__name__=='BusyError':
            print('SMOKE_STARTED=NO\nREASON=workflow_or_platform_operation_active\nGUI/Messung zuerst geordnet beenden; Lockdatei NICHT loeschen.')
            return 3
        print('SMOKE_STARTED=NO\nERROR='+type(exc).__name__+': '+str(exc));return 2


if __name__=='__main__':raise SystemExit(main())
