# ONNX Splitpoint Tool – akute Befunde und Fortsetzungsstand

Stand: 2026-09-03  
Untersuchte Ausführung: `biggerset_20260903_090110` mit Tool v2.79.14  
Primäre Evidenz: `biggerset_20260903_090110_debug_pack.zip`

## Verbindliche Leitplanken

- Keine zusätzlichen Hash-, Manifest- oder Versiegelungsebenen einführen.
- Bereits vorhandene Vertragsfelder nur dort korrekt weiterreichen, wo der bestehende Ablauf sie ohnehin verlangt.
- Energie wird physikalisch immer als Full-System-Aufnahme am u.RECS-Eingang gemessen.
- Ein technisch ausführbarer Messpunkt soll gemessen werden dürfen. Eine fehlende oder negative Quality-Bewertung darf anschließend seine Claim-Eignung sperren, aber nicht den ganzen Hardwarelauf vernichten.
- Vor einem weiteren Mehrmodell-Langlauf zuerst kleine Offline- und Einmodell-Smokes durchführen.

## Kurzfazit

Die lange Ausführung liefert nützliche technische Diagnosedaten, ist aber kein vollständiger oder wissenschaftlich vergleichbarer Ergebnislauf. Energie war aktiviert, wurde jedoch nie gestartet. Ein ungültiges YOLOv7-Benchmarkset brach die komplette Native-Stufe vor dem ersten Transfer ab. Mehrere zusätzliche Quality-, Scope-, Case- und Reportfehler hätten eine vollständige Auswertung ebenfalls verhindert.

Der Hailo-10H-Befund beweist nicht, dass der Chip grundsätzlich langsam ist. Der aktuelle Runner liefert Detection-Boundaries hostseitig als `float32`, während Hailo-8 sie quantisiert als `uint8` belässt. Der geplante eigenständige A/B-Test isoliert genau diesen Unterschied.

## 1. Energie war aktiviert, wurde aber nicht gestartet

Der aufgelöste Plan bestätigt:

```text
native_energy_requested: true
native_energy_enabled: true
generic_energy_enabled: false
measurement_path: native_only
physical_scope: full_system
```

`full_system` bezeichnet, **was** u.RECS misst. `native_only` bezeichnet, **in welcher Workflow-Stufe** der Collector gestartet wird. Die lange Generic-Stufe wurde deshalb absichtlich nicht mit Energie erfasst. Die Energiemessung sollte erst innerhalb von `run_native_producers` beginnen.

Diese Stufe stoppte nach rund `0.038736 s`:

```text
selection_errors: ["benchmark_set_invalid:yolov7_ultralytics"]
failure_class: native_selection_preflight
transfer_attempted: false
started_remote_count: 0
started_performance_count: 0
```

Folge: Kein Native Runner, kein u.RECS-Collector und keine Messung wurden gestartet. Sämtliche Energy-CSVs sind leer beziehungsweise enthalten nur Kopfzeilen.

Daneben waren bereits neun zentrale Quality-Aufträge technisch fehlgeschlagen. Der aufgelöste Vertrag enthält:

```text
technical_quality_error: hard_fail
native_energy_after_technical_error: blocked_before_transfer
```

Dieser zweite Blocker wurde im konkreten Lauf nicht mehr ausgeführt, weil der YOLOv7-Preflight zuerst zurückkehrte. Nach alleiniger Entfernung von YOLOv7 hätte er Energy aber weiterhin verhindert.

### Erforderliche Korrektur

1. Native-Auswahl modelllokal durchführen.
2. Ein ungültiges Modell als `skipped/failed` markieren und gültige Modelle weiterlaufen lassen.
3. Quality-Fehler nur an die betroffene Modell-/Case-Zeile binden.
4. Technisch gültige Rohenergie messen und deren Claim-Eignung separat kennzeichnen.
5. Einen tatsächlichen Laufgrund ausgeben, zum Beispiel:

```text
Energy requested, not started: Native preflight blocked by yolov7_ultralytics
```

Hierfür sind keine neuen Provenienzartefakte erforderlich.

## 2. Quality-Fehler

Von 53 Quality-Aufträgen wurden 44 technisch abgeschlossen; neun scheiterten.

Fünf Generic-Composed-Requests für `mobilenet_v3_large`, `resnet50`, `yolo11l`, `yolo26m` und `yolo26s` melden:

```text
request lacks duplicated producer binding preprocessing_contract_sha256
```

Der Wert existiert bereits in `producer_identity`. Der bestehende Request-Builder muss denselben Wert lediglich auch in das bereits verlangte Top-Level-Feld übernehmen und die Gleichheit prüfen. Es wird kein neuer Hash berechnet.

Vier weitere Fehler stammen vom versehentlich aufgenommenen `yolo26x`:

