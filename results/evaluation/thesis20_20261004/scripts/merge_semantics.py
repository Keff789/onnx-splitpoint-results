#!/usr/bin/env python3
"""Curate existing original pair flags plus the separately verified local replay.
The local projection annotates comparison evidence; original files/gates remain.
"""
import argparse,shutil,json
from pathlib import Path
from extract_inputs import read,write,csvread,csvwrite,SETUP

def main():
 p=argparse.ArgumentParser();p.add_argument('--corrected',type=Path,required=True);p.add_argument('--semantic-source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();dest=a.output/'inputs/semantics';dest.mkdir(parents=True,exist_ok=True)
 for f in a.semantic_source.iterdir():
  if f.is_file() and f.suffix in ['.csv','.json','.md']:shutil.copy2(f,dest/f.name)
 if (a.semantic_source/'scripts').is_dir():shutil.copytree(a.semantic_source/'scripts',dest/'scripts',dirs_exist_ok=True)
 fields=['model','case','setup_id','split_backend','baseline_backend','baseline_kind','descriptive_comparable','semantic_comparable','semantic_comparison_reasons','claim_comparable','split_energy_per_work_j','baseline_energy_per_work_j','descriptive_energy_ratio','split_active_duration_s','baseline_active_duration_s','precision','split_boundary_precision','baseline_runtime_precision','energy_scope','energy_window_effective','energy_calibration_sha256']
 rows=[]
 for i,r in enumerate(read(a.corrected/'scientific-corrected-v2/native_energy_pair_comparison.json')):
  c={k:r.get(k) for k in fields};c['model_id']=c.pop('model');c['case_id']=c.pop('case');c['setup_id']=SETUP[c['setup_id']];c.update(cohort='base',evidence_id=f'BASE-PAIR-{i+1:03}',semantic_comparable_original=c['semantic_comparable'],semantic_projection_origin='corrected_original_report',runtime_conditions_comparable=False);rows.append(c)
 energies=csvread(a.output/'inputs/energy_cases.csv')
 for r in csvread(dest/'yolo_energy_semantic_projection_24.csv'):
  setup=SETUP[r['setup_id']]
  split=next(x for x in energies if x['cohort']=='augmentation' and x['model_id']==r['model_id'] and x['case_id']==r['case_id'] and x['setup_id']==setup and x['backend']==r['split_backend'])
  full=next(x for x in energies if x['cohort']=='base' and x['model_id']==r['model_id'] and x['case_id']=='full' and x['setup_id']==setup and x['backend']==r['baseline_backend'])
  rows.append(dict(r,setup_id=setup,cohort='augmentation',semantic_comparable_original=False,semantic_projection_origin='original_stored_outputs_local_functional_replay',claim_comparable=False,split_energy_per_work_j=split['energy_per_task_j'],baseline_energy_per_work_j=full['energy_per_task_j'],descriptive_energy_ratio=split['energy_per_task_j']/full['energy_per_task_j'],split_active_duration_s=split['actual_duration_s'],baseline_active_duration_s=full['actual_duration_s'],precision=split['precision'],baseline_runtime_precision=full['precision'],energy_scope=split['physical_scope'],energy_window_effective=split['window'],energy_calibration_sha256=split['calibration_sha256']))
 csvwrite(a.output/'inputs/energy_split_full_pairs.csv',rows)
 print(json.dumps({'pairs':len(rows),'descriptive':sum(r['descriptive_comparable'] is True for r in rows),'semantic_projected':sum(r['semantic_comparable'] is True for r in rows),'claim':sum(r['claim_comparable'] is True for r in rows)},indent=2))
if __name__=='__main__':main()
