#!/usr/bin/env bash
set -Eeuo pipefail

HERE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
DL="${DL:-$HOME/Downloads}"
H8="${H8:-nx@192.168.0.104}"
STAMP="$(date +%Y%m%d_%H%M%S)"
EXPECTED_JSON="$HERE/expected.json"
BINDING="$HERE/reference/native_split_quality_binding.json"

SOURCE_ZIP="${SOURCE_ZIP:-$(
  find "$DL" -maxdepth 1 -type f \
    -name 'ONNX-Splitpoint-Tool_v2.79.4_native_productized_three_stage_release_consistency_source*.zip' \
    -printf '%T@ %p\n' 2>/dev/null \
  | sort -nr | head -n 1 | cut -d' ' -f2-
)}"

read_expected() {
  python3 - "$EXPECTED_JSON" "$1" <<'PY'
import json,sys
print(json.load(open(sys.argv[1],encoding="utf-8"))[sys.argv[2]])
PY
}

EXPECTED_SOURCE_SHA="$(read_expected source_release_sha256)"
EXPECTED_BINDING_SHA="$(read_expected binding_sha256)"
EXPECTED_IMAGE_SHA="$(read_expected image_sha256)"
EXPECTED_HEF_SHA="$(read_expected hef_sha256)"
EXPECTED_ENGINE_SHA="$(read_expected engine_sha256)"

test -n "${SOURCE_ZIP:-}" && test -f "$SOURCE_ZIP" || {
  echo "STOP: v2.79.4 source ZIP missing under $DL"
  exit 66
}
[[ "$(sha256sum "$SOURCE_ZIP" | awk '{print $1}')" == "$EXPECTED_SOURCE_SHA" ]] || {
  echo "STOP: source ZIP SHA-256 mismatch"
  exit 65
}
[[ "$(sha256sum "$BINDING" | awk '{print $1}')" == "$EXPECTED_BINDING_SHA" ]] || {
  echo "STOP: binding SHA-256 mismatch"
  exit 65
}
unzip -t "$SOURCE_ZIP" >/dev/null

REMOTE_ROOT="/home/nx/v2794_yolov7_b066_product_normal_runner_${STAMP}"
LOCAL_RESULT="$DL/v2794_yolov7_b066_product_normal_runner_${STAMP}.zip"

echo "============================================================"
echo " v2.79.4 YOLOv7 b066 PRODUCT NORMAL-RUNNER SMOKE"
echo "============================================================"
echo "H8=$H8"
echo "SOURCE_ZIP=$SOURCE_ZIP"
echo "SOURCE_SHA256=$EXPECTED_SOURCE_SHA"
echo "REMOTE_ROOT=$REMOTE_ROOT"

ssh -o BatchMode=yes -o ConnectTimeout=10 "$H8" \
  "rm -rf '$REMOTE_ROOT' && mkdir -p '$REMOTE_ROOT'"
scp -q "$SOURCE_ZIP" "$H8:$REMOTE_ROOT/source.zip"
scp -q "$BINDING" "$H8:$REMOTE_ROOT/native_split_quality_binding.json"

set +e
ssh -o BatchMode=yes -o ConnectTimeout=10 "$H8" \
  bash -s -- \
  "$REMOTE_ROOT" "$EXPECTED_SOURCE_SHA" "$EXPECTED_BINDING_SHA" \
  "$EXPECTED_IMAGE_SHA" "$EXPECTED_HEF_SHA" "$EXPECTED_ENGINE_SHA" <<'REMOTE'
set -Eeuo pipefail

ROOT="$1"
EXPECTED_SOURCE_SHA="$2"
EXPECTED_BINDING_SHA="$3"
EXPECTED_IMAGE_SHA="$4"
EXPECTED_HEF_SHA="$5"
EXPECTED_ENGINE_SHA="$6"
OUT="$ROOT/evidence"
SOURCE_ZIP="$ROOT/source.zip"
BINDING="$ROOT/native_split_quality_binding.json"
SRC="$ROOT/source"
BS="$ROOT/benchmark_set"
mkdir -p "$OUT"
exec > >(tee "$OUT/full_console.log") 2>&1

