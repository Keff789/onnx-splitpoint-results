# R9B-Restabnahme – Abschluss der Fortsetzung

Maßgeblicher Auftrag: ${CONTROLLER_HOME}/.local/share/onnx-splitpoint-codex/v283_R9B_Restabnahme_20260917_084323_PgRFm8. Fortsetzung desselben Budgets; ursprüngliche Marker, Journale und Rohdaten erhalten. Kein Commit, Push, Reset oder Versionswechsel.

## Ergebnis und Ursachen

BACKFILL-02: Der alte externe Helfer verlangte forced_cases=b364 und widersprach dem gewünschten Backfill. Das korrigierte Profil und der Helfer lassen jetzt die normale Reserve frei. Im echten H8-Lauf wurden b364/b365 ausgeschlossen und b021 mit vorhandenen Modellartefakten ausgeführt; 3/3 Native-Zeilen und GUI-Abschluss sind belegt.

DeepX-P2: Die frühe pauschale Abweisung identischer Sourcehashes blockierte eine belegte FLOAT/as_input-No-op-Brücke. Der enge Fix führt ausschließlich diesen Fall durch den vollständigen vorhandenen Native-Bindingvalidator. Parenthash/-größe, Modell/Case/Setup/Backend/Task/Precision, Enginebytes, ABI, Shapes, Policy, Namespace und Crosslinks bleiben Pflicht. UINT8-Cast-/Dequant-Ausnahmen wurden nicht erweitert. Beide lesenden Gerätepreflights liefern strikten HIT.

Versionsmetadaten: Die aktuelle Source bindet __version__ bereits an release_identity.VERSION. Frischer Import ergibt 2.83; kein Sourcealiasfehler reproduziert, keine neue Versionsänderung. Die frühere abweichende Importbeobachtung wird nicht nachträglich einer unbelegten Ursache zugeschrieben.

## Änderungen und lokale Nachweise

Produktcode: onnx_splitpoint_tool/benchmark/remote_run.py. Regressionen: tests/test_v283_r9b_restabnahme.py und tests/fixtures/v283_r9b_deepx_noop.json. Dokumentation: docs/ARBEITSSTAND.md; vorhandene SOURCE_MANIFEST.json/SHA256SUMS.txt aktualisiert. Externe Profile, import-/spawn-sicherer Bedienhelfer, H8-Tk-/Queue-/Generatorprüfungen und begrenzte Geräteprüfhelfer sind mitgeliefert. Der kumulative Diff beginnt am gespeicherten Auftragsstart, nicht an HEAD mit dessen älteren uncommitteten Änderungen.

Finale Produktauswahl: **971 PASS, 0 FAIL, 0 SKIP**, 219,475 s; alle bisherigen 939 Knoten erhalten. Separate **26 Tk-Knoten PASS, 0 FAIL, 0 SKIP**, 178,835 s. Weitere 3 unveränderte Bridge-/Bindingknoten PASS. Fünf einzigartige lokale H8-Fälle PASS; zunächst 3 falsche Statusassertionen auf infrastructure_blocked wurden auf das bei Kaltbuildbudget 0 tatsächliche build_budget_exhausted korrigiert. Kein Produktgate geändert. Alle Erstfehler und Folgeläufe bleiben als JUnit/JSON erhalten; Wiederholungen werden nicht addiert.

H8-Lokalnachweis: echte Editorvariablen/Callbacks, Snapshot und Queueoptionen; Workflowthread vor Start angehalten. Produktresolver bewahrt [364,365,21,…], Quote 1, exact=False. Separater echter Generator verwendet diese aus Queueoptionen aufgelöste Reserve und Originalnegativbelege bis zur Backendmatrix; Materializer-Handoff ergänzend statisch geprüft. Kein vollständiger lokaler Hardwareworkflow behauptet. Echter ManagementQualityService-Spawnworker exitcode 0; Import erzeugt weder GUI noch Marker oder Start.

## Reale normale GUI-Abdeckung

| Zelle | Start | Native erfolgreich | Split ausgeführt | Technik | Quality | Finalisierung | Dauer |
|---|---:|---:|---|---|---|---|---:|
| hailo8_detection | 1 | 3/3 | b021: True | ok | fail | pass | 538.969 s |
| deepx_classification | 1 | 3/3 | b135: True | ok | inconclusive | pass | 474.833 s |
| deepx_detection | 1 | 3/3 | b062: True | ok | fail | pass | 510.226 s |

Die oben einzeln ausgewiesenen Zellen belegen ihren jeweiligen Verlauf vom normalen Startknopf über Queue und Runner bis zu Nativezeilen, Export und terminalem Dialog. Screenshots, Widgettext, Journal und Cleanupbelege liegen bei. Quality FAIL/INCONCLUSIVE werden unverändert ausgewiesen; technische Durchführung ist keine Qualitätsfreigabe.

