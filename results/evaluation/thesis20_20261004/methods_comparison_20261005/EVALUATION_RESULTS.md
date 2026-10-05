# Vorhandene Rangverfahren: tatsächlicher Offlinevergleich

Die gemessene Generic-Completion erreicht unter den 204 vorhandenen Splitkandidaten **10/21 Top1-Treffer**, die fünf verfügbaren statischen Methoden **5–7/21**. Das ist keine allgemeine Überlegenheit in jeder Gruppe oder für jedes Auswahlziel. Alle fünf statischen Methoden treffen in den neun Klassifikationsgruppen **0/9** exakte Native-Beste; ihre Treffer liegen in den zwölf sehr kleinen YOLO-Gruppen. Generic-Completion trifft 3/9 Klassifikations- und 7/12 YOLO-Beste. Die Verfahren und ihre historischen Parameter bleiben unverändert, einschließlich des nur H10-bezogenen gespeicherten Hardwareprofils.

## Gleiche Kandidaten, unterschiedliche Proxies

`inputs/method_availability.csv` nennt Quellen, Einheiten und Parameter. Von neun inventarisierten Methoden sind fünf statische Scores sowie die beiden gemessenen Proxies auswertbar. Native-Handovermodell und originales GUI-SystemSpec bleiben mangels vollständiger historischer Bindung **unverfügbar**; sie erhalten keine Nullprognose. Die eigentliche Scoreberechnung und Vollgraph-Normierung stehen in `scripts/reproduce_method_scores.py`; nachträgliche Parametertuningversuche wurden nicht durchgeführt.

Primär gelten die exakt gleichen gemessenen Kandidaten je Modell/Setup/Richtung/Boundarypräzision/Vergleichsbackend/Endpoint/Messgrenze. 204 technisch paarbare Fälle, 201 mit bestehendem Qualitytransfer und 184 zusätzlich beidseitig reference_close bleiben getrennt. Die Rangmetriken verlangen n≥3. Deshalb sind bei Qualitytransfer 195 Fälle in 18 Gruppen, bei reference_close 178 Fälle in 18 Gruppen rangmetrisch auswertbar; jeweils drei Zweiergruppen bleiben sichtbar, ohne aufgefüllte Kandidaten. Die übrigen Fälle bleiben im Fallbestand erhalten.

Die historische Raw-Generic-Sicht verwendet ausschließlich die genaue Basis-Schnittmenge von **192 Fällen**. Davon liegen 177 in zwölf Gruppen mit n≥3; neun weitere Gruppen enthalten zusammen 15 Fälle und bleiben unter der Rangschwelle. Auf genau diesen zwölf ursprünglichen Gruppen trifft Raw-Generic 3/12, Generic-Completion 5/12. Diese Zähler dürfen nicht ohne Nennerangabe mit 10/21 nach Augmentierung verglichen werden. Die zwölf kurzen Augmentierungsvorläufe werden nicht als historische Raw-Beobachtungen verwendet.

Alle folgenden Mittel/Mediane fassen **Gruppenmetriken** mit gleichem Gruppengewicht zusammen; es gibt keine gepoolte Modell-/Setup-Rangkorrelation und keinen Signifikanztest. Die zwölf YOLO-Dreiergruppen überwiegen zahlenmäßig die neun Klassifikationsgruppen mit 17, 19 oder 20 Kandidaten. Gesamtmediane sind daher keine Aussage über alle Graphpositionen oder eine repräsentative Gerätepopulation.

| Methode | Top1 /21 | Median Spearman innerhalb Gruppen | Median L_R | Mittel L_R | maximal L_R | Median Energieaufschlag | Mittel Energieaufschlag |
|---|---:|---:|---:|---:|---:|---:|---:|
| Cut payload | 5 | 0,471 | 5,07 % | 25,31 % | 88,49 % | 1,47 % | 49,86 % |
| Weighted score | 7 | 0,611 | 8,03 % | 14,99 % | 66,61 % | 4,39 % | 21,19 % |
| Hardware fit, archiviertes H10-Profil | 5 | 0,500 | 12,81 % | 19,67 % | 68,58 % | 11,72 % | 30,09 % |
| Cycle, no handover | 7 | 0,642 | 8,03 % | 14,99 % | 66,61 % | 4,39 % | 21,19 % |
| Stored stream FPS | 6 | 0,595 | 9,25 % | 17,45 % | 66,61 % | 9,16 % | 23,70 % |
| Gemessene Generic-Completion | 10 | 0,941 | 1,24 % | 12,25 % | 70,61 % | 0,00 % | 26,54 % |

