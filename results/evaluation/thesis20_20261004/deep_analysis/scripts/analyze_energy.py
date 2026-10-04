#!/usr/bin/env python3
"""Offline post-hoc energy analysis of existing compact THESIS20 product projections.
No network, inference, compilation, hardware access or original-file modification.
"""
from __future__ import annotations
import argparse, csv, json, math, statistics, sys
from collections import Counter, defaultdict
from pathlib import Path

GROUP_FIELDS = ('model_id', 'setup_id', 'direction', 'precision', 'comparison_backend',
                'output_endpoint_id', 'boundary_class', 'calibration_sha256', 'window', 'physical_scope')

def read_csv(path):
    def value(x):
        if x == '': return None
        if x in ('True', 'False'): return x == 'True'
        if x.startswith(('[', '{')):
            try: return json.loads(x)
            except ValueError: pass
        try:
            f = float(x)
            return int(f) if f.is_integer() else f
        except ValueError: return x
    with path.open(newline='') as f:
        return [{k: value(v) for k, v in r.items()} for r in csv.DictReader(f)]

def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n'); w.writeheader()
        for r in rows:
            w.writerow({k: json.dumps(v, sort_keys=True, separators=(',', ':')) if isinstance(v, (dict,list,tuple)) else v for k,v in r.items()})

def ident(r): return tuple(r[k] for k in ('cohort','model_id','case_id','setup_id','backend'))
def case_ident(r): return tuple(r[k] for k in ('model_id','case_id','setup_id'))
def unique_index(rows, key):
    out={}
    for r in rows:
        k=key(r)
        if k in out: raise ValueError(f'duplicate identity: {k}')
        out[k]=r
    return out

def quantile(values, q):
    vals=sorted(values)
    if not vals:return None
    pos=(len(vals)-1)*q; lo=math.floor(pos); hi=math.ceil(pos)
    return vals[lo]+(vals[hi]-vals[lo])*(pos-lo)

def summarize_repeats(reps):
    if len(reps)!=3 or {r['repetition'] for r in reps}!={0,1,2}:raise ValueError('expected three original repetitions')
    e=[r['energy_j'] for r in reps]; n=[r['completed_count'] for r in reps]; t=[r['active_duration_s'] for r in reps]
    if any(x<=0 for x in e+n+t):raise ValueError('nonpositive energy/count/window')
    j=[a/b for a,b in zip(e,n)]; p=[a/b for a,b in zip(e,t)]; rate=[a/b for a,b in zip(n,t)]
    out={}
    for k,v in [('j_per_task',j),('power_w',p),('energy_fps',rate)]:
        out.update({k+'_mean':statistics.mean(v),k+'_median':statistics.median(v),k+'_min':min(v),k+'_max':max(v),k+'_sd':statistics.stdev(v)})
    out.update(j_per_task_pooled=sum(e)/sum(n),power_w_pooled=sum(e)/sum(t),energy_fps_pooled=sum(n)/sum(t),
               completed_count_total=sum(n),active_duration_s_total=sum(t),energy_j_total=sum(e),
               pooled_j_relative_difference=sum(e)/sum(n)/statistics.mean(j)-1,
               mean_identity_relative_gap=statistics.mean(p)/statistics.mean(rate)/statistics.mean(j)-1)
    return out

def pareto_flags(rows, rate='energy_fps_mean', energy='j_per_task_mean'):
    return {r['case_uid']:not any(o[rate]>=r[rate] and o[energy]<=r[energy] and (o[rate]>r[rate] or o[energy]<r[energy]) for o in rows) for r in rows}

def winner(rows, metric, maximize=False):
    return sorted(rows,key=lambda r:((-r[metric] if maximize else r[metric]),r['case_id'],r['case_uid']))[0]

def groupkey(r):return tuple(r[k] for k in GROUP_FIELDS)
def groupbase(r):return {k:r[k] for k in GROUP_FIELDS}

