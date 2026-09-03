# Run Status Summary — paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251

Technical status: `failed`
Quality-evaluation technical status: `failed`
Aggregate quality decision: `not_evaluated`
Scientific status: `not_evaluated`
Legacy workflow status: `failed`
Workflow: `v2.78.2-immutable-management-reference-evidence-fixes`

## Native evidence axes
- Runtime: `complete`
- Semantics: `complete_pass`
- Claim: `ready`
- Energy: `measurement_failed`

## Stage counts
- failed: 1
- ok: 14
- partial: 2

## Blocking partial / failure reasons
- `yolov7_paper` / `run_benchmarks` / `partial` — Remote benchmark suite dispatched per hardware target/run-profile.; preserved 8 measured row(s), but the requested hardware matrix is incomplete; duplicate logical profile row(s): hailo8:full:fullx2, hailo8_to_tensorrt:split:b066x2, tensorrt:full:fullx2, tensorrt:split:b066x2.
- `workflow` / `evaluate_quality` / `failed` — Central management quality: requests=5, completed=5, matched=1, summary_only_native_full=1, unmatched=3, failed=0; technical_status=failed, quality_decision=not_evaluated; workers=4. CPU reference rows remain semantic-only.
- `workflow` / `run_native_producers` / `partial` — Native runtime, semantic, claim or energy evidence is not technically complete

## Non-blocking warnings
- `yolov7_paper` / `validate_outputs` / `valid_complete_splits_present` — 7 result row(s) validated, 1 optional row(s) have no explicit validation metric, and 2 invalid row(s) are reported separately; validation_ok means valid complete splits are present, not all rows valid.
