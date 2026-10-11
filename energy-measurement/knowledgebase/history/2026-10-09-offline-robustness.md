# Knowledgebase-Nachtrag: Scope- und FP16-Robustheitsprüfung

Stand der Ergebnisprüfung: **09.10.2026**. Dieser Nachtrag ergänzt den
[operativen Einstieg](../Energy_Paper_TIM_KnowledgeBase_CURRENT_2026-10-01.md).
Die historische KB und ursprüngliche Paper-Exporte bleiben erhalten.
Die neuen Zahlen stammen aus einer **zusätzlichen Offline-Sensitivitätsprüfung**,
nicht aus einer neuen Messkampagne und nicht aus einer behaupteten exakten Table-2-Reproduktion.

## 1. Abgeschlossene Scope-Auswertung und verifizierte Pfade

`energy_paper_checks.py` **v1.0.1** meldet `completed_requested_probe`:
**118 erfolgreiche Quellspuren, null Fehler**, sechs Workloads und 59 Tek/Pico-Paare.
IDs 0–9 wurden für GEMM-FP32, GEMM-INT8, YOLO-FP32, YOLO-INT8 und Gemma3-4B
verwendet, IDs 0–8 für ResNet50. Die Inventare zeigen keine mehrdeutigen, unpaarigen
oder zusätzlichen Paare und keine Zugriffs- oder Scanlimitfehler.

Die ausgewählte Rateebene heißt in allen sechs Workloads tatsächlich:

```text
/homes/jwachsmuth/power_measurements/tek_scope_comparison/<workload>/5000000/
```

**Ohne `Sps` am Ordnernamen.** Der ursprüngliche Zusatzcheck v1.0.0 suchte nur unter
`5000000Sps` und fand deshalb keine Scope-Dateien. Seine leeren Scope-Tabellen waren
kein Nachweis fehlender Rohdaten. Der Collector kann auch unnummerierte Dateien in
Run-Unterordnern erzeugen; diese zusätzliche Möglichkeit war nicht die Ursache des
hier durch die Inventare erklärten Nullfunds. Konkrete Rohdateipfade und Fundformen
werden mit dem lokalen `input_inventory.json` ergänzt.

Quellen: [Scope-Summary](../2026-10-09-offline-robustness/scopes/summary.json) und
[Originalbericht](../2026-10-09-offline-robustness/scopes/REPORT.txt).

## 2. Geprüfte Aggregation und Rasterumfang

Die Rückgabe enthält **19.824 Run-Zeilen → 2.016 Workload/Quellen-Zellen → 168
Hüllkurvenzellen**. Die äußeren Q95-Werte wurden mit einer unabhängigen Type-7-Formel
aus je einem gespeicherten inneren Q95 pro physischer Quellaufnahme nachgerechnet,
danach das Maximum über die zwölf Gruppen gebildet. Größter Rechenrest:
`2.22e-16` Prozentpunkte. Die CSVs und die Summary stimmen überein.

Das nominale Raster enthält 19 Raten von 50 bis 160.000 S/s und neun Dauern von
20 ms bis 10 s. Bei nominal 10 s wird ein einziges Fenster mit tatsächlicher Spanne
9,999999 s ausgewertet; bei kürzeren Dauern werden 16 Fenster angesetzt. Pro Rate
sind 64 Phasen vorgesehen. Drei zu kurze Dauer-/Ratenkombinationen fehlen wegen
der Mindestzahl von vier Zielrastersamples.

**Randfall 20 ms / 150 S/s:** je Run nur ein zulässiger von 1.024 versuchten Fällen.
Diese Kombination fehlt im ursprünglichen Export. Sie verändert keines der hier
berichteten persistenten Minima und ist nicht als vollständiger 16×64-Test darzustellen.

Die unabhängige Nachrechnung prüft die äußere Aggregation. Die innere Stufe aus den
Fenster-/Phasenwerten, die Kalibrierung und die ausgeführte Filterung sind damit noch
nicht unabhängig neu gerechnet. Der lokale Detail-Export erhält gezielt die relevanten
Vergleichsvektoren zur weiteren Prüfung.

Quellen: [Run-Tabelle](../2026-10-09-offline-robustness/scopes/scope_per_run.csv),
[Gruppentabelle](../2026-10-09-offline-robustness/scopes/scope_groups.csv),
[Hüllkurve](../2026-10-09-offline-robustness/scopes/scope_envelope.csv) und
[unabhängiger Audit](../2026-10-09-offline-robustness/review/scope_independent_audit.json).

