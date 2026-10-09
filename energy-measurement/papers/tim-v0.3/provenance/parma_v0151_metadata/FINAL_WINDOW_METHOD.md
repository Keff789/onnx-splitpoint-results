# Final direct-window definition used by this manuscript

This note states the applied definition without a debugging chronology. The original detector
is documented in the results Git at the pinned commit, `2026-09-30-offline-windows/WINDOW_METHOD.md`.
The current series policy supersedes historical reporting exclusions in that old note.

## Detector and integration

For a uniform stored-power trace, trapezoidal integration uses every original adjacent pair,
with N-1 intervals. Nominal 0.1-s bin edges use numpy.rint to select original sample indices.
Bin power means are integral/bin_duration; boundaries can be irregular at low nominal rates.
A timestamped trace is integrated piecewise-linearly on its stored time axis. A finer display
bin is not evidence of a finer physical telemetry update rate.

Each recording must provide at least eight bins, at least two fully-contained bins in each
edge region and span >=1 s. Edge length is min(2 s, record_span/5).
Let B=min(median_pre,median_post), H=P95(all bin means), D=H-B and
s=1.4826*max(MAD_pre,MAD_post). Require

    D > max(1e-9 W, 0.005*max(abs(H),abs(B),1e-6 W), 6*s).

Qualified segments are strictly above B+f*D for >=0.2 s (numerical time tolerance 1e-10 s).
The envelope spans the first to the last qualified segment. Internal pauses are included.
Fixed f values are 0.4/0.5/0.6, with 0.5 as the main candidate; no best-energy search.
Edge-distance, elevated-edge, baseline-disagreement, sensitivity and provenance flags remain
in the exported metadata. Flags and large values are not used to trim otherwise available
finite, positive-duration candidates in this final paper view.

LLM uses the NPY-derived candidate; Hailo random-pattern uses reported_legacy across the whole
series, including recorded padding. This is not a per-run fallback to a favourable threshold.
Stationary comparisons (not in the main variable-load tables) retain explicit recorded windows.
No known/requested duration is forced on a new envelope. Actual integration span is the E/T
denominator. The old fixed 104-s common-reference cohort and native Hailo spectral prefixes
remain separate definitions, not output of this detector.

## Retention and limitations

All finite candidates with positive spans are retained, including sensitivity notes; missing
windows stay missing. No calibration, current offset, clock, temperature or spectral correction
is derived from the final manuscript statistics. Repeatability is not a total uncertainty budget.
Source snapshot contains narrowly documented terminal-prefix telemetry derivations from earlier
analysis; their flags remain in data/final_direct, and this build does not modify a time axis.
