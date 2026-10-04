# Daten, Kohorten und Ausschlüsse

Stand: 04.10.2026. Dies ist eine neue explorative Ableitung der geschlossenen THESIS20-Kampagne. Historische Referenzausgaben und Toolrelease v2.92.0 bleiben unverändert. Die Quelldateien sind die kompakte veröffentlichte Produktprojektion aus Ergebniscommit `e7bd8d82283034efa8bdaddf9dc987d3008d4885`; eine unveränderte Kopie liegt unter `source/`. Die vorhandenen Produktionsreader wurden für diese ursprüngliche Projektion verwendet. Die neue portable Reproduktion braucht weder private Roh-Parquets noch Hardware.

## Getrennte Quellenrollen

| Rolle | Inhalt und Nenner |
|---|---|
| BASE | 588 ursprüngliche Generic-Sollfälle = 527 gemessen + 37 Buildfehler + 24 Policyfälle; 499 Raw-Splits und 28 Completed-Fulls getrennt |
| CORRECTED | Korrigierte bestehende Basisprojektion einschließlich F01–F06, 548 Qualityresultate, 234 Native-/Energiefälle |
| COMPLETION192 | 192 Generic-Completed-Task-Fälle, 576 Wiederholungen; referenziert bereits gemessene Nativefälle, erzeugt keine weiteren Nativebaselines |
| YOLO | Zwölf postgeplante zusätzliche Splitfälle, 36 Native-/36 Generic-/36 Energiereplikate; zwölf separate kurze Rohoutputvorläufe bleiben reine Inventur |
| Augmentierte Vereinigung | 204 Splits und 42 genau einmal gezählte Fulls; 246 Nativefälle/738 Reps, 204 Generic-Completionfälle/612 Reps/612.000 Tasks, 246 Energiefälle/738 Reps; keine Summierung der Union mit ihren Teilmengen |

Quality enthält 560 Ergebnisse = 548 Basis + 12 Zusatz: 521 reference_close, 39 accuracy_loss. Die 261 Top1- und 299 AP50:95-Ergebnisse bleiben getrennte Metriken. Original N5000, B1000, Seed20260710, originale Intervalle und Entscheidungen sind erhalten. Die eingefrorene Reportingpolicy `accuracy_reporting_v1` nutzt 5% relativen Punktverlust; die separat gespeicherte absolute Taskmargin 0,01 ist kein Ersatz für diese Reportingregel. Beide stehen in `inputs/quality_policy_details.csv` und `tables/quality_effects.csv`.

## Vergleichsfilter

| Filter | Fälle | Bedeutung |
|---|---:|---|
| Generic↔Native technical | 204 | bestehender technischer Paar-Gate |
| Generic↔Native qualitytransfer | 201 | zusätzlicher bestehender Transfer-Gate, enthält auch gültige accuracy_loss |
| Nur beiderseits reference_close, ohne Transferfilter | 187 | reine Accuracyentscheidung; für Energie als zusätzliche Ansicht geführt |
| reference_close mit bestehendem Transfer-Gate | 184 | keine Rückfüllung der drei ausgeschlossenen Zusatzpaare |
| Split↔Full deskriptiv | 408 | 204 Splits × zwei Fulltypen, **42** geteilte Fullmessungen |
| Split↔Full semantisch bestätigt | 392 | 188 Vendor + 204 TRT; 16 Grenzen individuell erhalten |
| Semantik + Split und Full reference_close | 327 | 140 Vendor + 187 TRT; andere Population als 184er-Transferfilter |

Die drei trotz reference_close ausgeschlossenen Transferpaare sind in der tatsächlichen Eingabe als **augmentation** markiert: YOLO11l/H8 b120, YOLO26s/H10 b038, YOLOv7/DeepX b044. Das ungenaue historische Wort „Startpaare“ wird nicht in eine falsche Basezuordnung übersetzt. Nach diesem Filter enthalten drei YOLO-Gruppen nur n=2; daher haben nur 18 Gruppen n≥3 (178 der 184 Kandidaten). Alle 21 Gruppen bleiben in den Tabellen auffindbar. Keine Auswertung nennt Top3 bei n=3 eine Auswahlleistung.

