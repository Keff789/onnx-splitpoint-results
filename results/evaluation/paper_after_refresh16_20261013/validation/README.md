# Validation

`independent_check.py` recalculates the paper's core quantities with only the
Python standard library. It does not import the dataset builder or its metric
functions. Checks cover all selected FPS cohort medians, all per-repeat E/N
values and their means, exact Refresh16 replacement and quality preservation,
Table 2's host aggregates, Table 3's retrospective top two and same-Full energy
gain, all comparison pairs, equal model weighting, and figure payloads when
figures are present. Original flags are compared without rewriting unknown or
ineligible values. The checks use the compact archived input observations.

The Pareto extension is checked with a separate exhaustive pairwise comparison,
independent of the builder's sorted sweep. It checks all 450 exported rows,
21 model/setup populations, common and runner-only front flags, deterministic
dominating witnesses, exact plotted coordinates and quality, both Full labels,
runner F/E labels, front connections and singleton fronts. Inclusion is checked
without using quality, claim or contract-hash flags.

`test_edge_cases.py` exercises missing energy with available FPS, valid older
energy fallback, invalid newer reports, actual identity mismatches, newer worse
quality, one repeat without an invented interval, large repeat dispersion,
reexport duplication, distinct energy aggregations, equal model weighting,
different fastest/lowest-energy Full alternatives, deterministic ties and
identical repeated builds. It uses synthetic observations; they are not paper
measurements. The separate independent checker tests the real paper data.

Ten additional tests cover objective direction, duplicate coordinates, equal
FPS, equal energy, singleton fronts, genuine conflicting objectives, model/setup
separation, split-only runner fronts, neutral missing quality and missing or
nonfinite coordinates with explicit reasons. There are 21 targeted tests in total.

`HANDOFF_CURRENT_CHECK.json` records the bounded pre-publication check against
the confirmed Current and the local original reports: 48 independent FPS
reports and 48 calibrated energy summaries. FPS was reconstructed from completed
images and measured duration; energy from calibrated joules and the matching
completed-image counter. The 16 replacements, 434 untouched rows and all 450
unchanged quality/original-gate selections were compared to the historical
snapshot. No sensor trace was reprocessed and no quality evaluation was run.

The public reproduction CLI runs the tests and checker when `--verify` is used.
The resulting independent-check report states the actual checked populations.
Private original-report validation is preserved with the dated analysis under
`evidence/`; publication reproducibility depends only on this compact package.

The final [independent result](INDEPENDENT_CHECK.json), [21 targeted tests](EDGE_TESTS.json), [complete byte reproduction](REPRODUCTION_CHECK.json), [LaTeX compilation](LATEX_ASSET_CHECK.json) and [visual review](VISUAL_REVIEW.md) record the checks performed on this package. The reproduction record identifies the tested command, the unchanged baseline files and the output count. The original Current/hardware provenance and input-extraction checks above are retained historical evidence; the Pareto extension does not rerun measurements, quality evaluation or input extraction.
