# Hailo-8 UINT8 Cast-vs-Dequant A/B aus dem erhaltenen Cache – Revision 3

Dieses Paket ersetzt das erste Replay-Paket, das irrtümlich ein inzwischen
gelöschtes vollständiges BenchmarkSet und zwei bereits vorhandene Engines
voraussetzte.

Revision 3 korrigiert zusätzlich die Python-Umgebung des TensorRT-Builders:
`onnx` liegt auf diesem Jetson in der User-Site von `/usr/bin/python3`.
Der Builder darf deshalb nicht mit dem die User-Site ausblendenden Schalter
`-I` gestartet werden. Fremde `PYTHONPATH`-/`PYTHONHOME`-Vorgaben werden
weiterhin entfernt.

Der belegte Cache enthält noch alles, was für eine neue Performance-Messung
benötigt wird:

- YOLO26s, Case `b038`
- `part1.hef`
- `benchmark_set/b038/source_part2.onnx`
- Boundary-Metadaten und Quality-Binding
- Metadaten des erhaltenen korrekten Dequant-Engines

Das Skript liest Scale, Zero-Point und Layout aus dem erhaltenen Vertrag und
prüft sie wertbasiert gegen Boundary- und Dequant-Metadaten. Danach baut es
**beide** A/B-Engines
frisch aus demselben Part2-ONNX in einem neuen Zeitstempel-Verzeichnis:

- `uint8_cast_fp16`
- `uint8_dequant_fp16`

Der ursprüngliche Cache wird nur gelesen. Es werden keine Dateien darin
geändert, keine alten Engines überschrieben und keine zusätzliche
Hash-/Versiegelungsebene eingeführt.

## Bedeutung des Tests

Dies ist eine neue serielle Pipeline-Performance-Messung, keine exakte
Wiederherstellung des verlorenen historischen Reports und kein
Quality-Äquivalenztest.

Der Cast-Arm lässt sowohl die fachlich notwendige Dequantisierung als auch die
Layout-Transformation aus und ist deshalb nur diagnostisch. Der Dequant-Arm
wird mit dem erhaltenen Cache-Vertrag gebaut; seine Output-Quality wird durch
diesen Lauf nicht erneut bewertet.

Da kein Validierungsbild mehr beim Cache liegt, erzeugt das Skript eine feste,
deterministische 640×640-PPM-Testfläche. Dasselbe Bild wird für alle Läufe
einmal vorverarbeitet; die Bildvorverarbeitung liegt außerhalb der gezählten
Pipeline-Schleife. Die Messung bleibt deshalb für den Overhead-Vergleich der
beiden Bridge-Varianten geeignet.

## 1. Kurzer Preflight

Auf Smartmirror2:

```bash
cd "$HOME/Downloads/hailo8_uint8_bridge_ab_v3"
chmod +x run_hailo8_uint8_bridge_ab_from_cache.sh
H8_PREFLIGHT_ONLY=1 ./run_hailo8_uint8_bridge_ab_from_cache.sh
```

Erwartetes Ende:

```text
CACHE_CONTRACT=PASS
HAILO8_UINT8_BRIDGE_AB_CACHE_PREFLIGHT=PASS
```

Der Preflight baut noch keine Engine und startet keine Messung.

## 2. Vollständiger A/B-Test

Während dieses Tests darf kein anderer Benchmark oder EvalRun auf dem
Hailo-8-Jetson laufen:

```bash
cd "$HOME/Downloads/hailo8_uint8_bridge_ab_v3"
./run_hailo8_uint8_bridge_ab_from_cache.sh
```

Der erste Teil kann wegen der beiden TensorRT-Neubauten einige Zeit dauern.
Anschließend laufen standardmäßig 1.000 Frames, 100 Warmup-Frames,
Queue-Tiefe 3 und vier Prozesse je Arm in der positionsbalancierten Reihenfolge
ABBA-BAAB. Nach Engine- und C++-Build wartet das Skript vor der ersten Messung
15 Sekunden zur Stabilisierung. Es wird keine zusätzliche Parallelitätsebene
eingeführt.

Optionale kleinere Diagnoseeinstellung:

```bash
H8_FRAMES=300 H8_WARMUP=30 H8_REPETITIONS=2 \
  ./run_hailo8_uint8_bridge_ab_from_cache.sh
```

Die Stabilisierung kann bei Bedarf mit `H8_STABILIZE_SECONDS` angepasst werden.

## Ergebnis

Die lokalen Ergebnisse landen unter:

```text
~/Downloads/hailo8_uint8_bridge_ab_cache_<UTC-Zeit>_<PID>/
```

Wichtig sind:

- `cache_contract.json`
- `replay_preflight.json`
- `build_uint8_cast_fp16.json`
- `build_uint8_dequant_fp16.json`
- `build_fairness.json`
- `hailo8_uint8_bridge_ab_summary.json`
- `hailo8_uint8_bridge_ab_summary.md`
- `hailo8_uint8_bridge_ab_runs.csv`
- `raw/run_*.json`
- `logs/run_*.log`
- `build_logs/`

Die großen neu gebauten Engines und Bridge-ONNX-Dateien verbleiben im
isolierten Zeitstempel-Verzeichnis auf dem Jetson und werden nicht in das
lokale Evidence-Verzeichnis kopiert.

`HAILO8_UINT8_BRIDGE_AB=PASS` bedeutet, dass beide Engine-Builds, alle
Messläufe und die strukturellen Fairnessprüfungen erfolgreich waren. Es gibt
bewusst keine harte FPS-Akzeptanzgrenze.

## Abweichende Pfade

Nur falls sich Host, lokales Tool oder der belegte Cache verschoben haben:

```bash
H8_HOST=nx@192.168.0.104 \
H8_LOCAL_TOOL="$HOME/ONNX-Splitpoint-Tool" \
H8_CACHE_ROOT=/absoluter/pfad/zum/b038/cache-root \
  H8_PREFLIGHT_ONLY=1 ./run_hailo8_uint8_bridge_ab_from_cache.sh
```

Keine Pfade verschiedener Cases oder Cache-Roots miteinander kombinieren.
