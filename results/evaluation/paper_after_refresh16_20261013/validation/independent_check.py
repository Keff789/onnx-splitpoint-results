#!/usr/bin/env python3
"""Recalculate paper core quantities independently, using Python's standard library.

No import of the dataset builder, its metric functions, or the plotting code.
The compact original observations are the numerical authority for this check.
"""
import argparse
import collections
import csv
import json
import math
from pathlib import Path
import statistics


def read(path):
    return json.loads(path.read_text())


def close(actual, expected, label):
    if actual is None or expected is None:
        assert actual is expected, (label, actual, expected)
    else:
        assert math.isclose(actual, expected, rel_tol=1e-10, abs_tol=1e-12), (label, actual, expected)


def unique(rows, field='uid'):
    mapped = {r[field]: r for r in rows}
    assert len(mapped) == len(rows), ('Duplicate identity', field)
    return mapped


def finite_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def check_pareto(paper, output):
    """Independent exhaustive comparison; never import the sweep implementation."""
    exported = unique(read(output/'tables/PARETO_POINTS.json'))
    assert set(exported) == set(paper), 'Pareto export changed selected population'
    groups = collections.defaultdict(list)
    for uid, row in paper.items():
        point = exported[uid]
        for field, source_field in [('model','model_id'), ('setup','setup_id'), ('case','case_id'),
                                    ('runner','runner'), ('kind','kind'), ('backend','backend')]:
            assert point[field] == row[source_field], ('Pareto grouping/identity', uid, field)
        reasons = []
        for field in ['fps', 'energy_mj_per_image']:
            value = row.get(field)
            if value is None:
                reasons.append('missing_' + field)
            elif not isinstance(value, (int, float)) or isinstance(value, bool):
                reasons.append('invalid_' + field)
            elif not math.isfinite(value):
                reasons.append('nonfinite_' + field)
            assert point[field] == (value if finite_number(value) else None), ('Exact Pareto coordinate', uid, field)
        assert point['included'] is (not reasons), ('Pareto numeric-only inclusion', uid)
        assert point['omission_reason'] == (';'.join(reasons) or None), ('Pareto omission reason', uid)
        q = row.get('quality_value')
        assert point['quality_value'] == (q if finite_number(q) else None), ('Exact Pareto quality', uid)
        assert point['quality_percent'] == (100*q if finite_number(q) else None), ('Exact Pareto color', uid)
        assert point['quality_metric'] == row.get('quality_metric'), ('Pareto quality metric', uid)
        if not reasons:
            groups[(row['model_id'], row['setup_id'])].append(uid)
        else:
            assert all(point[k] is None for k in ['pareto_all','pareto_native','pareto_generic','dominated_by_uid'])

    def dominators(uid, population):
        a = paper[uid]
        return sorted(other for other in population
                      if paper[other]['fps'] >= a['fps']
                      and paper[other]['energy_mj_per_image'] <= a['energy_mj_per_image']
                      and (paper[other]['fps'] > a['fps']
                           or paper[other]['energy_mj_per_image'] < a['energy_mj_per_image']))

    front_sizes = []
    for (model, setup), population in sorted(groups.items()):
        for uid in population:
            witnesses = dominators(uid, population)
            assert exported[uid]['pareto_all'] is (not witnesses), ('Pairwise Pareto mismatch', uid)
            assert exported[uid]['dominated_by_uid'] == (witnesses[0] if witnesses else None), ('Pareto witness', uid)
        for runner in ['native', 'generic']:
            splits = [u for u in population if paper[u]['kind'] == 'split' and paper[u]['runner'] == runner]
            for uid in population:
                expected = not dominators(uid, splits) if uid in splits else None
                assert exported[uid]['pareto_' + runner] is expected, ('Runner Pareto mismatch', uid, runner)
        front = [u for u in population if not dominators(u, population)]
        front_sizes.append({'model': model, 'setup': setup, 'observations': len(population),
                            'front_uids': sorted(front), 'front_size': len(front),
                            'front_coordinates': len({(paper[u]['fps'],paper[u]['energy_mj_per_image']) for u in front}),
                            'native_split_front_size': sum(exported[u]['pareto_native'] is True for u in population),
                            'generic_split_front_size': sum(exported[u]['pareto_generic'] is True for u in population)})
    with (output/'tables/PARETO_POINTS.csv').open(newline='') as handle:
        csv_points = unique(list(csv.DictReader(handle)))
    assert set(csv_points) == set(exported), 'CSV/JSON Pareto population differs'
    for uid, point in exported.items():
        assert set(csv_points[uid]) == set(point), ('CSV/JSON Pareto fields', uid)
        for field, value in point.items():
            assert csv_points[uid][field] == ('' if value is None else str(value)), ('CSV/JSON Pareto value', uid, field)
    return exported, {'points': len(exported), 'included': sum(p['included'] for p in exported.values()),
                      'groups': len(groups), 'front_sizes': front_sizes,
                      'algorithm': 'exhaustive pairwise comparison of original unrounded PAPER_DATASET coordinates'}


