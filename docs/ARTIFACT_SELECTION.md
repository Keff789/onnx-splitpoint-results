# Artifact selection for the first archive

The source inventory was taken from `tree` listings of `~/Downloads` and
`~/Models` on Smartmirror2. Those listings contain names but no reliable sizes
or modification timestamps. The collection script therefore performs a
read-only scan before copying anything.

## Priority 0: preserve now

| Area | Canonical source | Git content | Raw archive |
| --- | --- | --- | --- |
| Hailo-10 output-format A/B | `~/Downloads/hailo10_ab/` and `hailo10_infermodel_format_ab_20260903_122158.json` | scripts, README, result JSON | packaged A/B ZIP |
| Hailo-10 input-format A/B | `~/Downloads/hailo10_input_ab/` and `hailo10_input_format_ab_20260903_131242.json` | scripts, README, result JSON | packaged A/B ZIP |
| Hailo-10 v2.79.16 HEF smoke | Hailo-10 Jetson: `/home/nx/v27916_hailo10_uint8_hef_smoke/report.json` | report JSON if reachable | optional smoke directory |
| Hailo-8 completion-tail A/B | `~/Downloads/native_completion_tail_canary_results/completion_tail_v2_20260828_082714/` | report JSON/Markdown and text profile summary | existing ZIP |
| Hailo-8 fast decode | `~/Downloads/native_completion_tail_fast_decode_results/fast_decode_v1_20260828_093339/` | report JSON/Markdown | existing ZIP |
| Hailo-8 32-image decode | `~/Downloads/native_yolov7_multi_image_fast_decode_results/yolov7_multi_image_fast_decode_v1_20260828_101748/` | JSON/Markdown results | existing ZIP |
| Hailo-8 three-stage | `~/Downloads/native_yolov7_three_stage_results/yolov7_three_stage_v1_20260828_120045/` | reports, oracle and repetition JSON | existing ZIP |
| Hailo-8 product runner | `v2794_yolov7_b066_product_normal_runner_20260901_092235.zip` | result is documented; compact ZIP remains raw evidence | ZIP |
| Hailo-8 32-image claim gate | `v2796_yolov7_b066_claim_gate_32_20260901_130453/` and retained v2.79.7 evidence | selected JSON/Markdown/env status, no corpus images or build tree | existing ZIP |
| M.2 idle baselines | three `m2_idle_power_calibration_*.json` files | JSON | source JSON also retained |
| Full-system calibration history | `~/Models/EnergyMeasurements/` | compact JSON/CSV/Markdown | complete measurement directory only with explicit full-archive option |
| v2.79.16 acceptance | `v27916_install_acceptance_20260903_154343_058884999_781004/` | status, identity and selected logs | acceptance ZIP and updated delivery bundle |

## Priority 1: analysis and failure evidence

| Area | Treatment |
| --- | --- |
| Seven-model run | Prefer `v2784_7model_evidence_reconciliation_v2`; keep v1 only in the raw archive if needed. |
| Final seven-model evidence | Preserve `v2784_seven_model_final_evidence_20260831_103034.zip` in the raw archive. |
| `biggerset` failed run | Commit only the compact plan/status/report subset as a diagnostic fixture; preserve the complete debug ZIP separately. |
| Paper comparison runs | Scan sizes first. Their compact reports are Git-suitable; full run directories are optional raw-archive material. |

## Priority 2: keep only if later needed

- old native producer bring-up and infrastructure-failure packs;
- earlier v2.79.1/v2.79.2 product-runner iterations superseded by later evidence;
- cancelled v2.79.7 diagnostics;
- redundant extracted copies of release bundles;
- old reconciliation v1 after v2 has been confirmed complete.

## Never mirror blindly

`~/Models/BackendArtifacts` contains hundreds of compiled DeepX artefact
variants. Together with ONNX/PT models, HEFs, TensorRT engines, validation
images, CMake build directories and raw boundary tensors, it is intentionally
excluded from the Git collection. These files are large, often reproducible,
and can also carry third-party licence restrictions.

