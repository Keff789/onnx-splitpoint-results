# Offline energy windows — evidence update, 30 September 2026

This is a compact evidence freeze for the completed offline reanalysis and focused follow-up. It supplements, and does not modify, the [29 September window/pause evidence](../2026-09-29-jetson-window-pause/README.md).

- [Implemented v0.2.0 window method](WINDOW_METHOD.md)
- [v0.3.0 result and cross-device comparison policy](PLOT_POLICY.md)
- [Checked counts and limitations](EVIDENCE.json)
- [Example duration and sweep tables](data/)
- [Original artifact identities](sources.json)

The large original data acquisition is NOT repeated. The data-integrating batch is complete. A result-only postpass reuses its integrals, inherits parent-window quality flags, keeps sensitive cases visible and imports eight narrowly checked terminal-row prefix derivations.

The operator clarified that acquisition was started manually/by the benchmarking tool before the benchmark and stopped roughly ten seconds afterwards. This is an approximate procedural statement, not an exact per-file offset or synchronized timestamp. The offline window detector did not control acquisition.

Private full reviews, raw arrays, operational paths, credentials and the complete project knowledgebase remain outside public Git. Checksums identify originals; they do not replace backups. This freeze does not claim an absolute calibration, a universal rate correction, a precise throttling mechanism or synchronized instrument accuracy.

Run `python3 verify.py` here to check file integrity and evidence-table structure. It does not re-integrate the raw data.

The two CSV tables are selected checked v0.2.0 full-review summaries, not a blanket release of all v0.3.0 main-curve candidates. The source reports and new quality/cohort policy remain authoritative.
