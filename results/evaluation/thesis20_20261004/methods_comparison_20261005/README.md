# THESIS20 ranking-method comparison — 5 October 2026

One additional offline analysis of the closed campaign, prepared for scientific
review. The earlier deep analysis was integrated into `main` at `82f0a257` and
the navigation update at `29d9312`. This comparison was integrated into `main` on
5 October 2026 by a normal fast-forward to reviewed commit `9c9c1c5`, followed by
a regular push and remote verification. The original
`analysis/thesis20-ranking-methods-20261005` branch is retained.

The question is whether existing graph selectors, cost proxies and measured
Generic rankings select the best observed Native candidate in the same exact
group, and what energy penalty follows that selection. The existing **10/21**
Generic-Completion Top1 result is a regression reference, not a Cut-Bytes result.

Read the [analysis plan](ANALYSEPLAN.md) and [evaluation definitions](EVALUATION_METHODS.md).
The method inventory distinguishes saved historical scores, deterministic
recomputations from frozen parameters, measured predictors, and unavailable models.
No score is fitted to Native outcomes.

## Results and review material

The [results](EVALUATION_RESULTS.md) give the numerical interpretation; the
[method provenance](METHOD_PROVENANCE.md) and [189-row availability matrix](inputs/method_availability.csv)
document the actual parameters and missing bindings. On all 204 technical cases:

| Selector | Native Top1 hits / 21 groups | Mean throughput loss |
|---|---:|---:|
| Cut bytes | 5 | 25.31% |
| Historical weighted score | 7 | 14.99% |
| Stored hardware fit, H10 profile | 5 | 19.67% |
| Cycle without handover | 7 | 14.99% |
| Stored streaming-rate prediction | 6 | 17.45% |
| Measured Generic completion | 10 | 12.25% |

These means weight exact groups equally. All five static methods have 0/9 exact
Top1 hits in classification; the twelve detection groups each contain only three
measured candidates. Weighted score and cycle without handover have identical
Top1 selections in 21/21 groups, but identical full rank vectors in only 12/21.
Generic completion's mean energy excess is 26.54%, versus 21.19% for weighted
score/cycle: a better mean throughput loss does not imply the best energy choice.

The [throughput figure](figures/fig01_ranking_methods_loss.pdf) and
[energy figure](figures/fig02_selector_energy_cost.pdf) have matching SVGs,
[English captions](METHOD_FIGURE_CAPTIONS.md), PNG previews and exact source CSVs.
[Group metrics](tables/method_groups.csv), [case ranks](tables/method_case_ranks.csv),
[shortlists](tables/method_shortlists.csv), coverage, repetition and tie tables
retain negative results. [Global recommendations](tables/method_global_selection.csv)
are a separate view: only 33/105 available static recommendations are measured,
with no fallback to another candidate. Repeated setup projections are dependent.

Frozen weighted-score parameters are **1 / 3 / 0.2**, with logarithmic communication
normalization over the original candidate universe. All saved accelerator-fit
profiles refer to Hailo-10→TensorRT; using their rankings to predict other setups
does not establish a matching device model. All saved streaming profiles are
`yolov7_streaming_v1`. The historical Native handover model is unconfigured.
All seven historical SystemSpecs are null. The saved workflow latency fallback
is therefore not relabelled as a reconstructed GUI latency model. Current GUI
settings are not substituted for these historical parameters.

Technical, quality-transfer and both-reference-close comparisons are separate.
Historical Raw is restricted to exact base identities. Missing scores and groups
with fewer than three cases remain explicit; the global graph recommendation is
reported separately from selection within measured candidates. An unmeasured
recommendation has no inferred performance or quality value.

Energy comparisons use the existing Native energy windows and per-repeat E/N.
They do not estimate Generic energy. Throughput loss, cycle regret and energy
excess have different denominators; none is measured single-request latency.
Repeated combinations are dependent sensitivity views, not extra experiments.

Existing data, quality decisions and claim gates are preserved. This is post-hoc
development evidence, not an independent hold-out or causal runtime comparison.
The existing archive queue and its frozen inputs remain unchanged by this Git
integration. Actual archive exit codes and destination checks are tracked
separately; publication on `main` does not certify completion of the raw archive.
Manuscript work remains private and is not included here.

## Offline reproduction

From this directory inside the result repository, use the existing scientific
Python environment (Python 3.12, NumPy 1.26.4, Matplotlib 3.5.2, pytest):

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/reproduce_methods.py --source-root .. --output-root /tmp/thesis20-methods-reproduced
THESIS20_SOURCE_ROOT="$(cd .. && pwd)" PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider --basetemp /tmp/thesis20-methods-tests tests
```

Choose new output paths. The first command reproduces the scores from compact
frozen graph inputs, evaluates the existing measurements and renders both figures.
It needs the adjacent original THESIS20 and `deep_analysis` inputs; they are not
duplicated here. No model, hardware runner or private original is required.
The optional private-source metadata extractor is documented in the provenance
report and is not part of normal reproduction. See [validation](VALIDIERUNG.md)
for actual final results and the artifact comparison.
