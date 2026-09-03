#!/usr/bin/env bash
set -u
timing_path=/home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/reports/window_method_validation_probe/attempts/20260827T095446_478761Z_97b44f361c9f/measurement/repeat_000/attempt_00/run_000/workload_timing.txt
start_ns=$(date +%s%N)
printf 'start_ns=%s
' "$start_ns" > "$timing_path"
set +e
/home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/reports/window_method_validation_probe/attempts/20260827T095446_478761Z_97b44f361c9f/measurement/repeat_000/attempt_00/run_000/workload_command.sh > /home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/reports/window_method_validation_probe/attempts/20260827T095446_478761Z_97b44f361c9f/measurement/repeat_000/attempt_00/run_000/workload_stdout.log 2> /home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/reports/window_method_validation_probe/attempts/20260827T095446_478761Z_97b44f361c9f/measurement/repeat_000/attempt_00/run_000/workload_stderr.log
rc=$?
set -e
end_ns=$(date +%s%N)
printf 'end_ns=%s
rc=%s
' "$end_ns" "$rc" >> "$timing_path"
exit "$rc"
