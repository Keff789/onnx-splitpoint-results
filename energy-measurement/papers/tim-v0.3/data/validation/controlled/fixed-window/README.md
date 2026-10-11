# Fixed-window audit of the historical direct sweeps

The audit uses the same 20–80 s interval for every selected trace: five workloads, three rates (2 kS/s, 250 kS/s and 5 MS/s) and 15 runs per rate, for 225 traces. All 900 fixed-window integrals were independently re-summed from the supplied energy bins. No run was removed by magnitude, spread, run ID or sensitivity.

## Main result

Median 5-MS/s versus 2-kS/s fixed-window power changes are:

| Workload | Difference |
|---|---:|
| GEMM FP16 | -2.299 % |
| GEMM INT8 | -2.567 % |
| LLM | -1.967 % |
| YOLO FP32 | -0.981 % |
| YOLO INT8 | -0.036 % |

The differences persist in the pre-declared 20–40 s, 40–60 s and 60–80 s subwindows. An exploratory 1–4 s pre-load view shows that 74–92 % of the arithmetic load-level shift for the four conspicuous workloads is already present before the detected main load. This is diagnostic decomposition, not a correction or causal attribution.

Run 0 at 5 MS/s is above all other 5-MS/s runs for GEMM FP16, GEMM INT8, LLM and YOLO FP32, but not YOLO INT8. All runs remain in the statistics.

## Scope and limits

This is a recomputation from previously integrated energy bins, not a second read of raw ADC samples and not a validation of sample continuity, hardware timebase, calibration or physical measurement boundary. The source review is identified in `../sources.json`; full private review artifacts remain in laboratory storage.
