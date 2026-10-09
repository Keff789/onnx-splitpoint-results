# Static current calibration and verification

## Sources and identity

The unmodified `data/validation/calibration/jetson_calibration.ods` is the archived
Jetson calibration workbook from the frozen repository commit
`e87730135385e756c667fc2b573fb1a86834d4bb`:

<https://github.com/Keff789/onnx-splitpoint-results/blob/e87730135385e756c667fc2b573fb1a86834d4bb/energy-measurement/Ergebnisse_Joris/power_measurements_plots/calibration/jetson_calibration.ods>

- Workbook SHA-256: `1f4c154806426dd2db193ce4cff7b7c7b88b8c778954cdf9058f44c498bf1e16`.
- Original `content.xml` SHA-256: `4adaea65b4aeaf77fdde510dea4200677d0c3cfabd8a01b2c7ea1a732d97bdc8`.
- The verification-row CSV and supplied summary JSON are preserved source exports.
  They are checked against the workbook, not substituted for its original cells.

The setup description is independently documented in Joris Wachsmuth,
*Entwicklung und Validierung eines Messsystems zur energetischen Bewertung
eingebetteter KI-Beschleuniger*, Master's thesis, Universitaet Bielefeld,
Technische Fakultaet, July 2026. The supplied thesis PDF has SHA-256
`897428afa66e9674f8e3ef9b2356bba2cf565fda471803bb9a2ed28de8001191`.
The actual title and month were verified by rendering its title page (PDF page 1).
The thesis itself is not bundled in this calibration directory.

## Measurement procedure

Thesis section 6.3, printed pages 53--54 / PDF pages 59--60, documents an
EA-EL 9080-60 DT electronic load and a Fluke 179 multimeter. Multimeter current
readings were recorded manually. There were 36 approximately equally spaced
load settings from commanded zero to 3.5 A, about 100 mA apart. Each setting was
recorded for ten seconds and reduced to one average per path. The u.RECS path
sampled at 2 kS/s and PicoScope at 5 MS/s. Gain and offset corrections were
obtained from the calibration sweep and retained for a separate verification
sweep. This release retains the archived coefficients and recalculates their
application; it does not estimate a new calibration or alter stored power data.

The ODS contains the following original verification blocks:

| Current path | Sheet | All verification rows | Adjusted-current column | Signed-error column | Stored median cell |
|---|---|---|---|---|---|
| PicoScope / external INA225 | `INA225` | 43--78 | D | F | F80: `MEDIAN(F44:F78)` |
| u.RECS | `firmware` | 44--79 | E | G | G81: `MEDIAN(G45:G79)` |

The relative deviation is `100 * (corrected current - multimeter current) /
multimeter current`. Its sign is retained. The first point in each block is the
commanded-zero load setting, although both multimeter readings are 0.002 A.
Those two rows remain in the exported data and are explicitly flagged. They are
excluded from the percentage summaries, leaving 35 verification points per
path. Filtering on a numerically positive multimeter reading would incorrectly
retain these commanded-zero settings.

## Independently recalculated summaries

`scripts/verify_calibration.py` reads `content.xml` directly using only the Python
standard library. It expands ODF repeated rows/cells, checks the original
gain/offset formulas, recomputes corrected currents from the raw source cells,
and compares all 72 rows and both summaries with the preserved exports.

| Statistic, nonzero-target points only | PicoScope / INA225 | u.RECS |
|---|---:|---:|
| Number of points | 35 | 35 |
| Median signed relative deviation | -0.037667387120% | -0.046521946457% |
| Mean signed relative deviation | -0.189204884531% | -0.050531278655% |
| Mean absolute relative deviation | 0.193914268089% | 0.060140554922% |
| Maximum absolute relative deviation | 1.977118158660% | 0.439000977984% |
| Mean absolute current difference | 0.000937568611 A | 0.000820505508 A |

The approximately 0.04% and 0.05% figures therefore describe the **magnitudes of
the signed medians**, rounded to two decimals. They must not be labelled mean
absolute deviations. The source ODS median formulas are explicit. Machine-readable
results are in `data/validation/calibration/validation_result.json`; manuscript
macros are in `generated/calibration_numbers.tex`.

Reproduction:

```bash
python3 scripts/verify_calibration.py --write
python3 scripts/verify_calibration.py
```

The first command updates the derived QA JSON and macros only after the checks
pass; the second validates the generated macros without changing the sources.
There are no new fits, raw-waveform reads or network reads.

## Voltage treatment and Jetson scale provenance

Thesis section 6.3.2, printed pages 55--56 / PDF pages 61--62, documents a
current-to-voltage estimate obtained using PicoScope voltage and multimeter
current under fixed supply/connection conditions. It was checked on a second
sweep. Its reported static voltage deviations are specific to that setup.
This revision preserves each campaign's recorded voltage treatment and does not
create, update or retrospectively apply a voltage correction.

Thesis section 7.3, printed pages 65--66 / PDF pages 71--72, documents the additional
approximately 0.97 Jetson u.RECS power multiplier. It was obtained from the mean
of the previously observed u.RECS/PicoScope differences in the first variable-YOLO
and GEMM-FP16 benchmark families and then applied consistently to the affected
Jetson measurements. It is an empirical comparison-derived scale, distinct from
the static multimeter current calibration. The thesis does not establish its
applicability to Hailo. No factor is fitted or transferred to another campaign
by this revision.

## Hardware identity and interpretation

Thesis section 4.1.4, printed page 29 / PDF page 35, explicitly identifies an
ADS7953 12-bit ADC; section 6.1.2, printed page 48 / PDF page 54, instead writes
ADS7952 while discussing expected errors. The supported hardware description
and existing paper use ADS7953; this revision retains that identity rather than
inferring a different part from the inconsistent discussion.

The approximately 77-kHz differential current-path bandwidth is a nominal
component/setup description. The thesis ADC sine test uses a 300-Hz, 0--2-V
signal connected directly to the u.RECS ADC, and gives SINAD 58.9 dB / ENOB 9.49
(section 6.2, printed pages 49--52 / PDF pages 55--58). The chip-select timing
measurement reports 3.334-ns standard deviation and 452.2-ns maximum deviation.
These characterisations are useful evidence, but do not isolate the complete
dynamic shunt/amplifier/voltage response. The static verification residuals are
agreement with the recorded multimeter readings. No calibration certificate,
absolute electrical accuracy bound or complete power-uncertainty budget is
introduced or inferred here.
