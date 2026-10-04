# Split/Full-Nutzen und Energie: tatsächliche post-hoc-Auswertung

Die 204 Splitfälle erlauben 408 deskriptive Paarvergleiche gegen **42 einmal gemessene Fullbaselines**, jeweils drei Replikate. Davon sind 392 semantisch bestätigt. Splitten spart gegenüber Vendor Full häufiger Energie als gegenüber TensorRT Full; trotzdem existieren zahlreiche schlechtere Splitpunkte und vollständige Gruppen ohne gleichzeitigen Vorteil. Die folgenden Effekte beschreiben die erfassten Software-/Hardwarepfade und diesen Kandidatenbestand. Sie isolieren keinen kausalen Effekt des Splitten oder eines Herstellers.

Plan: `energy_plan.md`. Reproduktion: `scripts/analyze_energy.py --source-root PATH_TO_EXISTING_PUBLIC --output-root PATH_TO_DEEP_ANALYSIS`. Sämtliche Zahlen stammen aus den vorhandenen kompakten Produktprojektionen; keine Messung, Inferenz oder Kompilierung wurde gestartet. Es werden ausschließlich neue Ableitungen geschrieben.

## Definitionen, Zulässigkeit und Abhängigkeit

Primär pro Energiereplikat: **J/task = E/N**, **P = E/T**, **R_E = N/T**, jeweils dasselbe tatsächlich aktive Fenster. Die 738 Replikate gehören zu 246 Fällen (204 Splits + 42 Fulls). Fallwerte sind die ursprünglichen Mittel der drei Replikatquotienten. `tables/energy_recomputed_repeats.csv` enthält E, N, T und die neu berechneten Quotienten; `energy_cases.csv` die Mittel, Mediane, Minima, Maxima und gepoolten Sensitivitätswerte. Separat gemessene Native-Performance-FPS dienen niemals als Energienenner.

Die Joins verwenden Kohorte, Modell, Fall, Setup und Backend eindeutig; doppelte Fullidentitäten werden abgewiesen. Exakte vorhandene Produktgruppen enthalten Modell, Setup, Richtung, Split-Boundarypräzision, Vergleichsbackend, Completed-Endpoint und Messgrenze sowie Energiefenster, physikalischen Scope und Kalibrierung. Inputgleichheit wird aus den ursprünglichen produktgeprüften deskriptiven Paaren übernommen: Der vorhandene Reader prüft Modell-/Input-/Dataset-/Preprocessingidentität, Task, Completed-Endpoint, Kalibrierung und Fenster sowie verträgliche Dauer. Die jeweils gleiche eindeutige Fullreferenz verbindet Splitkandidaten innerhalb der Gruppe. Die kompakte Projektion enthält keine erneuten Inputbytes; eine zweite Byteprüfung wurde nicht behauptet.

Full-Ausführungspräzision bleibt separat sichtbar: TRT `fp16`; Vendor Full explizite HEF-/DXNN-Artefaktidentität. Die Split-Boundarybezeichnungen `float32_layout_fp16` bzw. `uint8_dequant_fp16` beschreiben andere Teile des Ausführungspfads. Die Ergebnisse vergleichen diese vorhandenen Implementierungen, keine kontrolliert auf gleiche interne Quantisierung gebrachten Engines. Keine setupübergreifenden Paretofronten oder gepoolten Rangtests.

Alle Quotienten in `energy_split_full.csv` sind **Split / Full**: Für Energie ist <1 günstig, für Durchsatz >1. Leistung ist Full-System-Leistung, keine Beschleunigerleistung. Die neun Kombinationen aus drei Split- und drei Full-Replikaten sind eine Sensitivitätsmenge, keine neun unabhängigen Versuche und keine synchronisierten A/B-Paare. Wiederverwendungszahlen stehen in `energy_full_baselines.csv`; die 408 Paare werden nicht als 408 unabhängige Baselines oder Studien interpretiert.

## A: Wann lohnt Splitten gegenüber welcher Fullbaseline?

| Population | Baseline | Paare / verschiedene Fulls | energieärmer | schneller in E-Fenster | beides | weder noch |
|---|---|---:|---:|---:|---:|---:|
| technisch/deskriptiv | Vendor | 204 / 21 | 142 | 182 | 142 | 22 |
| technisch/deskriptiv | TRT | 204 / 21 | 121 | 93 | 86 | 76 |
| semantisch bestätigt | Vendor | 188 / 18 | 128 | 166 | 128 | 22 |
| semantisch bestätigt | TRT | 204 / 21 | 121 | 93 | 86 | 76 |
| semantisch + beide reference_close | Vendor | 140 / 11 | 80 | 118 | 80 | 22 |
| semantisch + beide reference_close | TRT | 187 / 21 | 118 | 91 | 84 | 62 |

