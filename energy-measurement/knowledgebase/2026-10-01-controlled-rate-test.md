# Knowledgebase-Nachtrag: kontrollierter 2-kS/s-/5-MS/s-Test

Stand: 01.10.2026. Dieser Nachtrag setzt [Prio A vom 30.09.](2026-09-30-prio-a.md) fort und hat für dessen noch offene Statusangaben Vorrang. Die vollständige Knowledgebase vom 30.09. bleibt unverändert erhalten.

## 1. Fester Fenstervergleich abgeschlossen

Der vorbereitete Cachetest wurde auf den echten Twix-Caches ausgeführt: fünf historische Pico-Reihen, drei Raten und jeweils alle 15 Wiederholungen, insgesamt 225 Läufe. Das feste Fenster umfasst 20,0–80,0 s ab gespeichertem Aufnahmebeginn, exakt 60 s je Lauf; zusätzlich wurden 20–40, 40–60 und 60–80 s ausgewertet. Keine ergebnisabhängige Auswahl, keine neue Kalibrierung und kein erneuter Rohdatenbatch.

Der Leistungsabfall bei 5 MS/s gegenüber 2 kS/s bleibt im identischen 60-s-Ausschnitt bestehen: GEMM FP16 -2,299 %, GEMM INT8 -2,567 %, LLM -1,967 %, YOLO FP32 -0,981 %, YOLO INT8 -0,036 %. Die äußere Lastfenstergrenze ist damit nicht die alleinige Ursache.

## 2. Kontrollierter Hardwaretest

GEMM FP16 wurde mit fester Arbeit und kontrollierter Pause gemessen:

- Reihenfolge: 2 kS/s, 5 MS/s, 5 MS/s, 2 kS/s, 2 kS/s, 5 MS/s;
- 250 vollständig protokollierte TensorRT-Queries je Lauf;
- eine zusätzliche ungewertete Konditionierungsausführung mit derselben Arbeit;
- 120 s gemessene Prozessende-zu-Prozessstart-Pause vor jedem gewerteten Lauf;
- drei Wiederholungen je Rate;
- PicoScope INA225NVGPU/NvGpu und Jetson VDD_IN parallel;
- keine Analyse zwischen den sechs Aufnahmen;
- Rohkanäle erhalten, aber nicht Teil des öffentlichen Evidencepakets.

Alle sechs Aufnahmen, Queryzahlen und Pausen sind vollständig. Der erste 100-Query-Versuch wurde vor jeder Messaufnahme kontrolliert gestoppt, weil seine 46,8272 s nicht zum vorab festgelegten 20–80-s-Lastfenster passten; er wird nicht mit dem erfolgreichen Test gepoolt.

## 3. Zentrale Zahlen

Die im Originalreport ausgegebenen Gruppenmediane ergeben für Pico-Lastleistung -0,508 % bei 5 MS/s gegenüber 2 kS/s. Bei nur drei Läufen pro Rate und einem klaren Sitzungsdrift ist dieser Median allein jedoch nicht belastbar. Über alle drei Läufe pro Rate ergeben die arithmetischen Mittel:

| Größe | 2 kS/s | 5 MS/s | 5 MS/s relativ zu 2 kS/s |
|---|---:|---:|---:|
| TensorRT-Zeit für 250 Queries | 117,441667 s | 117,416667 s | -0,021287 % |
| Pico Lastleistung, festes 60-s-Fenster | 34,919299 W | 34,935988 W | +0,047794 % |
| VDD_IN Lastleistung | 34,155372 W | 34,159222 W | +0,011272 % |
| Pico Last minus Vorlauf | 27,275545 W | 27,208911 W | -0,244300 % |
| VDD_IN Last minus Vorlauf | 26,784372 W | 26,793222 W | +0,033042 % |

Der Test liefert damit keine Evidenz für ein intrinsisches mehrprozentiges Leistungsdefizit bei 5 MS/s unter dem kontrollierten Protokoll. Mit n=3 je Rate ist dies keine universelle Gleichheitsbehauptung.

## 4. Additiver Sitzungsdrift im Pico-Stromkanal

Der collector-transformierte Stromkanal steigt über die sechs Aufnahmen nahezu parallel in Vorlauf, Last und Nachlauf. Explorative lineare Steigungen:

- Vorlauf: ungefähr +0,190 mV je Lauf;
- Last: ungefähr +0,202 mV je Lauf;
- Nachlauf: ungefähr +0,181 mV je Lauf.

