# Methods and evidence specification — manuscript v0.15.1

This document supplies executable detail for the concise manuscript. The main
paper uses one explicit numerical specification for each experiment. Physical
cohorts remain separate; numerical windows and offsets are never counted as new
measurements. This package regenerates results from existing summaries. It does
not repeat raw-waveform acquisition, current calibration, integration or PSD
estimation. All calculations retain input precision; manuscript values are rounded
only for display.

[SOURCE_MAPPING.md](SOURCE_MAPPING.md) identifies every main table and figure.
[EXPERIMENT_CONFIGURATIONS.md](EXPERIMENT_CONFIGURATIONS.md) contains the detailed
workload configuration moved out of the main table. The selected scope and FP16
results are pinned to repository commit
`9b4208c97420b1621a14b7dc91f051985e65e6f5`; other frozen input snapshots keep their
own original provenance and are not represented as if newly acquired at that commit.

## 0. Publication scope: PARMA on Jetson, Hailo reserved for TIM

The PARMA manuscript uses Jetson throughout: the six-workload paired-scope study,
the separate all-15-run FP16 reconstruction/spectral study, eight direct-rate
workloads and seven duration/meter workloads. The original multi-platform input
exports remain unchanged. Hailo results and their estimator descriptions below
are retained for TIM and provenance, **not presented as PARMA results**. There is
no outcome-based exclusion or new signal processing in this scope change.

Figure 5 selects all six continuous GEMM/YOLO duration series plus variable YOLO
at the existing 300-s request. Each has 15 physical executions and all three
comparators (u.RECS, input telemetry, scaled Shelly), yielding 21 summary cells
and 315 pair comparisons from 105 physical executions. Each comparison uses the
same source series, fixed `envelope_0.5` policy and matching recording IDs, but
retains the sensor-specific integration span. The variable-activity result is
included with exactly the same rule, not discarded because it differs more.

Main selections are in `generated/parma_selection.json` and the
`generated/parma_*.csv` files. Full-platform derived tables without that prefix
remain supporting material. The scope decision and TIM boundaries are recorded
in `PARMA_TIM_SCOPE_v014.md`.

## 1. Energy, actual duration and integration

For an interval with endpoints \(t_0,t_1\), actual span \(T=t_1-t_0>0\), voltage
\(U(t)\) and current \(I(t)\),

\[
E=\int_{t_0}^{t_1}U(t)I(t)\,\mathrm{d}t,\qquad
\overline P=\frac{E}{T}.
\]

Where the stored signal is already calibrated power \(P(t)\), it is integrated
directly; it is not multiplied by a current calibration a second time. For
adjacent stored samples,

\[
E=\sum_{i=0}^{N-2}
 \frac{P_i+P_{i+1}}{2}(t_{i+1}-t_i).
\]

A uniform trace has \(N-1\) integration intervals. Timestamped telemetry retains
its stored time axis and is integrated piecewise-linearly. The requested
benchmark duration controls the command; it is not substituted for the actual
integration span in \(\overline P\). Recorded voltage treatment, calibration and
empirical scaling remain acquisition-specific.

The duration figure compares the median per-run power at request \(d\) with the
same series' 600-s-request median:

\[
D_d=100\left[
 \frac{\operatorname{median}_r\overline P_{d,r}}
      {\operatorname{median}_r\overline P_{600,r}}-1
 \right].
\]

The denominator is a within-series comparison point, not a proved steady-state
limit. The generator also exports empirical power Q05/Q95, scaled by this same
fixed median reference; those are descriptive run ranges, not confidence
intervals.

Sources: [metadata/FINAL_WINDOW_METHOD.md](metadata/FINAL_WINDOW_METHOD.md),
[metadata/DIRECT_SOURCE_METHODS.md](metadata/DIRECT_SOURCE_METHODS.md) and the
individual candidates in
[data/final_direct/plotted_candidates.csv](data/final_direct/plotted_candidates.csv).
Generators: [scripts/build_tables.py](scripts/build_tables.py) and
[scripts/extend_tables.py](scripts/extend_tables.py).

## 2. Direct-study load detector and retention policy

The detector operates offline on time-weighted means in nominal 100-ms bins.
Bin means are bin energy divided by actual bin duration. For uniform traces,
nominal edges are mapped to original sample indices with NumPy rounding; low
rates can therefore produce unequal bin durations. Timestamped signals retain
their own timestamps. Display interpolation does not increase physical telemetry
resolution.