FINALIZED=0
finalize() {
  local rc="${1:-99}"
  (( FINALIZED == 0 )) || return 0
  FINALIZED=1
  {
    echo "RUNNER_RC=$rc"
    echo "REMOTE_HOST=$(hostname -f 2>/dev/null || hostname)"
    echo "REMOTE_TIME=$(date --iso-8601=seconds 2>/dev/null || date)"
  } >"$OUT/final_status.env"
  (
    cd "$OUT"
    find . -type f ! -name SHA256SUMS.txt -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS.txt
  )
  /usr/bin/python3 - "$OUT" "$ROOT/v2794_yolov7_b066_product_normal_runner_$(date +%Y%m%d_%H%M%S).zip" <<'PY'
import sys,zipfile
from pathlib import Path
src=Path(sys.argv[1]).resolve(); dst=Path(sys.argv[2]).resolve()
with zipfile.ZipFile(dst,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(src.rglob("*")):
        if p.is_file(): z.write(p,arcname=f"{src.name}/{p.relative_to(src)}")
with zipfile.ZipFile(dst) as z:
    bad=z.testzip()
    if bad: raise SystemExit(f"CRC failure: {bad}")
print(dst)
PY
}
trap 'rc=$?; finalize "$rc"; exit "$rc"' EXIT

[[ "$(sha256sum "$SOURCE_ZIP" | awk '{print $1}')" == "$EXPECTED_SOURCE_SHA" ]]
[[ "$(sha256sum "$BINDING" | awk '{print $1}')" == "$EXPECTED_BINDING_SHA" ]]
rm -rf "$SRC"; mkdir -p "$SRC"; unzip -q "$SOURCE_ZIP" -d "$SRC"
TOOL="$SRC/ONNX-Splitpoint-Tool_v2.79.4"
RUNNER="$TOOL/scripts/native_hailo_trt_fifo_from_benchmarkset.py"
HELPER="$TOOL/scripts/native_hailo_trt_concurrent_three_stage_from_benchmarkset.py"
CANARY="$TOOL/onnx_splitpoint_tool/resources/native_concurrent_three_stage_yolov7/three_stage_canary.py"
test -f "$RUNNER"; test -f "$HELPER"; test -f "$CANARY"

echo "V2793_ISOLATED_SOURCE_PATCH=NOT_REQUIRED"

SYS_PY=/usr/bin/python3
HAILO_PY=/home/nx/hailo_py/bin/python
test -x "$HAILO_PY"
HAILO_SITE="$("$HAILO_PY" - <<'PY'
import os,site,sysconfig
p=[]
try:p+=site.getsitepackages()
except Exception:pass
for k in ("purelib","platlib"):
    v=sysconfig.get_paths().get(k)
    if v:p.append(v)
print(os.pathsep.join(dict.fromkeys(x for x in p if os.path.isdir(x))))
PY
)"
test -n "$HAILO_SITE"
export PYTHONNOUSERSITE=1
export SPLITPOINT_EXTRA_SITES="$HAILO_SITE"

"$SYS_PY" - "$TOOL" <<'PY'
import os,site,sys
from pathlib import Path
tool=Path(sys.argv[1]);sys.path.insert(0,str(tool))
for p in os.environ["SPLITPOINT_EXTRA_SITES"].split(os.pathsep):
    if p:site.addsitedir(p)