Die Spannung bleibt praktisch konstant. VDD_IN, TensorRT-Laufzeit, gemeldete Frequenzen und die expliziten CPU/GPU/SOC-Throttle-Flags zeigen keinen vergleichbaren Rateeffekt; die gemeldeten Throttle-Flags blieben null. Das Muster ist mit einem additiven Stromkanal-/Sessiondrift vereinbar. Es lokalisiert die Ursache nicht eindeutig auf INA225, PicoScope-Offset, Probe, Verkabelung oder Software. Kein automatischer Offsetabzug wird angewandt.

## 5. Historische Baseline-Zerlegung

Diagnostisch wurde für die historischen Direkt-Sweeps die zehn Sekunden beschnittene Lastleistung in Vorlaufniveau und `Last minus Vorlauf` zerlegt. 5 MS/s gegenüber 2 kS/s:

| Reihe | gesamte Lastleistung | Vorlaufniveau | Last minus Vorlauf |
|---|---:|---:|---:|
| GEMM FP16 | -2,138756 % | -6,681699 % | -0,566234 % |
| GEMM INT8 | -2,569228 % | -8,302055 % | -0,615881 % |
| LLM | -1,702227 % | -6,689653 % | +0,168251 % |
| YOLO FP32 | -0,943274 % | -2,751570 % | +0,077389 % |
| YOLO INT8 | -0,028740 % | -0,931032 % | +0,440828 % |

Damit erklärt das mitverschobene Vorlaufniveau den Großteil der auffälligen historischen Endpunkttrends. Diese Zerlegung ist eine Diagnose, keine freigegebene Kalibrier- oder Energie-Korrektur: Ein Vorlaufunterschied kann reale Systemleistung oder Messoffset enthalten.

Eine getrennte historische statische 37-W-Reihe zeigt zwischen 2 kS/s und 5 MS/s nur -0,069733 % Medianleistungsänderung; die gesamte Spannweite aller Rate-Gruppenmediane beträgt 0,081546 %. Das spricht gegen einen generischen mehrprozentigen numerischen Integrationsbias, bleibt aber setup-spezifisch.

## 6. Verbindliche Interpretation

- Lastfensterdefinition bleibt methodisch wesentlich, erklärt aber nicht sämtliche Direkt-Sweep-Trends.
- Unter kontrollierter Arbeit und Pause zeigt der neue GEMM-FP16-Test keinen mehrprozentigen 2-kS/s-/5-MS/s-Unterschied.
- Historische Direkt-Sweeps enthalten starke Vorlauf-/Sessionverschiebungen und dürfen nicht als isolierter Samplingfehler interpretiert werden.
- Baseline-subtrahierte Werte dürfen als diagnostische inkrementelle Leistung gezeigt werden, nicht still die Total-Input-Energie ersetzen.
- Common Reference und PSD bleiben die primären Quellen für isolierte Sampling- und Spektralaussagen.
- Die große historische Messkampagne wird nicht wiederholt.

## 7. Provenienz und Grenzen

- Erfolgreicher Hardware-Review: `baseline_20261001_065752Z_c8a3cc42_review_20261001_072601Z_47c45cae.zip`, SHA-256 `ac8e7ceffad42a1bb6a9fdea86a69d825c17695368c29a00548017a4ad1f3187`; 117 Manifestdateien geprüft.
- Kontrollierter Erstversuch, erwarteter Stopp vor Messaufnahmen: `baseline_20261001_064406Z_0d74d15c_review_20261001_064519Z_a68b0490.zip`, SHA-256 `a0f40e57839696693f8642a7b66055da9b2dfc6b705a301993bc7766f28c1aec`.
- Privater Review mit Tabellen/Grafiken: `baseline_rate_test_review_20261001.zip`, SHA-256 `664f33b5e50362bfbe23e1cb1455e448c7c3aa43f840e712839c6b06348c0184`.
- Öffentliche Tabellen: [kontrollierte Gruppenwerte](../2026-10-01-controlled-rate-test/data/controlled-group-stats.csv) und [historische Baseline-Zerlegung](../2026-10-01-controlled-rate-test/data/historical-endpoint-decomposition.csv).
- Pico- und VDD_IN-Fenster sind nicht hardwarezeitsynchron und besitzen unterschiedliche Messgrenzen/Glättungen.
- Das aktuelle INA225NVGPU/NvGpu-Profil ist keine nachträgliche elektrische Abnahme der historischen Jetson-Kampagne.
- Drei Wiederholungen je Rate begrenzen die statistische Aussage.