Let \(T_{\mathrm{record}}\) be the stored recording span and
\(\ell=\min(2\,\mathrm{s},T_{\mathrm{record}}/5)\) the edge-region length.
A recording needs span at least 1 s, at least eight bins, and at least two bins
fully contained in each edge region. Define

\[
B=\min\{\operatorname{median}(P_{\mathrm{pre}}),
        \operatorname{median}(P_{\mathrm{post}})\},\qquad
H=Q_{0.95}(P_{\mathrm{bins}}),\qquad D=H-B,
\]

\[
s=1.4826\max\{\operatorname{MAD}(P_{\mathrm{pre}}),
             \operatorname{MAD}(P_{\mathrm{post}})\}.
\]

MAD is the median absolute deviation from the respective edge median.
The robust contrast requirement is

\[
D>\max\left\{
10^{-9}\,\mathrm{W},
0.005\max(|H|,|B|,10^{-6}\,\mathrm{W}),
6s
\right\}.
\]

For a fixed threshold fraction \(a\), qualifying activity remains strictly above
\(B+aD\) for at least 0.2 s, with the documented numerical time tolerance
\(10^{-10}\) s. The load envelope extends from the first through the last
qualifying segment and includes intervening pauses. The main candidate uses
\(a=0.5\); \(a=0.4,0.6\) assess sensitivity. No candidate is fitted to a requested
duration or selected to minimise energy, variation or a rate trend.

The series-level policy is fixed in
[data/final_direct/paper_window_policy.csv](data/final_direct/paper_window_policy.csv):
NPY-derived envelope 0.5 for every Jetson series, including the LLM and variable
YOLO. The retained TIM-only Hailo variable-YOLO series uses its recorded interval,
including padding; it is not in the PARMA tables or duration figure.
The final paper view retains all available finite results with positive spans.
Missing intervals remain missing. Edge, sensitivity and provenance notes do not
produce magnitude-based trimming of otherwise available candidates. The detector
does not establish a hardware-synchronised inference boundary.

Exact bin rounding, eligibility and flags are documented in
[metadata/FINAL_WINDOW_METHOD.md](metadata/FINAL_WINDOW_METHOD.md). This source
package reads the exported detector results; its generators do not rerun the
detector on raw traces. The 104-s FP16 reconstruction intervals and native
spectral windows below are separate definitions.

## 3. Direct rate summaries and paired-meter differences

### 3.1 Variation within a rate group

For \(n_j\) included run energies at tested rate group \(j\), define

\[
\mu_j=\frac{1}{n_j}\sum_r E_{j,r},\qquad
m_j=\operatorname{median}_r E_{j,r},\qquad
\sigma_j=\sqrt{\frac{1}{n_j}\sum_r(E_{j,r}-\mu_j)^2}.
\]

The within-rate energy coefficient of variation is

\[
\mathrm{CV}_{E,j}=100\frac{\sigma_j}{|\mu_j|}.
\]

The implementation uses the population standard deviation, with divisor
\(n_j\), or NumPy ddof = 0. Table 3 reports \(\max_j\mathrm{CV}_{E,j}\), not an
energy range, a maximum single-run error, or a total measurement uncertainty.

### 3.2 Displacement between rate groups

For \(J\) available rate groups, the reference is the equally weighted arithmetic
mean of the group energy means,

\[
E_{\mathrm{ref}}=\frac{1}{J}\sum_{k=1}^{J}\mu_k.
\]

The reported largest group deviation is

\[
B_{\max}=100\max_j\left|\frac{\mu_j}{E_{\mathrm{ref}}}-1\right|.
\]

This is not deviation from a 5-MS/s reference and not the range between the
largest and smallest group. The same mean-based statistic is used on both sides,
and each available rate group receives equal weight even when its valid run count differs.
The previous mean-versus-average-of-medians definition is superseded, not reproduced
as the current Table 3 statistic. Separate direct-rate groups contain separate physical executions;
\(B_{\max}\) includes execution and protocol effects and is not an isolated
sampling bias. All finite positive-span candidates under the series policy are
retained. Table 3 selects the eight Jetson series. Hailo-LLM variation stays
in the unchanged supporting source archive and is not a PARMA result.