Beleg: `tables/energy_sensitivity.csv`, `view=augmented,attestor_gap=included`, getrennte `filter` und `baseline_kind`. `semantic_reference_close` prüft die tatsächliche Accuracy von Split **und Full**, kein unsichtbares Weglassen schlechter Fulls. Neun der 21 Vendor-Fulls haben `accuracy_loss` (fünf H8, vier H10), alle 21 TRT-Fulls sind `reference_close`. Die zusätzliche strengere Generic↔Native-Qualitytransferbindung ergibt 139 Vendor- bzw. 184 TRT-Paare, davon 79 bzw. 83 mit beiden Vorteilen. Diese Bindung ist eine getrennte Sensitivität und nicht mit der Accuracyentscheidung identisch.

Die deskriptiven Energiequotienten reichen gegen Vendor Full von **0,1624 bis 2,7992** (Median 0,7629), gegen TRT von **0,2150 bis 4,1021** (Median 0,9577). Die Durchsatzquotienten reichen von 0,4508 bis 11,2823 (Median 1,7590) bzw. 0,1634 bis 8,2822 (Median 0,9735). Das sind Verteilungsbeschreibungen des ungleich besetzten Bestands; Klassifikationsgruppen mit 17–20 Punkten erhalten dabei mehr Gewicht als YOLO-Gruppen mit drei Punkten. Sie sind kein populationsweiter Hardwareeffekt. Vollständige Min/Q25/Median/Q75/Max, alle Einzelpunkte und leere Filtergruppen stehen in `energy_group_distributions.csv` und `energy_split_full.csv`.

**Gegenbefunde:** Gegen Vendor Full besitzen 40 Punkte ausschließlich einen Durchsatzvorteil, aber keinen Energievorteil. Gegen TRT sparen 35 Punkte Energie bei geringerem Durchsatz, sieben sind schneller bei höherer Energie, 76 liefern keines von beiden. In ResNet/DeepX spart **kein einziger der 19 Splits** gegenüber Vendor Full Energie (bestes Verhältnis 1,0103). Gegen TRT haben ResNet/DeepX, YOLO26m/DeepX, YOLO26m/H8, YOLO26s/DeepX und YOLOv7/DeepX sowie YOLOv7/H10 keinen Split mit beiden Vorteilen. Diese Gruppen bleiben vollständig sichtbar.

Konkreter negativer Fall: **ResNet/DeepX b023**, `BASE-PAIR-081`, ist semantisch bestätigt und auf beiden Seiten `reference_close`. Der Split erreicht 144,955 Task/s und 0,134801 J/task; Vendor Full 321,571 Task/s und 0,048157 J/task. Trotz 19,539 gegenüber 15,486 W folgt ein Energieverhältnis von 2,7992 und ein Durchsatzverhältnis von 0,4508. Ein technisch korrekt gemessener Qualitäts-PASS garantiert somit keinen Ausführungsnutzen.

Konkreter positiver Fall: **YOLOv7/H8 b066**, `YOLO-SEM-23/24`, erreicht in seinen Energiefenstern 110,674 Task/s, 0,324744 J/task und 35,941 W. Die entsprechenden Fulls erreichen Vendor 13,499 Task/s und 1,250346 J/task bzw. TRT 13,363 Task/s und 1,510593 J/task. Gegen TRT ergeben sich 8,2822× Durchsatz und 0,2150× Energie. Das gehört zum aktuellen Prepared-Input-Pfad und seiner gebundenen Engine, nicht zur historischen Paperengine oder anders begrenzten 97-FPS-Zahl. Die höhere Leistung bei deutlich größerem Durchsatz erklärt den Quotienten algebraisch; eine isolierte kausale Laufzeiterklärung folgt daraus nicht.

## D: Durchsatz- oder Energiebester?

In **17/21** exakten Gruppen fallen höchster Energie-Fensterdurchsatz und geringste J/task zusammen. Bei Verwendung der separat aufgenommenen Native-Performance-FPS sind es **15/21**. Dieser Unterschied zeigt, weshalb Performance-FPS nicht in E/N eingesetzt werden dürfen. Technische Paretofronten stimmen fallweise mit der bisherigen Produktdarstellung überein.

