# R9G — abgeschlossene Gegenprüfung der Text-/Reportbelege

> Öffentliche kuratierte Kopie der vorhandenen R9G-Gegenprüfung. Die dort beschriebenen
> Nachrechnungen wurden bei der ursprünglichen Gegenprüfung vorgenommen, nicht durch
> diesen Git-Patch erneut als Hardware-/Rohtraceexperiment ausgeführt. Private Pfade sind redigiert.

**Tabellen:** [Full 42](Full_42.csv), [Splits 21](Splits_21.csv),
[Energie 189](Energy_189.csv), [Quality 77](Quality_77.csv), [Zeilenquellen](ROW_SOURCES.csv),
[Backfill](Backfill.csv), [Audit](ENERGY_AND_INTEGRITY_AUDIT.json), [offene R9G-Befunde](OPEN_FINDINGS.json).
In Full/Splits stehen Qualitätswerte auf der 0–100-Skala; `Quality_77.csv` erhält die
ursprünglichen 0–1-Werte. Mittelwerte/Streuung und Messendpunktgrenzen bleiben erhalten.
`BEFUNDE_FUER_CODEX.json` ist die außerhalb dieses kleinen Patches erhaltene ausführliche
Quellprojektion; die hier enthaltene Datei `OPEN_FINDINGS.json` ist deren markierter Auszug.

Stand: 18.09.2026. Gegenstand ist ausschließlich `r9g_eval_20260918_171131`, nicht eval_01.

## Ergebnis

Der Integrationslauf bleibt technisch erfolgreich: 63 Nativezeilen (42 Full, 21 Split), alle mit aufgezeichneten Requestlatenzen; 77 zentrale Qualitätsauswertungen (40 PASS, 25 FAIL, 12 INCONCLUSIVE); 189 erfolgreiche Energieaufnahmen. Die H8-/H10-Ersatzgrenzen sind YOLO26s/b021 und YOLO26m/b038. Die alten späten HEFs sind damit nicht numerisch repariert.

Die Aufnahme ist vollständig. Die abschließende Auswertung zeigt jedoch tatsächliche Grenzen bei Taskgleichheit, Vergleichseingaben und Reporterprojektion. Sie werden unten von legitimen Qualitäts-/Screeningentscheidungen getrennt. Es ist keine neue Collector- oder Kalibrierungsreparatur begründet.

## 1. Umfang der unabhängigen Prüfung

Quellen: `r9g_eval_20260918_171131_debug_core.zip` und `r9g_eval_20260918_171131_debug_nachtrag_20260918_225653_2333399.zip`. Das Nachtragsarchiv enthält 11.030 Einträge, davon 11.028 inventarisierte Run-Nutzdateien. Alle Nutzdateien stimmen in Größe und SHA256; beim Lesen bestanden die CRC-Prüfungen. Zusammengenommen wurden 19.463 Run-Dateien erfolgreich gegen den gespeicherten terminalen Artefaktindex geprüft. Ausgenommen von seiner eigenen Hashprüfung ist nur der Index selbst.

Die bereits gegen die 6.300 Requestzeitpaare geprüften Performance-/Latenzwerte aus dem Core bleiben erhalten. Der Nachtrag ergänzt insbesondere `reports/`, Energie-Einzelberichte, normalisierte Werte und Vergleichsgründe. Die Produkttests, GUI, Inferenz, DFC und Messhardware wurden hier NICHT neu ausgeführt.

Roh-Parquets sind nicht enthalten. Deshalb wurde keine erneute Integration der Rohspannungs-/Stromtraces durchgeführt. Die folgende Energieprüfung bezieht sich auf die gespeicherten Einzelmesswerte, Kalibrierungsfaktoren, Marker-/Fensterbindung, Ergebnisarithmetik und UDP-Empfangsprotokolle.

## 2. Energieaufnahme und gespeicherte Auswertung

Alle 63 Zeilen enthalten genau drei gültige logische Wiederholungen. Alle 189 tatsächlichen Collectorstarts enden erfolgreich, ohne zusätzliche Retryversuche. In sämtlichen Empfangsprotokollen: 844 Datendatagramme, Counter durchgehend 1–54.016, genau ein Enddatagramm, kein gemeldeter Socketverlust und bestätigter Abschluss.

Für jede der 189 Wiederholungen wurden unabhängig geprüft: E = P × T, J/Work-Unit = E/N, exakt beobachtete und verwendete Arbeitseinheiten, FS-Kalibrierungsfaktor, zugehörige Request-/Marker-/Timing-/Postprocessor-/Ergebnisbindung und vollständige Fensterabdeckung. Alle Prüfungen bestehen. Die 63 Mittelwerte und Stichprobenstreuungen der J/Work-Unit-Werte stimmen mit den Aggregaten überein.

