# Wissenschaftliche Offlineanalyse der konsolidierten Revision 3


Die kanonische Auswahl umfasst 450 Betriebspunktidentitäten (246 Native, 204 Generic). Davon sind 437 normal energiegebunden; 13 Grenzfälle bleiben ausdrücklich sichtbar. Die Analyse wurde aus den festgehaltenen kompakten Eingaben berechnet. Alle Vergleichsaussagen gelten für die tatsächlich gemessenen Modelle, Setups, Inputs und Laufzeitverträge.

## Native und Generic

Bei 204 technisch gebundenen Performancepaaren ist Native an 139 Punkten schneller. Das Medianverhältnis der gespeicherten FPS-Mediane beträgt 1.361335; Quartile 0.970668 und 1.749171. In 198 beidseitig energiezugelassenen Paaren liegt die Native-Rohenergie an 154 Punkten niedriger; Median E/N-Verhältnis 0.755246. Beide Vorteile treten an 134/198 gemeinsam auswertbaren Punkten auf. Die Tabellen enthalten alle Paare und Nenner je Modell/Setup, nicht nur Gewinner.

Native nutzt spezialisierte FIFO-/Workerimplementierungen; Generic den gemessenen generischen Completionrunner. Die Messgrenze beginnt nach der Eingabevorbereitung und endet mit der letzten Task-Completion; diese Zahlen sind keine Ende-zu-Ende-Anwendungs- oder Requestlatenzen. Drei frische Performanceprozesse mit je 1000 Tasks liefern den gespeicherten FPS-Median. Energie stammt aus eigenen Sensorwiederholungen mit dokumentiertem Lastfenster und exakter Performance-/Qualitätsbindung. Ein Vergleich der Regime beweist keine isolierte Ursache für einen Implementierungsvorteil.

## Splits und Fullalternativen

Von 396 archivierten Energiepaaren tragen 340 ein positives Claimflag. Die strenge Schnittmenge mit semantischer Zulassung enthält 312 Paare; 28 zusätzliche positive Claimflags haben ungesicherte Decoder-/NMS-Gleichwertigkeit und bleiben ausgeschlossen. Die Performanceanalyse verwendet konservativ nur die Teilmenge mit vorhandenem strengem Energiepaarvertrag und bindet zusätzlich beide Performancefreigaben; sie behauptet keine vollständige unabhängige Performancepaarabdeckung (200 Paare); historische Full-Einzelbeobachtungen liefern keinen neuen Performanceclaim.
Gegen die jeweils schnellste zulässige Fullalternative sind 44/132 Splits schneller; Median Speedup 0.898095, Quartile 0.645053 bis 1.087011. Gegen die energieärmste zulässige Fullalternative sind 60/188 Splits energieärmer; Median Verhältnis 1.071691. Beide Fullauswahlen erfolgen getrennt und fallbezogen. Fehlende Baselines werden nicht aus einem anderen Setup ergänzt.

| Modell | Setup | Schnellster Split | FPS | Schnellste Full | Speedup | Energieminimum Split | mJ/Task | Energieärmste Full | Energieverhältnis |
|---|---|---|---:|---|---:|---|---:|---|---:|
| mobilenet_v3_large | DeepX | b027 | 770 | native_full_tensorrt | 1.108 | b135 | 25.374 | native_full_tensorrt | 1.034 |
| mobilenet_v3_large | H10 | NA | NA | NA | NA | b085 | 18.357 | native_full_tensorrt | 0.697 |
| mobilenet_v3_large | H8 | b027 | 993 | native_full_tensorrt | 1.327 | b027 | 23.011 | native_full_tensorrt | 0.868 |
| regnet_x_1_6gf | DeepX | b052 | 403 | native_full_tensorrt | 1.210 | b052 | 59.521 | native_full_tensorrt | 0.926 |
| regnet_x_1_6gf | H10 | NA | NA | NA | NA | b123 | 15.826 | native_full_tensorrt | 0.223 |
| regnet_x_1_6gf | H8 | b073 | 618 | native_full_hailo8 | 1.705 | b073 | 41.734 | native_full_hailo8 | 0.965 |
| resnet50 | DeepX | b002 | 444 | native_full_tensorrt | 0.859 | b119 | 49.862 | native_full_deepx | 1.015 |
| resnet50 | H10 | NA | NA | NA | NA | b095 | 29.459 | native_full_tensorrt | 0.553 |
| resnet50 | H8 | b038 | 581 | native_full_tensorrt | 1.111 | b060 | 45.172 | native_full_tensorrt | 0.854 |
| yolo11l | DeepX | b062 | 49 | native_full_tensorrt | 1.263 | b062 | 546.005 | native_full_tensorrt | 0.895 |
| yolo11l | H10 | b062 | 51 | native_full_tensorrt | 1.315 | b062 | 558.635 | native_full_tensorrt | 0.889 |
| yolo11l | H8 | b062 | 43 | native_full_tensorrt | 1.094 | b062 | 574.553 | native_full_tensorrt | 0.915 |
| yolo26m | DeepX | b043 | 61 | native_full_tensorrt | 0.728 | b038 | 428.822 | native_full_tensorrt | 1.195 |
| yolo26m | H10 | b043 | 110 | native_full_tensorrt | 1.310 | b043 | 319.651 | native_full_tensorrt | 0.845 |
| yolo26m | H8 | b038 | 79 | native_full_tensorrt | 0.929 | b043 | 355.993 | native_full_tensorrt | 0.948 |
| yolo26s | DeepX | b021 | 114 | native_full_tensorrt | 0.752 | b021 | 217.629 | native_full_tensorrt | 1.271 |
| yolo26s | H10 | NA | NA | NA | NA | NA | NA | NA | NA |
| yolo26s | H8 | NA | NA | NA | NA | NA | NA | NA | NA |
| yolov7_paper | DeepX | b009 | 34 | native_full_tensorrt | 0.707 | b009 | 715.749 | native_full_tensorrt | 1.275 |
| yolov7_paper | H10 | b009 | 51 | native_full_tensorrt | 0.971 | b009 | 587.485 | native_full_tensorrt | 1.041 |
| yolov7_paper | H8 | b009 | 45 | native_full_tensorrt | 0.846 | b009 | 599.653 | native_full_hailo8 | 1.091 |

