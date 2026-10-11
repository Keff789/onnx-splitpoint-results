#!/usr/bin/env python3
"""Structural/numerical verification of the public compact evidence.

This does not read raw NPY/Parquet channels and is not a hardware or calibration
verification.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


sources = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
assert sources["successful_control_review_v1_0_1"]["manifest_files_verified"] == 117
assert sources["successful_complementary_review_v1_0_2"]["manifest_files_verified"] == 117

fixed_qa = json.loads((ROOT / "fixed-window/data/QA.json").read_text(encoding="utf-8"))
assert fixed_qa["status"] == "PASS"
assert fixed_qa["reported_summary"]["checked"] == 225
assert fixed_qa["reported_summary"]["magnitude_exclusions"] == 0
assert fixed_qa["fixed_results_recomputed"] == 900

fixed = read_csv(ROOT / "fixed-window/data/main_summary.csv")
assert len(fixed) == 5
assert {row["workload"] for row in fixed} == {
    "gemm_fp16", "gemm_int8", "llm", "yolo_fp32", "yolo_int8"
}

qa = json.loads((ROOT / "complementary/data/QA.json").read_text(encoding="utf-8"))
assert qa["status"] == "PASS"
assert qa["completed_measured_runs"] == 12
assert qa["manifest_files_checked_total"] == 234
assert qa["complementary_at_every_position"] is True

runs = read_csv(ROOT / "complementary/data/combined_runs.csv")
assert len(runs) == 12
assert {int(row["TRT_queries"]) for row in runs} == {250}
assert sum(int(row["rate_Sps"]) == 2000 for row in runs) == 6
assert sum(int(row["rate_Sps"]) == 5_000_000 for row in runs) == 6

positions = read_csv(ROOT / "complementary/data/position_balance.csv")
assert len(positions) == 6
for row in positions:
    assert {int(row["v1.0.1_rate_Sps"]), int(row["v1.0.2_rate_Sps"])} == {2000, 5_000_000}

effects = {row["metric"]: row for row in read_csv(ROOT / "complementary/data/balanced_effects.csv")}
pico = effects["pico_load_20_80_mean_power_W"]
assert abs(float(pico["balanced_effect_percent_of_2kSps_mean"]) - (-0.06097609791226118)) < 1e-12
assert int(pico["n_2kSps"]) == 6 and int(pico["n_5MSps"]) == 6

print("PASS: fixed-window audit and complementary controlled-rate evidence")
print("Scope: compact public tables only; no raw-data/hardware verification")
