"""Small mathematical/identity regressions for the new energy derivation only.
Run: THESIS20_SOURCE_ROOT=/path/to/public python -m unittest discover -s tests -p test_energy.py -v
"""
import contextlib
import importlib.util
import io
import math
import os
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/analyze_energy.py'
spec=importlib.util.spec_from_file_location('deep_energy_analysis',SCRIPT)
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)

class EnergyMathTests(unittest.TestCase):
    def test_mean_of_ratios_is_not_ratio_of_totals(self):
        rr=[dict(repetition=i,energy_j=e,completed_count=n,active_duration_s=t) for i,(e,n,t) in enumerate([(10,2,2),(30,10,5),(60,30,10)])]
        r=a.summarize_repeats(rr)
        self.assertAlmostEqual(r['j_per_task_mean'],10/3)
        self.assertAlmostEqual(r['j_per_task_pooled'],100/42)
        self.assertNotEqual(r['j_per_task_pooled'],r['j_per_task_mean'])
        for q in rr:self.assertAlmostEqual(q['energy_j']/q['completed_count'],(q['energy_j']/q['active_duration_s'])/(q['completed_count']/q['active_duration_s']))

    def test_duplicate_baseline_is_rejected(self):
        with self.assertRaises(ValueError):a.unique_index([{'id':'same'},{'id':'same'}],lambda r:r['id'])

    def test_repeat_identity_is_not_inferred_from_count(self):
        rr=[dict(repetition=0,energy_j=2,completed_count=2,active_duration_s=2) for _ in range(3)]
        with self.assertRaises(ValueError):a.summarize_repeats(rr)

    def test_pareto_direction_and_ties(self):
        rr=[dict(case_uid=k,energy_fps_mean=r,j_per_task_mean=j) for k,r,j in [('fast',10,2),('low',5,1),('dominated',4,3),('tied',5,1)]]
        self.assertEqual(a.pareto_flags(rr),{'fast':True,'low':True,'dominated':False,'tied':True})

    def test_stable_tie_selection(self):
        rr=[dict(case_id='b002',case_uid='2',m=1),dict(case_id='b001',case_uid='1',m=1)]
        self.assertEqual(a.winner(rr,'m')['case_id'],'b001')

    def test_grouping_preserves_calibration_and_precision(self):
        r={k:'same' for k in a.GROUP_FIELDS}
        for k in ['calibration_sha256','precision','window','output_endpoint_id','setup_id']:
            self.assertNotEqual(a.groupkey(r),a.groupkey(dict(r,**{k:'different'})))

    def test_empty_summary_preserves_unknown_quantiles(self):
        r=a.joint_summary([])
        self.assertEqual(r['n_pairs'],0)
        self.assertIsNone(r['energy_ratio_median'])

@unittest.skipUnless(os.environ.get('THESIS20_SOURCE_ROOT'),'set THESIS20_SOURCE_ROOT for existing-input integration checks')
class ExistingInputTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=Path(os.environ['THESIS20_SOURCE_ROOT']);cls.tmp=tempfile.TemporaryDirectory(prefix='thesis20-energy-tests-');cls.out=Path(cls.tmp.name)
        with contextlib.redirect_stdout(io.StringIO()):cls.result=a.analyze(cls.source,cls.out)
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()

    def test_exact_case_baseline_and_semantic_counts(self):
        r=self.result
        self.assertEqual((r['case_n'],r['split_n'],r['full_n'],r['repeat_n']),(246,204,42,738))
        self.assertEqual((r['descriptive_pair_n'],r['semantic_pair_n'],r['semantic_limit_n']),(408,392,16))
        full=a.read_csv(self.out/'tables/energy_full_baselines.csv')
        self.assertEqual(sum(x['pair_reuse_count'] for x in full),408)
        self.assertEqual(len({x['case_uid'] for x in full}),42)

    def test_product_pareto_membership_is_preserved(self):
        old=a.read_csv(self.source/'tables/within_stratum_pareto.csv');new=a.read_csv(self.out/'tables/energy_pareto.csv')
        for src,dst in [('all_valid_quality','technical'),('reference_close','reference_close_transfer')]:
            oldmap={(r['model_id'],r['case_id'],r['setup_id']):r['pareto'] for r in old if r['filter']==src}
            newmap={(r['model_id'],r['case_id'],r['setup_id']):r['pareto'] for r in new if r['view']=='augmented' and r['filter']==dst}
            self.assertEqual(oldmap,newmap)

    def test_attestor_exclusion_does_not_replace_baselines(self):
        rr=a.read_csv(self.out/'tables/energy_sensitivity.csv')
        for r in rr:
            if r['attestor_gap']=='excluded' and r['baseline_kind']=='tensorrt_full':
                self.assertEqual(r['n_pairs'],0);self.assertEqual(r['n_unique_fulls'],0);self.assertIsNone(r['energy_ratio_median'])
        self.assertEqual((self.result['attestor_gap_full_n'],self.result['attestor_gap_pair_n']),(21,204))

    def test_mixed_original_baseline_field_never_controls_primary_ratio(self):
        rows=a.read_csv(self.out/'tables/energy_legacy_field_audit.csv')
        self.assertEqual(sum(r['original_baseline_field_role']=='host_normalized_secondary_estimate' for r in rows),192)
        for r in rows:self.assertTrue(math.isclose(r['original_descriptive_ratio'],r['recomputed_raw_fs_ratio'],rel_tol=1e-12))
        self.assertEqual(self.result['secondary_host_normalization_n'],21)

    def test_filter_exclusions_are_visible_even_empty_groups(self):
        rr=a.read_csv(self.out/'tables/energy_group_distributions.csv')
        for view in ['base','augmentation_only','augmented']:
            for filt in ['descriptive','semantic','semantic_reference_close','semantic_reference_close_transfer']:
                self.assertEqual(sum(r['view']==view and r['filter']==filt for r in rr),42)

    def test_deterministic_regeneration(self):
        again=self.out/'again'
        with contextlib.redirect_stdout(io.StringIO()):a.analyze(self.source,again)
        names=[p.relative_to(self.out) for p in (self.out/'tables').glob('energy_*.csv')]+[Path('energy_results.json')]
        for n in names:self.assertEqual((self.out/n).read_bytes(),(again/n).read_bytes(),str(n))

if __name__=='__main__':unittest.main()