Source tables:
[data/final_direct/groups_all_candidates.csv](data/final_direct/groups_all_candidates.csv)
and [data/final_direct/plotted_candidates.csv](data/final_direct/plotted_candidates.csv).
[scripts/build_tables.py](scripts/build_tables.py) recomputes group CVs and
\(B_{\max}\), writes
[generated/direct_rates.csv](generated/direct_rates.csv), and generates the Jetson-only Table 3. `generated/parma_direct_rates.csv`
records the explicit manuscript selection.

### 3.3 Paired-meter statistics

Meter pairing intersects record IDs within the same source series. Let
\(\mathcal R\) be that intersection, \(p\) denote PicoScope and \(s\) the other
sensor. Each meter retains its own integration interval and mean power.
Individual paired differences and the reported central statistic are

\[
d_r=100\left(\frac{\overline P_{s,r}}{\overline P_{p,r}}-1\right),\qquad
\Delta_{\mathrm{pair}}=\operatorname{median}_{r\in\mathcal R}d_r.
\]

The reported spread is \([Q_{0.05,r}(d_r),Q_{0.95,r}(d_r)]\), using linear
empirical quantiles. This range is not a confidence interval. The ratio of the
two group medians is retained as an explicitly named diagnostic column in
`generated/device_pair_spread.csv`, but is no longer the central statistic of
Figure 5 or the associated abstract/results ranges.
Identifying the same execution does not establish synchronous windows, equal
electrical boundaries or independently certified absolute accuracy.

[scripts/extend_tables.py](scripts/extend_tables.py) derives these statistics
from the exported candidates; outputs include
[generated/device_pair_spread.csv](generated/device_pair_spread.csv) and the
paired-meter manuscript table. `generated/parma_device_pair_spread.csv` and
`generated/parma_device_pair_values.csv` contain exactly the seven-workload
Jetson selection used in Figure 5; the unprefixed files retain both platforms.

## 4. Native same-trace energy reconstruction

### 4.1 Scope cohort and primary processing path

The cohort contains 59 paired executions, 118 source traces: GEMM-FP32,
GEMM-INT8, YOLO-FP32, YOLO-INT8 and Gemma3-4B each have IDs 0–9 in both
acquisition paths; ResNet-50 FP32 has IDs 0–8. Source sampling is 5,000,000 S/s.
Native calibrated/model-derived power is represented as float64. Each trace's
own native integral is the reference; the other scope is not substituted as
its energy ground truth.

The prescribed durations in seconds are
`[0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10]`. The target rates in S/s are
`[50, 85, 150, 240, 400, 680, 1200, 2000, 2500, 3300, 5500, 9400, 16000,
25000, 45000, 80000, 100000, 125000, 160000]`.

The source analysis uses up to 16 windows per duration and 64 sampling offsets.
The exact positions, interpolation, endpoint handling, exception handling and
eligibility checks are specified by the pinned analysis script, not inferred
from aggregate counts. The script and settings are linked below. The native
path adds no target-rate filtering. Source endpoints are retained when the
recorded power is interpolated onto each shifted target grid. At least four
target-rate samples are required. The nominal 10-s case uses one available
window with an actual span of 9.999999 s; shorter durations normally use 16.
At 20 ms / 150 S/s, only one numerical case per source recording is eligible;
this cell is not a complete 16 × 64 comparison and determines none of the
reported persistent minima.

For recording r, window w and offset k:

\[
 e_{r,w,k}=100|E_{r,w,k}-E_{r,\mathrm{ref}}|/E_{r,\mathrm{ref}},
 \quad q_r=Q_{0.95,w,k}(e_{r,w,k}).
\]

The group statistic is `Q95` of the per-recording q values. The envelope is the
maximum of these statistics across six workloads and two acquisition paths.
Quantiles use NumPy's linear/type-7 convention. The effective sample count for
between-recording aggregation is the number of physical traces in each group,
not the product of windows and offsets. Neither Q95 level is a confidence bound.

The paired processing-path comparison uses the same windows and offsets after
soxr VHQ reduction to 1 MS/s, with 0.5-s constant endpoint guards that are removed
after filtering; reduced data are float32. Both paths use the same native
reference integral. Consequently this tests the combined resampling,
representation and interpolation path, not just a separately identified filter
or a frequency band above 500 kHz. It is a robustness analysis, not a second
main result table.

