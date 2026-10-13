#!/usr/bin/env python3
"""Project exactly selected archived reports; all reads stay under canonical B."""
import argparse, collections, csv, hashlib, json, math, statistics
from pathlib import Path
SETUP={'orin_nx_deepx_m1_01':'DeepX','orin_nx_hailo8_01':'H8','orin_nx_hailo10_01':'H10'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def write(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,sort_keys=True,allow_nan=False)+'\n')
def rows(p):return list(csv.DictReader(p.open()))
def key(r):return (r['model_id'],SETUP.get(r['setup_id'],r['setup_id']),r.get('backend',r.get('direction')),r['case_id'])
def num(x):return float(x) if x not in (None,'') else None
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--base',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();B=a.base.resolve();O=a.output
 review=read(B/'_analysis/twix_20261013/evidence/reviewer_provenance_native_join.json')
 gap_native={r['uid'].replace('native|revision3|','native|') for r in review['rows'] if not r['matches']}
 entries=read(B/'_supplements/native_fairness_rev3_20261013/ENTRYPOINTS.json');provenance=[]
 def get(name):
  es=[e for e in entries if e['source'].endswith('/'+name)];assert len(es)==1,(name,len(es));e=es[0];p=B/e['canonical_path'];assert p.resolve().is_relative_to(B);assert sha(p)==e['sha256'];provenance.append({'role':name,'source_sha256':e['sha256']});return read(p)
 N=get('current_results/native_current.json')['rows'];G=get('current_results/generic_current.json')['rows'];P=get('native_energy_pair_comparison.json');E=get('scientific_energy_rows.json');D=get('DELTA_CENTRAL_RESULTS.json')
 receipt=read(B/'_supplements/native_fairness_rev3_20261013/COPY_RECEIPT.json')
 byhash={e['sha256']:e['destination'] for e in receipt['files']}
 def bound(h):
  p=B/byhash[h];assert p.resolve().is_relative_to(B);assert sha(p)==h;return read(p)
 modelhashes={r['model_id']:r['model_sha256'] for r in E}
 generic_reps=get('current_results/generic_repeats.json')['rows'];gri=collections.defaultdict(list)
 for r in generic_reps:gri[r['case_key']].append(r)
 energy={key(x):x for x in E}; native={key(x):x for x in N};assert len(native)==246
 output=[];repeats=[];pairing=[]
 for runner,rs in [('native',N),('generic',G)]:
  for r in rs:
   k=key(r);uid='|'.join((runner,)+k);n=r if runner=='native' else native[k];sci=energy.get(k,{})
   q=r.get('quality_provenance') or {};ep=r.get('energy_provenance') or {};ob=r.get('observation') or {};gq=r.get('generic_quality_transfer') or {}
   if runner=='generic':
    assert r['native_quality_provenance']['performance_summary_sha256']==n['observation']['summary_sha256'];assert r['fresh_native_fps_median']==n['fps']
    assert r['native_pair_status']=='technical_comparable';assert all(r['normal_technical_gates'].values())
    gr=gri[r['case_key']];assert len(gr)==3 and len({(t['boot_id'],t['pid'],t['process_start_ticks']) for t in gr})==3
    assert len({(t['queue_depth'],t['worker_count']) for t in gr})==1
   fps=r.get('fps',r.get('fps_median'));samples=r['fps_samples']; perfsha=ob.get('summary_sha256') if runner=='native' else r['raw_result_sha256']
   if samples:
    assert math.isclose(statistics.median(samples),fps,rel_tol=1e-12)
    if runner=='native':
     prs=ob['repeats'];assert len(prs)==3 and len({(t['runner_pid'],t['runner_start_monotonic_ns']) for t in prs})==3
   if r.get('normal_energy_eligible'):
    assert ep.get('performance_summary_sha256',ep.get('performance_result_sha256'))==perfsha
   er=r.get('energy_repeats') or [];cr=r.get('energy_comparison_repeats') or []
   for i,t in enumerate(er):
    en=t['energy_j'];count=t['completed_tasks'];v=t.get('joules_per_task',t.get('energy_per_completed_task_j'));eff=t.get('tasks_per_joule',t.get('completed_tasks_per_j'));assert math.isclose(en/count,v,rel_tol=1e-10);assert math.isclose(count/en,eff,rel_tol=1e-10)
    repeats.append({'uid':uid,'repeat':i,'energy_j':en,'completed_tasks':count,'j_per_task':v,'tasks_per_j':eff,'duration_s':t.get('sensor_interval_s',t.get('active_duration_s')),'comparison_j_per_task':cr[i]['joules_per_task'] if cr else v,'source_sha256':t.get('report_sha256',t.get('raw_aggregate_sha256',t.get('summary_sha256')))})
   if er:
    assert math.isclose(statistics.mean(x['energy_j']/x['completed_tasks'] for x in er),r['energy_per_task_j'],rel_tol=1e-10)
    assert math.isclose(statistics.mean(x['completed_tasks']/x['energy_j'] for x in er),r['tasks_per_j'],rel_tol=1e-10)
   quality=r.get('accuracy_class') if runner=='native' else gq.get('generic_task_quality_status')
   loss=num(r.get('quality_relative_loss')) if runner=='native' else (gq.get('generic_accuracy_assessment',{}).get('relative_loss') if isinstance(gq.get('generic_accuracy_assessment'),dict) else None)
   x={'uid':uid,'runner':runner,'model_id':k[0],'setup_id':k[1],'backend':k[2],'case_id':k[3],'kind':r.get('kind','split'),'task':r['task'],'fps':fps,'fps_samples':samples,'performance_observations':len(samples) or 1,'performance_aggregation':'stored_median' if samples else 'historical_single','performance_source_sha256':perfsha,'quality_class':quality,'quality_relative_loss':loss,'normal_quality':r.get('normal_quality_eligible') is True,'normal_performance_claim':r.get('normal_claim_eligible') is True,'normal_energy':r.get('normal_energy_eligible') is True,'energy_claim':r.get('energy_efficiency_claim_eligible') is True,'diagnostic_energy':r.get('energy_diagnostic_only') is True,'energy_status':r['energy_status'],'raw_j_per_task':r.get('energy_per_task_j'),'mean_tasks_per_j':r.get('tasks_per_j'),'comparison_j_per_task':r.get('energy_comparison_per_task_j',r.get('energy_per_task_j')),'comparison_basis':r.get('energy_comparison_basis','raw_measured'),'energy_ci':r.get('energy_per_task_j_ci'),'energy_repeat_n':len(er),'quality_source_sha256':q.get('quality_summary_sha256'),'quality_exclusions':q.get('claim_exclusion_reasons',[]),'energy_exclusions':ep.get('claim_exclusion_reasons',[]),'model_sha256':sci.get('model_sha256'),'energy_scope':sci.get('energy_scope','full_system' if runner=='generic' else None),'energy_window':sci.get('energy_window_effective','command_window' if runner=='generic' else None),'calibration_sha256':sci.get('energy_calibration_sha256'),'comparison_endpoint':sci.get('comparison_endpoint_contract_hash'),'measurement_boundary':ob.get('measurement_boundary',r.get('measurement_boundary')),'completion_contract_sha256':None,'completion_mode':ob.get('completion_mode',r.get('completed_stage')),'precision':sci.get('precision',r.get('precision')),'contract_preprocessing':sci.get('preprocessing_contract_sha256'),'contract_decoder':sci.get('decoder_contract_sha256'),'contract_nms':sci.get('nms_contract_sha256'),'prepared_image_sha256':sci.get('prepared_feed_source_image_sha256'),'scheduling':ob.get('scheduling'),'supersedes':r.get('supersedes'),'current_status':r.get('status')}
   # public inputs retain identities and hashes; historical raw paths stay in private originals.
   x['administrative_quality_receipt_gap']=('|'.join(('native',)+k)) in gap_native
   x.pop('supersedes')
   x['scheduling']=json.dumps(x['scheduling'],sort_keys=True) if x['scheduling'] is not None else None
   if runner=='generic':
    report=bound(ep['normal_report_sha256']);assert report['performance_result_sha256']==perfsha
    assert report['identity']['model_id']==r['model_id'] and report['identity']['case_id']==r['case_id'] and report['identity']['setup_id']==r['setup_id']
    contracts=[]
    for t in er:
     agg=bound(t['raw_aggregate_sha256']);contracts.append((agg['energy_physical_scope_canonical'],tuple(agg['energy_window_effective_values']),agg.get('energy_calibration_sha256') or agg.get('full_system_current_scale_calibration_sha256_actual')))
    assert len(set(contracts))==1
    scope,windows,calibration=contracts[0];assert scope=='full_system' and windows==('command_window',)
    complete=json.dumps(r['completion_contract'],sort_keys=True);contract=hashlib.sha256(complete.encode()).hexdigest()
    x.update(model_sha256=modelhashes[r['model_id']],model_binding_basis='exact_current_native_pair_and_shared_original_model_manifest',energy_scope=scope,energy_window=windows[0],calibration_sha256=calibration,comparison_endpoint=report['identity']['output_endpoint_id'],precision=r['precision'],contract_preprocessing=r['input_binding'].get('preprocessing_contract_sha256'),contract_decoder=None,contract_nms=None,prepared_image_sha256=r['input_binding'].get('input_image_sha256',r['input_binding'].get('source_image_sha256')),scheduling=json.dumps({'queue_depth':gr[0]['queue_depth'],'worker_count':gr[0]['worker_count']},sort_keys=True),completion_contract_sha256=contract,generic_energy_report_sha256=ep['normal_report_sha256'],pareto_contract_basis='own_energy_aggregates_and_current_completed_endpoint_input_completion_contract')
   output.append(x)
   if runner=='generic':pairing.append({'native_uid':'|'.join(('native',)+k),'generic_uid':uid,'technical_gates':r['normal_technical_gates'],'native_summary_sha256':r['native_quality_provenance']['performance_summary_sha256'],'generic_result_sha256':perfsha,'stored_fps_ratio':r['native_over_generic_completed_task_ratio']})
 assert len({r['uid'] for r in output})==450
 # Full comparison records preserve all gates and exact endpoint/input/model/calibration contract hashes.
 pairs=[]
 for p in P:
  k=(p['model'],SETUP[p['setup_id']],p['split_backend'],p['case']);bk=(p['model'],SETUP[p['setup_id']],p['baseline_backend'],'full')
  d={k:v for k,v in p.items() if not k.endswith('_source') and not (isinstance(v,str) and ('/home/' in v or '/homes/' in v))}
  d.update(split_uid='|'.join(('native',)+k),baseline_uid='|'.join(('native',)+bk));pairs.append(d)
 # Explicit, fallgenau replacement: old performance projections are not overwritten.
 old=B/'_analysis/final_20261004/analysis/public/inputs';hist={name:rows(old/(name+'.csv')) for name in ['native_cases','generic_cases','quality','energy_cases','coverage','generic_raw','generic_short_predecessors','performance_repeats','energy_repeats','energy_physical_attempts']}
 actions=[]
 for runner,ns,oname in [('native',N,'native_cases'),('generic',G,'generic_cases')]:
  om={key(x):x for x in hist[oname]};assert len(om)==len(hist[oname])
  for r in ns:
   k=key(r);o=om.pop(k,None);newfps=r.get('fps',r.get('fps_median'));same=o is not None and num(o['fps'])==newfps
   if runner=='native' and o:assert o['case_uid'] in r['supersedes']
   actions.append({'runner':runner,'model':k[0],'setup':k[1],'backend':k[2],'case':k[3],'old_uid':o['case_uid'] if o else None,'current_uid':'|'.join((runner,)+k),'overlap':'common_identical_value' if same else 'common_updated' if o else 'F_only','selection_action':'retain_single_observation' if r.get('status')=='reused_verified' else 'select_qualified_rev3_generation','old_fps':num(o['fps']) if o else None,'current_fps':newfps,'performance_contract':'explicit_native_supersedes' if runner=='native' else 'logical_identity_with_preserved_historical_reference','energy_action':'select_exact_current_binding' if r.get('normal_energy_eligible') else 'preserve_exclusion_no_old_fill','quality_action':'select_bound_current_including_negative','historical_preserved':True})
  for k,o in om.items():actions.append({'runner':runner,'model':k[0],'setup':k[1],'backend':k[2],'case':k[3],'old_uid':o['case_uid'],'current_uid':None,'overlap':'B_only','selection_action':'retain_historical_cohort','old_fps':num(o['fps']),'current_fps':None,'performance_contract':'separate_historical','energy_action':'preserve_historical','quality_action':'preserve_historical','historical_preserved':True})
 # Compare measured axes without equating a matching FPS value with an identical cohort.
 oldperf={}
 for runner,name in [('native','native_cases'),('generic','generic_cases')]:
  for r in hist[name]:oldperf['|'.join((runner,)+key(r))]=r
 oldenergy={key(r):r for r in hist['energy_cases']};axisactions=[]
 for c in output:
  o=oldperf[c['uid']];ek=(c['model_id'],c['setup_id'],c['backend'],c['case_id']);oe=oldenergy.get(ek) if c['runner']=='native' else None
  axisactions.append({'axis':'performance','current_uid':c['uid'],'historical_uid':o['case_uid'],'logical_overlap':'common','generation_action':'retain_historical_single' if c['performance_observations']==1 else 'select_qualified_rev3_cohort','old_value':num(o['fps']),'current_value':c['fps'],'unit':'tasks/s_stored_median_or_labelled_single','same_numeric_value':num(o['fps'])==c['fps'],'old_repeat_n':int(o['repetitions']),'current_repeat_n':c['performance_observations'],'current_admitted':c['normal_performance_claim'],'current_source_sha256':c['performance_source_sha256'],'original_retained':True,'interpretation':'same value does not establish identical observation bytes'})
  axisactions.append({'axis':'energy','current_uid':c['uid'],'historical_uid':oe['case_uid'] if oe else None,'logical_overlap':'common_native_identity' if oe else 'F_only_generic_energy_axis','generation_action':'select_exact_current_energy_binding' if c['normal_energy'] else 'preserve_current_exclusion_no_historical_fill','old_value':num(oe['energy_per_task_j']) if oe else None,'current_value':c['raw_j_per_task'],'unit':'mean_J_per_completed_task','same_numeric_value':bool(oe and num(oe['energy_per_task_j'])==c['raw_j_per_task']),'old_repeat_n':3 if oe else 0,'current_repeat_n':c['energy_repeat_n'],'current_admitted':c['normal_energy'],'original_retained':True,'interpretation':'historical Native energy is not old Generic energy'})
  axisactions.append({'axis':'quality','current_uid':c['uid'],'historical_uid':None,'logical_overlap':'historical_dataset_cohort_relation_not_inferred','generation_action':'select_current_bound_quality_including_negative' if c['normal_quality'] else 'retain_current_quality_exclusion','old_value':None,'current_value':c['quality_class'],'unit':'dataset_quality_class_not_numerical_parity','current_admitted':c['normal_quality'],'current_source_sha256':c['quality_source_sha256'],'administrative_receipt_gap':c['administrative_quality_receipt_gap'],'original_retained':True,'interpretation':'all 560 historical dataset rows retained separately; no unproven cross-generation dataset join'})
 write(O/'cohort_axis_actions.json',axisactions)
 summary={'current_rows':len(output),'action_counts':dict(collections.Counter(r['overlap'] for r in actions)),'performance_actions':dict(collections.Counter(r['selection_action'] for r in actions)),'historical_axes':{k:len(v) for k,v in hist.items()},'historical_quality_classes':dict(collections.Counter(r['accuracy_class'] for r in hist['quality'])),'historical_coverage_status':dict(collections.Counter(r['status'] for r in hist['coverage'])),'unresolved_scientific_identity_assignments':0,'historical_raw_generic_policy':'separate raw-endpoint regime, not replaced by completed-task Rev3; all original rows retained','historical_quality_policy':'560 original dataset observations retained as original cohorts; new quality bindings select Current at each of 450 result identities, not deletion/relabeling of old quality observations'}
 summary['current_axis_counts']={'performance_repeated_cohorts':sum(c['performance_observations']==3 for c in output),'performance_historical_singles':sum(c['performance_observations']==1 for c in output),'performance_observations':sum(c['performance_observations'] for c in output),'energy_cohorts':sum(c['normal_energy'] for c in output),'energy_repeats':sum(c['energy_repeat_n'] for c in output),'axis_actions':{axis:dict(collections.Counter(r['generation_action'] for r in axisactions if r['axis']==axis)) for axis in ['performance','energy','quality']}}
 # Record broader historical axes fall by fall; logical overlap never equates quality generations.
 historical_records=[]
 aliases={'deepx_m1':'deepx','deepx_m1_to_tensorrt':'deepx','deepx_to_trt':'deepx','hailo8_to_trt':'hailo8','hailo8_to_tensorrt':'hailo8','hailo10h_to_trt':'hailo10h','hailo10_to_tensorrt':'hailo10h','hailo10':'hailo10h','ort_tensorrt':'tensorrt','native_full_tensorrt':'tensorrt','native_full_deepx':'deepx','native_full_hailo8':'hailo8','native_full_hailo10h':'hailo10h'}
 def broadkey(r):return (r.get('model_id'),SETUP.get(r.get('setup_id'),r.get('setup_id')),r.get('case_id'),aliases.get(r.get('backend'),r.get('backend')))
 logical=collections.defaultdict(list)
 for r in output:logical[broadkey(r)].append(r['uid'])
 for axis in ['quality','coverage','generic_raw','generic_short_predecessors','energy_cases','energy_physical_attempts']:
  for i,r in enumerate(hist[axis]):
   matches=logical.get(broadkey(r),[])
   status='logical_common_distinct_generation' if matches else 'B_only_historical_scope'
   historical_records.append({'axis':axis,'historical_row':i,'historical_id':r.get('quality_id',r.get('case_uid')),'model':r.get('model_id'),'setup':r.get('setup_id'),'case':r.get('case_id'),'backend':r.get('backend'),'cohort':r.get('cohort'),'status':r.get('status',r.get('accuracy_class')),'overlap':status,'current_logical_matches':matches,'generation_relation':'not_equated_from_compact_identity' if matches else 'separate_historical','action':'retain_original_historical_cohort'})
 unsupported=read(B/'reports/native_expected_matrix.json')['excluded_expected_rows']
 for i,r in enumerate(unsupported):historical_records.append({'axis':'native_unsupported','historical_row':i,'model':r['model'],'setup':SETUP[r['setup_id']],'case':r['case'],'backend':r['backend'],'status':r['actual_status'],'reason':r['primary_failure_reason'],'overlap':'B_only_historical_scope','action':'retain_terminal_negative'})
 summary['historical_axes_overlap']={axis:dict(collections.Counter(r['overlap'] for r in historical_records if r['axis']==axis)) for axis in sorted({r['axis'] for r in historical_records})}
 summary['historical_generation_relations_not_inferred']=sum(r.get('generation_relation')=='not_equated_from_compact_identity' for r in historical_records)
 summary['unresolved_scientific_identity_assignments_in_completed_task_450']=summary.pop('unresolved_scientific_identity_assignments')
 write(O/'historical_records.json',historical_records)
 # Graph evidence: verified model SHA equality + original index hashes for each graph file.
 manifest=read(B/'run_manifest.json');index=read(B/'artifact_index.json')['artifacts'];ih=collections.defaultdict(set)
 for e in index:ih[e['path']].add(e.get('sha256','').removeprefix('sha256:'))
 graphs=[];graphproof=[]
 for model,m in sorted(manifest['models'].items()):
  modelhash=m['model_sha256'].removeprefix('sha256:');es={r['model_sha256'] for r in E if r['model_id']==model};assert es=={modelhash},(model,es)
  docs=[]
  for name in ['analysis.json','candidate_ranking.json']:
   rel=f'models/{model}/analysis/{name}';p=B/rel;h=sha(p);assert h in ih[rel];docs.append(read(p));graphproof.append({'model_id':model,'model_sha256':modelhash,'file':rel,'sha256':h})
  analysis,ranking=docs
  for r in ranking['candidates']:
   graphs.append({'model_id':model,'model_sha256':modelhash,'case_id':r['case_id'],'boundary':r['boundary'],'node_count':analysis['node_count'],'topological_position':(r['boundary']+1)/analysis['node_count'],'cut_bytes':r.get('cut_bytes'),'n_cut_tensors':r.get('n_cut_tensors'),'part2_input_count':r.get('part2_input_count'),'flops_left_ratio':r.get('flops_left_ratio')})
 # Resolve each measured pipeline report by exact archived SHA, not historical filename.
 receipt=read(B/'_supplements/native_fairness_rev3_20261013/COPY_RECEIPT.json')
 byhash={e['sha256']:e['destination'] for e in receipt['files']};pipe=[];pipe_missing=[]
 fields=['p1_ms','p1_thread_ms','p2_run_ms','p2_thread_ms','handoff_ms','trt_input_copy_ms','deepx_run_ms','output_map_ms','fifo_put_block_ms','completion_tail_ms','postprocess_ms','producer_makespan_ms','consumer_makespan_ms','p1_effective_cycle_ms','consumer_effective_cycle_ms','hailo_latency_ms','queue_wait_ms','makespan_ms','completed_frames','producer_impl','queue_depth','inflight']
 for n in N:
  for i,r in enumerate(n['observation'].get('repeats',[])):
   h=r['raw_report_sha256']
   if h not in byhash:pipe_missing.append({'uid':'|'.join(('native',)+key(n)),'repeat':i,'sha256':h});continue
   p=B/byhash[h];assert sha(p)==h;raw=read(p)
   if isinstance(raw,list):
    assert len(raw)==1 and raw[0]['case_id']==n['case_id'];raw=raw[0]
   pp={'uid':'|'.join(('native',)+key(n)),'repeat':i,'raw_sha256':h,'kind':n['kind'],'task':n['task'],'setup_id':n['setup_id'],'model_id':n['model_id'],'case_id':n['case_id'],'runner_pid':r.get('runner_pid'),'runtime_instance_id':r.get('runtime_instance_id'),'completed_tasks':r['completed_tasks'],'stored_makespan_s':r['makespan_s']}
   pp.update({f:raw.get(f) for f in fields});pipe.append(pp)
 diag=get('analysis_review/REDUCED_ACCEPTANCE_EVIDENCE.json')
 cell=next(c for c in diag['cells'] if c.get('model_id')=='yolov7_paper' and c.get('setup_id')=='orin_nx_deepx_m1_01')
 diagnostic={'model':'yolov7_paper','setup_id':'DeepX','case_id':'b044','role':'separate_diagnostic_single','metrics':{'fps_display':cell['metrics']['fps_display'],'energy':{'energy_per_completed_task_j':cell['metrics']['energy']['energy_per_completed_task_j']}},'historical_baseline_context':{k:cell['historical_baseline_context'][k] for k in ['historical_fps','historical_energy_per_task_j']}}
 # Strip absolute raw paths recursively from public diagnostic projection.
 def clean(d):
  if isinstance(d,dict):return {k:clean(v) for k,v in d.items() if not (isinstance(v,str) and ('/home/' in v or '/homes/' in v))}
  if isinstance(d,list):return [clean(v) for v in d]
  return d
 write(O/'provenance_limits.json',review);write(O/'diagnostic_acceptance.json',clean(diagnostic));write(O/'pipeline_repeats.json',pipe);write(O/'pipeline_missing.json',pipe_missing)
 for name,value in [('cases',output),('energy_repeats',repeats),('native_generic_bindings',pairing),('split_full_contracts',pairs),('graph_features',graphs),('graph_provenance',graphproof),('cohort_actions',actions),('historical_scope',summary),('source_provenance',provenance)]:write(O/(name+'.json'),value)
 # Copy complete historic compact projections to the canonical historical selector only; already inside B.
 selected={'revision3':'_analysis/twix_20261013/public/inputs/cases.json','historical':{k:str((old/(k+'.csv')).relative_to(B)) for k in hist},'precedence':'Rev3 replaces 450 completed-task result selections only. Broader historical quality/raw-endpoint/unsupported/diagnostic cohorts retain their own identities.'}
 write(O/'canonical_selection.json',selected)
 # Matrix / control totals are derived, not treated as fitting targets.
 assert sum(x['normal_energy'] for x in output)==437
 assert collections.Counter(x['quality_class'] for x in output if x['runner']=='native')['accuracy_loss']==26
 assert collections.Counter(x['quality_class'] for x in output if x['runner']=='generic')['accuracy_loss']==17
 write(O/'MANIFEST.json',{p.name:sha(p) for p in sorted(O.glob('*.json')) if p.name!='MANIFEST.json'})
 print(json.dumps(summary),flush=True)
if __name__=='__main__':main()
