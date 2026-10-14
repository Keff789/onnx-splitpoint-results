#!/usr/bin/env python3
"""Behavioral regression tests for scientific selection and aggregation boundaries."""
import copy
import json
from pathlib import Path
import statistics
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import build_paper_dataset as tool


def repeat(joules, images, index=0):
    return {'energy_j':joules,'completed_tasks':images,'duration_s':10,
            'repeat':index,'source_sha256':'sensor-'+str(index)}


class ScientificEdgeCases(unittest.TestCase):
    def test_energy_means_reciprocal_and_pooled_are_distinct(self):
        s = tool.energy_statistics([repeat(2,1,0),repeat(30,10,1),repeat(400,100,2)])
        self.assertAlmostEqual(s['mean_E_over_N'],3)
        self.assertAlmostEqual(s['mean_N_over_E'],(1/2+1/3+1/4)/3)
        self.assertAlmostEqual(s['reciprocal_mean_E_over_N'],1/3)
        self.assertAlmostEqual(s['sum_E_over_sum_N'],432/111)
        self.assertAlmostEqual(s['sum_N_over_sum_E'],111/432)
        self.assertNotAlmostEqual(s['mean_N_over_E'],s['reciprocal_mean_E_over_N'])
        self.assertNotAlmostEqual(s['mean_E_over_N'],s['sum_E_over_sum_N'])

    def test_single_repeat_has_no_invented_ci_or_stdev(self):
        s = tool.energy_statistics([repeat(2,10)])
        self.assertEqual(s['n_energy'],1)
        self.assertIsNone(s['energy_mean_ci95_low'])
        self.assertIsNone(s['energy_mean_ci95_high'])
        self.assertIsNone(s['energy_cv'])

    def test_large_observed_variation_is_retained(self):
        s = tool.energy_statistics([repeat(.01,1,0),repeat(1,1,1),repeat(100,1,2)])
        self.assertEqual(s['n_energy'],3)
        self.assertGreater(s['energy_cv'],1)
        self.assertEqual(s['energy_min'],.01)
        self.assertEqual(s['energy_max'],100)

    def test_reexport_is_not_an_independent_repeat(self):
        r = repeat(2,10)
        with self.assertRaises(AssertionError):
            tool.energy_statistics([r,dict(r)])

    def test_energy_denominator_must_be_positive(self):
        with self.assertRaises(AssertionError):
            tool.energy_statistics([repeat(2,0)])

    def test_latest_matching_completed_value_not_fastest_or_mtime(self):
        rows = [dict(source_id='old',completed=True,completed_at='2026-01-01',fps=100,host='A',runtime='TRT',input_hw=224,endpoint='logits'),
                dict(source_id='new',completed=True,completed_at='2026-02-01',fps=80,host='A',runtime='TRT',input_hw=224,endpoint='logits'),
                dict(source_id='empty',completed=True,completed_at='2026-03-01',fps=None,host='A',runtime='TRT',input_hw=224,endpoint='logits'),
                dict(source_id='failed',completed=False,completed_at='2026-04-01',fps=1000,host='A',runtime='TRT',input_hw=224,endpoint='logits')]
        for r in rows:
            r['cut']='b001'
        identity = dict(host='A',runtime='TRT',input_hw=224,endpoint='logits',cut='b001')
        for key,value in [('host','B'),('runtime','other'),('input_hw',320),('endpoint','boxes'),('cut','b002')]:
            rows.append(dict(rows[1],source_id='wrong-'+key,completed_at='2026-05-01',**{key:value}))
        self.assertEqual(tool.select_metric(rows,'fps',identity)['source_id'],'new')

    def test_metric_specific_historical_fallback_fills_only_real_gap(self):
        rows = [dict(source_id='old',completed=True,completed_at='2026-01-01',fps=100,energy=.1,host='A'),
                dict(source_id='new',completed=True,completed_at='2026-02-01',fps=80,energy=None,host='A')]
        self.assertEqual(tool.select_metric(rows,'fps',{'host':'A'})['source_id'],'new')
        self.assertEqual(tool.select_metric(rows,'energy',{'host':'A'})['source_id'],'old')
        rows[1]['energy'] = .3
        self.assertEqual(tool.select_metric(rows,'energy',{'host':'A'})['source_id'],'new')

    def test_new_worse_dataset_quality_wins_by_measurement_time(self):
        rows = [dict(source_id='old',completed=True,completed_at='2026-01-01',quality=.9,host='A'),
                dict(source_id='new',completed=True,completed_at='2026-02-01',quality=.1,host='A')]
        self.assertEqual(tool.select_metric(rows,'quality',{'host':'A'})['quality'],.1)

    def test_zero_accuracy_and_negative_relative_loss_are_real_observations(self):
        rows = [dict(source_id='old',completed=True,completed_at='2026-01-01',quality_value=.9,quality_relative_loss=.05,host='A'),
                dict(source_id='new',completed=True,completed_at='2026-02-01',quality_value=0,quality_relative_loss=-.02,host='A')]
        self.assertEqual(tool.select_metric(rows,'quality_value',{'host':'A'})['quality_value'],0)
        self.assertEqual(tool.select_metric(rows,'quality_relative_loss',{'host':'A'})['quality_relative_loss'],-.02)

    def test_models_are_not_point_weighted(self):
        rows = [dict(model='many',setup='H8',fps_ratio=2,energy_ratio=.5) for _ in range(20)]
        rows += [dict(model='few',setup='H8',fps_ratio=4,energy_ratio=1.5)]
        groups,models,equal = tool.equal_model_summary(rows)
        all_models = next(r for r in equal if r['setup']=='all')
        self.assertEqual(all_models['n_models'],2)
        self.assertEqual(all_models['fps_ratio'],3)
        self.assertEqual(all_models['energy_ratio'],1)
        self.assertNotAlmostEqual(all_models['fps_ratio'],statistics.mean(r['fps_ratio'] for r in rows))

    def test_build_preserves_fps_only_bad_quality_and_same_full_energy(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp); inp=base/'inputs'; inp.mkdir()
            template = json.loads((ROOT/'inputs/cases.json').read_text())[0]
            rows=[]; er=[]; evidence=[]
            def add(case,backend,kind,runner,fps,energy,samples=None):
                r=copy.deepcopy(template)
                r.update(model_id='fixture',setup_id='DeepX',case_id=case,backend=backend,
                         kind=kind,runner=runner,fps=fps,fps_samples=samples if samples is not None else [fps],
                         performance_observations=len(samples) if samples is not None else 1,
                         raw_j_per_task=energy,comparison_j_per_task=energy,
                         quality_class='accuracy_loss',quality_relative_loss=.8,
                         normal_performance_claim=False,normal_energy=False,energy_claim=False,
                         completion_mode=None,energy_repeat_n=1 if energy is not None else 0)
                r.pop('refresh16',None)
                r['uid']='|'.join([runner,'fixture','DeepX',backend,case])
                rows.append(r)
                evidence.append(dict(uid=r['uid'],quality_value=.1,quality_reference_value=.5,quality_numeric_relative_loss=.8,
                                     quality_metric='top1',quality_n=5000,execution_notes=['unknown remains unknown']))
                if energy is not None:
                    er.append(dict(repeat(energy*10,10),uid=r['uid'],j_per_task=energy))
                return r['uid']
            vendor=add('full','native_full_deepx','full','native',90,.05)
            trt=add('full','native_full_tensorrt','full','native',100,.1)
            no_energy=add('a','deepx_to_trt','split','native',120,None)
            second=add('b','deepx_to_trt','split','native',110,.2)
            add('c','deepx_to_trt','split','native',110,.4)
            add('a','deepx_to_trt','split','generic',60,.15)
            for name,value in [('cases',rows),('selected_evidence',evidence),('energy_repeats',er),('pipeline_repeats',[]),('split_full_contracts',[])]:
                (inp/(name+'.json')).write_text(json.dumps(value))
            config=json.loads((ROOT/'config.json').read_text())
            a,b=base/'a',base/'b'
            summary=tool.build(inp,a,config)
            tool.build(inp,b,config)
            data={r['uid']:r for r in json.loads((a/'PAPER_DATASET.json').read_text())}
            self.assertTrue(data[no_energy]['included_performance'])
            self.assertFalse(data[no_energy]['included_energy'])
            self.assertEqual(data[no_energy]['performance_n'],1)
            self.assertEqual(data[second]['quality_value'],.1)
            self.assertEqual(data[second]['quality_class'],'accuracy_loss')
            self.assertIsNone(data[second]['completion_mode'])
            top=json.loads((a/'tables/table3_top2_native.json').read_text())
            self.assertEqual([r['split_uid'] for r in top],[no_energy,second])
            self.assertTrue(all(r['baseline_uid']==trt for r in top))
            self.assertIsNone(top[0]['energy_gain_same_full'])
            self.assertEqual(top[1]['energy_gain_same_full'],.5)
            self.assertEqual(top[1]['lowest_energy_full_uid'],vendor)
            self.assertEqual(summary['performance_coverage'],6)
            self.assertEqual(summary['energy_coverage'],5)
            self.assertEqual(summary['native_generic']['n_performance'],1)
            self.assertEqual(summary['native_generic']['n_energy'],0)
            pareto={r['uid']:r for r in json.loads((a/'tables/PARETO_POINTS.json').read_text())}
            self.assertEqual(set(pareto),set(data))
            self.assertFalse(pareto[no_energy]['included'])
            self.assertEqual(pareto[no_energy]['omission_reason'],'missing_energy_mj_per_image')
            self.assertTrue(pareto[second]['included'])
            opts=json.loads((a/'tables/model_setup_optima.json').read_text())
            singleton=next(r for r in opts if r['runner']=='generic')
            self.assertEqual(singleton['candidate_count'],1)
            self.assertFalse(singleton['multiple_candidates'])
            self.assertTrue(singleton['same_optimum'])
            for path in a.rglob('*'):
                if path.is_file():
                    self.assertEqual(path.read_bytes(),(b/path.relative_to(a)).read_bytes(),str(path.relative_to(a)))