```text
quality_reference_not_emitted
```

Zusätzlich wurden für YOLO26x nur 50 statt 500 Bilder ausgewertet. YOLO26x soll im nächsten regulären Profil wieder durch RegNet ersetzt werden; deshalb ist dafür zunächst kein spekulativer Runner-Umbau nötig.

Die zentrale Quality-Matrix ist nicht vollständig:

```text
required: 52
present: 23
complete: 20
claim_eligible: 0
overall_decision: not_evaluated
```

Die vorhandenen 500-Bild-Ergebnisse sind als Diagnose brauchbar, aber nicht als finale Backend-Rangliste.

## 3. Case- und Scope-Weitergabe ist inkonsistent

Mehrere ausgewählte Cases entsprechen nicht den ausgeführten Cases:

| Modell | ausgewählt/erwartet | ausgeführt |
|---|---:|---:|
| YOLO11l | `b062` | `b067` |
| YOLO26m | `b398` | `b072` |
| YOLO26s | `b364` | `b024` |

Für alle Modelle gilt außerdem:

```text
authoritative_scope_injected_run_count: 0
```

Selbst die physisch vollständigen ResNet50-Messungen erscheinen deshalb im Required-Scope-Vertrag als acht fehlende Zeilen.

### Erforderliche Korrektur

- Nach Backfill genau eine finale Accepted-Case-Liste erzeugen.
- Diese Liste vor dem Dispatch in Plan und Run-Deskriptoren injizieren.
- `selected_case_id == dispatched_case_id == executed_case_id == reported_case_id` vor und nach der Ausführung prüfen.
- Scope- und Case-Probleme modelllokal behandeln.
- Für YOLOv7 zunächst den bekannten kompatiblen Pfad `yolov7_paper/b066` verwenden. Die Multi-Input-Unterstützung für `yolov7_ultralytics` ist ein separates Vorhaben.

## 4. Report-Artefakte werden nach ihrer Registrierung gelöscht

`aggregate_results` erzeugt und registriert unter anderem:

```text
reports/prediction_vs_benchmark.csv
reports/validation_summary.csv
```

Eine spätere Legacy-Cleanup-Liste entfernt diese Dateien, obwohl Jobplan, Root-Outputs, Aggregate-Stufe, Run-Manifest, Dashboard und Artifact Index sie weiterhin erwarten. Der Finalizer meldet deshalb:

```text
artifact_index_registered_file_missing:reports/prediction_vs_benchmark.csv
```

### Erforderliche Korrektur

Beide Dateien aus der Legacy-Cleanup-Liste entfernen und erhalten. Eine Deregistrierung wäre größer und riskanter, weil mehrere aktive Verbraucher die Dateien weiterhin verwenden. Es ist keine Ersatzdatei und keine zusätzliche Integritätsstufe nötig.

## 5. Weitere akute Laufprobleme

- Der sichtbare Bericht enthält 63 Zeilen, aber nur 36 physisch gemessene Endpunkte. Unscoped- und setup-scoped Projektionen erzeugen Duplikate.
- Die gespeicherten FPS haben nicht überall dieselbe Semantik. Beispiel ResNet50 TensorRT-Split: Report `283.17 FPS`, Runner-Pipeline/Makespan `142.01 FPS`.
- Hailo-8-Cycle-FPS liegt systematisch ungefähr 9 % über der gemessenen Makespan-FPS.
- `yolov7_ultralytics` erzeugte 348 Kandidaten, aber keinen zulässigen Single-Part2-Input-Case. Trotzdem lief vorher unnötig schwere Erzeugungsarbeit.
- 78 Hailo-Buildversuche scheiterten wiederholt am selben lokalen Speicher-Preflight. Benötigt waren rund 61.1 GB; verfügbar waren nur ungefähr 46 bis 34 GB.

### Kleine Korrekturen

- Bei `candidate_pool_size == 0` vor Prefetch und Compilerarbeit abbrechen.
- Einen Low-Disk-Fehler einmal pro Dateisystem erkennen und weitere lokale Builds dort überspringen; vorhandene Cache-Treffer weiterhin zulassen.
- Eine einzige, eindeutig benannte FPS-Kennzahl für Vergleiche verwenden: gemessene End-to-End-Makespan-FPS. Cycle-/Modell-FPS nur zusätzlich ausgeben.
- Projektionsduplikate nicht als zusätzliche physische Messungen zählen.

## 6. Hailo-10H-Leistungsbefund

Der aktuelle Lauf zeigt:

| Merkmal | Hailo-8 | Hailo-10H |
|---|---|---|
| Runtime-API | VStreams | InferModel |
| Detection-Ausgabe am Host | quantisiertes `uint8` | dequantisiertes `float32` |
| Boundary-Modus | `raw_uint8_hailo` | `canonical_float32` |
| typische Detection-Stage 1 | ca. 3.3–5.1 ms | ca. 63.8–121.1 ms |

