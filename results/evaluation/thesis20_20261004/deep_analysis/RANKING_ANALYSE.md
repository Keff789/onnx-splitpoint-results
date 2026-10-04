# Durchgeführte Rang- und Proxyanalyse B/C mit Gegenfällen F

Explorative, datierte Ableitung vom 04.10.2026. Der vor Detailrechnung geschriebene `ranking_plan.md` legt die untersuchten Ansichten fest. Keine Messung, Inferenz, Bootstrap-Neuberechnung oder Compileraktivität. Eingefrorene Originale und wissenschaftliche Claim-Gates sind unverändert.

## Population und genaue Metriken

204 technisch paarbare Splits (192 Basis + zwölf Augmentierung) stehen 201 Qualitytransfer-Fällen und 184 Fällen mit Qualitytransfer **und** beiden reference_close-Entscheidungen gegenüber. Die technische Sicht enthält 17 accuracy_loss-Fälle. Die drei zusätzlichen Gateausschlüsse sind YOLO11l/H8/b120, YOLO26s/H10/b038 und YOLOv7/DeepX/b044; ihre kompakten Quellen nennen ausdrücklich observation_origin=augmentation. Sie bleiben trotz reference_close ausgeschlossen.

Die 21 exakten Gruppen enthalten neun Klassifikationsgruppen mit n=17,19,20 und zwölf YOLO-Gruppen mit n=3. In der Basis erreichen nur drei YOLO26m-Gruppen n=3; übrige YOLO-Basisgruppen mit n=1 oder 2 bleiben als unzureichend sichtbar. Nach Qualitytransfer/reference_close haben drei augmentierte YOLO-Gruppen nur n=2. Deshalb bedeuten 201 Qualitytransfer-Fälle 18 auswertbare Gruppen mit zusammen 195 Kandidaten plus sechs weitere Kandidaten in drei unzureichenden Gruppen; reference_close entsprechend 178 plus sechs =184.

Stratifiziert wird nach Modell, Setup, Richtung, Precision, Vergleichsbackend, gespeichertem Completion-Paar-Endpunkt und Boundaryklasse. Keine gepoolte Rangkorrelation. Die bestehende Pair-Projektion ist die Bindungsautorität: bei 36 YOLO-Fällen benennen `generic_cases.endpoint_id` und `completion_pairs.output_endpoint_id` den physischen Quellendpunkt (z.B. raw_head), `native_cases.endpoint_id` dagegen den normalisierten decoded_nms-Vergleichsendpunkt. Diese unterschiedlichen Felder werden in `rank_cases.csv` separat erhalten; ein bloßer Stringvergleich ersetzt weder bestehende Gateprüfung noch semantischen Beleg. Precision stimmt in allen Joins.

- S=R_native/R_generic vergleicht Durchsätze desselben Falls und ist keine Auswahlmetrik.
- i_G ist der Generic-Durchsatzbeste derselben Gruppe; bei exaktem Tie gilt die vorhandene stabile Eingabereihenfolge.
- L_R=1−R_native,i_G/R_native,best ist der verlorene Native-Durchsatzanteil.
- L_C=R_native,best/R_native,i_G−1 ist der Kapazitäts-/Cycleregret. Er hat einen anderen Nenner; 50% L_R entsprechen 100% L_C. Inverser Durchsatz ist keine gemessene Einzelanfragelatenz.

Spearman, Kendall tau-b und tie-exkludierende Paar-Konkordanz verwenden unveränderte reine Projektfunktionen. Ties erhalten Durchschnittsränge; Top1 wird zusätzlich tie-aware geprüft. In den vorliegenden Median-Gruppen gibt es keine exakten Top-Ties. Sensitivitätsfelder für alle möglichen Generic-Top-Ties bleiben dennoch explizit enthalten. n<3 liefert keine Rang-/Top1-Behauptung.

## B: vollständige technische Gruppenübersicht

