#!/usr/bin/env python3
"""Verify the public projection's hashes and arithmetic with Python's stdlib.

Raw sensor traces, model artefacts and exact private report bytes remain external.
This check neither recreates measurements nor grants scientific eligibility.
"""
from pathlib import Path
import hashlib
import json
import math
import statistics

ROOT = Path(__file__).resolve().parent


def read(name):
    return json.loads((ROOT / name).read_text())


def close(a, b):
    assert math.isclose(float(a), float(b), rel_tol=1e-10, abs_tol=1e-10), (a, b)


def main():
    manifest = read('PUBLICATION_MANIFEST.json')
    for entry in manifest['files']:
        path = ROOT / entry['path']
        assert path.resolve().is_relative_to(ROOT)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['public_sha256'], entry['path']
    native = read('current_results/native_current.json')['rows']
    generic = read('current_results/generic_current.json')['rows']
    assert len(native) == 246 and len(generic) == 204
    assert len({r['case_uid'] for r in native}) == 246
    new = [r for r in native if r['status'] == 'new_measurement']
    reuse = [r for r in native if r['status'] == 'reused_verified']
    assert len(new) == manifest['native_new_performance_points'] == 15
    assert len(reuse) == manifest['native_verified_performance_reuse'] == 9
    for row in new:
        reps = row['observation']['repeats']
        assert len(reps) == len({r['runner_pid'] for r in reps}) == 3
        assert len({r['runner_start_monotonic_ns'] for r in reps}) == 3
        for rep in reps:
            assert rep['completed_tasks'] == 1000 and rep['warmup_tasks'] == 100
            close(rep['fps'], 1000 / rep['makespan_s'])
        close(row['fps'], statistics.median(r['fps'] for r in reps))
    for row in reuse:
        assert row['fps'] > 0 and not row['fps_samples'] and not row['observation']['repeats']
        assert row['observation']['fps_median'] is None
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
    assert len(energies) == manifest['normal_current_energy_points'] == 3
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
    print(json.dumps({'status': 'PASS', 'verified_public_files': len(manifest['files']),
                      'native_new': len(new), 'native_reused': len(reuse),
                      'generic_process_repeats': len(generic_repeats),
                      'sensor_acquisitions': len(acquisitions), 'normal_energy_points': len(energies),
                      'raw_sensor_or_model_verification': False, 'task_complete': False}))


if __name__ == '__main__':
    main()
