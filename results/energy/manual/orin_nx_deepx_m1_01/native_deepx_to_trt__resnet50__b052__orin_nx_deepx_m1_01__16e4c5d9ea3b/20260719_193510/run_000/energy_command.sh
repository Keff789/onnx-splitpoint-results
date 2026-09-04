#!/usr/bin/env bash
set -u
timing_path=/home/kmika/Models/EnergyMeasurements/Manual/orin_nx_deepx_m1_01/native_deepx_to_trt__resnet50__b052__orin_nx_deepx_m1_01__16e4c5d9ea3b/20260719_193510/run_000/workload_timing.txt
start_ns=$(date +%s%N)
printf 'start_ns=%s
' "$start_ns" > "$timing_path"
set +e
/home/kmika/Models/EnergyMeasurements/Manual/orin_nx_deepx_m1_01/native_deepx_to_trt__resnet50__b052__orin_nx_deepx_m1_01__16e4c5d9ea3b/20260719_193510/run_000/workload_command.sh > /home/kmika/Models/EnergyMeasurements/Manual/orin_nx_deepx_m1_01/native_deepx_to_trt__resnet50__b052__orin_nx_deepx_m1_01__16e4c5d9ea3b/20260719_193510/run_000/workload_stdout.log 2> /home/kmika/Models/EnergyMeasurements/Manual/orin_nx_deepx_m1_01/native_deepx_to_trt__resnet50__b052__orin_nx_deepx_m1_01__16e4c5d9ea3b/20260719_193510/run_000/workload_stderr.log
rc=$?
set -e
end_ns=$(date +%s%N)
printf 'end_ns=%s
rc=%s
' "$end_ns" "$rc" >> "$timing_path"
exit "$rc"