import onnx_splitpoint_tool as pkg
import tensorrt, hailo_platform, numpy
assert pkg.__version__=="2.79.4"
assert pkg.__build_id__=="v2.79.4-native-productized-three-stage-release-consistency"
print("VERSION="+pkg.__version__)
print("BUILD_ID="+pkg.__build_id__)
print("NUMPY_VERSION="+numpy.__version__)
print("TENSORRT_VERSION="+tensorrt.__version__)
print("MIXED_RUNTIME_IMPORT=PASS")
import json
manifest=json.loads((tool / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
assert manifest["package_version"] == "2.79.4"
assert manifest["workflow_version"] == "v2.79.4-native-productized-three-stage-release-consistency"
print("SOURCE_MANIFEST_IDENTITY=PASS")
PY

# Verify dispatch and binding propagation without hardware.
"$SYS_PY" - "$RUNNER" "$BINDING" <<'PY'
import importlib.util,sys
from pathlib import Path
from types import SimpleNamespace
path=Path(sys.argv[1]);binding=sys.argv[2]
spec=importlib.util.spec_from_file_location("runner",path)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
a=SimpleNamespace(
 task="detection",hw_arch="hailo8",detection_endpoints="dual",
 completion_runtime_mode="fast_oracle_outside_timing",
 native_split_quality_binding=binding,case="b066",model_id="yolov7_paper",
 precision="uint8_dequant_fp16",benchmark_set="/tmp/bs",image="/tmp/image.jpg",
 frames=1000,warmup=100,repetitions=3,queue_depth=3,post_queue_depth=4,
 duration_s=0.0,setup_id="orin_nx_hailo8_01",eval_run_id="run",
 source_run_id="hailo8_to_trt",expected_image_sha256="",
 expected_hef_sha256="",expected_engine_sha256="",
 expected_boundary_layout="memory_nhwc_to_nchw",work_dir="/tmp/work",
 result_json="/tmp/result.json",build=True,run=True,device_id="",
 expected_runner_sha256="",source_contract_sha256="",
 expected_executable_sha256="",raw_preprocess_scope="paper_image",
 preprocess_mode="letterbox",letterbox_pad_value=114,hailo_format="uint8",
 copy_outputs=True,concurrent_timeout_s=3600.0)
assert m._v2791_use_concurrent_three_stage(a)
for endpoint in ("raw_model_outputs","completed_task"):
    cmd=m._dual_child_command(args=a,endpoint=endpoint,work=Path("/tmp")/endpoint,
        result_json=Path("/tmp")/(endpoint+".json"),
        config_json=Path("/tmp")/(endpoint+"-config.json"))
    assert "--native-split-quality-binding" in cmd
print("CONCURRENT_DISPATCH=PASS")
print("DUAL_BINDING_PROPAGATION=PASS")
PY

CACHE_BS="$("$SYS_PY" - "$BINDING" <<'PY'
import json,sys
from pathlib import Path
b=json.load(open(sys.argv[1],encoding="utf-8"))
print(Path(b["artifacts"]["source_part2_onnx"]["path"]).resolve().parents[1])
PY
)"
HEF="$("$SYS_PY" - "$BINDING" <<'PY'
import json,sys
print(json.load(open(sys.argv[1],encoding="utf-8"))["artifacts"]["part1_runtime"]["path"])
PY
)"
ENGINE="$("$SYS_PY" - "$BINDING" <<'PY'
import json,sys
print(json.load(open(sys.argv[1],encoding="utf-8"))["artifacts"]["engine"]["path"])
PY
)"
test -d "$CACHE_BS"; test -f "$HEF"; test -f "$ENGINE"
[[ "$(sha256sum "$HEF"|awk '{print $1}')" == "$EXPECTED_HEF_SHA" ]]
[[ "$(sha256sum "$ENGINE"|awk '{print $1}')" == "$EXPECTED_ENGINE_SHA" ]]

IMAGE=""
for p in \
 /home/nx/onnx_splitpoint_resurrection_canary_v3/staged_inputs/000000000632.jpg \
 "$CACHE_BS/resources/validation/detection/val2017_n500_s20260710/000000000632.jpg" \
 "$CACHE_BS/resources/validation/detection/000000000632.jpg"
do
  if [[ -f "$p" ]] && [[ "$(sha256sum "$p"|awk '{print $1}')" == "$EXPECTED_IMAGE_SHA" ]]; then
    IMAGE="$p"; break
  fi
done
test -n "$IMAGE"
rm -rf "$BS"; cp -a "$CACHE_BS" "$BS"

cat >"$OUT/runtime_identity.env" <<EOF
TOOL=$TOOL
CACHE_BS=$CACHE_BS
BENCHMARK_SET=$BS
BINDING=$BINDING
IMAGE=$IMAGE
HEF=$HEF
ENGINE=$ENGINE
EOF

set +e
"$SYS_PY" "$RUNNER" \
 --benchmark-set "$BS" \
 --case b066 \
 --hw-arch hailo8 \
 --precision uint8_dequant_fp16 \
 --image "$IMAGE" \
 --frames 1000 \
 --warmup 100 \
 --repetitions 3 \
 --queue-depth 3 \
 --hailo-format uint8 \
 --task detection \
 --detection-endpoints dual \
 --completion-runtime-mode fast_oracle_outside_timing \
 --raw-preprocess-scope paper_image \
 --preprocess-mode letterbox \
 --letterbox-pad-value 114 \
 --copy-outputs \
 --setup-id orin_nx_hailo8_01 \
 --eval-run-id paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251 \
 --source-run-id hailo8_to_trt \
 --model-id yolov7_paper \
 --native-split-quality-binding "$BINDING" \
 --expected-image-sha256 "$EXPECTED_IMAGE_SHA" \
 --expected-hef-sha256 "$EXPECTED_HEF_SHA" \
 --expected-engine-sha256 "$EXPECTED_ENGINE_SHA" \
 --expected-boundary-layout memory_nhwc_to_nchw \
 --work-dir "$OUT/work" \
 --result-json "$OUT/native_fifo_results.json"