Drei-Wiederholungsmediane; alle Werte deskriptiv. Die Tabellenzeile wird durch `(cohort=augmented,tier=technical,model_id,setup_id)` eindeutig bezeichnet; die CSV enthält die volle Stratumdefinition.

| Modell | Setup | n | ρ | τ-b | Konkordanz | Generic Top1 → Native best | L_R % | L_C % |
|---|---|---:|---:|---:|---:|---|---:|---:|
| MobileNetV3-L | DeepX | 17 | 0.946 | 0.838 | 0.919 | b062 → b056 | 1.24 | 1.25 |
| MobileNetV3-L | H10 | 17 | 0.382 | 0.206 | 0.603 | b027 → b085 | 31.86 | 46.75 |
| MobileNetV3-L | H8 | 17 | 0.995 | 0.971 | 0.985 | b027 → b027 | 0.00 | 0.00 |
| RegNetX-1.6GF | DeepX | 20 | 0.983 | 0.926 | 0.963 | b052 → b052 | 0.00 | 0.00 |
| RegNetX-1.6GF | H10 | 20 | -0.456 | -0.421 | 0.289 | b052 → b123 | 70.61 | 240.23 |
| RegNetX-1.6GF | H8 | 20 | 0.941 | 0.821 | 0.911 | b066 → b073 | 8.03 | 8.74 |
| ResNet-50 | DeepX | 19 | 0.981 | 0.918 | 0.959 | b002 → b002 | 0.00 | 0.00 |
| ResNet-50 | H10 | 19 | 0.489 | 0.333 | 0.667 | b002 → b095 | 52.15 | 108.98 |
| ResNet-50 | H8 | 19 | 0.854 | 0.696 | 0.848 | b002 → b031 | 13.92 | 16.17 |
| YOLO11l | DeepX | 3 | 0.500 | 0.333 | 0.667 | b062 → b062 | 0.00 | 0.00 |
| YOLO11l | H10 | 3 | -0.500 | -0.333 | 0.333 | b003 → b120 | 13.34 | 15.40 |
| YOLO11l | H8 | 3 | 1.000 | 1.000 | 1.000 | b120 → b120 | 0.00 | 0.00 |
| YOLO26m | DeepX | 3 | 1.000 | 1.000 | 1.000 | b043 → b043 | 0.00 | 0.00 |
| YOLO26m | H10 | 3 | 0.500 | 0.333 | 0.667 | b038 → b043 | 1.64 | 1.66 |
| YOLO26m | H8 | 3 | 1.000 | 1.000 | 1.000 | b043 → b043 | 0.00 | 0.00 |
| YOLO26s | DeepX | 3 | 1.000 | 1.000 | 1.000 | b021 → b021 | 0.00 | 0.00 |
| YOLO26s | H10 | 3 | 1.000 | 1.000 | 1.000 | b021 → b021 | 0.00 | 0.00 |
| YOLO26s | H8 | 3 | 1.000 | 1.000 | 1.000 | b021 → b021 | 0.00 | 0.00 |
| YOLOv7 | DeepX | 3 | 0.500 | 0.333 | 0.667 | b044 → b066 | 5.07 | 5.34 |
| YOLOv7 | H10 | 3 | 0.500 | 0.333 | 0.667 | b066 → b044 | 6.51 | 6.97 |
| YOLOv7 | H8 | 3 | 0.500 | 0.333 | 0.667 | b044 → b066 | 52.96 | 112.59 |

Beleg: `tables/rank_groups.csv`. Top1 trifft insgesamt 10/21 Gruppen, getrennt 3/9 Klassifikation und 7/12 YOLO. Der ungewichtete Gruppenmedian L_R ist 1,24%, der Mittelwert 12,25%. Das sind Zusammenfassungen dieser Kandidatengruppen, keine Schätzung einer zufälligen Deploymentpopulation. Positive Gegenbeispiele (MobileNet/H8, RegNet/DeepX, ResNet/DeepX) und Null-/Kleinverlustfälle bleiben neben großen Fehlselektionen sichtbar.