class ParetoEdgeCases(unittest.TestCase):
    @staticmethod
    def point(uid, fps, energy, **changes):
        row = dict(uid=uid, model_id='model', setup_id='H8', runner='native',
                   kind='split', backend='split_backend', case_id=uid, fps=fps,
                   energy_mj_per_image=energy, quality_value=.7, quality_metric='top1')
        row.update(changes)
        return row

    def calculate(self, rows):
        return {r['uid']:r for r in tool.pareto_points(rows)}

    def test_maximize_fps_minimize_energy_and_deterministic_witness(self):
        rows = [self.point('slow_hot', 1, 10), self.point('z_fast_cool', 9, 2),
                self.point('a_fast_cool', 10, 1)]
        p = self.calculate(rows)
        self.assertEqual({u for u,r in p.items() if r['pareto_all']}, {'a_fast_cool'})
        self.assertEqual(p['slow_hot']['dominated_by_uid'], 'a_fast_cool')
        self.assertIsNone(p['a_fast_cool']['dominated_by_uid'])
        self.assertEqual(tool.pareto_points(rows), tool.pareto_points(list(reversed(rows))))

    def test_tied_coordinates_keep_every_uid_without_mutating_inputs(self):
        rows = [self.point('a', 10, 2), self.point('b', 10, 2), self.point('c', 5, 3)]
        original = copy.deepcopy(rows)
        p = self.calculate(rows)
        self.assertEqual({u for u,r in p.items() if r['pareto_all']}, {'a','b'})
        self.assertEqual(p['c']['dominated_by_uid'], 'a')
        self.assertEqual(rows, original)

    def test_same_fps_only_lower_energy_is_front(self):
        p = self.calculate([self.point('cool', 10, 1), self.point('hot', 10, 2)])
        self.assertTrue(p['cool']['pareto_all'])
        self.assertFalse(p['hot']['pareto_all'])

    def test_same_energy_only_higher_fps_is_front(self):
        p = self.calculate([self.point('slow', 5, 1), self.point('fast', 10, 1)])
        self.assertTrue(p['fast']['pareto_all'])
        self.assertFalse(p['slow']['pareto_all'])

    def test_singleton_front_is_one_observation(self):
        p = self.calculate([self.point('single', 10, 2)])['single']
        self.assertTrue(p['pareto_all'])
        self.assertTrue(p['pareto_native'])
        self.assertIsNone(p['pareto_generic'])
        self.assertIsNone(p['dominated_by_uid'])
        self.assertEqual(tool.pareto_points([]), [])

    def test_real_tradeoffs_are_all_front_without_rounding(self):
        rows = [self.point('low', 1, 1), self.point('middle', 2, 2),
                self.point('high', 3, 3), self.point('rounded_tie', 1.0000000001, 1)]
        p = self.calculate(rows)
        self.assertEqual({u for u,r in p.items() if r['pareto_all']},
                         {'middle','high','rounded_tie'})
        self.assertEqual(p['low']['dominated_by_uid'], 'rounded_tie')

    def test_model_and_setup_fronts_are_separate(self):
        p = self.calculate([self.point('strong', 100, 1),
                            self.point('other_model', 2, 20, model_id='other'),
                            self.point('other_setup', 2, 20, setup_id='DeepX')])
        self.assertTrue(all(r['pareto_all'] for r in p.values()))

    def test_full_alternatives_and_runner_fronts_have_different_populations(self):
        p = self.calculate([self.point('n', 10, 5), self.point('g', 8, 4, runner='generic'),
                            self.point('trt', 15, 3, kind='full', backend='native_full_tensorrt'),
                            self.point('vendor', 20, 2, kind='full', backend='native_full_hailo8')])
        self.assertEqual({u for u,r in p.items() if r['pareto_all']}, {'vendor'})
        self.assertTrue(p['n']['pareto_native'])
        self.assertTrue(p['g']['pareto_generic'])
        self.assertIsNone(p['n']['pareto_generic'])
        self.assertIsNone(p['g']['pareto_native'])
        self.assertIsNone(p['trt']['pareto_native'])
        self.assertIsNone(p['vendor']['pareto_native'])

    def test_missing_quality_and_old_flags_never_filter_or_change_front(self):
        rows = [self.point('poor', 10, 1, quality_value=0, quality_class='accuracy_loss',
                           quality_relative_loss=.99, normal_performance_claim=False,
                           energy_claim=False, included_joint=False, contract_sha256=None),
                self.point('missing', 12, 2, quality_value=None),
                self.point('nonfinite', 15, 3, quality_value=float('nan'))]
        p = self.calculate(rows)
        self.assertTrue(all(r['included'] and r['pareto_all'] for r in p.values()))
        self.assertEqual(p['poor']['quality_percent'], 0)
        self.assertIsNone(p['missing']['quality_percent'])
        self.assertIsNone(p['nonfinite']['quality_percent'])
        json.dumps(list(p.values()), allow_nan=False)

    def test_missing_nonfinite_and_invalid_axes_are_never_zero_filled(self):
        rows = [self.point('missing', None, 1), self.point('nan', float('nan'), 1),
                self.point('infinite', 10, float('inf')), self.point('boolean', True, 1),
                self.point('text', 10, '1'), self.point('both', None, None)]
        p = self.calculate(rows)
        self.assertTrue(all(not r['included'] for r in p.values()))
        self.assertTrue(all(r['pareto_all'] is None and r['dominated_by_uid'] is None
                            for r in p.values()))
        self.assertEqual(p['missing']['omission_reason'], 'missing_fps')
        self.assertEqual(p['nan']['omission_reason'], 'nonfinite_fps')
        self.assertEqual(p['infinite']['omission_reason'], 'nonfinite_energy_mj_per_image')
        self.assertEqual(p['boolean']['omission_reason'], 'invalid_fps')
        self.assertEqual(p['text']['omission_reason'], 'invalid_energy_mj_per_image')
        self.assertEqual(p['both']['omission_reason'], 'missing_fps;missing_energy_mj_per_image')
        self.assertIsNone(p['nan']['fps'])
        self.assertIsNone(p['infinite']['energy_mj_per_image'])
        json.dumps(list(p.values()), allow_nan=False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
