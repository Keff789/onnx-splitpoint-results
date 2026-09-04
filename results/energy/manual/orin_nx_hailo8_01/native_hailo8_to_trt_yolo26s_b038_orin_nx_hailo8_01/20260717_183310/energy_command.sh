#!/usr/bin/env bash
set -euo pipefail
#!/usr/bin/env bash
set -euo pipefail
ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new nx@192.168.0.104 'source ~/hailo_py/bin/activate && cd /home/nx/ONNX-Splitpoint-Tool && python /home/nx/ONNX-Splitpoint-Tool/scripts/run_and_report_work_units.py -- python -u scripts/native_hailo_trt_fifo_from_benchmarkset.py --benchmark-set /home/nx/native_fifo_evalsets/resnet_yolo26s_20260717_171223/yolo26s/benchmark_set --case b038 --hw-arch hailo8 --precision uint8_dequant_fp16 --duration-s 60 --warmup 0 --queue-depth 3 --hailo-format uint8 --no-build'
