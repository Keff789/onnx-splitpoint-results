#!/usr/bin/env bash
set -Eeuo pipefail

HOST="${H8_HOST:-nx@192.168.0.104}"
LOCAL_TOOL="${H8_LOCAL_TOOL:-$HOME/ONNX-Splitpoint-Tool}"
CACHE_ROOT="${H8_CACHE_ROOT:-/home/nx/splitpoint_runs/_onnx_splitpoint_cache/tensorrt/yolo26s-f5342b1cdbe0343f/native_split_quality/orin_nx_hailo8_01/yolo26s/b038/hailo8_to_trt/2f23be01e394bcda6679e87b833f8c2f0aed9c804ca86fff3fa7195c7a4657bb}"
FRAMES="${H8_FRAMES:-1000}"
WARMUP="${H8_WARMUP:-100}"
REPETITIONS="${H8_REPETITIONS:-4}"
QUEUE_DEPTH="${H8_QUEUE_DEPTH:-3}"
PAUSE_SECONDS="${H8_PAUSE_SECONDS:-2}"
STABILIZE_SECONDS="${H8_STABILIZE_SECONDS:-15}"
PREFLIGHT_ONLY="${H8_PREFLIGHT_ONLY:-0}"

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
RUN_ID="hailo8_uint8_bridge_ab_cache_$(date -u +%Y%m%d_%H%M%S)_$$"
LOCAL_OUT="$HOME/Downloads/$RUN_ID"
HELPER="$SCRIPT_DIR/hailo8_uint8_bridge_ab.py"
BUILDER_SOURCE="$LOCAL_TOOL/scripts/native_trt_from_benchmarkset.py"
RUNNER_SOURCE="$LOCAL_TOOL/scripts/native_hailo_trt_fifo_from_benchmarkset.py"

fail() {
  echo "STOP: $*" >&2
  exit 2
}

[[ -f "$HELPER" ]] || fail "helper missing: $HELPER"
[[ -f "$BUILDER_SOURCE" ]] || fail "TensorRT builder missing: $BUILDER_SOURCE"
[[ -f "$RUNNER_SOURCE" ]] || fail "native Hailo runner source missing: $RUNNER_SOURCE"
command -v ssh >/dev/null 2>&1 || fail "ssh is not installed"
command -v rsync >/dev/null 2>&1 || fail "rsync is not installed"

for value_name in FRAMES WARMUP REPETITIONS QUEUE_DEPTH; do
  value="${!value_name}"
  [[ "$value" =~ ^[0-9]+$ ]] || fail "$value_name must be an integer"
done
[[ "$PAUSE_SECONDS" =~ ^[0-9]+([.][0-9]+)?$ ]] || \
  fail "H8_PAUSE_SECONDS must be a nonnegative number"
[[ "$STABILIZE_SECONDS" =~ ^[0-9]+([.][0-9]+)?$ ]] || \
  fail "H8_STABILIZE_SECONDS must be a nonnegative number"
(( FRAMES > 0 )) || fail "H8_FRAMES must be > 0"
(( WARMUP >= 0 )) || fail "H8_WARMUP must be >= 0"
(( REPETITIONS > 0 )) || fail "H8_REPETITIONS must be > 0"
(( QUEUE_DEPTH > 0 )) || fail "H8_QUEUE_DEPTH must be > 0"
[[ "$PREFLIGHT_ONLY" == "0" || "$PREFLIGHT_ONLY" == "1" ]] || \
  fail "H8_PREFLIGHT_ONLY must be 0 or 1"

mkdir -p "$LOCAL_OUT"

