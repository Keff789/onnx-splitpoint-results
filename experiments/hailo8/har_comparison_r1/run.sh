#!/usr/bin/env bash
set -Eeuo pipefail
HERE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
TOOL="${ONNX_SPLITPOINT_TOOL_DIR:-$HOME/ONNX-Splitpoint-Tool}"
PY="$TOOL/.venv/bin/python"
[[ -x "$PY" ]] || { printf 'STOP: Tool-Python fehlt: %s\n' "$PY"; exit 2; }
export PYTHONDONTWRITEBYTECODE=1
exec "$PY" -I -B "$HERE/run_har_and_git.py" "$@"