**Quality-Sensitivität:** Die reference_close-Sicht verändert MobileNet/H10 von n=17, ρ=0,382, L_R=31,86% auf n=9, ρ=−0,533, L_R=24,91% (L_C=33,17%). Ein kleinerer Fehler bedeutet hier keine bessere Rangkorrelation; die verfügbare Kandidatenmenge und ihr Native-Maximum haben sich geändert. Die drei großen RegNet/H10-, ResNet/H10- und YOLOv7/H8-Gegenfälle bleiben bestehen. Gesamte reference_close-Gruppenübersicht ist in derselben Tabelle enthalten.

**Sinnvolle Shortlists:** Nur die neun Klassifikationsgruppen erfüllen n>=4. k=2 und k=3 werden fest vor der Detailrechnung verwendet. Bewertet wird jeweils der beste Native-Fall **innerhalb** der Generic-Shortlist, also ein Auswahlverfahren, das diese k Kandidaten anschließend Native prüfen könnte. Hier werden dafür ausschließlich vorhandene Messungen benutzt. Die Referenz ist die exakte Erwartung aller gleichwahrscheinlichen k-Teilmengen ohne Zurücklegen, berechnet per Kombinatorik; keine simulierten Messungen.

| technische Ansicht, neun Klassifikationsgruppen | k=2 | k=3 |
|---|---:|---:|
| Shortlist enthält Native-Maximum | 5/9 | 6/9 |
| Erwartete Trefferzahl zufälliger Shortlists | 0,969/9 | 1,453/9 |
| Mittlerer L_R der Generic-Shortlist | 14,23% | 12,51% |
| Exakter erwarteter mittlerer L_R zufälliger Shortlists | 24,39% | 18,49% |
| Gruppen mit geringerem L_R als Random-Erwartung | 7/9 | 7/9 |

RegNet/H10 bleibt bei k=3 deutlich schlechter als Zufallserwartung: L_R=68,58% gegenüber erwartet 38,96% (1.140 mögliche Dreiermengen). Seine Generic-Top3 b052,b030,b059 enthalten b123 nicht. MobileNet/H10 ist der zweite Gegenfall zur Random-Erwartung. ResNet/H10 verbessert sich von Top1 L_R=52,15% auf Top3 16,70%, trifft den Native-Besten aber weiterhin nicht. Damit hilft eine kleine Shortlist in vielen Gruppen, bietet aber keine allgemeine Auswahlgarantie. Beleg: `tables/rank_shortlists.csv`; qualitytransfer und reference_close vollständig enthalten. Kein Top3-Erfolg wird für n=3-YOLO behauptet.

## Robustheit gegenüber tatsächlich vorhandenen Wiederholungen

`tables/rank_repeat_combinations.csv` enthält alle neun Kombinationen von drei Generic- und drei Native-Wiederholungen pro auswertbarer Gruppe; `rank_repeat_sensitivity.csv` fasst sie zusammen. Das sind abhängige Rekombinationen von sechs Messreihen, keine neun unabhängigen Experimente und keine Konfidenzintervalle. Jede Wiederholung umfasst 1.000 abgeschlossene Tasks, die nicht als 1.000 unabhängige Studien zählen.

| Gegenfall | Top1-Treffer / neun Kombinationen | beobachteter L_R-Bereich | beobachteter L_C-Bereich |
|---|---:|---:|---:|
| RegNetX-1.6GF/H10 | 0/9 | 70.22–74.67% | 235.84–294.81% |
| ResNet-50/H10 | 0/9 | 49.76–53.52% | 99.04–115.13% |
| YOLOv7/H8 | 0/9 | 52.92–53.11% | 112.42–113.25% |

MobileNet/H8, RegNet/DeepX und ResNet/DeepX bleiben jeweils in 9/9 Kombinationen richtige Top1-Auswahlen. Die kleinen Medianfehler sind teils instabil: MobileNet/DeepX 3/9 Treffer bei L_R bis 3,15%; YOLO26m/DeepX 6/9 bei maximal 0,39%; YOLOv7/DeepX 5/9 bei maximal 11,34%. Ein Median-Top1-Miss kann daher entweder eine persistente große Fehlselektion oder eine enge, instabile Rangfolge bezeichnen.