Sources: `data/robustness_20261009/scopes_run_settings.json`,
`scope_persistent_minima.csv`, `scope_selected_envelope.csv`, and the explicitly
selected fixed-rate excerpt in `data/final_reconstruction/`. The excerpt is not
claimed to be the complete source CSV. Its source row numbers, repository path
and Git blob identity are in `data/final_reconstruction/SOURCE.json`.

Upstream complete analysis and result files at the pinned commit:
- `energy-measurement/2026-10-09-offline-robustness/energy_paper_checks.py`;
- `.../scopes/scope_per_run.csv`, `scope_groups.csv`, `scope_envelope.csv`;
- `.../scopes/record_audit.jsonl`, `critical_comparisons.jsonl.gz` and
  `archive_index.json`;
- `.../review/audit_scope_results.py` and `scope_persistent_minima.csv`.

### 4.2 FP16 long-window energy

The primary FP16 summary uses all 15 available recordings, IDs 0–14. It is a
separate cohort from the six-workload scope study. Each recording contributes a
104-s nominal energy interval with actual integration span 103.9999998 s and
64 offset cases at each of 50, 85 and 2,000 S/s. There are 960 numerical cases
per target rate, not 960 physical measurements. Reference and reconstructed
energy use the same native stored-power trace and endpoints. The reported Q95
pools the 15 × 64 errors with equal offset counts per recording.

The manuscript does not claim a rate minimum over untested rates. At 50 S/s the
native pooled Q95 is 0.6349568548870242%; at 85 S/s the largest native case is
0.8783758253321633%; at 2,000 S/s native pooled Q95 is 0.09323977142936536%.
The intermediate-processing comparison and subset summaries remain preserved
as sensitivity evidence, but are not mixed into those main statistics.

Input: `data/robustness_20261009/fp16_energy_selection.csv`, rows
`cohort=all_ids_0_to_14`, native columns. The generated
`generated/final_fp16_energy.csv` preserves all selected fields.

## 5. Fixed-rate tests and persistent rate selection

At a fixed rate f and duration T, a criterion is met when the envelope is at
most the stated tolerance. The persistent minimum for that duration requires
the criterion at f **and at every higher eligible rate in the tested grid**.
A higher rate can fail after a lower rate passes; therefore the first pointwise
pass is not a persistent minimum. Neither rule extrapolates to untested rates,
intervals or signal classes.

`generated/final_native_duration_table.csv` combines the nine fixed-2-kS/s
native values with the audited native persistent minima. It never takes the
pointwise minimum over the native and reduced paths. The 2-s / 1% persistent
minimum is 16 kS/s; 2 kS/s still passes its individual test. At 5 s it is
1.2 kS/s. At 50 ms the 0.5% criterion is not achieved within the grid through
160 kS/s. The full 36 duration/tolerance rows stay in the source package.

## 6. Spectral estimators and their measurement meaning

### 6.1 All-15-run, matched-interval FP16 estimator

The manuscript uses the `all_ids_0_to_14` / `matched_4s_4s` branch of
`data/robustness_20261009/fp16_psd_selection.json`: all 15 recordings, a 4-s
active segment from the workload middle and a 4-s pre-idle segment ending
0.5 s before the workload interval. The numerical source analysis at 1 MS/s
uses separate mean removal, one-second Hann Welch segments and 50% overlap,
so both intervals provide seven complete segments. This is the matched-length
estimator, not the 10-s/4-s branch.

For each recording, subtract the idle PSD from the active PSD and clip the
difference below zero. Coverage at rate f is the integral below f/2 divided by
the positive-excess integral over the available analysis band. This is measured
fluctuation variance, not energy in joules. The method does not deconvolve the
analogue path and does not claim that positive clipping removes noise bias.

The criterion is the empirical fifth percentile of per-recording coverage,
with linear quantiles. The source summary provides evaluated coverage at 2,
125 and 160 kS/s. Figure 3 displays the complementary variance **above** Nyquist,
with median and empirical Q05/Q95 across recordings. For this complement, the
bounds reverse: its lower bound is `100 − coverage_Q95`, upper bound
`100 − coverage_Q05`. No curve is interpolated between the three rates and no
spectral minimum is inferred from this three-rate summary.

