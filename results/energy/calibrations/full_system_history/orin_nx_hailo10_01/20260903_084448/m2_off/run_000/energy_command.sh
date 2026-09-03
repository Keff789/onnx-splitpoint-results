#!/usr/bin/env bash
set -u
timing_path=/home/kmika/Models/EnergyMeasurements/Calibrations/orin_nx_hailo10_01/20260903_084448/m2_off/run_000/workload_timing.txt
start_ns=$(date +%s%N)
printf 'start_ns=%s
' "$start_ns" > "$timing_path"
set +e
/home/kmika/Models/EnergyMeasurements/Calibrations/orin_nx_hailo10_01/20260903_084448/m2_off/run_000/workload_command.sh > /home/kmika/Models/EnergyMeasurements/Calibrations/orin_nx_hailo10_01/20260903_084448/m2_off/run_000/workload_stdout.log 2> /home/kmika/Models/EnergyMeasurements/Calibrations/orin_nx_hailo10_01/20260903_084448/m2_off/run_000/workload_stderr.log
rc=$?
set -e
end_ns=$(date +%s%N)
printf 'end_ns=%s
rc=%s
' "$end_ns" "$rc" >> "$timing_path"
exit "$rc"
