#!/usr/bin/env bash
set -Eeuo pipefail

usage() {
  cat <<'EOF'
Usage:
  collect_from_smartmirror2.sh --scan
  collect_from_smartmirror2.sh --collect
  collect_from_smartmirror2.sh --collect --full-local-archive

--scan                Read-only existence and size report.
--collect             Copy curated Git files and existing compressed evidence.
--full-local-archive  Additionally copy selected irreplaceable raw measurement
                      and evaluation directories. Consider another disk/NAS.

Environment overrides:
  DOWNLOADS_ROOT  default: $HOME/Downloads
  MODELS_ROOT     default: $HOME/Models
  ARCHIVE_ROOT    default: $HOME/ONNX-Splitpoint-Results-Archive
  HAILO10_HOST    default: nx@192.168.0.145
EOF
}

MODE="${1:-}"
FULL_ARCHIVE=false
if [[ "$MODE" != "--scan" && "$MODE" != "--collect" ]]; then
  usage
  exit 2
fi
if [[ "${2:-}" == "--full-local-archive" ]]; then
  FULL_ARCHIVE=true
elif [[ -n "${2:-}" ]]; then
  usage
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DOWNLOADS_ROOT="${DOWNLOADS_ROOT:-$HOME/Downloads}"
MODELS_ROOT="${MODELS_ROOT:-$HOME/Models}"
ARCHIVE_ROOT="${ARCHIVE_ROOT:-$HOME/ONNX-Splitpoint-Results-Archive}"
HAILO10_HOST="${HAILO10_HOST:-nx@192.168.0.145}"

if [[ ! -f "$REPO_ROOT/README.md" || ! -f "$REPO_ROOT/.gitignore" ]]; then
  echo "ERROR: repository starter root was not detected: $REPO_ROOT" >&2
  exit 1
fi
if [[ "$REPO_ROOT" == "$DOWNLOADS_ROOT" || "$REPO_ROOT" == "$MODELS_ROOT" ]]; then
  echo "ERROR: repository destination must not equal a source root" >&2
  exit 1
fi

declare -a LARGE_CANDIDATES=(
  "$MODELS_ROOT/EnergyMeasurements"
  "$MODELS_ROOT/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251"
  "$MODELS_ROOT/EvaluationRuns/paper_comparison_resnet50_hailo8_full_native_energy_b500_20260827_105134"
  "$MODELS_ROOT/EvaluationRuns/v2784_7model_b500_audit20_launch_20260828_194905_185725341_1413672"
  "$MODELS_ROOT/EvaluationRuns/biggerset_20260903_090110"
)

scan_sources() {
  local path bytes
  printf 'status\tbytes\tpath\n'
  for path in "${LARGE_CANDIDATES[@]}"; do
    if [[ -e "$path" ]]; then
      bytes="$(du -sb -- "$path" | cut -f1)"
      printf 'present\t%s\t%s\n' "$bytes" "$path"
    else
      printf 'missing\t0\t%s\n' "$path"
    fi
  done

  for path in \
    "$DOWNLOADS_ROOT/hailo10_infermodel_format_ab_20260903_122158.json" \
    "$DOWNLOADS_ROOT/hailo10_input_format_ab_20260903_131242.json" \
    "$DOWNLOADS_ROOT/v2794_yolov7_b066_product_normal_runner_20260901_092235.zip" \
    "$DOWNLOADS_ROOT/v2796_yolov7_b066_claim_gate_32_20260901_130453.zip" \
    "$DOWNLOADS_ROOT/v2784_seven_model_final_evidence_20260831_103034.zip" \
    "$DOWNLOADS_ROOT/biggerset_20260903_090110_debug_pack.zip" \
    "$DOWNLOADS_ROOT/v27916_install_acceptance_20260903_154343_058884999_781004.zip"; do
    if [[ -f "$path" ]]; then
      printf 'present\t%s\t%s\n' "$(stat -c %s -- "$path")" "$path"
    else
      printf 'missing\t0\t%s\n' "$path"
    fi
  done
}

if [[ "$MODE" == "--scan" ]]; then
  scan_sources
  echo
  echo "SCAN_ONLY=PASS"
  exit 0
fi

