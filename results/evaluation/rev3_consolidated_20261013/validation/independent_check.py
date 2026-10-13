#!/usr/bin/env python3
"""Independent stdlib review; does not import the production analysis code."""
import argparse
import collections
import csv
import hashlib
import json
import math
import statistics
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', '--publication-root', dest='publication_root', type=Path, required=True,
                    help='Package directory containing inputs/, results/, METHODS.md and scripts/')
    ap.add_argument('--output', type=Path, default=Path(__file__).resolve().parent / 'INDEPENDENT_CHECKS.json')
    args = ap.parse_args()
    root = args.publication_root
    hashes = {}
    checks = collections.Counter()

    def read(relative):
        data = (root / relative).read_bytes()
        hashes[relative] = hashlib.sha256(data).hexdigest()
        if relative.endswith('.csv'):
            return list(csv.DictReader(data.decode().splitlines()))
        return json.loads(data)

    def equal(actual, expected, label):
        if expected is None:
            assert actual in (None, ''), (label, actual, expected)
        elif isinstance(expected, bool):
            assert actual == expected or actual == str(expected), (label, actual, expected)
        elif isinstance(expected, (float, int)):
            assert actual not in (None, '') and math.isclose(float(actual), expected, rel_tol=2e-10, abs_tol=2e-12), (label, actual, expected)
        else:
            assert actual == expected, (label, actual, expected)
        checks[label.split(':')[0]] += 1

    C = read('inputs/cases.json')
    manifest = read('inputs/MANIFEST.json')
    for relative, expected_hash in manifest.items():
        data = (root / 'inputs' / relative).read_bytes()
        actual_hash = hashlib.sha256(data).hexdigest()
        equal(actual_hash, expected_hash, 'input_manifest:' + relative)
        hashes['inputs/' + relative] = actual_hash
    cases = {r['uid']: r for r in C}
    assert len(cases) == len(C) == 450
    ER = read('inputs/energy_repeats.json')
    reps = collections.defaultdict(list)
    for r in ER:
        reps[r['uid']].append(r)
    summary = read('results/summary.json')
    uncertainty = {r['uid']: r for r in read('results/tables/repeat_uncertainty.csv')}
    for r in C:
        uid = r['uid']
        if r['fps_samples']:
            equal(r['fps'], statistics.median(r['fps_samples']), 'stored_median:' + uid)
            assert len(r['fps_samples']) == 3
        else:
            assert r['runner'] == 'native' and r['kind'] == 'full' and not r['normal_performance_claim']
        equal(r['performance_observations'], len(r['fps_samples']) or 1, 'performance_n:' + uid)
        rr = reps[uid]
        assert len(rr) == (3 if r['normal_energy'] else 0), uid
        assert len({x['source_sha256'] for x in rr}) == len(rr), uid
        if rr:
            assert all(x['energy_j'] > 0 and x['completed_tasks'] > 0 for x in rr)
            values = [x['energy_j'] / x['completed_tasks'] for x in rr]
            for x, v in zip(rr, values):
                equal(x['j_per_task'], v, 'repeat_energy:' + uid)
                equal(x['tasks_per_j'], 1/v, 'repeat_efficiency:' + uid)
            avg = sum(values)/3
            variance = sum((x-avg)**2 for x in values)/2
            half = 4.302652729749461 * math.sqrt(variance/3)
            equal(r['raw_j_per_task'], avg, 'mean_energy:' + uid)
            equal(r['comparison_j_per_task'], sum(x['comparison_j_per_task'] for x in rr)/3, 'comparison_mean:' + uid)
            equal(r['mean_tasks_per_j'], sum(1/x for x in values)/3, 'mean_efficiency:' + uid)
            u = uncertainty[uid]
            for field, value in [('energy_mean_ci95_low', avg-half), ('energy_mean_ci95_high', avg+half),
                                 ('reciprocal_mean_E_over_N', 1/avg),
                                 ('sum_N_over_sum_E', sum(x['completed_tasks'] for x in rr)/sum(x['energy_j'] for x in rr))]:
                equal(u[field], value, 'uncertainty:' + uid + ':' + field)
            for actual, expected in zip(r['energy_ci'], [avg-half, avg+half]):
                equal(actual, expected, 'source_ci:' + uid)

    def uidkey(r):
        return (r['model_id'], r['setup_id'], r['backend'], r['case_id'])

    natives = {uidkey(r): r for r in C if r['runner'] == 'native'}
    generic = [r for r in C if r['runner'] == 'generic']
    binding = {b['generic_uid']: b for b in read('inputs/native_generic_bindings.json')}
    ngtable = {r['generic_uid']: r for r in read('results/tables/native_generic_pairs.csv')}
    ngcounts = collections.Counter()
    ngrates = []; ngenergy = []
    for g in generic:
        n = natives[uidkey(g)]
        b = binding[g['uid']]
        assert all(b['technical_gates'].values())
        assert b['native_summary_sha256'] == n['performance_source_sha256']
        assert b['generic_result_sha256'] == g['performance_source_sha256']
        pr = n['fps']/g['fps']
        equal(b['stored_fps_ratio'], pr, 'ng_source_ratio:' + g['uid'])
        t = ngtable[g['uid']]
        equal(t['fps_ratio'], pr, 'ng_table_ratio:' + g['uid'])
        assert n['normal_performance_claim'] and g['normal_performance_claim']
        ngcounts['performance'] += 1; ngcounts['faster'] += pr > 1; ngrates.append(pr)
        admitted = n['normal_energy'] and g['normal_energy']
        equal(t['energy_admitted'], admitted, 'ng_energy_gate:' + g['uid'])
        if admitted:
            assert (n['calibration_sha256'], n['energy_window'], n['energy_scope']) == (g['calibration_sha256'], g['energy_window'], g['energy_scope'])
            ratio = n['raw_j_per_task']/g['raw_j_per_task']
            equal(t['energy_ratio'], ratio, 'ng_table_energy:' + g['uid'])
            ngcounts['energy'] += 1; ngcounts['energy_lower'] += ratio < 1
            ngcounts['both_better'] += ratio < 1 and pr > 1; ngenergy.append(ratio)
        equal(t['both_reference_close'], n['quality_class'] == g['quality_class'] == 'reference_close', 'ng_quality:' + g['uid'])
        for metric, left, right in [('fps', n['fps_samples'], g['fps_samples']), ('energy', [x['j_per_task'] for x in reps[n['uid']]], [x['j_per_task'] for x in reps[g['uid']]])]:
            if metric == 'energy' and not admitted: continue
            ratios = [x/y for x in left for y in right]
            equal(t[metric+'_repeat_ratio_min'], min(ratios), 'ng_repeat_min:' + g['uid'])
            equal(t[metric+'_repeat_ratio_max'], max(ratios), 'ng_repeat_max:' + g['uid'])

    contracts = read('inputs/split_full_contracts.json')
    fulltable = {(r['split_uid'], r['baseline_uid']): r for r in read('results/tables/split_full_pairs.csv')}
    eligible = collections.defaultdict(list)
    fullcounts = collections.Counter()
    for p in contracts:
        n, f = cases[p['split_uid']], cases[p['baseline_uid']]
        assert n['kind'] == 'split' and f['kind'] == 'full'
        assert n['setup_id'] == f['setup_id'] and n['model_id'] == f['model_id']
        admitted = bool(p['semantic_comparable'] and p['claim_comparable'] and n['normal_energy'] and f['normal_energy'])
        perf = admitted and n['normal_performance_claim'] and f['normal_performance_claim']
        out = fulltable[n['uid'], f['uid']]
        equal(out['energy_admitted'], admitted, 'full_energy_gate:' + n['uid'])
        equal(out['performance_admitted'], perf, 'full_perf_gate:' + n['uid'])
        fullcounts['energy'] += admitted; fullcounts['performance'] += perf
        fullcounts['claim_not_semantic'] += p['claim_comparable'] and not p['semantic_comparable']
        if admitted:
            equal(p['split_energy_per_work_j'], n['comparison_j_per_task'], 'full_source_binding:' + n['uid'])
            equal(p['baseline_energy_per_work_j'], f['comparison_j_per_task'], 'full_source_binding:' + f['uid'])
            equal(out['energy_ratio'], n['comparison_j_per_task']/f['comparison_j_per_task'], 'full_comparison_ratio:' + n['uid'])
            equal(out['raw_energy_ratio'], n['raw_j_per_task']/f['raw_j_per_task'], 'full_raw_ratio:' + n['uid'])
            equal(out['split_raw_mj'], 1000*n['raw_j_per_task'], 'mj_units:' + n['uid'])
            ratios = [x['comparison_j_per_task']/y['comparison_j_per_task'] for x in reps[n['uid']] for y in reps[f['uid']]]
            equal(out['energy_repeat_ratio_min'], min(ratios), 'full_repeat_min:' + n['uid'])
            equal(out['energy_repeat_ratio_max'], max(ratios), 'full_repeat_max:' + n['uid'])
            eligible[n['uid']].append((f, perf))
        if perf: equal(out['fps_ratio'], n['fps']/f['fps'], 'full_fps_ratio:' + n['uid'])

    native_splits = [r for r in C if r['runner'] == 'native' and r['kind'] == 'split']
    selected = {(r['quality_filter'], r['energy_basis'], r['split_uid']): r for r in read('results/tables/baseline_selection_sensitivity.csv')}
    original = {r['split_uid']: r for r in read('results/tables/baseline_selection.csv')}
    sensitivity = {}; sensitivity_results = []
    for population in ['all_admitted', 'both_reference_close', 'exclude_administrative_receipt_gaps']:
        for basis in ['comparison', 'raw']:
            results = []
            for n in native_splits:
                options = [(f, perf) for f, perf in eligible[n['uid']] if population == 'all_admitted' or
                           (population == 'both_reference_close' and n['quality_class'] == f['quality_class'] == 'reference_close') or
                           (population == 'exclude_administrative_receipt_gaps' and not n['administrative_quality_receipt_gap'] and not f['administrative_quality_receipt_gap'])]
                faster = [f for f, perf in options if perf]
                fastest = sorted(faster, key=lambda f: (-f['fps'], f['uid']), reverse=False)[0] if faster else None
                # No equal-FPS ties are present in this generation.
                assert len({f['fps'] for f in faster}) == len(faster)
                energyfield = 'comparison_j_per_task' if basis == 'comparison' else 'raw_j_per_task'
                lowest = min((f for f, _ in options), key=lambda f: (f[energyfield], f['uid']), default=None)
                ratio = n[energyfield]/lowest[energyfield] if lowest else None
                speedup = n['fps']/fastest['fps'] if fastest else None
                t = selected[population, basis, n['uid']]
                for field, value in [('fastest_full', fastest['backend'] if fastest else None), ('lowest_energy_full', lowest['backend'] if lowest else None), ('speedup', speedup), ('energy_ratio', ratio)]:
                    equal(t[field], value, 'baseline_reselection:' + n['uid'] + ':' + field)
                if population == 'all_admitted' and basis == 'comparison':
                    base = original[n['uid']]
                    equal(base['speedup_vs_fastest_full'], speedup, 'primary_selection:' + n['uid'])
                    equal(base['energy_ratio_vs_lowest_full'], ratio, 'primary_selection:' + n['uid'])
                results.append((n, fastest, lowest, speedup, ratio))
            stat = {'n_performance': sum(x[3] is not None for x in results), 'faster_than_fastest_full': sum(x[3] is not None and x[3] > 1 for x in results), 'n_energy': sum(x[4] is not None for x in results), 'lower_than_min_full': sum(x[4] is not None and x[4] < 1 for x in results)}
            sensitivity[population + '/' + basis] = stat
            for model, setup in sorted({(n['model_id'], n['setup_id']) for n in native_splits}):
                within = [x for x in results if (x[0]['model_id'], x[0]['setup_id']) == (model, setup)]
                pp = [x for x in within if x[3] is not None]; ee = [x for x in within if x[4] is not None]
                winp = max(pp, key=lambda x: (x[0]['fps'], x[0]['case_id']), default=None)
                wine = min(ee, key=lambda x: (x[0][energyfield], x[0]['case_id']), default=None)
                sensitivity_results.append((population, basis, model, setup, winp, wine))
    optima = {(r['quality_filter'],r['energy_basis'],r['model'],r['setup']):r for r in read('results/tables/model_setup_sensitivity_optima.csv')}
    for pop, basis, model, setup, p, e in sensitivity_results:
        t = optima[pop,basis,model,setup]
        for field,value in [('fastest_split',p[0]['case_id'] if p else None),('lowest_energy_split',e[0]['case_id'] if e else None),('speedup',p[3] if p else None),('energy_ratio',e[4] if e else None)]:
            equal(t[field],value,'sensitivity_optimum:'+model+':'+setup)

    pareto = read('results/tables/pareto.csv')
    group_fields = ['model_id','setup_id','runner','comparison_endpoint','contract_preprocessing','contract_decoder','contract_nms','prepared_image_sha256','calibration_sha256','backend','precision','measurement_boundary','energy_scope','energy_window','completion_mode','completion_contract_sha256','scheduling']
    for t in pareto:
        r = cases[t['uid']]
        peers = [q for q in C if q['kind'] == 'split' and q['normal_performance_claim'] and q['normal_energy'] and q['comparison_endpoint'] and q['prepared_image_sha256'] and
                 (t['quality_filter'] == 'all_admitted' or q['quality_class'] == 'reference_close') and all(q.get(k)==r.get(k) for k in group_fields)]
        dominating = {q['uid'] for q in peers if q['fps'] >= r['fps'] and q['raw_j_per_task'] <= r['raw_j_per_task'] and (q['fps'] != r['fps'] or q['raw_j_per_task'] != r['raw_j_per_task'])}
        equal(t['pareto'], not dominating, 'pareto:' + r['uid'])
        equal(t['cohort_n'], len(peers), 'pareto_size:' + r['uid'])
        assert set(json.loads(t['dominated_by'])) == dominating

    # Spearman via average ranks and Pearson correlation, independently of scipy.
    def ranks(vals):
        positions = collections.defaultdict(list)
        for i,v in enumerate(sorted(vals),1): positions[v].append(i)
        return [sum(positions[v])/len(positions[v]) for v in vals]
    graph = {(x['model_id'],x['case_id']):x for x in read('inputs/graph_features.json')}
    for row in read('results/tables/graph_associations.csv'):
        data=[]
        for c in C:
            if c['kind']!='split' or (c['model_id'],c['setup_id'],c['runner'])!=(row['model'],row['setup'],row['runner']):continue
            g=graph.get((c['model_id'],c['case_id']))
            if g is None or (row['metric']=='raw_j_per_task' and not c['normal_energy']):continue
            x,y=g.get(row['feature']),c[row['metric']]
            if x is not None and y is not None:data.append((x,y))
        equal(row['n'],len(data),'graph_n:'+row['model'])
        rho=None
        if len(data)>=3 and len({x for x,y in data})>1 and len({y for x,y in data})>1:
            x=ranks([x for x,y in data]);y=ranks([y for x,y in data]);xm=sum(x)/len(x);ym=sum(y)/len(y)
            rho=sum((a-xm)*(b-ym) for a,b in zip(x,y))/math.sqrt(sum((a-xm)**2 for a in x)*sum((b-ym)**2 for b in y))
        equal(row['spearman_rho'],rho,'graph_rho:'+row['model'])

    pipe=read('inputs/pipeline_repeats.json')
    assert len(pipe)==720 and len({(x['uid'],x['repeat']) for x in pipe})==720
    assert not read('inputs/pipeline_missing.json')
    limits=read('inputs/provenance_limits.json')
    gapcount=sum(not r['matches'] for r in limits['rows'])
    equal(gapcount,17,'provenance_gap_count')
    assert all(r['normal_report_matches_current'] and r['validation_summary_matches_current'] for r in limits['rows'])
    for field,value in [('faster',ngcounts['faster']),('energy_lower',ngcounts['energy_lower']),('both_better',ngcounts['both_better']),('fps_ratio_median',statistics.median(ngrates)),('energy_ratio_median',statistics.median(ngenergy))]:
        equal(summary['native_generic'][field],value,'summary:'+field)
    equal(summary['full_pair_gates']['energy_admitted'],fullcounts['energy'],'summary:full_energy')
    equal(summary['full_pair_gates']['performance_admitted'],fullcounts['performance'],'summary:full_performance')
    equal(summary['full_pair_gates']['claim_but_not_semantic'],fullcounts['claim_not_semantic'],'summary:semantic_exclusions')
    equal(len([x for x in C if not x['normal_energy']]),13,'boundary_preservation')
    equal(len([x for x in C if x['quality_class']=='accuracy_loss']),43,'negative_quality_preservation')
    diagnostic = read('inputs/diagnostic_acceptance.json')
    diagnostic_result = read('results/diagnostic_result.json')
    dfps = diagnostic['metrics']['fps_display']
    de = diagnostic['metrics']['energy']['energy_per_completed_task_j']
    oldfps = diagnostic['historical_baseline_context']['historical_fps']
    olde = diagnostic['historical_baseline_context']['historical_energy_per_task_j']
    for field, value in [('fps_single', dfps), ('energy_single_j_per_task', de),
                         ('historical_fps_median', oldfps), ('historical_mean_j_per_task', olde),
                         ('fps_relative_change', dfps/oldfps-1), ('energy_relative_change', de/olde-1)]:
        equal(diagnostic_result[field], value, 'diagnostic:' + field)
    assert diagnostic['role'] == 'separate_diagnostic_single'
    normalization_direction_changes = sum(
        (float(p['raw_energy_ratio']) < 1) != (float(p['energy_ratio']) < 1)
        for p in fulltable.values() if p['energy_admitted'] == 'True')
    equal(normalization_direction_changes, 34, 'normalization_direction_changes')
    for relative in ['METHODS.md', 'scripts/extract_canonical.py', 'scripts/reproduce.py',
                     'results/WISSENSCHAFTLICHE_ANALYSE.md']:
        hashes[relative] = hashlib.sha256((root / relative).read_bytes()).hexdigest()
    result={'status':'PASS_COMPACT_ARITHMETIC_WITH_DECLARED_ARCHIVE_LIMITS','implementation':'Independent Python standard library; no production analysis imports','review_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':dict(checks),'native_generic':dict(ngcounts),'native_generic_median_fps_ratio':statistics.median(ngrates),'native_generic_median_raw_energy_ratio':statistics.median(ngenergy),'full_pair_counts':dict(fullcounts),'selection_sensitivity':sensitivity,'normalization_direction_changes':normalization_direction_changes,'diagnostic_fps_relative_change':dfps/oldfps-1,'diagnostic_energy_relative_change':de/olde-1,'energy_repeats':len(ER),'pareto_decisions_checked':len(pareto),'graph_associations_checked':420,'pipeline_repeats_checked':len(pipe),'administrative_receipt_version_gaps':gapcount,'limitations':['17 selected Native administrative receipt versions remain unresolved; exact normal result/quality leaf hashes match the archived alternate receipts','21 historical Full-producer source references remain a declared source-code limit','No raw sensor reintegration or dataset evaluation was rerun','No hardware or network access; no independent validation of physical calibration'],'file_sha256':hashes}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='file_sha256'},indent=2))


if __name__=='__main__':
    main()
