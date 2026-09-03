#!/usr/bin/env bash
set -Eeuo pipefail

# Read-only search for the previously documented Hailo-8 format A/B report.
DOWNLOADS_ROOT="${DOWNLOADS_ROOT:-$HOME/Downloads}"
MODELS_ROOT="${MODELS_ROOT:-$HOME/Models}"

declare -a roots=()
for path in \
  "$DOWNLOADS_ROOT" \
  "$MODELS_ROOT/EvaluationRuns" \
  "$MODELS_ROOT/EvaluationRunsAnalysis" \
  "$MODELS_ROOT/NativeFIFO"; do
  [[ -d "$path" ]] && roots+=("$path")
done

if [[ "${#roots[@]}" -eq 0 ]]; then
  echo "No search roots found." >&2
  exit 1
fi

echo "Searching filenames..."
find "${roots[@]}" -type f \
  \( -iname '*hailo8*ab*' -o -iname '*format*ab*' \
     -o -iname '*uint8*dequant*' \) -print 2>/dev/null || true

echo
echo "Searching text reports for known markers..."
if command -v rg >/dev/null 2>&1; then
  rg -l --no-messages \
    -g '*.json' -g '*.md' -g '*.txt' -g '*.log' \
    '146[.,]259|0[.,]147|uint8_cast_fp16|uint8_dequant_fp16' \
    "${roots[@]}" || true
else
  grep -RIlE --include='*.json' --include='*.md' --include='*.txt' \
    --include='*.log' \
    '146[.,]259|0[.,]147|uint8_cast_fp16|uint8_dequant_fp16' \
    "${roots[@]}" 2>/dev/null || true
fi

echo
echo "SEARCH_COMPLETE=PASS"

