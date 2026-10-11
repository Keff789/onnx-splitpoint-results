# Native/Generic fairness — Revision 3 Current snapshot

This snapshot reports the actual selected Current rows at **2026-10-11T05:37:24.626853+00:00**.
Execution state: `continuous_revision3_in_progress_transport_diagnosis_and_offline_completion`. Counts below are derived from those rows;
the finalized Quality pointer describes its own normal report generation separately.
Missing values remain null/NA. This page does not declare the campaign complete.

| Current axis | Native | Generic |
|---|---:|---:|
| Newly measured Native / completed Generic performance | 240 | 204 |
| Verified original single-observation performance reuse | 6 | — |
| Performance not measured/completed | 0 | 0 |
| Normally bound dataset Quality | 244 | 204 |
| Normal comparative performance claims | 235 | 204 |
| Normally admitted current energy | 143 | 9 |

Generic points still requiring final-bundle confirmation according to Resume:
0.
Completed historical cohorts remain visible; this count is not inferred from a free lease.

Start with [the result report](RESULT_REPORT.md), [fairness matrix](FAIRNESS_MATRIX.csv),
[Native Current](current_results/native_current.json), [Generic Current](current_results/generic_current.json),
[finalized Quality pointer](quality_transfer/CURRENT_FINALIZED.json),
[review holds](current_results/QUALITY_JOIN_REVIEW_HOLDS.json),
[audit dispositions](AUDIT_FINDING_DISPOSITION.csv) and [Resume state](RESUME_STATE.json).
[PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) records the exported checkpoint and source bindings.

Runtime freeze: `8346d43d526221bd9d138943122206b658d56cbf` (241 files).
The canonical CPU-reference Controller correction is `ec68097d0ca161a75380da158a257ad495296d90`.
Controller reporting is `5e742b34862a7d0e0760474a1ff3e4826854f20e`; the retained-origin reader
guard is `6ca5b3cedf3fda0f69397ad0e7a3e7abbe0194ae`. The bound cohort reader is
`b7c2094e329351dcbdbeef4d3fcac48eec9458f3`. These local reporting amendments are bound by the existing
[reporting source supplement](REPORTING_SOURCE_SUPPLEMENT.json); deployed runtime bytes remain
at the original freeze.
Current normal Quality generation: `revision3:/quality_transfer/final_native_187_20261011/finalized_187_normal_full_context`. Its composition and
independent-review references follow the current pointer; no historical generation count is substituted.
Complete Quality summaries, N5000/CPU evidence, model binaries and original raw captures remain private.

H8 classification was corrected against the actual HEF/SDK domain. Corrected Vendor/TRT Full
Quality bindings and same-setup comparisons use the normal consumer; `accuracy_loss` remains visible.
Original Vendor-DX/H10 dataset Quality reuse retains one performance observation, no new repeats/CI
and no new performance claim. The conflicted H10 historical physical Full context stays excluded.

The [DX56 input-source finding](quality_transfer/classifier_split_preparation_20261008/DX56_N5000_INPUT_SOURCE_REVIEW.json)
records the original inverse-ImageNet-to-UINT8 truncation versus the final direct-RGB path.
The preliminary roundtrip transfer remains invalid and its original hold is retained as historical
negative evidence. All 56 cases now have separately completed N5000 Quality with the matching direct-RGB
input and canonical CPU references. Current uses their normally verified additive joins and exact
performance cohorts; it does not reinterpret the old mismatching input as equivalent. The retained
hold file describes those original exclusions; each applicable Current row binds its verified later
resolution in quality_provenance.postmeasurement_dataset_quality_join_evidence.

