# Repository map

> **Added 7 October 2026:**
> [YOLOv7 native-completion findings](YOLOV7_NATIVE_COMPLETION_20261007.md) and
> [reported performance data](../results/evaluation/yolov7_native_completion_20261007/README.md)
> form a separate dated update. The supplied report was transcribed and checked
> arithmetically; its new raw-data/source archive was not independently verified.
> Current performance and historical energy are kept separate; all 15 updated
> variants have energy NA. Existing THESIS20 paths and historical results remain.

Current navigation, 5 October 2026. Evidence paths stay fixed so that old reports,
figure references and scripts continue to resolve. Dated directories describe
their own run; they do not override a newer analysis merely by remaining present.

| Area | Purpose and authoritative entry point | Boundary |
|---|---|---|
| [Project knowledge base](KNOWLEDGEBASE.md) | Canonical, continuously updated account of Splitpoint methods, evidence and open items | Earlier states are retained as dated history and in Git |
| [THESIS20](../results/evaluation/thesis20_20261004/START_HERE.md) | Closed campaign, corrected base, Generic completion and YOLO augmentation | Original identities, exclusions and negative results are preserved |
| [Scientific deep analysis](../results/evaluation/thesis20_20261004/deep_analysis/README.md) | Integrated post-hoc ranking, quality, graph and energy analysis; portable reproduction and publication figures | Technical comparability, quality transfer and causal/hold-out claims remain distinct |
| [Evaluation history](../results/evaluation/README.md) | Earlier runs and reconciliations, including [R9G](../results/evaluation/r9g_eval_20260918_171131/README.md) | Historical evidence, not the current THESIS20 population |
| [Acceptance](../results/acceptance/README.md) | Dated software and hardware acceptance records | A software PASS does not imply a hardware PASS |
| [Paper comparison history](../results/paper/README.md) | Earlier Hailo-8 B500 comparisons | Separate engines, endpoints and runs; not interchangeable with THESIS20 |
| [Energy measurement methodology](../energy-measurement/README.md) | Independent URECS/PSD/IEEE TIM work and its own current knowledge base | Remains separate from the heterogeneous inference paper |
| [Energy records](../results/energy/README.md) | Original calibration and manual energy evidence | Read the recorded physical scope and historical status |
| [Experiments](../experiments/README.md) | Bounded A/B studies and runtime investigations | Microbenchmarks do not establish complete pipeline claims |
| [Diagnostics](../diagnostics/README.md) | Technical failures and explanatory fixtures | Diagnostic evidence is not a successful measurement |
| [Inventory](../inventory/README.md) | Existing collection inventories and missing-source reports | Collection status is not scientific validation or a complete raw-content check |

## Reproduction and archive boundary

The [root README](../README.md) and [deep-analysis README](../results/evaluation/thesis20_20261004/deep_analysis/README.md)
give the small offline entry point. Use a separate output directory; retain the
checked-in source projections. [Integration validation](THESIS20_INTEGRATION_20261005.md)
records the tested commit and reproduction result.

Large models, engines, runtime payloads and private original reports belong to the
existing separate raw archive. Its original copy, finalization and frozen-analysis
follow-up are sequential. On 5 October the YOLO transfer was still active; the
archive was not yet accepted as complete. The declared historical source gap is
one `native_output_endpoint.py` version with 21 references, not 21 missing measurements.

Current local manuscript work is not a public paper in this repository. Later
method comparisons are separate review contributions until explicitly integrated.
No directory relocation or duplicated “final” dataset is required for navigation.
