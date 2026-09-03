# YOLOv7 Multi-Image Fast-Decode Parity Canary

- Status: **PASS_MULTI_IMAGE_EXACT_TARGET_MET**
- Images: **32/32 exact**
- Fast median across image medians: **1.2967 ms**
- Fast P95 across image medians: **2.4857 ms**
- Fast worst image median: **4.8987 ms**
- Median speedup: **25.90×**

| Image | Bin | GT objects | Obj survivors | Score survivors | Detections | Oracle ms | Fast ms | Speedup | Exact |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 632 | `forced_anchor` | 17 | 56 | 56 | 9 | 36.4795 | 1.6381 | 22.27× | yes |
| 550939 | `sparse_0_2` | 0 | 10 | 10 | 1 | 36.1685 | 0.9783 | 36.97× | yes |
| 87742 | `sparse_0_2` | 1 | 28 | 27 | 3 | 37.0807 | 1.1487 | 32.28× | yes |
| 286507 | `sparse_0_2` | 1 | 10 | 10 | 1 | 32.2463 | 0.8129 | 39.67× | yes |
| 206025 | `sparse_0_2` | 2 | 17 | 17 | 2 | 37.1409 | 1.0649 | 34.88× | yes |
| 297830 | `sparse_0_2` | 2 | 16 | 16 | 2 | 32.5785 | 1.0647 | 30.60× | yes |
| 251119 | `sparse_0_2` | 2 | 27 | 23 | 3 | 36.5664 | 1.1319 | 32.31× | yes |
| 79031 | `sparse_0_2` | 2 | 15 | 15 | 2 | 32.4400 | 0.8951 | 36.24× | yes |
| 161044 | `sparse_0_2` | 2 | 19 | 19 | 2 | 36.3339 | 1.0541 | 34.47× | yes |
| 42102 | `light_3_5` | 3 | 27 | 27 | 3 | 32.5924 | 1.1349 | 28.72× | yes |
| 210030 | `light_3_5` | 3 | 28 | 27 | 3 | 36.4593 | 1.1305 | 32.25× | yes |
| 249643 | `light_3_5` | 3 | 31 | 31 | 3 | 32.5815 | 1.2928 | 25.20× | yes |
| 268000 | `light_3_5` | 3 | 26 | 20 | 3 | 36.5800 | 1.2936 | 28.28× | yes |
| 412531 | `light_3_5` | 4 | 39 | 37 | 4 | 32.7618 | 1.3452 | 24.35× | yes |
| 307598 | `light_3_5` | 4 | 9 | 9 | 1 | 36.1742 | 0.8157 | 44.35× | yes |
| 408696 | `light_3_5` | 5 | 39 | 39 | 5 | 32.8128 | 1.2553 | 26.14× | yes |
| 485480 | `light_3_5` | 5 | 43 | 40 | 6 | 36.5142 | 1.4225 | 25.67× | yes |
| 31817 | `medium_6_10` | 6 | 55 | 54 | 6 | 32.8004 | 1.2999 | 25.23× | yes |
| 146489 | `medium_6_10` | 6 | 46 | 44 | 5 | 36.6183 | 1.2788 | 28.63× | yes |
| 460347 | `medium_6_10` | 7 | 65 | 63 | 8 | 32.8244 | 1.6079 | 20.41× | yes |
| 189078 | `medium_6_10` | 7 | 64 | 64 | 7 | 36.4572 | 1.3824 | 26.37× | yes |
| 411754 | `medium_6_10` | 8 | 58 | 58 | 7 | 32.9549 | 1.5187 | 21.70× | yes |
| 27768 | `medium_6_10` | 9 | 56 | 54 | 7 | 36.5798 | 1.5016 | 24.36× | yes |
| 482436 | `medium_6_10` | 9 | 55 | 49 | 10 | 33.0818 | 1.6766 | 19.73× | yes |
| 146825 | `medium_6_10` | 10 | 46 | 45 | 8 | 36.6432 | 1.5658 | 23.40× | yes |
| 110999 | `dense_11_plus` | 11 | 109 | 107 | 13 | 33.4767 | 1.9717 | 16.98× | yes |
| 70774 | `dense_11_plus` | 12 | 26 | 25 | 4 | 36.4076 | 1.1565 | 31.48× | yes |
| 154004 | `dense_11_plus` | 14 | 131 | 131 | 16 | 33.4555 | 2.0238 | 16.53× | yes |
| 214539 | `dense_11_plus` | 16 | 118 | 118 | 18 | 37.0545 | 2.0503 | 18.07× | yes |
| 142324 | `dense_11_plus` | 19 | 175 | 165 | 24 | 33.8202 | 2.4222 | 13.96× | yes |
| 146667 | `dense_11_plus` | 24 | 178 | 174 | 25 | 37.7896 | 2.5633 | 14.74× | yes |
| 435081 | `dense_11_plus` | 62 | 506 | 415 | 67 | 36.2960 | 4.8987 | 7.41× | yes |

The C++ raw-head collection is used only to generate diverse current payloads; its one-frame process startup timings are not interpreted as performance.
No HEF/engine build, B500, energy measurement or installed-tool mutation was performed.
