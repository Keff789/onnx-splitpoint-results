# Hailo-10H Input-Format-A/B-Test

Dieser eigenständige Test isoliert ausschließlich den Host-Eingangsdatentyp des vorhandenen YOLO26s-`b024`-Part1-HEFs.

## Feste Testbedingungen

- Variante A: Host-Eingang `FLOAT32`
- Variante B: Host-Eingang im nativen HEF-Typ `UINT8` beziehungsweise `UINT16`
- Ausgang in beiden Varianten: derselbe native HEF-Typ
- exakt dieselben quantisierten Geräte-Eingabewerte
- genau ein offener InferModel-Job
- keine interne InferModel-Parallelität
- keine Änderung am Tool, HEF, Power Mode oder an der Hardware
- keine Energie- oder Qualitätsmessung

Der Test verwendet weiterhin die pyHailoRT-`InferModel`-API. `run_async` ist deren Ausführungsaufruf, aber jeder Job wird vollständig abgewartet, bevor der nächste gestartet wird. Die maximale Zahl gleichzeitig offener Jobs ist daher ausdrücklich `1`.

## Messwerte

Erfasst werden:

- sequenzielle Latenz über standardmäßig 100 Frames,
- daraus direkt gemessene Single-Job-FPS,
- Eingabepuffergröße,
- native Ausgangspuffer und deren exakte Übereinstimmung,
- Referenzzeit einer expliziten Float32→Native-Quantisierung außerhalb der Inferenzmessung,
- Runtime-, HEF-, Quantisierungs- und Power-Mode-Informationen.

Für identische Gerätewerte erzeugt der Test zuerst einen nativen Quantisierungstensor `q`. Die Float32-Variante erhält dessen Dequantisierung mit HailoRTs eigener Transformfunktion. Vor dem Hardwarelauf quantisiert dieselbe HailoRT-Transformation diesen Tensor zurück und muss wieder bitgenau `q` ergeben. Die manuelle Formel `(q - zero_point) * scale` wird zusätzlich gegengeprüft.

## Start auf Smartmirror2

GUI und laufende Benchmarks vorher schließen. Danach:

```bash
cd ~/Downloads/hailo10_input_ab
bash run_hailo10_input_ab_from_smartmirror2.sh
```

Voreinstellungen:

```text
Hailo-10H Jetson: nx@192.168.0.145
HEF: neuestes vorhandenes yolo26s/b024/hailo10 Part1-HEF
Warm-up: 10 Frames je Variante
Messung: 100 Frames je Variante
Maximal offene Jobs: 1
```

Das Ergebnis wird nach

```text
~/Downloads/hailo10_input_format_ab_<UTC>.json
```

kopiert.

## Optionales HEF oder andere Messlänge

Ein konkreter HEF-Pfad auf dem Hailo-10H-Jetson kann als erstes Argument angegeben werden:

```bash
bash run_hailo10_input_ab_from_smartmirror2.sh \
  /home/nx/splitpoint_runs/_onnx_splitpoint_cache/.../yolo26s/b024/.../part1.hef
```

Die Messlänge kann ohne Änderung des Tests angepasst werden:

```bash
AB_WARMUP=20 AB_FRAMES=200 \
  bash run_hailo10_input_ab_from_smartmirror2.sh
```

## Auswertung

Wichtige JSON-Felder:

```text
variants.float32_input.latency.mean_ms
variants.native_input.latency.mean_ms
variants.float32_input.single_outstanding_job_stream.fps
variants.native_input.single_outstanding_job_stream.fps
comparison.native_input_vs_float32_input.*
correctness.all_outputs_exactly_equal
```

Interpretation:

- Native Eingabe deutlich schneller: Die Hailo-10H-Float32-Eingangskonvertierung ist ein relevanter Teil der verbleibenden Part1-Latenz.
- Nur kleiner Unterschied: Die verbleibende Laufzeit liegt überwiegend im weiteren InferModel-/VStream-/HEF-Pfad.
- Ausgang nicht bitgenau gleich: Der Vergleich wird als `output_mismatch` beendet und darf nicht als gültiger Performancevergleich verwendet werden.

Als Plausibilitätswert sollte die Float32-Eingangsvariante ungefähr an die vorherige Messung `FLOAT32 input → UINT8 output` von rund `49,74 ms` anschließen. Abweichungen sind wegen Power-/Temperaturzustand möglich.
