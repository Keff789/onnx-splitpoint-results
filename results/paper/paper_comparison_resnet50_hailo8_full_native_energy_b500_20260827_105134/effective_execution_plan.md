# Effective execution plan

```text
Run mode: Standard (balanced) (standard)
Artifact policy: normal · compiler dispatch=allowed
Models: 1 — resnet50
Deployment shortlist/model: 1 · shortlist=1 · strategy=stratified_windows
Part-2 input count = 1: requested=off · effective=off (selection only; Generic remains multi-input/multi-output capable)
Score-independent audit candidates: none (development=none; hold-out=none; minimum valid=none)
Execution union candidates/model: {'resnet50': '1'} (audit + deployment shortlist, deduplicated; configured range)
Generic normalized result rows (planned): 3 ({'resnet50': 3}; logical runs=2)
Remote benchmark invocations: 1 (1/model)
Suite uploads: cold cache <= 1 (1/model); warm cache = 0
Setup groups: hailo8_setup=[hailo8, ort_tensorrt]
Validation: exact run-mode subsets {'classification': 500, 'detection': 500} · estimated embedded files=501
Task Quality: bootstrap=500 · benchmark warmup/runs=3/5
Quality reference: central_management · workers=4 · management profiles=['ort_cpu']
Hailo: preset=balanced · opt=1 · calibration storage=memmap
DeepX classification preprocessing: imagenet_mean_std · cache contract=v2_exact_explicit · cache root=~/Models/BackendArtifacts/deepx
Native: on · full baselines=on · frames/warmup=1000/100 · performance repetitions=3 · queue/inflight=3/8 · contract=5cbfa17564a2
Energy: Generic=off · Native=on (mode default=off; profile override) · path=native_only
Remote TensorRT cache: on
Warnings:
  - Ranking transfer requires at least 3 measured candidates per comparable model/backend/contract group. Insufficient planned candidate counts: {'resnet50': 2}. For score-independent audits, this count comes from the audit universe and is not limited by max_accepted_cases_per_model. Performance and task-quality rows remain valid; Spearman/Kendall/Top-k transfer will be reported as insufficient_candidates.
```
