"""Unchanged observation logic from the delivered v2.80.2 model probe."""
from pathlib import Path
import os,shutil,subprocess,threading,time
from h8_model_request import write_json,file_identity,attributable_gpu_evidence

class GpuActivity:
    """Observe pmon samples only; this does not run any GPU kernel itself."""
    def __init__(self, directory):
        self.directory = Path(directory)
        self.proc = None
        self.thread = None
        self.samples = []
        self.status = 'not_available'

    def start(self):
        binary = shutil.which('nvidia-smi')
        if not binary:
            self.status = 'nvidia_smi_not_available'
            return
        try:
            self.proc = subprocess.Popen([binary, 'pmon', '-s', 'u', '-d', '1'],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        except OSError as exc:
            self.status = 'pmon_unavailable:' + str(exc)
            return
        self.status = 'collecting'
        self.thread = threading.Thread(target=self._read, daemon=True)
        self.thread.start()

    def _read(self):
        from deepx_full_workflow_smoke_worker_v27930 import _capture_owned
        tracked = {}
        columns = None
        try:
            with (self.directory / 'gpu_activity.log').open('w', encoding='utf-8') as log:
                for line in self.proc.stdout:
                    stamp = time.monotonic()
                    log.write(line)
                    log.flush()
                    words = line.strip().split()
                    if words[:2] == ['#', 'gpu'] and 'pid' in words and 'sm' in words:
                        columns = words[1:]
                        continue
                    if not columns or not words or words[0] == '#' or len(words) < len(columns):
                        continue
                    values = dict(zip(columns, words))
                    try:
                        pid, gpu, sm = int(values['pid']), int(values['gpu']), float(values['sm'])
                    except (KeyError, ValueError):
                        continue
                    owned = _capture_owned(os.getpid(), tracked)
                    # A fresh namespace-correct descendant snapshot excludes
                    # unrelated GUI/workstation activity and the sampler itself.
                    self.samples.append({'pid': pid, 'gpu_index': gpu,
                        'sm_utilization_percent': sm, 'observed_monotonic_s': stamp,
                        'interval_start_monotonic_s': stamp - 1.1,
                        'owned_compiler_descendant': pid in owned and pid != self.proc.pid,
                        'process_identity': tracked.get(pid)})
        except Exception as exc:
            self.status = 'pmon_collection_error:' + type(exc).__name__ + ':' + str(exc)

    def stop(self):
        if self.proc is not None:
            if self.proc.poll() is None:
                self.proc.terminate()
                try:
                    self.proc.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    self.proc.kill()
                    self.proc.wait(timeout=3)
            self.thread.join(timeout=3)
            if self.thread.is_alive():
                raise RuntimeError('diagnostic_gpu_sampler_did_not_stop')
            if self.status == 'collecting':
                self.status = 'collected' if self.samples else 'no_supported_process_samples'
        write_json(self.directory / 'gpu_activity.json', {'status': self.status, 'samples': self.samples})

def result_events(result):
    for area in ('details', 'calib_info'):
        events = (result.get(area) or {}).get('phase_events')
        if isinstance(events, list):
            return events
    return []

def summarize_result(result, request, work, samples):
    """A successful call is insufficient without completed actual phases."""
    events = result_events(result)
    completed = {r.get('phase') for r in events if r.get('event') == 'completed'}
    receipt = None
    hef = result.get('hef_path')
    error = None
    if hef and Path(hef).is_file():
        if not Path(hef).resolve().is_relative_to(Path(work).resolve()):
            raise ValueError('diagnostic_builder_returned_nonprivate_artifact')
        from onnx_splitpoint_tool.hailo_backend import _load_valid_hailo_receipt
        receipt = _load_valid_hailo_receipt(Path(hef), allow_diagnostic=True)
    recipe_match = False
    if receipt:
        expected = request['cpu_build_receipt']['cache_payload']
        actual = receipt['cache_payload']
        keys = ('model_sha256', 'optimization_level', 'calibration_identity',
                'prepared_calibration_identity_sha256', 'calibration_count',
                'requested_calibration_count', 'calibration_storage',
                'calibration_memory_cap_bytes', 'calibration_batch_size',
                'extra_model_script', 'start_nodes', 'end_nodes', 'integrity',
                'preprocessing_contract', 'preprocessing_contract_sha256',
                'net_name', 'net_input_shapes', 'disable_rt_metadata_extraction', 'hailo_sdk_version')
        differences = [k for k in keys if expected.get(k) != actual.get(k)]
        for key in ('compiler_onnx_sha256', 'source_onnx_sha256'):
            if receipt.get(key) != request['compiler_onnx']['sha256']:
                differences.append('private_' + key + '_not_exact_bound_compiler_graph')
        recipe_match = not differences
    else:
        differences = ['valid_private_receipt_missing']
    calibration = result.get('calib_info') or {}
    if calibration.get('source') != request['calibration_dir'] or calibration.get('used_count') != 500:
        differences.append('actual_calibration_not_bound_B500_images')
        recipe_match = False
    if result.get('skipped'):
        status = 'model_build_not_executed'
    elif result.get('ok') is True and receipt and {'translate', 'optimize', 'compile', 'publication'} <= completed:
        status = 'pass' if recipe_match else 'recipe_mismatch'
    else:
        status = 'failed' if result.get('ok') is not True else 'build_completion_unproven'
    context = (result.get('details') or {}).get('compiler_context') or (result.get('calib_info') or {}).get('compiler_context') or {}
    selected = context.get('gpu_index', context.get('physical_gpu_index'))
    if isinstance(selected, str) and selected.isdigit():
        selected = int(selected)
    gpu = attributable_gpu_evidence(samples, events, gpu_index=selected)
    if context.get('device', context.get('compute_effective')) != 'gpu':
        gpu['status'] = 'gpu_execution_unproven'
        gpu['reason'] = 'last_effective_compiler_context_not_GPU'
    hef_validation = (result.get('details') or {}).get('hef_validation') or calibration.get('hef_validation') or {}
    return {'schema': 'hailo_model_diagnostic_result_v27934',
        'model_build_status': status, 'gpu_execution_status': gpu['status'],
        'gpu_execution_evidence': gpu, 'compute_requested': 'gpu',
        'compute_effective': context.get('device', context.get('compute_effective', 'not_available')),
        'compiler_context': context, 'phase_events': events,
        'recipe_matches_cpu_baseline': recipe_match, 'recipe_differences': differences,
        'bound_original_source_onnx': request['source_onnx'],
        'bound_cpu_compiler_onnx': request['compiler_onnx'],
        'hef_receipt_status': 'validated' if receipt else 'not_available',
        'hef_readability_status': {'passed': 'pass'}.get(hef_validation.get('status'), hef_validation.get('status', 'not_run')),
        'hef_validation': hef_validation, 'runtime_status': 'not_run',
        'quality_status': 'not_evaluated', 'raw_energy_status': 'not_run',
        'claim_eligible': False, 'regular_path_released': False,
        'cache_reuse_proven': False, 'publication': 'private_only',
        'compiler_dispatch_count': 1 if 'translate' in completed else (0 if result.get('skipped') else None),
        'error': result.get('error'), 'failure_kind': result.get('failure_kind'),
        'last_stage': result.get('last_stage'), 'timed_out': result.get('timed_out', False),
        'private_hef': file_identity(hef) if receipt else None,
        'optimization_procedure_source': 'actual_compiler.log_unmodified',
        'optimization_procedure_equivalence': 'not_evaluated', 'speedup_claim': False}