**Dominante Gruppen:** Die vollständige Hauptansicht bleibt unverändert. Nur als Sensitivität sinkt bei Weglassen von RegNet/H10 der mittlere Gruppen-L_R von 12,25% (21 Gruppen) auf 9,34% (20); beim gemeinsamen Weglassen aller drei vorab benannten Gegenfälle auf 4,53% (18). Trotzdem verfehlt Generic Top1 noch 8/18 Gruppen; größter L_R bleibt 31,86% bei MobileNet/H10. Der Gesamtmittelwert ist stark durch wenige Gruppen geprägt, die grundsätzliche Heterogenität verschwindet nicht. Beleg: `tables/rank_dominant_case_sensitivity.csv`. Keine Fullbaseline wird in B/C eingesetzt, deshalb verändert die 21-Full-Attestorquellenlücke diese Split-vs-Split-Ränge nicht.

## C: historische Raw- und Completion-Proxies auf identischen Fällen

Alle 192 Basisfälle haben einen eindeutigen historischen Raw-Splitpartner. Der Join verwendet Modell, Case, Setup und Vergleichsbackend; einzig der explizite gespeicherte Backendalias deepx_m1→deepx wird kanonisiert. Zusätzlich muss der Raw-FPS-Wert mit der bereits gebundenen historischen Projektion im eingefrorenen Completion-Paar übereinstimmen. Die historische kompakte CSV enthält keine ausgefüllten Precision-/Endpunkt-IDs; eine neue unabhängige Vollidentitätsprüfung dieser fehlenden Felder wird nicht behauptet. Der bestehende Pair-Plan bindet diese Historie. Zwölf kurze Augmentierungsvorläufe sind ausgeschlossen. Beleg für jede Identität: `tables/rank_raw_join_audit.csv`.

Neun Klassifikations- und drei YOLO26m-Basisgruppen erfüllen n>=3. Die anderen neun Basisgruppen bleiben mit n<3 sichtbar. In den neun Klassifikationsgruppen verbessert sich ρ siebenmal, verschlechtert sich einmal (RegNet/H10) und bleibt einmal gleich (ResNet/H10). Der tatsächlich relevante Top1-L_R verbessert sich aber nur dreimal, verschlechtert sich zweimal und bleibt viermal unverändert. Die drei YOLO26m-Gruppen verändern ihre Auswahlmetrik nicht.

| Modell / Setup | n gemeinsam | Raw ρ → Completion ρ | Raw L_R % → Completion L_R % | Raw L_C % → Completion L_C % |
|---|---:|---:|---:|---:|
| MobileNetV3-L/DeepX | 17 | 0.941 → 0.946 | 0.92 → 1.24 | 0.93 → 1.25 |
| MobileNetV3-L/H10 | 17 | 0.341 → 0.382 | 31.86 → 31.86 | 46.75 → 46.75 |
| MobileNetV3-L/H8 | 17 | 0.990 → 0.995 | 13.90 → 0.00 | 16.15 → 0.00 |
| RegNetX-1.6GF/DeepX | 20 | 0.929 → 0.983 | 19.87 → 0.00 | 24.79 → 0.00 |
| RegNetX-1.6GF/H10 | 20 | -0.430 → -0.456 | 70.61 → 70.61 | 240.23 → 240.23 |
| RegNetX-1.6GF/H8 | 20 | 0.392 → 0.941 | 41.43 → 8.03 | 70.73 → 8.74 |
| ResNet-50/DeepX | 19 | 0.954 → 0.981 | 0.00 → 0.00 | 0.00 → 0.00 |
| ResNet-50/H10 | 19 | 0.489 → 0.489 | 52.15 → 52.15 | 108.98 → 108.98 |
| ResNet-50/H8 | 19 | 0.761 → 0.854 | 1.90 → 13.92 | 1.94 → 16.17 |
| YOLO26m/DeepX | 3 | 1.000 → 1.000 | 0.00 → 0.00 | 0.00 → 0.00 |
| YOLO26m/H10 | 3 | 0.500 → 0.500 | 1.64 → 1.64 | 1.66 → 1.66 |
| YOLO26m/H8 | 3 | 1.000 → 1.000 | 0.00 → 0.00 | 0.00 → 0.00 |

