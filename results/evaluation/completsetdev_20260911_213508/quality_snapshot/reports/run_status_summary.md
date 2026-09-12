# Run Status Summary — completsetdev_20260911_213508

Technical status: `cancelled`
Quality-evaluation technical status: `failed`
Aggregate quality decision: `fail`
Scientific status: `not_evaluated`
Legacy workflow status: `cancelled`
Workflow: `v2.80.3-build-readiness-native-not-started-debug-export`

## Native evidence axes
- Runtime: `unavailable`
- Semantics: `unavailable`
- Claim: `unavailable`
- Energy: unavailable; plan completion / matrix coverage unavailable

## Stage counts
- cancelled: 1
- ok: 70
- partial: 6
- warn: 4

## Blocking partial / failure reasons
- `yolo11l` / `build_backend_artifacts` / `partial` — Backend build/reuse decisions recorded; reusable full-baseline artifacts copied when present. Hailo HEF reuse/build service plan recorded; existing HEFs were detected and missing heavy builds are structured. Hailo build queue: 0 item(s); dispatch status: not_required. DeepX full DXNN artifact ready. Selected deferred artifact readiness is incomplete: hailo8:b064/part1: Venv HEF build failed to launch: CompilerContextError: hailo_compiler_components_missing: No complete local ptxas/libdevice pair in selected DFC venv
- `yolo11l` / `run_benchmarks` / `partial` — Remote benchmark suite dispatched per hardware target/run-profile.; preserved 16 measured row(s), but the requested hardware matrix is incomplete; missing required profile row(s): hailo8_to_tensorrt:split:b064.
- `yolo26m` / `build_backend_artifacts` / `partial` — Backend build/reuse decisions recorded; reusable full-baseline artifacts copied when present. Hailo HEF reuse/build service plan recorded; existing HEFs were detected and missing heavy builds are structured. Hailo build queue: 0 item(s); dispatch status: not_required. DeepX full DXNN artifact ready. Selected deferred artifact readiness is incomplete: hailo8:b398/part1: Exact build evidence prevents repeated compiler attempt: COMPILE_INFEASIBLE (exact_deterministic_outcome); hailo10h:b399/part1: Exact build evidence prevents repeated compiler attempt: COMPILE_INFEASIBLE (exact_deterministic_outcome); hailo8:b399/part1: Exact build evidence prevents repeated compiler attempt: COMPILE_INFEASIBLE (exact_deterministic_outcome)
- `yolo26m` / `run_benchmarks` / `partial` — Remote benchmark suite dispatched per hardware target/run-profile.; preserved 16 measured row(s), but the requested hardware matrix is incomplete; missing required profile row(s): hailo8_to_tensorrt:split:b398, hailo8_to_tensorrt:split:b399, hailo10_to_tensorrt:split:b399.
- `yolo26s` / `build_backend_artifacts` / `partial` — Backend build/reuse decisions recorded; reusable full-baseline artifacts copied when present. Hailo HEF reuse/build service plan recorded; existing HEFs were detected and missing heavy builds are structured. Hailo build queue: 0 item(s); dispatch status: not_required. DeepX full DXNN artifact ready. Selected deferred artifact readiness is incomplete: hailo8:b364/part1: Exact build evidence prevents repeated compiler attempt: COMPILE_INFEASIBLE (exact_deterministic_outcome); hailo10h:b365/part1: Exact build evidence prevents repeated compiler attempt: COMPILE_INFEASIBLE (exact_deterministic_outcome); hailo8:b365/part1: Exact build evidence prevents repeated compiler attempt: COMPILE_INFEASIBLE (exact_deterministic_outcome)
- `yolo26s` / `run_benchmarks` / `partial` — Remote benchmark suite dispatched per hardware target/run-profile.; preserved 16 measured row(s), but the requested hardware matrix is incomplete; missing required profile row(s): hailo8_to_tensorrt:split:b364, hailo8_to_tensorrt:split:b365, hailo10_to_tensorrt:split:b365.

## Non-blocking warnings
- `yolo11l` / `validate_outputs` / `warn` — Validation produced invalid measured rows; runtime/interface validation and central task-quality decisions are reported separately. This validation warning is non-blocking in summary_only mode. Use validation.mode=strict to make this a blocking gate.
- `yolo26m` / `validate_outputs` / `warn` — Validation produced invalid measured rows; runtime/interface validation and central task-quality decisions are reported separately. This validation warning is non-blocking in summary_only mode. Use validation.mode=strict to make this a blocking gate.
- `yolo26s` / `validate_outputs` / `warn` — Validation produced invalid measured rows; runtime/interface validation and central task-quality decisions are reported separately. This validation warning is non-blocking in summary_only mode. Use validation.mode=strict to make this a blocking gate.
- `yolov7_paper` / `validate_outputs` / `warn` — Validation produced invalid measured rows; runtime/interface validation and central task-quality decisions are reported separately. This validation warning is non-blocking in summary_only mode. Use validation.mode=strict to make this a blocking gate.
- `mobilenet_v3_large` / `validate_outputs` / `valid_complete_splits_present` — 6 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `regnet_x_1_6gf` / `validate_outputs` / `valid_complete_splits_present` — 5 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `resnet50` / `validate_outputs` / `valid_complete_splits_present` — 4 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `yolo11l` / `validate_outputs` / `validation_failed` — 11 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `yolo26m` / `validate_outputs` / `validation_failed` — 9 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `yolo26s` / `validate_outputs` / `validation_failed` — 10 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
- `yolov7_paper` / `validate_outputs` / `validation_failed` — 12 measured row(s) failed validation. Validation evaluation completed; invalid cases are kept in validation_summary.json and excluded/marked by reports. Runtime and central task-quality outcomes are reported separately. Use validation.mode=strict to make this validation gate blocking.