mkdir -p \
  "$REPO_ROOT/inventory" \
  "$REPO_ROOT/experiments/hailo10" \
  "$REPO_ROOT/experiments/hailo8" \
  "$REPO_ROOT/results/hailo10/infermodel_output_format" \
  "$REPO_ROOT/results/hailo10/input_format" \
  "$REPO_ROOT/results/hailo10/part1_hef_smoke" \
  "$REPO_ROOT/results/hailo8" \
  "$REPO_ROOT/results/paper" \
  "$REPO_ROOT/results/energy/calibrations" \
  "$REPO_ROOT/results/evaluation" \
  "$REPO_ROOT/results/acceptance/v2.79.16" \
  "$REPO_ROOT/diagnostics/biggerset_20260903_090110" \
  "$ARCHIVE_ROOT/ab-tests" \
  "$ARCHIVE_ROOT/acceptance" \
  "$ARCHIVE_ROOT/debug" \
  "$ARCHIVE_ROOT/energy" \
  "$ARCHIVE_ROOT/evaluation" \
  "$ARCHIVE_ROOT/releases"

MISSING_FILE="$REPO_ROOT/inventory/missing_sources.txt"
: > "$MISSING_FILE"

missing() {
  printf '%s\n' "$1" >> "$MISSING_FILE"
  printf 'MISSING %s\n' "$1" >&2
}

copy_file() {
  local src="$1" dst="$2"
  if [[ ! -f "$src" ]]; then
    missing "$src"
    return 0
  fi
  mkdir -p "$dst"
  rsync -a -- "$src" "$dst/"
}

copy_tree_text() {
  local src="$1" dst="$2"
  if [[ ! -d "$src" ]]; then
    missing "$src"
    return 0
  fi
  mkdir -p "$dst"
  rsync -a --prune-empty-dirs \
    --include='*/' \
    --include='*.json' --include='*.md' --include='*.csv' \
    --include='*.tsv' --include='*.txt' --include='*.yaml' \
    --include='*.yml' --include='*.py' --include='*.sh' \
    --exclude='*' \
    "$src/" "$dst/"
}

copy_archive() {
  local src="$1" dst="$2"
  if [[ ! -f "$src" ]]; then
    missing "$src"
    return 0
  fi
  mkdir -p "$dst"
  rsync -a -- "$src" "$dst/"
}

# Hailo-10 A/B results and their exact experiment scripts.
copy_file "$DOWNLOADS_ROOT/hailo10_infermodel_format_ab_20260903_122158.json" \
  "$REPO_ROOT/results/hailo10/infermodel_output_format"
copy_tree_text "$DOWNLOADS_ROOT/hailo10_ab" \
  "$REPO_ROOT/experiments/hailo10/infermodel_output_format"
copy_file "$DOWNLOADS_ROOT/hailo10_input_format_ab_20260903_131242.json" \
  "$REPO_ROOT/results/hailo10/input_format"
copy_tree_text "$DOWNLOADS_ROOT/hailo10_input_ab" \
  "$REPO_ROOT/experiments/hailo10/input_format"

copy_archive "$DOWNLOADS_ROOT/ONNX_Splitpoint_Hailo10H_UINT8_Input_AB_Test_2026-09-03.zip" \
  "$ARCHIVE_ROOT/ab-tests"
copy_archive "$DOWNLOADS_ROOT/ONNX_Splitpoint_v2.79.14_Akutbefunde_und_Hailo10_AB_Test_2026-09-03.zip" \
  "$ARCHIVE_ROOT/ab-tests"

# Current real Hailo-10 HEF Part-1 smoke, if the target is reachable.
H10_REMOTE_REPORT="/home/nx/v27916_hailo10_uint8_hef_smoke/report.json"
if ssh -o BatchMode=yes -o ConnectTimeout=5 "$HAILO10_HOST" \
    "test -f '$H10_REMOTE_REPORT'" 2>/dev/null; then
  rsync -a -e 'ssh -o BatchMode=yes -o ConnectTimeout=5' -- \
    "$HAILO10_HOST:$H10_REMOTE_REPORT" \
    "$REPO_ROOT/results/hailo10/part1_hef_smoke/"
  rsync -a -- "$REPO_ROOT/results/hailo10/part1_hef_smoke/report.json" \
    "$ARCHIVE_ROOT/ab-tests/"
else
  missing "$HAILO10_HOST:$H10_REMOTE_REPORT"
fi

# Hailo-8 compact A/B, fast-decode, multi-image and three-stage reports.
copy_tree_text \
  "$DOWNLOADS_ROOT/native_completion_tail_canary_results/completion_tail_v2_20260828_082714" \
  "$REPO_ROOT/results/hailo8/completion_tail_ab"
