# Run Status Summary — v27929_acceptance_d_yolo11l_b003_deepx_gpu_20260907_151417

Technical status: `failed`
Quality-evaluation technical status: `failed`
Aggregate quality decision: `not_evaluated`
Scientific status: `not_evaluated`
Legacy workflow status: `failed`
Workflow: `v2.79.29-deepx-prepared-full-without-opencv`

## Native evidence axes
- Runtime: `incomplete`
- Semantics: `incomplete`
- Claim: `incomplete`
- Energy: plan 2/2 successful (complete); matrix 2/3 measured (incomplete); excluded 1

## Stage counts
- failed: 2
- ok: 15
- warn: 1

## Blocking partial / failure reasons
- `workflow` / `evaluate_quality` / `failed` — Central management quality: requests=5, completed=4, matched=3, summary_only_native_full=1, unmatched=1, failed=1; matrix_required=4, matrix_present=4, quality_applicable=4, quality_completed=3, quality_blocked=0, quality_not_applicable=0, companions=1; technical_status=failed, quality_decision=not_evaluated; workers=4. CPU reference rows remain semantic-only.
- `workflow` / `run_native_producers` / `failed` — Native runtime, semantic, claim or energy evidence is not technically complete

## Non-blocking warnings
- `yolo11l` / `validate_outputs` / `warn` — Validation produced invalid measured rows; runtime/interface validation and central task-quality decisions are reported separately. This validation warning is non-blocking in summary_only mode. Use validation.mode=strict to make this a blocking gate.
- `yolo11l` / `validate_outputs` / `validation_failed` — 2 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
