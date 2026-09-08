# Run Status Summary — v27926_acceptance_d_yolo11l_b003_deepx_gpu_20260907_101443

Technical status: `failed`
Quality-evaluation technical status: `ok`
Aggregate quality decision: `not_evaluated`
Scientific status: `not_evaluated`
Legacy workflow status: `failed`
Workflow: `v2.79.26-deepx-full-diagnostics-fix`

## Native evidence axes
- Runtime: `incomplete`
- Semantics: `incomplete`
- Claim: `incomplete`
- Energy: `complete`

## Stage counts
- failed: 1
- ok: 15
- partial: 1
- warn: 1

## Blocking partial / failure reasons
- `yolo11l` / `run_benchmarks` / `partial` — Remote benchmark suite dispatched per hardware target/run-profile.; preserved 6 measured row(s), but the requested hardware matrix is incomplete; missing required profile row(s): tensorrt:full:full, tensorrt:split:b003, deepx_m1:full:full, deepx_m1_to_tensorrt:split:b003.
- `yolo11l` / `validate_outputs` / `warn` — Validation produced invalid measured rows; recorded as case-level quality failures, non-blocking in summary_only mode. Use validation.mode=strict to make this a blocking gate.
- `workflow` / `run_native_producers` / `failed` — Native runtime, semantic, claim or energy evidence is not technically complete
- `yolo11l` / `run_benchmarks` / `partial_measured` — measured_results=6, missing_measurements=2; normalized_results contains incomplete or optional-missing benchmark rows

## Non-blocking warnings
- `yolo11l` / `validate_outputs` / `validation_failed` — 4 measured row(s) failed validation. The workflow completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Use validation.mode=strict to make this blocking.
