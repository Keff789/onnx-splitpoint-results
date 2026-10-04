"""Offline derived quality, coverage and graph associations; no new quality tests."""
import argparse,csv,json,math,statistics,sys
from collections import Counter,defaultdict
from pathlib import Path

def changes(candidate,reference):
    if reference<=0: return 100*(candidate-reference),None
    return 100*(candidate-reference),100*(candidate/reference-1)
def unique_index(rows,fields):
    out={}
    for row in rows:
        key=tuple(row[f] for f in fields)
        if key in out: raise ValueError(f'Duplicate identity: {key}')
        out[key]=row
    return out
def main():
    p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);a=p.parse_args()
    sys.path.insert(0,str(a.source_root/'scripts'))
    from extract_inputs import csvread,csvwrite,write
    from project_rank_metrics import _spearman
    I=a.source_root/'inputs'; O=a.output_root;T=O/'tables';T.mkdir(parents=True,exist_ok=True)
    q=csvread(I/'quality.csv'); details=unique_index(csvread(O/'inputs/quality_policy_details.csv'),['quality_id'])
    graph=unique_index(csvread(O/'inputs/graph_features.csv'),['model_id','case_id'])
    rows=[]
    for r in q:
        d=details[(r['quality_id'],)]
        for k in ['cohort','model_id','case_id','setup_id','backend','variant','metric']:assert r[k]==d[k]
        pp,rel=changes(r['candidate'],r['reference'])
        assert math.isclose(pp,100*r['delta'],abs_tol=1e-8)
        assert math.isclose(rel,-100*r['relative_loss'],abs_tol=1e-8)
        ci_low=d['relative_loss_ci_low'];ci_high=d['relative_loss_ci_high']
        row=dict(r,**{k:v for k,v in d.items() if k not in r},delta_pp=pp,relative_change_pct=rel,delta_ci_low_pp=100*r['ci_low'],delta_ci_high_pp=100*r['ci_high'],relative_ci_crosses_original_threshold=(ci_low<=d['relative_loss_threshold']<=ci_high) if ci_low is not None else None)
        g=graph.get((r['model_id'],r['case_id'])) if r['variant']=='split' else None
        row['graph_feature_available']=g is not None
        if g:row.update({k:v for k,v in g.items() if k not in row})
        rows.append(row)
    csvwrite(T/'quality_effects.csv',rows);csvwrite(T/'quality_losses.csv',[r for r in rows if r['accuracy_class']=='accuracy_loss'])
    groups=defaultdict(list)
    for r in rows:groups[(r['cohort'],r['model_id'],r['setup_id'],r['backend'],r['variant'],r['metric'])].append(r)
    summaries=[]
    for key,rs in sorted(groups.items()):
        summaries.append(dict(zip(['cohort','model_id','setup_id','backend','variant','metric'],key),n=len(rs),loss_count=sum(r['accuracy_class']=='accuracy_loss' for r in rs),delta_pp_min=min(r['delta_pp'] for r in rs),delta_pp_median=statistics.median(r['delta_pp'] for r in rs),delta_pp_max=max(r['delta_pp'] for r in rs),relative_loss_pct_max=max(100*r['relative_loss'] for r in rs),ci_crosses_reporting_threshold=sum(r['relative_ci_crosses_original_threshold'] is True for r in rs)))
    csvwrite(T/'quality_group_summary.csv',summaries)
    coverage=csvread(I/'coverage.csv');native=csvread(I/'native_cases.csv');energy=csvread(I/'energy_cases.csv');pairs=csvread(I/'completion_pairs.csv');unsupported=csvread(O/'inputs/native_unsupported.csv')
    # A saved Vendor-Full companion can carry a boundary-like case_id. The
    # quality variant is therefore mandatory, never inferred from case_id.
    split_quality=unique_index([r for r in q if r['variant']=='split'],['cohort','model_id','case_id','setup_id','backend'])
    aliases={'hailo10':'hailo10h','deepx_m1':'deepx'}
    join_audit=[]
    for r in pairs:
        backend=aliases.get(r['comparison_backend'],r['comparison_backend'])
        k=(r['observation_origin'],r['model_id'],r['case_id'],r['setup_id'],backend)
        quality=split_quality[k]
        assert quality['accuracy_class']==r['generic_task_quality_status']==r['native_task_quality_status'],k
        join_audit.append(dict(model_id=r['model_id'],case_id=r['case_id'],setup_id=r['setup_id'],cohort=r['observation_origin'],comparison_backend=r['comparison_backend'],quality_id=quality['quality_id'],quality_variant=quality['variant'],accuracy_class=quality['accuracy_class'],relative_loss=quality['relative_loss'],pair_generic_status=r['generic_task_quality_status'],pair_native_status=r['native_task_quality_status']))
    csvwrite(T/'quality_pair_join_audit.csv',join_audit)
    matrix=[]
    for m,s in sorted({(r['model_id'],r['setup_id']) for r in pairs}):
        select=lambda rr:[r for r in rr if r['model_id']==m and r['setup_id']==s]
        cc=select(coverage);nn=select(native);ee=select(energy);qq=select(q);gg=select(pairs);uu=select(unsupported)
        row=dict(model_id=m,setup_id=s,generic_required=len(cc),generic_measured=sum(r['raw_representation']=='present' for r in cc),native_base_split=sum(r['cohort']=='base' and r['execution_mode']=='split' for r in nn),native_added_split=sum(r['cohort']=='augmentation' for r in nn),native_full=sum(r['execution_mode']=='full' for r in nn),native_unsupported=len(uu),completed_base=sum(r['observation_origin']=='base' for r in gg),completed_added=sum(r['observation_origin']=='augmentation' for r in gg),quality_total=len(qq),quality_added=sum(r['cohort']=='augmentation' for r in qq),quality_loss=sum(r['accuracy_class']=='accuracy_loss' for r in qq),energy_cases=len(ee),energy_repeats=sum(r['valid_repeats'] for r in ee))
        row.update({'generic_status_'+k:v for k,v in Counter(r['status'] for r in cc).items()});matrix.append(row)
    csvwrite(T/'coverage_matrix.csv',matrix)
    technical=[]
    for r in coverage:
        g=graph.get((r['model_id'],r['case_id']))
        technical.append(dict(r,**({k:v for k,v in g.items() if k not in r} if g else {}),graph_feature_available=g is not None))
    csvwrite(T/'coverage_graph_cases.csv',technical)
    feature_rows=[]
    for r in pairs:
        g=graph.get((r['model_id'],r['case_id']))
        feature_rows.append(dict(r,**({k:v for k,v in g.items() if k not in r} if g else {}),graph_feature_available=g is not None))
    csvwrite(T/'graph_completed_cases.csv',feature_rows)
    correlations=[]
    features=['topological_position','cut_bytes','n_cut_tensors','part2_input_count','stored_flops_left_ratio','stored_predicted_stream_fps','stored_predicted_bottleneck_ms']
    for population,data,groupfields,targets in [('completed',feature_rows,['model_id','setup_id','direction','precision','output_endpoint_id','boundary_class'],['native_completed_task_fps','generic_completed_task_fps','native_over_generic_completed_task_ratio']),('quality_split',[r for r in rows if r['variant']=='split'],['model_id','setup_id','backend','metric'],['delta_pp'])]:
        for view in ['base','augmented']:
            groups=defaultdict(list)
            for r in data:
                if view=='base' and (r.get('cohort') or r.get('observation_origin'))!='base':continue
                groups[tuple(r[k] for k in groupfields)].append(r)
            for key,rs in sorted(groups.items()):
                for feature in features:
                    for target in targets:
                        ok=[r for r in rs if isinstance(r.get(feature),(float,int)) and isinstance(r.get(target),(float,int))]
                        rho=_spearman([r[feature] for r in ok],[r[target] for r in ok]) if len(ok)>=3 else None
                        correlations.append(dict(population=population,view=view,**dict(zip(groupfields,key)),feature=feature,target=target,n=len(ok),n_missing=len(rs)-len(ok),distinct_feature_values=len({r[feature] for r in ok}),rho=rho,interpretation='exploratory_within_group_no_causal_or_predictive_validation'))
    csvwrite(T/'graph_associations.csv',correlations)
    summary=dict(quality_n=len(rows),quality_loss_n=sum(r['accuracy_class']=='accuracy_loss' for r in rows),loss_by_metric=dict(Counter(r['metric'] for r in rows if r['accuracy_class']=='accuracy_loss')),loss_by_model=dict(Counter(r['model_id'] for r in rows if r['accuracy_class']=='accuracy_loss')),uncertainty_all=dict(Counter(r['uncertainty'] for r in rows)),loss_uncertainty=dict(Counter(r['uncertainty'] for r in rows if r['accuracy_class']=='accuracy_loss')),ci_crosses_threshold=sum(r['relative_ci_crosses_original_threshold'] is True for r in rows),quality_graph_joined=sum(r['graph_feature_available'] for r in rows),completed_graph_joined=sum(r['graph_feature_available'] for r in feature_rows),native_unsupported=len(unsupported),unsupported_reasons=dict(Counter(r['reason'] for r in unsupported)),coverage_status=dict(Counter(r['status'] for r in coverage)),original_absolute_margins=sorted({r['original_absolute_margin'] for r in rows}),original_relative_thresholds=sorted({r['relative_loss_threshold'] for r in rows}))
    summary.update(loss_by_variant=dict(Counter(r['variant'] for r in rows if r['accuracy_class']=='accuracy_loss')),paired_quality_classes=dict(Counter(r['accuracy_class'] for r in join_audit)))
    write(O/'quality_graph_results.json',summary);print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