## Qualityrollen und eindeutiger Join

39 Accuracyverluste = neun Vendor-Full-Verluste + 17 Completed-paarbare Splitverluste + 13 Native-unsupported-Splitverluste. Der varianten- und backendgerechte Splitjoin bestätigt alle 204 Pairflags (187 close / 17 loss). Full-Companions können dieselbe boundaryartige `case_id` wie ein Split tragen; `variant` ist zwingend Teil des Qualityschlüssels. Das historische Qualitylabel `vendor_full` umfasst außerdem 28 TRT-Full-Ergebnisse, weshalb der Backendtyp mitgelesen wird. Die neun Fullverluste sind tatsächlich H8/H10-Vendorfälle. Beispiel: YOLO11l/H8 b003, Fullverlust 5,424% vs Splitverlust 1,993%. `quality_pair_join_audit.csv` sichert die Rollen.

## Identitäten und Messgrenzen

Ranggruppen verwenden Modell, Setup, Richtung, Boundarypräzision, Vergleichsbackend, bestehenden Completed-Endpoint-Vertrag und Zeitgrenze. Energie ergänzt Kalibrierung, physikalischen Full-System-Scope und aktives Fenster. Die ursprünglichen Produktpaare sind die Autorität für Input-/Endpunktkompatibilität. Bei den 36 Detektionspaaren unterscheiden sich die wörtlichen kompakten Generic-/Native-Endpunktlabels; ihre bestehenden Paarverträge, nicht Zeichenketten-Gleichheit, tragen den Vergleich. Dies wird nicht durch einen neuen positiven Gate ersetzt.

Historical Raw enthält keine vollständig befüllten Precision-/Endpointfelder. Der eindeutige Modell/Fall/Setup/Backendjoin (expliziter DeepX-Alias) wird zusätzlich gegen die eingefrorene Roh-FPS-Projektion jedes ursprünglichen Completionplans geprüft: 192 gemeinsame Identitäten. Fehlende Rawmetadaten werden nicht erfunden; zwölf kurze Zusatzvorläufe bleiben ausgeschlossen.

Die neun Kombinationen dreier Wiederholungen sind abhängige Sensitivitätswerte, keine neuen Studien oder Konfidenzintervalle. Tausend Tasks innerhalb eines Replikats bleiben ein Timingexperiment. Gleiches gilt für Leistungssamples. Für Energie sind E/N, E/T und N/T an dasselbe reale Fenster gebunden; Primäraggregation bleibt das Mittel dreier Einzelquotienten.

## Zusätzliche kompakte Projektionen

`extract_quality_graph.py` liest ausschließlich gespeicherte kleine Qualitäts-/Analyseberichte: 560 Quality-Policy-/Intervallzeilen, 2.111 vorhandene Graphkandidaten und 228 dokumentierte unsupported-Fälle. Alle 204 Completed-Fälle und 511 Quality-Splits haben Graphfeatures. Normierte topologische Position ist (zero-based boundary+1)/node_count; sie ist kein Zeit- oder Rechenanteil. Gespeicherte FLOPs-/Bottleneck-/Streamproxies sind analytische historische Prognosen, keine neu gemessenen Stagezeiten. Das gespeicherte Kalibrierprofil bleibt sichtbar und wird nicht als passende Validierung für jedes Modell ausgegeben.

228 Nativefälle sind terminal wegen `part2_input_count_not_one` ausgeschlossen. Diese systematische Fähigkeitsauswahl und die postgeplante YOLO-Erweiterung sind keine zufällig fehlenden Daten. 37 Buildfehler und 24 Policyfälle sind eigene Generic-Scopekategorien, keine Accuracyfehler.

Die genaue private Pfadzuordnung liegt außerhalb des Reviewpakets. Reproduktion, Originalmargen, Negativbefunde, Semantikgrenzen und Vorher/Nachher-Audit der gemischt benannten Legacy-Energiespalte sind vollständig in den kleinen öffentlichen Tabellen enthalten.
