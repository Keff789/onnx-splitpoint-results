# Current methods and evidence specification — IEEE TIM v0.3

## 1. Scope and provenance

This document describes the manuscript's actual calculations. The supplied TIM
v0.1 is the structural starting point; the final PARMA v0.15.1 numerical
conventions supersede its old 1-MS/s-primary, 13-recording and mixed-aggregation
conventions. This history is preserved here, not narrated in the main paper.
The fixed evidence source is `Keff789/onnx-splitpoint-results` at
`85eb488587a51659239c45d966f930f7c7b72a6e`.

The inputs are exported outcomes and already estimated spectra. This package
regenerates their summaries, not acquisition or raw-waveform reconstruction.
`provenance/parma_v0151_METHOD_DETAILS.md` preserves the full source method
specification unchanged. Its PARMA-only publication statements are prior scope,
not the current journal scope. Its references to metadata resolve to the copied
`provenance/parma_v0151_metadata/` source records where included. The current
source mapping, rather than an old package's relative path, governs this package.

## 2. Electrical quantity and time interval

Energy is the integral of recorded/calibrated power over the retained interval.
Mean power is that energy divided by **actual span**, not requested runtime.
For equally spaced stored samples the integral has N−1 intervals; telemetry
retains timestamps. Separate device intervals remain separate. A matching run ID
identifies the same execution, not common start/end timestamps or common rails.

Jetson: selected module-associated DC input on u.RECS. Hailo: complete M.2 card
input, excluding the host. Shelly: the connected AC supply arrangement, with
recorded empirical scaling. The arrangement does not independently establish
all host consumption. Vendor telemetry retains its own reported domain. Thus an
AC/DC difference is neither an intrinsic meter error nor a measured host share.

## 3. Load-window selection and finite cases

`data/final_direct/paper_window_policy.csv` fixes a rule per series. The default
is `envelope_0.5`. The detector uses energy/time-weighted 100-ms bins, edge
medians for baseline, the global bin P95 for active level, relative and robust
contrast checks, at least 200 ms of qualifying activity and the envelope from
first to last qualifying segment. Internal pauses are retained. Fractions 0.4
and 0.6 are sensitivity candidates, not selectable alternatives chosen by the
appearance of a curve. The complete implemented eligibility and edge rules are
in the copied `FINAL_WINDOW_METHOD.md` and prior method specification.

Hailo variable YOLO uses `reported_legacy`, the source's name for its explicitly
recorded interval including padding. That input label is not renamed in source
CSVs. This applies consistently to its rate and duration series. A high initial
level does not justify inventing a detected onset. The separate Jetson
`random_pattern_yolo_adjusted` series is not selected as another ordinary repeat.

The generator selects primary Jetson/Hailo summary series. Direct-rate results:
12 series, 323 groups and 4842 finite records. Eight Jetson series contribute
215 groups and 3225 records; four Hailo series contribute 108 groups and 1617
finite records. Three Hailo-LLM intervals are unavailable. No zero or alternate
window replaces them. Duration results: ten series, 100 groups; 1022 finite
Jetson load records and 450 finite Hailo load records. Actual counts remain in
the generated table; missing source outcomes are not recreated.

## 4. Pairwise energy, power and span

For every series/request/comparator, intersect unique execution IDs with
PicoScope. For each matched pair and X = E, P or T:

`delta_X_pct = 100 * (X_sensor / X_Pico - 1)`.

Calculate P from that path's E/T. Report medians of individual differences;
empirical fifth and 95th percentiles use linear/type-7 interpolation. Do not use
the ratio of group medians as an interchangeable estimator. Per pair:

`E_sensor/E_Pico = (P_sensor/P_Pico) * (T_sensor/T_Pico)`.

This identity does not hold in general after independently taking medians. The
numerical audit therefore checks all individual identities, not a product of
three displayed median values.

At 300 s there are seven Jetson and three Hailo workloads, 15 executions each:
**150 physical executions, 450 comparator pairs and 30 summary cells**. Across
the ten requests there are 4416 available pair rows and 300 summary cells. A run
observed by three comparators is not three independent physical executions.
Hailo has exactly 15 pairs per comparator/workload/request. The deployed-meter figures display
medians without percentile brackets; full distributions remain in CSV.