Bereich der Zeilenmittelwerte: kalibrierte FS-Leistung 14,57–21,25 W; aktive Commandfenster 2,21–4,38 s. Variationskoeffizient der drei Energie-pro-Work-Unit-Replikate: 0,21–4,21 %. Dies wird als beobachtete Variabilität dokumentiert, nicht als Fehler oder Anlass für eine Wiederholungsserie gewertet. Scheduling ist ohne zusätzliche Beobachtung eine mögliche, keine bewiesene Ursache.

### Ausgewählte neue Detection-Splits

| Pfad | Grenze | FS-J/Work-Unit, Mittelwert | Work-Units/J |
|---|---|---:|---:|
| YOLO26s H8 → TRT | b021 | 0,289961 | 3,448737 |
| YOLO26s H10H → TRT | b021 | 0,387084 | 2,583417 |
| YOLO26m H8 → TRT | b038 | 0,655946 | 1,524516 |
| YOLO26m H10H → TRT | b038 | 0,672025 | 1,488040 |

Keine qualitätsgleichen Speedup- oder wissenschaftlichen Effizienzfreigaben daraus ableiten. Das sind kurze FS/Commandmessungen ohne Idleabzug. Die Workbook-Energieeffizienz ist 1/Mittelwert(J_i/N_i), nicht Performance-FPS geteilt durch Leistung eines anderen Fensters. Idle-normalisierte Schätzwerte werden nicht als rohe FS-Werte verwendet.

## 3. Belegter Taskunterschied im Energiepfad

Für alle neun TensorRT-Full-Klassifikationskombinationen (drei Klassifikationsmodelle auf drei Setups) zeigen alle 27 Energie-Workloadlogs noch die tatsächliche `trtexec`-Ausführung. Der Performancepfad verwendet hingegen seit R9C den Prepared-Input-Hotloop einschließlich Top-1/Top-5.

Damit sind diese 27 Energieaufnahmen reale und arithmetisch gültige Messungen, aber kein Nachweis für Energie desselben abgeschlossenen Klassifikationstasks wie in der aktuellen Performance-Spalte. Im Workbook sind die neun Zeilen ausdrücklich entsprechend markiert. Das ist eine Dispatch-/Integrationlücke, kein fehlgeschlagener Collector und keine bloße Frage der Streuung. Für die anderen Runner muss die tatsächliche Taskgleichheit lokal anhand des gemeinsamen Energie-/Performance-Dispatches geprüft werden; fehlender Top-k-Logtext allein beweist dort noch keinen Fehler.

Quellen: `reports/native_energy_measurements/measurements/native_full_tensorrt__*/.../run_00*/workload_stdout.log`, zugehörige Commandverträge und Native-Performanceberichte. `BEFUNDE_FUER_CODEX.json` enthält die konkreten Pfade; `TRT_CLASSIFICATION_ENERGY_EXCERPT.txt` repräsentative Originalzeilen.

## 4. Vergleichseingaben und Projektionen

### Unterschiedliche DeepX-Eingaben

Alle sieben DeepX-Full-/Split-Vergleichspaare verwenden tatsächlich unterschiedliche Quelldateien/Bildhashes. Bei vier Full-Detectionpfaden fehlt zusätzlich ein Padwert in der Prepared-Feeddarstellung. Der aktuelle Vergleichsschutz hat daher einen realen Grund zur Ablehnung; bloß identische Labels nachzutragen wäre falsch. Für neue Runs sollte derselbe vorher deterministisch gewählte Modelleingabe-Fall über die bestehenden Full-/Splitpfade weitergereicht werden; die backendgerechte Vorverarbeitung bleibt getrennt.

### Verlorene Vergleichsendpunkte

Zwölf Detection-Split-Beobachtungen besitzen physische Taskabschlussbelege, aber leere Vergleichsendpunkt-/Vertragsfelder in `reports/scientific/native_energy_observations.json`. Dadurch entstehen in 24 Full-vs-Split-Vergleichen entsprechende Ablehnungsgründe. Die vorhandene Projektion und der Join müssen die tatsächliche Identität prüfen und vollständige Belege korrekt weiterreichen. Nicht jede vorhandene Completion darf pauschal zum Beweis der Vergleichbarkeit werden.

### Normalisierte TRT-Full-Metriken

