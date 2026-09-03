# Results bundle

Run ID: `paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251`  
Profile: `paper_comparison_yolov7_b066_hailo8_native_full_energy_b500`  
Tool: `2.78.2`  
Workflow: `v2.78.2-immutable-management-reference-evidence-fixes`

Key files:

- `profile.yaml` — snapshot of the Evaluation Profile.
- `run_manifest.json` — reproducibility manifest with stages and model metadata.
- `artifact_index.json` — generated artifact index with hashes.
- `models/<model>/analysis/prediction.json` — splitpoint predictions.
- `models/<model>/model_preparation/preparation_plan.json` — internal preparation/diagnostics stage.
- `models/<model>/benchmark_set/final_candidate_plan.json` — candidate plan benchmark generation must consume.
- `models/<model>/benchmark_set/generator_input.json` — materialized input for the benchmark generator.
- `models/<model>/benchmark_set/generator_binding.json` — formal benchmark-suite binding summary.
- `models/<model>/benchmark_set/legacy_suite/benchmark_set.json` — authoritative BenchmarkSet output from the existing generator.
- `models/<model>/benchmark_set/backend_artifact_decisions.json` — structured build/reuse decisions for HEFs/providers.
- `models/<model>/benchmark_set/hailo_artifact_service_plan.json` — Hailo HEF reuse/build queue and expected-unsupported contract.
- `models/<model>/benchmark_set/hailo_artifact_status.json` — compact Hailo readiness status.
- `models/<model>/hardware/hardware_smoke_status.json` — local runtime, HEF reuse, and optional remote preflight status.
- `models/<model>/full_baselines/output_contracts.json` — decoded/raw-head output contract.
- `models/<model>/full_baselines/baseline_reuse_decisions.json` — reuse/build decision record.
- `models/<model>/benchmark_results/benchmark_executor_status.json` — v49g local/remote execution dispatch status when generate_and_run is selected.
- `models/<model>/benchmark_results/normalized_results.json` — normalized result contract or measured-result ingestion.
- `models/<model>/validation/validation_adapter_plan.json` — v49g adapter plan for classification, decoded detection, raw YOLO head, or generic numeric validation.
- `models/<model>/validation/validation_summary.json` — v49g evidence-based validation summary from normalized rows.
- `models/<model>/hardware/hardware_smoke_status.json` — v49g Hailo/remote readiness and local runtime smoke summary.
- `reports/scientific/scientific_report.md` / `.json` — canonical run report with task-quality gates, row eligibility, and hold-out status.
- `reports/scientific/task_quality.csv` — non-inferiority decisions and confidence bounds.
- `reports/scientific/ranking_method_comparison.csv` — per-model/direction/runner comparison of the frozen Cut Bytes workflow selector with Weighted Score, both cycle-time predictors, and the hardware-aware ONNX-boundary baseline.
- `reports/scientific/ranking_method_macro.csv` — macro summaries with MAE/MAPE where meaningful, rank correlation, Hit@k, Elite Recall, Validity@k, and Regret@k.
- `reports/scientific/thesis_tables/*.tex` and `reports/scientific/figures/*` — thesis-ready exports.
- `reports/result_dashboard.*`, `reports/summary.csv`, and `reports/model_summary.csv` remain compatibility views of the canonical report; they are not independent claim-selection implementations.
