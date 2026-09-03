# Effective execution plan

```text
Run mode: YOLOv7 paper split b066 — Hailo-8 Native Full + Energy, B500 (standard)
Artifact policy: normal · compiler dispatch=allowed
Models: 1 — yolov7_paper
Deployment shortlist/model: 1 · shortlist=1 · strategy=stratified_windows
Part-2 input count = 1: requested=on · effective=on (Native capability: reject and deterministically backfill; Generic remains technically multi-input/multi-output capable)
Score-independent audit candidates: none (development=none; hold-out=none; minimum valid=none)
Execution union candidates/model: {'yolov7_paper': '1'} (audit + deployment shortlist, deduplicated; configured range)
Generic normalized result rows (planned): 4 ({'yolov7_paper': 4}; logical runs=3)
Remote benchmark invocations: 1 (1/model)
Suite uploads: cold cache <= 1 (1/model); warm cache = 0
Setup groups: hailo8_setup=[hailo8, hailo8_to_trt, ort_tensorrt]
Validation: exact run-mode subsets {'classification': 500, 'detection': 500} · estimated embedded files=1002
Task Quality: bootstrap=500 · benchmark warmup/runs=3/5
Quality reference: central_management · workers=4 · management profiles=['ort_cpu']
Hailo: preset=balanced · opt=1 · calibration storage=memmap
DeepX classification preprocessing: imagenet_mean_std · cache contract=v2_exact_explicit · cache root=~/Models/BackendArtifacts/deepx
Native: on · full baselines=on · frames/warmup=1000/100 · performance repetitions=3 · queue/inflight=3/8 · contract=1c31fa8655d6
Energy: Generic=off · Native=on (mode default=on; profile override) · path=native_only
Remote TensorRT cache: on
```
