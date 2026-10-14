# Findings from the broad Refresh16 selection

This report is generated from the same selected rows as Tables 2/3 and all figures. 450 identities provide 450 FPS and 450 energy observations, including all 42 Full deployments. Numeric dataset quality covers 450 identities. No measurement or quality evaluation was started by this analysis.

Native exceeds Generic throughput in 139/204 paired points and uses less raw energy in 160/204; 138/204 improve both. The point-pooled median Native/Generic ratios are 1.3637 for throughput and 0.7552 for energy. Separate equal-model results in `tables/equal_model_summary.json` avoid weighting models by their number of cuts.

Against the fastest Full on the same host, 94/204 Native splits are faster. Against the separately selected minimum-energy Full, 82/204 use less energy. The largest observed speedup is 4.329x for regnet_x_1_6gf H10/b123; its energy gain against that exact same Full is 4.692. Table 3 reports the Top-2 for every model, selected from unrounded FPS ratios without energy filtering. These are retrospective results.

The fastest and minimum-energy Native split differ in 6/21 groups with more than one candidate. Shared optima and the candidate counts are shown explicitly. A small ratio above one is described as a small observed advantage; the analysis does not infer statistical significance from it.

Quality is a separate result axis. The original 26 Native and 17 Generic accuracy-loss flags remain visible. Vendor Full quality, model reference quality and every available split score appear in the quality figures. 53 cached Current losses differ from the numerical selected quality reports; both are retained. The Full and split figures display actual deployments with their quality and timed-work differences, including the YOLO26s fast-oracle versus host-tail distinction described in `METHODS.md`.

See [Table 2](tables/table2_full.md), [Table 3](tables/table3_top2_native.md), [methods](METHODS.md), [claim evidence](CLAIM_EVIDENCE.md), [figure captions](CAPTIONS.md), and [all machine-readable findings](summary.json). Missing values, if any, are enumerated by UID in `summary.json`. Historical source-version and clock-profile limitations remain; these do not trigger a new measurement campaign.
