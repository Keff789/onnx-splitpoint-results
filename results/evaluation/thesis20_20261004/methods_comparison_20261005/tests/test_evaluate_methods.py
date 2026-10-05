"""Focused offline ranking mathematics and frozen-input regression checks."""
import contextlib,importlib.util,io,itertools,math,os,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('method_evaluation',ROOT/'scripts/evaluate_methods.py');e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)

class RankFixture:
    _spearman=staticmethod(lambda x,y:None)
    _kendall_tau_b=staticmethod(lambda x,y:None)

def rows(values):
    return [dict(case_id=f'b{i}',utility=u,native_fps=n,j_per_task=j,pair_order=i,original_order=o) for i,(u,n,j,o) in enumerate(values)]

class MathTests(unittest.TestCase):
    def test_score_direction_does_not_convert_bytes_into_runtime_volume(self):
        self.assertEqual(e.utility(1048576,'ascending'),-1048576)
        self.assertEqual(e.utility(200,'descending'),200)
        self.assertIsNone(e.utility(float('nan'),'ascending'))
        with self.assertRaises(ValueError):e.utility(1,'guessed')

    def test_regret_denominators(self):
        self.assertEqual(e.regrets(50,100),(.5,1))
        with self.assertRaises(ValueError):e.regrets(100,50)

    def test_original_method_order_and_energy_metric(self):
        rr=rows([(10,50,4,2),(10,100,2,1),(0,10,1,0)])
        m=e.evaluate_group(rr,RankFixture)
        self.assertEqual(m['selected_case'],'b1');self.assertTrue(m['top1_hit_tie_aware'])
        self.assertEqual(m['energy_excess_fraction'],1);self.assertEqual(m['energy_lost_savings_fraction'],.5)
        self.assertEqual(m['tie_L_R_min'],0);self.assertEqual(m['tie_L_R_max'],.5)
        self.assertEqual(m['tie_energy_excess_min'],1);self.assertEqual(m['tie_energy_excess_max'],3)

    def test_missing_method_is_never_zero_score_or_replacement_candidate(self):
        rr=rows([(10,50,4,2),(None,100,2,1),(0,10,1,0)])
        m=e.evaluate_group(rr,RankFixture)
        self.assertEqual(m['status'],'incomplete_method_coverage');self.assertIsNone(m['selected_case']);self.assertEqual(m['n_missing'],1)

    def test_filtered_small_groups_remain_insufficient(self):
        m=e.evaluate_group(rows([(1,10,1,0),(0,5,2,1)]),RankFixture)
        self.assertEqual(m['status'],'insufficient_candidates');self.assertIsNone(m['L_R'])

    def test_exact_join_rejects_duplicate(self):
        with self.assertRaises(ValueError):e.exact_index([{'id':'a'},{'id':'a'}],['id'])

    def test_quality_exclusion_is_not_accuracy_loss(self):
        r=dict(eligible_for_technical_transfer=True,eligible_for_quality_transfer=False,generic_task_quality_status='reference_close',native_task_quality_status='reference_close')
        self.assertTrue(e.eligible(r,'technical'));self.assertFalse(e.eligible(r,'reference_close'))
        r.update(eligible_for_quality_transfer=True,generic_task_quality_status='accuracy_loss')
        self.assertTrue(e.eligible(r,'qualitytransfer'));self.assertFalse(e.eligible(r,'reference_close'))

    def test_random_subsets_equal_enumeration_with_ties(self):
        for ns in [[1,2,4,8],[1,4,4,4]]:
            for k in [1,2,3]:
                sub=list(itertools.combinations(ns,k));r=e.random_metrics(ns,k);best=max(ns)
                self.assertAlmostEqual(r['random_native_best_hit_probability'],sum(max(s)==best for s in sub)/len(sub))
                self.assertAlmostEqual(r['random_expected_L_R'],sum(e.regrets(max(s),best)[0] for s in sub)/len(sub))
                self.assertAlmostEqual(r['random_expected_L_C'],sum(e.regrets(max(s),best)[1] for s in sub)/len(sub))

    def test_boundary_tie_shortlist_bounds(self):
        rr=rows([(3,4,1,0),(2,1,1,1),(2,8,1,2),(2,2,1,3)])
        m=e.shortlist_metrics(rr,2)
        self.assertEqual(m['boundary_tie_resolutions'],3)
        self.assertEqual(m['tie_L_R_min'],0);self.assertEqual(m['tie_L_R_max'],.5)
        self.assertEqual(m['native_topk_recall'],.5)

    def test_top3_is_explicitly_trivial_at_n3(self):
        rr=rows([(3,4,1,0),(2,1,1,1),(1,8,1,2)])
        m=e.shortlist_metrics(rr,3);self.assertTrue(m['trivial_k_equals_n']);self.assertEqual(m['random_native_best_hit_probability'],1)

@unittest.skipUnless(os.environ.get('THESIS20_SOURCE_ROOT'),'set THESIS20_SOURCE_ROOT for frozen-input tests')
class FrozenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=Path(os.environ['THESIS20_SOURCE_ROOT']);cls.method=Path(os.environ.get('THESIS20_METHOD_ROOT',ROOT));cls.tmp=tempfile.TemporaryDirectory(prefix='thesis20-method-tests-');cls.output=Path(cls.tmp.name)
        with contextlib.redirect_stdout(io.StringIO()):cls.result=e.analyze(cls.source,cls.method,cls.output)
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()
    def test_generic_regression_and_existing_cohorts(self):
        self.assertEqual(self.result['cohort_counts'],{'technical':204,'qualitytransfer':201,'reference_close':184})
        self.assertEqual(self.result['base_raw_n'],192);self.assertEqual(self.result['generic_completion_regression_top1_hits'],10)
        self.assertEqual(self.result['generic_completion_regression_groups'],21);self.assertEqual(self.result['full_references_used'],0)
    def test_identical_evaluation_candidate_sets(self):
        rr=e.read_csv(self.output/'tables/method_groups.csv');groups={}
        for r in rr:
            if r['status'] not in ('ok','constant_scores'):continue
            k=(r['cohort'],r['tier'],*(r[s] for s in e.STRATUM))
            if k in groups:self.assertEqual(groups[k],r['candidate_ids'])
            groups[k]=r['candidate_ids']
        self.assertEqual(self.result['group_candidate_equality_checks'],len(groups))
    def test_unconfigured_handover_and_gui_do_not_gain_guessed_scores(self):
        rr=e.read_csv(self.output/'tables/method_groups.csv')
        for r in rr:
            if r['method'] in ['cycle_time_with_handover','gui_total_latency']:
                self.assertEqual(r['n_scored'],0);self.assertIsNone(r['L_R']);self.assertIsNone(r['selected_case'])
    def test_deterministic_csv_json_reproduction(self):
        second=self.output/'second'
        with contextlib.redirect_stdout(io.StringIO()):e.analyze(self.source,self.method,second)
        for p in sorted((self.output/'tables').glob('*.csv')):self.assertEqual(p.read_bytes(),(second/'tables'/p.name).read_bytes(),p.name)
        self.assertEqual((self.output/'method_evaluation_results.json').read_bytes(),(second/'method_evaluation_results.json').read_bytes())

if __name__=='__main__':unittest.main()
