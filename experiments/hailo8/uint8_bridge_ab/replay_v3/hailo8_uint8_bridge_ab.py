#!/usr/bin/env python3
"""Serial Hailo-8 UINT8 cast-vs-dequant performance A/B harness.

The launcher builds both engines beforehand in a timestamped minimal overlay.
This helper then reuses the installed tool's C++ runtime source while bypassing
the larger workflow layer.  It does not mutate the preserved cache and makes no
quality-equivalence claim.
"""

from __future__ import annotations

import argparse
import ast
import csv
import fcntl
import json
import math
import os
from pathlib import Path
import platform
import shutil
import statistics
import subprocess
import sys
import time
from typing import Any


CAST = "uint8_cast_fp16"
DEQUANT = "uint8_dequant_fp16"
MODES = (CAST, DEQUANT)
EXPECTED_IMAGE_REL = Path(
    "resources/validation/detection/val2017_n500_s20260710/000000000632.jpg"
)


class HarnessError(RuntimeError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise HarnessError(f"invalid JSON: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise HarnessError(f"JSON root is not an object: {path}")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=False, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def require_file(path: Path, label: str) -> Path:
    path = path.expanduser().resolve()
    if not path.is_file():
        raise HarnessError(f"{label} missing: {path}")
    return path


def find_hef(root: Path, case: str) -> Path:
    candidates = [
        root / case / "hailo" / "hailo8" / "part1" / "compiled.hef",
        root / case / "hailo" / "hailo8" / "part1" / f"{case}_part1.hef",
        root / case / "hailo" / "hailo8" / "part1" / "hailo8.hef",
    ]
    candidates.extend(sorted((root / case).glob("**/hailo8/part1/**/*.hef")))
    candidates.extend(sorted((root / case).glob("**/part1/**/*.hef")))
    for path in candidates:
        if path.is_file():
            return path.resolve()
    raise HarnessError(f"Hailo-8 Part1 HEF missing below {root / case}")


def find_engine(root: Path, case: str, mode: str) -> Path:
    expected_name = f"part2_{mode}.engine"
    candidates = [
        root / "native_trt" / case / "part2" / mode / expected_name,
        root / case / "native_trt" / "part2" / mode / expected_name,
    ]
    candidates.extend(
        sorted((root / "native_trt" / case / "part2" / mode).glob("*.engine"))
    )
    candidates.extend(
        sorted((root / case / "native_trt" / "part2" / mode).glob("*.engine"))
    )
    for path in candidates:
        if path.is_file():
            return path.resolve()
    raise HarnessError(
        f"freshly built {mode} engine missing in isolated overlay {root}; "
        "inspect the corresponding build report and log"
    )


def find_image(root: Path, explicit: str) -> Path:
    if explicit:
        return require_file(Path(explicit), "input image")
    exact = root / EXPECTED_IMAGE_REL
    if exact.is_file():
        return exact.resolve()
    suffixes = {".jpg", ".jpeg", ".png", ".bmp"}
    validation = root / "resources" / "validation"
    if validation.is_dir():
        for path in sorted(validation.rglob("*")):
            if path.is_file() and path.suffix.lower() in suffixes:
                return path.resolve()
    raise HarnessError(
        f"validation image missing (expected {exact}); pass --image explicitly"
    )


def validate_bridge_meta(
    mode: str,
    meta_path: Path,
    *,
    expected_scale: float | None,
    expected_zero_point: float | None,
    expected_layout: str | None,
) -> dict[str, Any]:
    meta = load_json(meta_path)
    for key, expected in (
        ("case", "b038"),
        ("variant", "part2"),
        ("precision", mode),
        ("build_ok", True),
    ):
        if meta.get(key) != expected:
            raise HarnessError(
                f"{mode} metadata mismatch for {key}: "
                f"{meta.get(key)!r} != {expected!r}"
            )
    if str(meta.get("precision") or "") != mode:
        raise HarnessError(
            f"{mode} metadata precision mismatch in {meta_path}: "
            f"{meta.get('precision')!r}"
        )
    bridge = meta.get("uint8_cast_bridge")
    if not isinstance(bridge, dict):
        raise HarnessError(f"{mode} bridge metadata missing in {meta_path}")
    expected_schema = (
        "onnx-splitpoint/uint8-cast-bridge"
        if mode == CAST
        else "onnx-splitpoint/uint8-dequant-bridge"
    )
    if bridge.get("schema") != expected_schema:
        raise HarnessError(
            f"{mode} bridge schema mismatch: {bridge.get('schema')!r}; "
            f"expected {expected_schema!r}"
        )
    if str(bridge.get("input_dtype") or "").upper() != "UINT8":
        raise HarnessError(f"{mode} bridge input is not UINT8")
    inputs = meta.get("inputs")
    if not isinstance(inputs, list) or len(inputs) != 1:
        raise HarnessError(f"{mode} metadata does not describe one TensorRT input")
    input_spec = inputs[0] if isinstance(inputs[0], dict) else {}
    if str(input_spec.get("elem_type") or "").upper() != "UINT8":
        raise HarnessError(f"{mode} TensorRT build metadata input is not UINT8")
    if mode == DEQUANT:
        scale = float(bridge.get("scale"))
        zero_point = float(bridge.get("zero_point"))
        layout = bridge.get("boundary_layout")
        layout = layout if isinstance(layout, dict) else {}
        if expected_scale is not None and not math.isclose(
            scale, expected_scale, rel_tol=0.0, abs_tol=1e-12
        ):
            raise HarnessError(
                f"dequant scale mismatch: {scale}; expected {expected_scale}"
            )
        if expected_zero_point is not None and not math.isclose(
            zero_point, expected_zero_point, rel_tol=0.0, abs_tol=1e-12
        ):
            raise HarnessError(
                "dequant zero point mismatch: "
                f"{zero_point}; expected {expected_zero_point}"
            )
        if (
            expected_layout is not None
            and (
                layout.get("effective") != expected_layout
                or layout.get("applied") is not True
            )
        ):
            raise HarnessError(
                "dequant boundary layout is not the expected applied "
                f"{expected_layout}: {layout!r}"
            )
    return meta


def resolve_artifacts(args: argparse.Namespace) -> dict[str, Any]:
    root = Path(args.benchmark_set).expanduser().resolve()
    if not root.is_dir():
        raise HarnessError(f"BenchmarkSet missing: {root}")
    if not args.minimal_overlay:
        require_file(root / "benchmark_set.json", "benchmark_set.json")
        require_file(root / args.case / "split_manifest.json", "split manifest")
    else:
        require_file(
            root / args.case / "source_part2.onnx",
            "minimal-overlay source Part2 ONNX",
        )
    hef = find_hef(root, args.case)
    image = find_image(root, args.image)
    engines: dict[str, Path] = {}
    metas: dict[str, Path] = {}
    meta_payloads: dict[str, dict[str, Any]] = {}
    for mode in MODES:
        engine = find_engine(root, args.case, mode)
        meta_path = require_file(engine.parent / "native_trt_meta.json", f"{mode} metadata")
        engines[mode] = engine
        metas[mode] = meta_path
        meta_payloads[mode] = validate_bridge_meta(
            mode,
            meta_path,
            expected_scale=args.expected_dequant_scale,
            expected_zero_point=args.expected_dequant_zero_point,
            expected_layout=args.expected_layout,
        )
        meta_engine = Path(str(meta_payloads[mode].get("engine") or "")).expanduser()
        if not meta_engine.is_absolute():
            meta_engine = meta_path.parent / meta_engine
        if meta_engine.resolve() != engine:
            raise HarnessError(
                f"{mode} metadata identifies a different engine: {meta_engine}"
            )
        bridge = meta_payloads[mode]["uint8_cast_bridge"]
        bridge_path = Path(str(bridge.get("bridge") or "")).expanduser()
        if not bridge_path.is_absolute():
            bridge_path = meta_path.parent / bridge_path
        bridge_path = require_file(bridge_path, f"{mode} bridge ONNX")
        meta_onnx = Path(str(meta_payloads[mode].get("onnx") or "")).expanduser()
        if not meta_onnx.is_absolute():
            meta_onnx = meta_path.parent / meta_onnx
        if meta_onnx.resolve() != bridge_path:
            raise HarnessError(f"{mode} metadata bridge ONNX identity mismatch")
        receipt = meta_payloads[mode].get("engine_build_receipt")
        if not isinstance(receipt, dict) or receipt.get("build_returncode") != 0:
            raise HarnessError(f"{mode} successful engine build receipt missing")
        receipt_engine = Path(str(receipt.get("engine") or "")).expanduser()
        receipt_source = Path(str(receipt.get("source_onnx") or "")).expanduser()
        if receipt_engine.resolve() != engine or receipt_source.resolve() != bridge_path:
            raise HarnessError(f"{mode} engine build receipt path mismatch")

    cast_bridge = meta_payloads[CAST]["uint8_cast_bridge"]
    dequant_bridge = meta_payloads[DEQUANT]["uint8_cast_bridge"]
    cast_source = str(cast_bridge.get("source") or "")
    dequant_source = str(dequant_bridge.get("source") or "")
    if not cast_source or not dequant_source:
        raise HarnessError(
            "cast or dequant metadata does not identify its source Part2 ONNX: "
            f"cast={cast_source!r}, dequant={dequant_source!r}"
        )
    cast_source_path = Path(cast_source).expanduser()
    dequant_source_path = Path(dequant_source).expanduser()
    if not cast_source_path.is_absolute():
        cast_source_path = root / cast_source_path
    if not dequant_source_path.is_absolute():
        dequant_source_path = root / dequant_source_path
    cast_source_path = require_file(cast_source_path, "cast source Part2 ONNX")
    dequant_source_path = require_file(dequant_source_path, "dequant source Part2 ONNX")
    if cast_source_path != dequant_source_path:
        raise HarnessError(
            "cast and dequant engines do not identify the same source Part2 ONNX: "
            f"cast={cast_source_path}, dequant={dequant_source_path}"
        )
    cast_source_identity = str(cast_bridge.get("source_sha256") or "")
    dequant_source_identity = str(dequant_bridge.get("source_sha256") or "")
    if (
        not cast_source_identity
        or cast_source_identity != dequant_source_identity
    ):
        raise HarnessError(
            "fresh cast and dequant bridge metadata do not carry the same "
            "existing source identity"
        )
    if meta_payloads[CAST].get("outputs") != meta_payloads[DEQUANT].get("outputs"):
        raise HarnessError("cast and dequant TensorRT output contracts differ")
    cast_inputs = meta_payloads[CAST]["inputs"]
    dequant_inputs = meta_payloads[DEQUANT]["inputs"]
    if cast_inputs != dequant_inputs:
        raise HarnessError("cast and dequant TensorRT input contracts differ")
    if os.path.samefile(engines[CAST], engines[DEQUANT]):
        raise HarnessError("cast and dequant unexpectedly resolve to the same engine")

    return {
        "benchmark_set": root,
        "hef": hef,
        "image": image,
        "engines": engines,
        "metas": metas,
        "meta_payloads": meta_payloads,
        "source_part2": cast_source_path,
    }


def extract_runtime_sources(runner_source: Path) -> tuple[str, str]:
    text = require_file(runner_source, "v2.79 Hailo runner source").read_text(
        encoding="utf-8"
    )
    try:
        tree = ast.parse(text, filename=str(runner_source))
    except SyntaxError as exc:
        raise HarnessError(f"cannot parse runner source: {exc}") from exc
    values: dict[str, str] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not isinstance(node.value, ast.Constant) or not isinstance(node.value.value, str):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in {"CPP_SOURCE", "CMAKE_TXT"}:
                values[target.id] = node.value.value
    missing = {"CPP_SOURCE", "CMAKE_TXT"} - set(values)
    if missing:
        raise HarnessError(
            "required native runtime source constants missing from runner: "
            + ", ".join(sorted(missing))
        )
    return values["CPP_SOURCE"], values["CMAKE_TXT"]


def run_logged(command: list[str], *, cwd: Path, log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    print("+ " + " ".join(command), flush=True)
    with log_path.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            command,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert process.stdout is not None
        for line in process.stdout:
            sys.stdout.write(line)
            log.write(line)
        returncode = process.wait()
    if returncode != 0:
        raise HarnessError(
            f"command failed with exit code {returncode}; see {log_path}"
        )


def capture(command: list[str], timeout: float = 8.0) -> dict[str, Any]:
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=timeout,
            check=False,
        )
        return {
            "command": command,
            "returncode": result.returncode,
            "output": result.stdout.strip(),
        }
    except Exception as exc:
        return {"command": command, "error": str(exc), "output": ""}


def environment_snapshot() -> dict[str, Any]:
    return {
        "hostname": platform.node(),
        "platform": platform.platform(),
        "python": platform.python_version(),
        "uname": capture(["uname", "-a"]),
        "jetson_release": capture(["sh", "-c", "cat /etc/nv_tegra_release 2>/dev/null"]),
        "nvpmodel": capture(["nvpmodel", "-q"]),
        "jetson_clocks": capture(["jetson_clocks", "--show"]),
        "tegrastats_sample": capture(["tegrastats", "--interval", "1000", "--count", "1"], 5.0),
    }


def copy_metadata(artifacts: dict[str, Any], out_dir: Path) -> None:
    target = out_dir / "metadata"
    target.mkdir(parents=True, exist_ok=True)
    for mode in MODES:
        shutil.copy2(
            artifacts["metas"][mode], target / f"{mode}_native_trt_meta.json"
        )


def artifact_record(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path),
        "size_bytes": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
    }


def build_runtime(runner_source: Path, work_dir: Path, log_dir: Path) -> Path:
    cpp, cmake = extract_runtime_sources(runner_source)
    source_dir = work_dir / "native_runtime"
    build_dir = source_dir / "build"
    source_dir.mkdir(parents=True, exist_ok=True)
    (source_dir / "main.cpp").write_text(cpp, encoding="utf-8")
    (source_dir / "CMakeLists.txt").write_text(cmake, encoding="utf-8")
    build_dir.mkdir(parents=True, exist_ok=True)
    run_logged(
        ["cmake", "-S", str(source_dir), "-B", str(build_dir), "-DCMAKE_BUILD_TYPE=Release"],
        cwd=source_dir,
        log_path=log_dir / "cmake_configure.log",
    )
    run_logged(
        ["cmake", "--build", str(build_dir), "-j"],
        cwd=source_dir,
        log_path=log_dir / "cmake_build.log",
    )
    return require_file(build_dir / "split_native_hailo_trt_fifo", "native executable")


def sequence_for(repetitions: int) -> list[str]:
    # The default four-per-arm design is position-balanced across the run:
    # ABBA-BAAB.  For custom repetition counts, alternate each pair so that
    # neither arm is permanently first.
    if repetitions == 4:
        return [CAST, DEQUANT, DEQUANT, CAST, DEQUANT, CAST, CAST, DEQUANT]
    sequence: list[str] = []
    for pair_index in range(repetitions):
        sequence.extend((CAST, DEQUANT) if pair_index % 2 == 0 else (DEQUANT, CAST))
    return sequence


def validate_raw_result(
    payload: dict[str, Any], *, mode: str, args: argparse.Namespace, artifacts: dict[str, Any]
) -> None:
    expected = {
        "ok": True,
        "mode": "native_hailort_tensorrt_fifo",
        "frames": args.frames,
        "completed_frames": args.frames,
        "requested_frames": args.frames,
        "warmup": args.warmup,
        "queue_depth": args.queue_depth,
        "hailo_format": "uint8",
        "task": "detection",
        "preprocess_mode_effective": "letterbox",
        "preprocess_pad_value_effective": 114,
        "letterbox_pad_value": 114,
        "reuse_preprocessed_input": True,
        "prepared_feed_contract": "prepared_feed_preprocess_outside_counted_loop",
        "measurement_boundary": "workers_ready_to_last_completed_trt_frame",
        "warmup_contract": "fully_drained_before_worker_start",
        "trt_host_memory_policy": "cuda_pinned_all_bindings",
        "trt_output_materialization_policy": "synchronized_d2h_pinned_buffer_no_post_copy",
        "trt_copy_outputs": True,
        "hailo_runtime_output_count": 1,
        "hailo_runtime_output_name": args.expected_output_name,
        "hailo_runtime_output_frame_bytes": args.expected_output_bytes,
        "native_split_quality_runtime_boundary_verified": True,
        "trt_input_dtype": "uint8",
        "trt_input_bytes": args.expected_output_bytes,
    }
    for key, value in expected.items():
        if payload.get(key) != value:
            raise HarnessError(
                f"{mode} result contract mismatch for {key}: "
                f"{payload.get(key)!r} != {value!r}"
            )
    if Path(str(payload.get("hef") or "")).resolve() != artifacts["hef"]:
        raise HarnessError(f"{mode} result used an unexpected HEF")
    if Path(str(payload.get("engine") or "")).resolve() != artifacts["engines"][mode]:
        raise HarnessError(f"{mode} result used an unexpected engine")
    hailo_bytes = int(payload.get("hailo_runtime_output_frame_bytes") or 0)
    trt_bytes = int(payload.get("trt_input_bytes") or 0)
    if hailo_bytes <= 0 or hailo_bytes != trt_bytes:
        raise HarnessError(
            f"{mode} boundary/TRT byte mismatch: "
            f"hailo={hailo_bytes}, trt={trt_bytes}"
        )
    nonnegative_metrics = (
        "fps_makespan",
        "paper_equivalent_fps",
        "paper_equivalent_cycle_ms",
        "preprocess_ms",
        "p1_ms",
        "handoff_ms",
        "trt_input_copy_ms",
        "p2_run_ms",
        "p1_thread_ms",
        "p2_thread_ms",
        "makespan_ms",
        "single_latency_model_ms",
    )
    for key in nonnegative_metrics:
        value = payload.get(key)
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(float(value))
        ):
            raise HarnessError(f"{mode} result has invalid metric {key}: {value!r}")
        if float(value) < 0.0:
            raise HarnessError(f"{mode} result has negative metric {key}: {value!r}")
    for key in ("fps_makespan", "paper_equivalent_fps", "paper_equivalent_cycle_ms", "makespan_ms"):
        if float(payload[key]) <= 0.0:
            raise HarnessError(f"{mode} reported non-positive metric {key}")
    if int(payload.get("duration_s") or 0) != 0:
        raise HarnessError(f"{mode} unexpectedly used duration mode")
    expected_fps = 1000.0 * args.frames / float(payload["makespan_ms"])
    if not math.isclose(
        float(payload["fps_makespan"]), expected_fps, rel_tol=1e-4, abs_tol=1e-4
    ):
        raise HarnessError(f"{mode} fps/makespan metrics are inconsistent")
    expected_paper_fps = 1000.0 / float(payload["paper_equivalent_cycle_ms"])
    if not math.isclose(
        float(payload["paper_equivalent_fps"]), expected_paper_fps,
        rel_tol=1e-4, abs_tol=1e-4,
    ):
        raise HarnessError(f"{mode} paper FPS/cycle metrics are inconsistent")
    if not math.isclose(
        float(payload["handoff_ms"]), float(payload["trt_input_copy_ms"]),
        rel_tol=0.0, abs_tol=1e-6,
    ):
        raise HarnessError(f"{mode} handoff/copy metrics are inconsistent")


