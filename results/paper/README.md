# Paper comparison evidence

The collection script copies compact reports and top-level run contracts from
the two existing Hailo-8 B500 paper-comparison runs:

- YOLOv7 paper, split `b066`;
- ResNet-50 full/native comparison.

Large model, dataset, cache and binary artefacts are not copied into Git. Full
run directories can be copied to the separate raw archive with the explicit
`--full-local-archive` option after checking their size.

