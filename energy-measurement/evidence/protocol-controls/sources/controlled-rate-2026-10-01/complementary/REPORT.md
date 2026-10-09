# Complementary GEMM-FP16 baseline/rate diagnostic

Stand: 1 October 2026.

## Result

Both six-run sessions completed. They used the same 250-query command, engine hash, collector/power-calculation binaries, 120-s end-to-start pause and Jetson boot ID. The rate order was complementary at every sequence position:

- v1.0.1: 2 kS/s, 5 MS/s, 5 MS/s, 2 kS/s, 2 kS/s, 5 MS/s
- v1.0.2: 5 MS/s, 2 kS/s, 2 kS/s, 5 MS/s, 5 MS/s, 2 kS/s

The unadjusted *median* Pico load comparison changes sign with the sequence:

- v1.0.1: -0.508 %
- v1.0.2: +0.441 %

After balancing every sequence position and allowing a separate session offset, the estimated 5-MS/s-minus-2-kS/s effect is:

| Quantity | Balanced effect | Relative effect | Descriptive 95% interval |
|---|---:|---:|---:|
| Pico inner-load power | -0.021363 W | -0.061 % | -0.182 to +0.060 % |
| Pico pre-window power | +0.034309 W | +0.443 % | -0.442 to +1.327 % |
| Pico load minus pre | -0.055673 W | -0.204 % | -0.607 to +0.199 % |
| Jetson VDD_IN load | +0.002919 W | +0.009 % | -0.072 to +0.089 % |
| TensorRT runtime | -0.035167 s | -0.030 % | -0.172 to +0.112 % |

The interval is from an additive session-plus-position model with four residual degrees of freedom. It is a diagnostic interval, not a metrological uncertainty budget or a population-general claim.

## Main interpretation

The controlled experiment does **not** reproduce the historical multi-percent decrease as a deterministic effect of the configured PicoScope sample rate.

The external Pico pre and load levels both rise through the two sessions. Their first-to-last changes are very similar in each session, whereas `VDD_IN` and TensorRT runtime do not show a comparable drift. Removing the pre-window level substantially reduces the time/order drift; the balanced load-minus-pre estimate is about -0.204 %.

This supports the following interpretation:

1. The historical direct sweeps contain important session/order/acquisition-state components and cannot be interpreted as pure sampling-rate effects.
2. The present controlled test bounds the remaining rate-associated effect in this setup to a small sub-percent range; it does not establish absolute electrical accuracy.
3. No offset or drift correction should be silently applied to the historical data. The pre-window observation is diagnostic evidence, not an independently verified electrical zero.
4. Pico and Jetson VDD_IN have different physical boundaries and are not hardware-time-synchronized; agreement of trends is informative but not a calibration proof.

## Data handling

- All 12 measured runs are retained.
- No magnitude-based exclusions.
- No offset, gain, time or drift correction.
- Raw channels remain outside this public evidence directory.
- Both uploaded review manifests were checked file-by-file.