Die Optima sind post hoc aus denselben beobachteten Kandidaten ausgewählt. Sie sind kein unabhängiger Selektor-, Vorhersage- oder Generalisierungsnachweis. Häufigkeiten, alle Baselineentscheidungen sowie Top- und Worstfälle stehen in `tables/`; gemeinsame Fullbaselines erzeugen abhängige Vergleichspaare.

## Qualität und Pareto

26 Native- und 17 Generic-Zeilen mit accuracy_loss bleiben im Gesamtbestand erhalten. Davon sind 23 Native und 17 Generic sowohl performance- als auch energiezugelassen. Die Zusatzanalyse both_reference_close ist ausdrücklich eine Sensitivitätsauswahl. Dataset-Accuracy bzw. COCO-mAP und funktionale numerische Ausgabeparität sind verschiedene Evidenzachsen. Die zweidimensionale Paretofront setzt höhere FPS und niedrigere Rohenergie innerhalb eines Modell-/Setup-/Runner-/Vertragskontexts voraus. Negative Qualität wird dokumentiert, nicht durch historische positive Werte ersetzt.

## Robustheit und Unsicherheit

Rohenergie und vorhandene hostnormalisierte Vergleichsenergie werden getrennt gerechnet. Die Normalisierung ändert bei 34 zulässigen Split/Full-Paaren die Richtung des Energievergleichs. `sensitivity.csv` zeigt Baselineart, Qualitätsfilter und Energiegrundlage mit ihren Nennern. Es wurde keine neue Idlekorrektur erfunden.

Gespeicherte FPS-Mediane werden nicht in Mittelwerte umgedeutet. Primärenergie ist mean(E/N), Effizienz mean(N/E); 1/mean(E/N) und sum(N)/sum(E) stehen als gesonderte Rechnungen in der Unsicherheitstabelle. Energie-CIs sind zweiseitige Student-t-Intervalle des Mittelwerts aus drei tatsächlichen Sensorwiederholungen (df=2, t=4.302652729749461). Sie sind keine Vorhersageintervalle. Für FPS wird die beobachtete Spannweite ausgewiesen, kein Mittelwert-CI auf den Median übertragen. Historische Einzelwerte erhalten kein CI. Alle neun ungepaarten Repeatquotienten dienen nur als empirischer Stabilitätscheck, nicht als neun unabhängige Beobachtungen. Keine neue Randomisierung, kein Bootstrap und kein neuer Seed werden verwendet.

## Erklärung durch Graph und Pipeline

Graphmerkmale sind über alle sieben Modell-SHAs sowie die Indexhashes der gespeicherten Analyse-/Rankingdateien gebunden. Spearman-Assoziationen werden innerhalb Modell/Setup/Runner berechnet; konstante Merkmale bleiben ohne Korrelationswert. Kandidaten sind ausgewählt und abhängig, daher werden keine Kausal- oder Signifikanzclaims aus diesen Assoziationen abgeleitet.
Die Pipelineprojektion bindet 720 Rohreportwiederholungen direkt über ihren Current-SHA; 0 direkte Rohreportbindungen fehlen. Workerzeiten überlappen. H10-P1-Latenz ist nicht P1-Durchsatzzyklus; FIFO-Wartezeit ist keine Handoff-Rechenarbeit. Completiontail und postprocess können Aliase sein. Deshalb zeigt die Abbildung absolute getrennte Workerzeiten, keine summierten Gesamtprozente. Fehlende Felder bleiben NA.

