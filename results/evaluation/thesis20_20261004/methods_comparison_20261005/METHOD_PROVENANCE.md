# Methoden, eingefrorene Parameter und Grenzen

Diese ergänzende Auswertung vom 05.10.2026 ist **post hoc**. Sie bewertet vorhandene Verfahren und gespeicherte Prognosen ohne neue Messungen, Optimierung oder Kalibrierung. Begriffe wie „pre-registered“ in übernommenen historischen Moduldocstrings beschreiben deren ursprünglichen Designkontext, keine Präregistrierung dieser neuen Auswertung. Der tatsächlich eingefrorene Workflowselector heißt `cut_bytes_only`; die Messkohorte entstand zusätzlich durch `stratified_windows` und technische Unterstützung, nicht durch die globale Top1-Auswahl jeder hier verglichenen Methode.

## Tatsächlich gelesene Quellen

`BASE/profile.yaml` und `BASE/profile_source.yaml` enthalten dieselbe `ranking_validation`-Konfiguration. Die Gewichte sind **w_comm=1, w_imb=3, w_tensors=0.2, log_comm=true**. Die aktuellen GUI-Regler 2/0.1/10 werden nicht verwendet. Ein Rankingmodellbundle ist nicht konfiguriert; `stage_time_models` und `backend_throughput_gops` sind leer. Die generischen und nativen `handover_models` enthalten keine expliziten Fits.

Die sieben `BASE/models/<model>/analysis/candidate_ranking.json` liefern insgesamt **2.111** gespeicherte Graphkandidaten: MobileNetV3-L 138, RegNetX-1.6GF 133, ResNet-50 120, YOLO11l 615, YOLO26m 416, YOLO26s 382, YOLOv7 307. Alle haben `strict_ok=true`. `analysis.json` und `selection_input.json` beschreiben die Graph- und Auswahlsicht. In allen sieben `BASE/models/<model>/benchmark_set/legacy_benchmark_set.json` ist **system_spec=null**.

`inputs/method_parameters.json` enthält nur die relevanten Parameter, relative Quellpfade, ursprüngliche Artefaktbezeichner und die SHAs dieser kleinen Originalmetadaten. `inputs/method_graph_features.csv` enthält die benötigten numerischen Felder und originale Reihenfolgen; keine Modelle, Images oder Roh-Parquets. Die vorangegangenen öffentlichen Ergebnisinputs werden über `--source-root` referenziert und nicht nochmals vollständig kopiert.

Die vorhandenen reinen Definitionen aus Toolcommit `d164aad6d7c7ef68c1b371c49a1fdea0a3b27dd7` (v2.92.0) sind unverändert unter `scripts/method_core/` enthalten: `ranking_methods.py`, `objective_scoring.py`, `system_model.py`, `units.py`. `inputs/method_code_provenance.json` dokumentiert die Kopien. Es wird kein altes Paket installiert/importiert und kein ONNX-Analyse-/Benchmarkentry aufgerufen. Reproduktion verwendet nur diese reinen Scorefunktionen und gespeicherte Zahlen. Der heutige Toolcommit wird nicht rückwirkend als ausgeführter Messstand behauptet.

## Verfahren und Verfügbarkeit

`inputs/method_availability.csv` enthält **189 Zeilen = neun Verfahren × sieben Modelle × drei Setups**. `method_candidate_scores.csv` enthält **14.777 Zeilen = sieben statische Verfahren × 2.111 Graphkandidaten**. Da die hier beurteilten historischen statischen Scores tatsächlich in allen drei Setups gleich sind, steht dort explizit `setup_id=all`; die Verfügbarkeitsmatrix bindet diese Projektion an jedes Zielsetup. Dies ist keine Behauptung identisch passender Hardwareparameter.

