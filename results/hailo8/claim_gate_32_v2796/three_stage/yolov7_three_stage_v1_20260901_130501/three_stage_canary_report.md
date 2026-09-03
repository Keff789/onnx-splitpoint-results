# YOLOv7 Native Three-Stage Canary

- Status: **PASS_THREE_STAGE_TARGET_MET**
- Topology: **P1 → P2 → Postprocessing**
- Quality oracle: **outside all performance timing windows**
- Raw endpoint median: **100.004 FPS**
- Device-completed detection median: **99.992 FPS**
- Completed/raw ratio: **0.9999**
- Postprocessing P95 guard: **3.011 ms**
- Postflight oracle parity: **32/32 exact**

| Rep | P1 mean ms | P2 mean ms | Post mean ms | Post P95 ms | Raw FPS observed | Raw FPS stage-theoretical | Completed FPS | Ratio | corpus result parity |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 9.983 | 8.766 | 1.905 | 2.960 | 100.004 | 100.166 | 99.992 | 0.9999 | 32/32 |
| 2 | 9.988 | 8.791 | 1.956 | 3.001 | 99.954 | 100.118 | 99.941 | 0.9999 | 32/32 |
| 3 | 9.976 | 8.757 | 1.955 | 3.011 | 100.083 | 100.244 | 100.071 | 0.9999 | 32/32 |

The performance callback performs no SHA-256 hashing, JSON evidence generation or slow-oracle execution.
A separate postflight over the configured sentinel corpus replays the same runtime artifacts and requires exact raw-head hashes, exact current-oracle parity and equality to the prior validated oracle results.
No HEF or TensorRT engine is built, no B500 or energy run is executed, and the installed tool is not modified.
