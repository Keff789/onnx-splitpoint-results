# Hailo-10H InferModel Format-A/B-Test

Dieser Test beantwortet eine eng begrenzte Frage:

> Wie viel Zeit kostet die aktuelle Float32-Hostausgabe gegenüber der nativen quantisierten HEF-Ausgabe auf demselben Hailo-10H?

Er verändert weder das ONNX Splitpoint Tool noch das HEF und schaltet keine Hardware. Es läuft direkt auf dem Hailo-10H-Jetson und schreibt nur ein JSON-Ergebnis.

## Varianten

- **A / `float32`:** Inputs und Outputs werden hostseitig als Float32 konfiguriert. Das entspricht dem im v2.79.14-Debug-Pack protokollierten Hailo-10H-Pfad.
- **B / `native`:** Inputs bleiben Float32, Outputs verwenden im bestehenden VStream den nativen Elementtyp des zugrunde liegenden HEF-Streams (`UINT8` oder `UINT16`). Layout-/VStream-Verarbeitung bleibt identisch. Die optionale Dequantisierung wird separat gemessen und gehört nicht zur nativen Inferenzzeit.

Beide Varianten verwenden dasselbe HEF, dieselben deterministischen Eingaben, dieselben Warm-ups, dieselbe Zahl Messframes und dieselbe Inflight-Tiefe.

## Empfohlener Start von Smartmirror2

GUI und laufende Benchmarks vorher schließen. Dann das Paket entpacken und ausführen:

```bash
cd ~/Downloads/hailo10_infermodel_format_ab
bash run_hailo10_ab_from_smartmirror2.sh
```

Voreinstellungen:

```text
Hailo-10H Jetson: nx@192.168.0.145
HEF: neuestes vorhandenes yolo26s/b024/hailo10/part1/compiled.hef
Warm-up: 10 Frames
Latenz: 50 Frames je Variante
Durchsatz: 200 Frames je Variante
Inflight: 2
```

Das Ergebnis wird nach `~/Downloads/hailo10_infermodel_format_ab_<UTC>.json` kopiert.

## Optionales HEF oder andere Messlänge

Ein konkretes HEF kann als erstes Argument angegeben werden. Der Pfad gilt auf dem Hailo-10H-Jetson:

```bash
bash run_hailo10_ab_from_smartmirror2.sh \
  /home/nx/splitpoint_runs/legacy_suite/.../suite/b024/hailo/hailo10/part1/compiled.hef
```

Die Messlänge lässt sich über Umgebungsvariablen ändern:

```bash
AB_WARMUP=20 AB_LATENCY_FRAMES=100 AB_THROUGHPUT_FRAMES=500 AB_INFLIGHT=4 \
  bash run_hailo10_ab_from_smartmirror2.sh
```

## Auswertung

Entscheidend sind im JSON:

```text
variants.float32.latency.mean_ms
variants.native.latency.mean_ms
variants.float32.throughput.fps
variants.native.throughput.fps
comparison.native_vs_float32.*
correctness.outputs[*].max_abs
correctness.outputs[*].mean_abs
```

Interpretation:

- Deutlich schnellere native Ausgabe bei vergleichbaren dequantisierten Werten: Die frühe Float32-Transformation ist ein relevanter Teil des Problems.
- Ähnliche Inferenzzeiten, aber unterschiedliche Puffergrößen: Der große Verlust liegt eher im nachfolgenden Boundary-/TensorRT-Pfad.
- Liegt bereits die eigenständige Float32-Variante deutlich unter den im v2.79.14-Lauf beobachteten rund `63.85 ms` beziehungsweise über `15.55 FPS`, entsteht der Hauptverlust im Produkt-Runner und nicht in `InferModel` selbst.
- Beide Varianten weit langsamer als `hailortcli benchmark` desselben HEFs: zusätzlicher Overhead in unserem Python-/Runner-Pfad.
- Native Ausgabe nicht unterstützt: Im Ergebnis steht der genaue API-/Formatfehler. Das Skript fällt nicht still auf Float32 zurück.

## Bewusste Grenzen

- Dies ist ein Runtime-Microbenchmark, kein wissenschaftlicher Ergebnislauf.
- Synthetische, deterministische Inputs reichen für die Laufzeit- und Formatfrage. Sie ersetzen keine COCO-/ImageNet-Quality-Auswertung.
- Der Test misst keine Full-System-Energie. Energie wird erst nach Reparatur der Native-/Energy-Gates wieder im Produktworkflow gemessen.
- Der erste Test ändert den Power Mode nicht. `PERFORMANCE` gegen `ULTRA_PERFORMANCE` sollte erst danach als eigener A/B-Faktor untersucht werden.
