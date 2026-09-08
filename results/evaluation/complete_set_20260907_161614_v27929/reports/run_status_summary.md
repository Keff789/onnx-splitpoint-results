# Run Status Summary — complete_set_20260907_161614

Technical status: `failed`
Quality-evaluation technical status: `failed`
Aggregate quality decision: `fail`
Scientific status: `not_evaluated`
Legacy workflow status: `failed`
Workflow: `v2.79.29-deepx-prepared-full-without-opencv`

## Native evidence axes
- Runtime: `incomplete`
- Semantics: `incomplete`
- Claim: `incomplete`
- Energy: plan 55/55 successful (incomplete); matrix 55/63 measured (incomplete); excluded 8

## Stage counts
- failed: 2
- ok: 75
- partial: 3
- warn: 4

## Blocking partial / failure reasons
- `yolo11l` / `run_benchmarks` / `partial` — Remote benchmark suite dispatched per hardware target/run-profile.; preserved 9 measured row(s), but the requested hardware matrix is incomplete; missing selected run(s): deepx_m1_to_tensorrt; missing required profile row(s): deepx_m1_to_tensorrt:split:b062.
- `yolo26m` / `run_benchmarks` / `partial` — Remote benchmark suite dispatched per hardware target/run-profile.; preserved 10 measured row(s), but the requested hardware matrix is incomplete; missing selected run(s): deepx_m1_to_tensorrt; missing required profile row(s): deepx_m1_to_tensorrt:split:b398, hailo8_to_tensorrt:split:b398.
- `yolo26s` / `run_benchmarks` / `partial` — Remote benchmark suite dispatched per hardware target/run-profile.; preserved 10 measured row(s), but the requested hardware matrix is incomplete; missing selected run(s): deepx_m1_to_tensorrt; missing required profile row(s): deepx_m1_to_tensorrt:split:b364, hailo8_to_tensorrt:split:b364.
- `workflow` / `evaluate_quality` / `failed` — Central management quality: requests=70, completed=69, matched=48, summary_only_native_full=21, unmatched=1, failed=1; matrix_required=56, matrix_present=51, quality_applicable=56, quality_completed=48, quality_blocked=0, quality_not_applicable=0, companions=21; technical_status=failed, quality_decision=fail; workers=4. CPU reference rows remain semantic-only.
- `workflow` / `run_native_producers` / `failed` — Native runtime, semantic, claim or energy evidence is not technically complete

## Non-blocking warnings
- `yolo11l` / `validate_outputs` / `warn` — Validation produced invalid measured rows; runtime/interface validation and central task-quality decisions are reported separately. This validation warning is non-blocking in summary_only mode. Use validation.mode=strict to make this a blocking gate.
- `yolo26m` / `validate_outputs` / `warn` — Validation produced invalid measured rows; runtime/interface validation and central task-quality decisions are reported separately. This validation warning is non-blocking in summary_only mode. Use validation.mode=strict to make this a blocking gate.
- `yolo26s` / `validate_outputs` / `warn` — Validation produced invalid measured rows; runtime/interface validation and central task-quality decisions are reported separately. This validation warning is non-blocking in summary_only mode. Use validation.mode=strict to make this a blocking gate.
- `yolov7_paper` / `validate_outputs` / `warn` — Validation produced invalid measured rows; runtime/interface validation and central task-quality decisions are reported separately. This validation warning is non-blocking in summary_only mode. Use validation.mode=strict to make this a blocking gate.
- `mobilenet_v3_large` / `validate_outputs` / `valid_complete_splits_present` — 2 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `regnet_x_1_6gf` / `validate_outputs` / `valid_complete_splits_present` — 2 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `resnet50` / `validate_outputs` / `valid_complete_splits_present` — 1 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `yolo11l` / `validate_outputs` / `validation_failed` — 3 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `yolo26m` / `validate_outputs` / `validation_failed` — 2 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `yolo26s` / `validate_outputs` / `validation_failed` — 2 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `yolov7_paper` / `validate_outputs` / `validation_failed` — 4 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
