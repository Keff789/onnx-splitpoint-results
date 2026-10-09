#!/usr/bin/env python3
"""Figure 5: median paired power differences; percentile data remain in the artifact."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
WORKLOADS = ['gemm_fp32','gemm_fp16','gemm_int8','yolo_fp32','yolo_fp16','yolo_int8','random_pattern_yolo']
LABELS = ['GEMM-FP32','GEMM-FP16','GEMM-INT8','YOLO-FP32','YOLO-FP16','YOLO-INT8','Variable YOLO']
SENSORS = [('firmware','u.RECS','o'),('jetson','INA3221 telemetry','s'),('shelly','Shelly (scaled AC)','^')]

def render(root: Path = ROOT) -> Path:
    pairs = pd.read_csv(root/'generated/parma_device_pair_values.csv')
    source = pd.read_csv(root/'generated/parma_device_pair_spread.csv')
    assert len(pairs)==315 and pairs.record_id.nunique()==105
    assert len(source)==21 and source.n.eq(15).all()
    rows=[]
    for w in WORKLOADS:
        for sensor, label, marker in SENSORS:
            p=pairs[pairs.slug.eq(w)&pairs.sensor.eq(sensor)]
            assert len(p)==15 and p.record_id.is_unique
            delta=100*(p.sensor_W.to_numpy()/p.pico_W.to_numpy()-1)
            median=float(np.median(delta))
            s=source[source.slug.eq(w)&source.sensor.eq(sensor)].iloc[0]
            assert np.isclose(median,s.paired_median_pct,atol=1e-10,rtol=0)
            rows.append(dict(slug=w,sensor=sensor,n=15,median_pct=median,
                             q05_pct=float(np.quantile(delta,.05)),q95_pct=float(np.quantile(delta,.95))))
    data=pd.DataFrame(rows)
    data.to_csv(root/'generated/device_pair_medians.csv',index=False)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.labelsize':9,
                         'xtick.labelsize':8,'ytick.labelsize':9,'legend.fontsize':8,'pdf.fonttype':42})
    fig=plt.figure(figsize=(5.5,3.0));ax=fig.add_axes([.23,.17,.74,.68])
    y=np.array([6,5,4,3,2,1,-.45])
    for off,(sensor,label,marker) in zip([.20,0,-.20],SENSORS):
        sub=data[data.sensor.eq(sensor)].set_index('slug').loc[WORKLOADS]
        ax.plot(sub.median_pct.to_numpy(),y+off,linestyle='None',marker=marker,
                markersize=4.7,label=label)
    # Exactly between the continuous workload group and variable YOLO.
    ax.axhline(.25,lw=.65,ls=':')
    ax.axvline(0,lw=.8,ls='--')
    ax.set(yticks=y,yticklabels=LABELS,xlim=(-7.1,3.65),ylim=(-1.05,6.6),
           xlabel='Mean-power difference from PicoScope (%)')
    ax.set_xticks([-6,-4,-2,0,2]);ax.grid(axis='x',alpha=.18,lw=.6)
    ax.set_axisbelow(True)
    handles,labels=ax.get_legend_handles_labels()
    fig.legend(handles,labels,loc='upper center',bbox_to_anchor=(.52,1),ncol=3,
               frameon=False,handlelength=1,columnspacing=1.0)
    target=root/'figures/device_pair_medians.pdf'
    fig.savefig(target,metadata={'CreationDate':None,'ModDate':None})
    fig.savefig(target.with_suffix('.png'),dpi=220)
    plt.close(fig)
    (root/'generated/device_figure_qa.json').write_text(json.dumps({
        'status':'PASS','groups':21,'pairs_per_group':15,'paired_comparisons':315,
        'unique_executions':105,'metric':'median of per-execution signed mean-power differences',
        'uncertainty_bars_displayed':False,'full_percentiles_retained':True,
        'new_measurements':False,'raw_waveform_integration':False},indent=2)+'\n')
    return target

if __name__=='__main__':
    print(render())