MobileNet: Zusätzlich bleibt die vorhandene optionale Legacy-Validierungswarnung für eine TRT-Full-Zeile dokumentiert; der separate native TRT-Full-Pfad besteht Runtime-/Struktur-/Qualitygates. Der GUI-Text Scientific ready=True wird angesichts der Qualitätsentscheidung INCONCLUSIVE nicht als wissenschaftliche Freigabe übernommen.

## Latenzen aus Rohpaaren

| Zelle / Backend / Case | Paare | Semantik | Mean ms | P50 ms | P95 ms |
|---|---:|---|---:|---:|---:|
| deepx_classification / deepx_to_trt / b135 | 100 | Hostoutput ohne Top-k | 2.092954 | 2.007623 | 2.086204 |
| deepx_classification / native_full_deepx / full | 100 | Hostoutput ohne Top-k | 1.509901 | 1.505653 | 1.534267 |
| deepx_classification / native_full_tensorrt / full | 0 | unavailable | unavailable | unavailable | unavailable |
| deepx_detection / deepx_to_trt / b062 | 100 | Taskabschluss | 117.542954 | 123.239755 | 124.203195 |
| deepx_detection / native_full_deepx / full | 100 | Taskabschluss | 47.368797 | 47.377479 | 47.574537 |
| deepx_detection / native_full_tensorrt / full | 100 | Taskabschluss | 27.508763 | 27.489994 | 27.734013 |
| hailo8_detection / hailo8_to_trt / b021 | 100 | Taskabschluss | 26.753192 | 27.375758 | 27.415302 |
| hailo8_detection / native_full_hailo8 / full | 100 | Taskabschluss | 46.112306 | 46.088751 | 46.284652 |
| hailo8_detection / native_full_tensorrt / full | 100 | Taskabschluss | 6.737188 | 6.731160 | 6.770212 |

Mean/P50/P95 jeweils aus 100 eindeutigen zugehörigen monotonen Start-/Endpaaren nachgerechnet, Warmup ausgeschlossen; keine Ableitung aus 1/FPS. Rohpaare und getrennte FPS stehen in latency_matrix.json/LATENZ_ERGEBNISSE.csv. N=1 ist keine Population unabhängiger Wiederholungen. Fehlende TRT-Classificationpaare bleiben unavailable.

## Budgets, Installationsbindung und Grenzen

Kumulativ maximal drei Geräte-GUI-Starts, pro Ziel einer; keine Wiederholung. Zwei dedizierte lesende DeepX-P2-Preflights verbraucht (2,426/4,883 s). Die normalen GUI-Ketten führen zusätzlich ihre unveränderten verpflichtenden Cachegates aus; diese sind in den jeweiligen Runreports separat belegt. Eine notwendige H8-C++-Wrappergeneration (9,318 s), anschließend gebundener Reuse. Vorherige passende Generation im Remote-Ergebnisroot nicht vorhanden. Null neue HEF/DXNN/TRT-Engines, null Energie, null Force/Rebuild oder Nachtlauf. Native 100/10/1 und Quality maximal 32 Bilder/100 Bootstrap; bestehende Seeds, Margen, Queue/Inflight und Power unverändert.

MAIN_INSTALLATION_FINAL.json belegt Imports aus dem Hauptrepo, Version 2.83/Build v2.83-r9b-request-latency, Source-/Installedverifier, Script-Mirrors und aktive normale Configpfade. SOURCE_BEFORE_HARDWARE.json bindet 926 Produktdateien; nach Hardware wurden nur Dokumentation/Manifeste finalisiert. HEAD und getrackter Indexinhalt unverändert (anfangs ungestagt, finaler cached Diff leer; kein anfänglicher Binärhash der Indexdatei); voller git status --short und git diff --stat liegen als GIT_STATUS_FINAL.txt und GIT_DIFF_STAT_FINAL.txt bei. Der bereits vorher stark geänderte Arbeitsbaum wurde erhalten.

Bewusst nicht ausgeführt: H8/MobileNet oder H10 erneut, volle Testsuite außerhalb der beauftragten Auswahl, neue Modellbuilds, weitere P2-Preflights, GUI-Retries, Energie- oder Langzeitkampagnen. Frühere H10-/H8-Belege bleiben historisch. Classification-Top-k, TRT-Classificationpaare, H10-/DeepX-Numerik, Qualitätsforschung, Papervergleich, Ranking und finale Langzeitenergie bleiben spätere Aufgaben.

Empfohlene nächste Aktion: Diese begrenzte Restabnahme anhand von GUI_COVERAGE.json, Rohpaaren und strikten Bindingbelegen prüfen. Keine automatische Folgekampagne. Offene wissenschaftliche Punkte benötigen einen eigenen Auftrag.

Lieferung: ERGEBNISSE_R9B_RESTABNAHME_FORTSETZUNG.zip mit kumulativem Auftragsdiff, geänderten Sources, alten und neuen Belegen sowie Größen-/SHA256-Inventar. Keine Modelle, Schlüssel, Enginebinaries, Bildkorpora oder großen Roharrays.
