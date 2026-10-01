# Controlled 2 kS/s / 5 MS/s diagnostic — 1 October 2026

Compact public evidence for the completed GEMM FP16 control test and the historical baseline decomposition. This directory does not contain raw Parquet channels, private operational paths or credentials.

## Controlled protocol

- six scored runs: 2 kS/s, 5 MS/s, 5 MS/s, 2 kS/s, 2 kS/s, 5 MS/s;
- 250 completed TensorRT queries per run;
- one unscored conditioner with the same work;
- measured 120 s process-end-to-next-start pause;
- three repeats per rate;
- PicoScope INA225NVGPU/NvGpu and Jetson VDD_IN observed in parallel;
- no inline analysis between captures.

All six scored captures completed. The preceding 100-query attempt was intentionally stopped before any scored capture because its 46.8272 s duration did not support the frozen 20–80 s inner-window design.

## Main observation

Arithmetic mean load power differs by +0.047794 % on Pico and +0.011272 % on VDD_IN at 5 MS/s versus 2 kS/s; TensorRT time differs by -0.021287 %. The current-signal channel nevertheless drifts upward with measurement order in pre-, load- and post-windows. The result does not support a multi-percent intrinsic high-rate deficit under this protocol, but n=3 per rate does not establish universal equivalence.

Historical direct sweeps track their pre-load levels strongly. A diagnostic `load minus pre-load` view reduces the 5-MS/s versus 2-kS/s endpoint shifts to approximately -0.57 % (GEMM FP16), -0.62 % (GEMM INT8), +0.17 % (LLM), +0.08 % (YOLO FP32), and +0.44 % (YOLO INT8). This is not an automatic calibration correction.

## Files

- `data/controlled-group-stats.csv`: mean, median and population spread for the six-run control.
- `data/historical-endpoint-decomposition.csv`: diagnostic endpoint decomposition from all 15 historical repeats per rate.
- `sources.json`: source archive identities and limits.

The separate static 37 W rate sweep changes by -0.069733 % between the 2-kS/s and 5-MS/s group medians. Raw data and the complete private review remain in laboratory storage.
