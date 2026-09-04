# YOLOv7 Native Three-Stage Canary

- Status: **PASS_THREE_STAGE_TARGET_MET**
- Topology: **P1 → P2 → Postprocessing**
- Quality oracle: **outside all performance timing windows**
- Raw endpoint median: **97.018 FPS**
- Device-completed detection median: **97.000 FPS**
- Completed/raw ratio: **0.9998**
- Postprocessing P95 guard: **2.111 ms**
- Postflight oracle parity: **1/1 exact**

| Rep | P1 mean ms | P2 mean ms | Post mean ms | Post P95 ms | Raw FPS observed | Raw FPS stage-theoretical | Completed FPS | Ratio | corpus result parity |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 10.291 | 8.771 | 2.049 | 2.111 | 97.018 | 97.173 | 97.000 | 0.9998 | 1/1 |
| 2 | 10.290 | 8.746 | 1.982 | 2.032 | 97.026 | 97.184 | 97.008 | 0.9998 | 1/1 |
| 3 | 10.306 | 8.769 | 1.979 | 2.033 | 96.874 | 97.029 | 96.856 | 0.9998 | 1/1 |

The performance callback performs no SHA-256 hashing, JSON evidence generation or slow-oracle execution.
A separate postflight over the configured sentinel corpus replays the same runtime artifacts and requires exact raw-head hashes, exact current-oracle parity and equality to the prior validated oracle results.
No HEF or TensorRT engine is built, no B500 or energy run is executed, and the installed tool is not modified.
