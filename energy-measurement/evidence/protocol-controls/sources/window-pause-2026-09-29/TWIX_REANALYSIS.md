# Twix reanalysis handoff

Status at freeze: not started. Existing campaigns remain the input; no new large
hardware campaign is required.

## Data readiness

Historical data and an earlier verified backup are accessible through Twix according
to the operator. That backup predates the newest 45-run iterations and pause tests.
Copy and verify those two complete experiment directories before assuming all new
raw arrays are available. Account-specific source/destination paths remain in the
private companion handoff. Git is not the raw-data archive.

## Offline contract

1. Read-only inventory: dataset identity, protocol, calibration profile, measurement
   boundary, available raw/power files and logs. Distinguish originals from duplicates.
2. Versioned window definitions: legacy, operational load/process window without
   forced duration, and interior diagnostic. Preserve intentional burst pauses.
3. Report energy, duration and per-run mean power separately. Reconstruct original
   detector bounds only where log/index evidence allows it; otherwise mark a new rule.
4. Use all quality-eligible repetitions and report exclusions; bind source labels to
   data keys. Different sensors need physical-time alignment, not matching indices.
5. Cache per-source/per-version results and support safe resume; never silently mix
   versions. Regenerate figures from result tables, not repeated multi-GB scans.
6. Keep Tek/Pico PSD/common-reference separate. Only update imported energy/duration
   tables if a concrete dependency exists. No broad spectral redo by default.

No thermal normalization, universal gain correction, engine rebuild or repetition
of the multi-week measurement campaign follows from this document. The current
45-run and pause tests are complete and should not be restarted to restore context.
