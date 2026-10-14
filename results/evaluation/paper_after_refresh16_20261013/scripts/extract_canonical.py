#!/usr/bin/env python3
"""Project the selected CURRENT snapshot and existing quality evidence, offline.

Extends the Revision-3 extractor's readers and exact identity joins. It never
executes measurement, inference, dataset evaluation, or an archived command.
"""
import argparse
import collections
import hashlib
import json
import math
import shutil
from pathlib import Path

SETUP = {'orin_nx_deepx_m1_01': 'DeepX', 'orin_nx_hailo8_01': 'H8', 'orin_nx_hailo10_01': 'H10'}
FILES = ['cases.json', 'energy_repeats.json', 'pipeline_repeats.json',
         'native_generic_bindings.json', 'split_full_contracts.json',
         'refresh16_provenance.json', 'refresh16_observation_delta.json',
         'cohort_actions.json', 'cohort_axis_actions.json', 'historical_scope.json',
         'provenance_limits.json']

def read(p):
    return json.loads(p.read_text())

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write(p, v):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(v, indent=2, sort_keys=True, allow_nan=False) + '\n')

def key(r):
    return (r.get('model_id', r.get('model')), SETUP.get(r.get('setup_id'), r.get('setup_id')),
            r.get('backend', r.get('direction')), r.get('case_id', r.get('case')))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--base', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    b, out = a.base.resolve(), a.output
    assert not out.exists() or not any(out.iterdir()), 'Use a fresh output directory'
    cur = read(b/'CURRENT.json')
    assert cur['generation'] == 'refresh16_20261013', 'This dated paper package requires the Refresh16 generation'
    src = b/cur['selected_inputs']
    manifest = read(src/'MANIFEST.json')
    assert sha(src/'MANIFEST.json') == cur['selected_input_manifest_sha256']
    out.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        assert sha(src/name) == manifest[name], name
        shutil.copyfile(src/name, out/name)
    # The prior snapshot is used only for preservation checks, never selection.
    baseline = b/cur['historical_analysis']/'inputs/cases.json'
    shutil.copyfile(baseline, out/'baseline_cases.json')
    write(out/'source_manifest.json', manifest)
    supplement = b/cur['immutable_supplement']
    entries = read(supplement/'ENTRYPOINTS.json')
    receipt = read(supplement/'COPY_RECEIPT.json')
    byhash = {e['sha256']: e['destination'] for e in receipt['files']}
    for e in read(supplement/'RESOLVER.json')['entries']:
        if e.get('canonical_path') and e.get('sha256'):
            byhash.setdefault(e['sha256'], e['canonical_path'])
    cache = {}
    def bound(h):
        if h not in byhash:
            return None
        if h not in cache:
            p = b/byhash[h]
            assert p.resolve().is_relative_to(b)
            assert sha(p) == h, byhash[h]
            cache[h] = read(p)
        return cache[h]
    def get(name):
        es = [e for e in entries if e['source'].endswith('/'+name)]
        assert len(es) == 1, name
        e = es[0]
        p = b/e['canonical_path']
        assert sha(p) == e['sha256']
        return read(p)['rows'], e
    native, ne = get('current_results/native_current.json')
    generic, ge = get('current_results/generic_current.json')
    original = {'native': {key(r): r for r in native}, 'generic': {key(r): r for r in generic}}
    evidence = []
    cases = read(src/'cases.json')
    refreshed = {key(r['identity']): r for r in read(src/'refresh16_observation_delta.json')['rows']}
    fresh_raw = {}
    for rep in read(src/'pipeline_repeats.json'):
        if rep.get('raw_source') and rep['uid'] not in fresh_raw:
            ref = rep['raw_source']
            path = b/ref['canonical_path']
            assert sha(path) == ref['sha256']
            raw = read(path)
            fresh_raw[rep['uid']] = raw[0] if isinstance(raw, list) else raw
    for c in cases:
        r = original[c['runner']][key(c)]
        q = r.get('quality_provenance') or {}
        ep = r.get('energy_provenance') or {}
        ob = r.get('observation') or {}
        gq = r.get('generic_quality_transfer') or {}
        own = r.get('own_dataset_quality_evidence') or gq.get('own_dataset_quality_evidence') or gq.get('generic_dataset_quality_evidence') or {}
        qh = q.get('quality_summary_sha256') if c['runner'] == 'native' else own.get('result_sha256', own.get('central_result_sha256'))
        v = bound(qh)
        source_result_hash = qh
        summary_selected = False
        historical_transfer = False
        if v is None and not own and gq.get('eligible_for_quality_transfer'):
            # Preserve the already selected cross-runner quality transfer.
            # Its current Native evidence is explicit, and its numerical
            # assessment must match exactly; no new transfer is inferred.
            qh = r.get('native_quality_provenance', {}).get('quality_summary_sha256')
            v = bound(qh)
            assert v is not None, (c['uid'], 'selected transfer evidence unavailable')
            matches = [x for x in v['rows'] if key(x) == key(c)]
            assert len(matches) == 1, (c['uid'], 'selected transfer identity')
            pvalue = matches[0]['accuracy_gate_metrics']
            expected = gq.get('generic_accuracy_assessment')
            if isinstance(expected, str):
                expected = json.loads(expected)
            observed_loss = (pvalue['reference']-pvalue['candidate'])/pvalue['reference']
            assert math.isclose(observed_loss, expected['relative_loss'], rel_tol=1e-10, abs_tol=1e-12)
            historical_transfer = True
        if v is None and own.get('central_summary_sha256'):
            qh = own['central_summary_sha256']
            summary = bound(qh)
            assert summary is not None, (c['uid'], 'selected central summary unavailable')
            matches = [x for x in summary['results'] if (x.get('source_request_sha256') or '').removeprefix('sha256:') == own['source_request_sha256'] and x.get('model_id') == c['model_id'] and x.get('case_id') == c['case_id'] and x.get('variant') == 'composed']
            assert len(matches) == 1, (c['uid'], 'selected quality request', len(matches))
            v = matches[0]
            summary_selected = True
        qrow = None
        qfield = None
        if v is not None and 'rows' in v:
            matches = [x for x in v['rows'] if key(x) == key(c)]
            assert len(matches) == 1, (c['uid'], len(matches))
            qrow = matches[0]
            prim = qrow.get('accuracy_gate_metrics') or {}
            metric = qrow.get('accuracy_gate_metric')
            qfield = 'rows[identity].accuracy_gate_metrics' + ('; existing explicitly eligible Generic quality transfer, numerical assessment matched' if historical_transfer else '')
        elif v is not None and 'primary' in v:
            qrow = v
            prim = v['primary']
            metric = prim.get('metric')
            qfield = ('results[model, source_setup, source_run, case, composed].primary; exact stored transfer assessment matched' if historical_transfer else
                      'results[source_request_sha256, identity, composed].primary' if summary_selected else 'primary')
        else:
            # Generic transfer records may embed the selected dataset gate.
            gate = gq.get('task_quality_gate') or gq.get('generic_task_quality_gate') or {}
            prim = gate.get('primary', {})
            metric = prim.get('metric')
        value, reference = prim.get('candidate'), prim.get('reference')
        n = prim.get('n', own.get('record_count'))
        numeric_loss = (reference-value)/reference if value is not None and reference else None
        loss_disagrees = numeric_loss is not None and c['quality_relative_loss'] is not None and not math.isclose(numeric_loss, c['quality_relative_loss'], rel_tol=1e-8, abs_tol=1e-12)
        perf_source = c.get('refresh16', {}).get('performance_summary', {}).get('canonical_path') or byhash.get(c['performance_source_sha256']) or ob.get('summary') or r.get('current_result_path')
        energy_hash = c.get('refresh16', {}).get('energy_source', {}).get('sha256') or ep.get('normal_source_report_sha256') or ep.get('normal_report_sha256')
        energy_source = c.get('refresh16', {}).get('energy_source', {}).get('canonical_path') or byhash.get(energy_hash) or ep.get('normal_source_report')
        runtime = c['backend']
        timing = ob.get('timing_input_binding') or r.get('input_binding') or {}
        notes = []
        completion = c.get('completion_mode') or r.get('completed_stage')
        if c.get('refresh16'):
            fresh = refreshed[key(c)]
            modes = sorted({t['completion_mode'] for t in fresh['performance']['repeats'] if t.get('completion_mode')})
            if modes:
                completion = ' / '.join(modes)
                notes.append('Refresh16 measured completion mode=' + completion)
            raw = fresh_raw[c['uid']]
            for f in ['completed_task_completion_mode', 'latency_semantics', 'postprocess_runtime_mode', 'postprocess_location', 'postprocess_included', 'producer_impl']:
                if raw.get(f) not in (None, ''):
                    notes.append('Refresh16 raw ' + f + '=' + str(raw[f]))
        if completion and 'fast_oracle_outside_timing' in completion:
            notes.append('fast_oracle_outside_timing: correctness oracle outside the timed loop; not dense decode/NMS per image')
        if c['task'] == 'detection' and completion is None:
            notes.append('completion implementation not recorded in compact selection; endpoint equivalence is not inferred')
        if qrow and not c.get('refresh16'):
            for f in ['postprocess_runtime_mode', 'completed_task_completion_mode', 'postprocess_location', 'host_postprocess_required', 'postprocess_included', 'producer_impl']:
                if qrow.get(f) not in (None, ''):
                    notes.append(f + '=' + str(qrow[f]))
        def clean_path(v):
            if not isinstance(v, str):
                return v
            for prefix in ['/home/kmika/Reports/native-fairness-rev3-20261007/', '/homes/kmika/diss_results/']:
                v = v.removeprefix(prefix)
            return v
        evidence.append({'uid': c['uid'], 'quality_value': value,
            'quality_reference_value': reference, 'quality_metric': metric,
            'quality_n': n, 'quality_source': byhash.get(qh), 'quality_evidence_sha256': qh,
            'quality_bound_result_sha256': source_result_hash,
            'quality_source_request_sha256': own.get('source_request_sha256'),
            'quality_primary_observation': {k: prim[k] for k in ['candidate','reference','n','delta','candidate_hits','reference_hits','ci_low','ci_high','metric'] if k in prim},
            'quality_original_field': qfield, 'quality_numeric_relative_loss': numeric_loss,
            'quality_cached_loss_disagrees': loss_disagrees,
            'quality_binding_note': 'Selected summary numerical metric retained; cached Current loss differs; both exposed without changing Current.' if loss_disagrees else None,
            'quality_result_class': (qrow or {}).get('accuracy_class', (qrow or {}).get('accuracy_assessment', {}).get('accuracy_class')),
            'quality_relative_loss_ci': (qrow or {}).get('accuracy_relative_loss_ci', (qrow or {}).get('accuracy_assessment', {}).get('relative_loss_ci')),
            'quality_remeasured_in_refresh16': False,
            'quality_observation_status': r.get('quality_provenance_status', r.get('generic_quality_transfer_status')),
            'performance_source': clean_path(perf_source), 'performance_original_field': 'fps_samples / fps_median' if c['fps_samples'] else 'fps (historical single)',
            'performance_generation': 'refresh16_20261013' if c.get('refresh16') else ('historical_single_reused' if c['performance_observations']==1 else 'rev3_consolidated_20261013'),
            'energy_source': clean_path(energy_source), 'energy_source_sha256': energy_hash,
            'energy_original_field': 'energy_repeats[].energy_j / completed_tasks',
            'energy_generation': 'refresh16_20261013' if c.get('refresh16') else 'rev3_consolidated_20261013',
            'quality_generation': 'pre_refresh16_selected_evidence_reused',
            'runtime': runtime, 'timing_input': {k: timing.get(k) for k in ['sequence','preprocessing_timed','preprocessing_contract','geometry'] if k in timing},
            'measured_completion_mode': completion,
            'execution_notes': notes,
            'original_current_source': ne['canonical_path'] if c['runner']=='native' else ge['canonical_path'],
            'original_current_sha256': ne['sha256'] if c['runner']=='native' else ge['sha256']})
    write(out/'selected_evidence.json', evidence)
    write(out/'source_binding.json', {'generation': cur['generation'], 'selected_inputs': cur['selected_inputs'],
        'selected_input_manifest_sha256': cur['selected_input_manifest_sha256'],
        'baseline_cases_sha256': sha(baseline), 'projection': 'CURRENT-selected exact compact observations plus existing selected quality summaries',
        'quality_numeric_coverage': sum(e['quality_value'] is not None for e in evidence),
        'quality_cached_loss_disagreements': sum(e['quality_cached_loss_disagrees'] for e in evidence),
        'quality_evaluations_started': 0, 'measurement_starts': 0})
    write(out/'MANIFEST.json', {p.name: sha(p) for p in sorted(out.glob('*.json')) if p.name != 'MANIFEST.json'})
    print(json.dumps(read(out/'source_binding.json'), sort_keys=True))

if __name__ == '__main__':
    main()