def metric_stats(values: list[float]) -> dict[str, float]:
    return {
        "median": statistics.median(values),
        "mean": statistics.fmean(values),
        "min": min(values),
        "max": max(values),
        "population_stdev": statistics.pstdev(values),
    }


def build_summary(
    *, args: argparse.Namespace, artifacts: dict[str, Any], runs: list[dict[str, Any]],
    started_utc: str, finished_utc: str, environment_before: dict[str, Any],
    environment_after: dict[str, Any], runner_source: Path, executable: Path,
) -> dict[str, Any]:
    metric_names = (
        "fps_makespan",
        "paper_equivalent_fps",
        "paper_equivalent_cycle_ms",
        "preprocess_ms",
        "p1_ms",
        "handoff_ms",
        "trt_input_copy_ms",
        "p2_run_ms",
        "p1_thread_ms",
        "p2_thread_ms",
        "makespan_ms",
        "single_latency_model_ms",
    )
    per_mode: dict[str, Any] = {}
    for mode in MODES:
        selected = [row for row in runs if row["variant"] == mode]
        if len(selected) != args.repetitions:
            raise HarnessError(
                f"{mode} has {len(selected)} valid runs; expected {args.repetitions}"
            )
        metrics: dict[str, Any] = {}
        for key in metric_names:
            values = [float(row["result"][key]) for row in selected]
            metrics[key] = metric_stats(values)
        per_mode[mode] = {
            "valid_runs": len(selected),
            "quality_eligible": mode == DEQUANT,
            "measurement_quality_qualified": False,
            "quality_note": (
                "diagnostic_only_raw_uint8_cast_omits_dequantization_and_layout_transform"
                if mode == CAST
                else "matches_the_preserved_cache_dequant_and_layout_runtime_contract"
            ),
            "quality_revalidated_by_this_ab": False,
            "metrics": metrics,
        }

    comparison: dict[str, Any] = {}
    for key in metric_names:
        cast_value = per_mode[CAST]["metrics"][key]["median"]
        dequant_value = per_mode[DEQUANT]["metrics"][key]["median"]
        comparison[key] = {
            "cast_median": cast_value,
            "dequant_median": dequant_value,
            "dequant_minus_cast": dequant_value - cast_value,
            "dequant_over_cast": dequant_value / cast_value if cast_value else None,
            "dequant_percent_change": (
                ((dequant_value / cast_value) - 1.0) * 100.0 if cast_value else None
            ),
        }

    bridge_contracts = {}
    for mode in MODES:
        bridge = artifacts["meta_payloads"][mode]["uint8_cast_bridge"]
        bridge_contracts[mode] = {
            "schema": bridge.get("schema"),
            "input_name": bridge.get("input_name"),
            "input_dtype": bridge.get("input_dtype"),
            "source": bridge.get("source"),
            "scale": bridge.get("scale"),
            "zero_point": bridge.get("zero_point"),
            "params_source": bridge.get("params_source"),
            "boundary_layout": bridge.get("boundary_layout"),
        }

    return {
        "schema": "onnx-splitpoint/hailo8-uint8-cast-vs-dequant-ab",
        "schema_version": 2,
        "measurement_status": "PASS",
        "measurement_kind": "new_remeasurement_not_exact_historical_reproduction",
        "comparison_scope": "serial_cpp_pipeline_performance_diagnostic_not_quality_equivalence",
        "scientific_quality_comparison": False,
        "started_utc": started_utc,
        "finished_utc": finished_utc,
        "identity": {
            "model_id": "yolo26s",
            "case_id": args.case,
            "setup_id": "orin_nx_hailo8_01",
            "hardware": "Hailo-8 plus Jetson Orin NX TensorRT",
            "endpoint": "p2_output",
        },
        "protocol": {
            "serial_execution": True,
            "additional_parallelism": False,
            "sequence": [row["variant"] for row in runs],
            "frames_per_run": args.frames,
            "warmup_frames_per_run": args.warmup,
            "runs_per_variant": args.repetitions,
            "queue_depth": args.queue_depth,
            "pre_measurement_stabilize_seconds": args.stabilize_seconds,
            "hailo_format": "uint8",
            "preprocess": "letterbox_rgb_uint8_pad_114",
            "prepared_feed": "same_exact_image_prepared_outside_counted_loop",
            "copy_outputs": True,
            "input_kind": args.input_kind,
            "dequant_contract": {
                "scale": args.expected_dequant_scale,
                "zero_point": args.expected_dequant_zero_point,
                "boundary_layout": args.expected_layout,
            },
            "runtime_boundary_contract": {
                "output_count": 1,
                "output_name": args.expected_output_name,
                "output_bytes": args.expected_output_bytes,
                "runtime_verified_in_every_run": True,
            },
        },
        "fairness_checks": {
            "status": "PASS",
            "same_benchmark_set": True,
            "same_case": True,
            "same_source_part2": True,
            "same_hef": True,
            "same_input_image": True,
            "same_native_executable": True,
            "same_runtime_parameters": True,
            "engines_intentionally_different": artifacts["engines"][CAST]
            != artifacts["engines"][DEQUANT],
            "note": (
                "The intended A/B difference is the TensorRT bridge graph: the "
                "dequant arm includes dequantization plus HWC-to-NCHW layout conversion."
            ),
        },
        "artifacts": {
            "benchmark_set": str(artifacts["benchmark_set"]),
            "source_part2": artifact_record(artifacts["source_part2"]),
            "hef": artifact_record(artifacts["hef"]),
            "input_image": artifact_record(artifacts["image"]),
            "runner_source": artifact_record(runner_source),
            "native_executable": artifact_record(executable),
            "engines": {mode: artifact_record(artifacts["engines"][mode]) for mode in MODES},
            "bridge_contracts": bridge_contracts,
        },
        "variants": per_mode,
        "comparison_dequant_vs_cast": comparison,
        "runs": [
            {
                "order": row["order"],
                "variant": row["variant"],
                "raw_result": row["raw_result"],
                "metrics": {key: row["result"].get(key) for key in metric_names},
                "command": row["command"],
            }
            for row in runs
        ],
        "historical_reference": {
            "raw_report_available": False,
            "documented_approximate_fps_both_variants": 146.259,
            "documented_approximate_handoff_ms_both_variants": 0.147,
            "used_as_acceptance_threshold": False,
        },
        "environment_before": environment_before,
        "environment_after": environment_after,
    }


