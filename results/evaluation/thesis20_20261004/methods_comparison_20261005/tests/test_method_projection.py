"""Focused projection checks; no hardware, inference, or calibration."""
import importlib.util,json,os,sys
from pathlib import Path
import pytest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from reproduce_method_scores import derive_scores,read_csv,system_proxy,analyze
from method_core.ranking_methods import compute_ranking_predictions,candidate_cut_bytes,candidate_cut_mib


def test_cut_units_are_explicit_and_no_runtime_precision_conversion():
    assert candidate_cut_bytes({'cut_mb_val':1})==1_000_000
    assert candidate_cut_bytes({'cut_mib':1})==1_048_576
    assert candidate_cut_mib({'cut_bytes':1_048_576})==1
    assert candidate_cut_bytes({'cut_bytes':6_553_600,'precision':'uint8'})==6_553_600


def test_existing_method_ties_use_boundary_not_input_list_order():
    candidates=[dict(case_id='b020',boundary=20,cut_bytes=5,imbalance_val=1,n_cut_tensors=1),dict(case_id='b010',boundary=10,cut_bytes=5,imbalance_val=1,n_cut_tensors=1)]
    rows=compute_ranking_predictions(candidates,[],{})
    ranks={r['case_id']:r['predicted_rank'] for r in rows if r['method_id']=='cut_bytes_only'}
    assert ranks=={'b020':2,'b010':1}


def test_full_universe_weight_normalization_is_not_subset_normalization():
    candidates=[dict(case_id='a',boundary=1,cut_bytes=1,imbalance_val=1,n_cut_tensors=1),dict(case_id='b',boundary=2,cut_bytes=1e6,imbalance_val=.9,n_cut_tensors=1),dict(case_id='outside_measured',boundary=3,cut_bytes=1e6+1,imbalance_val=0,n_cut_tensors=1)]
    cfg={'weighted_score':{'w_comm':1,'w_imb':3,'w_tensors':.2,'log_comm':True}}
    full={r['case_id']:r['predicted_value'] for r in compute_ranking_predictions(candidates,[],cfg) if r['method_id']=='weighted_score'}
    subset={r['case_id']:r['predicted_value'] for r in compute_ranking_predictions(candidates[:2],[],cfg) if r['method_id']=='weighted_score'}
    assert full['a']<full['b'] and subset['a']>subset['b']


def test_unconfigured_native_handover_does_not_borrow_generic_prediction():
    c=dict(case_id='b1',boundary=1,cut_bytes=1,imbalance_val=0,n_cut_tensors=1,predicted_bottleneck_ms=2,predicted_handover_ms=999)
    context=dict(stage1='hailo8',stage2='tensorrt',runner_regime='native_fifo')
    row=next(r for r in compute_ranking_predictions([c],[context],{}) if r['method_id']=='cycle_time_with_handover')
    assert row['predicted_value'] is None
    assert row['prediction_source'].endswith('native_handover_model_unconfigured')


def test_missing_system_spec_never_uses_stored_fallback_latency():
    c=dict(cut_bytes=1e6,flops_left_abs=5e9,total_flops=1e10,predicted_total_latency_ms=999)
    assert system_proxy(c,None) is None
    assert system_proxy(c,{'left':{'gops':100}}) is None
    spec={'left':{'gops':100},'right':{'gops':200},'link':{'bandwidth_value':100,'bandwidth_unit':'MB/s','overhead_ms':2},'overhead_ms':1}
    assert system_proxy(c,spec)==pytest.approx(88)


def test_saved_whole_universe_source_parameters_and_scores():
    features=read_csv(ROOT/'inputs/method_graph_features.csv');params=json.loads((ROOT/'inputs/method_parameters.json').read_text())
    assert params['ranking_validation']['weighted_score']=={'w_comm':1.0,'w_imb':3.0,'w_tensors':.2,'log_comm':True}
    assert all(spec is None for spec in params['system_spec_by_model'].values())
    scores,verified=derive_scores(features,params)
    assert len(features)==2111 and len(scores)==14777 and len(verified)==7
    assert len({(r['model_id'],r['case_id'],r['method']) for r in scores})==len(scores)
    assert all(r['score'] is None for r in scores if r['method'] in {'gui_total_latency','cycle_time_with_handover'})
    assert all(r['score'] is not None for r in scores if r['method'] not in {'gui_total_latency','cycle_time_with_handover'})
    expected_order={(r['model_id'],r['case_id']):r['original_order'] for r in features}
    assert all(r['original_order']==expected_order[(r['model_id'],r['case_id'])] for r in scores)


def test_public_reproduction_and_global_no_fallback(tmp_path):
    source=Path(os.environ['THESIS20_SOURCE_ROOT'])
    first=tmp_path/'first';second=tmp_path/'second';analyze(ROOT,source,first);analyze(ROOT,source,second)
    files=[str(p.relative_to(first)) for p in sorted(first.rglob('*')) if p.is_file()]
    assert len(files)==5
    assert all((first/f).read_bytes()==(second/f).read_bytes() for f in files)
    global_rows=read_csv(first/'tables/method_global_selection.csv')
    row=next(r for r in global_rows if r['model_id']=='yolov7_paper' and r['setup_id']=='H8' and r['method']=='cut_bytes_only')
    assert row['selected_case_id']=='b306'
    assert row['completed_measurement_available'] is False
    assert row['native_support_status']=='unsupported_by_single_input_contract'
    assert row['no_fallback_to_measured_candidate'] is True
    assert row['native_fps'] is None and row['quality_status'] is None
