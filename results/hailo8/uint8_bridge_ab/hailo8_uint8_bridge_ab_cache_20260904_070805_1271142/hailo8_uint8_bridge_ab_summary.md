# Hailo-8 UINT8 Cast-vs-Dequant A/B

**MEASUREMENT_STATUS: PASS**

Neue serielle C++-Pipeline-Messung für YOLO26s/b038. Sie ist keine 
bytegenaue Rekonstruktion des verlorenen historischen Reports.

| Variante | Läufe | FPS (Median) | Handoff ms (Median) | P1 ms | P2 ms | Quality-Status |
|---|---:|---:|---:|---:|---:|---|
| `uint8_cast_fp16` | 4 | 211.166 | 0.179 | 2.056 | 4.542 | nur Diagnose, nicht quality-qualifiziert |
| `uint8_dequant_fp16` | 4 | 213.064 | 0.164 | 2.039 | 4.524 | korrekter Boundary-Laufzeitvertrag; Quality hier nicht neu validiert |

## Differenz Dequant gegenüber Cast

- Pipeline-FPS: 1.898 FPS (0.899 %)
- Handoff: -0.015 ms (-8.527 %)

## Interpretation

Der Cast-Arm lässt die fachlich notwendige Dequantisierung und die Boundary-Layout-Transformation aus. Der Vergleich misst deshalb den kombinierten Laufzeitaufschlag des korrekten Dequant+Layout-Vertrags; er ist kein Output-Quality-Vergleich.

Alle Arme nutzten dasselbe BenchmarkSet, denselben Case, dasselbe HEF, dasselbe Eingabebild, dieselbe ausführbare C++-Pipeline und dieselben Laufparameter. Nur die absichtlich unterschiedlichen TensorRT-Bridge-Engines wurden gewechselt.

Eingabeart: `synthetic_performance_input`. Das Bild wird einmal vorbereitet und liegt außerhalb der gezählten Pipeline-Schleife.

Historischer Hinweis: dokumentiert waren ungefähr 146,259 FPS und 0,147 ms Handoff für beide Varianten. Diese Werte sind keine Akzeptanzgrenze für die neue Messung.