## 3. Vorverarbeitung auf 1 MS/s ist nicht allgemein wirkungslos

Beide Zielratenintegrale werden gegen dieselbe native Referenzenergie ausgewertet.
Ein Pfad rekonstruiert unmittelbar aus nativer 5-MS/s-Leistung, der andere nach
VHQ-Reduktion auf 1 MS/s. Es erfolgt keine zusätzliche Zielratenfilterung.

An 0,5 % oder 1 % wechseln **acht von 168 punktuellen Hüllkurvenentscheidungen**,
jeweils von via 1M bestanden zu nativ verfehlt:

| Dauer | Zielrate | Grenze | Q95 nativ | Q95 via 1M |
|---|---:|---:|---:|---:|
| 20 ms | 100.000 S/s | 1 % | 1,081221 % | 0,951987 % |
| 20 ms | 125.000 S/s | 1 % | 1,063863 % | 0,803916 % |
| 50 ms | 160.000 S/s | 0,5 % | 0,529260 % | 0,478179 % |
| 100 ms | 25.000 S/s | 1 % | 1,073761 % | 0,948999 % |
| 100 ms | 80.000 S/s | 0,5 % | 0,509054 % | 0,461056 % |
| 100 ms | 125.000 S/s | 0,5 % | 0,595404 % | 0,432012 % |
| 2 s | 5.500 S/s | 0,5 % | 0,510485 % | 0,466878 % |
| 5 s | 680 S/s | 1 % | 1,064280 % | 0,979507 % |

Die Hüllkurve dieser nativen Werte wird sechsmal von YOLO-INT8/Tek und zweimal von
GEMM-FP32/Tek bestimmt. Eine Differenz zweier Hüllkurven-Q95 ist kein Quantil der
gepaarten Einzelfalldifferenzen; die bestimmende Gruppe kann zwischen Pfaden wechseln.

Die Referenzintegrale selbst ändern sich über alle ausgewerteten Fenster nur um
maximal **0,000557364 %**. Trotzdem sind die späteren Zielratenintegrale nicht
gleichwertig. Die Integralerhaltung beantwortet daher nicht die frühere Frage nach
dem Einfluss der Zwischenverarbeitung auf Aliasing und Rekonstruktion.

Der Vergleich isoliert den **gesamten Verarbeitungspfad** einschließlich VHQ,
Float32-Darstellung und Interpolation vom gröberen Raster. Er identifiziert nicht
separat den Anteil ausschließlich oberhalb 500 kHz oder einen reinen Filtereffekt.

## 4. Persistente Minima und Abgrenzung zum ursprünglichen Paper

Ein persistentes Minimum muss die Toleranz **an dieser und jeder höheren geeigneten
getesteten Rate** einhalten. Acht punktuelle Wechsel sind keine acht geänderten Minima.
Bei 0,5 % oder 1 % ändern sich zwischen den beiden neuen Pfaden vier Minima; bei
5 % kommen zwei hinzu. Bei 2 % unterscheiden sich die neuen Pfade in ihren Minima nicht.

Ausgewählte Vergleiche, sämtliche Raten in S/s:

| Dauer | Toleranz | Ursprünglicher Export | Neue Probe via 1M | Neue Probe nativ |
|---|---:|---:|---:|---:|
| 20 ms | 1 % | 160.000 | 100.000 | 160.000 |
| 50 ms | 0,5 % | 160.000 | 160.000 | nicht erreicht |
| 100 ms | 0,5 % | 160.000 | 80.000 | 160.000 |
| 2 s | 1 % | 2.000 | 16.000 | 16.000 |
| 5 s | 1 % | 680 | 680 | 1.200 |
| 10 s nominal | 0,5 % | 16.000 | 16.000 | 16.000 |

Alle 36 Dauer-/Toleranzkombinationen, einschließlich 2 % und 5 %, stehen in
[scope_persistent_minima.csv](../2026-10-09-offline-robustness/review/scope_persistent_minima.csv).
„Nicht erreicht“ bedeutet nur: nicht innerhalb des getesteten Rasters bis 160.000 S/s.
Die Originalwerte wurden aus `mode=phase_only` des öffentlichen
[Common-Reference-Exports](../PSD_Analysis_multi_workload_documentation_artifacts/common_reference/common_reference_summary.csv)
nachgerechnet. Die 2-/5-%-Werte sind eine Zusatzableitung aus diesem Export, keine
entsprechenden Spalten der ursprünglichen Table 2.