def write_csv_report(summary: dict[str, Any], path: Path) -> None:
    fields = [
        "order", "variant", "fps_makespan", "paper_equivalent_fps",
        "paper_equivalent_cycle_ms", "preprocess_ms", "p1_ms", "handoff_ms",
        "trt_input_copy_ms", "p2_run_ms", "p1_thread_ms", "p2_thread_ms",
        "makespan_ms", "single_latency_model_ms", "raw_result",
    ]
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in summary["runs"]:
            writer.writerow({
                "order": row["order"],
                "variant": row["variant"],
                **row["metrics"],
                "raw_result": row["raw_result"],
            })


def fmt(value: Any, digits: int = 3) -> str:
    return "n/a" if value is None else f"{float(value):.{digits}f}"


def write_markdown_report(summary: dict[str, Any], path: Path) -> None:
    cast = summary["variants"][CAST]["metrics"]
    dequant = summary["variants"][DEQUANT]["metrics"]
    fps_cmp = summary["comparison_dequant_vs_cast"]["fps_makespan"]
    handoff_cmp = summary["comparison_dequant_vs_cast"]["handoff_ms"]
    lines = [
        "# Hailo-8 UINT8 Cast-vs-Dequant A/B",
        "",
        "**MEASUREMENT_STATUS: PASS**",
        "",
        "Neue serielle C++-Pipeline-Messung für YOLO26s/b038. Sie ist keine ",
        "bytegenaue Rekonstruktion des verlorenen historischen Reports.",
        "",
        "| Variante | Läufe | FPS (Median) | Handoff ms (Median) | P1 ms | P2 ms | Quality-Status |",
        "|---|---:|---:|---:|---:|---:|---|",
        (
            f"| `{CAST}` | {summary['variants'][CAST]['valid_runs']} | "
            f"{fmt(cast['fps_makespan']['median'])} | {fmt(cast['handoff_ms']['median'])} | "
            f"{fmt(cast['p1_ms']['median'])} | {fmt(cast['p2_run_ms']['median'])} | "
            "nur Diagnose, nicht quality-qualifiziert |"
        ),
        (
            f"| `{DEQUANT}` | {summary['variants'][DEQUANT]['valid_runs']} | "
            f"{fmt(dequant['fps_makespan']['median'])} | {fmt(dequant['handoff_ms']['median'])} | "
            f"{fmt(dequant['p1_ms']['median'])} | {fmt(dequant['p2_run_ms']['median'])} | "
            "korrekter Boundary-Laufzeitvertrag; Quality hier nicht neu validiert |"
        ),
        "",
        "## Differenz Dequant gegenüber Cast",
        "",
        f"- Pipeline-FPS: {fmt(fps_cmp['dequant_minus_cast'])} FPS "
        f"({fmt(fps_cmp['dequant_percent_change'])} %)",
        f"- Handoff: {fmt(handoff_cmp['dequant_minus_cast'])} ms "
        f"({fmt(handoff_cmp['dequant_percent_change'])} %)",
        "",
        "## Interpretation",
        "",
        "Der Cast-Arm lässt die fachlich notwendige Dequantisierung und die "
        "Boundary-Layout-Transformation aus. Der Vergleich misst deshalb den "
        "kombinierten Laufzeitaufschlag des korrekten Dequant+Layout-Vertrags; "
        "er ist kein Output-Quality-Vergleich.",
        "",
        "Alle Arme nutzten dasselbe BenchmarkSet, denselben Case, dasselbe HEF, "
        "dasselbe Eingabebild, dieselbe ausführbare C++-Pipeline und dieselben "
        "Laufparameter. Nur die absichtlich unterschiedlichen TensorRT-Bridge-"
        "Engines wurden gewechselt.",
        "",
        f"Eingabeart: `{summary['protocol']['input_kind']}`. Das Bild wird einmal "
        "vorbereitet und liegt außerhalb der gezählten Pipeline-Schleife.",
        "",
        "Historischer Hinweis: dokumentiert waren ungefähr 146,259 FPS und "
        "0,147 ms Handoff für beide Varianten. Diese Werte sind keine "
        "Akzeptanzgrenze für die neue Messung.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runner-source", required=True)
    parser.add_argument("--benchmark-set", required=True)
    parser.add_argument("--case", default="b038")
    parser.add_argument("--image", default="")
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--work-dir", required=True)
    parser.add_argument("--frames", type=int, default=1000)
    parser.add_argument("--warmup", type=int, default=100)
    parser.add_argument("--repetitions", type=int, default=4)
    parser.add_argument("--queue-depth", type=int, default=3)
    parser.add_argument("--pause-seconds", type=float, default=2.0)
    parser.add_argument("--stabilize-seconds", type=float, default=15.0)
    parser.add_argument("--device-id", default="")
    parser.add_argument("--minimal-overlay", action="store_true")
    parser.add_argument("--expected-dequant-scale", type=float, default=None)
    parser.add_argument("--expected-dequant-zero-point", type=float, default=None)
    parser.add_argument("--expected-layout", default=None)
    parser.add_argument("--expected-output-name", default="")
    parser.add_argument("--expected-output-bytes", type=int, default=0)
    parser.add_argument(
        "--input-kind",
        default="validation_image",
        choices=["validation_image", "synthetic_performance_input"],
    )
    parser.add_argument("--preflight-only", action="store_true")
    return parser.parse_args()