def joint_summary(rows):
    return dict(n_pairs=len(rows),n_unique_splits=len({r['split_uid'] for r in rows}),n_unique_fulls=len({r['baseline_uid'] for r in rows}),
        n_semantic=sum(r['semantic_comparable'] for r in rows),n_reference_close=sum(r['both_reference_close'] for r in rows),
        n_energy_saving=sum(r['energy_ratio']<1 for r in rows),n_faster_energy_window=sum(r['energy_window_rate_ratio']>1 for r in rows),
        n_both_advantages=sum(r['energy_ratio']<1 and r['energy_window_rate_ratio']>1 for r in rows),
        n_neither_advantage=sum(r['energy_ratio']>=1 and r['energy_window_rate_ratio']<=1 for r in rows),
        n_only_energy_advantage=sum(r['energy_ratio']<1 and r['energy_window_rate_ratio']<=1 for r in rows),
        n_only_throughput_advantage=sum(r['energy_ratio']>=1 and r['energy_window_rate_ratio']>1 for r in rows),
        n_energy_saving_all_9_repeat_combinations=sum(r['energy_ratio_repeat9_max']<1 for r in rows),
        n_faster_all_9_repeat_combinations=sum(r['rate_ratio_repeat9_min']>1 for r in rows),
        n_both_all_9_repeat_combinations=sum(r['energy_ratio_repeat9_max']<1 and r['rate_ratio_repeat9_min']>1 for r in rows),
        n_pooled_changes_energy_advantage=sum((r['energy_ratio']<1)!=(r['energy_ratio_pooled']<1) for r in rows),
        **{f'{m}_{lab}':quantile([r[m] for r in rows],q) for m in ['energy_ratio','energy_window_rate_ratio','power_ratio','performance_rate_ratio'] for lab,q in [('min',0),('q25',.25),('median',.5),('q75',.75),('max',1)]})