| ID | Primärer Wert, bessere Richtung | Quelle / Behandlung |
|---|---|---|
| `cut_bytes_only` | geschätzte Graphbytes, kleiner | Vorhandene `candidate_cut_bytes`-Definition; alle 2.111 gespeichert. |
| `weighted_score` | dimensionsloser gewichteter Score, kleiner | Deterministische Neuberechnung mit belegten alten 1/3/0.2-Gewichten. Normierung im **vollständigen jeweiligen Modelluniversum**, vor jedem Mess-/Qualityfilter. |
| `onnx_real_boundary_hardware_aware` | gespeicherter Accelerator-Fit-Score, kleiner | Alle Originalzeilen tragen das **Hailo10→TensorRT-Profil**. Diese tatsächlich gespeicherten Scores bleiben für alle Zielsetups erhalten; keine nachträgliche Umparametrisierung auf H8 oder DeepX. |
| `cycle_time_no_handover` | gespeicherter heuristischer Bottleneck in ms, kleiner | Existierende `candidate_bottleneck`-Fallbackdefinition; keine gemessenen Stagetimings und keine gerätespezifisch gefitteten GOPS. |
| `cycle_time_with_handover` | nicht verfügbar | Native-FIFO-Handovermodell unkonfiguriert, keine gespeicherten nativen Handoverprognosen. `None` bleibt fehlend; die generische Heuristik wird nicht als Native-Fit eingesetzt. |
| `stored_predicted_stream_fps` | gespeicherte heuristische Rate, größer | Eigene Definition `1000/(bottleneck + calibrated_handover)` mit `yolov7_streaming_v1` und historischer Hailo10-Richtung; kein unabhängiger Fit pro Modell oder Setup. |
| `gui_total_latency` | nicht verfügbar | `SystemSpec.estimate_boundary` gelesen, aber Original-SystemSpec siebenmal null. Aktuelle GUI-Werte oder rekonstruierte freie Parameter werden nicht untergeschoben. |
| `measured_generic_raw` | tatsächlich gemessene historische Raw-Rate, größer | Nur die 192 ursprünglichen exakt gebundenen Raw/Completion-Identitäten; zwölf kurze Ergänzungsvorläufe ausgeschlossen. |
| `measured_generic_completion` | tatsächlich gemessene Completed-Task-Rate, größer | Vorhandene 204 Fälle und unveränderte Mediane als Vergleich und Regressionskontrolle. |

Die beiden gemessenen Verfahren werden vom Gruppen-Evaluator direkt aus der bereits veröffentlichten Paartabelle gelesen; sie werden nicht als neue Graphprognosen in der Scorematrix dupliziert. Native-Qualitytransfer und beidseitig reference_close bleiben zusätzliche vorhandene, voneinander getrennte Filter.

### Gewichtete Heuristik und Reihenfolge

Die bestehende Funktion `compute_ranking_predictions` normalisiert drei Terme per Min/Max über das jeweilige vollständige Modelluniversum: `log10(1+cut_bytes)`, gespeicherte Rechenungleichheit und `max(n_cut_tensors−1,0)`. Danach gilt `1*comm_norm + 3*imbalance_norm + 0.2*tensor_norm`. Eine erneute Normierung nur innerhalb der gemessenen oder referenznahen Teilmenge würde die effektiven Gewichte und unter Umständen die Sieger verändern; sie wird ausdrücklich nicht durchgeführt.

Die vorhandene deterministische Methodentieordnung ist **Boundaryindex, danach Case-ID**, nachweisbar in `_candidate_identity_tie_key` und `compute_ranking_predictions`. `original_order` enthält deren aufsteigenden Rang; `source_list_order` bewahrt unabhängig davon die originale Reihenfolge in `candidate_ranking.json`, die bereits nach dem Workflowselector sortiert ist. Gemessene Generic-Proxies behalten die Reihenfolge der ursprünglichen Paartabelle. Exakte Gleichstände werden nicht durch Rundung erzeugt. Die ergänzende Tie-Sensitivität kann beide gespeicherten Ordnungen und sämtliche gleich guten Topkandidaten prüfen.

### Historisches Hardwareprofil