Beleg: `tables/method_summary.csv`, `cohort=augmented,tier=technical,family=all`. Gruppeneinzelwerte und Kendall tau-b stehen vollständig in `method_groups.csv`, alle Fallränge in `method_case_ranks.csv`. L_R=1−R_selected/R_best; der getrennte Cycle-/Kapazitätsregret L_C=R_best/R_selected−1 ist ebenfalls tabelliert, ohne ihn als gemessene Anfragelatenz auszugeben.

**Familienunterschied:** Die mittleren L_R der Klassifikationsgruppen betragen Cut 51,77 %, Weighted/Cycle 22,33 %, Hardware fit 29,29 %, Stored FPS 22,33 % und Generic-Completion 19,76 %. In den YOLO-Gruppen sind es 5,46 %, 9,49 %, 12,46 %, 13,79 % und 6,63 %. Cut wirkt daher im Gesamtmedian besser als mehrere stärker parametrisierte Methoden, während seine großen Klassifikationsfehler den Gesamtmittelwert verschlechtern. Kein einzelner dieser aggregierten Kennwerte beschreibt die ganze Auswahlleistung.

## Nicht unabhängige Verfahren und echte Gleichstände

Weighted score und Cycle ohne Handover wählen in **allen 21 Gruppen denselben Top1**. Ihre vollständigen Rangvektoren sind in 12/21 Gruppen gleich; sie sind unterschiedliche Verfahren mit hier teilweise gleicher Auswahl, keine zwei unabhängigen positiven Befunde. Stored stream FPS und Cycle ohne Handover haben 18/21 gleiche Top1 und 15/21 gleiche vollständige Rangvektoren. Die getrennte Untersuchung der gespeicherten Streamprognose ist somit sachlich begründet. Beleg: `method_order_equivalence.csv`.

Cut payload hat in allen drei YOLO26m-Setups einen identischen niedrigsten Graphbytewert für b038 und b043. Der originale Tool-Tiebreak `(score,boundary,case_id)` wählt b038, obwohl b043 jeweils Native-besser ist. Die verlorenen Durchsätze sind DeepX 0,658 %, H10 1,637 % und H8 0,663 %. Eine günstigste Auflösung dieser drei exakten Ties könnte den Cut-Trefferzähler von 5/21 auf 8/21 ändern. Sie wird als Tie-Sensitivität ausgewiesen und nicht nachträglich zur Hauptregel gemacht. Die zusätzliche historische Listenordnung ändert hier keine Auswahl. Alle anderen fünf auswertbaren Hauptmethoden haben keine Top1-Scoreties. Kleinere als drei Kandidaten und konstante Scores bleiben als eigene Status erhalten.

## Shortlists und analytische Zufallsauswahl

Die Shortlisttabellen trennen „Native-Bester enthalten“ von „Anteil der stabilen Native-Top-k in der Auswahl“. Top3 bei n=3 ist explizit trivial und wird nicht als Methodenerfolg zusammengefasst. Für die neun Klassifikationsgruppen mit n≥17 enthält Generic-Completion-Top3 in **6/9** Fällen den Native-Besten; seine mittlere Top3-Überdeckung ist 55,56 %. Weighted/Cycle trifft den Native-Besten jeweils in 1/9, Cut und Hardware fit jeweils in 2/9, Stored FPS in 1/9.

