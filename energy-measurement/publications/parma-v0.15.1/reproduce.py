#!/usr/bin/env python3
"""Reproduce PARMA Figure 5 from stored paired mean powers, not raw waveforms."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from figure import render

R=Path(__file__).resolve().parent
payload=json.loads((R/'pairs.json').read_text())
assert payload['columns']==['record_id','pico_W','firmware','jetson','shelly']
assert payload['requested_duration_s']==300 and payload['window']=='envelope_0.5'
assert len(payload['workloads'])==7
rows=[];execution_ids=set()
for slug,records in payload['workloads'].items():
    assert len(records)==15 and len({r[0] for r in records})==15
    for rid,pico,*powers in records:
        assert rid not in execution_ids, 'Repeated physical execution across workloads'
        execution_ids.add(rid)
        assert pico>0 and len(powers)==3 and all(np.isfinite(powers))
        for sensor,power in zip(['firmware','jetson','shelly'],powers):
            rows.append(dict(slug=slug,sensor=sensor,record_id=rid,pico_W=pico,
                sensor_W=power,paired_difference_pct=100*(power/pico-1)))
assert len(rows)==315 and len(execution_ids)==105
G=R/'generated';F=R/'figures';G.mkdir(exist_ok=True);F.mkdir(exist_ok=True)
pd.DataFrame(rows).to_csv(G/'parma_device_pair_values.csv',index=False)
expected=pd.read_csv(R/'summary.csv')
expected.rename(columns={'median_pct':'paired_median_pct','q05_pct':'paired_q05_pct',
                         'q95_pct':'paired_q95_pct'}).to_csv(G/'parma_device_pair_spread.csv',index=False)
render(R)
got=pd.read_csv(G/'device_pair_medians.csv').set_index(['slug','sensor'])
expected=expected.set_index(['slug','sensor'])
assert got.index.equals(expected.index)
for col in ['median_pct','q05_pct','q95_pct']:
    assert np.allclose(got[col],expected[col],rtol=0,atol=1e-10),col
print('PASS: 105 executions; 315 paired comparisons; all 21 medians and percentiles reproduced.')
print('Figure:', F/'device_pair_medians.pdf')
