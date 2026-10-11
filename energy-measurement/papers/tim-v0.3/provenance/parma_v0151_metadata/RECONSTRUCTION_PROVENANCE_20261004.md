# Six-workload reconstruction provenance — 2026-10-04

Review item 4.1 is **partially resolved**. The new collector identifies the same
frozen six-workload input bytes and recovers a tool-0.8.2 caller, its referenced
template configuration and a completed artifact refresh. It does not establish
all historical numerical settings or supply the implementation of the sampling
and integration helpers. The reconstruction recipe below separates observed
source behavior from a verified historical application.

This audit reads existing collector text and checks file identities. It does not
execute collected programs, reconstruct waveforms, change results, acquire data
or repeat the numerical analysis. Only the selected reconstruction excerpts and
binding records are retained in
[data/provenance/reconstruction](../data/provenance/reconstruction/); the collector
archive, unrelated history and hardware records are not bundled.

## 1. Evidence binding and its limit

The existing [MULTI_WORKLOAD_SOURCE.json](MULTI_WORKLOAD_SOURCE.json) pins the
public inputs to repository commit
`e87730135385e756c667fc2b573fb1a86834d4bb`. Collector sources on `twix` have original
SHA-256 hashes equal to the nine relevant bundled inputs: the multi-workload
manifest and summary, both inventories, the common-reference summary,
rate/duration threshold summaries, cache-energy QC and worst-case envelope.
The corresponding package bytes were checked against those recorded hashes;
no result values were recomputed. The complete selected identity mapping is
[input_binding.json](../data/provenance/reconstruction/input_binding.json).

| Anchor | Collector source ID | Original SHA-256 |
|---|---|---|
| Frozen multi-workload manifest | `ca8617d545012307d9c0` | `a43f833e05f2c810846bda4dc3d2810d62413501b152a73aa1b2405552c07b7f` |
| Frozen common-reference summary | `f8141a4bbe8a699d9a2c` | `fa67f7fc332326ec5afd89ff1d74a1188a11535feac753ab566cf38cb55ccdbb` |
| Generated multi-workload config | `3cb261d25c58dca17610` | `e72b4f7913948525463185685922db199676cde2a8d03c17cfd1a000fa464493` |
| Observed `commonref/workload_compare.py` | `39ff7ffa8dc923f76514` | `80cb8ce7961a44769972e5cd4c2eaa0caeab955f070f27307f1f4ec402582ec5` |
| Observed template `config_gemm_fp16.yaml` | `2233f50612a8b3086561` | `89b73c928e0e6440cd46be9bc148ec802fd932f7654ec3b85be1d6efd87b3b12` |
| Completed automatic-pipeline manifest | `6c93d1e09f93c2a5f1d0` | `27f964bea60df731296be82ddc2542022a91ce9575835548517fdf03010cd536` |

The frozen manifest records tool version `0.8.2`, 59 paired executions / 118
instrument traces, the generated config path and the six workload-specific
scope-manifest hashes. The collector's generated YAML has the same
common-reference settings as `$.config.common_reference` in that manifest.
The other sections correspond after the loader's field normalization, including
`id` to `workload_id`, `direct_rate_validation` to `direct_validation`,
`paper_artifacts` to `paper`, and PSD band/window mappings to triples.

The automatic-pipeline manifest records a completed
`workload-compare --config …/config_multi_workload_auto.yaml --artifacts-only`
invocation with tool version `0.8.2` (`$.results[6]`, original lines 67–87).
Its creation time is `2026-08-28T13:34:44.147274+00:00`; the frozen multi-workload
manifest was created at `2026-08-28T13:34:20.563875+00:00`. This establishes the
recorded artifact-refresh lineage. The caller's artifact-only branch reads
existing per-run rows or existing aggregate summaries; it does not run the
common-reference reconstruction (source `39ff7ffa8dc923f76514`, lines 4187–4235).
Consequently this completed invocation cannot certify the code bytes that
originally generated individual reconstruction errors.

The recorded `source_fingerprint` is also insufficient for that certification.
In the observed `auto_pipeline.py` (source `98bfc5bccef62f5b3761`, lines 695–715),
it hashes the schema, tool version, loaded multi-config and scope fingerprints /
usable states. The nested scope fingerprints cover scope config and
measurement-file stat metadata (the same source, lines 534–574). Neither level
hashes reconstruction source files. The frozen
multi-workload manifest does not contain hashes for the reconstruction caller,
template contents, or its helper modules. The original SHA-256 values above
identify files observed by the collector on 2026-10-04, not a historically
recorded numerical-execution code fingerprint.

Preserve the path distinction: the collector found the copies below
`/homes/kmika/energy_analysis/…`, whereas the stored historical config and command
paths use `/homes/kmika/common_reference_psd_tool_v0.8.2/…` and
`/homes/kmika/common_trace_analysis/…`. Corresponding contents and referenced
paths provide a useful bridge; pathname similarity alone is not a proof of
historical application.

## 2. Recipe recovered from the observed caller

