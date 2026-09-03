# Current result and claim status

Updated: 2026-09-03

| Evidence | Status | What it demonstrates | Important limit |
| --- | --- | --- | --- |
| Hailo-10 output-format A/B | validated microbenchmark | Native UINT8 output reduces host output bytes 4x and dequantizes exactly for the tested tensor; throughput at inflight 2 is essentially unchanged | Not a full split-pipeline benchmark |
| Hailo-10 input-format A/B | validated microbenchmark | Native UINT8 input is exactly device-equivalent, reduces input bytes 4x and improves single-outstanding-job rate from about 20.15 to 78.28 FPS | Part 1 only; no additional InferModel job parallelism |
| Hailo-10 v2.79.16 HEF smoke | validated hardware microbenchmark; report collected | UINT8 input and output through `infer_model`; console result reported 13.335 ms mean over 20 runs | Part 1 only, diagnostic inflight 1; not P1→FIFO→TRT-P2 |
| Hailo-8 YOLOv7 product normal runner | validated within archived run | Three-stage concurrency with about 97.077 P2-output FPS, 97.059 completed-detection FPS and a ratio near 1 | Historical hardware evidence; keep the exact archived result with the claim |
| Hailo-8 32-image gate | validated within gate scope | Multi-image and postflight quality/oracle evidence | Corpus images and binaries should not be published blindly |
| Existing M.2 idle JSONs | historical baseline | Plausibility of off/on deltas for DeepX, Hailo-8 and Hailo-10 | Old full-system scale domain; repeat after v2.79.16 FS gain calibration |
| v2.79.16 installation acceptance | validated software/install scope | Installed release and focused acceptance passed | Does not replace real FS calibration or end-to-end evaluation |
| `biggerset_20260903_090110` | diagnostic only | Explains the former global native-preflight stop, missing energy start and report-finalization failure | Zero claim-eligible energy measurements; not a benchmark result |
| v2.78.4 seven-model reconciliation v2 | analysis evidence | Reconstructs useful rows and quality joins from the long run | Preserve exclusions and original run limitations |

## Hailo-10 A/B values already present

### Native output versus FLOAT32 output

- output bytes per frame: 3,276,800 → 819,200 (`4x` reduction);
- mean latency: 63.027 ms → 49.741 ms (`1.267x` latency speedup);
- throughput: 28.348 → 28.294 FPS at effective inflight 2;
- dequantized output comparison: exact for the tested output tensor.

The output-format change reduces transfer volume and latency, but it did not
increase throughput in that inflight-2 microbenchmark.

### Native UINT8 input versus FLOAT32 input

- input bytes per frame: 4,915,200 → 1,228,800 (`4x` reduction);
- mean InferModel latency: 49.618 ms → about 12.769 ms;
- single-outstanding-job rate: 20.151 → 78.280 FPS (`3.885x`);
- output equality: exact in quantized units;
- external reference quantization: about 1.259 ms, reported separately and not
  included in either InferModel timing.

This is the evidence behind the v2.79.16 native-UINT8 input correction.

## v2.79.16 software checks already completed

- installation acceptance: `PASS`;
- focused closure tests: `468/468`;
- inherited problem subset: `13 PASS / 12 FAIL` with the same failures as the
  pristine comparison bundle, so this is regression parity rather than a fully
  green total suite;
- current Paper three-stage offline tests: `14/14`.

None of these software checks substitutes for the pending calibrated hardware
end-to-end run.

## Known evidence-discovery gap

An earlier Hailo-8 UINT8-cast-versus-correct-dequant format A/B was documented
with about 146.259 FPS and 0.147 ms handoff for both variants. The supplied
Smartmirror2 trees do not reveal an unambiguous raw-report filename for that
test. Until the exact JSON/report is found, this remains a documented prior
observation rather than primary evidence in this repository. The Hailo-8
completion-tail, fast-decode, multi-image and three-stage A/B records are
separate experiments and are collected normally.

## Pending before final thesis claims

1. Record a consistent Jetson power-mode/clock policy on all three systems.
2. Perform the guided v2.79.16 full-system gain calibration with actual load
   current values.
3. Repeat M.2 idle calibration on the corrected full-system scale.
4. Run one small full end-to-end evaluation on all three setups with Native and
   Energy enabled.
5. Verify Hailo-10 P1→FIFO→TensorRT-P2, non-zero energy, final reports and
   correct combined Generic/Native energy-plan semantics.
