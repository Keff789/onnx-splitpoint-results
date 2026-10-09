#!/usr/bin/env python3
"""Verify the public projection's hashes and arithmetic with Python's stdlib.

Raw sensor traces, model artefacts and exact private report bytes remain external.
This check neither recreates measurements nor grants scientific eligibility.
"""
from pathlib import Path
import csv
import hashlib
import json
import math
import statistics
from decimal import Decimal

ROOT = Path(__file__).resolve().parent


def read(name):
    return json.loads((ROOT / name).read_text())


def close(a, b):
    assert math.isclose(float(a), float(b), rel_tol=1e-10, abs_tol=1e-10), (a, b)


def native_repeat_rate(row, rep):
    rate = 1000 / rep['makespan_s']
    if math.isclose(rep['fps'], rate, rel_tol=1e-10, abs_tol=1e-10):
        return
    # The verified H8 classification C++ writer prints FPS and milliseconds
    # to six decimals. Use the same exact print-cell check as the existing
    # portable verifier; retain strict arithmetic for every other path.
    assert (row['setup_id'] == 'H8' and row['backend'] == 'hailo8_to_trt'
            and row['task'] == 'classification'
            and row['observation']['technical_checks_passed'] is True)
    fps = Decimal(str(rep['fps']))
    ms = Decimal(str(rep['makespan_s'] * 1000)).quantize(Decimal('0.000001'))
    half = Decimal('0.0000005')
    assert fps.is_finite() and fps > 0 and ms > half and fps.as_tuple().exponent >= -6
    assert float(ms) / 1000 == rep['makespan_s']
    assert (fps-half)*(ms-half) <= 1000000 <= (fps+half)*(ms+half)


