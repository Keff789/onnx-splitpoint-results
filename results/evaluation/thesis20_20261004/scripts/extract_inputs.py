#!/usr/bin/env python3
"""Offline curated projection using the installed project's existing readers.
Original roots are explicit CLI inputs. Writes occur only below --output and
--private-index; no inference, bootstrap, process dispatch or raw-data rewrite.
"""
import argparse,csv,json,math,statistics,subprocess,sys
from collections import Counter
from pathlib import Path

def read(p):return json.loads(Path(p).read_text())
def write(p,d):p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
def csvwrite(p,rows):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
 fields=list(dict.fromkeys(k for r in rows for k in r))
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:(json.dumps(v,separators=(',',':')) if isinstance(v,(dict,list)) else v) for k,v in r.items()} for r in rows)
def parse(v):
 if not isinstance(v,str):return v
 if v=='':return None
 if v in ('True','true'):return True
 if v in ('False','false'):return False
 try:return json.loads(v)
 except Exception:return v
def csvread(p):return [{k:parse(v) for k,v in r.items()} for r in csv.DictReader(Path(p).open())]
def ident(r):return (r.get('model_id',r.get('model')),r.get('case_id',r.get('case')),r.get('setup_id'),r.get('backend',r.get('direction')),r.get('comparison_backend',''))
def positive(v):return isinstance(v,(float,int)) and not isinstance(v,bool) and math.isfinite(v) and v>0
SETUP={'orin_nx_hailo8_01':'H8','orin_nx_hailo10_01':'H10','orin_nx_deepx_m1_01':'DeepX'}
def common(r,cohort):
 return dict(cohort=cohort,model_id=r.get('model_id') or r.get('model'),case_id=r.get('case_id') or r.get('case'),
 setup_id=SETUP.get(r.get('setup_id'),r.get('setup_id') or 'controller'),backend=r.get('backend') or r.get('direction'),
 comparison_backend=r.get('comparison_backend',''),precision=r.get('precision') or r.get('execution_precision',''),task=r.get('task',''),
 endpoint_id=r.get('comparison_output_endpoint_id') or r.get('output_endpoint_id',''))
