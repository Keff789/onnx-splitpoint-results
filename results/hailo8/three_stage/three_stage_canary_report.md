# YOLOv7 Native Three-Stage Canary

- Status: **PASS_THREE_STAGE_TARGET_MET**
- Topology: **P1 → P2 → Postprocessing**
- Quality oracle: **outside all performance timing windows**
- Raw endpoint median: **95.902 FPS**
- Device-completed detection median: **95.889 FPS**
- Completed/raw ratio: **0.9999**
- Postprocessing P95 guard: **3.327 ms**
- Postflight oracle parity: **32/32 exact**

| Rep | P1 mean ms | P2 mean ms | Post mean ms | Post P95 ms | Raw FPS observed | Raw FPS stage-theoretical | Completed FPS | Ratio | 32-image result parity |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 10.378 | 8.760 | 2.098 | 3.253 | 96.207 | 96.359 | 96.194 | 0.9999 | 32/32 |
| 2 | 10.411 | 8.753 | 2.097 | 3.320 | 95.902 | 96.049 | 95.889 | 0.9999 | 32/32 |
| 3 | 10.412 | 8.746 | 2.120 | 3.327 | 95.896 | 96.041 | 95.885 | 0.9999 | 32/32 |

The performance callback performs no SHA-256 hashing, JSON evidence generation or slow-oracle execution.
A separate 32-image postflight replays the same runtime artifacts and requires exact raw-head hashes, exact current-oracle parity and equality to the prior validated oracle results.
No HEF or TensorRT engine is built, no B500 or energy run is executed, and the installed tool is not modified.
