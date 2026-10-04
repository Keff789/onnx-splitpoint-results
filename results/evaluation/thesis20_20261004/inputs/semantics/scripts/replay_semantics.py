"""Offline, case-bound audit of saved detector outputs; never executes inference.

Inputs are the original energy pair CSV, final Native summary, corrected Native
validation, base validation, and the original base artifact index. Outputs go
to a new report directory. Source
contract verification uses the existing product processors without changing SHA
expectations. Tensor names are mapped only when shape/dtype identifies exactly
one tensor in each original declared signature. This tests processor behaviour,
not interchangeability of native artifact identities or scientific claim gates.
"""
import argparse,csv,json,re
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import numpy as np
from scripts import native_producer_validate_visualize as v
from onnx_splitpoint_tool.native_detection_postprocess import (
 FrozenDetectionPostprocessor,_AttestedDecodedNmsMaterializer,
 DetectionCompletionRuntime,verify_frozen_decoded_nms_normalization_contract)
from onnx_splitpoint_tool.validation.accuracy_gates import AccuracyGatePolicy
from onnx_splitpoint_tool.native_command_contract import verify_native_command_contract
from scripts.native_producer_energy_plan import _verify_full_command_contract


def read(p):return json.loads(Path(p).read_text())
def processor(c):
 if c['schema']=='onnx-splitpoint/attested-decoded-nms-materialization':
  return _AttestedDecodedNmsMaterializer(c)
 return FrozenDetectionPostprocessor(c)
def execute(p,arrays):
 r=p.process(arrays);r['detections']=p.last_detections;return r
def signature(c):return c.get('raw_output_tensor_signature') or c['source_output_tensor_signature']
def map_arrays(arrays,contract):
 result={}
 for t in signature(contract)['tensors']:
  hits=[(k,a) for k,a in arrays.items() if list(a.shape)==t['shape'] and str(a.dtype)==t['dtype']]
  if len(hits)!=1:raise ValueError('tensor_shape_dtype_mapping_missing_or_ambiguous')
  result[t['name']]=hits[0][1]
 if len(result)!=len(arrays):raise ValueError('unmapped_tensor')
 return result

def primitive_diff(a,b):
 # These fields identify the binding; they do not choose numerical operators.
 metadata={'contract_sha256','invariant_contract_sha256','invariant_identity',
 'source_output_endpoint_attestation_sha256'}
 result={}
 for k in sorted(set(a)|set(b)):
  if k in metadata:continue
  av,bv=a.get(k),b.get(k)
  if k in ('raw_output_tensor_signature','source_output_tensor_signature'):
   def shape(x):return [(t['index'],t['dtype'],t['rank'],t['shape']) for t in (x or {}).get('tensors',[])]
   av,bv=shape(av),shape(bv)
  if av!=bv:result[k]={'split':av,'full':bv}
 return result


def sha(value):
 value=str(value or '').removeprefix('sha256:')
 if not re.fullmatch(r'[0-9a-f]{64}',value):raise ValueError('original_sha256_missing_or_invalid')
 return value


@lru_cache(maxsize=4)
def energy_report(path):return read(path)

def original_energy_row(pair,role):
 source,pointer=pair[role+'_evaluation_role_source'].split('#',1)
 if not pointer.endswith('/row/evaluation_role'):raise ValueError('original_energy_row_pointer_invalid')
 report=energy_report(source);row=report
 for token in pointer.strip('/').split('/')[:-1]:row=row[int(token)] if isinstance(row,list) else row[token]
 expected=(pair['model'],pair['case'] if role=='split' else 'full',pair['setup_id'],pair[role+'_backend'])
 if tuple(row.get(k) for k in ('model','case','setup_id','backend'))!=expected:raise ValueError('original_energy_row_identity_mismatch')
 command=pair[role+'_command_contract_source']
 if row.get('command_contract_file')!=command:raise ValueError('original_command_source_path_mismatch')
 if v._sha256_file(command)!=sha(row.get('command_contract_file_sha256')):raise ValueError('original_command_file_sha256_mismatch')
 return row,report.get('plan_payload',{}).get('execution_context',{})