copy_tree_text \
  "$DOWNLOADS_ROOT/native_completion_tail_fast_decode_results/fast_decode_v1_20260828_093339" \
  "$REPO_ROOT/results/hailo8/fast_decode"
copy_tree_text \
  "$DOWNLOADS_ROOT/native_yolov7_multi_image_fast_decode_results/yolov7_multi_image_fast_decode_v1_20260828_101748" \
  "$REPO_ROOT/results/hailo8/multi_image_fast_decode"
copy_tree_text \
  "$DOWNLOADS_ROOT/native_yolov7_three_stage_results/yolov7_three_stage_v1_20260828_120045" \
  "$REPO_ROOT/results/hailo8/three_stage"
copy_tree_text "$DOWNLOADS_ROOT/v2794_yolov7_b066_product_normal_runner_smoke" \
  "$REPO_ROOT/experiments/hailo8/product_normal_runner"
copy_tree_text "$DOWNLOADS_ROOT/v2796_yolov7_b066_claim_gate_32_20260901_130453/evidence" \
  "$REPO_ROOT/results/hailo8/claim_gate_32_v2796"
copy_tree_text "$DOWNLOADS_ROOT/v2797_retained_yolov7_claim_20260901_200915_1323297/evidence" \
  "$REPO_ROOT/results/hailo8/claim_gate_32_retained_v2797"

for archive in \
  native_completion_tail_canary_results/completion_tail_v2_20260828_082714.zip \
  native_completion_tail_fast_decode_results/fast_decode_v1_20260828_093339.zip \
  native_yolov7_multi_image_fast_decode_results/yolov7_multi_image_fast_decode_v1_20260828_101748.zip \
  native_yolov7_three_stage_results/yolov7_three_stage_v1_20260828_120045.zip \
  v2794_yolov7_b066_product_normal_runner_20260901_092235.zip \
  v2796_yolov7_b066_claim_gate_32_20260901_130453.zip; do
  copy_archive "$DOWNLOADS_ROOT/$archive" "$ARCHIVE_ROOT/evaluation"
done

# Historical energy/calibration evidence.
copy_file "$DOWNLOADS_ROOT/m2_idle_power_calibration_deepx.json" \
  "$REPO_ROOT/results/energy/calibrations"
copy_file "$DOWNLOADS_ROOT/m2_idle_power_calibration_hailo10.json" \
  "$REPO_ROOT/results/energy/calibrations"
copy_file "$DOWNLOADS_ROOT/m2_idle_power_calibration_Hailo8.json" \
  "$REPO_ROOT/results/energy/calibrations"
copy_archive "$DOWNLOADS_ROOT/m2_idle_power_calibration_deepx.json" \
  "$ARCHIVE_ROOT/energy"
copy_archive "$DOWNLOADS_ROOT/m2_idle_power_calibration_hailo10.json" \
  "$ARCHIVE_ROOT/energy"
copy_archive "$DOWNLOADS_ROOT/m2_idle_power_calibration_Hailo8.json" \
  "$ARCHIVE_ROOT/energy"
copy_tree_text "$MODELS_ROOT/EnergyMeasurements/Calibrations" \
  "$REPO_ROOT/results/energy/calibrations/full_system_history"

# Compact paper-run reports and their top-level execution contracts.
for run in \
  paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251 \
  paper_comparison_resnet50_hailo8_full_native_energy_b500_20260827_105134; do
  RUN_SRC="$MODELS_ROOT/EvaluationRuns/$run"
  RUN_DST="$REPO_ROOT/results/paper/$run"
  copy_tree_text "$RUN_SRC/reports" "$RUN_DST/reports"
  for name in artifact_index.json dataset_registry_binding.json \
    effective_execution_plan.json effective_execution_plan.md \
    hardware_matrix.json profile_resolution.json profile_source.yaml \
    profile_start_snapshot.json profile.yaml run_manifest.json; do
    [[ -f "$RUN_SRC/$name" ]] && copy_file "$RUN_SRC/$name" "$RUN_DST"
  done
done

# Seven-model reconciliation and compact failed-run diagnostic.
copy_tree_text "$MODELS_ROOT/EvaluationRunsAnalysis/v2784_7model_evidence_reconciliation_v2" \
  "$REPO_ROOT/results/evaluation/v2784_7model_reconciliation_v2"
copy_archive "$DOWNLOADS_ROOT/v2784_seven_model_final_evidence_20260831_103034.zip" \
  "$ARCHIVE_ROOT/evaluation"
