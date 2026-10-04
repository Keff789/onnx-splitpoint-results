import csv,importlib.util,math
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('quality_graph',ROOT/'scripts/analyze_quality_graph.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
def rows(name):
    with (ROOT/'tables'/name).open() as f:return list(csv.DictReader(f))
class QualityGraphTests(unittest.TestCase):
    def test_percent_point_and_relative_denominators(self):
        pp,rel=module.changes(.72,.8)
        self.assertAlmostEqual(pp,-8);self.assertAlmostEqual(rel,-10)
        self.assertEqual(module.changes(.1,0), (10,None))
    def test_duplicate_identity_rejected(self):
        with self.assertRaises(ValueError):module.unique_index([{'id':'x'},{'id':'x'}],['id'])
    def test_quality_original_decisions_and_intervals(self):
        q=rows('quality_effects.csv');self.assertEqual(len(q),560)
        self.assertEqual(sum(r['accuracy_class']=='accuracy_loss' for r in q),39)
        for r in q:
            self.assertAlmostEqual(float(r['delta_pp']),100*(float(r['candidate'])-float(r['reference'])))
            self.assertLessEqual(float(r['relative_loss_ci_low']),float(r['relative_loss_ci_high']))
            self.assertEqual(float(r['original_absolute_margin']),.01)
            self.assertEqual(float(r['relative_loss_threshold']),.05)
    def test_graph_join_complete_and_no_full_in_graph(self):
        r=rows('graph_completed_cases.csv');self.assertEqual(len(r),204)
        self.assertEqual(len({(x['model_id'],x['case_id'],x['setup_id']) for x in r}),204)
        self.assertTrue(all(x['case_id']!='full' and x['graph_feature_available']=='True' for x in r))
        for x in r:self.assertAlmostEqual(float(x['topological_position']),(int(x['boundary'])+1)/int(x['node_count']))
    def test_scope_sums_do_not_double_count_fulls(self):
        r=rows('coverage_matrix.csv');self.assertEqual(sum(int(x['generic_required']) for x in r),588)
        self.assertEqual(sum(int(x['generic_measured']) for x in r),527)
        self.assertEqual(sum(int(x['native_full']) for x in r),42)
        self.assertEqual(sum(int(x['native_unsupported']) for x in r),228)
        self.assertEqual(sum(int(x['completed_base']) for x in r),192)
        self.assertEqual(sum(int(x['completed_added']) for x in r),12)
    def test_constant_features_are_unknown_not_zero_correlation(self):
        for r in rows('graph_associations.csv'):
            if int(r['distinct_feature_values'])<2:self.assertEqual(r['rho'],'')
    def test_quality_full_companions_never_join_as_split(self):
        q=rows('quality_pair_join_audit.csv');self.assertEqual(len(q),204)
        self.assertTrue(all(r['quality_variant']=='split' for r in q))
        self.assertEqual(sum(r['accuracy_class']=='accuracy_loss' for r in q),17)
        losses=rows('quality_losses.csv')
        self.assertEqual(sum(r['variant']=='vendor_full' for r in losses),9)
        self.assertEqual(sum(r['variant']=='split' for r in losses),30)
if __name__=='__main__':unittest.main()
