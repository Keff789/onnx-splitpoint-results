"""Read small saved reports only; project additional quality/graph evidence.

No ONNX load, inference, imports from historical packages, or recomputation of
quality/bootstrap. Original source paths are supplied explicitly by the operator.
"""
import argparse
import csv
import json
from pathlib import Path

SETUP = {'orin_nx_hailo8_01':'H8','orin_nx_hailo10_01':'H10','orin_nx_deepx_m1_01':'DeepX'}
def read(p): return json.loads(p.read_text())
def csvwrite(p, rows):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=list(dict.fromkeys(k for r in rows for k in r)), lineterminator='\n')
        w.writeheader(); w.writerows(rows)
def main():
    a=argparse.ArgumentParser()
    for k in ['base','corrected','yolo','output_root']: a.add_argument('--'+k.replace('_','-'),type=Path,required=True)
    args=a.parse_args(); out=args.output_root/'inputs'
    for src in (args.base,args.corrected,args.yolo):
        if args.output_root.resolve().is_relative_to(src.resolve()): raise ValueError('Output must be separate')
    quality=[]
    for cohort, source in [('base',args.corrected/'scientific-corrected-v2'),('augmentation',args.yolo/'runs/yolo_min3_20261002_222904/reports/scientific')]:
        csv.field_size_limit(20000000)
        with (source/'central_quality_results.csv').open() as f: central=list(csv.DictReader(f))
        for i,r in enumerate(read(source/'task_quality_reference_comparison.json')):
            # Match the central consumer by identity and numeric values; backend
            # labels differ in the existing reporting projection (e.g. deepx).
            metric='Top1' if r['task']=='classification' else 'COCO_AP_50_95'
            aliases={'deepx_m1':'deepx','deepx_m1_to_tensorrt':'deepx','deepx_to_trt':'deepx','hailo8_to_trt':'hailo8','hailo10_to_tensorrt':'hailo10h','hailo10h_to_trt':'hailo10h','hailo10':'hailo10h','ort_tensorrt':'tensorrt'}
            candidates=[x for x in central if x['model_id']==r['model'] and x['case_id']==r['case_id'] and x['setup_id']==r['setup_id'] and aliases.get(x['backend'],x['backend'])==aliases.get(r['backend'],r['backend']) and (x['variant']=='composed')==(r['variant']=='split') and abs(float(x['task_quality_candidate'])-r['row_'+metric])<1e-12]
            assert len(candidates)==1,(cohort,i,len(candidates))
            c=candidates[0]; ac=r['accuracy_assessment']; ci=ac.get('relative_loss_ci') or [None,None]
            quality.append(dict(quality_id=f'{cohort}_quality_{i:03d}',cohort=cohort,model_id=r['model'],case_id=r['case_id'],setup_id=SETUP.get(r['setup_id'],r['setup_id']),backend=r['backend'],variant=r['variant'],metric=metric,original_absolute_margin=c['task_quality_margin'],accuracy_policy_id=ac['policy_id'],relative_loss_threshold=0.05,relative_loss_ci_low=ci[0],relative_loss_ci_high=ci[1],uncertainty=ac['uncertainty'],confidence_level=ac['confidence_level'],source_role=cohort+'_central_quality_and_reference_comparison'))
    csvwrite(out/'quality_policy_details.csv',quality)
    # Numeric policy is explicit in existing frozen accuracy_reporting_v1;
    # the old 0.01 absolute margin is a different, retained historical field.
    graph=[]
    for model in sorted((args.base/'models').iterdir()):
        analysis=read(model/'analysis/analysis.json'); ranking=read(model/'analysis/candidate_ranking.json')
        for r in ranking['candidates']:
            graph.append(dict(model_id=model.name,case_id=r['case_id'],boundary=r['boundary'],node_count=analysis['node_count'],topological_position=(r['boundary']+1)/analysis['node_count'],cut_bytes=r.get('cut_bytes'),n_cut_tensors=r.get('n_cut_tensors'),part2_input_count=r.get('part2_input_count'),stored_flops_left_ratio=r.get('flops_left_ratio'),stored_total_flops=r.get('total_flops'),stored_predicted_stream_fps=r.get('predicted_stream_fps'),stored_predicted_bottleneck_ms=r.get('predicted_bottleneck_ms'),prediction_calibration_profile=r.get('throughput_calibration_profile'),source_role='base_saved_candidate_ranking'))
    assert len({(r['model_id'],r['case_id']) for r in graph})==len(graph)
    csvwrite(out/'graph_features.csv',graph)
    excluded=read(args.base/'reports/native_expected_matrix.json')['excluded_expected_rows']
    csvwrite(out/'native_unsupported.csv',[dict(model_id=r['model'],case_id=r['case'],setup_id=SETUP[r['setup_id']],backend=r['backend'],precision=r['precision'],status=r['actual_status'],reason=r['primary_failure_reason'],part2_input_count=r.get('native_capability_exclusion',{}).get('part2_input_count')) for r in excluded])
    print(json.dumps(dict(quality_details=len(quality),graph_candidates=len(graph),unsupported=len(excluded))))
if __name__=='__main__': main()