Alle 2.111 gespeicherten Accelerator-Fit-Profile lauten stage1=`hailo10`, stage2=`tensorrt`, low=.25, ideal=.42, high=.58, hard_high=.72, cut_free_mib=10, cut_soft_mib=20, over_w=2.2, under_w=.6. Der Workflowpfad `_analysis_stage_pair_for_targets` priorisiert Hailo10, sobald Hailo10 und TensorRT im aktiven Zielsatz vorkommen. Das erklärt die gemeinsame gespeicherte Herkunft; es belegt keine individuelle Eignung für H8 und DeepX.

Die Originalwerte wurden für alle 2.111 Fälle gegen `accelerator_fit_metrics` mit genau diesem gespeicherten Profil nachgerechnet. Die Funktion konsumiert hier **`cut_mb_val` in dezimalen MB**, obwohl interne Schwellenbezeichner „mib“ heißen. Diese bestehende Einheiteninkonsistenz wird offengelegt und unverändert reproduziert; es wird keine still korrigierte neue Heuristik als historische Methode bewertet. Der reine Cut-Bytes-Ranker hat diese MB/MiB-Verwechslung nicht.

### Fallback-Latenz ist nicht das GUI-Systemmodell

Der tatsächliche vorhandene Workflowcode `_make_real_analysis_candidates` setzt:

```
predicted_total_latency_ms = 5 + total_flops / 1e10 + cut_bytes / 1e9
predicted_transfer_latency_ms = cut_bytes / 1e9
```

`candidate_objective_metrics` verteilt diese erste Heuristik nach dem größeren FLOP-Anteil auf den gespeicherten Bottleneck. `predicted_stream_fps` addiert die gespeicherte kalibrierte Übergabeheuristik und invertiert den resultierenden Cyclewert. Diese Herkunft wurde für alle 2.111 gespeicherten Total-/Bottleneck-/Streamwerte numerisch bestätigt. Sie ist weder eine vollständige Hardwarelatenzkalibrierung noch der GUI-Pfad.

`SystemSpec.estimate_boundary` summiert dagegen linkes Compute, modellierte Linkzeit, rechtes Compute und expliziten Overhead mit konfigurierten GOPS/Bandbreiten. Ohne die gespeicherte SystemSpec sind diese Parameter unbekannt. Die Formel wird deshalb **nicht** aus vorhandenen Prognosezahlen zurückgefittet. Die GUI-Prognose von 56,96 FPS für YOLOv7/b044 wird nicht mit den historisch gespeicherten 132,967447854 heuristischen FPS gleichgesetzt. Auch der latenzartige Fallback wird nicht als zusätzliche gemessene Zeit oder als GUI-Methode umbenannt.

### Was die Bytegröße aussagt

`cut_bytes` ist die gespeicherte Graph-/Tensorabschätzung. Der ursprüngliche Analysepfad nutzt ValueInfo-Formen und Tensor-Datentypbreiten, bei fehlender Typinformation den bestehenden Default; das konkrete per-Tensor-Dtypeinventar wurde nicht in `candidate_ranking.json` gespeichert. Deshalb wird weder pauschal „immer FP32“ noch „FP16“ als belegte universelle Runtimeprecision behauptet. `cut_mb_val=bytes/1e6`, `cut_mib_val=bytes/2^20` werden getrennt geführt.

Konkretes Gegenbeispiel: YOLOv7/b044 hat 6.553.600 gespeicherte Graphbytes. Der bereits veröffentlichte Originalpfadbeleg in `deep_analysis/inputs/ranking_path_evidence.csv`, Schlüssel `(yolov7_paper,b044,H8)`, nennt nur 1.638.400 TRT-Inputbytes bei `uint8_dequant_fp16`; die gezielt gelesene Runtimebindung beschreibt `[80,80,256]` UINT8 mit anschließendem Layout-/Dequantisierungsschritt. Weder Graphbytes noch diese gebundene Puffergröße sind eine neue Messung des gesamten PCIe-Verkehrs. Kopien, Layout und Hostverarbeitung werden nicht aus der Graphspalte erfunden.