**Besonders wichtig: 2 s / 2 kS/s bleibt punktweise unter 1 %.** Das neue native Q95
beträgt 0,853155 %, via 1M 0,792110 %. Bei **2 s / 9,4 kS/s** liegt dagegen
ResNet50/Tek in beiden neuen Pfaden knapp über der Grenze:

- ursprünglicher Export: **0,978769 %**;
- neue Probe via 1M: **1,018562 %**;
- neue Probe nativ: **1,019762 %**.

Das erklärt das persistente 16-kS/s-Minimum der neuen Probe. Der entscheidende
Unterschied zum Original ist bereits im via-1M-Zweig vorhanden und kann daher nicht
allein dem Weglassen der Zwischenreduktion zugeschrieben werden.

Weitere Originalabweichungen bei 2 %: Für 20/50 ms liefern beide neuen Pfade
80 kS/s statt ursprünglich 45/25 kS/s. Ausschlaggebend sind die neuen
Gemma3-4B/Tek-Spitzen bei 45 kS/s. Ursache der Unterschiede zum ursprünglichen
Fenster-/Phasen-/Interpolationsraster ist aus den Aggregaten nicht identifiziert.
Es erfolgt keine nachträgliche Rasterwahl anhand günstiger Ergebniswerte.

## 5. Strommodell: 51 markierte Aufzeichnungen

Die Summary meldet Stromwerte außerhalb des verwendeten Modellbereichs 0–3,5 A in
**49 von 59 Tek-Spuren** (alle Workloads außer Gemma3-4B) und **zwei von 59 Pico-Spuren**
(GEMM-FP32, IDs 6 und 7). Das Modell wurde dort extrapoliert, nicht geclippt.

Der Rechenlauf und die Auswertung desselben definierten Leistungsmodells sind erfolgt.
Die physikalische Bedeutung der Extrapolation erfordert zunächst deren Größenordnung:
Anzahl betroffener Samples geteilt durch `n_samples`, sowie `current_min_A` und
`current_max_A`. Diese Felder sind in den bestehenden Record-Audits gespeichert und
werden kompakt exportiert. Separate Zählungen unter 0 bzw. über 3,5 A und Zeitpositionen
der Überschreitungen sind dort nicht gespeichert und werden nicht aus dem Flag erfunden.
Eine erfolgreiche Verarbeitung bestätigt keine neue absolute Kalibrierung oder
extern verifizierte Hardware-Zeitkontinuität.

## 6. Getrennte FP16-Prüfung: Kohorten und Energie

Die vorherigen normalen und Full-Grid-Rückgaben enthalten identische FP16-Ergebnisse
für dieselben 15 physischen Aufzeichnungen. Im Full-Grid-Aufruf änderte sich nur das
damals noch erfolglose Scope-Raster. Sie werden nicht als 30 unabhängige Messungen gezählt.
Die neue Scope-only-Summary enthält folgerichtig keine neuen FP16-Ergebnisse.

Q95 bei 50 S/s:

| Kohorte | direkt nativ | via 1M |
|---|---:|---:|
| IDs 2–14 | 0,629400 % | 0,630735 % |
| IDs 0–14 | 0,634957 % | 0,632085 % |

Damit bleibt 50 S/s für das empirische 1-%-Q95-Kriterium ausreichend. Bei 85 S/s
bleiben alle 960 geprüften Fälle je Pfad unter 1 %; größtes Maximum 0,879285 %.
Die maximale punktweise Änderung des relativen Fehlers durch den Zwischenpfad beträgt
bei 50 S/s 0,014832 Prozentpunkte. Keine untersuchte 1-%-Einzelfallentscheidung wechselt.

Der früher im Paper genannte Maximalfehler **1,071 %** wird vom Zusatzraster nicht
reproduziert: nativ **1,236306 %**, via 1M **1,229935 %**, jeweils schon innerhalb
der IDs 2–14. Der Unterschied wird weder durch IDs 0/1 noch allein durch die
Zwischenreduktion erklärt. Ein anderer Phasenanker ist eine konkrete mögliche
Erklärung, aber keine belegte historische Implementierung. Der ursprüngliche
Q95-Wert 0,641 % wird ebenfalls nicht durch die Zahlen des Zusatzchecks ersetzt,
ohne dessen andere Auswertungsgrundlage kenntlich zu machen.

Alle 15 Energieintervalle stimmen mit den gespeicherten inklusiven YAML-Indizes
überein; ihre tatsächliche Integrationsspanne beträgt 103,9999998 s bei nominal
104 s. Die Wirkung des Einschlusses von IDs 0/1 ist geprüft; der historische Grund
für ihre ursprüngliche Nichtauswahl bleibt mangels Originalmetadaten offen.