Beleg: `tables/rank_proxy_comparison.csv`; alle drei Qualityansichten enthalten. RegNet/H8 zeigt einen großen Proxygewinn, während ResNet/H8 trotz höherem ρ den schlechteren Top1 wählt. Das stützt die Aussage, Rangkorrelation und praktische Auswahl getrennt zu beurteilen. Historische Raw-Zeitmessung, Completion und Native unterscheiden sich in Datum, Runtime, Thread-/Thermikzustand und Endpunkt. Der Unterschied kann nicht ausschließlich kausal dem hinzugefügten Postprocessing zugeschrieben werden. Keine Ersatzzeit aus Raw+geschätztem Postprocessing wurde erzeugt.

## F: konkrete Sprünge und alternative Erklärungen

Alle folgenden FPS sind Mediane von drei gespeicherten 1.000-Task-Wiederholungen. Count/Makespan wurde zusätzlich für alle 1.350 öffentlichen Performance-Wiederholungen geprüft; Originalrundung bis zur dokumentierten Toleranz 1e-6 ist zulässig. Die Tabellen enthalten die drei Einzelwerte und tatsächlichen Zeitfenster.

| Modell / Setup / Grenze | Generic completed task/s | Native completed task/s | S=Native/Generic |
|---|---:|---:|---:|
| RegNetX-1.6GF/H10/b052 | 349.190 | 446.943 | 1.280 |
| RegNetX-1.6GF/H10/b123 | 228.212 | 1520.613 | 6.663 |
| ResNet-50/H10/b002 | 304.089 | 507.268 | 1.668 |
| ResNet-50/H10/b095 | 182.628 | 1060.075 | 5.805 |
| YOLOv7/H8/b044 | 13.721 | 53.461 | 3.896 |
| YOLOv7/H8/b066 | 12.449 | 113.654 | 9.129 |

Gezielte Quellenprüfung von neun Fällen, ohne breite Rohdateninventur, liegt als kompakte öffentliche Projektion in `inputs/ranking_path_evidence.csv` vor. Sie umfasst die sechs Tabellenfälle, MobileNet/H8/b027 als stabiles positives Auswahlbeispiel, MobileNet/DeepX/b001 als kleinsten S-Wert (0,865) und YOLOv7/H10/b066 als weiteren S<1-Fall (0,871). In allen neun Fällen stimmen die gespeicherten vorbereiteten Input-SHAs, Quellbild-SHAs und TensorRT-Engine-SHAs zwischen den beiden Runnerbindungen überein; bei den acht Hailo-Fällen stimmen auch die HEF-SHAs. Für DeepX wird die HEF-Rolle sachgerecht nicht behauptet.

**Bestätigte Verträge:** Generic speichert zwei Worker, Queue 2, Batch 1, genau wiederholten vorbereiteten Input, 100 Warm-ups, 1.000 Tasks, Fill/Drain inklusive, Preprocessing außerhalb, Übergabe/Nachverarbeitung/Materialisierung innerhalb des Timers. Der bestehende `runners/task_completion.py:measure_split_completion` ruft pro Produceriteration Stage1 bis zu materialisierten Hosttensoren auf; der Consumer führt Stage2 plus Completion aus. Das ist eine gepipelinte Zweiworker-Ausführung; es wird keine völlig serielle Gesamtausführung behauptet.