## Separate diagnostische Abnahme

YOLOv7/DeepX/b044: ein diagnostischer Generic-Einzelwert von 49 FPS gegenüber dem historischen Median 50 FPS (-2.3711 %); Energie 551.484 gegenüber 549.507 mJ/Task (+0.3598 %). Diese Abnahme wird nicht in die 450 wissenschaftlichen Identitäten gemischt. Ein Mittelwert-CI darf den Einzelwert nicht als bestanden/fehlgeschlagen klassifizieren; ein kanonischer RGB-Hash bleibt in diesem Abnahmevergleich unbekannt.

## Beleggrenzen und Reproduktion

Bei 17 aktuellen MobileNet-/DeepX-Native-Punkten ist die referenzierte Verwaltungsreceipt-Dateiversion nicht mit dem erwarteten Hash vorhanden. Die normalen Ergebnis- und Qualitätsblätter sind separat exakt an Current gebunden; die gespeicherten Zulassungsflags werden deshalb unverändert berichtet, aber keine lückenlose Receiptkette behauptet. Die zugehörigen Generic-Paarungen sind ebenfalls markiert. Die Sensitivität exclude_administrative_receipt_gaps zeigt die Auswertung ohne diese Fälle.
Die kompakte Reproduktion benötigt Python, NumPy, SciPy und Matplotlib; sie öffnet keine Modelle, Sensoren oder Runtime-SDKs. `scripts/reproduce.py --output NEUER_ORDNER` erzeugt Tabellen, Zahlen und Abbildungen aus `inputs/`. Die private Extraktion liest ausschließlich den konsolidierten Archivbestand. Öffentliche Tabellen ersetzen kein vollständiges Rohtrace-/Datasetreplay. Der fehlende historische Full-Producer-Quellhash mit 21 Referenzen bleibt eine Beleggrenze. Rohtraces werden hier nicht neu kalibriert oder numerisch integriert; ihre vorhandenen normalen Produktions- und Archivbelege werden übernommen.

Die Hash-/Kopierbilanz der SM2-Übergabe ist übernommene Sicherungsevidenz, kein auf Twix wiederholter Vollhash. Datierte THESIS20-, PSD-/TIM- und Abnahmebestände behalten ihren eigenen Geltungsbereich. Keine neue Messung, kein Rebuild und keine Queuefortsetzung wurde für diese Auswertung ausgeführt.

## Verteilungen und Zielkonflikte nach Setup

DeepX: Native ist an 8/68 Punkten schneller als Generic (Medianverhältnis 0.953) und an 24/68 Punkten energieärmer (Median 1.007). Über alle neun ungepaarten Repeatquotienten bleibt der Performancevorteil an 5 Punkten und der Energievorteil an 15 Punkten erhalten.
H8: Native ist an 63/68 Punkten schneller als Generic (Medianverhältnis 1.423) und an 65/65 Punkten energieärmer (Median 0.696). Über alle neun ungepaarten Repeatquotienten bleibt der Performancevorteil an 63 Punkten und der Energievorteil an 65 Punkten erhalten.
H10: Native ist an 68/68 Punkten schneller als Generic (Medianverhältnis 2.059) und an 65/65 Punkten energieärmer (Median 0.597). Über alle neun ungepaarten Repeatquotienten bleibt der Performancevorteil an 68 Punkten und der Energievorteil an 65 Punkten erhalten.
In 5/16 auswertbaren Modell-/Setupgruppen unterscheiden sich der schnellste und der energieärmste beobachtete Split. Ein universeller bester Split folgt daraus nicht.
Speedup gegen schnellste zulässige Full: Minimum 0.1673 bei mobilenet_v3_large/H8/b135, Maximum 1.7053 bei regnet_x_1_6gf/H8/b073. Die Einzelfälle sind deskriptiv; vollständige Rangextreme stehen in top_worst_splits.csv.
Energieverhältnis gegen energieärmste zulässige Full: Minimum 0.2226 bei regnet_x_1_6gf/H10/b123, Maximum 4.6009 bei mobilenet_v3_large/H8/b135. Die Einzelfälle sind deskriptiv; vollständige Rangextreme stehen in top_worst_splits.csv.

## Sensitivität mit expliziten Nennern