The duration-wise energy/power/span comparison is newly assembled for TIM v0.2
from existing outcomes. No endpoints, readings or scaling coefficients are
changed. At the variable-Hailo 5-s request the retained Pico span is 7 s;
paired HailoRT medians are about −0.71% power, −10.31% energy and −9.69% span.
This describes interval-specific procedures, not loss of a synchronised event
or a directly measured telemetry lag.

## 5. Duration and direct-rate summaries

Duration curves calculate P_r = E_r/T_r and divide by the workload's median P
in its 600-s group. Fifth/95th percentiles use the same **fixed group median**
as denominator. The 600-s group is a comparator, not a proven steady state.

Within-rate energy CV uses population standard deviation divided by the mean.
The reference for between-rate group displacement is the unweighted mean of
rate-group energy means. The maximum absolute percentage displacement is
reported. This replaces the mixed mean/median statistic in TIM v0.1; it does
not change any energy integration. Direct-rate observations are separate
executions, not a same-trace sampling-error distribution.

## 6. Native Jetson reconstruction reference

There are 59 paired executions / 118 source traces: ten pairs each for
GEMM-FP32, GEMM-INT8, YOLO-FP32, YOLO-INT8 and Gemma3-4B, and nine for
ResNet-50 FP32. Use native derived power at 5 MS/s as the main source. The
1-MS/s VHQ path is a sensitivity branch, not the main table.

The fixed grid contains nine nominal durations (20, 50, 100, 200, 500 ms;
1, 2, 5, 10 s), 19 rates from 50 to 160000 S/s, up to 16 distributed windows
and 64 offsets per rate. Four target-grid samples are required. Actual source
endpoints are used; nominal 10 s has span 9.999999 s and one eligible full
window. The 20-ms/150-S/s edge cell has only one valid case per recording and
changes none of the quoted persistent minima. See exact source settings in
`data/robustness_20261009/scopes_run_settings.json`.

The hierarchy is inner Q95 over window/offset cases per recording, then Q95
across recordings, then maximum across workload/acquisition-path groups. It is
an empirical envelope, not a confidence guarantee. A persistent minimum must
pass at that rate and every higher eligible **tested** rate. Fixed 2 kS/s
passing at 2 s therefore coexists with a 16-kS/s persistent 1% minimum. No
untested rates are interpolated.

TIM Table II now presents all nine duration rows, including the native 1-% and
0.5-% persistent minima. The source also retains all 36 duration/tolerance
combinations. This is a fuller presentation of the same source, not a new run
on 118 raw traces.

## 7. FP16 all-15 reference

The energy cohort is all 15 IDs 0–14, 64 offsets at each of the three evaluated
rates (50, 85, 2000 S/s), hence 960 numerical cases per rate. Its nominal 104-s
energy interval is actually 103.9999998 s. The pooled energy Q95 is not the
six-workload hierarchy. At 50 S/s native Q95 is 0.6349568549%; individual
cases can exceed 1%. All tested 85-S/s cases remain below 1%.

The primary spectral branch is `matched_4s_4s`: all 15 recordings, 4-s active
and idle segments, 1-MS/s analysis representation, 1-s Hann Welch segments,
50% overlap (seven complete segments on each side). Subtract each recording's
idle PSD from its active PSD and clip positive; integrate and calculate its
coverage fractions before cross-recording empirical quantiles. The Q05
criterion tests 95/99% fractions at the evaluated 125/160 kS/s rates. This
three-rate selection is not a new complete minimum-rate search. Robustness
variants and source estimator detail remain in the source package.

## 8. Native spectral comparisons

Hailo: 15 GEMM plus 15 YOLO native recordings, 10-s matched active prefixes and
same-record idle. Welch uses 1048576-sample Hann segments, half overlap,
constant detrending, one-sided density and mean segment averaging. Compute
active and positive-excess metrics per recording, then empirical quantiles
across recordings. Active and excess are two estimators on the same 30
recordings, not 60 recordings. Data are from
`data/git/platform_spectral_metrics.csv`, `window=matched_prefix`,
`basis=active|excess`.