| Gruppe | schnellster / sparsamster Split | schnellster: Task/s; J/task | sparsamster: Task/s; J/task | Energieaufschlag des Schnellsten | Durchsatzverlust des Sparsamsten |
|---|---|---:|---:|---:|---:|
| MobileNet/DeepX, n=17 | b056 / b135 | 789,611; 0,024803 | 647,020; 0,024761 | 0,172 % | 18,058 % |
| ResNet/DeepX, n=19 | b002 / b119 | 439,591; 0,061350 | 331,604; 0,048653 | 26,097 % | 24,565 % |
| ResNet/H8, n=19 | b031 / b060 | 626,885; 0,047715 | 615,646; 0,042286 | 12,837 % | 1,793 % |
| YOLO26m/DeepX, n=3 | b038 / b043 | 59,222; 0,425048 | 58,801; 0,423072 | 0,467 % | 0,711 % |

Belege: `energy_selection.csv`, `view=augmented,filter=technical`, und `energy_pareto.csv` mit allen Punkten. Der Nenner des Energieaufschlags ist die Energie des sparsamsten Splits; der Nenner des Durchsatzverlusts ist der schnellste Durchsatz. Keine neue Einsatzschwelle wird daraus abgeleitet.

Beide ResNet-Gegenfälle behalten jeweils dieselben Gewinner in allen drei Einzelreplikaten und besitzen gegenüber ihren Konkurrenten getrennte beobachtete Min/Max-Bereiche. MobileNet/DeepX ist ein schwacher Trade-off: Schnellster und Sparsamster stimmen jeweils nur in 2/3 Replikaten mit der Mittelwertauswahl überein und die Bereiche überlappen. YOLO26m/DeepX behält beide Gewinner in allen drei Replikaten, aber die kleinen Unterschiede trennen die Bereiche nicht. Ein überall gleicher Gewinner bedeutet folglich nicht automatisch einen gut aufgelösten Abstand.

Insgesamt ist der Durchsatzgewinner in **19/21**, der Energiegewinner in **18/21** Gruppen über alle drei Einzelreplikate stabil. Vollständig getrennte beobachtete Bereiche bestehen für **18/21** Durchsatz- und **16/21** Energiegewinner. Es gibt keine exakten Mittelwert-Ties; bei einem Tie verwendet die Ableitung die dokumentierte lexikographische Fall-ID. Bereiche und Replikatvorkommen sind keine Konfidenzintervalle.

`reference_close_native` (187 Splitfälle) und das produktidentische `reference_close_transfer` (184) sind getrennte Paretoansichten. In der letzteren ändern sich insbesondere MobileNet/H10 (17→9 Kandidaten; Energiebester b085→b074), YOLO11/H8 (3→2; b120→b062) und YOLOv7/DeepX (3→2; b044→b066). YOLO26s/H10 enthält ebenfalls nur zwei und MobileNet/H8 acht Kandidaten. Auch in der strengeren Ansicht bleiben 17/21 gemeinsame Gewinner; das bedeutet keine unveränderte Auswahl aller Fälle.

## Robustheit, algebraische Kopplung und Hostnormalisierung