def main():
    manifest = read('PUBLICATION_MANIFEST.json')
    for entry in manifest['files']:
        path = ROOT / entry['path']
        assert path.resolve().is_relative_to(ROOT)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['public_sha256'], entry['path']
    native = read('current_results/native_current.json')['rows']
    generic = read('current_results/generic_current.json')['rows']
    assert len(native) == 246 and len(generic) == 204
    with (ROOT / 'FAIRNESS_MATRIX.csv').open() as matrix_file:
        matrix = list(csv.DictReader(matrix_file))
    assert len(matrix) == len(native) + len(generic) == 450
    assert len({r['case_uid'] for r in native}) == 246
    new = [r for r in native if r['status'] == 'new_measurement']
    reuse = [r for r in native if r['status'] == 'reused_verified']
    assert len(new) == manifest['native_new_performance_points']
    assert len(reuse) == manifest['native_verified_performance_reuse']
    assert sum(row['status'] == 'not_measured' for row in native) == manifest['native_performance_not_measured']
    assert sum(row['status'] == 'completed' for row in generic) == manifest['generic_measured_points']
    assert sum(row['status'] != 'completed' for row in generic) == manifest['generic_additional_points_not_measured']
    versions = manifest.get('source_versions') or {}
    if versions.get('canonical_cpu_reference_commit'):
        freeze = read('final_implementation_20261008/IMPLEMENTATION_FREEZE.json')
        reporting = read('REPORTING_SOURCE_SUPPLEMENT.json')['final_runtime_controller_changes']
        reference = read('operations/h8_classifier_domain_20261008/CONTROLLER_REFERENCE_FIX_20261008.json')
        assert versions['runtime_freeze_commit'] == freeze['base_commit']
        assert versions['runtime_file_count'] == len(freeze['runtime_files'])
        assert versions['canonical_cpu_reference_commit'] == reference['source_versioning']['commit']
        assert versions['controller_reporting_commit'] == reporting['controller_commit']['commit']
        assert versions['controller_guard_commit'] == reporting['controller_guard_commit']['commit']
    for rows, fields in ((native, {'native_normal_quality_points': 'normal_quality_eligible',
                                  'native_normal_claim_points': 'normal_claim_eligible'}),
                         (generic, {'generic_normal_quality_points': 'normal_quality_eligible',
                                    'generic_normal_claim_points': 'normal_claim_eligible',
                                    'generic_normal_energy_points': 'normal_energy_eligible'})):
        for published, current in fields.items():
            if published in manifest:
                assert sum(row.get(current) is True for row in rows) == manifest[published]
    resume = read('RESUME_STATE.json')
    if 'remaining' in resume:
        assert manifest['generic_current_points_require_final_bundle_confirmation'] == resume['remaining'].get('generic_current_points_to_confirm_after_final_duration_worker_change')
        if 'native_current_points_require_bounded_source_confirmation' in manifest:
            assert manifest['native_current_points_require_bounded_source_confirmation'] == resume['remaining'].get('native_existing_points_requiring_bounded_normal_source_admission_confirmation')
    for row in new:
        reps = row['observation']['repeats']
        assert len(reps) == len({r['runner_pid'] for r in reps}) == 3
        assert len({r['runner_start_monotonic_ns'] for r in reps}) == 3
        for rep in reps:
            assert rep['completed_tasks'] == 1000 and rep['warmup_tasks'] == 100
            native_repeat_rate(row, rep)
        close(row['fps'], statistics.median(r['fps'] for r in reps))
    for row in reuse:
        assert row['fps'] > 0 and not row['fps_samples'] and not row['observation']['repeats']
        assert row['observation']['fps_median'] is None
        if row.get('normal_quality_eligible') is True:
            assert row['normal_claim_eligible'] is False
            assert row['quality_provenance']['performance_observation_count'] == 1
            assert row['quality_provenance']['new_performance_observations'] == 0
    generic_repeats = read('current_results/generic_repeats.json')['rows']
    for row in generic:
        if row['status'] != 'completed':
            assert row['fps_median'] is None and not row['fps_samples']
            continue
        reps = [r for r in generic_repeats if r['case_key'] == row['case_key']]
        assert len(reps) == len({(r['boot_id'], r['pid'], r['process_start_ticks']) for r in reps}) == 3
        for rep in reps:
            assert rep['completed_count'] == 1000 and rep['warmup_count'] == 100
            close(rep['fps'], 1000 / rep['makespan_s'])
        close(row['fps_median'], statistics.median(r['fps'] for r in reps))
    acquisitions = read('current_results/energy_acquisitions.json')['rows']
    for row in acquisitions:
        reps = row['repeats']
        assert len(reps) == 3 and all(r['source_completion_verified'] for r in reps)
        for rep in reps:
            assert rep['requested_workload_s'] == 60 and rep['completed_tasks'] > 0 and rep['energy_j'] > 0
            close(rep['joules_per_task'], rep['energy_j'] / rep['completed_tasks'])
            close(rep['tasks_per_joule'], rep['completed_tasks'] / rep['energy_j'])
        values = [r['joules_per_task'] for r in reps]
        mean = statistics.mean(values)
        half = 4.302652729749461 * statistics.stdev(values) / math.sqrt(3)
        stats = row['repeat_statistics']['energy_per_work_unit_j']
        close(stats['mean'], mean)
        close(stats['ci_low'], mean - half)
        close(stats['ci_high'], mean + half)
    energies = [r for r in native if r.get('normal_energy_eligible')]
    assert len(energies) == manifest['normal_current_energy_points']
    for row in energies:
        proof = row['energy_provenance']
        assert proof['normal_report_verified'] is True
        assert proof['performance_summary_sha256'] == row['observation']['summary_sha256']
        close(row['energy_per_task_j'], statistics.mean(r['joules_per_task'] for r in row['energy_repeats']))
        close(row['tasks_per_j'], statistics.mean(r['tasks_per_joule'] for r in row['energy_repeats']))
        close(row['energy_comparison_per_task_j'], statistics.mean(r['joules_per_task'] for r in row['energy_comparison_repeats']))
        close(row['energy_comparison_tasks_per_j'], statistics.mean(r['tasks_per_joule'] for r in row['energy_comparison_repeats']))
    for row in native:
        if not row.get('normal_energy_eligible'):
            assert row['energy_per_task_j'] is None and row['tasks_per_j'] is None
    generic_energies = [r for r in generic if r.get('normal_energy_eligible') is True]
    for row in generic_energies:
        proof = row['energy_provenance']
        assert proof['normal_report_verified'] is True and proof['parent_cleanup_proven'] is True
        assert proof['performance_result_sha256'] == row['raw_result_sha256']
        reps = row['energy_repeats']
        assert len(reps) == 3
        for rep in reps:
            assert rep['completed_tasks'] > 0 and rep['energy_j'] > 0
            close(rep['energy_per_completed_task_j'], rep['energy_j'] / rep['completed_tasks'])
            close(rep['completed_tasks_per_j'], rep['completed_tasks'] / rep['energy_j'])
        close(row['energy_per_task_j'], statistics.mean(r['energy_per_completed_task_j'] for r in reps))
        close(row['tasks_per_j'], statistics.mean(r['completed_tasks_per_j'] for r in reps))
        assert not row.get('energy_efficiency_claim_eligible') or row.get('normal_claim_eligible') is True
    print(json.dumps({'status': 'PASS', 'verified_public_files': len(manifest['files']),
                      'native_new': len(new), 'native_reused': len(reuse),
                      'generic_process_repeats': len(generic_repeats),
                      'sensor_acquisitions': len(acquisitions), 'normal_energy_points': len(energies),
                      'generic_normal_energy_points': len(generic_energies),
                      'raw_sensor_or_model_verification': False, 'task_complete': False}))


if __name__ == '__main__':
    main()