Der verbleibende mittlere L_R nach Auswahl des tatsächlich besten Native-Kandidaten aus der jeweiligen Dreier-Shortlist ist Generic-Completion **12,51 %**; exakt gleichverteilter Zufall ohne Zurücklegen liefert analytisch **18,49 %**. Weighted/Cycle liegt bei 19,54 %, Stored FPS 20,20 %, Hardware fit 24,81 %, Cut 35,49 %. Das ist ein innerhalb dieser Gruppen berechneter Vergleich vorhandener Werte, kein gemessener Random-Run und keine unabhängige Validierung. Die uniforme Top3-Wahrscheinlichkeit, den Native-Besten zu enthalten, beträgt gruppengemittelt 16,15 %. Belege: `method_shortlists.csv`, `cohort=augmented,tier=technical,family=classification,k=3`.

Für Top1 über alle 21 Gruppen beträgt der analytisch erwartete mittlere L_R 23,27 %. Cut liegt mit 25,31 % darüber; Generic-Completion mit 12,25 % darunter. Diese deskriptive Einordnung bleibt ohne nachträgliche Schwellen-/Methodensuche oder p-Wertbehauptung.

## Energie ist ein zusätzliches Auswahlziel

Primär wird `J_selected/min(J)−1` aus dem **Mittel der drei E/N-Einzelquotienten** berechnet. Keine Generic-Energie wird erfunden; der Methodenscore wählt eine existierende Native-Identität, deren eigene Energieaufnahme herangezogen wird. Geteilte Fullbaselines sind für diese Split-Auswahlfrage nicht nötig; ihre Zahl in dieser Untersuchung beträgt null. Die historische Full-Attestorlücke beeinflusst diese rein splitbezogenen Joins deshalb nicht.

Generic-Completion trifft den energieärmsten Split in **11/21** Gruppen. Trotz Medianaufschlag 0 % liegt sein mittlerer Energieaufschlag mit **26,54 %** höher als bei Weighted/Cycle mit **21,19 %**. Der maximale Aufschlag erreicht bei Generic-Completion 269,88 %, bei Cut 465,22 %. Mehr exakte Durchsatztreffer garantieren somit keine kleinere mittlere Energiestrafe. Die uniforme Auswahl hat einen analytisch erwarteten mittleren Energieaufschlag von 39,31 %.

**ResNet/H8:** Weighted/Cycle/Stored FPS wählen b060, das tatsächliche Energieminimum. Cut wählt b119 (L_R 77,75 %, Energieaufschlag 172,56 %), Hardware fit b052 (12,81 %; 14,92 %), Generic-Completion b002 (13,92 %; 31,40 %). Der Native-Performancebeste b031 erreicht im eigenen Energiefenster 626,885 Task/s und 0,047715 J/task; b060 615,646 Task/s und 0,042286 J/task. Die Energie beträgt bei b031 12,84 % mehr für 1,79 % geringeren Fensterdurchsatz des sparsameren b060. Performance-FPS und Energie-Fensterdurchsatz bleiben ausdrücklich verschiedene Aufnahmen. Belege: `method_groups.csv` und `fig02_selector_energy_cost_source.csv`.

**Negative Generic-Gegenfälle:** RegNet/H10 verliert durch Generic-Top1 70,61 % Native-Durchsatz, Cut 22,75 %. YOLOv7/H8 verliert durch Generic-Top1 52,96 %, Weighted/Cycle wählen den vorhandenen Native-Besten b066. Der b066-C++-Prepared-Input-Pfad unterscheidet sich vom b044-Pythonpfad; dies darf nicht kausal allein dem Cut zugeschrieben werden. Unbekannte oder global empfohlene, aber ungemessene Kandidaten werden nicht zu diesen Zahlen ergänzt.

## Replikate, Filter und Grenzen

Die drei ursprünglichen Native- und Generic-Performancewiederholungen sind die wiederholten Experimente; 1000 Tasks pro Wiederholung erhöhen deren Zahl nicht. Generic-Completion hat neun Kombinationen seiner drei Predictor- mit drei Native-Wiederholungen, statische Methoden und der gespeicherte Raw-Aggregatproxy jeweils drei Native-Varianten. Beim negativen RegNet/H10-Gegenfall bleibt Generic L_R zwischen 70,22 % und 74,67 %, bei YOLOv7/H8 zwischen 52,92 % und 53,11 %; beide haben null Treffer in neun Kombinationen. Keine dieser Spannweiten ist ein Konfidenzintervall.