def main():
 p=argparse.ArgumentParser();p.add_argument('--base',required=True,type=Path);p.add_argument('--corrected',required=True,type=Path);p.add_argument('--completion',required=True,type=Path);p.add_argument('--yolo',required=True,type=Path);p.add_argument('--output',required=True,type=Path);p.add_argument('--private-index',required=True,type=Path);a=p.parse_args()
 for root in (a.base,a.corrected,a.completion,a.yolo):
  if a.output.resolve().is_relative_to(root.resolve()):raise ValueError('output must be separate from original inputs')
 def forbidden(*args,**kwargs):raise RuntimeError('analysis forbids process/inference dispatch')
 subprocess.Popen=forbidden
 from onnx_splitpoint_tool.generic_completion_reporting import write_completion_reports
 from onnx_splitpoint_tool.yolo_augmentation_reporting import write_augmentation_reports
 from onnx_splitpoint_tool.native_energy_reporting import collect_native_energy
 from onnx_splitpoint_tool.native_rate_endpoints import rate_endpoint_fields
 out=a.output;inputs=out/'inputs';replay=a.private_index.parent/'reporter_replay';replay.mkdir(parents=True,exist_ok=True)
 C=a.corrected/'scientific-corrected-v2';Y=a.yolo;YR=Y/'runs/yolo_min3_20261002_222904';YF=Y/'attempts/h8_energy_rest_20261004_170518'
 terminal=read(YF/'terminal-status.json');assert terminal['exitcode']==0 and terminal['status']=='complete'
 locations=read(YF/'rest-result-sources.json')
 replay_summaries={}
 for cohort,root,planfile in [('base',a.completion,a.completion/'plan/execution-plan.json'),('augmentation',Y/'completion',Y/'completion/execution-plan.json')]:
  replay_summaries[cohort]=write_completion_reports(read(planfile),root/'results',replay/cohort)
  assert replay_summaries[cohort]['all_cases_measured'],replay_summaries[cohort]
 replay_summaries['augmentation_report']=write_augmentation_reports(Y/'plan/augmentation-plan.json',replay/'augmentation',locations['native_summary'],locations['energy_roots'],replay/'combined')
 # One authoritative corrected Native summary, not every copied attempt.
 base_native=read(a.corrected/'f02-f03/native-report-v2/native_producer_combined_summary.json')['rows']
 added_native=read(locations['native_summary'])['rows']
 native_terminal_counts=dict(Counter(str(r.get('status')) for r in base_native))
 selected=[('base',r) for r in base_native if r.get('ok') is True]+[('augmentation',r) for r in added_native if r.get('ok') is True]
 descriptor=[];native_cases=[];perf_reps=[];checks=[]
 for cohort,r in selected:
  c=common(r,cohort);uid='|'.join(map(str,('native',cohort,*ident(r))));c['case_uid']=uid;c['measurement']='native_completed';c['execution_mode']='full' if c['case_id']=='full' else 'split'
  rates=rate_endpoint_fields(r);counts=rates['completed_task_work_unit_counts'];times=rates['completed_task_measurement_times_s'];samples=rates['fps_repetition_samples']
  if not counts:
   # Complete reports already carry the strict normal endpoint projection.
   counts=r.get('completed_task_work_unit_counts',[]);times=r.get('completed_task_measurement_times_s',[]);samples=r.get('fps_repetition_samples',[])
  assert len(counts)==len(times)==len(samples)==3,(c,len(counts),rates['completed_task_fps_unavailable_reason'])
  values=[n/t for n,t in zip(counts,times)];reported=r.get('completed_task_fps') or r.get('fps_median') or r.get('fps_makespan')
  checks.append(dict(check='native_count_time_median',case_uid=uid,reported=reported,recomputed=statistics.median(values),abs_error=abs(reported-statistics.median(values))))
  c.update(fps=statistics.median(values),fps_min=min(values),fps_max=max(values),fps_sd=statistics.stdev(values),repetitions=3,
   native_quality_gate_status=r.get('quality_gate_status') or r.get('task_quality_status',''),claim_eligible=r.get('performance_claim_eligible') is True,
   source_runner=r.get('producer_impl',''),command_sha256=r.get('native_command_contract_sha256',''))
  native_cases.append(c)
  for i,(n,t,f) in enumerate(zip(counts,times,samples)):
   perf_reps.append({**c,'repetition':i,'completed_count':n,'makespan_s':t,'reported_fps':f,'recomputed_fps':n/t})
  descriptor.append({'cohort':cohort,'identity':ident(r),'report':r.get('report'),'source_root':r.get('source_root'),
   'source_reports':r.get('source_reports'), 'native_command_contract':r.get('native_command_contract'),
   'output_manifest':r.get('output_dump_manifest'),'command_sha256':r.get('native_command_contract_sha256')})
 write(a.private_index,{'selected_native_sources':descriptor,'reporter_replay':replay_summaries})
 del base_native,added_native,selected,descriptor
 # Completion observations are reread from the real original result files by the normal parser.
 pairs=[];gc_cases=[]
 for cohort in ('base','augmentation'):
  observed=read(replay/cohort/'generic_completion_observations.json')['rows'];pr=read(replay/cohort/'generic_completion_cross_runner.json')['pairs']
  pairs.extend([dict(r,observation_origin=cohort) for r in pr])
  for r in observed:
   c=common(r,cohort);uid='|'.join(map(str,('generic_completed',cohort,r['case_key'])));c.update(case_uid=uid,measurement='generic_completed',execution_mode='split')
   values=[x['completed_task_count']/x['measured_makespan_seconds'] for x in r['repetitions']]
   c.update(fps=statistics.median(values),fps_min=min(values),fps_max=max(values),fps_sd=statistics.stdev(values),repetitions=len(values),accuracy_class='',claim_eligible=False)
   gc_cases.append(c)
   checks.append(dict(check='generic_count_time_median',case_uid=uid,reported=r['completed_task_fps'],recomputed=statistics.median(values),abs_error=abs(r['completed_task_fps']-statistics.median(values))))
   for i,rep in enumerate(r['repetitions']):perf_reps.append({**c,'repetition':i,'completed_count':rep['completed_task_count'],'makespan_s':rep['measured_makespan_seconds'],'reported_fps':rep['completed_task_fps'],'recomputed_fps':values[i]})
 pairfields=['model_id','case_id','direction','precision','setup_id','comparison_backend','output_endpoint_id','boundary_class','observation_origin',
 'generic_completed_task_fps','native_completed_task_fps','native_over_generic_completed_task_ratio','historical_generic_raw_fps',
 'eligible_for_technical_transfer','eligible_for_quality_transfer','eligible_for_claim_transfer','generic_task_quality_status','native_task_quality_status',
 'runtime_conditions_comparable','measurement_boundaries_comparable']
 public_pairs=[{k:(SETUP[r[k]] if k=='setup_id' else r.get(k)) for k in pairfields} for r in pairs]
 raw=read(C/'performance_observations.json');rawrows=[]
 for r in raw:
  row=common(r,'base');row.update(measurement='historical_generic_output',throughput_fps=r['throughput_fps'],measurement_endpoint=r.get('measurement_endpoint'),accuracy_class=r.get('accuracy_class'),variant=r.get('variant'),postprocess_included=r.get('postprocess_included'))
  rawrows.append(row)
 # The twelve historical short runs are inventoried independently, never added to 204 completed-task cases.
 short=[]
 for pth in sorted((YR/'models').glob('*/benchmark_results/normalized_results.json')):
  payload=read(pth);rows=payload if isinstance(payload,list) else payload.get('rows',payload.get('results',[]))
  for r in rows:
   row=common(r,'augmentation_short');row.update(throughput_fps=r.get('throughput_primary_fps'),measurement_endpoint=r.get('measurement_endpoint'),measurement='generic_short_predecessor',source_role='inventory_only')
   short.append(row)
 # Unchanged quality results/decisions; no bootstrap recomputation.
 quality=[];quality_policy={}
 for cohort,qroot in [('base',a.base),('augmentation',YR)]:
  qr=read(qroot/'quality_management/central_quality_summary.json')['results']
  policies={(r['n'],r['primary']['bootstrap_repetitions'],r['seed_schema']['seed']) for r in qr}
  assert len(policies)==1,(cohort,policies)
  quality_policy[cohort]=dict(zip(['N','B','seed'],next(iter(policies))))
 for cohort,path in [('base',C/'task_quality_reference_comparison.json'),('augmentation',YR/'reports/scientific/task_quality_reference_comparison.json')]:
  for i,r in enumerate(read(path)):
   row=common(r,cohort);metric='Top1' if r['task']=='classification' else 'COCO_AP_50_95'
   row.update(quality_id=f'{cohort}_quality_{i:03d}',variant=r.get('variant'),metric=metric,candidate=r.get('row_'+metric),reference=r.get('reference_'+metric),
    delta=r.get('delta_vs_full_onnx_'+metric),ci_low=r.get('ci_low_'+metric),ci_high=r.get('ci_high_'+metric),accuracy_class=r.get('accuracy_class'),
    relative_loss=r.get('accuracy_relative_loss'),technical_fail=r.get('accuracy_technical_fail'),**quality_policy[cohort])
   quality.append(row)
 # Standard energy reader on real canonical sources, including selected retry references.
 energy_cases=[];energy_reps=[]
 energies=[('base',r) for r in collect_native_energy(a.base)]+[( 'augmentation',r) for root in locations['energy_roots'] for r in collect_native_energy(root)]
 for cohort,r in energies:
  c=common(r,cohort);uid='|'.join(map(str,('energy',cohort,*ident(r))));c.update(case_uid=uid,execution_mode=r['execution_mode'],accuracy_class=r.get('accuracy_class'),
   energy_per_task_j=r.get('energy_per_work_j'),power_w=r.get('average_power_w'),energy_j=r.get('energy_total_j'),performance_fps=r.get('fps'),
   actual_duration_s=r.get('active_duration_s'),claim_eligible=r.get('claim_eligible'),physical_scope=r.get('energy_physical_scope'),window=r.get('energy_window'),
   precision=r.get('execution_precision'),calibration_sha256=r.get('energy_calibration_sha256'),valid_repeats=r.get('energy_repeat_valid_n'),
   physical_attempts=r.get('energy_physical_collector_attempt_count'),failed_attempts=r.get('energy_failed_physical_collector_attempt_count'),
   decoder_sha256=r.get('decoder_contract_sha256'),nms_sha256=r.get('nms_contract_sha256'),quality_relative_loss=r.get('accuracy_relative_loss'))
  assert r['ok'] is True and c['valid_repeats']==3,c
  aggregate=read(r['energy_aggregate_source_path']);records=aggregate['runs'];assert len(records)==3
  values=[];powers=[];fps=[]
  for i,rep in enumerate(records):
   n=rep['energy_work_units_used'];t=rep['active_duration_s'];e=rep['energy_total_j'];power=rep['avg_power_w'];jpt=rep['energy_per_work_unit_j'];values.append(e/n);powers.append(e/t);fps.append(n/t)
   checks.extend([dict(check='energy_per_completed_task',case_uid=uid,repetition=i,reported=jpt,recomputed=e/n,abs_error=abs(jpt-e/n)),dict(check='energy_power',case_uid=uid,repetition=i,reported=power,recomputed=e/t,abs_error=abs(power-e/t))])
   energy_reps.append({**common(r,cohort),'case_uid':uid,'repetition':i,'completed_count':n,'active_duration_s':t,'energy_j':e,'reported_j_per_task':jpt,
    'recomputed_j_per_task':e/n,'reported_power_w':power,'recomputed_power_w':e/t,'energy_window_throughput_fps':n/t,
    'source_run_index':rep.get('run_index'),'reused_logical_repeat':bool(rep.get('campaign_reused_repeat'))})
  c.update(energy_window_throughput_fps=statistics.mean(fps),energy_window_throughput_fps_sd=statistics.stdev(fps),j_per_task_sd=statistics.stdev(values))
  checks.append(dict(check='energy_case_mean',case_uid=uid,reported=c['energy_per_task_j'],recomputed=statistics.mean(values),abs_error=abs(c['energy_per_task_j']-statistics.mean(values))))
  energy_cases.append(c)
 coverage=csvread(a.corrected/'korrigierte_falltabellen/F06_matrix_588.csv')
 coverage_rows=[]
 for r in coverage:
  c=common(r,'base');c.update(status=r.get('build_runtime_state'),raw_representation=r.get('raw_representation'),quality_completion=r.get('quality_completion'),quality_decision=r.get('quality_decision'),measurement_endpoint=r.get('measurement_endpoint'),variant=r.get('variant'))
  coverage_rows.append(c)
 for name,rows in [('native_cases',native_cases),('generic_cases',gc_cases),('performance_repeats',perf_reps),('completion_pairs',public_pairs),('generic_raw',rawrows),('generic_short_predecessors',short),('quality',quality),('energy_cases',energy_cases),('energy_repeats',energy_reps),('coverage',coverage_rows),('arithmetic_checks',checks)]:csvwrite(inputs/(name+'.csv'),rows)
 counts=dict(generic_raw_base=len(rawrows),generic_short_predecessor_rows=len(short),quality=len(quality),quality_classes=dict(Counter(r['accuracy_class'] for r in quality)),
 native_cases=len(native_cases),native_full=sum(r['execution_mode']=='full' for r in native_cases),native_repeats=sum(r['measurement']=='native_completed' for r in perf_reps),
 generic_completed_cases=len(gc_cases),generic_completed_repeats=sum(r['measurement']=='generic_completed' for r in perf_reps),generic_completed_tasks=sum(r['completed_count'] for r in perf_reps if r['measurement']=='generic_completed'),
 energy_cases=len(energy_cases),energy_repeats=len(energy_reps),native_terminal_counts=native_terminal_counts,quality_policy=quality_policy,arithmetic_check_count=len(checks),arithmetic_max_abs_error=max(r['abs_error'] for r in checks))
 write(inputs/'inventory.json',counts);write(a.private_index.parent/'reporter_replay_summary.json',replay_summaries);print(json.dumps(counts,indent=2))
if __name__=='__main__':main()
