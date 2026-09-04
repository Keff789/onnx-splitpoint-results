#!/usr/bin/env bash
set -euo pipefail
#!/usr/bin/env bash
set -euo pipefail
ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new nx@192.168.0.104 'cd /home/nx/ONNX-Splitpoint-Tool && python scripts/native_hailo_trt_fifo_from_benchmarkset.py --benchmark-set /home/nx/yolov7_paper_benchmark_20260625_070717 --case b066 --hw-arch hailo8 --precision uint8_cast_fp16 --frames 5000 --warmup 200 --queue-depth 3 --hailo-format uint8  --no-build'