| Normally admitted current energy row | Completed tasks/s, integer display | Raw system mJ/task | Tasks/J |
|---|---:|---:|---:|
| Native mobilenet_v3_large/DeepX/deepx_to_trt/b001 | 440 | 45.314575 | 22.070568588 |
| Native mobilenet_v3_large/DeepX/deepx_to_trt/b010 | 657 | 31.300637 | 31.948319460 |
| Native mobilenet_v3_large/DeepX/deepx_to_trt/b019 | 648 | 30.553837 | 32.729285537 |
| Native mobilenet_v3_large/DeepX/deepx_to_trt/b027 | 770 | 27.032971 | 36.992453163 |
| Native mobilenet_v3_large/DeepX/deepx_to_trt/b039 | 720 | 26.871707 | 37.214105366 |
| Native mobilenet_v3_large/DeepX/deepx_to_trt/b056 | 769 | 25.638459 | 39.004949731 |
| Native mobilenet_v3_large/DeepX/deepx_to_trt/b062 | 755 | 25.709275 | 38.896663295 |
| Native mobilenet_v3_large/DeepX/deepx_to_trt/b068 | 755 | 26.105054 | 38.307110957 |
| Native mobilenet_v3_large/DeepX/deepx_to_trt/b074 | 741 | 26.352370 | 37.947838398 |
| Native mobilenet_v3_large/DeepX/deepx_to_trt/b078 | 532 | 35.073633 | 28.513191059 |
| Native yolo11l/DeepX/deepx_to_trt/b003 | 37 | 700.079386 | 1.428417684 |
| Native yolo11l/DeepX/deepx_to_trt/b062 | 49 | 546.004889 | 1.831493419 |
| Native yolov7_paper/DeepX/deepx_to_trt/b009 | 34 | 715.748830 | 1.397140910 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b001 | 727 | 32.455070 | 30.812341888 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b010 | 786 | 29.364056 | 34.055443818 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b019 | 834 | 27.204462 | 36.758983420 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b027 | 849 | 26.245971 | 38.101220224 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b039 | 931 | 24.802824 | 40.318782007 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b056 | 1028 | 21.994619 | 45.465820821 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b062 | 1061 | 21.297827 | 46.953268731 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b068 | 1065 | 20.747943 | 48.197880868 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b074 | 1143 | 19.936170 | 50.162194741 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b078 | 1172 | 20.087543 | 49.782304073 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b085 | 1140 | 18.357030 | 54.475105228 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b097 | 761 | 26.037680 | 38.406950401 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b100 | 471 | 38.300963 | 26.109005516 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b108 | 402 | 43.512959 | 22.981711470 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b120 | 360 | 47.384215 | 21.104090423 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b132 | 320 | 52.679631 | 18.983282063 |
| Native mobilenet_v3_large/H10/hailo10h_to_trt/b135 | 312 | 53.493035 | 18.694303983 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b001 | 307 | 82.600888 | 12.107084178 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b008 | 319 | 78.165380 | 12.793523689 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b015 | 333 | 75.322273 | 13.276316432 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b023 | 326 | 75.258153 | 13.287620346 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b030 | 368 | 69.201605 | 14.450558434 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b037 | 384 | 66.999870 | 14.925414751 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b044 | 403 | 64.003620 | 15.624374005 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b052 | 437 | 58.064360 | 17.222316666 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b059 | 476 | 54.190914 | 18.453297639 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b066 | 507 | 50.251325 | 19.900024945 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b073 | 549 | 46.355623 | 21.572361133 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b080 | 580 | 42.385300 | 23.593119247 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b087 | 620 | 39.632045 | 25.232271034 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b088 | 612 | 40.039962 | 24.975064083 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b095 | 728 | 34.415290 | 29.056895520 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b102 | 785 | 30.422292 | 32.870689500 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b109 | 953 | 25.606019 | 39.053423672 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b115 | 1081 | 21.860304 | 45.745241476 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b123 | 1367 | 15.825867 | 63.188169985 |
| Native regnet_x_1_6gf/H10/hailo10h_to_trt/b132 | 1175 | 16.949287 | 59.000927606 |
| Native resnet50/H10/hailo10h_to_trt/b002 | 501 | 58.922669 | 16.971556463 |
| Native resnet50/H10/hailo10h_to_trt/b009 | 292 | 84.031077 | 11.900387776 |
| Native resnet50/H10/hailo10h_to_trt/b016 | 292 | 83.353514 | 11.997444479 |
| Native resnet50/H10/hailo10h_to_trt/b023 | 291 | 82.531325 | 12.116731755 |
| Native resnet50/H10/hailo10h_to_trt/b031 | 565 | 51.867774 | 19.279909937 |
| Native resnet50/H10/hailo10h_to_trt/b038 | 572 | 51.167090 | 19.544106544 |
| Native resnet50/H10/hailo10h_to_trt/b045 | 563 | 49.987210 | 20.005461525 |
| Native resnet50/H10/hailo10h_to_trt/b052 | 575 | 49.701732 | 20.120280079 |
| Native resnet50/H10/hailo10h_to_trt/b060 | 824 | 37.711591 | 26.517126714 |
| Native resnet50/H10/hailo10h_to_trt/b067 | 870 | 36.231759 | 27.600113278 |
| Native resnet50/H10/hailo10h_to_trt/b068 | 865 | 36.293108 | 27.553500197 |
| Native resnet50/H10/hailo10h_to_trt/b074 | 945 | 34.289235 | 29.164207029 |
| Native resnet50/H10/hailo10h_to_trt/b081 | 975 | 32.628775 | 30.647959968 |
| Native resnet50/H10/hailo10h_to_trt/b088 | 1060 | 30.573245 | 32.708481053 |
| Native resnet50/H10/hailo10h_to_trt/b095 | 1100 | 29.458791 | 33.945765850 |
| Native resnet50/H10/hailo10h_to_trt/b103 | 337 | 58.683364 | 17.041021980 |
| Native resnet50/H10/hailo10h_to_trt/b104 | 337 | 58.689174 | 17.038925188 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b001 | 820 | 29.640241 | 33.738176055 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b010 | 969 | 24.525612 | 40.773750457 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b019 | 947 | 24.131435 | 41.439760718 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b027 | 993 | 23.011387 | 43.457572698 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b039 | 775 | 26.757625 | 37.372545974 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b056 | 594 | 31.819006 | 31.427767326 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b062 | 585 | 31.857560 | 31.389744962 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b068 | 564 | 32.602272 | 30.672732268 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b074 | 552 | 33.165095 | 30.152192359 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b078 | 505 | 36.170516 | 27.646936029 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b085 | 448 | 38.891730 | 25.712414439 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b097 | 331 | 50.187444 | 19.925490639 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b100 | 305 | 53.731205 | 18.611162107 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b108 | 247 | 64.635662 | 15.471344608 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b120 | 172 | 90.491350 | 11.050806644 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b132 | 135 | 113.659188 | 8.798242257 |
| Native mobilenet_v3_large/H8/hailo8_to_trt/b135 | 125 | 122.039368 | 8.194078902 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b001 | 312 | 81.264825 | 12.305501317 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b008 | 340 | 73.932409 | 13.525875457 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b015 | 351 | 71.707258 | 13.945591448 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b023 | 383 | 66.422821 | 15.055318810 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b030 | 401 | 64.004186 | 15.624013019 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b037 | 420 | 61.428732 | 16.279068904 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b044 | 446 | 58.911204 | 16.974723408 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b052 | 500 | 52.442882 | 19.068369294 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b059 | 508 | 50.277730 | 19.889550512 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b066 | 584 | 44.599358 | 22.421914039 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b073 | 618 | 41.734257 | 23.961145052 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b080 | 548 | 43.147905 | 23.176161127 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b087 | 490 | 44.800615 | 22.321259561 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b088 | 485 | 44.738363 | 22.352344965 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b095 | 467 | 44.282629 | 22.582226700 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b102 | 442 | 44.439858 | 22.502349070 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b109 | 402 | 46.181553 | 21.653681795 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b115 | 386 | 46.077926 | 21.702401852 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b123 | 366 | 45.787713 | 21.839931285 |
| Native regnet_x_1_6gf/H8/hailo8_to_trt/b132 | 354 | 44.829971 | 22.306523291 |
| Native resnet50/H8/hailo8_to_trt/b002 | 554 | 55.961148 | 17.869599389 |
| Native resnet50/H8/hailo8_to_trt/b009 | 395 | 71.438108 | 13.998154507 |
| Native resnet50/H8/hailo8_to_trt/b016 | 386 | 71.453673 | 13.995111140 |
| Native resnet50/H8/hailo8_to_trt/b023 | 390 | 70.050279 | 14.275487524 |
| Native resnet50/H8/hailo8_to_trt/b031 | 581 | 50.293230 | 19.883453782 |
| Native resnet50/H8/hailo8_to_trt/b038 | 581 | 49.915384 | 20.033912069 |
| Native resnet50/H8/hailo8_to_trt/b045 | 529 | 51.508149 | 19.414599490 |
| Native resnet50/H8/hailo8_to_trt/b052 | 517 | 51.246894 | 19.513383760 |
| Native resnet50/H8/hailo8_to_trt/b060 | 570 | 45.172270 | 22.137476843 |
| Native resnet50/H8/hailo8_to_trt/b067 | 464 | 50.571145 | 19.774287745 |
| Native resnet50/H8/hailo8_to_trt/b068 | 464 | 50.266748 | 19.893870715 |
| Native resnet50/H8/hailo8_to_trt/b074 | 437 | 51.373430 | 19.465333394 |
| Native resnet50/H8/hailo8_to_trt/b081 | 395 | 53.920110 | 18.545966644 |
| Native resnet50/H8/hailo8_to_trt/b088 | 369 | 55.577790 | 17.992804265 |
| Native resnet50/H8/hailo8_to_trt/b095 | 338 | 58.352250 | 17.137332654 |
| Native resnet50/H8/hailo8_to_trt/b103 | 317 | 56.991417 | 17.546509526 |
| Native resnet50/H8/hailo8_to_trt/b104 | 318 | 56.895978 | 17.575994118 |
| Native resnet50/H8/hailo8_to_trt/b110 | 279 | 61.564386 | 16.243181264 |
| Native resnet50/H8/hailo8_to_trt/b119 | 143 | 116.070849 | 8.615428291 |
| Native yolo11l/H8/hailo8_to_trt/b003 | 39 | 668.805466 | 1.495206502 |
| Native yolo11l/H8/hailo8_to_trt/b062 | 43 | 574.553315 | 1.740487201 |
| Native yolo11l/DeepX/native_full_deepx/full | 21 | 756.063477 | 1.322649275 |
| Native yolov7_paper/DeepX/native_full_deepx/full | 23 | 689.874383 | 1.449540153 |
| Native mobilenet_v3_large/H8/native_full_hailo8/full | 118 | 126.753612 | 7.889332464 |
| Native regnet_x_1_6gf/H8/native_full_hailo8/full | 362 | 43.241850 | 23.125856666 |
| Native resnet50/H8/native_full_hailo8/full | 122 | 132.445698 | 7.550265190 |
| Native yolov7_paper/H8/native_full_hailo8/full | 32 | 549.843563 | 1.818699641 |
| Native mobilenet_v3_large/H8/native_full_tensorrt/full | 749 | 29.160781 | 34.294201045 |
| Native mobilenet_v3_large/H10/native_full_tensorrt/full | 710 | 27.627434 | 36.196050512 |
| Native regnet_x_1_6gf/H8/native_full_tensorrt/full | 314 | 77.224978 | 12.949193411 |
| Native regnet_x_1_6gf/H10/native_full_tensorrt/full | 316 | 74.249821 | 13.468086764 |
| Native resnet50/H8/native_full_tensorrt/full | 523 | 56.897414 | 17.575893462 |
| Native yolo11l/H8/native_full_tensorrt/full | 39 | 680.325600 | 1.469885549 |
| Native yolo11l/DeepX/native_full_tensorrt/full | 38 | 675.467247 | 1.480459144 |
| Native yolov7_paper/DeepX/native_full_tensorrt/full | 48 | 613.181286 | 1.630862555 |
| Native yolo11l/DeepX/deepx_to_trt/b120 | 33 | 705.628586 | 1.417383504 |
| Native yolov7_paper/DeepX/deepx_to_trt/b044 | 49 | 532.093280 | 1.879388384 |
| Native yolov7_paper/DeepX/deepx_to_trt/b066 | 31 | 712.277595 | 1.403947547 |
| Native yolo11l/H8/hailo8_to_trt/b120 | 44 | 555.167796 | 1.801258554 |
| Generic yolov7_paper/orin_nx_deepx_m1_01/deepx_to_trt/b009 | 37 | 722.850333 | 1.383472864 |
| Generic yolov7_paper/orin_nx_hailo10_01/hailo10h_to_trt/b009 | 29 | 843.153657 | 1.186033323 |
| Generic yolov7_paper/orin_nx_hailo8_01/hailo8_to_trt/b009 | 41 | 659.949179 | 1.515270832 |
| Generic yolov7_paper/orin_nx_deepx_m1_01/deepx_to_trt/b044 | 50 | 549.507174 | 1.819814862 |
| Generic yolov7_paper/orin_nx_hailo10_01/hailo10h_to_trt/b044 | 47 | 582.185876 | 1.717699817 |
| Generic yolov7_paper/orin_nx_hailo8_01/hailo8_to_trt/b044 | 45 | 576.904083 | 1.733390579 |
| Generic yolov7_paper/orin_nx_deepx_m1_01/deepx_to_trt/b066 | 32 | 734.054394 | 1.362370258 |
| Generic yolov7_paper/orin_nx_hailo10_01/hailo10h_to_trt/b066 | 28 | 809.995278 | 1.234581873 |
| Generic yolov7_paper/orin_nx_hailo8_01/hailo8_to_trt/b066 | 47 | 548.070886 | 1.824583230 |

