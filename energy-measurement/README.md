# Energy measurement evidence and knowledgebase

Separate area for the Energy Paper / IEEE TIM measurement-methodology work. It does not replace the ONNX Split-Point knowledgebase or alter its result archive.

## Read first — current knowledgebase status

1. [1 October: controlled 2-kS/s-/5-MS/s test and historical baseline decomposition](knowledgebase/2026-10-01-controlled-rate-test.md) — current compact amendment; fixed-window Prio A and the six-run hardware diagnostic are complete.
2. [30 September: Prio A, remaining energy drops and fixed-window follow-up](knowledgebase/2026-09-30-prio-a.md) — retained as the preceding audit state.
3. [Full knowledgebase, 30 September baseline](Energy_Paper_TIM_KnowledgeBase_2026-09-30.md) — retained unchanged. Current amendments supersede older workflow-status/exclusion statements; scientific baseline chapters remain available.

The fixed 20–80-s comparison confirms that outer window placement is not the sole explanation. The controlled fixed-work/fixed-pause test finds no multi-percent 2-kS/s-/5-MS/s load-power deficit; instead, the Pico current signal exhibits session-order drift shared by pre-load and load windows. Historical endpoint trends largely follow their pre-load levels. No repeat of the large acquisition campaign or raw-data batch is required.

## Evidence and original figure references

- [1 October: controlled rate-test evidence](2026-10-01-controlled-rate-test/README.md)
- [29 September: Jetson window and pause evidence](2026-09-29-jetson-window-pause/README.md)
- [30 September: offline-window evidence](2026-09-30-offline-windows/README.md)
- [Joris' original figure archive](Ergebnisse_Joris/)
- [Journal PSD documentation artifacts](PSD_Analysis_journal_documentation_artifacts/)
- [Multi-workload PSD documentation artifacts](PSD_Analysis_multi_workload_documentation_artifacts/)

The full baseline knowledgebase and PSD artifacts are stored in this repository. New compact evidence must not add credentials or complete operational archives. Raw NPY/Parquet data and private full review archives remain in laboratory storage; fingerprints alone are not backups.

The separate Tek/Pico PSD and common-reference analysis remains separate and unchanged. Direct-rate series compare separate physical executions and do not alone establish isolated sampling error.
