# Native/Generic fairness — Revision 3, 7 October 2026

This is an **incomplete execution snapshot**. It records 15 newly measured
YOLOv7 Native points, nine verified classifier Full performance reuses,
nine measured Generic pairs, and three normally admitted current energy points.
Another 222 Native and 195 Generic performance points remain unmeasured.
The nine Generic points require confirmation against the now integrated and frozen duration-worker
extension before final energy acquisition. Missing values remain null.

The historical archive was inspected read-only. No result data was deleted,
moved or cleaned up. New raw reports and failed attempts are retained in a
separate dated archive. The historical review ZIP passed its supplied checker
for 6,281 payload hashes, 27 split repeats, 18 Full repeats and three controls;
this is not a full cryptographic verification of the historical campaign archive.

Start with [RESULT_REPORT.md](RESULT_REPORT.md), the
[450-row fairness matrix](FAIRNESS_MATRIX.csv),
[audit dispositions](AUDIT_FINDING_DISPOSITION.csv),
[historical Generic usage](LEGACY_GENERIC_USAGE.csv) and
[remeasurement decisions](REMEASUREMENT_PLAN.csv).
Machine-readable observations are in
[native_current.json](current_results/native_current.json) and
[generic_current.json](current_results/generic_current.json).
Explicit `supersedes` links preserve older operating points.

New Native performance uses three actual processes, each with 100 completed
warmups and 1,000 completed tasks. Historical reuse keeps its original protocol;
it does not acquire invented three-process repeats. Quality class, technical
execution, normal report eligibility and broader scientific claims remain separate.
H8 regressions and `accuracy_loss` results are retained.

| Normally admitted Full point | Raw system J/task, mean E/N | Tasks/J, mean N/E |
|---|---:|---:|
| DeepX vendor | 0.689874383 | 1.449540153 |
| H8 vendor | 0.549843563 | 1.818699641 |
| DeepX TensorRT | 0.613181286 | 1.630862555 |

Each value uses three requested 60-second captures with actual completed counts
and confirmed source completion. The existing TensorRT comparison normalization
is stored separately: 0.561263320 J/task and 1.781724572 tasks/J. It does not replace
the raw system measurement. Mean N/E is not computed as the reciprocal of mean E/N.
Earlier diagnostic or strict-versus-fast captures remain visible but cannot supply
energy for the new performance points.

The first following H10 TensorRT capture failed with a source silence timeout
and no confirmed protocol end. Its physical STOP remains binding. A subsequent
H8 TensorRT reservation never started a collector. The concrete bounded recovery
requires a separate post-STOP authorization under the existing source-completion
guard; it was requested and has not been received at this snapshot.
No measurement processes remain according to the terminal ownership report.
[Resume state and retained budgets](RESUME_STATE.json).

The code audit preserves the general Generic streaming, multi-tensor,
`native_fifo` and `NativeTRTSession` paths. Only three unreachable DeepX P2
duplicates and their dead helpers, 197 lines, were removed with original sources
and a diff retained. Lossless queue drain, explicit input domains, canonical
prepared inputs, format-specific completion, evidence outside the timer and the
Student-t fallback were checked with targeted tests. The report-only correction
prevents an A/B shadow diagnostic flag from overriding the primary energy policy.
It also gives the normal consumer a hash-bound import for three real single
captures without changing their original raw repeat indices.

The Generic duration extension is now integrated in the regular worktree: six
product files and six regression-test sources. Candidate tests (182), independent
review probes (10), and actual-worktree/bundle checks (36) passed; these overlap
and are not summed. New Generic hardware energy has not been captured. The
80-file current source review snapshot is distinct from the original 223-file
DUT runtime freeze. Six existing DX/H10 performance cohorts remain valid, but
normal energy preflight requires six bounded deployment confirmations against
the repaired runner bytes; old reports are not resealed. The private incomplete
paper view was rebuilt and reproduced; its LaTeX remains outside this repository.

Run the public hash and arithmetic check from any directory:

```sh
python3 verify_snapshot.py
```

`PUBLICATION_MANIFEST.json` records both original private and public projection
hashes. Private paths and network identifiers are replaced by descriptive labels.
One repeated full producer row is represented by its canonical hash; the exact
original remains in the private report archive. The checker validates the
provided projections, repeat arithmetic and confidence intervals. It does not
independently replay sensor traces, model inference, normal consumer execution
or per-frame FIFO order. Raw data, precise source snapshots and the private
manuscript remain outside this Git payload. No final all-model ranking or paper
completion is claimed.