Energy uses actual completed counts and three accepted captures. Presentation multiplies the stored
J/task by 1000 only; raw values remain unchanged. Mean N/E is separate from inverse mean E/N, and
existing comparison normalization remains in separate Current fields. Final tables keep unadmitted rows NA; separately labeled diagnostic observations retain their original numeric values.

The continuous Revision-3 authorization replaces historical administrative one-grant and retry caps;
original attempts and counters remain retained. Scientific gates, source closure and resource exclusion
still apply. The latest H8/H10 incomplete-stream failures and repeated DeepX packet loss require transport
diagnosis before further affected captures. The current [Resume](RESUME_STATE.json) records exact
operations, retained partial repeats and missing technical access. No hardware defect or repaired
transport is inferred from idle processes. Diagnostic numeric observations remain explicitly excluded
from final energy claims and from the admitted energy table above.

The historical Generic streaming, multi-tensor, Raw, `native_fifo` and `NativeTRTSession` paths remain.
Only proven dead isolated duplicates were removed. Actual independent process cohorts, completion
counts, exact inputs, normal Quality, comparative claims and energy are separate evidence axes.
One thousand repetitions of one prepared input are not one thousand dataset images or independent sessions.

Run the standalone public hash and arithmetic check from any directory:

```sh
python3 verify_snapshot.py
```

The checker verifies supplied projections and repeat arithmetic; it does not replay raw sensors,
model inference or normal private consumer execution. Private paths/network labels are sanitized.
The private manuscript and all LaTeX remain outside this Git payload. Final rankings and private-paper
status are stated only by the current result/Resume checkpoint.
