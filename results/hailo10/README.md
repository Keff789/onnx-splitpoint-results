# Hailo-10 results

The two committed JSON files are real Hailo-10H hardware A/B microbenchmarks
for YOLO26s Part 1 (`b024`). They should remain unchanged as raw result records.

- `infermodel_output_format/`: compares FLOAT32 host output with HEF-native
  UINT8 output. It establishes transfer/latency effects, not a throughput win.
- `input_format/`: compares FLOAT32 host input with HEF-native UINT8 input. It
  shows exact device-equivalent values and the large single-job latency gain.
- `part1_hef_smoke/`: populated by the Smartmirror2 collector when the Hailo-10
  Jetson is reachable.

These results must not be presented as full pipeline FPS. The evaluated scope
ends at Hailo-10 Part 1; TensorRT Part 2 and the FIFO overlap are outside these
microbenchmarks.