| Vergleich | Qualitätsfilter | Energiegrundlage | Performancepaare | schneller | Energiepaare | energieärmer |
|---|---|---|---:|---:|---:|---:|
| native_generic | all_admitted | raw | 204 | 139 | 198 | 154 |
| all_full | all_admitted | comparison | 200 | 111 | 312 | 136 |
| all_full | all_admitted | raw | 200 | 111 | 312 | 170 |
| tensorrt_full | all_admitted | comparison | 132 | 47 | 188 | 75 |
| tensorrt_full | all_admitted | raw | 132 | 47 | 188 | 109 |
| vendor_full | all_admitted | comparison | 68 | 64 | 124 | 61 |
| vendor_full | all_admitted | raw | 68 | 64 | 124 | 61 |
| native_generic | both_reference_close | raw | 187 | 122 | 181 | 137 |
| all_full | both_reference_close | comparison | 164 | 84 | 268 | 107 |
| all_full | both_reference_close | raw | 164 | 84 | 268 | 141 |
| tensorrt_full | both_reference_close | comparison | 123 | 47 | 171 | 72 |
| tensorrt_full | both_reference_close | raw | 123 | 47 | 171 | 106 |
| vendor_full | both_reference_close | comparison | 41 | 37 | 97 | 35 |
| vendor_full | both_reference_close | raw | 41 | 37 | 97 | 35 |
| native_generic | exclude_administrative_receipt_gaps | raw | 187 | 138 | 181 | 151 |
| all_full | exclude_administrative_receipt_gaps | comparison | 183 | 105 | 278 | 136 |
| all_full | exclude_administrative_receipt_gaps | raw | 183 | 105 | 278 | 158 |
| tensorrt_full | exclude_administrative_receipt_gaps | comparison | 115 | 41 | 171 | 75 |
| tensorrt_full | exclude_administrative_receipt_gaps | raw | 115 | 41 | 171 | 97 |
| vendor_full | exclude_administrative_receipt_gaps | comparison | 68 | 64 | 107 | 61 |
| vendor_full | exclude_administrative_receipt_gaps | raw | 68 | 64 | 107 | 61 |

Die folgenden Auswahlen berechnen die zulässige schnellste und energieärmste Fullalternative je Split nach jedem Filter neu. Baseline-/Richtungswechsel beziehen sich auf all_admitted mit Vergleichsenergie; ausgeschiedene Fälle sind keine Richtungswechsel. Modelloptima werden in model_setup_sensitivity_optima.csv ebenfalls neu ausgewählt.

| Filter | Energie | Performance n | schneller | Energie n | energieärmer | andere Energie-Full | Energie-Richtungswechsel |
|---|---|---:|---:|---:|---:|---:|---:|
| all_admitted | comparison | 132 | 44 | 188 | 60 | 0 | 0 |
| all_admitted | raw | 132 | 44 | 188 | 75 | 37 | 15 |
| both_reference_close | comparison | 123 | 44 | 171 | 57 | 1 | 0 |
| both_reference_close | raw | 123 | 44 | 171 | 72 | 38 | 15 |
| exclude_administrative_receipt_gaps | comparison | 115 | 38 | 171 | 60 | 0 | 0 |
| exclude_administrative_receipt_gaps | raw | 115 | 38 | 171 | 75 | 20 | 15 |

## Ausgewählte Graphassoziationen

Die folgenden stärksten absoluten Korrelationen (mindestens zehn ausgewertete Grenzen) sind ebenfalls post hoc ausgewählt. Das Vorzeichen beschreibt die beobachtete Rangordnung, keinen isolierten kausalen Mechanismus.

| Modell | Setup | Runner | Graphmerkmal | Messgröße | n | Spearman rho |
|---|---|---|---|---|---:|---:|
| regnet_x_1_6gf | H10 | native | topological_position | raw_j_per_task | 20 | -0.9970 |
| regnet_x_1_6gf | H10 | native | flops_left_ratio | raw_j_per_task | 20 | -0.9970 |
| regnet_x_1_6gf | H10 | native | topological_position | fps | 20 | 0.9955 |
| regnet_x_1_6gf | H10 | native | flops_left_ratio | fps | 20 | 0.9955 |
| mobilenet_v3_large | H8 | native | topological_position | fps | 17 | -0.9779 |
| mobilenet_v3_large | H8 | native | flops_left_ratio | fps | 17 | -0.9779 |
| mobilenet_v3_large | H8 | generic | topological_position | fps | 17 | -0.9681 |
| mobilenet_v3_large | H8 | generic | flops_left_ratio | fps | 17 | -0.9681 |
| mobilenet_v3_large | H8 | native | topological_position | raw_j_per_task | 17 | 0.9657 |
| mobilenet_v3_large | H8 | native | flops_left_ratio | raw_j_per_task | 17 | 0.9657 |

Graphposition und Schnittgröße verändern auch die Arbeitsaufteilung. Die gebundenen Workerzeiten ermöglichen eine dazu passende Engpasshypothese: eine höhere P2-/Completionzeit kann den Durchsatz trotz geringem P1-Aufwand begrenzen. Aus überlappenden Pipelinezeiten und den gemeinsamen Änderungen von Modellpartition, Precision und Runtime lässt sich jedoch kein einzelner kausaler Effekt isolieren.