The following rules are directly visible in source `39ff7ffa8dc923f76514`.
Their source locators and verbatim excerpts are retained in
[source_excerpts.json](../data/provenance/reconstruction/source_excerpts.json).
They describe the observed tool snapshot; the historical code-byte limit above
applies to every rule.

### Analysis representation and numerical interval

The caller converts the derived-power vector from the physical 5-MS/s source
to 1 MS/s with `soxr.resample`, using the loaded template's `quality` setting,
then writes a float32 cache (lines 378–421). The collected template specifies
`quality: VHQ` (source `2233f50612a8b3086561`, lines 24–36). The six-workload
config independently specifies the 1-MS/s analysis rate and float32 cache.

Let `F = 1,000,000 S/s` and let `N` be the number of cached analysis samples.
The common-reference caller assigns the nominal physical interval `[0, N/F)`
and uses `T = N/F`. It appends one copy of the last analysis value to its
reference integration vector, assigning that endpoint to `T`. It pads the
resampling input at both ends by constant edge values, with
`g = max(1, round(guard_seconds * F))` samples per side. The recorded
`guard_seconds = 0.5` gives a padded origin of `-g/F = -0.5 s`.
These guards are outside the physical interval; the integration windows retain
the original interval endpoints (lines 1459–1495).

### Window-start generation

For requested duration `L`, count `C` and edge margin `m`, `_window_starts`
(lines 1424–1448) applies these rules in order:

1. If `L > T + 1.5/F`, return no window. If `L >= T - 1.5/F`, return start `0`.
2. Clamp the margin to `min(max(0, m), max(0, (T-L)/2))`; use `first = margin`
   and `last = T-L-margin`. If `last < first`, use `0` and `T-L`.
3. If `C <= 1` or `last <= first`, use the midpoint of that start range.
4. Otherwise form `C` endpoint-inclusive starts with
   `np.linspace(first, last, C, dtype=float64)`, round to analysis-sample
   indices with `np.rint(starts * F)`, remove duplicate indices with
   `np.unique`, and divide by `F`.

For the recorded `m = 0` and `C = 16`, an ordinary eligible interval therefore
uses 16 evenly distributed candidate starts from `0` through `T-L`, rounded
to the nearest 1-µs analysis grid and deduplicated. The actual count can be
smaller for a very short start range or a duration spanning the whole record.
Each stop is `min(start + L, T)`. A duration/rate combination is skipped when
`L*f < 4` (lines 1534–1537); this is the caller's eligibility test.

### Offset count and spacing

The six-workload generated config explicitly points to the tool-0.8.2 template
`config_gemm_fp16.yaml`. Thus its collected phase-plan settings are relevant as
a referenced dependency, even though the filename contains FP16. They are not
inferred from the separate pooled FP16 tool-0.3.0 illustration.

| Tested target rates, S/s | Collected v0.8.2 template request |
|---|---:|
| 50, 85, 150, 240, 400, 680, 1200, 2000 | 64 |
| 2500, 3300, 5500, 9400 | 32 |
| 16000, 25000, 45000, 80000, 100000, 125000, 160000 | 1 |

These are **template requests, not verified historical applied counts**.
The observed `AnalysisConfig.phase_count` selects the first phase-plan entry
whose maximum includes the rate (source `311d790efc1799b38066`, lines 124–128).
However, the caller actually invokes `phase_count_for_target(template_cfg, f)`,
whose definition in `commonref/resampling.py` is absent from the collector.
It then clamps the helper's requested count `R_f` to
`P_f = max(1, min(R_f, floor(F/f)))` (lines 1498–1504).
If that uncollected helper returns the phase-plan requests in the table, this
clamp changes none of them. That conditional calculation is not a replacement
for recorded per-run `phase_count` values.

Spacing is explicit conditional on the resulting count `P_f`. The caller
requires `grid_rate = f*P_f`, takes `grid[j::P_f]`, and assigns that phase's first
time to `-g/F + j/(f*P_f)`, for `j = 0, …, P_f-1` (lines 1521–1533).
Adjacent phases therefore have assigned separation `1/(f*P_f)`; samples within
a phase have assigned separation `1/f`. Relative to the physical record origin,
the offset in one target period is
`delta_j = (-g/F + j/(f*P_f)) mod (1/f)`.
For the 0.5-s guard and the conditional table counts, the 85-S/s phase labels
are permuted by a half-period shift; the offset set is still uniformly spaced.
The low-rate sample values themselves are produced by the missing
`phase_only_grid` helper. Its exact interpolation rule remains unverified. The alternative `anti_alias`
mode calls `resample_phase_grid` from the same missing module (lines 1505–1513);
its target-rate filter and resampling implementation also remain unverified.

### Fixed-endpoint integration and quantiles

Reference and reconstructed energies both call
`UniformLinearIntegral.integrate(start, stop)` at the same starts and stops.
The reference uses the appended endpoint described above; each reconstructed
phase uses the assigned target-rate grid and the padded input. The caller
therefore resolves interval selection and reference endpoint extension.
It does **not** resolve the helper's exact interpolation, partial-cell
quadrature, boundary handling, clipping or extrapolation: the implementation of
`UniformLinearIntegral` in `commonref/duration_sensitivity.py` was not exported.
Its name alone does not establish those numerical rules.

