# Energy measurement evidence and knowledgebase

Separate area for the Energy Paper / IEEE TIM measurement-methodology work. It does not replace the ONNX Split-Point knowledgebase or alter its result archive.

## Read first — current knowledgebase status

1. [1 October: complementary controlled rate test](knowledgebase/2026-10-01-complementary-rate-test.md) — current compact conclusion from two position-balanced six-run sessions.
2. [1 October: controlled rate test and historical decomposition](knowledgebase/2026-10-01-controlled-rate-test.md) — preceding fixed-window and first-session analysis.
3. [30 September: Prio A, remaining energy drops and fixed-window follow-up](knowledgebase/2026-09-30-prio-a.md) — retained as the preceding audit state.
4. [Full knowledgebase, 30 September baseline](Energy_Paper_TIM_KnowledgeBase_2026-09-30.md) — retained unchanged. Current amendments supersede older workflow-status/exclusion statements; scientific baseline chapters remain available.

The fixed 20–80-s comparison confirms that outer window placement is not the sole explanation. The two complementary fixed-work/fixed-pause sessions show that the raw Pico difference changes sign with measurement order; the position-balanced rate-associated load-power estimate is -0.061 %, not the historical multi-percent decrease. The external pre- and load-window levels drift together, while VDD_IN and TensorRT runtime remain nearly stable. No offset correction is applied.

## Evidence and original figure references

- [1 October: complete fixed-window and complementary controlled-rate evidence](2026-10-01-controlled-rate-test/README.md)
- [29 September: Jetson window and pause evidence](2026-09-29-jetson-window-pause/README.md)
- [30 September: offline-window evidence](2026-09-30-offline-windows/README.md)
- [Joris' original figure archive](Ergebnisse_Joris/)
- [Journal PSD documentation artifacts](PSD_Analysis_journal_documentation_artifacts/)
- [Multi-workload PSD documentation artifacts](PSD_Analysis_multi_workload_documentation_artifacts/)

The full baseline knowledgebase and PSD artifacts are stored in this repository. New compact evidence must not add credentials or complete operational archives. Raw NPY/Parquet data and private full review archives remain in laboratory storage; fingerprints alone are not backups.

The separate Tek/Pico PSD and common-reference analysis remains separate and unchanged. Direct-rate series compare separate physical executions and do not alone establish isolated sampling error.