copy_archive "$DOWNLOADS_ROOT/v2784_evidence_reconciliation_v2_bundle.zip" \
  "$ARCHIVE_ROOT/evaluation"

BIG="$DOWNLOADS_ROOT/biggerset_20260903_090110_debug_pack"
for rel in \
  artifact_index.json debug_pack_manifest.json effective_execution_plan.json \
  hardware_matrix.json pack_source_identity.json profile_resolution.json \
  run_manifest.json campaign/campaign_readiness.json \
  campaign/campaign_readiness.md campaign/native_preflight_asset_contract.json \
  jobs/job_plan.json jobs/job_summary.json jobs/job_timeline.md \
  jobs/workflow_control.json reports/run_status_summary.json \
  reports/results_bundle_manifest.json reports/report_manifest.json; do
  if [[ -f "$BIG/$rel" ]]; then
    mkdir -p "$REPO_ROOT/diagnostics/biggerset_20260903_090110/$(dirname "$rel")"
    rsync -a -- "$BIG/$rel" \
      "$REPO_ROOT/diagnostics/biggerset_20260903_090110/$rel"
  fi
done
copy_archive "$DOWNLOADS_ROOT/biggerset_20260903_090110_debug_pack.zip" \
  "$ARCHIVE_ROOT/debug"
copy_archive "$DOWNLOADS_ROOT/biggerset_20260903_090110_debug_pack.zip.manifest.json" \
  "$ARCHIVE_ROOT/debug"

# v2.79.16 installed acceptance: compact Git subset plus full compressed copy.
ACC="$DOWNLOADS_ROOT/v27916_install_acceptance_20260903_154343_058884999_781004"
for name in installed_identity.txt v27916_small_acceptance.json \
  dedicated_acceptance.log full_console.log SHA256SUMS.txt source_zip_test.txt; do
  [[ -f "$ACC/$name" ]] && copy_file "$ACC/$name" \
    "$REPO_ROOT/results/acceptance/v2.79.16"
done
copy_archive "$DOWNLOADS_ROOT/v27916_install_acceptance_20260903_154343_058884999_781004.zip" \
  "$ARCHIVE_ROOT/acceptance"
copy_archive "$DOWNLOADS_ROOT/ONNX-Splitpoint-Tool_v2.79.16_COMPLETE_DELIVERY_BUNDLE_UPDATED.zip" \
  "$ARCHIVE_ROOT/releases"

# Full raw directories are explicit because they can be large.
if [[ "$FULL_ARCHIVE" == true ]]; then
  mkdir -p "$ARCHIVE_ROOT/full-runs" "$ARCHIVE_ROOT/energy-measurements"
  [[ -d "$MODELS_ROOT/EnergyMeasurements" ]] && \
    rsync -a "$MODELS_ROOT/EnergyMeasurements/" \
      "$ARCHIVE_ROOT/energy-measurements/"
  for run in \
    paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251 \
    paper_comparison_resnet50_hailo8_full_native_energy_b500_20260827_105134 \
    v2784_7model_b500_audit20_launch_20260828_194905_185725341_1413672 \
    biggerset_20260903_090110; do
    if [[ -d "$MODELS_ROOT/EvaluationRuns/$run" ]]; then
      mkdir -p "$ARCHIVE_ROOT/full-runs/$run"
      rsync -a "$MODELS_ROOT/EvaluationRuns/$run/" \
        "$ARCHIVE_ROOT/full-runs/$run/"
    else
      missing "$MODELS_ROOT/EvaluationRuns/$run"
    fi
  done
fi

# Plain inventories: path, size and mtime only. No new hash/seal layer.
scan_sources > "$REPO_ROOT/inventory/source_candidates.tsv"
find "$REPO_ROOT" -path "$REPO_ROOT/.git" -prune -o -type f \
  -printf '%P\t%s\t%TY-%Tm-%TdT%TH:%TM:%TS%Tz\n' | sort \
  > "$REPO_ROOT/inventory/collected_files.tsv"

if [[ ! -s "$MISSING_FILE" ]]; then
  printf 'none\n' > "$MISSING_FILE"
  COLLECTION_STATUS="PASS"
else
  COLLECTION_STATUS="PASS_WITH_MISSING"
fi

echo "COLLECTION=$COLLECTION_STATUS"
echo "REPO_ROOT=$REPO_ROOT"
echo "RAW_ARCHIVE=$ARCHIVE_ROOT"
echo "MISSING_LIST=$MISSING_FILE"
echo "NEXT=python3 scripts/check_before_commit.py ."
