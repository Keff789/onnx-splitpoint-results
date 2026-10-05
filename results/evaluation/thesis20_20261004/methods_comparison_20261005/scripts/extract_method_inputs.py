#!/usr/bin/env python3
"""Bounded projection of saved candidate metadata and frozen profile parameters.
Reads no ONNX payload, executes no model/benchmark, writes only the separate output.
"""
import argparse,csv,hashlib,json
from pathlib import Path
import yaml
FIELDS=['case_id','boundary','cut_bytes','cut_mb_val','cut_mib_val','n_cut_tensors','part2_input_count','unknown_count','flops_left_abs','flops_right_abs','total_flops','flops_left_ratio','imbalance_val','peak_left_mib_val','peak_right_mib_val','strict_ok','accelerator_fit_score','accelerator_fit_profile','predicted_bottleneck_ms','predicted_handover_ms','predicted_handover_ms_raw','predicted_stream_cycle_ms','predicted_stream_fps','predicted_total_latency_ms','predicted_transfer_latency_ms','throughput_calibration_enabled','throughput_calibration_profile','source_rank','rank','workflow_ranking_method']

def write_csv(path,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(dict.fromkeys(k for r in rows for k in r)),lineterminator='\n');writer.writeheader()
        for row in rows:writer.writerow({k:json.dumps(v,separators=(',',':')) if isinstance(v,(dict,list)) else v for k,v in row.items()})

def main():
    p=argparse.ArgumentParser();p.add_argument('--base-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);a=p.parse_args()
    if a.output_root.resolve().is_relative_to(a.base_root.resolve()):raise ValueError('output must be separate')
    profiles=[yaml.safe_load((a.base_root/name).read_text()) for name in ['profile.yaml','profile_source.yaml']]
    policy=profiles[0]['ranking_validation'];source_policy=profiles[1]['ranking_validation'];assert policy==source_policy
    parameters=dict(ranking_validation=policy,source_role='BASE',source_files=['profile.yaml','profile_source.yaml'],profile_source_sha256=hashlib.sha256((a.base_root/'profile_source.yaml').read_bytes()).hexdigest(),profile_resolved_sha256=hashlib.sha256((a.base_root/'profile.yaml').read_bytes()).hexdigest(),ranking_model_bundle_configured=bool(profiles[0].get('campaign',{}).get('ranking_model_bundle')),system_spec_by_model={},candidate_provenance=[])
    rows=[]
    for model in sorted((a.base_root/'models').iterdir()):
        ranking_path=model/'analysis/candidate_ranking.json';ranking=json.loads(ranking_path.read_text());candidates=ranking['candidates']
        system_path=model/'benchmark_set/legacy_benchmark_set.json';system=json.loads(system_path.read_text()).get('system_spec');parameters['system_spec_by_model'][model.name]=system
        parameters['candidate_provenance'].append(dict(model_id=model.name,source_path=str(ranking_path.relative_to(a.base_root)),source_sha256=hashlib.sha256(ranking_path.read_bytes()).hexdigest(),source_artifact_id=ranking['artifact_id'],source_list_length=len(candidates),system_spec_source=str(system_path.relative_to(a.base_root)),system_spec_available=system is not None))
        identity_order={r['case_id']:i for i,r in enumerate(sorted(candidates,key=lambda r:(r['boundary'],r['case_id'])))}
        for index,candidate in enumerate(candidates):
            rows.append(dict(model_id=model.name,source_list_order=index,original_order=identity_order[candidate['case_id']],**{field:candidate.get(field) for field in FIELDS}))
    write_csv(a.output_root/'inputs/method_graph_features.csv',rows)
    (a.output_root/'inputs/method_parameters.json').write_text(json.dumps(parameters,indent=2)+'\n')
    print(json.dumps(dict(graph_candidates=len(rows),profile_match=True,system_spec_available=sum(v is not None for v in parameters['system_spec_by_model'].values()))))
if __name__=='__main__':main()
