# Energy measurement evidence and knowledgebase

Separate area for the Energy Paper / IEEE TIM measurement-methodology work. It does not replace the ONNX Split-Point knowledgebase or alter its result archive.

## Read first — current knowledgebase status

1. [9 October: consolidated current status](Energy_Paper_TIM_KnowledgeBase_CURRENT_2026-10-01.md) — operative Source of Truth; the existing filename is retained for link compatibility.
2. [9 October: completed Scope/FP16 offline robustness checks](knowledgebase/2026-10-09-offline-robustness.md) — native versus via-1M reconstruction, persistent-rate sensitivity, FP16 cohort and PSD checks, and remaining provenance questions.
3. [1 October: complementary controlled rate test](knowledgebase/2026-10-01-complementary-rate-test.md) — compact conclusion from two position-balanced six-run sessions.
4. [1 October: controlled rate test and historical decomposition](knowledgebase/2026-10-01-controlled-rate-test.md) — preceding fixed-window and first-session analysis.
5. [30 September: Prio A, remaining energy drops and fixed-window follow-up](knowledgebase/2026-09-30-prio-a.md) — retained as the preceding audit state.
6. [Full knowledgebase, 30 September baseline](Energy_Paper_TIM_KnowledgeBase_2026-09-30.md) — retained unchanged as the detailed historical baseline.

The fixed 20–80-s comparison confirms that outer window placement is not the sole explanation. The two complementary fixed-work/fixed-pause sessions show that the raw Pico difference changes sign with measurement order; the position-balanced rate-associated load-power estimate is -0.061 %, not the historical multi-percent decrease. The external pre- and load-window levels drift together, while VDD_IN and TensorRT runtime remain nearly stable. No offset correction is applied.

Current paper policy: NPY-derived windows by default, NPY-derived LLM results without a paper old/new comparison, and the historical explicit window for Hailo Random Pattern. Common Reference / Same Trace carries isolated sampling claims; direct sweeps remain protocol observations.

## Evidence and original figure references

- [9 October: compact offline robustness evidence and local archive helper](2026-10-09-offline-robustness/README.md)
- [1 October: complete fixed-window and complementary controlled-rate evidence](2026-10-01-controlled-rate-test/README.md)
- [29 September: Jetson window and pause evidence](2026-09-29-jetson-window-pause/README.md)
- [30 September: offline-window evidence](2026-09-30-offline-windows/README.md)
- [Joris' original figure archive](Ergebnisse_Joris/)
- [Journal PSD documentation artifacts](PSD_Analysis_journal_documentation_artifacts/)
- [Multi-workload PSD documentation artifacts](PSD_Analysis_multi_workload_documentation_artifacts/)

The full baseline knowledgebase and PSD artifacts are stored in this repository. New compact evidence must not add credentials or complete operational archives. Raw NPY/Parquet data and private full review archives remain in laboratory storage; fingerprints alone are not backups.

The original Tek/Pico PSD and common-reference exports remain unchanged. The additional 9 October sensitivity check shows that preprocessing to 1 MS/s can alter reconstruction decisions and that some persistent minima also depend on the tested window/phase grid; it is not an exact reproduction of Table 2. Direct-rate series compare separate physical executions and do not alone establish isolated sampling error.