- **Replikatquotienten:** 136/142 deskriptive Vendor-Paare mit beiden mittleren Vorteilen behalten beide Vorzeichen in allen neun Replikatkombinationen; bei TRT sind es 86/86. Unter Semantik+beide reference_close sind es 74/80 bzw. 84/84. Das sind Sensitivitätszählungen, keine Signifikanztests.
- **Basis/Zusatz:** Die Basis enthält 130/192 Vendor- und 82/192 TRT-Paare mit beiden Vorteilen. In der postgeplanten Ergänzung sind es 12/12 bzw. 4/12. Nach Semantik und beiderseitiger reference_close bleiben nur vier Vendor-Zusatzpaare; alle vier haben beide Vorteile. Diese bedingt ausgewählten Zusatzpunkte belegen keine repräsentative Verbesserung einer Grundgesamtheit.
- **Aggregation:** Gepooltes E/N weicht um maximal 0,4908 % vom primären Mittel der Einzelquotienten ab (YOLOv7/DeepX TRT Full). Pooling und Replikatmedian ändern in keiner der 21 technischen Gruppen den Durchsatz- oder Energiegewinner. Die Paarentscheidung „Energie <1“ ändert durch Pooling ebenfalls nicht ihr Vorzeichen. Diese numerische Robustheit macht die beiden Aggregationen begrifflich nicht gleich.
- **Kopplung:** Auf Replikatebene gilt exakt J/task=P/R_E. Getrennte Mittel erfüllen diese Gleichung nicht exakt: maximale relative Differenz 0,4903 % auf Fallebene, 0,4925 % bei Paarquotienten. `energy_split_full.csv` liefert Power-, Rate- und Energiequotienten sowie ihre logarithmischen Komponenten; `energy_selection.csv` die Leistungs-/Durchsatzspannweiten innerhalb jeder Gruppe. Eine starke negative Korrelation zwischen Energie und Durchsatz wäre daher kein unabhängiger neuer Befund. Zum Beispiel schwankt die Leistung in ResNet/DeepX um Faktor 1,672, der Fensterdurchsatz um 3,033; beides trägt zum Trade-off bei.
- **Dominanter H8/b066-Fall:** Ohne diesen Punkt bleibt die Vendor-Medianenergie 0,7643 statt 0,7629, bei TRT 0,9585 statt 0,9577. Die TRT-Maximalrate fällt von 8,2822 auf 5,0566; 85/203 statt 86/204 Punkte behalten beide Vorteile. Der Extremwert ist sichtbar empfindlich, die mittige Verteilungsbeschreibung kaum. Tabelle `energy_dominant_case_sensitivity.csv` enthält dieselbe Prüfung für alle Filter.
- **Historischer Attestor:** 21 TRT-Fulls tragen die im Ausgangsarchiv deklarierte Quellenlücke, betroffen sind alle 204 TRT-Paare. Ihre Entfernung lässt **keine TRT-Vergleichsmenge** zurück; ein „robuster TRT-Effekt ohne betroffene Referenzen“ wäre unzulässig. Vendor-Paarergebnisse bleiben unverändert. `energy_sensitivity.csv` enthält deshalb explizite Nullmengen mit unbekannten, leeren Quantilen. Dies ist eine Provenienzgrenze und kein behaupteter Messfehler.
- **21 sekundäre Hostnormalisierungen:** `energy_host_normalization_secondary.csv` hält diese vorhandenen Schätzungen getrennt. Gegen solche gekürzten TRT-Referenzen sparen 80/204 Splits Energie, gegenüber ungekürzter Full-System-Energie 121/204. Diese alternative physikalische Referenz ersetzt die Primäranalyse nicht; die 42 Roh-Fulls und alle Originalwerte bleiben erhalten. Generic-Energie existiert nicht.

## Eine konkret belegte Darstellungsgrenze der bisherigen kompakten Tabelle

Die ursprüngliche Tabelle `inputs/energy_split_full_pairs.csv` benutzt `baseline_energy_per_work_j` mit zwei Bedeutungen: In **192 Basis-TRT-Zeilen** steht die vorhandene hostnormalisierte Sekundärenergie, in den zwölf ergänzten TRT-Zeilen und allen Vendorzeilen die rohe Full-System-Energie. `descriptive_energy_ratio` war bereits korrekt gegen ungekürzte FS-Energie gerechnet. Die Messwerte und ursprünglichen Quotienten sind daher nicht fehlerhaft, aber eine erneute Division der zwei allgemein benannten Felder wäre falsch.

Beleg `BASE-PAIR-002`, MobileNet/DeepX b001: Split 0,04432113639 J/task; ursprüngliches allgemein benanntes Fullfeld 0,02415942036; tatsächliche ungekürzte Fullenergie 0,02738276288. Der korrekte Primärquotient ist **1,61857796**; blindes Dividieren durch das Legacyfeld ergäbe **1,83452814**, die sekundäre Hostnormalisierung. Die Bedeutung wurde gezielt im bestehenden korrigierten Produktreport und `native_energy_reporting` bestätigt; keine weiteren privaten Rohdaten wurden benötigt.

Die neue Ableitung berechnet sämtliche Primärwerte aus E/N und benennt das alte Feld `original_report_selected_baseline_j_per_task`, ergänzt seine Rolle und stellt `baseline_j_per_task` als ungekürzten Primärwert bereit. `energy_legacy_field_audit.csv` belegt Vorher/Nachher für alle 408 Paare. Kein historisches Original, Quellflag oder Release wurde verändert.

## Die 16 Semantikgrenzen bleiben individuell sichtbar

`energy_semantic_limits.csv` enthält jede betroffene Fall-ID, den ursprünglichen Grund, die deskriptiven Quotienten und ihre Fullreferenz. Acht historische DeepX-Detektionspaare haben fehlende/abweichende Decoder-/NMS-Identitätsbelege; diese allein sind keine nachgewiesenen numerischen Fehler. Sechs YOLO26s-Paare teilen die zwei negativ geprüften H8-/H10-Vendor-Fulls: die vorhandene gespeicherte Outputprüfung trifft jeweils 9/14 Referenzdetektionen, unter der unveränderten 0,8-Grenze. Zwei zusätzliche YOLO11-Paare haben unterschiedliche Decoderplatzierung ohne gemeinsamen primitiven Inputbeleg. Keine dieser Grenzen wurde positiv gesetzt.

