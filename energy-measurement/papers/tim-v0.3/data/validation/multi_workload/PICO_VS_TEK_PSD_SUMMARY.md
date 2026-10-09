# PicoScope versus Tektronix spectral comparison

Both sources are native-rate PSDs of the same physical paired recordings. No target-rate low-pass or Common-Reference cache is used.

Nominal analogue marker: 77 kHz. Digital Nyquist limit: 2.5 MHz. Neither is a claim of independent usable bandwidth.

| Workload | Current CDF maximum difference | Conditional low-band difference | Pico/Tek current variance |
|---|---:|---:|---:|
| GEMM-FP32 | 12.179 pp | 0.869 pp | -0.669 dB |
| GEMM-INT8 | 30.637 pp | 2.993 pp | -2.344 dB |
| YOLO-FP32 | 21.641 pp | 2.540 pp | -1.564 dB |
| YOLO-INT8 | 19.868 pp | 2.424 pp | -1.459 dB |
| Gemma3-4B | 16.069 pp | 0.349 pp | -0.872 dB |
| ResNet-50 FP32 | 19.106 pp | 1.776 pp | -1.248 dB |

## Interpretation limits

A full-band CDF normalises every setup separately. Suppressed high-frequency variance can change its low-frequency percentages even when low-band shapes agree. The conditional comparison separates this denominator effect.

The 77-kHz marker does not truncate spectra. Content above it is retained; attenuation is not identical to absence of information. No deconvolution, transfer function, or synthetic coherence is inferred.

Active-minus-idle is a descriptive clipped spectral difference from independent records, not a causal source separation. Current and estimated-power PSDs are separate quantities.

No legacy PARMA figure, table, calibration, offset model, sampling result, or manuscript was changed.