RC=$?
set -e

if [[ -f "$OUT/native_fifo_results.json" ]]; then
  "$SYS_PY" - "$OUT/native_fifo_results.json" >"$OUT/concise_result.json" <<'PY'
import json,sys
p=json.load(open(sys.argv[1],encoding="utf-8"))
keys=[
"ok","schema","mode","failure_reason","performance_endpoint",
"application_performance_endpoint","endpoint_execution_policy",
"three_stage_concurrency_directly_measured","three_stage_hardware_integration_status",
"p2_output_contract_family","postprocess_adapter_id","postprocess_location",
"quality_oracle_location","quality_oracle_status","p2_output_fps",
"completed_detection_fps","completed_to_p2_ratio","endpoint_relation_verified",
"directly_measured","stage_timings","oracle_parity","phases"]
print(json.dumps({k:p.get(k) for k in keys},indent=2))
PY
  cat "$OUT/concise_result.json"
fi

if [[ "$RC" -eq 0 ]]; then
  "$SYS_PY" - "$OUT/native_fifo_results.json" <<'PY'
import json, sys
p=json.load(open(sys.argv[1],encoding="utf-8"))
required={
    "ok": True,
    "performance_endpoint": "p2_output",
    "application_performance_endpoint": "completed_detection",
    "endpoint_execution_policy": "concurrent_three_stage_single_invocation",
    "three_stage_concurrency_directly_measured": True,
    "three_stage_hardware_integration_status": "directly_measured",
    "p2_output_contract_family": "yolov7_anchor_multiscale_raw",
    "postprocess_adapter_id": "yolov7_anchor_multiscale_sparse",
    "quality_oracle_location": "outside_performance_timing",
}
for key,value in required.items():
    if p.get(key) != value:
        raise SystemExit(f"result contract mismatch: {key}={p.get(key)!r} expected={value!r}")
for key in ("p2_output_fps","completed_detection_fps","completed_to_p2_ratio"):
    value=p.get(key)
    if not isinstance(value,(int,float)) or value <= 0:
        raise SystemExit(f"missing positive metric: {key}={value!r}")
if p["p2_output_fps"] < 85.0 or p["completed_detection_fps"] < 85.0:
    raise SystemExit("concurrent endpoint throughput below conservative smoke floor")
if p["completed_to_p2_ratio"] < 0.90:
    raise SystemExit("completed/p2 ratio below smoke floor")
if not p.get("stage_timings"):
    raise SystemExit("stage_timings missing from canonical result")
if not p.get("oracle_parity"):
    raise SystemExit("oracle_parity missing from canonical result")
print("V2793_PRODUCT_RESULT_CONTRACT=PASS")
PY
fi

echo "RUNNER_RC=$RC"
exit "$RC"
REMOTE
REMOTE_RC=$?
set -e

REMOTE_ZIP="$(
 ssh -o BatchMode=yes -o ConnectTimeout=10 "$H8" \
 "find '$REMOTE_ROOT' -maxdepth 1 -type f -name 'v2794_yolov7_b066_product_normal_runner_*.zip' -printf '%T@ %p\n' | sort -nr | head -1 | cut -d' ' -f2-"
)"
if [[ -n "$REMOTE_ZIP" ]]; then
  scp -q "$H8:$REMOTE_ZIP" "$LOCAL_RESULT"
fi

echo
echo "============================================================"
echo " v2.79.4 PRODUCT SMOKE - RESULT"
echo "============================================================"
echo "SMOKE_RC=$REMOTE_RC"
echo "REMOTE_RESULT_ROOT=$REMOTE_ROOT"
echo "RESULT_ZIP=$LOCAL_RESULT"
if [[ -f "$LOCAL_RESULT" ]]; then
  echo "RESULT_ZIP_SHA256=$(sha256sum "$LOCAL_RESULT"|awk '{print $1}')"
else
  echo "RESULT_ZIP_MISSING=yes"
fi
exit "$REMOTE_RC"
