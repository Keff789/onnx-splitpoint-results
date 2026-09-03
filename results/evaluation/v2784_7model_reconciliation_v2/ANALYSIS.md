# v2.78.4 Sieben-Modell-Evidenz: korrigierte read-only Reconciliation v2

## Ergebnis

**RECONCILED_WITH_REAL_GAPS — nicht claim-eligible und kein nachträgliches PASS.**

Der Originallauf bleibt `failed`. Der Central-Quality-Join ist als separate Projektion vollständig rekonstruierbar. v2 korrigiert jedoch die frühere Einordnung von YOLOv7/DeepX: Das ist ein Validator-/Schema-Konflikt und kein nachgewiesener Hardware-Semantikfehler.

## Materialisierte Messmatrix

- 1087 normalisierte Rohzeilen
- 551 materialisiert geforderte logische Identitäten
- 550 vorhandene logische Identitäten
- 537 setup-spezifische Spiegel-/Zusatzzeilen
- 1 materialisierte Lücke: `yolo11l / full / hailo10 / hailo10 / full`

| Modell | Gefordert | Vorhanden | Fehlend | Spiegelgruppen |
|---|---:|---:|---:|---:|
| `mobilenet_v3_large` | 84 | 84 | 0 | 81 |
| `regnet_x_1_6gf` | 84 | 84 | 0 | 81 |
| `resnet50` | 84 | 84 | 0 | 81 |
| `yolo11l` | 83 | 82 | 1 | 81 |
| `yolo26m` | 68 | 68 | 0 | 67 |
| `yolo26s` | 64 | 64 | 0 | 63 |
| `yolov7_paper` | 84 | 84 | 0 | 83 |

Die 550/551-Aussage ist für die **materialisierte** Required-Matrix korrekt. Sie ist wegen der unten beschriebenen Hailo-8-Abweichung aber keine vollständige Frozen-Scope-Aussage.

## Central Quality: Coverage und erzeugte Population

- **386/551** materialisierte Matrixidentitäten haben ein eindeutig zugeordnetes Primärergebnis.
- **407** Quality-Ergebnisse wurden technisch abgeschlossen: 386 Primärergebnisse plus 21 separate `full_quality_only`-Companions.
- 0 unmatched, 0 ambiguous; 0 Evaluatorfehler.
- Entscheidungen unverändert: 219 pass, 135 fail, 53 inconclusive.
- Primärpopulation: 198 pass, 135 fail, 53 inconclusive.

`407` ist daher **keine** Matrix-Coverage von 407/551. Keine Metrik oder Quality-Entscheidung wurde neu berechnet oder aufgewertet.

## Korrektur: YOLOv7 / DeepX Full

- Runtime und Ausführung waren erfolgreich.
- Die normalisierte Zeile enthält 7,506 Detektionen pro Bild, der alte Mini-AP-Validator meldet gleichzeitig 0 akzeptierte Predictions und AP50=0.
- Das SHA-gebundene kanonische Candidate-Artefakt enthält 500 Bilder, 3753 Detektionen und die Felder `x1,y1,x2,y2,score,class_id`.
- Central B500 bewertet exakt diesen Request mit `coco_ap_50_95=0.4562932667` gegen `0.4520187917` und entscheidet `pass`.

Damit liegt ein Legacy-Parser-/Schema-Konflikt (`box_xyxy/confidence` gegen kanonisches `x1...score`) vor. Die v1-Bezeichnung als realer semantischer DeepX-Fehler war zu stark und ist hier ausdrücklich zurückgenommen.

## Frozen Scope / Hailo-Provenienz

- Der globale Effective Plan enthält `hailo8` und `hailo10`; für YOLO11 werden mindestens 84 Ergebniszeilen erwartet.
- Der YOLO11-`benchmark_plan` enthält `hailo10`, lässt `hailo8` aber aus. Die sechs anderen Modellpläne enthalten `hailo8`.
- Der Workflow hat YOLO11 Full/Hailo-8 tatsächlich gebaut; der Fallback endete nach 9000 s mit Hard Timeout in `compile_prep`.
- Trotzdem fehlt diese Identität vollständig in der Required-Matrix. YOLO11 Full/Hailo-10 ist dagegen als required, aber missing materialisiert; dessen Fallback endete nach 9000 s in `bias_correction`.

v2 schreibt die Matrix nicht post hoc um. Der Befund wird als Planning-/Provenienzdefekt ausgewiesen und verlangt eine explizite Festlegung der autoritativen Frozen-Scope-Quelle.

## Weiterhin reale Lücken und Defekte

- `yolo11l / hailo10 / full` fehlt in der materialisierten Matrix.
- `yolo11l / deepx_m1_full` scheiterte real im Runtimepfad.
- Sechs DeepX-Full-Zeilen tragen einen Source-Identity-Repräsentationskonflikt.
- Energie war deaktiviert; Final-5000/Official COCO war nicht Bestandteil dieses B500-Development-Audits.

## Dateien

- `reconciliation_summary.json`: maschinenlesbare korrigierte Bewertung
- `logical_matrix.csv`: 551 materialisierte Identitäten
- `quality_join.csv`: 407 Quality-Ergebnisse mit konservativem Join
- `provenance_manifest.json`: Input-/Output-SHA-256 und Source-Unverändertheit
