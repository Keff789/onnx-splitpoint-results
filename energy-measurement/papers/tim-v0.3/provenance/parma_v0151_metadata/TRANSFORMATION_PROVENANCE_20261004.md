# Transformation provenance audit — 2026-10-04

This audit adds source evidence for review §4.2. It does not change measurements, calibration, offsets, models, fits, stored result tables, numerical outputs, or cohorts. Collected source/scripts were read as inert data and were not executed. Evidence for journal workload builds (§4.3) remains separate; no journal workload is substituted into the frozen 13-run GEMM-FP16 cohort.

**Outcome:** the earlier YOLO-FP32 report establishes a **reported applied +111.917 mA additive Tek correction**, with reported uncertainty **4.092 mA**, ten reference rates, and 100 reference pairs. The signed addition and its order before power reconstruction are explicit in collected implementation source. The frozen package also retains the exact current scope configuration parameters. **Exact historical result → offset model → executed source/configuration binding is still partial.** An applied report, a configuration match, and present implementation are distinct pieces of evidence.

## Evidence classes and allowed conclusions

`data/provenance/transformations/transformationtable.csv` is the machine-readable audit table. Its eleven rows include confidence, binding status, missing fields, and an allowed claim. Here, “resolved” refers only to the named evidence layer; it does not silently upgrade archived formulas or settings into verified raw-to-result execution.

| Item | What is resolved | What remains open |
|---|---|---|
| YOLO-FP32 Tek shift | Earlier report records +111.917 mA as both estimated and applied; positive additive operator is explicit in collected code | Exact historical model/result bytes, model-hash definition, and historical executed source binding |
| Pico current | Positive raw offset and gain are exact in workbook, frozen native-source snapshot, collected generated config, and cache sidecar metadata | Historical executed source and complete per-run raw-to-stored-power lineage |
| Shared voltage/power | Exact linear voltage parameters, range, and `P=U(I)I` source operator | Independent voltage validation and execution lineage for each direct campaign |
| u.RECS static current | Exact archived workbook formula | Applied coefficient/version binding for current direct runs |
| u.RECS approximately 0.97 | Historical application description and explicit prevention of a second correction in legacy duration processing | Exact scale/executable lineage per current direct trace |
| Shelly | Two explicit archived affine calibrations, including a labelled power-supply change | Which coefficient/supply version produced each current campaign trace |

## YOLO-FP32 correction: parameter, sign, and binding

The earlier `SCOPE_COMPARISON_SUMMARY.md` is retained verbatim as `historical_YOLO_FP32_SCOPE_COMPARISON_SUMMARY.md` (5,819 bytes; SHA-256 `1b16c27e20c3843cc6d7c8b176c45c8208bd1a1741ba51ae6c6c01803431591f`). Its original file identities are recorded in `frozen_current_binding.json`. It states `stable_offset_detected_and_corrected`, detection and application both true, estimated/applied **111.917 mA**, uncertainty **4.092 mA**, and `post_hoc_workload_minus_external_idle_session_shift_not_independent`. Its final interpretation explicitly reports **+111.917 mA**. It preserves raw metrics and states that no gain correction is fitted or applied. These are historical reported results, not a newly measured offset.

The collected `commonref/scope_compare.py` source (`a246e01221f962c9f44c`; whole-file SHA-256 `659a76aed55b31a46ee54d75bf5fca939cd19f4dbc714d570ab659a7ee2daf3e`) defines the signed formula at original line 1623 and applies it at line 3513:

\[
I_{\mathrm{Tek,corrected}}=I_{\mathrm{Tek,raw}}+\Delta I.
\]

Its selected excerpts show that the helper returns an offset only for a model whose `correction_applied` is true and whose target is Tek. The workload path adds the offset to calibrated Tek current before calling the current-dependent voltage/power reconstruction. The external-idle helper returns zero when the model does not cover external idle. Therefore, the positive sign means an increase in Tek current; it is not a subtraction or a fitted gain. This proves the collected operator contract. The audit has not established that these exact source bytes were executed to produce the earlier report.

The frozen `data/validation/multi_workload/multi_workload_manifest.json` has SHA-256 `a43f833e05f2c810846bda4dc3d2810d62413501b152a73aa1b2405552c07b7f`, exactly matching fresh collected source `ca8617d545012307d9c0`. Its `$.scope_outputs[2]` pins the YOLO scope manifest hash `489b8588e55030ff0b5376c136a8c540485bf322c9dbeacc600b63dbfc78615f`; `$.workload_inventory[2]` records corrected status. Those referenced historical manifest bytes were not recovered by this collector. The old output path was missing and the scan of the relocated output tree reached its text-byte limit. Absence from this collector is not proof of absence on the original machine.