At 125/160 kS/s, coverage Q05 is 97.5407884421667% / 99.31955963392936%.
Both meet the declared 95%/99% targets. The all-recording 10-s/4-s and subset
branches are retained as robustness evidence. The source record-level PSD
checks also include split-idle comparisons; their small nonzero differences
are diagnostics rather than a formal uncertainty budget.

The full-precision selected inputs are exported as
`generated/final_fp16_coverage.csv`. The generator reads existing PSD summaries;
it does not estimate new spectra from raw recordings.

### 6.2 Native paired-scope median-spectrum comparison

This six-workload comparison uses native 5-MS/s estimated-power spectra,
10-s active intervals and 11 separate 10-s idle recordings per acquisition
path. Welch uses 1,048,576-sample Hann segments and 50% overlap. The native
spectra cover 0–2.5 MHz; they do not use the 1-MS/s reconstruction cache.

For instrument \(m\), workload \(a\), active recordings \(r\) and idle
recordings \(j\), the estimator is

\[
S_{\mathrm{exc},m,a}^{\mathrm{native}}(f)=
\max\left\{
\operatorname{median}_r S_{\mathrm{active},m,a,r}(f)
-\operatorname{median}_j S_{\mathrm{idle},m,j}(f),0
\right\}.
\]

Thus the medians are taken before subtraction and clipping; this is distinct
from the FP16 per-recording order. Each path's full-band CDF divides by its own
integral over 0–2.5 MHz. The conditional CDF is

\[
C_{m,a}^{77}(f)=
\frac{\int_0^f S_{\mathrm{exc},m,a}^{\mathrm{native}}(\nu)\,\mathrm{d}\nu}
     {\int_0^{77000\,\mathrm{Hz}}S_{\mathrm{exc},m,a}^{\mathrm{native}}(\nu)\,\mathrm{d}\nu},
\qquad 0\le f\le77000\,\mathrm{Hz}.
\]

For the respective full or conditional frequency domain \(\mathcal B\), the
reported setup difference is

\[
\Delta_{\mathrm{CDF}}=100\max_{f\in\mathcal B}
|C_{\mathrm{Tek},a}(f)-C_{\mathrm{Pico},a}(f)|.
\]

It is measured in percentage points, not energy-error percent. Separately
normalising within 0–77 kHz changes the denominator and distinguishes low-band
shape agreement from differences in full-band spectral fractions. The nominal
77-kHz current-path bandwidth is not a hard cutoff, a noise criterion or an
independently certified transfer function. No deconvolution is applied. These
aggregate CDF differences are not per-recording uncertainty intervals.

Sources:
[data/validation/multi_workload/setup_comparison.csv](data/validation/multi_workload/setup_comparison.csv),
[data/validation/multi_workload/JOURNAL_METHODS.md](data/validation/multi_workload/JOURNAL_METHODS.md),
[data/validation/native_spectra/spectral_sources.json](data/validation/native_spectra/spectral_sources.json)
and [metadata/NATIVE_SPECTRAL_SOURCE.json](metadata/NATIVE_SPECTRAL_SOURCE.json).
[scripts/extend_native_spectra.py](scripts/extend_native_spectra.py) selects the six
power/excess comparisons and generates the manuscript ranges from exported
metrics. It does not recompute the CDFs from waveform samples.

### 6.3 Reserved TIM evidence: native Hailo per-recording estimator

This branch is not reported in the PARMA manuscript. It is preserved without
reanalysis for TIM. The Hailo branch uses 15 GEMM and 15 YOLO stored-power recordings at
5 MS/s, 10-s active prefixes and idle from the same recording. Welch uses
1,048,576-sample Hann segments, 50% overlap, constant detrending per segment,
one-sided density scaling and mean averaging of complete segments within each
recording. Physical recordings receive equal weight; they are not concatenated.

Positive active-minus-idle spectra and frequency metrics are calculated per
recording, then summarised by their medians and empirical Q05/Q95. The estimator
order is not the native Tek/Pico median-spectrum order. Hailo prefixes, FP16
middle-of-run windows and native paired-scope spectra remain separate cohorts.
An active prefix is not evidence of matched models, precision, batch or
measurement boundaries across platforms. The Hailo spectra do not establish a
Hailo minimum energy sampling rate.

