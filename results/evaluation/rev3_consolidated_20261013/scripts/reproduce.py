#!/usr/bin/env python3
"""Deterministic offline analysis of frozen compact Revision-3 inputs."""
import argparse, collections, csv, hashlib, json, math, statistics, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from legacy_energy_methods import quantile

def read(p):return json.loads(p.read_text())
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,sort_keys=True,allow_nan=False)+'\n')
def table(p,rs):
 p.parent.mkdir(parents=True,exist_ok=True);fields=list(dict.fromkeys(k for r in rs for k in r)) or ['empty']
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fields,lineterminator='\n');w.writeheader()
  for r in rs:w.writerow({k:json.dumps(v,sort_keys=True) if isinstance(v,(dict,list,tuple)) else v for k,v in r.items()})
def grouped(rs,keys):
 g=collections.defaultdict(list)
 for r in rs:g[tuple(r[k] for k in keys)].append(r)
 return sorted(g.items(),key=lambda x:str(x[0]))
def dist(v,prefix):
 v=[x for x in v if x is not None]
 return {prefix+'_'+n:quantile(v,q) for n,q in [('min',0),('q25',.25),('median',.5),('q75',.75),('max',1)]}
def mean(v):return statistics.mean(v) if v else None
def ci(v):
 if len(v)!=3:return [None,None]
 m=statistics.mean(v);h=4.302652729749461*statistics.stdev(v)/math.sqrt(3);return [m-h,m+h]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--inputs',type=Path,default=Path(__file__).resolve().parents[1]/'inputs');ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();I,O=a.inputs,a.output
 assert not O.exists() or not any(O.iterdir()),'Use a fresh output directory'
 O.mkdir(parents=True,exist_ok=True);T=O/'tables'
 for name,h in read(I/'MANIFEST.json').items():assert hashlib.sha256((I/name).read_bytes()).hexdigest()==h,('input changed',name)
 C=read(I/'cases.json');M={r['uid']:r for r in C};ER=read(I/'energy_repeats.json');P=read(I/'split_full_contracts.json');R=collections.defaultdict(list)
 for r in ER:R[r['uid']].append(r)
 assert len(M)==len(C)==450
 coverage=[]
 for k,rs in grouped(C,['model_id','setup_id','runner','kind']):
  coverage.append(dict(zip(['model','setup','runner','kind'],k),rows=len(rs),performance_observations=sum(r['performance_observations'] for r in rs),normal_quality=sum(r['normal_quality'] for r in rs),reference_close=sum(r['quality_class']=='reference_close' for r in rs),accuracy_loss=sum(r['quality_class']=='accuracy_loss' for r in rs),normal_performance_claim=sum(r['normal_performance_claim'] for r in rs),normal_energy=sum(r['normal_energy'] for r in rs),missing_energy=sum(not r['normal_energy'] for r in rs)))
 table(T/'coverage.csv',coverage);table(T/'all_cases.csv',C)
 boundaries=[r for r in C if not r['normal_energy']];table(T/'boundary_cases.csv',boundaries)
 table(T/'negative_quality.csv',[r for r in C if r['quality_class']=='accuracy_loss'])
 uncertainty=[]
 for c in C:
  rr=R[c['uid']];vs=[r['j_per_task'] for r in rr];fs=c['fps_samples'];q=ci(vs)
  if vs:
   assert math.isclose(mean(vs),c['raw_j_per_task'],rel_tol=1e-10)
   if c['energy_ci']:assert all(math.isclose(v,w,rel_tol=1e-9,abs_tol=1e-12) for v,w in zip(q,c['energy_ci']))
  uncertainty.append({'uid':c['uid'],'n_performance':c['performance_observations'],'stored_fps':c['fps'],'fps_min':min(fs) if fs else None,'fps_max':max(fs) if fs else None,'fps_cv':statistics.stdev(fs)/mean(fs) if len(fs)>1 else None,'n_energy':len(rr),'mean_E_over_N':mean(vs),'mean_N_over_E':mean([r['tasks_per_j'] for r in rr]),'reciprocal_mean_E_over_N':1/mean(vs) if vs else None,'sum_N_over_sum_E':sum(r['completed_tasks'] for r in rr)/sum(r['energy_j'] for r in rr) if rr else None,'energy_mean_ci95_low':q[0],'energy_mean_ci95_high':q[1],'energy_cv':statistics.stdev(vs)/mean(vs) if len(vs)>1 else None,'energy_independence_unit':'sensor_repeat','fps_independence_unit':'process' if fs else 'historical_single'})
 table(T/'repeat_uncertainty.csv',uncertainty)
 ng=[]
 for b in read(I/'native_generic_bindings.json'):
  n,g=M[b['native_uid']],M[b['generic_uid']];assert all(b['technical_gates'].values());assert n['performance_source_sha256']==b['native_summary_sha256']
  fps=n['fps']/g['fps'];assert math.isclose(fps,b['stored_fps_ratio'],rel_tol=1e-12)
  energy=n['normal_energy'] and g['normal_energy']
  if energy:assert (n['calibration_sha256'],n['energy_scope'],n['energy_window'])==(g['calibration_sha256'],g['energy_scope'],g['energy_window'])
  nr,gr=R[n['uid']],R[g['uid']]
  ng.append({'model':n['model_id'],'setup':n['setup_id'],'case':n['case_id'],'native_uid':n['uid'],'generic_uid':g['uid'],'administrative_quality_receipt_gap':n['administrative_quality_receipt_gap'] or g['administrative_quality_receipt_gap'],'performance_admitted':n['normal_performance_claim'] and g['normal_performance_claim'],'native_fps':n['fps'],'generic_fps':g['fps'],'fps_ratio':fps,'both_reference_close':n['quality_class']==g['quality_class']=='reference_close','energy_admitted':energy,'native_raw_mj':1000*n['raw_j_per_task'] if energy else None,'generic_raw_mj':1000*g['raw_j_per_task'] if energy else None,'energy_ratio':n['raw_j_per_task']/g['raw_j_per_task'] if energy else None,'fps_repeat_ratio_min':min(x/y for x in n['fps_samples'] for y in g['fps_samples']),'fps_repeat_ratio_max':max(x/y for x in n['fps_samples'] for y in g['fps_samples']),'energy_repeat_ratio_min':min(x['j_per_task']/y['j_per_task'] for x in nr for y in gr) if energy else None,'energy_repeat_ratio_max':max(x['j_per_task']/y['j_per_task'] for x in nr for y in gr) if energy else None})
 table(T/'native_generic_pairs.csv',ng)
 def comparison_summary(rs):
  pf=[r for r in rs if r.get('performance_admitted',True)];en=[r for r in rs if r.get('energy_admitted',True)]
  joint=[r for r in pf if r in en]
  return {'n_pairs':len(rs),'n_performance':len(pf),'n_energy':len(en),'n_joint':len(joint),'faster':sum(r['fps_ratio']>1 for r in pf),'energy_lower':sum(r['energy_ratio']<1 for r in en),'both_better':sum(r['fps_ratio']>1 and r['energy_ratio']<1 for r in joint),**dist([r['fps_ratio'] for r in pf],'fps_ratio'),**dist([r['energy_ratio'] for r in en],'energy_ratio')}
 ngsum=[]
 for k,rs in grouped(ng,['model','setup']):ngsum.append(dict(zip(['model','setup'],k),**comparison_summary(rs)))
 table(T/'native_generic_groups.csv',ngsum)
 full=[]
 for p in P:
  n=M[p['split_uid']];b=M.get(p['baseline_uid']);semantic=p['semantic_comparable'] is True;claim=p['claim_comparable'] is True;energy=semantic and claim and b is not None and n['normal_energy'] and b['normal_energy'];perf=energy and n['normal_performance_claim'] and b['normal_performance_claim']
  reasons=p['comparison_reasons']+p['semantic_comparison_reasons']
  if energy:
   assert math.isclose(p['split_energy_per_work_j'],n['comparison_j_per_task'],rel_tol=1e-10)
   assert math.isclose(p['baseline_energy_per_work_j'],b['comparison_j_per_task'],rel_tol=1e-10)
  rr={'model':n['model_id'],'setup':n['setup_id'],'case':n['case_id'],'split_uid':n['uid'],'baseline_uid':p['baseline_uid'],'administrative_quality_receipt_gap':n['administrative_quality_receipt_gap'] or bool(b and b['administrative_quality_receipt_gap']),'baseline_kind':p['baseline_kind'],'baseline_backend':p['baseline_backend'],'source_claim_flag':claim,'semantic_comparable':semantic,'energy_admitted':energy,'performance_admitted':perf,'exclusions':reasons,'both_reference_close':bool(b and n['quality_class']==b['quality_class']=='reference_close'),'split_fps':n['fps'],'baseline_fps':b['fps'] if b else None,'baseline_performance_n':b['performance_observations'] if b else None,'fps_ratio':n['fps']/b['fps'] if perf else None,'descriptive_fps_ratio':n['fps']/b['fps'] if b else None,'split_raw_mj':1000*n['raw_j_per_task'] if n['raw_j_per_task'] is not None else None,'baseline_raw_mj':1000*b['raw_j_per_task'] if b and b['raw_j_per_task'] is not None else None,'split_comparison_mj':1000*n['comparison_j_per_task'] if n['comparison_j_per_task'] is not None else None,'baseline_comparison_mj':1000*b['comparison_j_per_task'] if b and b['comparison_j_per_task'] is not None else None,'baseline_energy_basis':p['baseline_energy_comparison_basis'],'energy_ratio':n['comparison_j_per_task']/b['comparison_j_per_task'] if energy else None,'raw_energy_ratio':n['raw_j_per_task']/b['raw_j_per_task'] if energy else None}
  if energy:
   rr['energy_repeat_ratio_min']=min(x['comparison_j_per_task']/y['comparison_j_per_task'] for x in R[n['uid']] for y in R[b['uid']]);rr['energy_repeat_ratio_max']=max(x['comparison_j_per_task']/y['comparison_j_per_task'] for x in R[n['uid']] for y in R[b['uid']])
  full.append(rr)
 table(T/'split_full_pairs.csv',full);table(T/'excluded_full_pairs.csv',[r for r in full if not r['energy_admitted']])
 fs=[]
 for k,rs in grouped(full,['model','setup','baseline_kind']):fs.append(dict(zip(['model','setup','baseline_kind'],k),**comparison_summary(rs)))
 table(T/'split_full_groups.csv',fs)
 # Baseline selection is metric-specific, and only from admissible pairs for that split.
 choices=[]
 for k,rs in grouped(full,['split_uid']):
  p=[r for r in rs if r['performance_admitted']];e=[r for r in rs if r['energy_admitted']]
  fast=max(p,key=lambda r:(r['baseline_fps'],r['baseline_uid'])) if p else None;low=min(e,key=lambda r:(r['baseline_comparison_mj'],r['baseline_uid'])) if e else None
  r=rs[0];choices.append({'split_uid':k[0],'model':r['model'],'setup':r['setup'],'case':r['case'],'fastest_admitted_full':fast['baseline_backend'] if fast else None,'fastest_full_fps':fast['baseline_fps'] if fast else None,'speedup_vs_fastest_full':fast['fps_ratio'] if fast else None,'lowest_energy_admitted_full':low['baseline_backend'] if low else None,'lowest_full_comparison_mj':low['baseline_comparison_mj'] if low else None,'energy_ratio_vs_lowest_full':low['energy_ratio'] if low else None,'performance_candidates':len(p),'energy_candidates':len(e)})
 present={r['split_uid'] for r in choices}
 for r in C:
  if r['runner']=='native' and r['kind']=='split' and r['uid'] not in present:
   choices.append({'split_uid':r['uid'],'model':r['model_id'],'setup':r['setup_id'],'case':r['case_id'],'fastest_admitted_full':None,'fastest_full_fps':None,'speedup_vs_fastest_full':None,'lowest_energy_admitted_full':None,'lowest_full_comparison_mj':None,'energy_ratio_vs_lowest_full':None,'performance_candidates':0,'energy_candidates':0,'exclusion':'no_archived_full_pair_contract'})
 choices.sort(key=lambda r:r['split_uid'])
 assert len(choices)==204
 table(T/'baseline_selection.csv',choices)
 winners=[]
 for k,rs in grouped(choices,['model','setup']):
  ps=[r for r in rs if r['speedup_vs_fastest_full'] is not None];es=[r for r in rs if r['energy_ratio_vs_lowest_full'] is not None];sp=max(ps,key=lambda r:(M[r['split_uid']]['fps'],r['case'])) if ps else None;ep=min(es,key=lambda r:(M[r['split_uid']]['comparison_j_per_task'],r['case'])) if es else None
  winners.append({'model':k[0],'setup':k[1],'performance_splits':len(ps),'energy_splits':len(es),'faster_than_fastest_full':sum(r['speedup_vs_fastest_full']>1 for r in ps),'lower_than_lowest_energy_full':sum(r['energy_ratio_vs_lowest_full']<1 for r in es),'posthoc_fastest_split':sp['case'] if sp else None,'posthoc_fastest_split_fps':M[sp['split_uid']]['fps'] if sp else None,'speedup_vs_fastest_full':sp['speedup_vs_fastest_full'] if sp else None,'fastest_full_name':sp['fastest_admitted_full'] if sp else None,'posthoc_min_energy_split':ep['case'] if ep else None,'min_split_mj':1000*M[ep['split_uid']]['comparison_j_per_task'] if ep else None,'energy_ratio_vs_min_full':ep['energy_ratio_vs_lowest_full'] if ep else None,'min_energy_full_name':ep['lowest_energy_admitted_full'] if ep else None,'speed_and_energy_split_same':sp['case']==ep['case'] if sp and ep else None})
 table(T/'model_setup_optima.csv',winners)
 tops=[]
 for metric in ['speedup_vs_fastest_full','energy_ratio_vs_lowest_full']:
  v=[r for r in choices if r[metric] is not None]
  for order in ['min','max']:
   for rank,r in enumerate(sorted(v,key=lambda r:r[metric],reverse=order=='max')[:10],1):tops.append(dict(r,metric=metric,extreme=order,rank=rank))
 table(T/'top_worst_splits.csv',tops)
 # Robustness: keep all admitted accuracy-loss rows, then explicit reference-close sensitivity.
 robust=[]
 for population in ['all_admitted','both_reference_close','exclude_administrative_receipt_gaps']:
  ns=[r for r in ng if population=='all_admitted' or (population=='both_reference_close' and r['both_reference_close']) or (population=='exclude_administrative_receipt_gaps' and not r['administrative_quality_receipt_gap'])]
  robust.append(dict(comparison='native_generic',quality_filter=population,energy_basis='raw',**comparison_summary(ns)))
  for kind in ['all_full','tensorrt_full','vendor_full']:
   for basis in ['comparison','raw']:
    rs=[dict(r) for r in full if (population=='all_admitted' or (population=='both_reference_close' and r['both_reference_close']) or (population=='exclude_administrative_receipt_gaps' and not r['administrative_quality_receipt_gap'])) and (kind=='all_full' or r['baseline_kind']==kind)]
    if basis=='raw':
     for r in rs:r['energy_ratio']=r['raw_energy_ratio']
    robust.append(dict(comparison=kind,quality_filter=population,energy_basis=basis,**comparison_summary(rs)))
 table(T/'sensitivity.csv',robust)
 # Re-select metric-specific baselines under each quality/provenance/energy sensitivity.
 selection_sensitivity=[];selection_summary=[];basechoices={r['split_uid']:r for r in choices}
 for population in ['all_admitted','both_reference_close','exclude_administrative_receipt_gaps']:
  for basis in ['comparison','raw']:
   selected=[]
   for k,rs0 in grouped(full,['split_uid']):
    rs=[r for r in rs0 if population=='all_admitted' or (population=='both_reference_close' and r['both_reference_close']) or (population=='exclude_administrative_receipt_gaps' and not r['administrative_quality_receipt_gap'])]
    pr=[r for r in rs if r['performance_admitted']];er=[r for r in rs if r['energy_admitted']]
    fast=max(pr,key=lambda r:(r['baseline_fps'],r['baseline_uid'])) if pr else None
    energyfield='baseline_comparison_mj' if basis=='comparison' else 'baseline_raw_mj';ratiofield='energy_ratio' if basis=='comparison' else 'raw_energy_ratio'
    low=min(er,key=lambda r:(r[energyfield],r['baseline_uid'])) if er else None;b=basechoices[k[0]]
    row={'split_uid':k[0],'model':b['model'],'setup':b['setup'],'case':b['case'],'quality_filter':population,'energy_basis':basis,'fastest_full':fast['baseline_backend'] if fast else None,'speedup':fast['fps_ratio'] if fast else None,'lowest_energy_full':low['baseline_backend'] if low else None,'energy_ratio':low[ratiofield] if low else None,'fastest_baseline_changed':bool(fast and fast['baseline_backend']!=b['fastest_admitted_full']),'lowest_energy_baseline_changed':bool(low and low['baseline_backend']!=b['lowest_energy_admitted_full']),'speed_direction_changed':bool(fast and b['speedup_vs_fastest_full'] is not None and (fast['fps_ratio']>1)!=(b['speedup_vs_fastest_full']>1)),'energy_direction_changed':bool(low and b['energy_ratio_vs_lowest_full'] is not None and (low[ratiofield]<1)!=(b['energy_ratio_vs_lowest_full']<1))}
    selected.append(row)
   # Include splits with no archived pair contract under every sensitivity.
   known={r['split_uid'] for r in selected}
   for b in choices:
    if b['split_uid'] not in known:selected.append({'split_uid':b['split_uid'],'model':b['model'],'setup':b['setup'],'case':b['case'],'quality_filter':population,'energy_basis':basis,'fastest_full':None,'speedup':None,'lowest_energy_full':None,'energy_ratio':None,'fastest_baseline_changed':False,'lowest_energy_baseline_changed':False,'speed_direction_changed':False,'energy_direction_changed':False})
   selection_sensitivity.extend(selected);pr=[r for r in selected if r['speedup'] is not None];er=[r for r in selected if r['energy_ratio'] is not None]
   selection_summary.append({'quality_filter':population,'energy_basis':basis,'splits':len(selected),'n_performance':len(pr),'faster_than_fastest_full':sum(r['speedup']>1 for r in pr),'n_energy':len(er),'lower_than_min_full':sum(r['energy_ratio']<1 for r in er),'fastest_baseline_changes':sum(r['fastest_baseline_changed'] for r in selected),'lowest_energy_baseline_changes':sum(r['lowest_energy_baseline_changed'] for r in selected),'speed_direction_changes':sum(r['speed_direction_changed'] for r in selected),'energy_direction_changes':sum(r['energy_direction_changed'] for r in selected)})
 table(T/'baseline_selection_sensitivity.csv',selection_sensitivity);table(T/'baseline_sensitivity_summary.csv',selection_summary)
 sensitivity_optima=[]
 for k,rs in grouped(selection_sensitivity,['quality_filter','energy_basis','model','setup']):
  pr=[r for r in rs if r['speedup'] is not None];er=[r for r in rs if r['energy_ratio'] is not None];metric='comparison_j_per_task' if k[1]=='comparison' else 'raw_j_per_task'
  fast=max(pr,key=lambda r:(M[r['split_uid']]['fps'],r['case'])) if pr else None;low=min(er,key=lambda r:(M[r['split_uid']][metric],r['case'])) if er else None
  sensitivity_optima.append({'quality_filter':k[0],'energy_basis':k[1],'model':k[2],'setup':k[3],'n_performance':len(pr),'n_energy':len(er),'fastest_split':fast['case'] if fast else None,'fastest_full':fast['fastest_full'] if fast else None,'speedup':fast['speedup'] if fast else None,'lowest_energy_split':low['case'] if low else None,'lowest_energy_full':low['lowest_energy_full'] if low else None,'energy_ratio':low['energy_ratio'] if low else None})
 table(T/'model_setup_sensitivity_optima.csv',sensitivity_optima)

 # Pareto sets for same-runner split cohorts, exact scientific contract fields; no cross-setup domination.
 pareto=[];cohortfields=['model_id','setup_id','runner','comparison_endpoint','contract_preprocessing','contract_decoder','contract_nms','prepared_image_sha256','calibration_sha256','backend','precision','measurement_boundary','energy_scope','energy_window','completion_mode','completion_contract_sha256','scheduling']
 for pop in ['all_admitted','reference_close']:
  cand=[r for r in C if r['kind']=='split' and r['normal_performance_claim'] and r['normal_energy'] and r['comparison_endpoint'] and r['prepared_image_sha256'] and (pop=='all_admitted' or r['quality_class']=='reference_close')]
  for k,rs in grouped(cand,cohortfields):
   gid=hashlib.sha256(json.dumps(k).encode()).hexdigest()[:16]
   for r in rs:
    dominates=[x['uid'] for x in rs if x['fps']>=r['fps'] and x['raw_j_per_task']<=r['raw_j_per_task'] and (x['fps']>r['fps'] or x['raw_j_per_task']<r['raw_j_per_task'])]
    pareto.append({'uid':r['uid'],'model':r['model_id'],'setup':r['setup_id'],'runner':r['runner'],'quality_filter':pop,'cohort':gid,'cohort_n':len(rs),'fps':r['fps'],'raw_mj':1000*r['raw_j_per_task'],'pareto':not dominates,'dominated_by':dominates})
 table(T/'pareto.csv',pareto)
 # Graph associations remain within each model/setup/runner and use SHA-bound model features.
 from scipy.stats import spearmanr
 graph={(r['model_id'],r['case_id']):r for r in read(I/'graph_features.json')};associations=[]
 for k,rs in grouped([r for r in C if r['kind']=='split'],['model_id','setup_id','runner']):
  for feature in ['topological_position','cut_bytes','n_cut_tensors','part2_input_count','flops_left_ratio']:
   for metric in ['fps','raw_j_per_task']:
    ds=[(graph[(r['model_id'],r['case_id'])].get(feature),r[metric]) for r in rs if (r['model_id'],r['case_id']) in graph and (metric=='fps' or r['normal_energy'])];ds=[d for d in ds if d[0] is not None and d[1] is not None]
    rho=float(spearmanr([x for x,y in ds],[y for x,y in ds])[0]) if len(ds)>=3 and len({x for x,y in ds})>1 and len({y for x,y in ds})>1 else None
    associations.append({'model':k[0],'setup':k[1],'runner':k[2],'feature':feature,'metric':metric,'n':len(ds),'spearman_rho':rho,'interpretation':'exploratory_within_group_not_causal'})
 table(T/'graph_associations.csv',associations)
 pipeline=read(I/'pipeline_repeats.json');ps=[]
 for k,rs in grouped(pipeline,['model_id','setup_id','task','producer_impl','kind']):
  d={'model':k[0],'setup':k[1],'task':k[2],'producer_impl':k[3],'kind':k[4],'process_repeats':len(rs),'cases':len({r['uid'] for r in rs})}
  for f in ['p1_thread_ms','p2_thread_ms','p2_run_ms','completion_tail_ms','handoff_ms','trt_input_copy_ms','p1_effective_cycle_ms','queue_wait_ms']:
   vals=[r[f] for r in rs if isinstance(r.get(f),(int,float))];d[f+'_n']=len(vals);d[f+'_median']=statistics.median(vals) if vals else None
  ps.append(d)
 table(T/'pipeline_summary.csv',ps);table(T/'pipeline_repeats.csv',pipeline)
 diag=read(I/'diagnostic_acceptance.json');d=diag['metrics'];h=diag['historical_baseline_context'];diagnostic={'fps_single':d['fps_display'],'historical_fps_median':h['historical_fps'],'fps_relative_change':d['fps_display']/h['historical_fps']-1,'energy_single_j_per_task':d['energy']['energy_per_completed_task_j'],'historical_mean_j_per_task':h['historical_energy_per_task_j'],'energy_relative_change':d['energy']['energy_per_completed_task_j']/h['historical_energy_per_task_j']-1,'scope':'separate_diagnostic_single_no_generalization_or_CI_test'}
 write(O/'diagnostic_result.json',diagnostic)
 speedchoices=[r for r in choices if r['speedup_vs_fastest_full'] is not None];energychoices=[r for r in choices if r['energy_ratio_vs_lowest_full'] is not None]
 summary={'cases':len(C),'native':sum(c['runner']=='native' for c in C),'generic':sum(c['runner']=='generic' for c in C),'normal_energy':sum(c['normal_energy'] for c in C),'boundaries':len(boundaries),'quality_loss':dict(collections.Counter(c['runner'] for c in C if c['quality_class']=='accuracy_loss')),'admitted_quality_loss':dict(collections.Counter(c['runner'] for c in C if c['quality_class']=='accuracy_loss' and c['normal_performance_claim'] and c['normal_energy'])),'native_generic':comparison_summary(ng),'full_pair_gates':{'total':len(P),'claim_flag':sum(p['claim_comparable'] for p in P),'semantic_and_claim':sum(p['claim_comparable'] and p['semantic_comparable'] for p in P),'claim_but_not_semantic':sum(p['claim_comparable'] and not p['semantic_comparable'] for p in P),'energy_admitted':sum(r['energy_admitted'] for r in full),'performance_admitted':sum(r['performance_admitted'] for r in full)},'fastest_full_comparison':{'splits':len(speedchoices),'faster':sum(r['speedup_vs_fastest_full']>1 for r in speedchoices),**dist([r['speedup_vs_fastest_full'] for r in speedchoices],'speedup')},'lowest_full_energy_comparison':{'splits':len(energychoices),'lower':sum(r['energy_ratio_vs_lowest_full']<1 for r in energychoices),**dist([r['energy_ratio_vs_lowest_full'] for r in energychoices],'ratio')},'normalization_direction_changes':sum(r['energy_admitted'] and ((r['energy_ratio']<1)!=(r['raw_energy_ratio']<1)) for r in full),'pipeline_rows':len(pipeline),'pipeline_missing':len(read(I/'pipeline_missing.json')),'administrative_quality_receipt_gaps_native':sum(c['administrative_quality_receipt_gap'] for c in C if c['runner']=='native'),'posthoc_only':True,'diagnostic':diagnostic}
 write(O/'summary.json',summary)
 render(O,C,ng,choices,winners,pareto,ps)
 report(O,summary,winners,robust,associations,ng,choices,ps,selection_summary)
 files={str(p.relative_to(O)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(O.rglob('*')) if p.is_file()};write(O/'OUTPUT_MANIFEST.json',files)
 print(json.dumps(summary),flush=True)

def render(O,C,ng,choices,winners,pareto,ps):
 import matplotlib
 matplotlib.use('Agg');import matplotlib.pyplot as plt
 plt.rcParams.update({'svg.hashsalt':'twix-rev3-20261013','font.size':9,'axes.spines.top':False,'axes.spines.right':False})
 F=O/'figures';F.mkdir(exist_ok=True)
 def save(fig,name):
  fig.tight_layout();fig.savefig(F/(name+'.svg'),metadata={'Date':None});fig.savefig(F/(name+'.png'),dpi=160);plt.close(fig)
 fig,ax=plt.subplots(1,2,figsize=(10,4))
 for setup,color in [('DeepX','#2369a0'),('H8','#c65c26'),('H10','#348458')]:
  for i,metric in enumerate(['fps_ratio','energy_ratio']):
   v=sorted(r[metric] for r in ng if r['setup']==setup and r[metric] is not None);ax[i].step(v,[(j+1)/len(v) for j in range(len(v))],label=f'{setup} n={len(v)}',color=color,where='post')
 for i,title in enumerate(['Native / Generic stored median FPS','Native / Generic raw mean J/task']):ax[i].axvline(1,color='black',lw=.8);ax[i].set_xlabel(title);ax[i].set_ylabel('Cumulative fraction of admitted split points');ax[i].legend()
 save(fig,'01_native_generic_distribution')
 fig,ax=plt.subplots(figsize=(9,5))
 for setup,color in [('DeepX','#2369a0'),('H8','#c65c26'),('H10','#348458')]:
  rs=[r for r in choices if r['setup']==setup and r['speedup_vs_fastest_full'] is not None and r['energy_ratio_vs_lowest_full'] is not None];ax.scatter([r['speedup_vs_fastest_full'] for r in rs],[r['energy_ratio_vs_lowest_full'] for r in rs],label=f'{setup} n={len(rs)}',alpha=.65,color=color)
 ax.axhline(1,c='black',lw=.8);ax.axvline(1,c='black',lw=.8);ax.set(xlabel='Split FPS / fastest admissible Full FPS',ylabel='Split comparison J/task / lowest-energy admissible Full',title='Strict semantic + claim gates; baselines selected separately');ax.legend();save(fig,'02_split_full_tradeoff')
 fig,ax=plt.subplots(2,1,figsize=(12,7),sharex=True);labels=[r['model']+'\n'+r['setup'] for r in winners];x=list(range(len(labels)))
 ax[0].bar(x,[r['speedup_vs_fastest_full'] if r['speedup_vs_fastest_full'] is not None else math.nan for r in winners]);ax[1].bar(x,[r['energy_ratio_vs_min_full'] if r['energy_ratio_vs_min_full'] is not None else math.nan for r in winners],color='#348458')
 ax[0].set_ylabel('Post-hoc fastest split / fastest Full FPS');ax[1].set_ylabel('Post-hoc min-energy split / min Full J/task')
 for z in ax:z.axhline(1,c='black',lw=.8)
 ax[1].set_xticks(x,labels,rotation=75,ha='right',fontsize=7);ax[0].set_title('Model/setup optima; missing admissible comparisons shown as gaps (NA)');save(fig,'03_model_setup_optima')
 fig,axes=plt.subplots(1,3,figsize=(12,4))
 for ax,setup in zip(axes,['DeepX','H8','H10']):
  rs=[r for r in pareto if r['model']=='mobilenet_v3_large' and r['setup']==setup and r['runner']=='native' and r['quality_filter']=='all_admitted'];ax.scatter([r['fps'] for r in rs],[r['raw_mj'] for r in rs],c=['#c65c26' if r['pareto'] else '#888888' for r in rs]);ax.set(title=setup,xlabel='Stored median FPS',ylabel='Raw system mJ/task')
 fig.suptitle('MobileNet Native splits; orange = Pareto within exact contract cohort');save(fig,'04_pareto_example')
 ps=[r for r in ps if r['kind']=='split']
 producerlabels={'dx_engine_python_fifo':'DX FIFO','hailo10_infermodel_async_fifo':'H10 async FIFO','hailo8_python_vstreams_fifo':'H8 VStreams FIFO','hailo8_cpp_concurrent_three_stage':'H8 C++ concurrent'}
 fig,ax=plt.subplots(figsize=(12,8));labels=[r['model']+' / '+r['setup']+' / '+producerlabels.get(r['producer_impl'],str(r['producer_impl'] or 'unrecorded')) for r in ps];y=list(range(len(ps)))
 ax.scatter([r['p1_thread_ms_median'] if r['p1_thread_ms_median'] is not None else math.nan for r in ps],[i-.13 for i in y],marker='o',label='P1 worker')
 ax.scatter([r['p2_thread_ms_median'] if r['p2_thread_ms_median'] is not None else math.nan for r in ps],[i+.13 for i in y],marker='s',label='P2 worker incl completion')
 ax.set_yticks(y,labels,fontsize=8);ax.invert_yaxis();ax.set(xlabel='Median recorded worker time (ms/task)',title='Native split workers by recorded implementation; overlapping times are not additive');ax.legend();save(fig,'05_pipeline_times')
 fig,ax=plt.subplots(figsize=(7,4));counts=collections.Counter((r['runner'],r['quality_class']) for r in C)
 for i,runner in enumerate(['native','generic']):
  bottom=0
  for quality,color in [('reference_close','#348458'),('accuracy_loss','#c65c26'),('not_evaluated','#999999')]:
   n=counts[(runner,quality)];ax.bar(i,n,bottom=bottom,color=color,label=quality if i==0 else None);bottom+=n
  extra=sum(v for (rr,q),v in counts.items() if rr==runner and q not in ['reference_close','accuracy_loss','not_evaluated'])
  if extra:ax.bar(i,extra,bottom=bottom,color='#555555',label='other/unbound' if i==0 else None)
 ax.set_xticks([0,1],['Native n=246','Generic n=204']);ax.set_ylabel('Current result identities');ax.set_title('Quality class is separate from energy/claim admission');ax.legend();save(fig,'06_quality_coverage')

def report(O,s,w,robust,assoc,ngrows,choices,pipeline,selection_summary):
 ng=s['native_generic'];sp=s['fastest_full_comparison'];en=s['lowest_full_energy_comparison'];gate=s['full_pair_gates'];d=s['diagnostic']
 lines=['# Wissenschaftliche Offlineanalyse der konsolidierten Revision 3','',f"Die kanonische Auswahl umfasst {s['cases']} Betriebspunktidentitäten ({s['native']} Native, {s['generic']} Generic). Davon sind {s['normal_energy']} normal energiegebunden; {s['boundaries']} Grenzfälle bleiben ausdrücklich sichtbar. Die Analyse wurde aus den festgehaltenen kompakten Eingaben berechnet. Alle Vergleichsaussagen gelten für die tatsächlich gemessenen Modelle, Setups, Inputs und Laufzeitverträge.",'','## Native und Generic',f"Bei {ng['n_performance']} technisch gebundenen Performancepaaren ist Native an {ng['faster']} Punkten schneller. Das Medianverhältnis der gespeicherten FPS-Mediane beträgt {ng['fps_ratio_median']:.6f}; Quartile {ng['fps_ratio_q25']:.6f} und {ng['fps_ratio_q75']:.6f}. In {ng['n_energy']} beidseitig energiezugelassenen Paaren liegt die Native-Rohenergie an {ng['energy_lower']} Punkten niedriger; Median E/N-Verhältnis {ng['energy_ratio_median']:.6f}. Beide Vorteile treten an {ng['both_better']}/{ng['n_joint']} gemeinsam auswertbaren Punkten auf. Die Tabellen enthalten alle Paare und Nenner je Modell/Setup, nicht nur Gewinner.",'','Native nutzt spezialisierte FIFO-/Workerimplementierungen; Generic den gemessenen generischen Completionrunner. Die Messgrenze beginnt nach der Eingabevorbereitung und endet mit der letzten Task-Completion; diese Zahlen sind keine Ende-zu-Ende-Anwendungs- oder Requestlatenzen. Drei frische Performanceprozesse mit je 1000 Tasks liefern den gespeicherten FPS-Median. Energie stammt aus eigenen Sensorwiederholungen mit dokumentiertem Lastfenster und exakter Performance-/Qualitätsbindung. Ein Vergleich der Regime beweist keine isolierte Ursache für einen Implementierungsvorteil.','','## Splits und Fullalternativen',f"Von {gate['total']} archivierten Energiepaaren tragen {gate['claim_flag']} ein positives Claimflag. Die strenge Schnittmenge mit semantischer Zulassung enthält {gate['semantic_and_claim']} Paare; {gate['claim_but_not_semantic']} zusätzliche positive Claimflags haben ungesicherte Decoder-/NMS-Gleichwertigkeit und bleiben ausgeschlossen. Die Performanceanalyse verwendet konservativ nur die Teilmenge mit vorhandenem strengem Energiepaarvertrag und bindet zusätzlich beide Performancefreigaben; sie behauptet keine vollständige unabhängige Performancepaarabdeckung ({gate['performance_admitted']} Paare); historische Full-Einzelbeobachtungen liefern keinen neuen Performanceclaim.",f"Gegen die jeweils schnellste zulässige Fullalternative sind {sp['faster']}/{sp['splits']} Splits schneller; Median Speedup {sp['speedup_median']:.6f}, Quartile {sp['speedup_q25']:.6f} bis {sp['speedup_q75']:.6f}. Gegen die energieärmste zulässige Fullalternative sind {en['lower']}/{en['splits']} Splits energieärmer; Median Verhältnis {en['ratio_median']:.6f}. Beide Fullauswahlen erfolgen getrennt und fallbezogen. Fehlende Baselines werden nicht aus einem anderen Setup ergänzt.",'','| Modell | Setup | Schnellster Split | FPS | Schnellste Full | Speedup | Energieminimum Split | mJ/Task | Energieärmste Full | Energieverhältnis |','|---|---|---|---:|---|---:|---|---:|---|---:|']
 def fmt(x,n=3):return 'NA' if x is None else f'{x:.{n}f}'
 for r in w:lines.append(f"| {r['model']} | {r['setup']} | {r['posthoc_fastest_split'] or 'NA'} | {fmt(r['posthoc_fastest_split_fps'],0)} | {r['fastest_full_name'] or 'NA'} | {fmt(r['speedup_vs_fastest_full'])} | {r['posthoc_min_energy_split'] or 'NA'} | {fmt(r['min_split_mj'])} | {r['min_energy_full_name'] or 'NA'} | {fmt(r['energy_ratio_vs_min_full'])} |")
 lines+=['','Die Optima sind post hoc aus denselben beobachteten Kandidaten ausgewählt. Sie sind kein unabhängiger Selektor-, Vorhersage- oder Generalisierungsnachweis. Häufigkeiten, alle Baselineentscheidungen sowie Top- und Worstfälle stehen in `tables/`; gemeinsame Fullbaselines erzeugen abhängige Vergleichspaare.','','## Qualität und Pareto',f"{s['quality_loss']['native']} Native- und {s['quality_loss']['generic']} Generic-Zeilen mit accuracy_loss bleiben im Gesamtbestand erhalten. Davon sind {s['admitted_quality_loss']['native']} Native und {s['admitted_quality_loss']['generic']} Generic sowohl performance- als auch energiezugelassen. Die Zusatzanalyse both_reference_close ist ausdrücklich eine Sensitivitätsauswahl. Dataset-Accuracy bzw. COCO-mAP und funktionale numerische Ausgabeparität sind verschiedene Evidenzachsen. Die zweidimensionale Paretofront setzt höhere FPS und niedrigere Rohenergie innerhalb eines Modell-/Setup-/Runner-/Vertragskontexts voraus. Negative Qualität wird dokumentiert, nicht durch historische positive Werte ersetzt.",'','## Robustheit und Unsicherheit',f"Rohenergie und vorhandene hostnormalisierte Vergleichsenergie werden getrennt gerechnet. Die Normalisierung ändert bei {s['normalization_direction_changes']} zulässigen Split/Full-Paaren die Richtung des Energievergleichs. `sensitivity.csv` zeigt Baselineart, Qualitätsfilter und Energiegrundlage mit ihren Nennern. Es wurde keine neue Idlekorrektur erfunden.",'','Gespeicherte FPS-Mediane werden nicht in Mittelwerte umgedeutet. Primärenergie ist mean(E/N), Effizienz mean(N/E); 1/mean(E/N) und sum(N)/sum(E) stehen als gesonderte Rechnungen in der Unsicherheitstabelle. Energie-CIs sind zweiseitige Student-t-Intervalle des Mittelwerts aus drei tatsächlichen Sensorwiederholungen (df=2, t=4.302652729749461). Sie sind keine Vorhersageintervalle. Für FPS wird die beobachtete Spannweite ausgewiesen, kein Mittelwert-CI auf den Median übertragen. Historische Einzelwerte erhalten kein CI. Alle neun ungepaarten Repeatquotienten dienen nur als empirischer Stabilitätscheck, nicht als neun unabhängige Beobachtungen. Keine neue Randomisierung, kein Bootstrap und kein neuer Seed werden verwendet.','','## Erklärung durch Graph und Pipeline','Graphmerkmale sind über alle sieben Modell-SHAs sowie die Indexhashes der gespeicherten Analyse-/Rankingdateien gebunden. Spearman-Assoziationen werden innerhalb Modell/Setup/Runner berechnet; konstante Merkmale bleiben ohne Korrelationswert. Kandidaten sind ausgewählt und abhängig, daher werden keine Kausal- oder Signifikanzclaims aus diesen Assoziationen abgeleitet.',f"Die Pipelineprojektion bindet {s['pipeline_rows']} Rohreportwiederholungen direkt über ihren Current-SHA; {s['pipeline_missing']} direkte Rohreportbindungen fehlen. Workerzeiten überlappen. H10-P1-Latenz ist nicht P1-Durchsatzzyklus; FIFO-Wartezeit ist keine Handoff-Rechenarbeit. Completiontail und postprocess können Aliase sein. Deshalb zeigt die Abbildung absolute getrennte Workerzeiten, keine summierten Gesamtprozente. Fehlende Felder bleiben NA.",'','## Separate diagnostische Abnahme',f"YOLOv7/DeepX/b044: ein diagnostischer Generic-Einzelwert von {d['fps_single']:.0f} FPS gegenüber dem historischen Median {d['historical_fps_median']:.0f} FPS ({100*d['fps_relative_change']:.4f} %); Energie {1000*d['energy_single_j_per_task']:.3f} gegenüber {1000*d['historical_mean_j_per_task']:.3f} mJ/Task ({100*d['energy_relative_change']:+.4f} %). Diese Abnahme wird nicht in die 450 wissenschaftlichen Identitäten gemischt. Ein Mittelwert-CI darf den Einzelwert nicht als bestanden/fehlgeschlagen klassifizieren; ein kanonischer RGB-Hash bleibt in diesem Abnahmevergleich unbekannt.",'','## Beleggrenzen und Reproduktion',f"Bei {s['administrative_quality_receipt_gaps_native']} aktuellen MobileNet-/DeepX-Native-Punkten ist die referenzierte Verwaltungsreceipt-Dateiversion nicht mit dem erwarteten Hash vorhanden. Die normalen Ergebnis- und Qualitätsblätter sind separat exakt an Current gebunden; die gespeicherten Zulassungsflags werden deshalb unverändert berichtet, aber keine lückenlose Receiptkette behauptet. Die zugehörigen Generic-Paarungen sind ebenfalls markiert. Die Sensitivität exclude_administrative_receipt_gaps zeigt die Auswertung ohne diese Fälle.",'Die kompakte Reproduktion benötigt Python, NumPy, SciPy und Matplotlib; sie öffnet keine Modelle, Sensoren oder Runtime-SDKs. `scripts/reproduce.py --output NEUER_ORDNER` erzeugt Tabellen, Zahlen und Abbildungen aus `inputs/`. Die private Extraktion liest ausschließlich den konsolidierten Archivbestand. Öffentliche Tabellen ersetzen kein vollständiges Rohtrace-/Datasetreplay. Der fehlende historische Full-Producer-Quellhash mit 21 Referenzen bleibt eine Beleggrenze. Rohtraces werden hier nicht neu kalibriert oder numerisch integriert; ihre vorhandenen normalen Produktions- und Archivbelege werden übernommen.','','Die Hash-/Kopierbilanz der SM2-Übergabe ist übernommene Sicherungsevidenz, kein auf Twix wiederholter Vollhash. Datierte THESIS20-, PSD-/TIM- und Abnahmebestände behalten ihren eigenen Geltungsbereich. Keine neue Messung, kein Rebuild und keine Queuefortsetzung wurde für diese Auswertung ausgeführt.']
 # Additional calculated interpretation, without hand-entered scientific values.
 lines+=['','## Verteilungen und Zielkonflikte nach Setup']
 for setup in ['DeepX','H8','H10']:
  nr=[r for r in ngrows if r['setup']==setup];er=[r for r in nr if r['energy_admitted']]
  lines.append(f"{setup}: Native ist an {sum(r['fps_ratio']>1 for r in nr)}/{len(nr)} Punkten schneller als Generic (Medianverhältnis {statistics.median(r['fps_ratio'] for r in nr):.3f}) und an {sum(r['energy_ratio']<1 for r in er)}/{len(er)} Punkten energieärmer (Median {statistics.median(r['energy_ratio'] for r in er):.3f}). Über alle neun ungepaarten Repeatquotienten bleibt der Performancevorteil an {sum(r['fps_repeat_ratio_min']>1 for r in nr)} Punkten und der Energievorteil an {sum(r['energy_repeat_ratio_max']<1 for r in er)} Punkten erhalten.")
 comparable=[r for r in w if r['speed_and_energy_split_same'] is not None]
 lines.append(f"In {sum(not r['speed_and_energy_split_same'] for r in comparable)}/{len(comparable)} auswertbaren Modell-/Setupgruppen unterscheiden sich der schnellste und der energieärmste beobachtete Split. Ein universeller bester Split folgt daraus nicht.")
 for metric,label in [('speedup_vs_fastest_full','Speedup gegen schnellste zulässige Full'),('energy_ratio_vs_lowest_full','Energieverhältnis gegen energieärmste zulässige Full')]:
  valid=[r for r in choices if r[metric] is not None]
  lo=min(valid,key=lambda r:r[metric]);hi=max(valid,key=lambda r:r[metric]);lines.append(f"{label}: Minimum {lo[metric]:.4f} bei {lo['model']}/{lo['setup']}/{lo['case']}, Maximum {hi[metric]:.4f} bei {hi['model']}/{hi['setup']}/{hi['case']}. Die Einzelfälle sind deskriptiv; vollständige Rangextreme stehen in top_worst_splits.csv.")
 lines+=['','## Sensitivität mit expliziten Nennern','| Vergleich | Qualitätsfilter | Energiegrundlage | Performancepaare | schneller | Energiepaare | energieärmer |','|---|---|---|---:|---:|---:|---:|']
 for r in robust:lines.append(f"| {r['comparison']} | {r['quality_filter']} | {r['energy_basis']} | {r['n_performance']} | {r['faster']} | {r['n_energy']} | {r['energy_lower']} |")
 lines+=['','Die folgenden Auswahlen berechnen die zulässige schnellste und energieärmste Fullalternative je Split nach jedem Filter neu. Baseline-/Richtungswechsel beziehen sich auf all_admitted mit Vergleichsenergie; ausgeschiedene Fälle sind keine Richtungswechsel. Modelloptima werden in model_setup_sensitivity_optima.csv ebenfalls neu ausgewählt.','| Filter | Energie | Performance n | schneller | Energie n | energieärmer | andere Energie-Full | Energie-Richtungswechsel |','|---|---|---:|---:|---:|---:|---:|---:|']
 for r in selection_summary:lines.append(f"| {r['quality_filter']} | {r['energy_basis']} | {r['n_performance']} | {r['faster_than_fastest_full']} | {r['n_energy']} | {r['lower_than_min_full']} | {r['lowest_energy_baseline_changes']} | {r['energy_direction_changes']} |")
 lines+=['','## Ausgewählte Graphassoziationen' ,'Die folgenden stärksten absoluten Korrelationen (mindestens zehn ausgewertete Grenzen) sind ebenfalls post hoc ausgewählt. Das Vorzeichen beschreibt die beobachtete Rangordnung, keinen isolierten kausalen Mechanismus.','| Modell | Setup | Runner | Graphmerkmal | Messgröße | n | Spearman rho |','|---|---|---|---|---|---:|---:|']
 for r in sorted([r for r in assoc if r['n']>=10 and r['spearman_rho'] is not None],key=lambda r:-abs(r['spearman_rho']))[:10]:lines.append(f"| {r['model']} | {r['setup']} | {r['runner']} | {r['feature']} | {r['metric']} | {r['n']} | {r['spearman_rho']:.4f} |")
 lines+=['','Graphposition und Schnittgröße verändern auch die Arbeitsaufteilung. Die gebundenen Workerzeiten ermöglichen eine dazu passende Engpasshypothese: eine höhere P2-/Completionzeit kann den Durchsatz trotz geringem P1-Aufwand begrenzen. Aus überlappenden Pipelinezeiten und den gemeinsamen Änderungen von Modellpartition, Precision und Runtime lässt sich jedoch kein einzelner kausaler Effekt isolieren.']
 # Separate generated headings, paragraphs and Markdown tables for portable rendering.
 formatted=[]
 for line in lines:
  if formatted and formatted[-1] and ((formatted[-1].startswith('#') and not line.startswith('#')) or (line.startswith('|') and not formatted[-1].startswith('|'))):formatted.append('')
  formatted.append(line)
 (O/'WISSENSCHAFTLICHE_ANALYSE.md').write_text('\n'.join(formatted)+'\n')
 (O/'CAPTIONS.md').write_text('# Figure captions\n\n1. Cumulative Native/Generic ratios at exact current operating points; stored median FPS and raw mean system J/task, separately admitted denominators.\n\n2. Native split tradeoffs against independently selected fastest and lowest-energy admissible Full alternatives, strict semantic and claim gates.\n\n3. Post-hoc model/setup optima; missing admissible comparisons are gaps, not zero measurements.\n\n4. MobileNet Native split Pareto example within each exact contract cohort; raw system energy, quality losses retained.\n\n5. Measured Native worker times from exact Current raw-report hashes; overlapping worker times must not be added.\n\n6. Quality classes of all 450 Current identities; dataset quality is separate from energy and claim admission.\n')
if __name__=='__main__':main()
