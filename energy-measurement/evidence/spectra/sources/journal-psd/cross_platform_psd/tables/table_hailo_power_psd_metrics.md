Native power-spectrum percentiles; per-run medians, not percentiles of the aggregate curve. Active-only and idle-subtracted results remain separate.

| Workload | Basis | Window | Runs | f50 median (Hz) | f95 median (Hz) | f99 median (Hz) |
| --- | --- | --- | --- | --- | --- | --- |
| Hailo-10 / gemm | active | full_record | 15 | 393.948 | 1171.236 | 67534.256 |
| Hailo-10 / gemm | idle | full_record | 15 | 116533.847 | 177981.682 | 247081.352 |
| Hailo-10 / gemm | excess | full_record | 15 | 393.921 | 1170.858 | 26411.383 |
| Hailo-10 / gemm | active | matched_prefix | 15 | 393.938 | 1171.256 | 73036.786 |
| Hailo-10 / gemm | idle | matched_prefix | 15 | 116533.847 | 177981.682 | 247081.352 |
| Hailo-10 / gemm | excess | matched_prefix | 15 | 393.907 | 1170.818 | 26761.055 |
| Hailo-10 / yolo | active | full_record | 15 | 849.503 | 3843.466 | 104555.616 |
| Hailo-10 / yolo | idle | full_record | 15 | 117904.481 | 179522.582 | 248582.695 |
| Hailo-10 / yolo | excess | full_record | 15 | 842.742 | 3111.927 | 94047.800 |
| Hailo-10 / yolo | active | matched_prefix | 15 | 849.934 | 3956.608 | 105069.309 |
| Hailo-10 / yolo | idle | matched_prefix | 15 | 117904.481 | 179522.582 | 248582.695 |
| Hailo-10 / yolo | excess | matched_prefix | 15 | 834.327 | 3113.816 | 95482.636 |