def check(inputs, output):
    source = unique(read(inputs/'cases.json'))
    paper = unique(read(output/'PAPER_DATASET.json'))
    assert set(paper) == set(source), 'Broad paper selection changed canonical case scope'
    energies = collections.defaultdict(list)
    for r in read(inputs/'energy_repeats.json'):
        assert r['completed_tasks'] > 0 and r['energy_j'] > 0
        close(r['j_per_task'], r['energy_j']/r['completed_tasks'], r['uid']+' repeat E/N')
        energies[r['uid']].append(r)
    fps, energy = {}, {}
    uncertainty=unique(read(output/'tables/repeat_uncertainty.json'))
    for uid, row in source.items():
        # Check that the broad representation preserves every original flag/value.
        assert all(paper[uid].get(k) == v for k, v in row.items()), ('Original field changed', uid)
        samples = row.get('fps_samples') or []
        fps[uid] = statistics.median(samples) if samples else row['fps']
        close(paper[uid]['fps'], fps[uid], uid+' median FPS')
        close(paper[uid]['performance_n'], row['performance_observations'], uid+' performance n')
        repeats = energies.get(uid, [])
        energy[uid] = statistics.mean(r['energy_j']/r['completed_tasks'] for r in repeats) if repeats else None
        close(paper[uid]['energy_j_per_image'], energy[uid], uid+' mean(E/N)')
        close(paper[uid]['energy_mj_per_image'], energy[uid]*1000 if energy[uid] is not None else None, uid+' mJ/image')
        close(paper[uid]['energy_n'], len(repeats), uid+' energy n')
        if repeats:
            images_per_joule=statistics.mean(r['completed_tasks']/r['energy_j'] for r in repeats)
            close(paper[uid]['mean_tasks_per_j'],images_per_joule,uid+' original mean(N/E)')
            close(uncertainty[uid]['mean_N_over_E'],images_per_joule,uid+' mean(N/E)')
            close(uncertainty[uid]['reciprocal_mean_E_over_N'],1/energy[uid],uid+' reciprocal mean(E/N)')
            pooled=sum(r['energy_j'] for r in repeats)/sum(r['completed_tasks'] for r in repeats)
            close(uncertainty[uid]['sum_E_over_sum_N'],pooled,uid+' pooled energy')
            close(uncertainty[uid]['sum_N_over_sum_E'],1/pooled,uid+' pooled efficiency')

    # Exact targeted replacement and preservation, independently from the extractor.
    baseline = unique(read(inputs/'baseline_cases.json'))
    targets = set(read(inputs/'refresh16_provenance.json')['targeted_uids'])
    assert set(baseline) == set(source)
    assert {u for u in source if source[u] != baseline[u]} == targets
    gates = {k for c in source.values() for k in c if 'quality' in k or k in
             ['normal_performance_claim','energy_claim','energy_exclusions']}
    assert all(source[u].get(k) == baseline[u].get(k) for u in source for k in gates)
    for uid in targets:
        assert source[uid]['performance_observations'] == len(energies[uid]) == 3

    evidence = unique(read(inputs/'selected_evidence.json'))
    for uid, e in evidence.items():
        for field in ['quality_value','quality_reference_value','quality_numeric_relative_loss','quality_cached_loss_disagrees']:
            assert paper[uid].get(field) == e.get(field), (uid, field)

    # Recreate all host-specific Full alternatives; choose the FPS maximum before
    # looking at energy, then rank Native splits using unrounded values and UID.
    fulls = collections.defaultdict(list)
    models = set()
    for uid, row in source.items():
        models.add(row['model_id'])
        if row['kind'] == 'full':
            fulls[(row['model_id'], row['setup_id'])].append(uid)
    expected_top = {}
    for model in sorted(models):
        candidates = []
        for uid, row in source.items():
            if row['model_id'] != model or row['runner'] != 'native' or row['kind'] != 'split' or fps[uid] is None:
                continue
            available = [u for u in fulls[(model, row['setup_id'])] if fps[u] is not None]
            if not available:
                continue
            baseline_uid = sorted(available, key=lambda u: (-fps[u], u))[0]
            candidates.append((fps[uid]/fps[baseline_uid], uid, baseline_uid))
        expected_top[model] = sorted(candidates, key=lambda x: (-x[0],x[1]))[:2]
    table3 = read(output/'tables/table3_top2_native.json')
    observed_top = collections.defaultdict(list)
    for r in table3:
        uid, base = r['split_uid'], r['baseline_uid']
        observed_top[source[uid]['model_id']].append((uid,base))
        close(r['split_fps'], fps[uid], uid+' table3 split FPS')
        close(r['baseline_fps'], fps[base], uid+' table3 Full FPS')
        close(r['speedup'], fps[uid]/fps[base], uid+' table3 speedup')
        close(r['split_mj_per_image'], energy[uid]*1000, uid+' table3 energy')
        close(r['energy_gain_same_full'], energy[base]/energy[uid], uid+' table3 same-Full G_n')
        assert source[uid]['setup_id'] == source[base]['setup_id']
    for model, tuples in expected_top.items():
        assert observed_top[model] == [(u,b) for _,u,b in tuples], (model, observed_top[model], tuples)

    # Table 2 ranges span three host aggregates, not the underlying repeats.
    table2 = read(output/'tables/table2_full.json')
    assert {r['model'] for r in table2} == models
    for row in table2:
        model = row['model']
        tf = [uid for uid,c in source.items() if c['model_id']==model and c['kind']=='full'
              and c['backend']=='native_full_tensorrt']
        assert row['trt_host_count'] == len(tf)
        for unit,values in [('fps',[fps[u] for u in tf]),('mj',[1000*energy[u] for u in tf])]:
            for suffix,fn in [('min',min),('max',max),('mean',statistics.mean)]:
                close(row['trt_'+unit+'_'+suffix],fn(values),model+' TRT '+unit+' '+suffix)
        for setup in ['DeepX','H8','H10']:
            for trt in [True,False]:
                ids=[u for u in fulls[(model,setup)] if (source[u]['backend']=='native_full_tensorrt')==trt]
                assert len(ids)==1
                label=('trt_' if trt else '')+setup
                assert row[label+'_uid']==ids[0]
                close(row[label+'_fps'],fps[ids[0]],model+' '+label+' FPS')
                close(row[label+'_mj'],1000*energy[ids[0]],model+' '+label+' mJ/image')

    pairs = read(output/'tables/split_full_pairs.json')
    pair_ids = {(r['split_uid'], r['baseline_uid']) for r in pairs}
    expected_pair_ids={(u,b) for u,s in source.items() if s['kind']=='split'
                       for b in fulls[(s['model_id'],s['setup_id'])]}
    assert pair_ids==expected_pair_ids and len(pair_ids)==len(pairs)
    for r in pairs:
        u,b = r['split_uid'],r['baseline_uid']
        close(r['fps_ratio'],fps[u]/fps[b],u+' split/Full FPS')
        close(r['energy_ratio'],energy[u]/energy[b],u+' split/Full energy')
        close(r['energy_gain_same_full'],energy[b]/energy[u],u+' split/Full G_n')
    prior_contracts = read(inputs/'split_full_contracts.json')
    contract_map={(r['split_uid'],r['baseline_uid']):r for r in prior_contracts}
    for r in pairs:
        prior=contract_map.get((r['split_uid'],r['baseline_uid']))
        assert r['source_claim_flag']==(prior.get('claim_comparable') if prior else None)
        assert r['semantic_comparable']==(prior.get('semantic_comparable') if prior else None)
        assert r['original_semantic_reasons']==(prior.get('semantic_comparison_reasons',[]) if prior else [])
    required28 = {(r['split_uid'],r['baseline_uid']) for r in prior_contracts
                  if r.get('claim_comparable') and not r.get('semantic_comparable')}
    assert required28 <= pair_ids, ('Previously excluded Full pairs missing', required28-pair_ids)
    required3 = [r for r in source.values() if r['setup_id']=='H10' and r['task']=='classification'
                 and r['backend']=='native_full_tensorrt' and not r['normal_performance_claim']]
    for r in required3:
        assert paper[r['uid']]['fps'] is not None and not paper[r['uid']]['normal_performance_claim']

    ng = read(output/'tables/native_generic_pairs.json')
    groups = collections.defaultdict(list)
    for r in ng:
        n,g=r['native_uid'],r['generic_uid']
        assert source[n]['runner']=='native' and source[g]['runner']=='generic'
        assert all(source[n][k]==source[g][k] for k in ['model_id','setup_id','backend','case_id'])
        close(r['fps_ratio'],fps[n]/fps[g],n+' Native/Generic FPS')
        close(r['energy_ratio'],energy[n]/energy[g],n+' Native/Generic energy')
        groups[(source[n]['model_id'],source[n]['setup_id'])].append(r)
    medians = {key:{metric:statistics.median(r[metric] for r in rr)
                    for metric in ['fps_ratio','energy_ratio']} for key,rr in groups.items()}
    equal=read(output/'tables/equal_model_summary.json')
    for row in equal:
        for metric in ['fps_ratio','energy_ratio']:
            if row['setup']=='all':
                model_means=[statistics.mean(vals[metric] for (m,s),vals in medians.items() if m==model)
                             for model in sorted({m for m,s in medians})]
                expected=statistics.mean(model_means)
            else:
                expected=statistics.mean(vals[metric] for (m,s),vals in medians.items() if s==row['setup'])
            close(row[metric],expected,row['setup']+' equal-model '+metric)

    summary=read(output/'summary.json')
    assert summary['cases']==len(paper)
    assert summary['performance_coverage']==sum(v is not None for v in fps.values())
    assert summary['energy_coverage']==sum(v is not None for v in energy.values())
    assert summary['native_generic']['n_pairs']==len(ng)
    assert summary['all_runner_split_full']['n_pairs']==len(pairs)
    assert summary['historical_strict_excluded_pairs_retained']==len(required28)
    assert summary['nonclaim_performance_full_values_retained']==sum(r['kind']=='full' and not r['normal_performance_claim'] and fps[u] is not None for u,r in source.items())
    pareto, pareto_report = check_pareto(paper, output)

    # Figures retain an explicit payload of the points actually drawn. Check its
    # identities and values against this independently reconstructed population.
    figure_count=0
    figure_path=output/'figures/FIGURE_DATA.json'
    if figure_path.exists():
        figures=read(figure_path)
        figure_count=len(figures)
        full_ids={u for ids in fulls.values() for u in ids}
        for name,key,values in [('01_full_throughput','fps',fps),('02_full_energy','energy_mj_per_image',{u:1000*v for u,v in energy.items()})]:
            f=figures[name]
            assert set(f['scope_uids'])==full_ids
            assert {r['uid'] for r in f['points']}==full_ids
            for point in f['points']:
                close(point['value'],values[point['uid']],name+' '+point['uid'])
        for name in ['03a_native_generic_pooled','03c_native_generic_model_setup']:
            assert figures[name]['pairs']==ng
        for point in figures['03b_native_generic_equal_model']['model_setup_medians']:
            for metric in ['fps_ratio','energy_ratio']:
                close(point[metric],medians[(point['model'],point['setup'])][metric],'figure model/setup median')
        for point in figures['03b_native_generic_equal_model']['model_means_over_setups']:
            for metric in ['fps_ratio','energy_ratio']:
                expected=statistics.mean(vals[metric] for (m,s),vals in medians.items() if m==point['model'])
                close(point[metric],expected,'figure model mean over setups')
        equal_map={r['setup']:r for r in equal}
        for point in figures['03b_native_generic_equal_model']['setup_summaries']:
            t=equal_map['all' if point['setup']=='All' else point['setup']]
            close(point['mean_model_setup_medians'],t[point['metric']],'figure equal-model summary')
            assert point['n_models']==t['n_models']
        for model in sorted(models):
            ids={u for u,r in source.items() if r['model_id']==model}
            f=figures['04_tradeoff_'+model]
            plotted={u for u in ids if pareto[u]['included']}
            assert set(f['scope_uids'])==ids and set(unique(f['points']))==plotted
            assert set(f['omitted_uids'])==ids-plotted
            assert unique(f['omitted_points'])=={u:pareto[u] for u in ids-plotted}
            for point in f['points']:
                assert all(point[k]==v for k,v in pareto[point['uid']].items()), ('Exact plot/export point',point['uid'])
                close(point['fps'],fps[point['uid']],'figure tradeoff FPS')
                close(point['energy_mj_per_image'],1000*energy[point['uid']],'figure tradeoff energy')
                q=paper[point['uid']].get('quality_value')
                close(point['quality_percent'],100*q if q is not None else None,'figure tradeoff quality')
            front_payload=f['pareto_front']
            assert front_payload['grouping']==['model','setup']
            assert front_payload['objectives']=={'fps':'maximize','energy_mj_per_image':'minimize'}
            assert front_payload['quality_filter'] is False
            groups={(g['model'],g['setup']):g for g in front_payload['groups']}
            assert len(groups)==len(front_payload['groups'])
            assert set(groups)=={(model,paper[u]['setup_id']) for u in ids}
            expected_annotations=set()
            for (m,setup),group in groups.items():
                population={u for u in plotted if paper[u]['setup_id']==setup}
                front={u for u in population if pareto[u]['pareto_all']}
                coordinates=sorted({(paper[u]['fps'],paper[u]['energy_mj_per_image']) for u in front})
                assert sorted(group['front_uids'])==sorted(front), ('Figure front UIDs',m,setup)
                assert group['front_coordinates']==[{'fps':x,'energy_mj_per_image':y} for x,y in coordinates]
                assert group['n_observations']==len(population)
                assert group['n_front_uids']==len(front)
                assert group['n_front_coordinates']==len(coordinates)
                assert group['line_drawn'] is (len(coordinates)>1), ('Singleton front must have no line',m,setup)
                for uid in population:
                    if paper[uid]['kind']=='full':
                        label='TRT Full' if paper[uid]['backend']=='native_full_tensorrt' else 'Vendor Full'
                        expected_annotations.add((uid,label))
                for runner in ['native','generic']:
                    candidates=[u for u in population if paper[u]['kind']=='split' and paper[u]['runner']==runner]
                    if not candidates:
                        continue
                    fastest=min(candidates,key=lambda u:(-paper[u]['fps'],u))
                    lowest=min(candidates,key=lambda u:(paper[u]['energy_mj_per_image'],u))
                    prefix=runner[0].upper()+' '
                    if fastest==lowest:
                        expected_annotations.add((fastest,prefix+'F=E '+paper[fastest]['case_id']))
                    else:
                        expected_annotations.add((fastest,prefix+'F '+paper[fastest]['case_id']))
                        expected_annotations.add((lowest,prefix+'E '+paper[lowest]['case_id']))
            annotations=f['annotations']
            assert {(a['uid'],a['label']) for a in annotations}==expected_annotations, ('Figure F/E/Full annotations',model)
            assert len(annotations)==len(expected_annotations), ('Duplicate plot annotation',model)
            for a in annotations:
                assert a['model']==model and a['setup']==paper[a['uid']]['setup_id']
                assert len(a['text_offset_points'])==2 and all(finite_number(v) for v in a['text_offset_points'])
            qf=figures['06_quality_'+model]
            assert set(qf['scope_uids'])==ids
            for point in qf['points']:
                d=paper[point['uid']]
                close(point['quality_percent'],100*d['quality_value'],'figure absolute quality')
                close(point['reference_percent'],100*d['quality_reference_value'],'figure reference quality')
        f=figures['06_quality_reference_comparison']
        assert set(f['scope_uids'])==set(paper)
        quality_ids={u for u,r in paper.items() if r.get('quality_value') is not None and r.get('quality_reference_value') is not None}
        assert {r['uid'] for r in f['points']}==quality_ids
        assert set(f['missing_numeric_quality_uids'])==set(paper)-quality_ids
        for point in f['points']:
            d=paper[point['uid']]
            close(point['difference_percentage_points'],100*(d['quality_value']-d['quality_reference_value']),'figure quality percentage-point difference')
        optima=read(output/'tables/model_setup_optima.json')
        table_optima={(r['model'],r['setup'],r['runner']):r for r in optima}
        for r in figures['05_fastest_vs_min_energy']['optima']:
            t=table_optima[(r['model'],r['setup'],r['runner'])]
            assert all(r[k]==t[k] for k in ['candidate_count','fastest_uid','lowest_energy_uid','same_optimum'])
    return {'status':'PASS', 'dataset_cases':len(paper), 'energy_repeat_checks':sum(map(len,energies.values())),
            'fps_cohort_checks':len(fps), 'refresh_replacements':len(targets),
            'unchanged_complete_non_target_rows':len(source)-len(targets),
            'preserved_quality_and_original_gate_rows':len(source),
            'full_configurations':sum(map(len,fulls.values())), 'table2_model_rows':len(table2),'table3_rows':len(table3),
            'native_generic_pairs':len(ng),'split_full_pairs':len(pairs),'figure_payloads_checked':figure_count,
            'pareto':pareto_report,
            'restored_full_pairs_checked':len(required28), 'restored_h10_trt_classifier_values_checked':len(required3)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = check(args.inputs,args.output)
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__ == '__main__':
    main()