Die vier RegNet-/ResNet-H10-Gegenfallzeilen und YOLOv7/H10/b066 speichern Native `hailo10_infermodel_async_fifo`, Inflight 8 und Queue 3. Native-Completion ist im jeweiligen Count eingeschlossen. Gleiche Input-/Enginebytes beseitigen damit nicht die tatsächlichen Unterschiede des Ablaufplans. Die vorhandenen H10-Felder zu Queuewait und Stagezeiten sind als einzelne gespeicherte Reportdiagnose markiert, nicht als unabhängig gemittelte oder kausal isolierte Stagezerlegung interpretiert.

**YOLOv7/H8 ist zusätzlich kein einheitlicher Runnerpfad:** b044 meldet `hailo8_python_vstreams_fifo`, b066 `hailo8_cpp_concurrent_three_stage` mit Queue 3 und zusätzlicher Postqueue 4. b066 speichert einen Completion-Vertrag einschließlich Decode/NMS und Completionzählung; der `fast_oracle_outside_timing`-Modus beschreibt die separate Qualitätssentinelprüfung außerhalb der Performancezeit und darf nicht als fehlendes Performance-Postprocessing ausgelegt werden. Der aktuelle b066-Wert 113,654 task/s gehört genau zu diesem vorbereiteten Dreistufenpfad und seinen gebundenen Artefakten. Er ist weder eine historische Paperenginezahl noch der anders begrenzte 97-FPS-Wert.

**Nicht isoliert:** Die Rangumkehr ist gemessen und über die vorhandenen Wiederholungen robust. Async-/Inflight-/Queue-/Nachverarbeitungspfade liefern plausible Mechanismen, beweisen aber allein keinen isolierten kausalen Anteil am Sprung. Die neun gezielt gelesenen Belege liefern keinen paarweise kontrollierten Nachweis gleicher CPU-Affinität, Threadparameter, thermischer Zustände, Takte oder Uhrzeit. Native-Wanduhrstempel sind in dieser kompakten Projektion unbekannt; Generic-Daten liegen am 02.10. und 04.10. vor. Fehlende Werte bleiben leer, nicht Null. Keine universelle Herstellercharakterisierung und keine neue Claimfreigabe.

## Reproduktion und Prüfung

`python scripts/analyze_ranking.py --source-root SOURCE --output-root OUT` liest ausschließlich die eingefrorenen kompakten Quellen und importiert `SOURCE/scripts/project_rank_metrics.py`. SOURCE ist der ursprüngliche öffentliche Analysebereich bzw. dessen kuratierter Ergebnischeckout; OUT ist die separate neue Ableitung. Die acht Tabellen und `ranking_results.json` enthalten keine privaten absoluten Pfade. Zur optionalen erneuten Belegprojektion können `--private-source-index INDEX --private-replay-root REPLAY` explizit übergeben werden; sie liest nur die neun genannten bereits existierenden JSON-Fälle und schreibt `inputs/ranking_path_evidence.csv`. Öffentliches Review und Rangreproduktion benötigen diese privaten Quellen nicht.

Gezielte Tests: `THESIS20_SOURCE_ROOT=SOURCE PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider tests/test_ranking.py` in der vorhandenen Testumgebung: **11 passed**. Geprüft sind unterschiedliche Regretnenner, exakte Random-Erwartung gegen vollständig enumerierte kleine Mengen inklusive Ties, negative Qualitygates trotz reference_close, Ablehnung doppelter/alias-kollidierender Identitäten, Raw-Paarbindung, deterministische/tie-aware Top1-Auswahl und unzureichende Gruppen. System-Python ohne pytest führte zunächst nur zum dokumentierten Umgebungsfehler `No module named pytest`; der bestehende Projekt-Venv führt die Tests erfolgreich aus. Keine Toolvollsuite oder Hardwareabnahme wurde gestartet.


Zusätzlich automatisiert: 126 Gruppen stimmen in n, Spearman, Kendall tau-b, Konkordanz und L_C mit der unveränderten ursprünglichen `_groups`-Ableitung innerhalb 1e-12 überein. Alle acht Tabellen plus `ranking_results.json` sind bei unabhängiger Reproduktion in zwei frischen temporären Verzeichnissen bytegleich (9/9). Dieser Integrationscheck ist Teil der elf Tests.
