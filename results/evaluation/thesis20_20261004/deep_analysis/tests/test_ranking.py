"""Focused checks on new descriptive derivations, never hardware tests."""
import importlib.util
import itertools
import math
from pathlib import Path
import pytest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('analyze_ranking',ROOT/'scripts/analyze_ranking.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)


def test_regret_denominators_are_distinct():
    assert r.regrets(50,100)==(.5,1)
    assert r.regrets(100,100)==(0,0)
    with pytest.raises(ValueError): r.regrets(101,100)


@pytest.mark.parametrize('values,k', [([1,2,4,8],2),([1,2,4,8],3),([1,4,4,4],2),([2,2,2,2],3)])
def test_exact_random_shortlist_equals_exhaustive_subsets(values,k):
    subsets=list(itertools.combinations(values,k));best=max(values)
    actual=r.random_shortlist(values,k)
    assert actual['random_subset_count']==len(subsets)
    assert actual['random_hit_probability']==pytest.approx(sum(max(x)==best for x in subsets)/len(subsets))
    assert actual['random_expected_L_R']==pytest.approx(sum(r.regrets(max(x),best)[0] for x in subsets)/len(subsets))
    assert actual['random_expected_L_C']==pytest.approx(sum(r.regrets(max(x),best)[1] for x in subsets)/len(subsets))


def test_false_quality_gate_cannot_be_repaired_by_reference_close():
    row=dict(eligible_for_technical_transfer=True,eligible_for_quality_transfer=False,generic_task_quality_status='reference_close',native_task_quality_status='reference_close')
    assert r.admitted(row,'technical')
    assert not r.admitted(row,'qualitytransfer')
    assert not r.admitted(row,'reference_close')
    row.update(eligible_for_quality_transfer=True,generic_task_quality_status='accuracy_loss')
    assert r.admitted(row,'qualitytransfer') and not r.admitted(row,'reference_close')


def test_duplicate_and_alias_collision_are_rejected():
    row=dict(model_id='m',case_id='b1',setup_id='s',comparison_backend='deepx')
    with pytest.raises(ValueError):r.unique_index([row,row.copy()])
    raws=[dict(row,variant='split',throughput_fps=1),dict(row,comparison_backend='deepx_m1',variant='split',throughput_fps=1)]
    with pytest.raises(ValueError):r.raw_join([],raws)


def test_raw_join_requires_identity_and_projection_and_excludes_augmentation():
    p=dict(model_id='m',case_id='b1',setup_id='s',comparison_backend='deepx',observation_origin='base',historical_generic_raw_fps=2,generic_completed_task_fps=3,native_completed_task_fps=4)
    raw=dict(p,variant='split',comparison_backend='deepx_m1',throughput_fps=2,measurement_endpoint='logits')
    common,audit=r.raw_join([p,dict(p,case_id='b2',observation_origin='augmentation')],[raw])
    assert len(common)==len(audit)==1 and audit[0]['used']
    assert not r.raw_join([dict(p,case_id='wrong')],[raw])[0]
    with pytest.raises(ValueError):r.raw_join([p],[dict(raw,throughput_fps=2.1)])


class RankStub:
    @staticmethod
    def _pairwise_counts(x,y):return 0,0
    @staticmethod
    def _spearman(x,y):return None
    @staticmethod
    def _kendall_tau_b(x,y):return None


def test_stable_top1_and_tie_sensitive_regret_remain_explicit():
    rows=[dict(case_id='first',generic_completed_task_fps=10,native_completed_task_fps=5),dict(case_id='second',generic_completed_task_fps=10,native_completed_task_fps=10),dict(case_id='third',generic_completed_task_fps=1,native_completed_task_fps=10)]
    result=r.metric(rows,RankStub)
    assert result['generic_selected_case']=='first'
    assert result['generic_top_ties']==2 and result['native_top_ties']==2
    assert not result['top1_hit_stable'] and not result['top1_hit_tie_aware']
    assert result['L_R']==.5 and result['L_C']==1
    assert result['tie_L_R_min']==0 and result['tie_L_R_max']==.5
    reversed_tie=[rows[2],rows[1],rows[0]]
    result=r.metric(reversed_tie,RankStub)
    assert not result['top1_hit_stable'] and result['top1_hit_tie_aware']
    assert result['L_R']==result['L_C']==0


def test_insufficient_groups_remain_visible_without_rank_claim():
    rows=[dict(case_id='a',generic_completed_task_fps=1,native_completed_task_fps=2)]
    result=r.metric(rows,RankStub)
    assert result['n']==1 and result['status']=='insufficient_candidates'
    assert result['L_C'] is None and result['top1_hit_stable'] is None


def test_all_original_groups_and_reproduction(tmp_path):
    import os
    source=Path(os.environ['THESIS20_SOURCE_ROOT'])
    original_spec=importlib.util.spec_from_file_location('original_rank_metrics',source/'scripts/project_rank_metrics.py')
    original=importlib.util.module_from_spec(original_spec);original_spec.loader.exec_module(original)
    first=tmp_path/'first';second=tmp_path/'second';first.mkdir();second.mkdir()
    r.analyze(source,first)
    pairs=r.read_csv(source/'inputs/completion_pairs.csv')
    with (first/'tables/rank_groups.csv').open(newline='') as handle:
        import csv
        actual_groups=list(csv.DictReader(handle))
    checked=0
    for cohort,rows in [('base',[x for x in pairs if x['observation_origin']=='base']),('augmented',pairs)]:
        expected={r.stratum(x):x for x in original._groups(rows)}
        for actual in actual_groups:
            if actual['cohort']!=cohort:continue
            tier='quality' if actual['tier']=='qualitytransfer' else actual['tier']
            reference=expected[r.stratum(actual)]
            for name,old in [('n','candidate_count'),('rho','spearman_rho'),('tau_b','kendall_tau_b'),('pairwise_concordance','pairwise_concordance'),('L_C','native_regret_at_1')]:
                value=None if not actual[name] else float(actual[name]);expected_value=reference[tier+'_'+old]
                if expected_value is None:assert value is None
                else:assert value==pytest.approx(expected_value,abs=1e-12,rel=0)
            checked+=1
    assert checked==126
    r.analyze(source,second)
    generated=['ranking_results.json']+[str(x.relative_to(first)) for x in sorted((first/'tables').glob('rank_*.csv'))]
    assert len(generated)==9
    assert all((first/name).read_bytes()==(second/name).read_bytes() for name in generated)
