# ONNX Split-Point Results Archive

This repository is the curated, Git-friendly result archive for the ONNX
Split-Point evaluation project. It keeps compact measurement results,
experiment scripts, acceptance evidence and explanatory documentation. Large
runtime artefacts stay in a separate local raw archive and are not committed.

## THESIS20 completed analysis — 4 October 2026

Start with [the paper handoff](results/evaluation/thesis20_20261004/START_HERE.md),
[reproducible tables and figures](results/evaluation/thesis20_20261004/README.md), and
[findings and limits](results/evaluation/thesis20_20261004/PAPER_FINDINGS.md).
The corrected base, 192-case Generic completion and 12-case YOLO augmentation remain
separate cohorts: 560 quality results, 246 Native cases, 204 completed Generic/Native
pairs and 246 complete energy rows. Negative scientific results are retained.

[Tool release v2.92.0](https://github.com/Keff789/ONNX-Splitpoint-Tool/releases/tag/v2.92.0),
main commit `d164aad6d7c7ef68c1b371c49a1fdea0a3b27dd7`, its annotated tag and both
source archives are published and verified against the remote. Raw archive transfer remains in progress; compact public
inputs are not a replacement for the private original payloads. No new measurements
were made for this analysis or release.

## Knowledge base

The continuously maintained [project knowledge base](docs/KNOWLEDGEBASE.md)
is the canonical entry point for methods, current scope, open items and historical
context. Its filename stays fixed; updates and older states are tracked by Git.
The dated evidence directories below remain immutable records of their own runs.

## v2.83 evidence update — 19 September 2026

Historical snapshot: see [v2.83 scope and then-open items](docs/V283_STATUS_2026-09-19.md),
[GUI and software acceptance](results/acceptance/v2.83/README.md), and
[the completed R9G one-split evaluation](results/evaluation/r9g_eval_20260918_171131/README.md).
R9H three-split acceptance is still pending final evidence. Successful acquisition is not a
blanket scientific or task-equivalence claim. The initial inventory below remains historical.

## Historical initial inventory

- Hailo-10 `InferModel` output-format A/B result
- Hailo-10 FLOAT32-versus-native-UINT8 input A/B result
- v2.79.16 project knowledge base
- a non-destructive Smartmirror2 collection script
- a pre-commit privacy and large-file check

After collection, the repository also contains selected Hailo-8/Paper
three-stage reports, energy calibration records, v2.79.16 acceptance evidence,
the seven-model reconciliation and a compact diagnostic fixture from the
failed `biggerset` run.

## Collect on Smartmirror2

Extract this starter directory on Smartmirror2, then run:

```bash
cd "$HOME/onnx-splitpoint-results"
bash scripts/collect_from_smartmirror2.sh --scan
bash scripts/collect_from_smartmirror2.sh --collect
python3 scripts/check_before_commit.py .
```

`--scan` is read-only and reports which known sources exist and how large the
larger candidates are. `--collect` copies files without deleting sources or
destination files that are unrelated to the collection. It does not create a
new checksum or sealing layer.

The exact raw report for the older Hailo-8 UINT8/dequant format A/B is not
identifiable from the supplied directory trees. Locate it read-only with:

```bash
bash scripts/find_hailo8_format_ab.sh
```

The raw archive defaults to:

```text
~/ONNX-Splitpoint-Results-Archive
```

Override it only when desired:

```bash
ARCHIVE_ROOT=/path/to/other/disk \
  bash scripts/collect_from_smartmirror2.sh --collect
```

Using a different disk or NAS makes the raw archive a real second copy. A
second directory on the same Smartmirror2 filesystem is initially only a
staging copy.

## Historical repository bootstrap instructions

Review the output of the safety check first. Then:

```bash
git init -b main
git add README.md .gitignore docs inventory results experiments diagnostics scripts
git status --short
git diff --cached --stat
git commit -m "Initial curated ONNX Split-Point results archive"
```

Create the GitHub remote as **private first**. The result JSON files and logs
can contain local IP addresses, hostnames and absolute paths. A public release
should be made only after those fields have been reviewed or sanitized.

## Scope and claim status

This archive distinguishes three classes:

- `validated`: a test or measurement completed within its stated scope;
- `historical`: useful evidence from an older calibration or software state;
- `diagnostic`: useful for explaining a failure, but not a scientific result.

The Hailo-10 A/B files are real hardware microbenchmarks, not full
P1-to-FIFO-to-TensorRT-P2 pipeline claims. The old M.2 idle measurements are
historical until the v2.79.16 full-system gain calibration and subsequent idle
recalibration have been completed. The `biggerset` pack is a failed-run
diagnostic with zero started energy measurements.

See [docs/ARTIFACT_SELECTION.md](docs/ARTIFACT_SELECTION.md) and
[docs/CLAIM_STATUS.md](docs/CLAIM_STATUS.md) for the exact boundaries.

## Deliberately excluded from Git

- ONNX/PT models and validation images
- HEF, TensorRT and DeepX compiled binaries
- `BackendArtifacts`, compiler caches and build trees
- raw boundary/output `.bin` and `.npy` files
- complete delivery bundles and large evidence ZIPs
- credentials, private keys and environment files containing secrets

Existing compressed evidence is copied to the separate raw archive and can
later be attached to a GitHub Release if its licence, privacy and size have
been checked.