| Beleg | Modell / Setup / Split | Grenze | Energie Split/Full |
|---|---|---|---:|
| BASE-PAIR-113 | yolo11l / DeepX / b003 | Decoder-/NMS-Identitätsbeleg fehlt/abweichend | 0.9861 |
| BASE-PAIR-115 | yolo11l / DeepX / b062 | Decoder-/NMS-Identitätsbeleg fehlt/abweichend | 0.8077 |
| BASE-PAIR-117 | yolo26m / DeepX / b003 | Decoder-/NMS-Identitätsbeleg fehlt/abweichend | 1.1523 |
| BASE-PAIR-119 | yolo26m / DeepX / b038 | Decoder-/NMS-Identitätsbeleg fehlt/abweichend | 0.7995 |
| BASE-PAIR-121 | yolo26m / DeepX / b043 | Decoder-/NMS-Identitätsbeleg fehlt/abweichend | 0.7957 |
| BASE-PAIR-123 | yolo26s / DeepX / b003 | Decoder-/NMS-Identitätsbeleg fehlt/abweichend | 0.7291 |
| BASE-PAIR-125 | yolo26s / DeepX / b021 | Decoder-/NMS-Identitätsbeleg fehlt/abweichend | 0.5191 |
| BASE-PAIR-127 | yolov7_paper / DeepX / b009 | Decoder-/NMS-Identitätsbeleg fehlt/abweichend | 1.0697 |
| BASE-PAIR-251 | yolo26s / H10 / b003 | geteilte Vendor-Full-Ausgabe numerisch negativ | 0.2388 |
| BASE-PAIR-253 | yolo26s / H10 / b021 | geteilte Vendor-Full-Ausgabe numerisch negativ | 0.1624 |
| BASE-PAIR-379 | yolo26s / H8 / b003 | geteilte Vendor-Full-Ausgabe numerisch negativ | 0.3048 |
| BASE-PAIR-381 | yolo26s / H8 / b021 | geteilte Vendor-Full-Ausgabe numerisch negativ | 0.2167 |
| YOLO-SEM-09 | yolo11l / H10 / b120 | Decoderplatzierung; primitiver Inputbeweis fehlt | 0.3946 |
| YOLO-SEM-11 | yolo26s / H10 / b038 | geteilte Vendor-Full-Ausgabe numerisch negativ | 0.1814 |
| YOLO-SEM-17 | yolo11l / H8 / b120 | Decoderplatzierung; primitiver Inputbeweis fehlt | 0.3821 |
| YOLO-SEM-19 | yolo26s / H8 / b038 | geteilte Vendor-Full-Ausgabe numerisch negativ | 0.2617 |

## Tests, Grenzen und geeignete Paperaussage

13 gezielte Tests bestanden (`tests/test_energy.py`): feste Quotientenrechnung, eindeutige Joins, Replikatidentität, Paretorichtung/Ties, Gruppentrennung, unbekannte Nullmengen, Bestandszählungen, fallweise Gleichheit zur bisherigen Produkt-Paretofront, Attestorfilter, Legacyfeld-Rolle, sichtbare leere Filtergruppen und deterministische Regeneration. Reproduktion der 14 CSV-Tabellen und `energy_results.json` ist bytegleich. Maximale Rechenabweichung gegen gespeicherte Replikatquotienten 7,11×10⁻¹⁵. Es wurden keine Toolabnahme, Hardwaretests oder neuen Qualitätsberechnungen ausgeführt.

Für die Hauptdarstellung eignen sich die getrennte Nutzenverteilung gegenüber Vendor und TRT mit Semantik-/Qualitymarkern sowie die beiden stabilen ResNet-Energietrade-offs. Die kleinen MobileNet- und YOLO26m-Differenzen gehören als Gegenbefund ins Supplement. Eine zulässige Formulierung lautet: „On the observed development candidates, the throughput-maximizing and energy-minimizing split agreed in 17 of 21 exact groups, but stable counterexamples showed materially different energy–throughput tradeoffs.“ Zu stark wäre eine universelle Empfehlung des throughputbesten Splits oder ein kausaler Herstellervergleich.

Die Messungen bleiben kurze, kalibrierte, ungekürzte Full-System-Screenings mit drei Wiederholungen; Threads, Thermik, Zeitpunkt und Runtime sind nicht kontrolliert identisch. Tausende Workcounts oder Leistungssamples erhöhen die Zahl unabhängiger Wiederholungen nicht. Min/Max sind keine CI. Alte wissenschaftliche Freigaben bleiben unverändert; dieses Paket macht keine neuen positiven Claim-Gates.