The within-run caller computes signed percent error using finite, nonzero
reference energies, combines the evaluated window/phase cases, removes
nonfinite errors and applies `quantile(abs(errors), 0.95)` (lines 1538–1580).
The cohort summary applies `quantile(run_q95, 0.95)` across physical runs,
producing both `hierarchical_abs_error_q95_pct` and
`run_abs_error_q95_q95_pct` (lines 1593–1634). This confirms the caller's
hierarchical order. The implementation of its `quantile` helper in
`commonref/utils.py` is absent, so its exact empirical-percentile interpolation
method is not newly established here.

The cache-energy QC uses a separate rule: `_integral` calls SciPy `trapezoid`
with `dx = 1/rate` on the native and reduced vectors, without the appended
endpoint (lines 156–160 and 405–420). The reduced vector is integrated before
its float32 cache conversion. In the observed source, the exported QC therefore
compares the native/reduced resampling integrals, rather than directly testing
every stored float32 value or the fixed-window integration helper. The existing
maximum discrepancy remains an integral-consistency check; it cannot verify
the missing reconstruction interpolation or endpoint quadrature.

## 3. Resolved, partial and still open

| Question | Result of this audit |
|---|---|
| Are the new collector results tied to the existing 59-pair frozen inputs? | **Resolved for file identity:** nine selected original-file hashes match the pinned package bytes; manifest inventory remains 59 pairs / 118 traces. |
| Which config and tool version are recorded? | **Resolved at artifact-record level:** generated six-workload config, tool 0.8.2 and completed artifact-only invocation; referenced template settings recovered. |
| How are starts and stops generated? | **Resolved in the observed caller; historical application partial:** endpoint-inclusive linspace, nearest analysis-grid rounding, deduplication, fixed stops and explicit short/full-record cases. |
| How many offsets were actually evaluated per rate? | **Partial:** 64/32/1 template requests and caller clamp recovered; helper implementation and recorded applied counts still missing. |
| How are offsets spaced? | **Resolved conditional on applied count in the caller:** spacing `1/(f*P_f)`, origin including the constant guard; sample-value interpolation remains open. |
| What is the exact low-rate interpolation and integration algorithm? | **Open:** `phase_only_grid`, the alternative `resample_phase_grid` filter/resampling branch, and `UniformLinearIntegral` definitions are absent. Fixed physical boundaries and reference endpoint extension are recovered. |
| What exact code/config hashes generated individual errors? | **Open:** observed source/config SHA-256 values are retained, but the artifact-refresh record and fingerprints do not certify historical numerical-execution code bytes. |
| What exact empirical quantile estimator was used? | **Open beyond ordering:** caller hierarchy is recovered; the `quantile` helper implementation is absent. |

The most direct remaining artifact is already identified by the collector:
`twix:/homes/kmika/energy_analysis/common_trace_analysis/edge_ai_multi_workload_v1/common_reference/per_run_common_reference.csv`.
It was skipped because its `8,986,170` bytes exceeded the collector's
`8,388,608`-byte text cap (`data/scan_issues.csv`, line 56).
The observed writer places `phase_count`, `window_count`, `observation_count`,
workload, instrument, run, rate, duration and mode in that file.
A bounded read of these existing recorded columns could settle applied counts
without new measurements or waveform reconstruction. The full and review
bundle builder deliberately omits per-run common-reference rows and caches
(source `39ff7ffa8dc923f76514`, lines 3981–3999), so their absence from the public
frozen bundle is expected.

Completion also needs the relevant historical `commonref/resampling.py`,
`commonref/duration_sensitivity.py` and `commonref/utils.py`, with a code/config
fingerprint or an archived numerical-execution manifest tying them to those
per-run rows. A current copy alone would extend the observed recipe but would
not by itself prove historical use.

The collector reports `field_limit` and `text_byte_limit` on `twix`,
`100,663,296` text bytes read, `50,000` fields, and
`historical_completeness_claim = false`. Its scan issues explicitly state that
absence of findings is not proof of absence. These selected limits are retained
in [coverage_excerpt.json](../data/provenance/reconstruction/coverage_excerpt.json).

## 4. Curated-source convention

`source_excerpts.json` retains each original source ID, host, original path,
original SHA-256/hash scope, source-catalog row and exact line-range text.
For every retained source, the collector's text export omits one final newline;
restoring only that newline reproduces its catalogued original SHA-256.
The export's own hash is also recorded, so an excerpt/export hash is never
misrepresented as a historical source hash. No unrelated portions of the
original files were copied into the package.

This evidence supports a more precise description of the recovered caller and
an explicit route to close the remaining gaps. It does not authorize replacing
the six-workload contract's unspecified historical offset count with the pooled
FP16 branch's up-to-64 setting, or labeling the complete recipe as historically
reproduced.
