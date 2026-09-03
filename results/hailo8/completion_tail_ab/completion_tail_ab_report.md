# Detection Completion-Tail A/B Canary v2

- Status: **PASS**
- Python: `/home/nx/hailo_py/bin/python`
- NumPy: `1.26.4`
- Raw heads per frame: **8.568 MB**
- Reference integrated completion tail: **47.663 ms**

## Endpoint variants

| Mode | Median ms | P95 ms | Saved vs full | Speedup | Parity |
|---|---:|---:|---:|---:|---|
| `full_attested_completion` | 47.7567 | 47.8631 | 0.0000 | 1.00× | exact |
| `full_attested_cached_raw_hash` | 39.8130 | 39.8894 | 7.9438 | 1.20× | exact |
| `task_completion_no_crypto` | 39.5641 | 39.6468 | 8.1927 | 1.21× | exact |
| `task_completion_prebound_no_crypto` | 38.4568 | 38.5689 | 9.3000 | 1.24× | exact |
| `frozen_processor_prebound_only` | 38.4707 | 38.5522 | 9.2860 | 1.24× | exact |

## Meaning

- `full_attested_completion` is the current v2.78.2 hot-loop contract.
- `full_attested_cached_raw_hash` isolates repeated raw-head SHA-256 cost.
- `task_completion_no_crypto` keeps decode/NMS/result semantics but moves cryptographic evidence out of the timed path.
- `task_completion_prebound_no_crypto` additionally binds fixed model/head geometry once.
- `frozen_processor_prebound_only` is the closest CPU-side decode/NMS/coordinate-projection cost.

The current Python implementation remains the oracle. All lighter modes must reproduce the same detections within the frozen tolerance.