## Globale Empfehlung und Messabdeckung

`tables/method_global_selection.csv` hält je Modell/Setup/Methode den **unveränderten globalen Top1 im ursprünglichen Graphuniversum** fest; fehlende Methoden behalten eine explizite Zeile. Der Sieger wird niemals durch den nächsten gemessenen Kandidaten ersetzt. Native-Performance und Quality bleiben leer, wenn der globale Sieger nicht in der Completed-Kohorte liegt. „Single-Input-Vertrag erfüllt“ bedeutet allein keine nachgewiesene Compiler-/Runtimeunterstützung.

Über die fünf auswertbaren statischen Verfahren entstehen 105 Modell/Setup/Methoden-Empfehlungen; davon besitzen **33** eine vorhandene Completed-Messung. Diese 105 sind keine unabhängigen Experimente: identische Graphscores wiederholen sich über die drei Setups. Für YOLOv7/H8 empfiehlt Cut-Bytes global b306 (zwei Top-Ties, per Boundaryordnung b306), das den Single-Input-Vertrag nicht erfüllt und ungemessen bleibt. Die gemessene Dreiermenge b009/b044/b066 ist davon getrennt.

`tables/method_yolov7_global_context.csv` zeigt zusätzlich b009, b044, b066 und das im Auftrag genannte GUI-Beispiel b298 in jeder verfügbaren statischen Rangfolge. b298 erhält keine erfundene Qualitäts-/Performancemessung und keinen neuen Messauftrag. Da keine Original-GUI-SystemSpec vorliegt, wird b298 insbesondere nicht als globaler Sieger des historischen GUI-Modells behauptet.

## Reproduktion und gezielte Prüfung

Kompakte Offlineableitung (keine privaten Quellen erforderlich):

```bash
python scripts/reproduce_method_scores.py --input-root . \
  --source-root ../ --output-root /path/to/new-derived-output
```

Dabei bezeichnet `--source-root` den bestehenden THESIS20-Analysebereich mit `inputs/completion_pairs.csv`, `generic_raw.csv` und `coverage.csv`. Die Ausgabe erzeugt die Scorematrix, Verfügbarkeitsmatrix, zwei globale Auswahltabellen und den Prüfnachweis neu; ursprüngliche Ergebnisse bleiben erhalten. Der Gruppen-Evaluator benutzt anschließend diese Scorematrix, unveränderte vorhandene Pairgates und tatsächliche Native-/Energiewerte.

Die optional erforderliche Originalmetadatenprojektion ist als `scripts/extract_method_inputs.py --base-root BASE --output-root NEW` dokumentiert. Sie liest nur die beiden eingefrorenen Profile und sieben Candidate-/SystemSpec-Metadatenpaare; keine Modelle oder Rohdaten. PyYAML wird nur für diesen optionalen Schritt benötigt.

**Sieben neue Projektionsprüfungen bestanden** (`tests/test_method_projection.py`): Byteeinheiten/keine Runtimeumrechnung; ursprüngliche Methodentieordnung; tatsächlich rangverändernder Fehler einer Teilmengennormierung als Negativtest; unkonfiguriertes Native-Handover trotz vorhandener Genericfelder; SystemSpec-Summenmetrik und ehrliches Fehlen; vollständige 2.111-Kandidaten-/Parameter-/Scoreregression; bytegleiche Reproduktion aller fünf Score-/Provenienzoutputs in zwei separaten temporären Verzeichnissen samt globalem No-Fallback-Negativfall. Aufruf:

```bash
THESIS20_SOURCE_ROOT=/path/to/existing/thesis20_20261004 \
PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider \
  tests/test_method_projection.py
```

Die separate Gruppen-/Energieauswertung ergänzt ihre eigenen Tests. Es wurde keine Toolvollsuite, Hardwareabnahme, Inferenz oder neue Bootstraprechnung ausgeführt.
