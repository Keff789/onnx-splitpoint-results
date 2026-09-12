# Hailo8 MobileNet: HAR-Zwischenstufen

Status: **diagnostic_evaluated**

| Stufe | Top-1 richtig | Top-5 richtig |
|---|---:|---:|
| cpu_hef | 8/16 | 14/16 |
| gpu_hef | 10/16 | 15/16 |
| source_float | 13/16 | 14/16 |
| build_float | 13/16 | 14/16 |
| parsed_native | 13/16 | 14/16 |
| quantized | 9/16 | 13/16 |

## Grenzen

Compare first material numerical deviation; no universal emulation/hardware bit-exactness claim. Only quantized.har of GPU build available; quantized_vs_cpu_hef is cross-build comparison.

original_build_report_paths; HAR fingerprints recorded NOW, not retrospectively attested at build time

Keine Neuoptimierung, kein HEF-Neubau, keine erneute Hailo-Hardwareausfuehrung. FLOAT32-NHWC-Eingaben wurden aus dem gebundenen Runtime-Dump uebernommen, nicht neu normalisiert.

## Numerische Vergleiche

| Vergleich | Maximaler Absolutfehler | RMS | Mittlere Logit-Cosine | Top-1-Wechsel |
|---|---:|---:|---:|---:|
| source_float_vs_build_float | 0 | 0 | 1.0 | 0 |
| build_float_vs_parsed_native | 9.7751617e-06 | 1.4686827e-06 | 0.99999999999879 | 0 |
| parsed_native_vs_quantized | 4.9191899 | 0.70196528 | 0.7218788257173849 | 5 |
| quantized_vs_gpu_hef | 2.394485 | 0.39264502 | 0.9044324734749283 | 4 |
| quantized_vs_cpu_hef | 3.3921856 | 0.40897667 | 0.8963005387817756 | 5 |
| cpu_hef_vs_gpu_hef | 2.1949432 | 0.34478825 | 0.9246922939013743 | 6 |