def measured_main(args: argparse.Namespace) -> int:
    if args.frames <= 0 or args.warmup < 0 or args.repetitions <= 0 or args.queue_depth <= 0:
        raise HarnessError("frames/repetitions/queue-depth must be positive; warmup must be nonnegative")
    if args.case != "b038":
        raise HarnessError("this focused replay supports only the documented YOLO26s case b038")
    if args.pause_seconds < 0 or args.stabilize_seconds < 0:
        raise HarnessError("pause-seconds and stabilize-seconds must be nonnegative")
    if (
        args.expected_dequant_scale is None
        or args.expected_dequant_zero_point is None
        or not args.expected_layout
        or not args.expected_output_name
        or args.expected_output_bytes <= 0
    ):
        raise HarnessError(
            "explicit scale, zero point, layout and Hailo boundary identity "
            "from the preserved cache contract are required"
        )
    if shutil.which("cmake") is None:
        raise HarnessError("cmake is not installed on the Hailo-8 Jetson")
    hailo_devices = sorted(Path("/dev").glob("hailo*"))
    if not hailo_devices:
        raise HarnessError("no /dev/hailo* device is visible")

    out_dir = Path(args.out_dir).expanduser().resolve()
    work_dir = Path(args.work_dir).expanduser().resolve()
    runner_source = Path(args.runner_source).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    work_dir.mkdir(parents=True, exist_ok=True)
    log_dir = out_dir / "logs"
    raw_dir = out_dir / "raw"
    log_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)

    free_bytes = shutil.disk_usage(work_dir).free
    if free_bytes < 1024**3:
        raise HarnessError(
            f"less than 1 GiB free at work directory: {free_bytes} bytes"
        )

    artifacts = resolve_artifacts(args)
    copy_metadata(artifacts, out_dir)
    started_utc = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    preflight = {
        "status": "PASS",
        "measurement_kind": "new_remeasurement_not_exact_historical_reproduction",
        "benchmark_set": str(artifacts["benchmark_set"]),
        "case": args.case,
        "hef": artifact_record(artifacts["hef"]),
        "image": artifact_record(artifacts["image"]),
        "source_part2": artifact_record(artifacts["source_part2"]),
        "engines": {mode: artifact_record(artifacts["engines"][mode]) for mode in MODES},
        "metadata": {mode: str(artifacts["metas"][mode]) for mode in MODES},
        "hailo_devices": [str(path) for path in hailo_devices],
        "frames": args.frames,
        "warmup": args.warmup,
        "runs_per_variant": args.repetitions,
        "queue_depth": args.queue_depth,
        "pre_measurement_stabilize_seconds": args.stabilize_seconds,
        "input_kind": args.input_kind,
        "dequant_contract": {
            "scale": args.expected_dequant_scale,
            "zero_point": args.expected_dequant_zero_point,
            "boundary_layout": args.expected_layout,
        },
        "runtime_boundary_contract": {
            "output_count": 1,
            "output_name": args.expected_output_name,
            "output_bytes": args.expected_output_bytes,
        },
    }
    write_json(out_dir / "preflight.json", preflight)
    print("HAILO8_UINT8_BRIDGE_AB_PREFLIGHT=PASS", flush=True)
    if args.preflight_only:
        return 0

    executable = build_runtime(runner_source, work_dir, log_dir)
    if args.stabilize_seconds:
        print(
            f"=== STABILIZE {args.stabilize_seconds:g} seconds before measurement ===",
            flush=True,
        )
        time.sleep(args.stabilize_seconds)
    environment_before = environment_snapshot()
    sequence = sequence_for(args.repetitions)
    runs: list[dict[str, Any]] = []
    prepared_input = work_dir / "prepared_input_rgb_uint8.bin"

    for index, mode in enumerate(sequence, start=1):
        raw_path = raw_dir / f"run_{index:02d}_{mode}.json"
        log_path = log_dir / f"run_{index:02d}_{mode}.log"
        command = [
            str(executable),
            "--hef", str(artifacts["hef"]),
            "--engine", str(artifacts["engines"][mode]),
            "--image", str(artifacts["image"]),
            "--out", str(raw_path),
            "--frames", str(args.frames),
            "--warmup", str(args.warmup),
            "--queue-depth", str(args.queue_depth),
            "--hailo-format", "uint8",
            "--task", "detection",
            "--preprocess-mode", "letterbox",
            "--copy-outputs", "1",
            "--dump-outputs", "0",
            "--dump-boundary", "0",
            "--letterbox-pad-value", "114",
            "--output-dir", str(work_dir / "unused_outputs"),
            "--boundary-dir", str(work_dir / "unused_boundary"),
            "--prepared-input-out", str(prepared_input),
            "--reuse-preprocessed-input", "1",
            "--expected-output-count", "1",
            "--expected-output-name", args.expected_output_name,
            "--expected-output-bytes", str(args.expected_output_bytes),
        ]
        if args.device_id:
            command.extend(("--device-id", args.device_id.removeprefix("pci/")))
        print(
            f"=== RUN {index}/{len(sequence)}: {mode} ===",
            flush=True,
        )
        run_logged(command, cwd=work_dir, log_path=log_path)
        payload = load_json(raw_path)
        validate_raw_result(payload, mode=mode, args=args, artifacts=artifacts)
        runs.append(
            {
                "order": index,
                "variant": mode,
                "raw_result": str(Path("raw") / raw_path.name),
                "result": payload,
                "command": command,
            }
        )
        write_json(
            out_dir / "run_index.json",
            {
                "status": "RUNNING",
                "completed": len(runs),
                "expected": len(sequence),
                "runs": [
                    {"order": row["order"], "variant": row["variant"], "raw_result": row["raw_result"]}
                    for row in runs
                ],
            },
        )
        if index != len(sequence) and args.pause_seconds:
            time.sleep(args.pause_seconds)

    environment_after = environment_snapshot()
    finished_utc = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    summary = build_summary(
        args=args,
        artifacts=artifacts,
        runs=runs,
        started_utc=started_utc,
        finished_utc=finished_utc,
        environment_before=environment_before,
        environment_after=environment_after,
        runner_source=runner_source,
        executable=executable,
    )
    summary_path = out_dir / "hailo8_uint8_bridge_ab_summary.json"
    write_json(summary_path, summary)
    write_csv_report(summary, out_dir / "hailo8_uint8_bridge_ab_runs.csv")
    write_markdown_report(summary, out_dir / "hailo8_uint8_bridge_ab_summary.md")
    write_json(
        out_dir / "run_index.json",
        {
            "status": "PASS",
            "completed": len(runs),
            "expected": len(sequence),
            "summary": summary_path.name,
        },
    )
    print("MEASUREMENT_STATUS=PASS", flush=True)
    print(f"SUMMARY_JSON={summary_path}", flush=True)
    return 0


def main() -> int:
    args = parse_args()
    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    lock_path = Path("/tmp/onnx_splitpoint_hailo8_uint8_bridge_ab.lock")
    lock_stream = lock_path.open("w", encoding="utf-8")
    try:
        fcntl.flock(lock_stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("STOP: another Hailo-8 UINT8 bridge A/B is already running", file=sys.stderr)
        return 3
    try:
        return measured_main(args)
    except Exception as exc:
        failure = {
            "measurement_status": "FAIL",
            "error_type": type(exc).__name__,
            "error": str(exc),
            "argv": sys.argv,
            "time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        write_json(out_dir / "failure.json", failure)
        print(f"STOP: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2
    finally:
        fcntl.flock(lock_stream.fileno(), fcntl.LOCK_UN)
        lock_stream.close()


if __name__ == "__main__":
    raise SystemExit(main())