Twenty collected YOLO common-reference cache sidecar records cover Tek/Pico runs 0–9. Their selected metadata contains the current gain/offset and voltage parameters and records `zero_model_hash=f98ac74afe87d971d2040d5c6eb1777ff43f41596d1ccd4bd6bc02f4617092fc` in the exported CSV contexts. This is a recorded model identity; it is **not assumed to be a whole-file SHA-256**, and no exact offset-model bytes were available to associate this identity with the numeric 111.917-mA result. The cache raw-source hashes are explicitly **sampled hashes**, not whole-file raw-data identities.

The frozen native spectral inventory (`data/validation/native_spectra/spectral_sources.json`, SHA-256 `b2e810488a6221a621635c7af6ec58ca9a84551024848b027ebf0661f9fad392`) retains the YOLO source at `$[24]`. Its configuration snapshot is exactly equal, across every field after safe YAML parsing, to collected generated config `b4bdb81e6dd260524653` (SHA-256 `e4fc61d9d35cb87ede980bd84488471878854a694744e812dc2a63210690b638`). It records workload-only correction and no new fit, and references YOLO `pair_metrics.csv` SHA-256 `bd37ae697351f9b919931ea8be5cd89363485696febf97d8cb56ab732eaa651d` and `psd_metrics.json` SHA-256 `fa33fdb3b373dfbf9108e9434591e0afbe235829f8bb9faa99834b7fee68668f`. These are retained hash references, not recovered and independently verified result bytes. The earlier report's selected primary PSD rate is 25 MS/s; the current multi-workload stage uses a common 5-MS/s representation. The report is not substituted for the current stage.

To close the remaining binding, recover the exact referenced historical scope manifest and offset model; retain the signed applied offset and correction scope; document the model-hash algorithm; and bind them to the config, actual executed source/build, and the current stored outputs. No recalculation is required merely to preserve those historical artifacts.

## Current reconstruction settings and archived calibration

The frozen scope snapshot and collected configuration store:

\[
I_{\mathrm{Pico}}=(v_{\mathrm{raw}}+0.0004272598504)\,1.99000512058047,
\quad
U(I)=19.062607082705-0.07444582I,
\quad
P(I)=U(I)I.
\]

The raw Pico quantity is volts at the INA225 output; the gain is A/V and the offset is **added before multiplying**. Tek baseline calibration is identity (`offset_raw=0`, `gain_a_per_raw=1`, raw amperes) before its separate session shift. The shared voltage model is declared valid for **0–3.5 A**, is applied to both scope paths, and is not an independent voltage validation. `scope_compare_operator.txt` and `voltage_model_operator.txt` preserve the corresponding source operators.

The frozen workbook `data/validation/calibration/jetson_calibration.ods` has SHA-256 `1f4c154806426dd2db193ce4cff7b7c7b88b8c778954cdf9058f44c498bf1e16`; its `content.xml` has SHA-256 `4adaea65b4aeaf77fdde510dea4200677d0c3cfabd8a01b2c7ea1a732d97bdc8`. Selected formula strings and cached values are retained in `archived_ODS_formula_cells.csv`; no formulas were recalculated. INA225 cells `C43/D43` contain the above Pico conversion. Firmware cells `C44/D44/E44` contain:

\[
I_{\mu\mathrm{RECS}}=(i_{\mathrm{raw,mA}}/1000+0.004704622)\,0.997224237630222.
\]

The approximately **0.97** Jetson u.RECS power multiplier is a separate comparison-derived historical scale described in existing `metadata/CALIBRATION_VALIDATION.md`. Collected legacy duration config declares `urecs_values_already_include_correction_factor=true`; collected source creates a second factor-corrected variant only when that flag is false. Stored processed duration results must therefore not be multiplied again. The live Rust source instead contains `1-0.03127795823408493`, marks its validity TODO, and leaves the Jetson static-current calibration branch `todo!()`. It is a distinct source candidate, not proof of the exact factor used in current frozen traces.

The Shelly workbook contains `(P_raw-40.40749136)*0.796818078`, then explicitly labels row 155 **“RECALIBRATION – POWERSUPPLY Change”** and uses `(P_raw-41.36936767)*0.795372365`. These archival formulas do not identify the supply/coefficient version of each current campaign. Live Rust M2/NvGpu coefficients are different, and its Jetson Shelly branch is `todo!()`; those coefficients are retained only as rejected transfer candidates. This audit neither chooses a universal Shelly factor nor applies one.

## Curated proof and remaining scope

`CURATED_PROOF_MANIFEST.json` hashes the curated evidence files. `collector_selected_sources.csv` retains original source IDs, paths, hash scopes, and source classifications; filtered transformation/binding/hash-reference CSVs and run-0 sidecar excerpts preserve only the relevant proof. The collector strips one terminal LF from `evidence_text`: the included generated YAML restores exactly one LF, and its complete SHA-256 then matches the collector's original-file hash. Extracted subsets have their own artifact hashes and do not claim to be whole-source bytes.

The evidence improves parameter/operator provenance for review §4.2 while leaving the exact historical execution chain and current direct-campaign raw-to-power lineage explicitly open. It supplies no new measurements, fits, full private history, or credentials, and changes no paper or journal cohort.