Die materialisierte Boundary ist beim Hailo-10H viermal größer:

| Modell | Hailo-8 | Hailo-10H |
|---|---:|---:|
| YOLO11l | 1.64 MB | 6.55 MB |
| YOLO26m | 3.28 MB | 13.11 MB |
| YOLO26s | 0.82 MB | 3.28 MB |

Das ist nicht automatisch viermal mehr Device-zu-Host-PCIe-DMA. HailoRT kann das native quantisierte Device-Ergebnis hostseitig in Float32 transformieren. Sicher belegt sind jedoch viermal größere Host-/Boundary-Puffer sowie zusätzliche Dequantisierungs- und Kopierarbeit.

`InferModel` ist für Hailo-10H grundsätzlich der richtige API-Pfad. HailoRT erlaubt pro Stream `AUTO`, `UINT8`, `UINT16` oder `FLOAT32`. DFC/HEF bestimmt die native Aktivierungspräzision; der Runtime-Pfad bestimmt die Hostdarstellung. Eine Float32-Hostausgabe ist daher nicht grundsätzlich erzwungen.

Vierfache Boundary-Größe erklärt noch keine 10- bis 20-fache Stage-Latenz. Zusätzlich zu prüfen sind synchrone Wartezeiten, Buffer-/Binding-Reuse, Hosttransformationen und die Zahl gleichzeitig laufender Jobs.

Offizielle Referenzen:

- HailoRT Format und Quantisierung: <https://github.com/hailo-ai/hailort/blob/master/hailort/libhailort/include/hailo/hailort.h#L574-L594>
- Python InferModel `set_format_type` und Quant-Infos: <https://github.com/hailo-ai/hailort/blob/master/hailort/libhailort/bindings/python/platform/hailo_platform/pyhailort/pyhailort.py#L2125-L2399>
- Async-InferModel-Beispiel: <https://github.com/hailo-ai/hailort/blob/master/hailort/libhailort/examples/cpp/async_infer_advanced_example/async_infer_advanced_example.cpp>

## 7. Eigenständiger Hailo-10H-A/B-Test

Das zugehörige Testpaket vergleicht auf demselben HEF und denselben synthetischen Eingaben:

- A: `InferModel` mit Float32-Hostausgabe.
- B: `InferModel` mit quantisiertem VStream und dem nativen Elementtyp des zugrunde liegenden HEF-Streams (`UINT8` oder `UINT16`); die VStream-Order bleibt gleich.

Erfasst werden:

- tatsächliches Ausgabeformat und NumPy-Dtype,
- Hostpuffergröße pro Frame,
- sequenzielle Latenz,
- asynchroner Durchsatz mit identischer Inflight-Tiefe,
- Dequantisierungszeit außerhalb des gemessenen nativen Inferenzpfads,
- numerische Abweichung zwischen Float32-Ausgabe und nachträglich dequantisierter nativer Ausgabe.

Der Test verändert weder das Tool noch das HEF und benötigt keine Energiemessung. Als erster technischer Test dient das bereits vorhandene YOLO26s-`b024`-Part1-HEF. Dieser Case wird ausschließlich zur Ursachenanalyse verwendet und nicht als neuer wissenschaftlicher Ergebnislauf gewertet.

Zusätzliche Interpretation: Ist schon Variante A im eigenständigen Test wesentlich schneller als die im v2.79.14-Lauf beobachteten rund `63.85 ms` beziehungsweise `15.55 FPS`, liegt der dominante Verlust im Produkt-Runner oder seiner Boundary-Verarbeitung und nicht im bloßen Einsatz von `InferModel`.

## 8. Reihenfolge der Fortsetzung

1. Eigenständigen Hailo-10H-A/B-Test ausführen.
2. Beide erwarteten Report-CSVs erhalten.
3. Bestehendes Producer-Binding-Feld korrekt in Requests übernehmen.
4. Finale Case-Liste und authoritative Scope korrekt injizieren.
5. Native- und Energy-Gates modelllokal machen.
6. Profil korrigieren: RegNet statt versehentlichem YOLO26x; `yolov7_paper/b066` verwenden.
7. Kleine Offline- und Einmodell-Smokes.
8. Erst danach einen neuen vollständigen Lauf starten.

## Für die spätere Implementierung noch erforderlich

Der Debug-Pack reicht für diese Fehlerklassifikation und den eigenständigen A/B-Test. Für Änderungen am Produktcode wird anschließend die exakte aktuell installierte Source-Basis benötigt. Der hier verfügbare Debug-Pack enthält nicht den vollständigen v2.79.14-/v2.79.15-Quellbaum.
