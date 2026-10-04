#!/usr/bin/env python3
"""Read-only original budget-chain audit and small predecessor projection."""
import argparse,json,hashlib
from collections import Counter
from pathlib import Path
from extract_inputs import read,write,csvwrite,csvread,common,SETUP

def main():
 p=argparse.ArgumentParser();p.add_argument('--base',type=Path,required=True);p.add_argument('--yolo-run',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--reporter-replay',type=Path);a=p.parse_args();out=a.output/'inputs'
 attempts=[]
 for cohort,root in [('base',a.base),('augmentation',a.yolo_run)]:
  data=read(root/'energy_task_budget.json')
  for identity,task in data['tasks'].items():
   key=json.loads(identity);diagnostic=key[0]=='energy_setup_test'
   backend,model,case,setup=(key[0],'setup_diagnostic','sleep_2s',key[2]) if diagnostic else key
   for i,c in enumerate(task['chains']):
    if c.get('collector_started') is not True:continue
    valid=c.get('valid') is True;finished=c.get('finished') is True;closed=c.get('source_completion_verified') is True
    if valid:assert finished and closed
    attempts.append(dict(cohort=cohort,role='setup_diagnostic' if diagnostic else 'campaign_energy',model_id=model,case_id=case,setup_id=SETUP.get(setup,'H10' if diagnostic else setup),backend=backend,
      row_attempt_index=i,logical_repeat=c.get('logical_repeat'),finished=finished,valid=valid,source_completion_verified=closed,
      outcome='valid' if valid else 'completed_failed' if finished else 'interrupted_unconfirmed',
      evidence_sha256=hashlib.sha256(json.dumps(c,sort_keys=True,separators=(',',':')).encode()).hexdigest()))
 csvwrite(out/'energy_physical_attempts.csv',attempts)
 short=[]
 for path in sorted((a.yolo_run/'models').glob('*/benchmark_results/normalized_results.json')):
  for r in read(path)['results']:
   c=common(r,'augmentation_short');c.update(throughput_fps=r.get('throughput_primary_fps'),measurement_endpoint=r.get('measurement_endpoint'),measurement='generic_short_predecessor',source_role='inventory_only');short.append(c)
 csvwrite(out/'generic_short_predecessors.csv',short)
 inv=read(out/'inventory.json');inv['energy_physical_attempts']={cohort:dict(Counter(r['outcome'] for r in attempts if r['cohort']==cohort and r['role']=='campaign_energy')) for cohort in ('base','augmentation')};inv['setup_diagnostic_attempts']=dict(Counter(r['outcome'] for r in attempts if r['role']=='setup_diagnostic'));write(out/'inventory.json',inv)
 for name in ['native_cases','performance_repeats']:
  rows=csvread(out/(name+'.csv'))
  for r in rows:
   if r['measurement']=='native_completed' and 'accuracy_class' in r:r['native_quality_gate_status']=r.pop('accuracy_class')
  csvwrite(out/(name+'.csv'),rows)
 if a.reporter_replay:
  exclusions=[]
  for cohort in ['base','augmentation']:
   for r in read(a.reporter_replay/cohort/'generic_completion_cross_runner.json')['pairs']:
    if not r['eligible_for_quality_transfer']:
     exclusions.append(dict(cohort=cohort,model_id=r['model_id'],case_id=r['case_id'],setup_id=SETUP[r['setup_id']],technical_eligible=r['eligible_for_technical_transfer'],quality_eligible=r['eligible_for_quality_transfer'],generic_quality=r['generic_task_quality_status'],native_quality=r['native_task_quality_status'],quality_exclusion_reasons=r['quality_exclusion_reasons']))
  csvwrite(out/'quality_transfer_exclusions.csv',exclusions)
 print(json.dumps({k:inv[k] for k in ('energy_physical_attempts','setup_diagnostic_attempts')},indent=2))
if __name__=='__main__':main()
