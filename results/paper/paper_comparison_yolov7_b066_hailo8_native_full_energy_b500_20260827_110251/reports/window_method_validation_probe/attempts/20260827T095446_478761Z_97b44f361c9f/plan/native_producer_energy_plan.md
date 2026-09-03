# Native producer energy plan

Workload duration: `60` s.
Split rows are included only after the native semantic gate. Energy workloads are duration-driven and emit exact runtime-completed work units; historical FPS is context only.
Split boundary precision and Full runtime precision are reported separately and are not used as an equality key for setup-local Full matching.

## hailo8_to_trt / yolov7_paper / b066

Precision: `uint8_dequant_fp16`
Command file: `/home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/reports/window_method_validation_probe/attempts/20260827T095446_478761Z_97b44f361c9f/plan/hailo8_to_trt__yolov7_paper__b066__orin_nx_hailo8_01__b4a9dc5882cc.sh`

```bash
/home/kmika/ONNX-Splitpoint-Tool/.venv/bin/python -u /home/kmika/ONNX-Splitpoint-Tool/scripts/energy_measurement_cli.py measure --setup-id orin_nx_hailo8_01 --run-id native_hailo8_to_trt__yolov7_paper__b066__orin_nx_hailo8_01__b4a9dc5882cc --command-file /home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/reports/window_method_validation_probe/attempts/20260827T095446_478761Z_97b44f361c9f/plan/hailo8_to_trt__yolov7_paper__b066__orin_nx_hailo8_01__b4a9dc5882cc.sh --duration 60 --inference-count 1 --pipeline-fps 15.872171 --timeout 900 --runs 3 --physical-scope '' --window-label command --diagnostic-only --claim-exclusion-reason quality_or_pairing_not_claim_eligible --out /home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/reports/window_method_validation_probe/attempts/20260827T095446_478761Z_97b44f361c9f/measurement --preflight-command-file /home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/reports/window_method_validation_probe/attempts/20260827T095446_478761Z_97b44f361c9f/plan/hailo8_to_trt__yolov7_paper__b066__orin_nx_hailo8_01__b4a9dc5882cc.preflight.sh --preflight-runtime-attestation-path /home/nx/native_fifo_evalsets/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/.energy_replays/hailo8_to_trt__yolov7_paper__b066__orin_nx_hailo8_01__b4a9dc5882cc/preflight___ONNX_SPLITPOINT_PREFLIGHT_NONCE__.json --preflight-timeout-s 900 --preflight-attestation-max-age-s 300 --preflight-expected-command-contract-sha256 b4a9dc5882cc60c8196a9c6584f14707f3de88fb4c9cb1240b954608c76c8d1a --compare-legacy-window
```