Paired Jetson scopes: native 5-MS/s derived power, 10-s active records and 11
independent 10-s idle records per path. Take pointwise median active and idle
spectra separately, subtract and clip, then compare cumulative spectra. Full
band is 0–2.5 MHz; restricted curves are independently renormalised over
0–77 kHz. Those denominators and estimator orders must not be pooled with
FP16 or Hailo. The native-CDF figure selects power/excess rows from
`data/validation/multi_workload/setup_comparison.csv`.

PSD units are W²/Hz; area is W², not joules. The nominal 77-kHz analogue
bandwidth is neither a brick-wall cutoff nor an anti-alias guarantee at 2 kS/s.
Positive excess is descriptive and may retain estimation noise. There is no
transfer-function deconvolution, new spectral estimation, frame/layer
attribution or Hailo energy-rate bound computed in this package.

## 9. Protocol controls

The fixed-window comparison uses existing 225 Jetson recordings across five
workloads, three rates and 15 repeats, evaluated at record-relative 20–80 s.
It changes the window question but still compares independent executions.

The complementary control uses 12 FP16 outcomes: two sessions ABBAAB / BAABBA,
A=2 kS/s, B=5 MS/s, same engine, 250 completed queries, useSpinWait, 120-s
process-end-to-next-start waits. The design columns are intercept, rate
indicator, session indicator and five position indicators. Rank=8, residual
df=4. Ordinary least squares estimates the rate term; its two-sided 95% t
interval and estimate are divided by the observed 2-kS/s mean. No interaction
model, equivalence bounds or calibration-uncertainty propagation is implied.
The generator refits this from `combined_runs.csv` and cross-checks the source
`balanced_effects.csv`.

The separate FP32 pause diagnostic has one conditioning run (excluded by design)
and six scored 100-query runs, pauses 20/120/120/20/20/120 s, continuous 2-kS/s
acquisition, no per-run inline analysis. Three runs per condition in one session
support a diagnostic, not a causal randomised trial. Only runtime and pre-start
GPU temperature are used here. Original power/energy columns remain preserved
but are not treated as independently calibrated absolute Jetson energy.
The input blob is `bfc92d1b235ffbfd774e2953f3a08921b8855dfc`; its fixed repository
path and commit are in `data/pause/SOURCE.json`. Frequency readouts remaining
unchanged are counterevidence against claiming observed clock throttling.
Waiting energy is not included in activity energy.

## 10. Calibration and limits

Current verification uses an electronic load and Fluke reference, endpoint
gain/offset and an independent sweep over 36 settings (35 nonzero settings
for relative errors), ten-second means. Full verification points, the original
calibration workbook and transformation evidence are under `data/validation/`
and `data/provenance/`. We do not interpret every workbook sheet or refit it.

Paired-scope derived power uses P = I(a+bI), the recorded voltage model over
0–3.5 A; out-of-range values are extrapolated. Exact coefficients, units and
operator order are retained in the source transformation files and the prior
method specification. YOLO-FP32's workload-only current correction remains
disclosed; it does not create an independent validation of absolute agreement.
Jetson embedded and Shelly setup scaling is retained, not estimated anew from
this comparison. Current verification and nominal ADC/bandwidth properties do
not amount to a complete dynamic power uncertainty budget.

## 11. Reproduction boundary

This package checks arithmetic, selection, plotting and manuscript consistency
from frozen exports. `metadata/INDEPENDENT_QA.json` is a separate standard-library
calculation of pairs, type-7 quantiles, rate groups and duration curves.
`INPUT_PRESERVATION.json` verifies the 79 inherited data files. Raw traces,
some execution-bound deployment fields, Hailo same-trace energy distributions,
separate host measurements and synchronised telemetry timing are not supplied
by a successful reproduction. Their status is stated in the separate work plan.

## 12. Self-contained extension policy for v0.3

The journal states the foundational quantities, sampling experiment, aggregation
and spectral coverage equations in the main text and presents all central Jetson
results. It does not require the reader to reconstruct the argument from the
preceding manuscript. The introductory attribution identifies the reused basis;
`EXTENSIONS_VS_PARMA.md` separates context from additional experimental evidence.
All v0.2 numerical conclusions and input definitions are retained. Additional GPU
measurements remain pending, not an inferred third-platform outcome.
