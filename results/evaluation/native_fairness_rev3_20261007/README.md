# Native/Generic fairness — Revision 3 Current snapshot

This snapshot reports the actual selected Current rows at **2026-10-08T20:24:55.106351+00:00**.
Execution state: `bounded_three_points_current_plan_energy_paper_archive_complete_public_review_closure`. Counts below are derived from those rows;
the finalized Quality pointer describes its own normal report generation separately.
Missing values remain null/NA. This page does not declare the campaign complete.

| Current axis | Native | Generic |
|---|---:|---:|
| Newly measured Native / completed Generic performance | 232 | 204 |
| Verified original single-observation performance reuse | 6 | — |
| Performance not measured/completed | 8 | 0 |
| Normally bound dataset Quality | 180 | 148 |
| Normal comparative performance claims | 169 | 148 |
| Normally admitted current energy | 5 | 0 |

Generic points still requiring final-bundle confirmation according to Resume:
0.
Completed historical cohorts remain visible; this count is not inferred from a free lease.

Start with [the result report](RESULT_REPORT.md), [fairness matrix](FAIRNESS_MATRIX.csv),
[Native Current](current_results/native_current.json), [Generic Current](current_results/generic_current.json),
[finalized Quality pointer](quality_transfer/CURRENT_FINALIZED.json),
[review holds](current_results/QUALITY_JOIN_REVIEW_HOLDS.json),
[audit dispositions](AUDIT_FINDING_DISPOSITION.csv) and [Resume state](RESUME_STATE.json).
[PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) records the exported checkpoint and source bindings.

Runtime freeze: `8346d43d526221bd9d138943122206b658d56cbf` (241 files).
The canonical CPU-reference Controller correction is `ec68097d0ca161a75380da158a257ad495296d90`.
Controller reporting is `5e742b34862a7d0e0760474a1ff3e4826854f20e`; the retained-origin reader
guard is `6ca5b3cedf3fda0f69397ad0e7a3e7abbe0194ae`. The bound cohort reader is
`b7c2094e329351dcbdbeef4d3fcac48eec9458f3`. These local reporting amendments are bound by the existing
[reporting source supplement](REPORTING_SOURCE_SUPPLEMENT.json); deployed runtime bytes remain
at the original freeze.
Current normal Quality generation: `revision3:/quality_transfer/final_native_179_20261008/finalized_179_origin_verified`. Its composition and
independent-review references follow the current pointer; no historical generation count is substituted.
Complete Quality summaries, N5000/CPU evidence, model binaries and original raw captures remain private.

H8 classification was corrected against the actual HEF/SDK domain. Corrected Vendor/TRT Full
Quality bindings and same-setup comparisons use the normal consumer; `accuracy_loss` remains visible.
Original Vendor-DX/H10 dataset Quality reuse retains one performance observation, no new repeats/CI
and no new performance claim. The conflicted H10 historical physical Full context stays excluded.

The [DX56 input-source finding](quality_transfer/classifier_split_preparation_20261008/DX56_N5000_INPUT_SOURCE_REVIEW.json)
records the original inverse-ImageNet-to-UINT8 truncation versus the final direct-RGB path.
The unintegrated preliminary transfer is invalid; actual performance and valid original N5000 remain.
Current holds and Resume carry the exact applicable input/consumer blocker and targeted API readiness.
No Quality flag or hash-only dataset remeasurement resolves that difference.

| Normally admitted current energy row | Completed tasks/s, integer display | Raw system mJ/task | Tasks/J |
|---|---:|---:|---:|
| Native yolov7_paper/DeepX/native_full_deepx/full | 23 | 689.874383 | 1.449540153 |
| Native yolov7_paper/H8/native_full_hailo8/full | 32 | 549.843563 | 1.818699641 |
| Native yolov7_paper/DeepX/native_full_tensorrt/full | 48 | 613.181286 | 1.630862555 |
| Native yolov7_paper/DeepX/deepx_to_trt/b044 | 49 | 532.093280 | 1.879388384 |
| Native yolov7_paper/DeepX/deepx_to_trt/b066 | 31 | 712.277595 | 1.403947547 |

Energy uses actual completed counts and three accepted captures. Presentation multiplies the stored
J/task by 1000 only; raw values remain unchanged. Mean N/E is separate from inverse mean E/N, and
existing comparison normalization remains in separate Current fields. Unadmitted rows stay NA.

H10's specifically authorized energy continuation failed with 7,936 missing samples inside its command
window despite source closure and cleanup. Its authorization is consumed. H8 zero-start, accepted-repeat,
source STOP and budget restrictions remain governed by [Resume](RESUME_STATE.json); a free lease is no
capture authorization. Valid evidence and failed attempts are retained, with no deletion or cleanup.

The historical Generic streaming, multi-tensor, Raw, `native_fifo` and `NativeTRTSession` paths remain.
Only proven dead isolated duplicates were removed. Actual independent process cohorts, completion
counts, exact inputs, normal Quality, comparative claims and energy are separate evidence axes.
One thousand repetitions of one prepared input are not one thousand dataset images or independent sessions.

Run the standalone public hash and arithmetic check from any directory:

```sh
python3 verify_snapshot.py
```

The checker verifies supplied projections and repeat arithmetic; it does not replay raw sensors,
model inference or normal private consumer execution. Private paths/network labels are sanitized.
The private manuscript and all LaTeX remain outside this Git payload. Final rankings and private-paper
status are stated only by the current result/Resume checkpoint.