def analyze(source, output):
    I=source/'inputs';T=output/'tables';T.mkdir(parents=True,exist_ok=True)
    energies=read_csv(I/'energy_cases.csv');reps=read_csv(I/'energy_repeats.csv');orig_pairs=read_csv(I/'energy_split_full_pairs.csv')
    cp=unique_index(read_csv(I/'completion_pairs.csv'),case_ident); natives=unique_index(read_csv(I/'native_cases.csv'),ident)
    er=defaultdict(list)
    for r in reps:er[r['case_uid']].append(r)
    emap=unique_index(energies,ident);unique_index(energies,lambda r:r['case_uid']);unique_index(orig_pairs,lambda r:(r['model_id'],r['case_id'],r['setup_id'],r['split_backend'],r['baseline_backend']))
    cases=[];checks=[];recomputed_repeats=[]
    for e in energies:
        rr=sorted(er[e['case_uid']],key=lambda r:r['repetition']);s=summarize_repeats(rr)
        for r in rr:
            recomputed_repeats.append(dict(r,j_per_task=r['energy_j']/r['completed_count'],power_w=r['energy_j']/r['active_duration_s'],energy_fps=r['completed_count']/r['active_duration_s'],replicate_identity_absolute_residual=r['energy_j']/r['completed_count']-(r['energy_j']/r['active_duration_s'])/(r['completed_count']/r['active_duration_s'])))
            for calc,stored in [(r['energy_j']/r['completed_count'],r['reported_j_per_task']),(r['energy_j']/r['active_duration_s'],r['reported_power_w']),(r['completed_count']/r['active_duration_s'],r['energy_window_throughput_fps'])]:
                assert math.isclose(calc,stored,rel_tol=1e-10,abs_tol=1e-10)
                checks.append(abs(calc-stored))
        for calc,stored in [(s['j_per_task_mean'],e['energy_per_task_j']),(s['energy_fps_mean'],e['energy_window_throughput_fps']),(s['power_w_mean'],e['power_w'])]:
            assert math.isclose(calc,stored,rel_tol=1e-10,abs_tol=1e-10)
        c=dict(e,**s,performance_fps=natives[ident(e)]['fps'],attestor_source_gap=e['backend']=='native_full_tensorrt')
        if e['execution_mode']=='native_split':
            pair=cp[case_ident(e)]
            c.update({k:pair[k] for k in ['direction','output_endpoint_id','boundary_class']})
            c['reference_close_native']=e['accuracy_class']=='reference_close'
            c['reference_close_transfer']=pair['eligible_for_quality_transfer'] is True and pair['generic_task_quality_status']=='reference_close' and pair['native_task_quality_status']=='reference_close'
        cases.append(c)
    cmap=unique_index(cases,ident);uidmap=unique_index(cases,lambda r:r['case_uid'])
    pairs=[];repeatpairs=[];limits=[];legacy_audit=[]
    hostnorm={}
    for r in orig_pairs:
        if r['cohort']=='base' and r['baseline_kind']=='tensorrt_full':
            k=(r['model_id'],r['setup_id'],r['baseline_backend'])
            v=r['baseline_energy_per_work_j']
            if k in hostnorm:assert math.isclose(hostnorm[k],v,rel_tol=1e-12)
            hostnorm[k]=v
    for r in orig_pairs:
        split=cmap[(r['cohort'],r['model_id'],r['case_id'],r['setup_id'],r['split_backend'])]
        full=cmap[('base',r['model_id'],'full',r['setup_id'],r['baseline_backend'])]
        # Preserve product admission: original reader checked model/input/task/preprocessing/endpoint/calibration/window.
        assert r['descriptive_comparable'] is True
        for k in ['task','endpoint_id','physical_scope','window','calibration_sha256']:assert split[k]==full[k],(r['evidence_id'],k)
        assert split['precision']==r['precision'] and full['precision']==r['baseline_runtime_precision']
        assert math.isclose(split['j_per_task_mean']/full['j_per_task_mean'],r['descriptive_energy_ratio'],rel_tol=1e-12)
        jj=[];rates=[]
        for sr in er[split['case_uid']]:
            for fr in er[full['case_uid']]:
                jr=(sr['energy_j']/sr['completed_count'])/(fr['energy_j']/fr['completed_count']);rate=(sr['completed_count']/sr['active_duration_s'])/(fr['completed_count']/fr['active_duration_s']);power=(sr['energy_j']/sr['active_duration_s'])/(fr['energy_j']/fr['active_duration_s'])
                assert math.isclose(jr,power/rate,rel_tol=1e-12)
                jj.append(jr);rates.append(rate)
                repeatpairs.append(dict(evidence_id=r['evidence_id'],split_repetition=sr['repetition'],baseline_repetition=fr['repetition'],energy_ratio=jr,energy_window_rate_ratio=rate,power_ratio=power))
        p=dict(r,split_uid=split['case_uid'],baseline_uid=full['case_uid'],task=split['task'],endpoint_id=split['endpoint_id'],
            input_compatibility_evidence='original_product_descriptive_pair',full_precision=full['precision'],split_accuracy_class=split['accuracy_class'],baseline_accuracy_class=full['accuracy_class'],
            both_reference_close=split['accuracy_class']=='reference_close' and full['accuracy_class']=='reference_close',reference_close_transfer=split['reference_close_transfer'],
            attestor_source_gap=full['attestor_source_gap'],split_energy_fps=split['energy_fps_mean'],baseline_energy_fps=full['energy_fps_mean'],
            split_j_per_task=split['j_per_task_mean'],baseline_j_per_task=full['j_per_task_mean'],split_power_w=split['power_w_mean'],baseline_power_w=full['power_w_mean'],
            split_performance_fps=split['performance_fps'],baseline_performance_fps=full['performance_fps'],
            energy_ratio=split['j_per_task_mean']/full['j_per_task_mean'],energy_window_rate_ratio=split['energy_fps_mean']/full['energy_fps_mean'],power_ratio=split['power_w_mean']/full['power_w_mean'],
            performance_rate_ratio=split['performance_fps']/full['performance_fps'],energy_ratio_pooled=split['j_per_task_pooled']/full['j_per_task_pooled'],energy_ratio_median=split['j_per_task_median']/full['j_per_task_median'],
            energy_ratio_repeat9_min=min(jj),energy_ratio_repeat9_max=max(jj),rate_ratio_repeat9_min=min(rates),rate_ratio_repeat9_max=max(rates),
            energy_change_fraction=split['j_per_task_mean']/full['j_per_task_mean']-1,throughput_change_fraction=split['energy_fps_mean']/full['energy_fps_mean']-1)
        p['ratio_identity_relative_gap']=(p['power_ratio']/p['energy_window_rate_ratio'])/p['energy_ratio']-1
        p['original_report_selected_baseline_j_per_task']=p.pop('baseline_energy_per_work_j')
        p['original_baseline_field_role']='host_normalized_secondary_estimate' if r['cohort']=='base' and r['baseline_kind']=='tensorrt_full' else 'unsubtracted_fs_primary'
        legacy_audit.append(dict(evidence_id=r['evidence_id'],cohort=r['cohort'],baseline_kind=r['baseline_kind'],model_id=r['model_id'],setup_id=r['setup_id'],case_id=r['case_id'],original_baseline_field=r['baseline_energy_per_work_j'],original_baseline_field_role=p['original_baseline_field_role'],actual_raw_fs_baseline_j_per_task=p['baseline_j_per_task'],original_descriptive_ratio=r['descriptive_energy_ratio'],recomputed_raw_fs_ratio=p['energy_ratio'],incorrect_ratio_if_legacy_field_assumed_raw=p['split_j_per_task']/r['baseline_energy_per_work_j']))
        p['log_energy_ratio']=math.log(p['energy_ratio']);p['log_power_ratio']=math.log(p['power_ratio']);p['log_rate_ratio']=math.log(p['energy_window_rate_ratio'])
        if r['baseline_kind']=='tensorrt_full':
            p['secondary_host_normalized_baseline_j_per_task']=hostnorm[(r['model_id'],r['setup_id'],r['baseline_backend'])]
            p['secondary_host_normalized_energy_ratio']=p['split_j_per_task']/p['secondary_host_normalized_baseline_j_per_task']
        pairs.append(p)
        if not r['semantic_comparable']:
            reason=r.get('reason') or ';'.join(r.get('semantic_comparison_reasons') or [])
            limit_kind=('documented_vendor_numerical_negative' if r['model_id']=='yolo26s' and r['setup_id'] in ['H8','H10'] else 'decoder_placement_common_input_unestablished' if 'different_decoder_placement' in reason else 'decoder_nms_identity_evidence_gap')
            limits.append(dict(evidence_id=r['evidence_id'],model_id=r['model_id'],case_id=r['case_id'],setup_id=r['setup_id'],cohort=r['cohort'],baseline_kind=r['baseline_kind'],reason=reason,interpretation=limit_kind,
                semantic_comparable=False,energy_ratio=p['energy_ratio'],energy_window_rate_ratio=p['energy_window_rate_ratio'],baseline_uid=p['baseline_uid'],baseline_numerical_match=r.get('baseline_numerical_match'),baseline_numerical_mean_iou=r.get('baseline_numerical_mean_iou')))
    # Shared baseline dependence is explicit and does not create additional Full observations.
    usage=Counter(p['baseline_uid'] for p in pairs)
    fulls=[dict(c,pair_reuse_count=usage[c['case_uid']]) for c in cases if c['execution_mode']=='native_full_baseline']
    hostrows=[]
    for c in fulls:
        if c['backend']=='native_full_tensorrt':
            est=hostnorm[(c['model_id'],c['setup_id'],c['backend'])]
            hostrows.append(dict(model_id=c['model_id'],setup_id=c['setup_id'],baseline_uid=c['case_uid'],raw_fs_j_per_task=c['j_per_task_mean'],secondary_host_normalized_j_per_task=est,secondary_reduction_fraction=1-est/c['j_per_task_mean'],source='original_base_product_pair_selected_energy_field',role='secondary_host_idle_normalized_estimate_not_primary',attestor_source_gap=True))
    sensitivity=[];groups=[]
    views={'base':lambda r:r['cohort']=='base','augmentation_only':lambda r:r['cohort']=='augmentation','augmented':lambda r:True}
    filters={'descriptive':lambda r:True,'semantic':lambda r:r['semantic_comparable'],'semantic_reference_close':lambda r:r['semantic_comparable'] and r['both_reference_close'],
        'semantic_reference_close_transfer':lambda r:r['semantic_comparable'] and r['both_reference_close'] and r['reference_close_transfer']}
    for view,vf in views.items():
        for filt,ff in filters.items():
            for gap in ['included','excluded']:
                for kind in ['vendor_full','tensorrt_full']:
                    rr=[r for r in pairs if vf(r) and ff(r) and (gap=='included' or not r['attestor_source_gap']) and r['baseline_kind']==kind]
                    sensitivity.append(dict(view=view,filter=filt,attestor_gap=gap,baseline_kind=kind,**joint_summary(rr)))
                    if gap=='excluded':continue
                    gg=defaultdict(list)
                    for r in pairs:
                        if r['baseline_kind']==kind:
                            gk=(r['model_id'],r['setup_id'],r['precision'],r['full_precision'],r['endpoint_id'],r['energy_calibration_sha256'],r['energy_window_effective'])
                            gg[gk]
                            if vf(r) and ff(r):gg[gk].append(r)
                    for key,rrr in sorted(gg.items()):
                        groups.append(dict(view=view,filter=filt,baseline_kind=kind,**dict(zip(('model_id','setup_id','precision','full_precision','endpoint_id','calibration_sha256','window'),key)),**joint_summary(rrr)))
    dominant=[]
    for filt,ff in filters.items():
        for kind in ['vendor_full','tensorrt_full']:
            for omit in [False,True]:
                rr=[r for r in pairs if ff(r) and r['baseline_kind']==kind and not (omit and (r['model_id'],r['setup_id'],r['case_id'])==('yolov7_paper','H8','b066'))]
                dominant.append(dict(view='augmented',filter=filt,baseline_kind=kind,case_sensitivity='exclude_yolov7_H8_b066' if omit else 'all_cases',**joint_summary(rr)))
    # Three distinct close filters avoid silently treating Qualitytransfer as accuracy.
    fronts=[];selections=[];selections_reps=[]
    for view,vf in views.items():
        gs=defaultdict(list)
        for c in cases:
            if c['execution_mode']=='native_split' and vf(c):gs[groupkey(c)].append(c)
        for key,rr in sorted(gs.items()):
            for filt,ff in [('technical',lambda r:True),('reference_close_native',lambda r:r['reference_close_native']),('reference_close_transfer',lambda r:r['reference_close_transfer'])]:
                rr0=[r for r in rr if ff(r)]
                if not rr0:continue
                pp=pareto_flags(rr0);best_rate=winner(rr0,'energy_fps_mean',True);best_energy=winner(rr0,'j_per_task_mean');best_perf=winner(rr0,'performance_fps',True)
                pr=winner(rr0,'energy_fps_pooled',True);pe=winner(rr0,'j_per_task_pooled');mr=winner(rr0,'energy_fps_median',True);me=winner(rr0,'j_per_task_median')
                rates=[];ens=[];coinc=[]
                for i in range(3):
                    rs=[]
                    for c in rr0:
                        rep=next(x for x in er[c['case_uid']] if x['repetition']==i)
                        rs.append(dict(c,energy_fps_mean=rep['completed_count']/rep['active_duration_s'],j_per_task_mean=rep['energy_j']/rep['completed_count']))
                    wr=winner(rs,'energy_fps_mean',True);we=winner(rs,'j_per_task_mean');rates.append(wr['case_id']);ens.append(we['case_id']);coinc.append(wr['case_id']==we['case_id'])
                    selections_reps.append(dict(view=view,filter=filt,**groupbase(rr0[0]),n=len(rr0),repetition=i,fastest_case=wr['case_id'],lowest_energy_case=we['case_id'],winners_coincide=coinc[-1]))
                selections.append(dict(view=view,filter=filt,**groupbase(rr0[0]),n=len(rr0),pareto_n=sum(pp.values()),fastest_case=best_rate['case_id'],lowest_energy_case=best_energy['case_id'],performance_fastest_case=best_perf['case_id'],
                    winners_coincide=best_rate['case_id']==best_energy['case_id'],performance_energy_winners_coincide=best_perf['case_id']==best_energy['case_id'],
                    fastest_energy_fps=best_rate['energy_fps_mean'],fastest_j_per_task=best_rate['j_per_task_mean'],lowest_energy_fps=best_energy['energy_fps_mean'],lowest_j_per_task=best_energy['j_per_task_mean'],
                    energy_penalty_of_fastest_fraction=best_rate['j_per_task_mean']/best_energy['j_per_task_mean']-1,
                    rate_loss_of_energy_winner_fraction=1-best_energy['energy_fps_mean']/best_rate['energy_fps_mean'],
                    performance_winner_energy_penalty_fraction=best_perf['j_per_task_mean']/best_energy['j_per_task_mean']-1,
                    fastest_repetition_cases=rates,energy_repetition_cases=ens,fastest_stable_repeats=sum(x==best_rate['case_id'] for x in rates),energy_stable_repeats=sum(x==best_energy['case_id'] for x in ens),winners_coincide_repeats=sum(coinc),
                    fastest_separated_repeat_ranges=all(best_rate['energy_fps_min']>x['energy_fps_max'] for x in rr0 if x['case_uid']!=best_rate['case_uid']),
                    energy_winner_separated_repeat_ranges=all(best_energy['j_per_task_max']<x['j_per_task_min'] for x in rr0 if x['case_uid']!=best_energy['case_uid']),
                    n_exact_fastest_ties=sum(x['energy_fps_mean']==best_rate['energy_fps_mean'] for x in rr0),n_exact_energy_ties=sum(x['j_per_task_mean']==best_energy['j_per_task_mean'] for x in rr0),
                    pooled_changes_fastest=pr['case_id']!=best_rate['case_id'],pooled_changes_energy_winner=pe['case_id']!=best_energy['case_id'],median_changes_fastest=mr['case_id']!=best_rate['case_id'],median_changes_energy_winner=me['case_id']!=best_energy['case_id'],
                    power_range_min_w=min(r['power_w_mean'] for r in rr0),power_range_max_w=max(r['power_w_mean'] for r in rr0),energy_fps_range_min=min(r['energy_fps_mean'] for r in rr0),energy_fps_range_max=max(r['energy_fps_mean'] for r in rr0),
                    power_max_min_ratio=max(r['power_w_mean'] for r in rr0)/min(r['power_w_mean'] for r in rr0),energy_fps_max_min_ratio=max(r['energy_fps_mean'] for r in rr0)/min(r['energy_fps_mean'] for r in rr0)))
                for c in rr0:
                    fronts.append(dict(view=view,filter=filt,**groupbase(c),case_id=c['case_id'],case_uid=c['case_uid'],cohort=c['cohort'],n=len(rr0),accuracy_class=c['accuracy_class'],pareto=pp[c['case_uid']],
                        energy_fps=c['energy_fps_mean'],j_per_task=c['j_per_task_mean'],power_w=c['power_w_mean'],energy_fps_min=c['energy_fps_min'],energy_fps_max=c['energy_fps_max'],j_per_task_min=c['j_per_task_min'],j_per_task_max=c['j_per_task_max']))
    for name,rows in [('cases',cases),('full_baselines',fulls),('split_full',pairs),('split_full_repeat_sensitivity',repeatpairs),('semantic_limits',limits),('group_distributions',groups),('sensitivity',sensitivity),('pareto',fronts),('selection',selections),('selection_repeats',selections_reps),('host_normalization_secondary',hostrows),('legacy_field_audit',legacy_audit),('recomputed_repeats',recomputed_repeats),('dominant_case_sensitivity',dominant)]:write_csv(T/f'energy_{name}.csv',rows)
    mainselect=[r for r in selections if r['view']=='augmented' and r['filter']=='technical']
    close=[r for r in selections if r['view']=='augmented' and r['filter']=='reference_close_transfer']
    result=dict(schema='thesis20-exploratory-energy-analysis',aggregation='mean_of_three_replicate_ratios',case_n=len(cases),split_n=sum(c['execution_mode']=='native_split' for c in cases),full_n=len(fulls),repeat_n=len(reps),descriptive_pair_n=len(pairs),semantic_pair_n=sum(p['semantic_comparable'] for p in pairs),semantic_limit_n=len(limits),attestor_gap_full_n=sum(c['attestor_source_gap'] for c in fulls),attestor_gap_pair_n=sum(p['attestor_source_gap'] for p in pairs),arithmetic_max_absolute_error=max(checks),max_pooled_j_relative_difference=max(abs(c['pooled_j_relative_difference']) for c in cases),max_mean_identity_relative_gap=max(abs(c['mean_identity_relative_gap']) for c in cases),max_pair_ratio_identity_relative_gap=max(abs(p['ratio_identity_relative_gap']) for p in pairs),
        technical_group_n=len(mainselect),technical_winners_coincide=sum(r['winners_coincide'] for r in mainselect),technical_performance_energy_winners_coincide=sum(r['performance_energy_winners_coincide'] for r in mainselect),technical_fastest_all_reps_stable=sum(r['fastest_stable_repeats']==3 for r in mainselect),technical_energy_all_reps_stable=sum(r['energy_stable_repeats']==3 for r in mainselect),technical_pooled_energy_winner_changes=sum(r['pooled_changes_energy_winner'] for r in mainselect),technical_median_energy_winner_changes=sum(r['median_changes_energy_winner'] for r in mainselect),technical_fastest_separated_repeat_ranges=sum(r['fastest_separated_repeat_ranges'] for r in mainselect),technical_energy_separated_repeat_ranges=sum(r['energy_winner_separated_repeat_ranges'] for r in mainselect),secondary_host_normalization_n=len(hostrows),secondary_host_normalized_energy_saving_pair_n=sum(r.get('secondary_host_normalized_energy_ratio',float('inf'))<1 for r in pairs),legacy_mixed_baseline_field_rows=sum(r['original_baseline_field_role']=='host_normalized_secondary_estimate' for r in legacy_audit),reference_close_transfer_group_n=len(close),reference_close_transfer_winners_coincide=sum(r['winners_coincide'] for r in close),
        primary_summaries=[r for r in sensitivity if r['view']=='augmented' and r['attestor_gap']=='included'],limitations=['post_hoc_development_screening','shared_full_baselines_not_independent_pairs','three_repeats_not_thousands_independent_tasks','no_controlled_runtime_thread_temperature_time_equivalence','21_trt_full_historical_attestor_source_gaps','full_execution_precision_differs_from_split_boundary_precision','no_generic_energy_measured','same_index_repetitions_not_synchronized_trials','input_equality_inherited_from_original_product_pair_projection'])
    (output/'energy_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='primary_summaries'},indent=2))
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--source-root',required=True,type=Path);parser.add_argument('--output-root',required=True,type=Path)
    a=parser.parse_args();analyze(a.source_root.resolve(),a.output_root.resolve())
