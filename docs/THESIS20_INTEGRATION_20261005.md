# THESIS20 integration — 5 October 2026

The reviewed scientific analysis was fast-forwarded and normally pushed to `main`
before navigation changes or publication of any new ranking-method results.

| Reference | Commit |
|---|---|
| Main before integration, fetched from origin | `e7bd8d82283034efa8bdaddf9dc987d3008d4885` |
| Reviewed branch and main after integration, read back from origin | `82f0a257f32f5b9eaf4d04260bb2cf9fad0b9641` |
| Unchanged tool v2.92.0 checkout | `d164aad6d7c7ef68c1b371c49a1fdea0a3b27dd7` |

Both working trees were clean before integration. The review commit is the direct
child of the starting main commit; the fetched diff matched the documented review.
No conflicting writer to the result checkout was found. Git used `fetch origin`,
`switch main`, `merge --ff-only 82f0a257f32f5b9eaf4d04260bb2cf9fad0b9641`,
`push origin main` and `ls-remote origin refs/heads/main`. No history was rewritten.

Validation from the actual curated checkout: **31 passed in 1.18 s**, no failures
or skips. A new reproduction outside the source tree returned exit code 0 and
matched **71/71 generated files byte for byte**, including tables and PDF/SVG/PNG
figures. The test process also returned 0. Commands, with paths made portable:

```bash
THESIS20_SOURCE_ROOT="$PWD/results/evaluation/thesis20_20261004/deep_analysis/source" PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider --basetemp /tmp/thesis20-integration-tests results/evaluation/thesis20_20261004/deep_analysis/tests
PYTHONDONTWRITEBYTECODE=1 python results/evaluation/thesis20_20261004/deep_analysis/scripts/reproduce.py --output-root /tmp/thesis20-integration-reproduced
```

The controller used its existing Python 3.12 / NumPy 1.26.4 / Matplotlib 3.5.2
environment and fresh report directories for tests, plots and comparison logs.
The 31 tests are repetitions of the existing focused tests, not 31 additional
independent cases. The artifact comparison was run after the producer completed.

No tool-wide acceptance, normal-GUI acceptance, inference, calibration, model
compilation, quality campaign or energy/performance measurement was run. The
analysis remains post-hoc, with unchanged quality decisions and claim gates.

The existing archival sessions were inspected read-only. YOLO copying continued;
corrected inputs, external originals, source checkpoints, BASE verification and
the frozen deep-analysis follow-up remained on the existing sequential paths.
The new work is outside these copy sources. No new archival job was started.

The subsequent navigation change checked 33 relative links with no missing
targets, confirmed the documented reproduction script path, and passed
`git diff --check`. Only README/documentation files changed; evidence paths stayed fixed.