def verify_commands(split,full,pair,native,validated):
 split_energy,_=original_energy_row(pair,'split');full_energy,context=original_energy_row(pair,'baseline')
 if any(sha(row.get('successful_command_contract_sha256'))!=command['contract_sha256'] for row,command in ((split_energy,split),(full_energy,full))):raise ValueError('original_energy_command_identity_mismatch')
 identity={'model':pair['model'],'case':pair['case'],'setup_id':pair['setup_id'],'backend':pair['split_backend']}
 verified,status=verify_native_command_contract(split,expected_identity=identity)
 if verified is None:raise ValueError('split_command:'+status)
 full_identity={**identity,'case':'full','backend':pair['baseline_backend'],
  'model_sha256':pair['model_sha256'],'comparison_backend':validated.get('comparison_backend'),
  'remote_root':context['remote_root'],'remote_tool_dir':context['remote_tool_dir']}
 verified_full,full_status=_verify_full_command_contract(full,expected_identity=full_identity)
 if verified_full is None:raise ValueError('full_command:'+full_status)
 if sha(native.get('native_command_contract_sha256'))!=split['contract_sha256']:raise ValueError('split_row_command_mismatch')
 if sha(validated.get('full_command_contract_sha256'))!=full['contract_sha256']:raise ValueError('full_row_command_mismatch')
 image=sha(pair.get('prepared_feed_source_image_sha256'))
 if any(sha(c.get('input_image_sha256'))!=image for c in (split,full)):raise ValueError('pair_original_image_mismatch')
 return {'split_contract_sha256':split['contract_sha256'],'full_contract_sha256':full['contract_sha256'],
         'split_verifier':status,'full_verifier':full_status,'input_image_sha256':image,
         'split_command_file_sha256':split_energy['command_contract_file_sha256'],
         'full_command_file_sha256':full_energy['command_contract_file_sha256']}

