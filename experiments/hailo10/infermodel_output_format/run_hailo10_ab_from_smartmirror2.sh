#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
LOCAL_TEST="$SCRIPT_DIR/hailo10_infermodel_format_ab.py"

H10_TARGET="${H10_TARGET:-nx@192.168.0.145}"
AB_WARMUP="${AB_WARMUP:-10}"
AB_LATENCY_FRAMES="${AB_LATENCY_FRAMES:-50}"
AB_THROUGHPUT_FRAMES="${AB_THROUGHPUT_FRAMES:-200}"
AB_INFLIGHT="${AB_INFLIGHT:-2}"
AB_TIMEOUT_MS="${AB_TIMEOUT_MS:-10000}"
REQUESTED_HEF="${1:-__AUTO__}"

STAMP="$(date -u +%Y%m%d_%H%M%S)"
REMOTE_TEST="/tmp/hailo10_infermodel_format_ab_${STAMP}.py"
REMOTE_RESULT="/tmp/hailo10_infermodel_format_ab_${STAMP}.json"
LOCAL_RESULT="$HOME/Downloads/hailo10_infermodel_format_ab_${STAMP}.json"

test -f "$LOCAL_TEST" || {
  echo "STOP: test script missing: $LOCAL_TEST" >&2
  exit 2
}

for value_name in AB_WARMUP AB_LATENCY_FRAMES AB_THROUGHPUT_FRAMES AB_INFLIGHT AB_TIMEOUT_MS; do
  value="${!value_name}"
  [[ "$value" =~ ^[0-9]+$ ]] || {
    echo "STOP: $value_name must be an integer, got: $value" >&2
    exit 2
  }
done

mkdir -p "$HOME/Downloads"

echo "Hailo-10H target: $H10_TARGET"
echo "Copying isolated A/B test..."
scp -q "$LOCAL_TEST" "$H10_TARGET:$REMOTE_TEST"

set +e
ssh "$H10_TARGET" bash -s -- \
  "$REMOTE_TEST" \
  "$REMOTE_RESULT" \
  "$REQUESTED_HEF" \
  "$AB_WARMUP" \
  "$AB_LATENCY_FRAMES" \
  "$AB_THROUGHPUT_FRAMES" \
  "$AB_INFLIGHT" \
  "$AB_TIMEOUT_MS" <<'REMOTE'
set -Eeuo pipefail

TEST_SCRIPT="$1"
RESULT_JSON="$2"
REQUESTED_HEF="$3"
WARMUP="$4"
LATENCY_FRAMES="$5"
THROUGHPUT_FRAMES="$6"
INFLIGHT="$7"
TIMEOUT_MS="$8"
PYTHON="$HOME/venvs/hailo10/bin/python"

test -x "$PYTHON" || {
  echo "STOP: Hailo-10 Python missing: $PYTHON" >&2
  exit 3
}

if [[ "$REQUESTED_HEF" != "__AUTO__" ]]; then
  HEF="$REQUESTED_HEF"
else
  HEF="$({
    find "$HOME/splitpoint_runs/_onnx_splitpoint_cache" "$HOME/splitpoint_runs/legacy_suite" \
      -type f \
      \( -name 'part1.hef' -o -name 'compiled.hef' \) \
      -path '*yolo26s*' \
      -path '*b024*' \
      -path '*hailo10*' \
      -printf '%T@ %p\n' 2>/dev/null || true
  } | sort -nr | sed -n '1p' | cut -d' ' -f2-)"
fi

if [[ -z "$HEF" || ! -f "$HEF" ]]; then
  echo "STOP: no yolo26s/b024 Hailo-10 Part1 HEF found." >&2
  echo "Recent Hailo-10 HEF candidates:" >&2
  find "$HOME/splitpoint_runs" -type f \( -name 'part1.hef' -o -name 'compiled.hef' \) \
    -path '*hailo10*' -printf '%T@ %p\n' 2>/dev/null \
    | sort -nr | sed -n '1,10p' | cut -d' ' -f2- >&2 || true
  exit 4
fi

echo "Python: $PYTHON"
echo "HEF: $HEF"
echo "A/B: FLOAT32 output vs native HEF output"

"$PYTHON" "$TEST_SCRIPT" \
  --hef "$HEF" \
  --output "$RESULT_JSON" \
  --warmup "$WARMUP" \
  --latency-frames "$LATENCY_FRAMES" \
  --throughput-frames "$THROUGHPUT_FRAMES" \
  --inflight "$INFLIGHT" \
  --timeout-ms "$TIMEOUT_MS"
REMOTE
REMOTE_RC=$?
set -e

if ssh "$H10_TARGET" "test -f '$REMOTE_RESULT'"; then
  scp -q "$H10_TARGET:$REMOTE_RESULT" "$LOCAL_RESULT"
  echo "RESULT_JSON=$LOCAL_RESULT"
else
  echo "STOP: remote test produced no result JSON" >&2
fi

if (( REMOTE_RC != 0 )); then
  echo "A/B test ended with remote exit code $REMOTE_RC; inspect the JSON/error above." >&2
fi
exit "$REMOTE_RC"
