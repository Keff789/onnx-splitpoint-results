# Current YOLOv7 native performance: completed-task results

Integrated 7 October 2026. This directory provides the current compact YOLOv7
performance projection for the paper. It supersedes the throughput aggregates
of the nine matching Native split configurations and six Full alternatives in
the dated THESIS20 analysis. Historical measurements remain unchanged.

| Setup | TRT Full FPS | Accelerator Full FPS | Split b009 FPS | b044 FPS | b066 FPS |
|---|---:|---:|---:|---:|---:|
| H8 | 51.781526 | 31.477269 | 42.851710 | 47.800201 | 112.492794 |
| H10 | 51.480597 | 12.314299 | 51.357901 | 64.500526 | 53.350448 |
| DeepX | 47.319602 | 22.945769 | 33.866133 | 48.790077 | 30.594221 |

These are medians of three repeats, with 100 completed warmups and 1,000
completed tasks per repeat. The report describes nine newly measured split
configurations in 27 separate processes and six reused optimized Full
configurations with 18 repeats. Three additional Full controls are not mixed
into those triples. Decode and NMS remain inside the task-completion boundary.

H8 b066 reaches 2.17245x its fastest Full, and H10 b044 reaches 1.252909x.
DeepX b044 reaches 1.031075x; small observed gains are not claims of statistical
superiority. All nine split quality labels are reported as `reference_close`.
H8/H10 accelerator Fulls retain `accuracy_loss`; all TRT Fulls and DeepX
accelerator Full retain `reference_close`.

## Files and evidence scope

- [reported_results.csv](reported_results.csv): all 15 configurations, their
  three repeats, medians, comparison ratios, quality labels and energy status.
- [reported_results.provenance.json](reported_results.provenance.json): source
  hash, printed precision, cohort distinctions and arithmetic checks.
- [SOURCE_REPORT.md](SOURCE_REPORT.md): supplied result report, unchanged.
  Its relative diagnostic links refer to the original local review archive,
  not to files supplied in this compact projection.
- [extract_reported_results.py](extract_reported_results.py): deterministic
  extraction using only the Python standard library.

Reproduce with:

```bash
python3 results/evaluation/yolov7_native_completion_20261007/extract_reported_results.py
```

All 15 medians, 18 split/reference ratios and nine historical comparison
ratios were checked against the displayed six-decimal source precision.
The new 516-MB review ZIP was not available in the review environment. This
integration therefore verifies transcription and arithmetic, **not** the new
raw reports, source hashes, telemetry or quality joins. The report describes
those local checks; their independent archive verification remains a handoff
item. This limitation does not turn the reported measurements into simulated
or inferred FPS. Do not mislabel this projection as raw-archive verification.

## Applying the current projection

Match by model `yolov7_paper`, setup, Full/split role, backend and cut. H8/H10/
DeepX correspond to the existing H8/H10/DX setup labels in the compact inputs.
For those 15 configurations use the three repeats and medians here for the
current performance view. Select the fastest technically comparable Full on
the same host before applying quality labels; here that is TRT on every host.
Do not silently choose a slower quality-filtered baseline.

**All 15 current variants have energy `not_measured` / `NA`.** Supersede their
old current-view energy claims as well: do not join historical J/task or
energy-window rates to the new performance implementation. Preserve historical
energy only in its own dated cohort. Matching current energy thus covers 195
splits and 36 Fulls across the other six models, while throughput covers 204
splits and 42 Fulls. Dependent ranking/benefit summaries must be regenerated
with that distinction; dated October-4 analyses reproduce their own snapshot.

Generic timings remain the original separate exploration measurements. The
new Native measurements do not imply new Generic or dataset-quality runs.
The optimized worktree and isolated device runtimes were validated according
to the report; a global production rollout was not performed.

The [knowledge-base entry](../../../docs/YOLOV7_NATIVE_COMPLETION_20261007.md)
records the implementation explanation and remaining work. The paper presents
the final method and outcomes, not the debugging chronology.
