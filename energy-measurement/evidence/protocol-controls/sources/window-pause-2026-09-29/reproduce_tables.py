#!/usr/bin/env python3
"""Recreate six exact CSV field selections from fingerprinted review exports."""
import argparse
import csv
import json
from pathlib import Path
from zipfile import ZipFile
from verify import digest, require


def reproduce(sources, out):
    here = Path(__file__).resolve().parent
    reg = {s['id']: s for s in json.loads((here/'sources.json').read_text())['sources']}
    for sid in ('S04', 'S06', 'S07'):
        s = reg[sid]
        path = sources / s['name']
        require(path.is_file() and digest(path) == s['sha256'], 'Bad source: '+s['name'])
    out.mkdir(parents=True, exist_ok=False)

    def read(sid, member):
        with ZipFile(sources/reg[sid]['name']) as z:
            return json.loads(z.read(member))

    def emit(name, rows):
        with (here/'data'/name).open(newline='', encoding='utf-8') as f:
            fields = next(csv.reader(f))
        with (out/name).open('x', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fields, extrasaction='ignore', lineterminator='\n')
            writer.writeheader()
            writer.writerows(rows)
        require((out/name).read_bytes() == (here/'data'/name).read_bytes(), 'Mismatch: '+name)

    a = read('S06', 'jetson_ab_review_20260928/data/comparison.json')
    p = read('S07', 'jetson_pause_review_20260929/data/summary.json')
    emit('iteration_runs.csv', a['runs'])
    emit('timeout_rates.csv', [r for r in a['rates'] if r['protocol'] == 'timeout100'])
    emit('pause_runs.csv', p['runs'])
    emit('pause_window_sensitivity.csv', p['threshold_sensitivity'])
    emit('pause_latency_groups.csv', [dict(run_id=r['index'], conditioning=r['conditioning'],
         pause_s=r['pause_s'], group_of_ten=i+1, gpu_latency_mean_ms=v)
         for r in p['runs'] for i, v in enumerate(r['gpu_latency_10query_groups_ms'])])
    rows = []
    with ZipFile(sources/reg['S04']['name']) as z:
        for name in sorted(n for n in z.namelist() if n.startswith('runs/') and n.endswith('.json')):
            r = json.loads(z.read(name))
            o = {k:r[k] for k in ('rate_Sps','run_id','order','yaml_sha256','status','recomputed_minus_yaml_J')}
            for pre, key in [('legacy','legacy_selected'),('unforced','legacy_detector_unforced')]:
                for field in ('start_index_inclusive','stop_index_inclusive','assumed_interval_span_s',
                              'energy_J','mean_power_W'):
                    o[pre+'_'+field] = r['windows'][key][field]
            rows.append(o)
    rows.sort(key=lambda r:(r['rate_Sps'], r['run_id']))
    emit('window_runs.csv', rows)
    print('PASS: six CSVs byte-identical; no raw-sample integration or hardware access.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sources', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True, help='New output directory')
    args = parser.parse_args()
    try:
        reproduce(args.sources, args.out)
    except (OSError, ValueError, KeyError) as exc:
        raise SystemExit('FAILED: '+str(exc))
