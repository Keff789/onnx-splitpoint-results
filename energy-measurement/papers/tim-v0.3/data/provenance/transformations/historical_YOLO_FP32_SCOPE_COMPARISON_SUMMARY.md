# YOLO-FP32: Tektronix-primary PSD and PicoScope validation

Dataset root: `/homes/jwachsmuth/power_measurements/tek_scope_comparison/yolofp32`
Dataset ID: `yolofp32`

Each rate directory is analysed independently. The short records are repeated, simultaneously triggered observations and are never concatenated into an artificial long trace.

The Tektronix-native current-probe measurement is the primary spectral reference. The PicoScope/INA225 path is evaluated against that reference within the common bandwidth. Above 5 MS/s, the PicoScope remains fixed at 5 MS/s while the Tektronix rate increases.

Same-run pre-benchmark idle is preferred. When it is unavailable, the tool may use an independent exact-rate idle median from `/homes/jwachsmuth/power_measurements/tek_scope_comparison/idle`. Raw absolute current and energy are always preserved; idle-subtracted active-window results are reported only as additional diagnostics. If the paired idle campaign reveals a material, bounded and cross-rate-stable additive Tektronix zero error, a separately marked offset-corrected salvage result is also emitted.

Empty directories, one-sided pairs, unreadable files, and duration-mismatched pairs are skipped read-only and documented under `input_discovery/`.

## Adaptive Tektronix zero-offset handling

- Status: `stable_offset_detected_and_corrected`
- Offset detected: `True`
- Offset applied: `True`
- Estimated offset: 111.917 mA
- Applied offset: 111.917 mA
- Estimated uncertainty: 4.092 mA
- Reference rates: `[2500, 25000, 100000, 1000000, 5000000, 12500000, 25000000, 62500000, 125000000, 250000000]`
- Reference pairs: 100
- Confidence: `high`
- Validation independence: `post_hoc_workload_minus_external_idle_session_shift_not_independent`
- The correction is additive only. Raw metrics remain archived and no gain correction is fitted or applied.

## Time-domain agreement by rate

| Tek rate | Pico rate | Duration | Pairs | Median raw $\Delta E$ | q95 raw $|\Delta E|$ | Median selected $\Delta E$ | q95 selected $|\Delta E|$ nominal | Zero correction | q95 incremental $|\Delta E|$ | Idle source(s) | Median selected $\Delta I$ | Selected corr. | Window |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 2.5 kS/s | 2.5 kS/s | 10 s | 10 | +10.7255% | 10.8819% | +0.9344% | 1.0885% | 111.917 mA | 0.4231% | external_rate_matched_median:10 | 11.642 mA | -0.010101 | 100.000 ms |
| 25 kS/s | 25 kS/s | 10 s | 10 | +10.7602% | 10.8704% | +0.9151% | 0.9870% | 111.917 mA | 0.4395% | external_rate_matched_median:10 | 11.357 mA | 0.029745 | 100.000 ms |
| 100 kS/s | 100 kS/s | 10 s | 10 | +10.7346% | 10.8485% | +0.9097% | 0.9568% | 111.917 mA | 0.4590% | external_rate_matched_median:10 | 11.335 mA | 0.222867 | 100.000 ms |
| 1 MS/s | 1 MS/s | 10 s | 10 | +10.3813% | 10.6014% | +0.6198% | 0.6973% | 111.917 mA | 0.1393% | external_rate_matched_median:10 | 7.683 mA | 0.944922 | 100.000 ms |
| 5 MS/s | 5 MS/s | 10 s | 10 | +10.3943% | 10.7569% | +0.6131% | 0.7793% | 111.917 mA | 0.2536% | external_rate_matched_median:10 | 7.608 mA | 0.949101 | 100.000 ms |
| 12.5 MS/s | 5 MS/s | 5 s | 14 | +10.3565% | 10.4111% | +0.5882% | 0.6254% | 111.917 mA | 0.1435% | external_rate_matched_median:14 | 7.280 mA | 0.961227 | 100.000 ms |
| 25 MS/s | 5 MS/s | 2.5 s | 17 | +10.2247% | 10.4860% | +0.4657% | 0.5163% | 111.917 mA | 0.1804% | external_rate_matched_median:17 | 5.694 mA | 0.967263 | 100.000 ms |
| 62.5 MS/s | 5 MS/s | 1 s | 10 | +10.2931% | 10.4168% | +0.4988% | 0.5235% | 111.917 mA | 0.0562% | external_rate_matched_median:10 | 6.139 mA | 0.969066 | 100.000 ms |
| 125 MS/s | 5 MS/s | 0.5 s | 20 | +10.1642% | 10.4386% | +0.4008% | 0.4474% | 111.917 mA | 0.1521% | external_rate_matched_median:20 | 4.919 mA | 0.989565 | 50.000 ms |
| 250 MS/s | 5 MS/s | 0.25 s | 20 | +10.1837% | 10.2981% | +0.3897% | 0.4587% | 111.917 mA | 0.1732% | external_rate_matched_median:20 | 4.770 mA | 0.999324 | 10.000 ms |

## Primary Tektronix PSD reference

- Selected Tektronix rate: 25 MS/s
- Simultaneous PicoScope rate: 5 MS/s
- Paired segments: 17
- PSD basis: `active_minus_prebenchmark_idle`
- Tektronix $f_{95}$: 363.831 kHz
- Tektronix $f_{99}$: 539.324 kHz
- Workload-related variance above 77 kHz: 37.583%
- Workload-related variance above the PicoScope Nyquist limit: 0.00316%

## PicoScope usability derived from the Tektronix reference

- Paired validation: Tek 5 MS/s vs. Pico 5 MS/s
- Shared Nyquist limit: 2.5 MHz
- Tek-reference variance retained below the PicoScope Nyquist limit: 99.99684%
- Integrated paired PSD ratio (Pico/Tek): -1.561 dB
- Highest predefined band satisfying the configured coherence and PSD-ratio criteria: 1 kHz
- The reported band edge is a validation summary, not an analogue -3 dB bandwidth estimate.

## Interpretation

Low-current segments remain in the analysis and are reported separately because a small absolute gain/offset mismatch can produce a large relative percentage error. The global affine fits are diagnostic only and are not applied as a calibration correction.

The same current-dependent voltage model is applied to both current traces. The comparison therefore validates current-path agreement and consistent estimated-energy reconstruction; it does not independently validate the voltage model.

A large raw percentage difference can be caused by a stable idle/DC baseline mismatch when the workload duty cycle is low. The external-idle and incremental-energy fields diagnose this condition.

A stable additive Tektronix zero error was detected and corrected by +111.917 mA. Raw values remain archived. Because the paired PicoScope idle path supplied the reference, the selected corrected comparison is a post-hoc salvage result rather than an independent absolute validation of the PicoScope. No gain correction is applied.