20 von 21 TRT-Full-Zeilen werden als `required_tensorrt_full_normalized_metrics_invalid` abgelehnt, obwohl ihre gespeicherten normalisierten Einzelreplikate intern konsistent sind. Die starke Arbeitshypothese ist eine Prüfung von Mittelwerten mit einer unzulässigen Identität: Mittelwert(E_i/N_i) ist bei verschiedenen N_i nicht gleich Mittelwert(E_i)/Mittelwert(N_i). Entsprechend sind Mittelwert(P_i) und Summe(E_i)/Summe(T_i) unterschiedliche Definitionen.

Der einzige zufällig mit beiden aggregierten Identitäten übereinstimmende Fall ist zugleich der akzeptierte Fall. Das ist eine reproduzierbare Korrelation und eine konkrete Stelle für die Sourcegegenprüfung, noch kein hier ausgeführter Produktfix. Die Lösung muss Aggregation und Replikatbasis korrekt behandeln, nicht die Toleranz lockern.

## 5. Was ausdrücklich kein Fehler ist

`energy_quality_qualified=0` widerspricht den 189 gültigen Aufnahmen nicht: 26 Nativezeilen mit Quality-PASS werden unter der bestehenden kurzen Screeningpolicy weiterhin nicht wissenschaftlich freigegeben; 25 Zeilen haben Quality-FAIL und zwölf INCONCLUSIVE. Screening darf nicht allein für einen grünen Zähler abgeschaltet werden.

35 der 42 Energievergleichspaare überschreiten außerdem die vorhandene relative Toleranz der aktiven Commanddauer. Dies ist eine tatsächliche Vergleichsgrenze der kurzen Aufträge, kein Grund für eine automatische Gate-Lockerung. Mittelwerte/Streuungen der eigenen Messung bleiben berichtbar.

## 6. Validierungs-/Anzeigealtlasten

21 Splitvalidierungen führen gleichzeitig eine gültige native Qualityauthority und den alten Fehler `native_split_quality_authority_missing`. Aktuelle Urteile und historische Diagnosen müssen an ihrer gemeinsamen Quelle getrennt werden.

Die generische Matrix enthält 56 technisch ausgeführte Zeilen. Ihre zusätzlichen Verdicts lauten 36 `contract_fail_or_unavailable`, 14 `numerical_similarity_failed`, sechs `screening_only`; `validation_ok` ist bei 27 wahr und 29 falsch. Das sind nicht 50 Runtimeabstürze. Die Ursachen bleiben getrennt und werden nicht pauschal gegen einen Native-PASS ausgetauscht.

Generic-Energie war nicht angefragt. Ihre pauschale Anzeige als `missing_or_not_measured` bzw. `missing_row_level_energy` ist nicht gleich einer fehlenden Pflichtmessung. Der Text `Output/Qualität: claim_ok` bleibt missverständlich. Diese Reporterstellen sind offline mit den Originalberichten prüfbar.

## 7. Unverändert offen

Die beiden bekannten DeepX-Full-YOLO26s-Bilder `000000052891.jpg` und `000000395801.jpg` fehlen in dieser 500er-Teilmenge. Der frühere 5.000er-XYXY-Negativbefund bleibt damit offen. Nur ein belegter allgemeiner eigener Adapterfehler ist zu reparieren; keine Bildausnahme, Koordinatenvertauschung oder Schwellwertlockerung.

Der passende 97-FPS-Papervergleich erfordert weiterhin YOLOv7/H8-b066 mit gleichem Messumfang. Drei Splits im nächsten Lauf bedeuten nicht automatisch, dass b066 gewählt wird oder Rankingtransfer wissenschaftlich freigegeben ist. Dafür wird die normale Auswahl nicht nachträglich verzerrt.

## 8. Vorgesehene Fortsetzung

R9H ergänzt den bestehenden Energie-Dispatch und die geprüften Quellen-/Projektionsstellen. Danach ein kleiner MobileNet-GUI-Smoke auf allen drei Setups inklusive Energie, anschließend automatisch sieben Modelle mit drei Splits je Backend. Standard 500/500, Native100/10/1, Native-Energie1s×3. Bei voller Ausführbarkeit nominal 105 Nativezeilen und 315 Energiereplikate; tatsächliche Nenner aus dem Runplan.

Gezielte iterative Korrektur belegter Implementierungsfehler ist erlaubt, kein Tuning auf Qualitäts-PASS. Maximal vier lokale Reparaturrunden, zwei Smoke- und zwei abschließende Evalstarts. Die bisherigen Daten bleiben unverändert. Neu generierte Textdebugpacks werden nach Workflowende vollständig und transaktional gesammelt.
