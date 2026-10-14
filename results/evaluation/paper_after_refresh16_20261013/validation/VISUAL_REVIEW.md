# Visual review of generated figures

Reviewed the 21 generated PNG figure families using contact sheets, with enlarged checks of both Full figures, all three Native/Generic views, the optimum overview, the quality overview, and representative MobileNet/YOLO26s trade-off and absolute-quality figures. PDF and SVG use the same Matplotlib Figure objects.

The reviewed selection contains 42 Full throughput and 42 Full energy observations, 204 Native/Generic pairs, all 450 joint performance–energy observations, 42 model/setup/runner optimum groups, and 450 numerical quality observations. These counts come from the figure-data manifest, not preset plotting limits.

Full plots identify host-specific TRT and accelerator Full separately. Energy axes use mJ/image; Native/Generic ratios use matching J/image quantities. Top-1 and COCO mAP are separated, and absolute-quality model panels share a common y scale. Hailo Full losses and split improvements remain visible. Detector trade-off panels explicitly show the Native oracle outside timing, Generic `decoded_nms`, and the recorded dense/sparse host tail or BN6 normalization of each Full alternative. No common-endpoint Pareto front is drawn.

The review corrected overlapping Full whisker/value labels, crowded optimum labels, an ECDF legend covering the lower energy tail, and inconsistent optimum setup ordering. Titles, axes, legends, and color bars were within the visible frame in the reviewed previews. All per-model previews received contact-sheet inspection; enlarged checks were representative rather than a separate print-layout review of every PDF.
