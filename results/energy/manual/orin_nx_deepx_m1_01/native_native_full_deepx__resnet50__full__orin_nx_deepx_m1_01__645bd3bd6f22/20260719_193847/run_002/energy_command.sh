#!/usr/bin/env bash
set -u
timing_path=/home/kmika/Models/EnergyMeasurements/Manual/orin_nx_deepx_m1_01/native_native_full_deepx__resnet50__full__orin_nx_deepx_m1_01__645bd3bd6f22/20260719_193847/run_002/workload_timing.txt
start_ns=$(date +%s%N)
printf 'start_ns=%s
' "$start_ns" > "$timing_path"
set +e
/home/kmika/Models/EnergyMeasurements/Manual/orin_nx_deepx_m1_01/native_native_full_deepx__resnet50__full__orin_nx_deepx_m1_01__645bd3bd6f22/20260719_193847/run_002/workload_command.sh > /home/kmika/Models/EnergyMeasurements/Manual/orin_nx_deepx_m1_01/native_native_full_deepx__resnet50__full__orin_nx_deepx_m1_01__645bd3bd6f22/20260719_193847/run_002/workload_stdout.log 2> /home/kmika/Models/EnergyMeasurements/Manual/orin_nx_deepx_m1_01/native_native_full_deepx__resnet50__full__orin_nx_deepx_m1_01__645bd3bd6f22/20260719_193847/run_002/workload_stderr.log
rc=$?
set -e
end_ns=$(date +%s%N)
printf 'end_ns=%s
rc=%s
' "$end_ns" "$rc" >> "$timing_path"
exit "$rc"
