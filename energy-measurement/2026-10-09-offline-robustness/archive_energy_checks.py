#!/usr/bin/env python3
"""Ergaenzt den registrierten Scope-Review um kompakte lokale Belege.

Keine Rohdatenanalyse, keine Git-Befehle, keine Aenderung der Originalberichte.
Ausgabe: scopes/ neben diesem Skript; Python >= 3.10, nur Standardbibliothek.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import os
from pathlib import Path
import re
import tempfile

WORKLOADS = ("gemmfp32", "gemmint8", "yolofp32", "yoloint8", "gemma3-4b", "resnet50")
REGISTERED = ("summary.json", "scope_per_run.csv", "scope_groups.csv", "scope_envelope.csv", "REPORT.txt")
SMALL = ("run_settings.json", "environment.json", "input_inventory.json", "metadata_evidence.json")


def safe_path(root, relative):
    relative = Path(relative)
    if (relative.is_absolute() or "\\" in str(relative) or not relative.parts
            or any(part in (".", "..") for part in relative.parts)):
        raise ValueError(f"Unzulaessiger relativer Pfad: {relative}")
    path = root
    for number, part in enumerate(relative.parts):
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Symlink wird nicht uebernommen: {path}")
        if number < len(relative.parts) - 1 and path.exists() and not path.is_dir():
            raise ValueError(f"Datei blockiert erwarteten Unterordner: {path}")
    return path


def stamp(path):
    st = path.stat()
    return {"path": str(path), "bytes": st.st_size, "mtime_ns": st.st_mtime_ns}


def small_bytes(path, limit=16_000_000):
    if not path.is_file() or path.stat().st_size > limit:
        raise ValueError(f"Erwartete kleine regulaere Datei fehlt/ist zu gross: {path}")
    return path.read_bytes()


def dump(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n"


def critical_keys(source):
    with (source / "scope_envelope.csv").open(newline="", encoding="utf-8") as f:
        cells = {(float(r["nominal_duration_s"]), float(r["rate_sps"]))
                 for r in csv.DictReader(f) if r["decision_changed_at_1pct"] == "True"
                 or r["decision_changed_at_0p5pct"] == "True"}
    cells.add((2.0, 9400.0))
    with (source / "scope_groups.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    keys = set()
    for duration, rate in sorted(cells):
        group = [r for r in rows if float(r["nominal_duration_s"]) == duration
                 and float(r["rate_sps"]) == rate]
        if len(group) != 12:
            raise ValueError(f"Fokuszelle {duration}s/{rate}Sps hat nicht 12 Gruppen.")
        for field in ("native_hierarchical_Q95_pct", "via_1M_hierarchical_Q95_pct"):
            maximum = max(float(r[field]) for r in group)
            keys.update((r["workload"], r["source"], duration, rate)
                        for r in group if float(r[field]) == maximum)
    return cells, keys


def archive(source, analysis_script, destination):
    source = source.expanduser().resolve()
    destination = destination.absolute()
    if destination.is_symlink() or not destination.is_dir():
        raise ValueError(f"Registrierter scopes/-Ordner fehlt/ist ein Symlink: {destination}")
    if source == destination or source in destination.parents or destination in source.parents:
        raise ValueError("Quellbericht und Archiv muessen getrennte Verzeichnisse sein.")
    for name in REGISTERED:
        original = small_bytes(safe_path(source, name))
        saved = small_bytes(safe_path(destination, name))
        if original != saved:
            raise ValueError(f"Anderer als der registrierte Reviewstand: {name}; nichts ueberschrieben.")
    summary = json.loads((source / "summary.json").read_text(encoding="utf-8"))
    settings = json.loads(small_bytes(safe_path(source, "run_settings.json")))
    expected = {f"scope_{w}_{s}_{i}.json": (w, s, i) for w in WORKLOADS
                for s in ("tek", "pico") for i in range(9 if w == "resnet50" else 10)}
    names = summary.get("active_record_files", [])
    if (summary.get("script_version") != "1.0.1"
            or summary.get("status") != "completed_requested_probe"
            or summary.get("successful_records") != 118 or summary.get("failed_records") != 0
            or len(names) != 118 or set(names) != set(expected)
            or settings.get("script_version") != "1.0.1" or settings.get("part") != "scopes"
            or settings.get("native_fs") != 5_000_000 or settings.get("reduced_fs") != 1_000_000):
        raise ValueError("Erwartet wird genau der registrierte vollstaendige 1.0.1-Scope-Review (118 Records).")
    cells, keys = critical_keys(source)
    warnings, originals, record_sources = [], [], []
    critical_rows = 0
    observed_keys = set()
    with tempfile.TemporaryDirectory(prefix=".energy-archive-", dir=destination.parent) as temp:
        stage = Path(temp)

        def copy_small(relative, target=None, limit=16_000_000):
            path = safe_path(source, relative)
            data = small_bytes(path, limit)
            output = safe_path(stage, target or relative)
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(data)
            originals.append(stamp(path))

        for name in SMALL:
            copy_small(name)
        evidence = json.loads((stage / "metadata_evidence.json").read_text(encoding="utf-8"))
        budget = 12_000_000
        seen = set()
        for item in evidence.get("found", []):
            relative = item["copy"]
            path = safe_path(source, relative)
            if Path(relative).parts[0] != "metadata":
                raise ValueError(f"Metadatenkopie liegt ausserhalb metadata/: {relative}")
            if relative in seen:
                continue
            seen.add(relative)
            if not path.is_file() or path.stat().st_size > min(2_000_000, budget):
                warnings.append(f"Metadatenkopie fehlt/ueberschreitet Groessenbudget: {relative}")
                continue
            copy_small(relative, limit=2_000_000)
            budget -= path.stat().st_size
        script = analysis_script.expanduser().absolute()
        if script.is_symlink() or not script.is_file() or script.stat().st_size > 1_000_000:
            warnings.append(f"Optionales Analyseskript nicht uebernommen: {script}; Repo-Skript bleibt verfuegbar.")
        else:
            data = script.read_bytes()
            if not re.search(rb'(?m)^VERSION\s*=\s*[\"\x27]1\.0\.1[\"\x27]', data):
                warnings.append(f"Optionales Analyseskript nicht als Version 1.0.1 erkennbar: {script}")
            else:
                (stage / "energy_paper_checks.py").write_bytes(data)
                originals.append(stamp(script))
        with (stage / "record_audit.jsonl").open("w", encoding="utf-8") as audit_file:
            with (stage / "critical_comparisons.jsonl.gz").open("wb") as compressed:
                with gzip.GzipFile(filename="", mode="wb", fileobj=compressed, mtime=0) as critical:
                    for name in sorted(names):
                        path = safe_path(source, "records/" + name)
                        if not path.is_file():
                            raise ValueError(f"Record fehlt: {path}")
                        before = stamp(path)
                        with path.open(encoding="utf-8") as f:
                            record = json.load(f)
                        if before != stamp(path):
                            raise ValueError(f"Record waehrend des Lesens veraendert: {path}")
                        identity = (record.get("workload"), record.get("source"), record.get("run_id"))
                        if (identity != expected[name] or record.get("kind") != "scope"
                                or record.get("status") != "completed"):
                            raise ValueError(f"Unerwartete Record-Identitaet/Status: {name}")
                        record_sources.append(before)
                        windows = []
                        for window in record["windows"]:
                            compact = {k: v for k, v in window.items() if k != "comparisons"}
                            windows.append(compact)
                            selected = []
                            for comparison in window["comparisons"]:
                                key = identity[:2] + (float(window["nominal_duration_s"]), float(comparison["rate_sps"]))
                                if key in keys:
                                    selected.append(comparison)
                                    observed_keys.add(key)
                            if selected:
                                row = {"record_file": name, "workload": identity[0], "source": identity[1],
                                       "run_id": identity[2], "window": dict(compact, comparisons=selected)}
                                critical.write(dump(row).encode("utf-8"))
                                critical_rows += 1
                        record["windows"] = windows
                        audit_file.write(dump(record))
        if observed_keys != keys:
            raise ValueError("Angeforderte Fokusvergleiche fehlen in den Originalrecords.")
        full_zip = Path(str(source) + ".zip")
        archive_info = ({"status": "present", **stamp(full_zip)} if full_zip.is_file() and not full_zip.is_symlink()
                        else {"status": "not_found_or_symlink", "path": str(full_zip)})
        outputs = sorted(p for p in stage.rglob("*") if p.is_file())
        index = {"format_version": 1, "report_script_version": "1.0.1", "source_directory": str(source),
                 "record_count": len(record_sources), "registered_files": [stamp(source / n) for n in REGISTERED],
                 "companion_sources": originals, "record_sources": record_sources, "full_zip": archive_info,
                 "critical_cells": sorted(cells), "critical_group_keys": sorted(keys), "critical_rows": critical_rows,
                 "outputs": [{"path": str(p.relative_to(stage)), "bytes": p.stat().st_size} for p in outputs],
                 "warnings": warnings,
                 "note": "Keine Hashes oder Rohdatenpruefung; Originalrecords/ZIP unveraendert. Fokusvergleiche sind Originalwerte; Audits lassen comparisons weg."}
        (stage / "archive_index.json").write_text(dump(index), encoding="utf-8")
        outputs = sorted(p for p in stage.rglob("*") if p.is_file())
        for path in outputs:
            target = safe_path(destination, path.relative_to(stage))
            if target.exists() and (not target.is_file() or target.read_bytes() != path.read_bytes()):
                raise ValueError(f"Vorhandene Archivdatei weicht ab; nichts installiert: {target}")
        new_files = 0
        for path in outputs:
            target = safe_path(destination, path.relative_to(stage))
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                os.link(path, target)  # Atomar, kann vorhandene Dateien nicht ersetzen.
                new_files += 1
        total = sum(p.stat().st_size for p in outputs)
    print(f"118 Record-Audits; {len(keys)} Fokusgruppen, {critical_rows} Fokusfenster.")
    print(f"{len(outputs)} kompakte Dateien, {total / 1_000_000:.2f} MB; {new_files} neu: {destination}")
    for warning in warnings:
        print("HINWEIS: " + warning)
    print("Originalrecords/ZIP unveraendert. Kein Git-Commit oder Push ausgefuehrt.")
    return index


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("~/Reports/energy-paper-check-scopes"))
    parser.add_argument("--analysis-script", type=Path, default=Path("~/Downloads/energy_paper_checks.py"))
    args = parser.parse_args()
    try:
        archive(args.source, args.analysis_script, Path(__file__).resolve().parent / "scopes")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f"ABBRUCH: {exc}\n")


if __name__ == "__main__":
    main()