Source:
[data/git/platform_spectral_metrics.csv](data/git/platform_spectral_metrics.csv),
matched-prefix active/excess rows, with the method contract in
[data/validation/multi_workload/JOURNAL_METHODS.md](data/validation/multi_workload/JOURNAL_METHODS.md).
[scripts/extend_tables.py](scripts/extend_tables.py) extracts the archived per-run
summary ranges; [scripts/make_paper_figures.py](scripts/make_paper_figures.py)
draws the supplementary source-package spectral figure.

## 7. Fixed-window comparison and complementary acquisition control

The historical fixed-window branch includes 225 recordings: five workloads,
three acquisition rates (2 kS/s, 250 kS/s, 5 MS/s), fifteen repeats each,
integrated over record-relative 20–80 s. The supplied public evidence contains
the exported group summaries; the local generator checks their median ratios.
It does not reintegrate the 225 raw waveforms.

The complementary GEMM-FP16 control uses the same engine, 250 completed queries,
the documented spin-wait option and a 120-s process-end-to-next-start pause.
With \(A=2\) kS/s and \(B=5\) MS/s, the session orders are ABBAAB and BAABBA.
Each of the six sequence positions contains one observation at each rate
across sessions. All twelve runs are retained, six per rate.

For outcome \(Y_{s,p}\), with session \(s\in\{1,2\}\) and position
\(p\in\{1,\ldots,6\}\), the additive model is

\[
Y_{s,p}=\alpha+\beta\,\mathbf1(f_{s,p}=5\,\mathrm{MS/s})
        +\gamma_s+\eta_p+\epsilon_{s,p}.
\]

The reference coding sets \(\gamma_1=0,\eta_1=0\). The design matrix has an
intercept, rate indicator, one session indicator and five position indicators:
rank eight for twelve observations, hence four residual degrees of freedom.
Position is categorical; the model does not impose linear drift. It assumes
common position effects across sessions and additive session differences, with
no fitted session-by-position or rate interaction.

For design matrix \(X\), outcome vector \(y\) and coefficient vector \(\theta\),
ordinary least squares and the implemented standard-error calculation are

\[
\widehat\theta=(X^\top X)^{-1}X^\top y,\qquad
\widehat\sigma^2=\frac{\|y-X\widehat\theta\|^2}{4},\qquad
\operatorname{SE}(\widehat\beta)=
\sqrt{\widehat\sigma^2[(X^\top X)^{-1}]_{\beta,\beta}}.
\]

The two-sided model interval is

\[
[\beta_{\mathrm{lo}},\beta_{\mathrm{hi}}]=
\widehat\beta\pm t_{0.975,4}\operatorname{SE}(\widehat\beta).
\]

These are the ordinary OLS t intervals, using the fitted residual variance,
not heteroskedasticity-robust or cluster-robust intervals. Their usual
inferential interpretation depends on the model's residual assumptions; this
small control does not independently establish those assumptions.

For the selected outcomes' positive 2-kS/s reference mean
\(\overline Y_{2k}\), the displayed estimate and interval are

\[
\Delta_Y=100\frac{\widehat\beta}{\overline Y_{2k}},\qquad
\left[
100\frac{\beta_{\mathrm{lo}}}{\overline Y_{2k}},
100\frac{\beta_{\mathrm{hi}}}{\overline Y_{2k}}
\right].
\]

The observed 2-kS/s mean is the common scaling denominator; the script does
not fit a separate ratio model or propagate denominator uncertainty.
The sign is 5 MS/s minus 2 kS/s. The three manuscript outcomes are PicoScope
mean load power, Jetson VDD_IN load power and TensorRT runtime. Fourteen
exported outcomes are independently refitted in the generator.

The intervals characterise this configured control under its model. They are
not a metrological uncertainty budget, a causal drift mechanism, an equivalence
test or proof of universal equality between rates. No historical trace receives
a rate, drift, baseline or gain correction from this model.

Sources:
[data/validation/controlled/fixed-window/data/main_summary.csv](data/validation/controlled/fixed-window/data/main_summary.csv),
[data/validation/controlled/complementary/data/combined_runs.csv](data/validation/controlled/complementary/data/combined_runs.csv),
[data/validation/controlled/complementary/data/balanced_effects.csv](data/validation/controlled/complementary/data/balanced_effects.csv)
and [metadata/CONTROLLED_SOURCE.json](metadata/CONTROLLED_SOURCE.json).
[scripts/extend_controlled.py](scripts/extend_controlled.py) verifies the pinned
inputs, refits all fourteen outcomes, checks the upstream values and generates
[generated/controlled_effects.csv](generated/controlled_effects.csv) and Table 4.