REMOTE_HOME="$(ssh "$HOST" 'printf %s "$HOME"')"
[[ "$REMOTE_HOME" == /* ]] || fail "could not resolve remote home on $HOST"
REMOTE_RUN="$REMOTE_HOME/hailo8_uint8_bridge_ab_runs/$RUN_ID"
REMOTE_TOOL="$REMOTE_RUN/tool"
REMOTE_EVIDENCE="$REMOTE_RUN/evidence"

ssh "$HOST" "mkdir -p '$REMOTE_TOOL' '$REMOTE_EVIDENCE'"
rsync -a \
  "$HELPER" \
  "$BUILDER_SOURCE" \
  "$RUNNER_SOURCE" \
  "$HOST:$REMOTE_TOOL/"

remote_argv=(
  bash -s --
  "$REMOTE_TOOL" "$REMOTE_RUN" "$CACHE_ROOT"
  "$FRAMES" "$WARMUP" "$REPETITIONS" "$QUEUE_DEPTH"
  "$PAUSE_SECONDS" "$STABILIZE_SECONDS" "$PREFLIGHT_ONLY"
)
printf -v remote_shell_command '%q ' "${remote_argv[@]}"

set +e
ssh "$HOST" "$remote_shell_command" <<'REMOTE_RUN' \
  2>&1 | tee "$LOCAL_OUT/remote_console.log"
set -Eeuo pipefail

REMOTE_TOOL="$1"
REMOTE_RUN="$2"
CACHE_ROOT="$3"
FRAMES="$4"
WARMUP="$5"
REPETITIONS="$6"
QUEUE_DEPTH="$7"
PAUSE_SECONDS="$8"
STABILIZE_SECONDS="$9"
PREFLIGHT_ONLY="${10}"

PY=/usr/bin/python3
BUILDER="$REMOTE_TOOL/native_trt_from_benchmarkset.py"
RUNNER="$REMOTE_TOOL/native_hailo_trt_fifo_from_benchmarkset.py"
HELPER="$REMOTE_TOOL/hailo8_uint8_bridge_ab.py"
EVIDENCE="$REMOTE_RUN/evidence"
WORK="$REMOTE_RUN/work"
BENCHMARK_SET="$REMOTE_RUN/minimal_benchmark_set"
CASE=b038
SOURCE_CASE="$CACHE_ROOT/benchmark_set/$CASE"
SOURCE_PART2="$SOURCE_CASE/source_part2.onnx"
PART1_HEF="$CACHE_ROOT/part1.hef"
BOUNDARY_META="$CACHE_ROOT/part1_boundary_metadata.json"
QUALITY_BINDING="$CACHE_ROOT/native_split_quality_binding.json"
PRESERVED_DEQUANT_DIR="$CACHE_ROOT/engine_cache/$CASE/part2/uint8_dequant_fp16"
PRESERVED_DEQUANT_ENGINE="$PRESERVED_DEQUANT_DIR/part2_uint8_dequant_fp16.engine"
PRESERVED_DEQUANT_META="$PRESERVED_DEQUANT_DIR/native_trt_meta.json"
IMAGE="$REMOTE_RUN/synthetic_performance_input_640x640.ppm"

fail() {
  echo "STOP: $*" >&2
  exit 2
}

for command in "$PY" cmake g++ flock env; do
  command -v "$command" >/dev/null 2>&1 || fail "required command missing: $command"
done
exec 9>"/tmp/onnx_splitpoint_hailo8_uint8_bridge_ab_full.lock"
flock -n 9 || fail "another Hailo-8 UINT8 bridge A/B launcher is already running"
[[ -x /usr/src/tensorrt/bin/trtexec ]] || fail "trtexec missing"
compgen -G '/dev/hailo*' >/dev/null || fail "no /dev/hailo* device visible"

for path in \
  "$BUILDER" "$RUNNER" "$HELPER" "$SOURCE_PART2" "$PART1_HEF" \
  "$BOUNDARY_META" "$QUALITY_BINDING" \
  "$PRESERVED_DEQUANT_ENGINE" "$PRESERVED_DEQUANT_META"; do
  [[ -f "$path" ]] || fail "required file missing: $path"
done

env -u PYTHONPATH -u PYTHONHOME -u PYTHONNOUSERSITE \
  "$PY" -B -c 'import onnx, numpy' || \
  fail "/usr/bin/python3 cannot import onnx and numpy"

BUILDER_HELP="$(
  env -u PYTHONPATH -u PYTHONHOME -u PYTHONNOUSERSITE \
    "$PY" -B "$BUILDER" --help
)"
for token in \
  uint8_cast_fp16 uint8_dequant_fp16 --out-dir --dequant-scale \
  --dequant-zero-point --boundary-layout --artifact-policy --no-run-smoke; do
  grep -F -- "$token" <<<"$BUILDER_HELP" >/dev/null || \
    fail "installed TensorRT builder lacks required option: $token"
done

"$PY" - "$RUNNER" <<'PY'
from pathlib import Path
import ast
import sys

path = Path(sys.argv[1])
tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
values = {}
for node in tree.body:
    if not isinstance(node, ast.Assign):
        continue
    if not isinstance(node.value, ast.Constant) or not isinstance(node.value.value, str):
        continue
    for target in node.targets:
        if isinstance(target, ast.Name) and target.id in {"CPP_SOURCE", "CMAKE_TXT"}:
            values[target.id] = node.value.value
if set(values) != {"CPP_SOURCE", "CMAKE_TXT"}:
    raise RuntimeError("installed native runner lacks embedded C++/CMake sources")
if "copy_input_from_boundary" not in values["CPP_SOURCE"]:
    raise RuntimeError("installed native runner lacks timed boundary handoff")
print("NATIVE_RUNTIME_SOURCE_PREFLIGHT=PASS")
PY

mkdir -p "$EVIDENCE" "$WORK" "$BENCHMARK_SET/$CASE"
FREE_KB="$(df -Pk "$REMOTE_RUN" | awk 'NR == 2 {print $4}')"
[[ "$FREE_KB" =~ ^[0-9]+$ ]] || fail "cannot determine free disk space"
(( FREE_KB >= 1048576 )) || fail "less than 1 GiB free below $REMOTE_RUN"

IFS=$'\t' read -r DEQUANT_SCALE DEQUANT_ZERO_POINT BOUNDARY_LAYOUT \
  BOUNDARY_RUNTIME_NAME BOUNDARY_BYTES < <(
  "$PY" - "$QUALITY_BINDING" "$PRESERVED_DEQUANT_META" \
    "$BOUNDARY_META" "$SOURCE_PART2" "$EVIDENCE/cache_contract.json" <<'PY'
from pathlib import Path
import json
import math
import sys

binding_path, meta_path, boundary_path, source_path, output_path = map(
    Path, sys.argv[1:]
)

def load(path):
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"JSON root is not an object: {path}")
    return value

binding = load(binding_path)
meta = load(meta_path)
boundary = load(boundary_path)
contract = binding.get("boundary_contract")
bridge = meta.get("uint8_cast_bridge")
if not isinstance(contract, dict):
    raise RuntimeError("quality binding has no boundary_contract object")
if not isinstance(bridge, dict):
    raise RuntimeError("preserved dequant metadata has no bridge object")
if bridge.get("schema") != "onnx-splitpoint/uint8-dequant-bridge":
    raise RuntimeError(f"unexpected bridge schema: {bridge.get('schema')!r}")

scale = float(contract.get("dequant_scale"))
zero_point = float(contract.get("dequant_zero_point"))
layout = str(
    contract.get("boundary_layout")
    or contract.get("boundary_layout_effective")
    or contract.get("boundary_layout_requested")
    or ""
)
if not math.isfinite(scale) or scale <= 0.0:
    raise RuntimeError(f"invalid dequant scale: {scale!r}")
if not math.isfinite(zero_point):
    raise RuntimeError(f"invalid dequant zero point: {zero_point!r}")
if not layout:
    raise RuntimeError("boundary layout is missing")

bridge_layout = bridge.get("boundary_layout")
bridge_layout = bridge_layout if isinstance(bridge_layout, dict) else {}
bridge_effective = str(
    bridge_layout.get("effective") or bridge_layout.get("requested") or ""
)
boundary_tensor = boundary.get("boundary_tensor")
boundary_tensor = boundary_tensor if isinstance(boundary_tensor, dict) else {}
quantization = boundary_tensor.get("quantization")
quantization = quantization if isinstance(quantization, dict) else {}
runtime_name = str(boundary_tensor.get("runtime_name") or "")
boundary_shape = boundary_tensor.get("shape")
if not isinstance(boundary_shape, list) or not boundary_shape:
    raise RuntimeError("boundary tensor shape is missing")
boundary_bytes = math.prod(int(dim) for dim in boundary_shape)
if not runtime_name or boundary_bytes <= 0:
    raise RuntimeError("invalid Hailo runtime boundary identity")
source_value = Path(str(bridge.get("source") or ""))
if source_value.is_absolute():
    resolved_bridge_source = source_value.resolve()
else:
    candidates = [
        (meta_path.parent / source_value).resolve(),
        (source_path.parent / source_value).resolve(),
    ]
    resolved_bridge_source = next(
        (candidate for candidate in candidates if candidate == source_path.resolve()),
        candidates[0],
    )
checks = {
    "identity_model": boundary.get("model_id") == "yolo26s",
    "identity_case": boundary.get("case_id") == "b038",
    "identity_setup": boundary.get("setup_id") == "orin_nx_hailo8_01",
    "identity_backend": boundary.get("backend") == "hailo8_to_trt",
    "boundary_count": boundary.get("boundary_tensor_count") == 1,
    "meta_case": meta.get("case") == "b038",
    "meta_variant": meta.get("variant") == "part2",
    "meta_precision": meta.get("precision") == "uint8_dequant_fp16",
    "meta_build_ok": meta.get("build_ok") is True,
    "scale_matches": math.isclose(
        float(bridge.get("scale")), scale, rel_tol=0.0, abs_tol=1e-12
    ),
    "zero_point_matches": math.isclose(
        float(bridge.get("zero_point")), zero_point,
        rel_tol=0.0, abs_tol=1e-12,
    ),
    "layout_matches": bridge_effective == layout,
    "layout_applied": bridge_layout.get("applied") is True,
    "source_matches": resolved_bridge_source == source_path.resolve(),
    "boundary_scale_matches": math.isclose(
        float(quantization.get("scale")), scale,
        rel_tol=0.0, abs_tol=1e-12,
    ),
    "boundary_zero_point_matches": math.isclose(
        float(quantization.get("zero_point")), zero_point,
        rel_tol=0.0, abs_tol=1e-12,
    ),
    "boundary_layout_matches": boundary.get("boundary_layout") == layout,
    "boundary_dtype_matches": str(boundary_tensor.get("dtype") or "").lower()
        == str(contract.get("boundary_tensor_dtype") or "").lower()
        == "uint8",
    "boundary_name_matches": boundary_tensor.get("name")
        == contract.get("boundary_tensor_name"),
    "boundary_shape_matches": boundary_tensor.get("shape")
        == contract.get("boundary_tensor_shape"),
}
failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise RuntimeError("preserved cache contract mismatch: " + ", ".join(failed))

payload = {
    "status": "PASS",
    "contract_source": "preserved_quality_binding_cross_checked_with_dequant_meta",
    "dequant_scale": scale,
    "dequant_zero_point": zero_point,
    "boundary_layout": layout,
    "runtime_boundary": {
        "output_count": 1,
        "output_name": runtime_name,
        "output_bytes": boundary_bytes,
    },
    "checks": checks,
    "paths": {
        "quality_binding": str(binding_path),
        "preserved_dequant_meta": str(meta_path),
        "boundary_metadata": str(boundary_path),
        "source_part2": str(source_path),
    },
}
output_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(
    f"{scale:.17g}\t{zero_point:.17g}\t{layout}\t"
    f"{runtime_name}\t{boundary_bytes}"
)
PY
)

[[ -n "$DEQUANT_SCALE" && -n "$DEQUANT_ZERO_POINT" && \
   -n "$BOUNDARY_LAYOUT" && -n "$BOUNDARY_RUNTIME_NAME" && \
   "$BOUNDARY_BYTES" =~ ^[0-9]+$ && "$BOUNDARY_BYTES" -gt 0 ]] || \
  fail "cache contract extraction failed"

# The overlay contains only symlinks to the preserved input artifacts.  Every
# generated ONNX bridge, TensorRT engine and measurement remains below RUN_DIR.
cp -as "$SOURCE_CASE/." "$BENCHMARK_SET/$CASE/"
mkdir -p "$BENCHMARK_SET/$CASE/hailo/hailo8/part1"
ln -s "$PART1_HEF" \
  "$BENCHMARK_SET/$CASE/hailo/hailo8/part1/compiled.hef"

"$PY" - "$IMAGE" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
width = height = 640
pixels = bytearray(width * height * 3)
offset = 0
for y in range(height):
    for x in range(width):
        pixels[offset] = x & 255
        pixels[offset + 1] = y & 255
        pixels[offset + 2] = (x + y) & 255
        offset += 3
with path.open("wb") as stream:
    stream.write(f"P6\n{width} {height}\n255\n".encode("ascii"))
    stream.write(pixels)
PY

"$PY" - "$EVIDENCE/replay_preflight.json" "$CACHE_ROOT" \
  "$BENCHMARK_SET" "$SOURCE_PART2" "$PART1_HEF" "$IMAGE" \
  "$DEQUANT_SCALE" "$DEQUANT_ZERO_POINT" "$BOUNDARY_LAYOUT" \
  "$BOUNDARY_RUNTIME_NAME" "$BOUNDARY_BYTES" "$PREFLIGHT_ONLY" <<'PY'
from pathlib import Path
import json
import sys

(out, cache, overlay, source, hef, image, scale, zero_point, layout,
 runtime_name, boundary_bytes, preflight_only) = sys.argv[1:]
payload = {
    "status": "PASS",
    "mode": "preflight_only" if preflight_only == "1" else "full_measurement",
    "case": "b038",
    "model": "yolo26s",
    "cache_access": "read_only_by_design",
    "original_cache": cache,
    "minimal_overlay": overlay,
    "source_part2": source,
    "part1_hef": hef,
    "input": image,
    "input_kind": "synthetic_performance_input",
    "engine_action": "fresh_build_both_arms_inside_overlay",
    "comparison_scope": "performance_diagnostic_not_quality_equivalence",
    "dequant_contract": {
        "scale": float(scale),
        "zero_point": float(zero_point),
        "boundary_layout": layout,
    },
    "runtime_boundary_contract": {
        "output_count": 1,
        "output_name": runtime_name,
        "output_bytes": int(boundary_bytes),
    },
}
Path(out).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
PY

echo "CACHE_CONTRACT=PASS"
echo "DEQUANT_SCALE=$DEQUANT_SCALE"
echo "DEQUANT_ZERO_POINT=$DEQUANT_ZERO_POINT"
echo "BOUNDARY_LAYOUT=$BOUNDARY_LAYOUT"
echo "BOUNDARY_RUNTIME_NAME=$BOUNDARY_RUNTIME_NAME"
echo "BOUNDARY_BYTES=$BOUNDARY_BYTES"

if [[ "$PREFLIGHT_ONLY" == "1" ]]; then
  echo "HAILO8_UINT8_BRIDGE_AB_CACHE_PREFLIGHT=PASS"
  exit 0
fi

build_arm() {
  local mode="$1"
  shift
  echo "=== BUILD $mode ==="
  ONNX_SPLITPOINT_ARTIFACT_POLICY=normal \
    env -u PYTHONPATH -u PYTHONHOME -u PYTHONNOUSERSITE \
    "$PY" -B "$BUILDER" \
      --benchmark-set "$BENCHMARK_SET" \
      --case "$CASE" \
      --variants part2 \
      --precision "$mode" \
      --out-dir "$BENCHMARK_SET/native_trt" \
      --trtexec /usr/src/tensorrt/bin/trtexec \
      --artifact-policy normal \
      --workspace-mb 4096 \
      --workspace-mode auto \
      --shape-policy auto \
      --build \
      --no-run-smoke \
      --json-out "$EVIDENCE/build_${mode}.json" \
      "$@" \
      2>&1 | tee "$EVIDENCE/build_${mode}_console.log"
}

build_arm uint8_cast_fp16
build_arm uint8_dequant_fp16 \
  --dequant-scale "$DEQUANT_SCALE" \
  --dequant-zero-point "$DEQUANT_ZERO_POINT" \
  --boundary-layout "$BOUNDARY_LAYOUT"

"$PY" - "$EVIDENCE" "$BENCHMARK_SET" <<'PY'
from pathlib import Path
import json
import shutil
import sys

evidence = Path(sys.argv[1])
benchmark_set = Path(sys.argv[2])
build_signatures = {}
for mode in ("uint8_cast_fp16", "uint8_dequant_fp16"):
    report_path = evidence / f"build_{mode}.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    artifacts = report.get("artifacts") or []
    if report.get("ok") is not True or len(artifacts) != 1:
        raise RuntimeError(f"{mode} build report is not successful and singular")
    if Path(str(report.get("trtexec") or "")).resolve() != Path(
        "/usr/src/tensorrt/bin/trtexec"
    ).resolve():
        raise RuntimeError(f"{mode} used an unexpected trtexec")
    artifact = artifacts[0]
    expected = {
        "case": "b038",
        "variant": "part2",
        "precision": mode,
        "build_ok": True,
    }
    for key, value in expected.items():
        if artifact.get(key) != value:
            raise RuntimeError(
                f"{mode} build contract mismatch: {key}="
                f"{artifact.get(key)!r}, expected {value!r}"
            )
    engine = Path(str(artifact.get("engine") or ""))
    if not engine.is_file():
        raise RuntimeError(f"{mode} engine is missing after successful build")
    build_signatures[mode] = {
        "shapes_arg": artifact.get("build_success_shapes_arg"),
        "workspace_mode": artifact.get("build_success_workspace_mode"),
    }
    work_dir = benchmark_set / "native_trt/b038/part2" / mode
    target = evidence / "build_logs" / mode
    target.mkdir(parents=True, exist_ok=True)
    for name in (
        "native_trt_meta.json",
        "build_trtexec.log",
        "build_trtexec_attempt2.log",
        "build_trtexec_attempt3.log",
        "engine_build_receipt.json",
    ):
        source = work_dir / name
        if source.is_file():
            shutil.copy2(source, target / name)
if len({tuple(value.items()) for value in build_signatures.values()}) != 1:
    raise RuntimeError(
        "A/B engine builds did not use the same shape/workspace policy: "
        f"{build_signatures}"
    )
(evidence / "build_fairness.json").write_text(
    json.dumps({"status": "PASS", "build_signatures": build_signatures}, indent=2)
    + "\n",
    encoding="utf-8",
)
print("FRESH_ENGINE_BUILDS=PASS")
PY

PYTHONPATH= PYTHONHOME= "$PY" -I -B "$HELPER" \
  --runner-source "$RUNNER" \
  --benchmark-set "$BENCHMARK_SET" \
  --case "$CASE" \
  --image "$IMAGE" \
  --out-dir "$EVIDENCE" \
  --work-dir "$WORK" \
  --frames "$FRAMES" \
  --warmup "$WARMUP" \
  --repetitions "$REPETITIONS" \
  --queue-depth "$QUEUE_DEPTH" \
  --pause-seconds "$PAUSE_SECONDS" \
  --stabilize-seconds "$STABILIZE_SECONDS" \
  --minimal-overlay \
  --expected-dequant-scale "$DEQUANT_SCALE" \
  --expected-dequant-zero-point "$DEQUANT_ZERO_POINT" \
  --expected-layout "$BOUNDARY_LAYOUT" \
  --expected-output-name "$BOUNDARY_RUNTIME_NAME" \
  --expected-output-bytes "$BOUNDARY_BYTES" \
  --input-kind synthetic_performance_input
REMOTE_RUN
remote_rc=${PIPESTATUS[0]}
set -e

# Always attempt to retrieve partial diagnostics. Engines and generated bridge
# ONNX files stay on the Jetson and are intentionally not copied locally.
set +e
rsync -a "$HOST:$REMOTE_EVIDENCE/" "$LOCAL_OUT/"
transfer_rc=$?
set -e

echo "LOCAL_EVIDENCE=$LOCAL_OUT"
echo "REMOTE_RUN=$REMOTE_RUN"
if (( remote_rc != 0 )); then
  echo "MEASUREMENT_STATUS=FAIL" >&2
  echo "See $LOCAL_OUT/remote_console.log and copied diagnostics." >&2
  exit "$remote_rc"
fi
if (( transfer_rc != 0 )); then
  fail "remote run succeeded but evidence transfer failed (rsync rc=$transfer_rc)"
fi

test -f "$LOCAL_OUT/cache_contract.json" || \
  fail "cache contract report is missing after evidence transfer"
test -f "$LOCAL_OUT/replay_preflight.json" || \
  fail "replay preflight report is missing after evidence transfer"

if [[ "$PREFLIGHT_ONLY" == "1" ]]; then
  echo "HAILO8_UINT8_BRIDGE_AB_CACHE_PREFLIGHT=PASS"
else
  test -f "$LOCAL_OUT/hailo8_uint8_bridge_ab_summary.json" || \
    fail "remote run returned success but summary is missing"
  test -f "$LOCAL_OUT/hailo8_uint8_bridge_ab_summary.md" || \
    fail "Markdown summary is missing after transfer"
  test -f "$LOCAL_OUT/hailo8_uint8_bridge_ab_runs.csv" || \
    fail "CSV run table is missing after transfer"
  test -f "$LOCAL_OUT/build_fairness.json" || \
    fail "build fairness report is missing after transfer"
  grep -F '"measurement_status": "PASS"' \
    "$LOCAL_OUT/hailo8_uint8_bridge_ab_summary.json" >/dev/null || \
    fail "summary did not report PASS"
  for mode in uint8_cast_fp16 uint8_dequant_fp16; do
    test -f "$LOCAL_OUT/build_${mode}.json" || \
      fail "build report missing after transfer: $mode"
    test -f "$LOCAL_OUT/build_${mode}_console.log" || \
      fail "build console missing after transfer: $mode"
    test -f "$LOCAL_OUT/build_logs/$mode/native_trt_meta.json" || \
      fail "build metadata missing after transfer: $mode"
  done
  shopt -s nullglob
  raw_results=("$LOCAL_OUT"/raw/run_*.json)
  run_logs=("$LOCAL_OUT"/logs/run_*.log)
  shopt -u nullglob
  expected_runs=$(( 2 * REPETITIONS ))
  (( ${#raw_results[@]} == expected_runs )) || \
    fail "incomplete raw evidence: ${#raw_results[@]}/$expected_runs files"
  (( ${#run_logs[@]} == expected_runs )) || \
    fail "incomplete run logs: ${#run_logs[@]}/$expected_runs files"
  echo "HAILO8_UINT8_BRIDGE_AB=PASS"
  echo "SUMMARY=$LOCAL_OUT/hailo8_uint8_bridge_ab_summary.md"
fi