Quelle: [FP16-Energieergebnisse](../2026-10-09-offline-robustness/fp16/fp16_energy_selection.csv)
und die dort mitgesicherten 15 Record-JSONs.

## 7. FP16-Spektren: Robustheit bestätigt

Die Baseline reproduziert die publizierten Rundungswerte 53,83 kHz für Median f95,
71,06 kHz für Median f99 sowie Q05-Abdeckungen 97,536 % und 99,316 %.

| Kohorte | aktive/Idle-Welchsegmente | Q05 bei 125 kS/s | Q05 bei 160 kS/s |
|---|---:|---:|---:|
| IDs 2–14 | 19/7 | 97,536105 % | 99,316018 % |
| IDs 2–14 | 7/7 | 97,536212 % | 99,316305 % |
| IDs 0–14 | 19/7 | 97,540269 % | 99,319186 % |
| IDs 0–14 | 7/7 | 97,540788 % | 99,319560 % |

Auch mit einem identischen aktiven 2-s-Block gegen jeweils eine der beiden Idle-Hälften
(durchgehend 3/3 Segmente) bleiben die Entscheidungen bestehen. Über alle 15 Runs
und vier aktive Varianten beträgt die kleinste Einzelabdeckung 97,501520 % bzw.
99,293120 %. Auf dem ursprünglichen Ratenraster bleiben 125/160 kS/s damit die
kleinsten bestehenden Raten für 95/99 %.

Die größere positive Differenz der beiden Idle-Hälften je Run beträgt relativ zum
aktiven Baseline-Überschuss im Median 0,171690 %, maximal 0,483522 %. Der Rest ist
nicht null; Schätzerschwankung und zeitliche Idle-Änderung werden dadurch nicht getrennt.
Das ist eine deskriptive Robustheitsdiagnose, keine Konfidenzgrenze, Bias-Korrektur
oder Obergrenze des Fehlers einer unbekannten wahren Workload-Varianz.

Quelle: [FP16-PSD-Auswahl](../2026-10-09-offline-robustness/fp16/fp16_psd_selection.json)
und [PSD-Einzelwerte](../2026-10-09-offline-robustness/fp16/fp16_psd_per_run.csv).

## 8. Sicherung, offene Details und Paperumfang

Die gelieferten Scope-CSVs, Summary und Originalbericht sowie die vollständigen kleinen
FP16-Ergebnisse sind im [Evidenceordner](../2026-10-09-offline-robustness/README.md)
enthalten. Die gesamte Scope-ZIP über 500 MB wurde nicht übertragen oder geprüft.

Der Archivhelfer liest ausschließlich vorhandene lokale Ergebnisse unter
`~/Reports/energy-paper-check-scopes`, ergänzt Laufmetadaten und erstellt:

- `record_audit.jsonl`: alle 118 Record-Köpfe und Fensterköpfe ohne große Vergleichslisten;
- `critical_comparisons.jsonl.gz`: die unveränderten Vergleiche der bestimmenden Gruppen
  für die acht Schwellenwechsel und für 2 s / 9,4 kS/s;
- einen kleinen Index der übernommenen Dateien und des lokalen Vollarchivs.

Damit lassen sich Umfang der Modell-Extrapolation und die kritischen Fälle prüfen,
ohne Rohdaten oder die vollständige ZIP erneut zu übertragen. Der konkrete
Detail-Export bleibt bis zum erfolgreichen lokalen Aufruf und Commit ausstehend.
Die ursprünglichen Records und das vollständige Archiv bleiben lokal erhalten.

**Paperentscheidung:** Umfang und Verständlichkeit sollen nicht wachsen. Die neuen
Prüftabellen bleiben in der Evidence. Im vorhandenen Haupttext werden höchstens
Methodensätze ersetzt und die Bezugsauswertung einzelner Zahlen präzisiert.
Der exakte FP16-Maximalwert 1,071 % sollte bis zur Klärung nicht als durch diesen
Check bestätigt behandelt werden; die robuste 50-/85-S/s-Unterscheidung bleibt.
Bei Table 2 muss die Rasterabhängigkeit, insbesondere für das persistente
1-%-Minimum bei 2 s, geklärt oder entsprechend eingegrenzt werden. Keine stillschweigende
Vermischung ursprünglicher Werte und neuer Sensitivitätsergebnisse.
