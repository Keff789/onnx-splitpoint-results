#!/usr/bin/env python3
"""Read-only file and table checks; not a new hardware or raw-sample validation."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from statistics import median


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def table(root, name):
    with (root / 'data' / name).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def verify(root, sources=None):
    root = root.resolve()
    seen = set()
    for line in (root / 'SHA256SUMS').read_text().splitlines():
        expected, rel = line.split('  ', 1)
        path = (root / rel).resolve()
        require(path.is_relative_to(root) and rel not in seen, 'Bad manifest path')
        require(path.is_file() and digest(path) == expected, 'Hash mismatch: ' + rel)
        seen.add(rel)
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()
              and p.name != 'SHA256SUMS' and '__pycache__' not in p.parts}
    require(actual == seen, 'Missing/unmanifested files: ' + str(actual ^ seen))
    source_count = 0
    if sources is not None:
        for s in json.loads((root / 'sources.json').read_text())['sources']:
            path = sources / s['name']
            require(path.is_file() and path.stat().st_size == s['bytes']
                    and digest(path) == s['sha256'], 'Source mismatch: ' + s['name'])
            source_count += 1
    iterations = table(root, 'iteration_runs.csv')
    windows = table(root, 'window_runs.csv')
    require(len(iterations) == len(windows) == 45, 'Expected 45 iteration records')
    require(sorted(int(r['order']) for r in iterations) == list(range(1, 46)), 'Order')
    require(all(float(r['queries']) == 100 and float(r['warmup_queries']) == 1
                and r['passed'] == 'True' and int(r['exit_code']) == 0
                for r in iterations), 'Incomplete benchmark record')
    result = {'status': 'PASS', 'files_verified': len(seen),
              'sources_verified': source_count, 'windows': [], 'pause': []}
    for rate, expected in [(2000, 3998.095333943686),
                           (250000, 3942.563415703736),
                           (5000000, 3679.184790318036)]:
        rows = [r for r in windows if int(r['rate_Sps']) == rate]
        require(sorted(int(r['run_id']) for r in rows) == list(range(15)), 'Run IDs')
        for r in rows:
            require(r['status'] == 'OK', 'Bad window status')
            for pre in ('legacy', 'unforced'):
                span = (int(r[pre+'_stop_index_inclusive']) -
                        int(r[pre+'_start_index_inclusive'])) / rate
                require(math.isclose(span, float(r[pre+'_assumed_interval_span_s']),
                                     abs_tol=1e-9, rel_tol=0), 'Span')
                require(math.isclose(float(r[pre+'_energy_J']) / span,
                                     float(r[pre+'_mean_power_W']), rel_tol=1e-12), 'Power')
        energy = median(float(r['unforced_energy_J']) for r in rows)
        require(abs(energy - expected) < 1e-8, 'Unforced median')
        result['windows'].append({'rate_Sps': rate, 'n': 15, 'median_unforced_J': energy})
    pause = table(root, 'pause_runs.csv')
    require(sorted(int(r['index']) for r in pause) == list(range(7)), 'Pause IDs')
    require(sum(r['conditioning'] == 'True' for r in pause) == 1
            and pause[0]['conditioning'] == 'True', 'Conditioner')
    for gap, expected in [(20, 3836.71926153621), (120, 3646.6867354585916)]:
        rows = [r for r in pause if int(r['pause_s']) == gap and r['conditioning'] == 'False']
        require(len(rows) == 3, 'Pause repeats')
        energy = median(float(r['energy_J']) for r in rows)
        require(abs(energy - expected) < 1e-8, 'Pause median')
        result['pause'].append({'pause_s': gap, 'n': 3, 'median_energy_J': energy})
    latency = table(root, 'pause_latency_groups.csv')
    require(len(latency) == 70, 'Latency count')
    for i in range(7):
        require(sorted(int(r['group_of_ten']) for r in latency if int(r['run_id']) == i)
                == list(range(1, 11)), 'Latency groups')
    timeout = table(root, 'timeout_rates.csv')
    require(len(timeout) == 27 and all(int(r['n']) == 15 for r in timeout), 'Timeout')
    result['limits'] = 'Export/integrity check; no raw NPY/Parquet or hardware verification.'
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sources', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(verify(Path(__file__).parent, args.sources), indent=2))
    except (OSError, ValueError, KeyError) as exc:
        raise SystemExit('FAILED: ' + str(exc))