## 8. Calibration, transformations and interpretation limits

The EA-EL 9080-60 DT electronic load and Fluke 179 reference supply 36 load
settings over 0–3.5 A, ten-second means, endpoint gain/offset calibration and a
separate verification sweep. There are 35 nonzero verification settings per
shunt-based path. The maximum absolute relative current deviations are 1.98%
(PicoScope) and 0.44% (u.RECS); medians of the signed deviations are −0.038%
and −0.047%. The u.RECS 300-Hz sinusoidal ADC test reports SINAD 58.9 dB,
9.49 effective bits. Neither static verification nor this ADC test establishes
absolute dynamic-power uncertainty.

The source calibration workbook, exported verification rows, original fit
specification, arithmetic checks and qualifications are retained under
`data/validation/calibration/`, `metadata/CALIBRATION_VALIDATION.md` and
`metadata/TRANSFORMATION_PROVENANCE_20261004.md`. Those documents distinguish
documented configurations from proof of application to every acquisition.
No additional fit was introduced in this revision.

For the paired-scope cohort:

\[
 \widehat V(I) = 19.062607082705\;\mathrm V
              -0.07444582\;\mathrm{V/A}\,I,
 \qquad \widehat P(I)=I\widehat V(I).
\]

The stated model range is 0–3.5 A. The completed source check flags values outside
this range in 51 of 118 records (49 Tektronix, two PicoScope); values are
extrapolated rather than clipped. **Record counts are not the fraction of samples
outside the range.** The compact record audit is available at the pinned Git
location. No sample fractions or timing distributions are inferred from the
record-level flags.

Only YOLO-FP32 has the documented workload-specific Tektronix current-offset
correction. This prevents treating that workload's corrected absolute level as
an independent agreement test. Since model-derived power is quadratic in
current, subtracting a constant current offset need not be spectrally neutral
for power, even after mean removal. Other recorded transformations, including
the approximately 0.97 setup-derived Jetson u.RECS factor and empirical Shelly
scaling, are not silently removed or applied to other cohorts. Refer to the
transformation-provenance sheet for the available scope of those records.

The 250-MS/s reference check is retained in
`data/robustness_20261009/high_rate_coverage.md`. Its six workloads have less
than 0.02% measured spectral variance above 2.5 MHz. GEMM-FP32 is active-only;
the others use active-minus-idle. This supports the chosen reference for the
observed signals, not a universal instrument transfer function or accuracy
certificate. AC, selected DC input, module/card and telemetry boundaries remain
physically different even when results are paired by run ID.

## 9. Reproduction and availability

`bash build.sh` compiles the supplied manuscript without reanalysis.
`bash regenerate.sh` rebuilds manuscript tables and figures from included result
exports, rechecks frozen input identities and numerical aggregation, then compiles
and checks the PDF. It reads no raw waveform files. See the root README for the
Python/TeX environment and source mapping.

The package contains the inputs needed for these main outputs. It does not
contain the full raw waveform collection, the >500-MB complete scope result ZIP,
or all record-level compact comparison vectors. Those remain at the documented
laboratory or pinned repository locations. The current artifact supports
**result-summary regeneration**, not a claim of complete acquisition-level
reproduction. Missing model/build settings and acquisition metadata remain
limitations; they are not filled by general device specifications.

Previous manuscript descriptions are retained under `metadata/baseline_v012/`
and `revision_history/v013/` only for provenance. Their cohorts or publication
scope must not override this specification. The author-supplied boundary artwork
has been adapted to remove the Hailo alternative; its original SVG/PDF is retained
under `revision_history/v013/figures/`. This is a presentation change, not new
wiring or a new measurement campaign.

## v0.15.1 presentation and reproducibility

Figure 5 plots only the 21 workload/comparator medians, without percentile bars.
No underlying repetitions or percentile values are removed: the full 315 pair rows
and their Q05/Q95 summaries remain in `generated/parma_device_pair_values.csv`
and `generated/parma_device_pair_spread.csv`. The old detailed table is retained
as a supporting output only and is not included in the manuscript.
`make_device_comparison.py` reads the exact selected summaries; independent
verification reconstructs the ratios from the unchanged candidate inputs.