def verified_dump(path,manifest_sha,index,index_root):
 path=Path(path)
 expected=sha(manifest_sha)
 if v._sha256_file(path)!=expected:raise ValueError('original_output_manifest_sha256_mismatch')
 payload=read(path);outputs=payload.get('outputs') or []
 if not outputs:raise ValueError('original_output_entries_missing')
 evidence=[]
 for entry in outputs:
  recorded=Path(entry['file']);resolved=recorded if recorded.is_absolute() else path.parent/recorded
  if not resolved.is_file():resolved=path.parent/recorded.name # Same exact sibling mapping as load_dump.
  declared=entry.get('sha256');authority='original_output_manifest'
  expected_size=entry.get('size_bytes',entry.get('bytes'))
  if not declared:
   try:relative=resolved.resolve().relative_to(index_root).as_posix()
   except ValueError as exc:raise ValueError('raw_output_outside_original_index') from exc
   matches=index.get(relative,set())
   if len(matches)!=1:raise ValueError('original_raw_sha256_missing_or_ambiguous')
   declared,index_size=next(iter(matches));authority='original_artifact_index'
   if expected_size!=index_size:raise ValueError('original_raw_index_size_conflict')
  expected_raw=sha(declared)
  if type(expected_size) is not int or expected_size<=0:raise ValueError('original_raw_size_missing')
  if resolved.stat().st_size!=expected_size or v._sha256_file(resolved)!=expected_raw:raise ValueError('original_raw_content_mismatch')
  evidence.append({'name':entry['name'],'sha256':expected_raw,'size_bytes':expected_size,'authority':authority})
 arrays,_=v.load_dump(str(path))
 return arrays,{'manifest_sha256':expected,'outputs':evidence}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pairs',required=True);ap.add_argument('--native',required=True);ap.add_argument('--validation',required=True);ap.add_argument('--base-validation',required=True);ap.add_argument('--out',required=True);ap.add_argument('--base-artifact-index',required=True)
 ns=ap.parse_args();out=Path(ns.out);out.mkdir(parents=True,exist_ok=True)
 nr=read(ns.native)['rows'];vr=read(ns.validation)['rows'];basevr=read(ns.base_validation)['rows']
 entries=[];records=[];negatives=[]
 index_path=Path(ns.base_artifact_index).resolve();index_root=index_path.parent;index=defaultdict(set)
 original_index=read(index_path)
 if original_index.get('run_id')!=index_root.name:raise ValueError('original_artifact_index_run_mismatch')
 for item in original_index['artifacts']:
  index[item['path']].add((str(item.get('sha256') or '').removeprefix('sha256:'),item.get('size_bytes')))
 index_sha=v._sha256_file(index_path)
 del original_index
 for n,pair in enumerate(csv.DictReader(open(ns.pairs)),1):
  s=read(pair['split_command_contract_source']);f=read(pair['baseline_command_contract_source'])
  ec=s['runtime_options']['completion_execution_contract'];sp=ec['processor_contract'];w=f['energy_workload']
  if w.get('frozen_postprocess_contract'):fp=w['frozen_postprocess_contract']
  else:
   nc=w['frozen_decoded_nms_normalization_contract'];verify_frozen_decoded_nms_normalization_contract(nc);fp=nc['materialization_contract']
  # Constructors verify each original contract, code sources and policies.
  sr=DetectionCompletionRuntime(ec);p1=processor(sp);p2=processor(fp)
  native=[r for r in nr if (r['model'],r['case'],r['setup_id'])==(pair['model'],pair['case'],pair['setup_id'])]
  full=[r for r in vr if (r['model'],r['case'],r['setup_id'],r['backend'])==(pair['model'],'full',pair['setup_id'],pair['baseline_backend'])]
  assert len(native)==len(full)==1
  native=native[0];full=full[0]
  bindings=verify_commands(s,f,pair,native,full)
  sa,split_dump=verified_dump(native['native_output_manifest'],native.get('output_manifest_sha256'),index,index_root)
  fa,full_dump=verified_dump(full['dump_manifest'],full.get('output_manifest_sha256'),index,index_root)
  bindings.update(split_output=split_dump,full_output=full_dump,original_base_artifact_index_sha256=index_sha)
  split_result=execute(sr,sa)
  full_result=execute(p2,map_arrays(fa,fp))
  diffs=primitive_diff(sp,fp);checks=[]
  if not diffs:
   for label,arrays in [('split_original_output',sa),('full_original_output',fa)]:
    a=execute(processor(sp),map_arrays(arrays,sp));b=execute(processor(fp),map_arrays(arrays,fp))
    assert a['detections']==b['detections'], 'processor_numeric_difference'
    checks.append({'source':label,'detections':len(a['detections']),'equal':True})
  previous=next(r for r in basevr if (r['model'],r['case'],r['setup_id'],r['backend'])==(pair['model'],'full',pair['setup_id'],pair['baseline_backend']))
  prior=read(full['task_validation']);ref=prior['self_reference_report']
  assert ref.get('exact_completed_result_identity_bound') is True
  assert v._canonical_detection_json_sha256(ref['reference_detections'])==ref['full_reference_result_sha256']
  # Full processor replay must reproduce the stored exact hotloop result.
  stored_exact=full_result['detections']==ref['native_detections']
  coordinate_delta=max((abs(float(a[k])-float(b[k])) for a,b in zip(full_result['detections'],ref['native_detections']) for k in ('score','x1','x2','y1','y2')),default=0) if len(full_result['detections'])==len(ref['native_detections']) else None
  policy=AccuracyGatePolicy()
  for field,value in {'numerical_similarity_threshold':policy.native_self_reference_min_match,
    'numerical_similarity_mean_iou_threshold':policy.native_self_reference_min_mean_iou,
    'numerical_similarity_iou_threshold':policy.native_self_reference_iou_threshold,
    'numerical_similarity_confidence_threshold':policy.native_self_reference_confidence_threshold}.items():
   assert ref[field]==value,field
  match=v._match_detections(ref['reference_detections'],full_result['detections'],iou_thr=policy.native_self_reference_iou_threshold)
  agnostic=v._match_detections_class_agnostic(ref['reference_detections'],full_result['detections'],iou_thr=policy.native_self_reference_iou_threshold)
  sim=v.evaluate_detection_similarity(match,agnostic,policy)
  full_ok=sim['numerical_similarity_pass'] is True
  if not full_ok and pair['baseline_kind']=='vendor_full':
   negatives.append({'model_id':pair['model'],'case_id':'full','setup_id':pair['setup_id'],'backend':pair['baseline_backend'],**sim,'stored_outputs_exist':True,'stored_hotloop_result_reproduced':stored_exact,'max_record_field_delta':coordinate_delta})
  descriptive=pair['descriptive_comparable']=='True';semantic=descriptive and not diffs and len(checks)==2 and full_ok and stored_exact
  reason=('verified_original_processors_equal_on_both_saved_outputs' if semantic else
    'stored_vendor_full_output_fails_original_similarity_policy' if not full_ok else
    'different_decoder_placement_no_common_primitive_input')
  row=dict(evidence_id=f'YOLO-SEM-{n:02d}',model_id=pair['model'],case_id=pair['case'],setup_id=pair['setup_id'],split_backend=pair['split_backend'],baseline_backend=pair['baseline_backend'],baseline_kind=pair['baseline_kind'],descriptive_comparable=descriptive,semantic_comparable=semantic,reason=reason,primitive_difference_fields=';'.join(diffs),functional_input_sets=len(checks),baseline_numerical_match=sim['numerical_similarity_value'],baseline_numerical_mean_iou=sim['numerical_similarity_mean_iou'],scientific_claim_eligible=False,runtime_conditions_comparable=False)
  records.append(row)
  entries.append(dict(**row,original_binding_verification=bindings,split_processor_contract=sp,full_processor_contract=fp,primitive_differences=diffs,functional_checks=checks,split_detection_count=len(split_result['detections']),full_detection_count=len(full_result['detections']),stored_hotloop_result_reproduced=stored_exact,max_record_field_delta=coordinate_delta,original_semantic_comparison_reasons=json.loads(pair['semantic_comparison_reasons'])))
  print(row['evidence_id'],row['model_id'],row['setup_id'],row['baseline_kind'],semantic,reason,flush=True)
 with (out/'yolo_energy_semantic_projection_24.csv').open('w') as f:
  dw=csv.DictWriter(f,fieldnames=records[0]);dw.writeheader();dw.writerows(records)
 (out/'yolo_energy_semantic_evidence.json').write_text(json.dumps({'inference_count':0,'original_contracts_modified':False,'claim_gates_modified':False,'entries':entries},indent=2)+'\n')
 (out/'two_full_negative_replay.json').write_text(json.dumps({'inference_count':0,'records':negatives},indent=2)+'\n')
if __name__=='__main__':main()