Energiesensitivität wird in zwei Tabellenfamilien sichtbar: einmal erneute Bestimmung des Energieoptimums pro gespeichertem Wiederholungsindex; einmal neun Vergleiche der drei Replikate des fest ausgewählten Falls gegen die drei des nach Mittelwert optimalen Falls. Gleiche Wiederholungsnummern bedeuten keine zeitgleiche Aufnahme. Wenn Auswahl und Optimum dieselbe Identität sind, ist der **primäre Auswahlfehler null**. Nichtnullwerte zwischen zwei Wiederholungen derselben Identität sind ausdrücklich `same_case_repeat_ratio_variation_not_selection_penalty`, keine Auswahlschuld. Negative einzelne Quotientenabweichungen werden nicht auf null gekürzt.

Unter strikter reference_close-Sicht bleiben 18 ausreichend besetzte Gruppen: Top1 Cut 4/18, Weighted/Cycle 6/18, Hardware fit 5/18, Stored FPS 6/18, Generic-Completion 8/18. Generic-Completion hat dort medianen L_R 1,44 % und mittleren L_R 13,63 %. Qualitytransfer und reference_close sind keine identischen Filter; die drei ausgeschlossenen Augmentierungsfälle bleiben im technischen Bestand dokumentiert. Alle Qualitätsverluste bleiben in der technischen Hauptsicht.

Die gespeicherten Modell-/Hardwareprognosen sind keine gemessenen Runtimekosten. Cutbytes bezeichnen geschätzte Graphnutzlast, kein gemessenes PCIe-Volumen. Alle vorhandenen gespeicherten Streamprognosen tragen `yolov7_streaming_v1`, und der Hardwarefit hat eine historische H10-Bindung. Die Ergebnisse sind eine ehrliche Bewertung dieser konkreten Altverfahren, keine validierte Prognose jedes Geräts. Originale GUI-56,96-FPS-Werte und archivierte 132,967-FPS-Prognosen werden nicht vermischt. Das globale Graphuniversum und die Unterstützung/unbekannte Messlage stehen separat in `method_global_selection.csv`; es gibt keine verdeckte Empfehlung des nächsten gemessenen Ersatzfalls.

## Lieferung und Reproduktion

Zwei neue Hauptabbildungen liegen als PDF/SVG sowie PNG-Vorschau vor: `fig01_ranking_methods_loss` zeigt alle 21 Gruppen und sechs verfügbaren Hauptmethoden; `fig02_selector_energy_cost` zeigt die Energieauswahlkosten und den ResNet/H8-Gegenfall. Kleine exakte Eingabetabellen und englische Captions stehen neben den übrigen Methodenbelegen. Die Figurtexte wurden visuell geprüft; negative, schlechte und gleichwertige Ergebnisse bleiben sichtbar.

```bash
python scripts/reproduce_methods.py --source-root .. --output-root /path/to/fresh/output
```

`--deep-root` kann den unveränderten Vertiefungsbereich explizit angeben; standardmäßig wird `SOURCE_ROOT/deep_analysis` verwendet. Der Einstieg erzeugt zuerst aus den kleinen eingefrorenen Methodeninputs die Score-/Verfügbarkeitsprojektion, danach Gruppenmetriken und Figuren. Die alten THESIS20- und Vertiefungstabellen werden nur referenziert. Er verändert keine Originalmessung oder Tooldatei.

14 fokussierte Evaluatortests bestanden: Rangrichtung, verschiedene Regret-Nenner, ursprünglicher Tie-Key, fehlende Prognosen, kleine Filtergruppen, eindeutige Joins, unveränderte Qualitygates, analytischer Zufall gegen vollständige kleine Teilmengen, Shortlisttiegrenzen, triviales Top3, exakte 204/201/184-Kohorten, Generic-Regression 10/21, gleiche Kandidaten, unkonfigurierte Verfahren und deterministische CSV-/JSON-Reproduktion. Die Scoreextraktion hat separate Tests. Hardware-, Inferenz-, Quality-/Bootstrap- und Kompilierungsläufe wurden nicht ausgeführt.
