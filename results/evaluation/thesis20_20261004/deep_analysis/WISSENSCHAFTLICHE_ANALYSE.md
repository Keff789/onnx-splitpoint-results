# Wissenschaftliche Vertiefung THESIS20

Die vorhandenen Daten liefern mehr als einen technischen Abschluss: **Der Nutzen eines Splitpunkts hängt von Fullreferenz, Qualitymenge und Runner ab; ein guter Generic-Durchsatz ist keine verlässliche universelle Native-Auswahlregel.** Gleichzeitig ist der durchsatzbeste Split häufig, aber nicht immer, auch der energieeffizienteste. Die stabilen Gegenbeispiele sind deshalb ein wissenschaftlicher Befund und kein Anlass, die geschlossene Messkampagne zu verändern.

Diese Auswertung wurde am 04.10.2026 nach Abschluss der Erhebung geplant und ausgeführt. Sie ist explorativ/post hoc und verwendet ausschließlich vorhandene Messungen. Keine Vorabplanung, unabhängige Hold-out-Prüfung oder kausale Hardwareisolation wird behauptet. Alle ursprünglichen Qualityentscheidungen und Claimgates bleiben erhalten. `DATEN_UND_KOHORTEN.md` definiert Populationen; `CLAIM_EVIDENCE_MATRIX.csv` bindet die vorgeschlagenen Aussagen an Tabellenzeilen. Die umfangreichen Detailbelege stehen in `RANKING_ANALYSE.md` und `ENERGY_ANALYSE.md`.

## A. Wann bringt Splitten gegenüber Full einen messbaren Vorteil?

Die Antwort unterscheidet sich deutlich zwischen Vendor Full und TensorRT Full. Von jeweils 204 deskriptiven Splitvergleichen sind **142 gegen Vendor Full gleichzeitig schneller und energieärmer**, gegenüber TensorRT Full **86**. Nach semantischer Bestätigung und reference_close auf **beiden** Seiten bleiben **80/140** bzw. **84/187**. Das Weglassen schlechter Fullbaselines verändert somit auch den Nenner wesentlich: Neun der 21 Vendor-Fulls haben accuracy_loss; keine der 21 TRT-Fulls hat diese Einstufung.

| Augmentierte technische Menge | Vendor Full | TensorRT Full |
|---|---:|---:|
| schneller im Energiezeitfenster | 182/204 | 93/204 |
| niedrigere J/task | 142/204 | 121/204 |
| beide Vorteile | 142/204 | 86/204 |
| weder schneller noch sparsamer | 22/204 | 76/204 |
| J/task-Quotient Split/Full: Min–Median–Max | 0,162–0,763–2,799 | 0,215–0,958–4,102 |

Diese Verteilungen beschreiben den vorliegenden ungleich besetzten Bestand: 17–20 Klassifikationspunkte pro Gruppe, drei YOLO-Punkte. Sie sind keine gleichgewichtete Schätzung für beliebige Modelle. Es gibt 42 einmal gemessene Fullbaselines; die 408 wiederverwendenden Paarvergleiche sind abhängig. Die getrennten Präzisionsangaben für Splitboundary und Fullausführung bleiben sichtbar. Belege: `energy_sensitivity.csv`, `energy_group_distributions.csv`, `energy_full_baselines.csv`; exakte Population `view=augmented,attestor_gap=included`.

**Negativer Vergleich trotz gültiger Qualität:** ResNet/DeepX b023 (`BASE-PAIR-081`) erreicht 144,955 Task/s bei 0,134801 J/task; Vendor Full 321,571 Task/s bei 0,048157 J/task. Der Split verbraucht 2,799-mal so viel Energie pro Abschluss. Beide sind reference_close und semantisch vergleichbar. Keiner der 19 ResNet/DeepX-Splits spart gegenüber Vendor Full Energie. Das ist kein technischer Fehler, sondern ein negativer Nutzenbefund.

**Positiver Vergleich mit enger Geltung:** YOLOv7/H8 b066 erreicht im aktuellen Energiezeitfenster 110,674 Task/s und 0,324744 J/task, TRT Full 13,363 Task/s und 1,510593 J/task: 8,282-mal Durchsatz bei 0,215-mal J/task. Das ist der heutige gebundene Prepared-Input-/Dreistufenpfad; keine Gleichsetzung mit historischer Paperengine oder anders begrenzten 97-FPS-Werten. Ohne b066 bleiben 85/203 TRT-Paare mit beiden Vorteilen statt 86/204; die maximale Ratio sinkt auf 5,057, der Median der Energiequotienten kaum. Extremwert und mittiger Bestand reagieren verschieden.

Alle 16 Semantikgrenzen sind in `energy_semantic_limits.csv` einzeln benannt. Fehlender Decoder-/NMS-Beleg ist nicht dasselbe wie ein gespeicherter numerischer Negativbefund. 392/408 besitzen lokale semantische Bestätigung; darüber hinaus wird keine wissenschaftliche Claimfreigabe erzeugt.

## B. Kann Generic den besten Native-Split auswählen?

Auf den 204 technisch gepaarten Fällen trifft Generic-Top1 den Native-Besten in **10/21** Gruppen: **3/9** Klassifikations- und **7/12** YOLO-Gruppen. Dies ist eine Trefferzählung in Developmentkandidaten, keine gehaltene Testgenauigkeit. Rangkorrelationen werden ausschließlich innerhalb der exakten Gruppen berechnet. Die neun Klassifikationsgruppen reichen von Spearman −0,456 bis 0,995.

Die Definitionen haben unterschiedliche Nenner: `S=R_native/R_generic` vergleicht denselben Fall; `L_R=1−R_native,selected/R_native,best` ist verlorener Durchsatz; `L_C=R_native,best/R_native,selected−1` ist Cycle-/Kapazitätsregret. Keiner dieser Werte ist eine gemessene Einzelanfragelatenz.

| Gruppe | n | Spearman rho | L_R | L_C | L_R über neun Replikatkombinationen |
|---|---:|---:|---:|---:|---:|
| RegNet/H10 | 20 | −0,456 | 70,61 % | 240,23 % | 70,22–74,67 % |
| ResNet/H10 | 19 | 0,489 | 52,15 % | 108,98 % | 49,76–53,52 % |
| YOLOv7/H8 | 3 | 0,500 | 52,96 % | 112,59 % | 52,92–53,11 % |
| MobileNet/H8 | 17 | 0,995 | 0 % | 0 % | Top1 trifft in 9/9 Kombinationen |

Alle drei großen Fehlentscheidungen bleiben in 9/9 Kombinationen bestehen. Die Streuung ist daher keine ausreichende Erklärung dieser Rangprobleme. Andere kleine Fehler sind dagegen instabil: MobileNet/DeepX hat nur 1,24 % medianbasierten L_R und wechselnde Gewinner. Die Tabellen enthalten alle Gruppen, auch n<3 nach Filtern, Ties, Kendall tau-b und Konkordanz. Feste Reihenfolge entspricht dem ursprünglichen Rangcode; Tie-Sensitivitäten sind zusätzlich explizit.

Für die neun Klassifikationsgruppen mit n≥4 enthalten Top2-/Top3-Shortlists den Native-Besten in **5/9** bzw. **6/9** Gruppen. Die exakte Erwartung einer gleichverteilten zufälligen Auswahl ohne Zurücklegen beträgt über dieselben neun Mengen 0,969 bzw. 1,453 Treffer; das ist eine kombinatorische Rechnung, keine neue Random-Messung. Dennoch sind RegNet/H10 und MobileNet/H10 Gegenbeispiele zur generell nützlichen Shortlist. RegNet/H10 Top3 verliert weiterhin 68,58 % Durchsatz, gegenüber 38,96 % erwarteter Verlust einer zufälligen Dreierliste mit anschließender Native-Orakelauswahl. Top3 bei n=3 wird überhaupt nicht als Leistung gezählt.

Die strengere reference_close-Transfermenge enthält **184 Fälle**, nicht 201: 201 erlaubt auch technisch gültige Accuracyverluste. Drei zusätzliche Fälle sind trotz reference_close vom Transfer ausgeschlossen. Dann verbleiben 18 Gruppen mit n≥3 und acht Top1-Treffern; die übrigen drei Gruppen mit n=2 werden nicht unsichtbar ersetzt. Ohne die drei prominenten Gegenbeispiele bleibt ein maximaler technischer Gruppenverlust von 31,86 % (MobileNet/H10). Somit ist die Einschränkung nicht allein ein einzelner Ausreißer. Belege: `rank_groups.csv`, `rank_shortlists.csv`, `rank_repeat_sensitivity.csv`, `rank_dominant_case_sensitivity.csv`.

## C. Was verändert Task-Completion gegenüber dem historischen Rohoutputproxy?

Exakt 192 ursprüngliche Identitäten lassen sich unter der dokumentierten Rawmetadatengrenze paaren. In den neun Klassifikationsgruppen steigt rho in sechs, bleibt in zwei gleich und sinkt in einer. Top1-Durchsatzverlust verbessert sich jedoch nur in drei Gruppen, verschlechtert sich in zwei und bleibt in vier unverändert. Die sauberere Messgrenze garantiert daher keine bessere Auswahl.

RegNet/H8 verbessert sich auf denselben 20 Punkten von rho 0,392 auf 0,941 und von **41,43 % auf 8,03 % L_R**. Umgekehrt verschlechtert sich ResNet/H8 von **1,90 % auf 13,92 % L_R**, obwohl rho von 0,761 auf 0,854 steigt. MobileNet/H10 bleibt bei 31,86 % Verlust, RegNet/H10 bei 70,61 %. Rangübereinstimmung über alle Kandidaten und Qualität der einen ausgewählten Spitze sind verschiedene Fragen.

Der Rawproxy endet an Logits/P2-Ausgabe; neue Generic-Completion und Native schließen die Task ab. Messdatum, Threadbedingungen, Thermik und Runtime sind nicht kontrolliert gleich. Deshalb sind die Unterschiede mit Task-Completion vereinbar, aber nicht vollständig kausal durch zusätzliche Nachverarbeitung erklärt. Es wird keine Ersatzmessung `raw_time + geschätztes postprocessing` erzeugt. Die zwölf kurzen Zusatzvorläufe zählen weder zur historischen 499er-Raw-Splitkohorte noch zu den 192 Common-Identitäten. Beleg: `rank_proxy_comparison.csv`, technische Zeilen, und `rank_raw_join_audit.csv`.

## D. Energie, praktische Auswahl und Robustheit

**17/21** Gruppen haben denselben Split mit höchstem energiebezogenen Durchsatz und geringsten J/task. Zwei stabile ResNet-Gegenfälle sind praktisch aussagekräftiger als eine pauschale Regel: In ResNet/DeepX kostet der schnellste b002 **26,10 %** mehr J/task als b119; b119 verliert **24,57 %** Fensterdurchsatz. In ResNet/H8 kostet der schnellste b031 **12,84 %** mehr J/task als b060; der Energiegewinner verliert nur **1,79 %** Durchsatz. Beide Gruppen behalten ihre jeweiligen Gewinner in allen drei Replikaten mit getrennten beobachteten Bereichen. Eine universelle Deploymentschwelle folgt daraus nicht.

MobileNet/DeepX liefert einen Gegenbefund kleiner Effektgröße: 0,172 % Energieaufschlag bei 18,06 % Durchsatzunterschied, wechselnde Replikatgewinner und überlappende Bereiche. YOLO26m/DeepX hat ebenfalls sehr kleine Abstände (0,467 % Energie, 0,711 % Durchsatz). Drei Wiederholungen liefern hier begrenzte Auflösung.

Die primäre Aggregation ist das Mittel der drei replikatweisen E/N-Quotienten. Eine gepoolte Ratio weicht maximal 0,491 % ab, ändert aber keinen der 21 Energiegewinner und kein Vorzeichen der Energie-Paarvorteile. Dasselbe gilt für die geprüfte Medianauswahl. 136/142 Vendor- und 86/86 TRT-Paare mit beiden mittleren Vorteilen behalten beide Vorzeichen über sämtliche neun Replikatkombinationen.

Algebraisch gilt pro Replikat `J/task=P/R_E`. Getrennte Fallmittel erfüllen diese Identität nicht exakt (maximal 0,490 % relative Abweichung). Eine inverse Energie-/Durchsatzkorrelation wäre folglich kein unabhängiger Hardwarebefund. Leistung und Durchsatz werden separat ausgewiesen; beispielsweise schwankt ResNet/DeepX in diesem Bestand um Faktoren 1,672 bzw. 3,033. Primär ist kalibrierte ungekürzte **Full-System-Energie**, keine reine Beschleunigerenergie. Generic-Energie wurde nicht gemessen. Die 21 vorhandenen Hostnormalisierungen bleiben sekundär: Gegen diese Referenzen sind 80/204 TRT-Vergleiche energiesparend statt 121/204 primär.

Eine reproduzierbare Darstellungsreparatur wurde additiv durchgeführt: 192 ursprüngliche Basis-TRT-Zeilen enthielten im allgemein benannten Full-Energiefeld sekundäre Hostnormalisierung; der ursprüngliche deskriptive Quotient war bereits korrekt gegen Roh-FS-Energie. `energy_legacy_field_audit.csv` belegt jede Zeile. Beispiel BASE-PAIR-002: neues durchgängig rohes Fullfeld 0,02738276288 statt altem normalisierten Feld 0,02415942036 J/task; Primärquotient 1,61857796, sekundär 1,83452814. Kein Original verändert.

Ohne die 21 Fullreferenzen mit historischer Attestorquellenlücke bleibt die gesamte TRT-Vergleichsmenge leer. Ein „robuster TRT-Effekt nach Ausschluss“ wäre damit unbelegt. Die Vendorvergleiche und Split-Ranganalysen bleiben davon unberührt. Diese Lücke ist Provenienz, kein erfundener Messfehler.

## E. Quality, technische Realisierbarkeit und Graphposition

Von **39 Accuracyverlusten** gehören **22 zu Top1** (alle MobileNet), **17 zu AP50:95** (YOLO11l:1, YOLO26m:5, YOLO26s:7, YOLOv7:4). Sämtliche 39 liegen in der ursprünglichen Basis, kein Zusatzfall wurde zum positiven Abschluss umetikettiert. Alle 560 Qualityauswertungen sind technisch gültig. Der Punktverlust wird nach der bereits bestehenden 5%-Relative-Loss-Reportingpolicy klassifiziert; die separat gespeicherte absolute Taskmargin 0,01 bleibt dokumentiert.

Die 22 Top1-Verluste liegen bei −15,26 bis −3,72 Prozentpunkten, die 17 AP50:95-Verluste bei −7,761 bis −2,169 Prozentpunkten. Der stärkste Klassifikationsfall ist MobileNet/H10 b119 (`base_quality_038`), 20,71 % relativer Verlust; der stärkste Detektionsfall der YOLO26s/H8-Vendor-Full-Companion mit gespeicherter ID b003 (`base_quality_425`), 19,36 % relativer Verlust. Originalbootstrapintervalle stützen 32 der 39 Loss-Einstufungen; sieben sind grenznah. Insgesamt sind 543/560 Einstufungen unterstützt und 17 grenznah, davon zehn auf der reference_close-Seite. Grenznähe ändert die Originalentscheidung nicht. Positive kleine Abweichungen existieren ebenfalls: maximale Top1-Zunahme +0,44 pp, AP50:95 +0,0534 pp. Metriken werden nicht gepoolt.

Die vollständige Rollenbilanz lautet **39 = 9 Vendor-Full-Verluste + 17 technisch paarbare Splitverluste + 13 Native-unsupported-Splitverluste**. Alle 13 außerhalb der Completed-Paarmenge liegenden Splitverluste sind wegen `part2_input_count_not_one` terminal. Eine gespeicherte Boundary-ID ist kein eindeutiger Qualityschlüssel: YOLO11l/H8 b003 bezeichnet sowohl den Vendor-Full-Companion (`base_quality_294`, 5,424 % Verlust) als auch den Split (`base_quality_295`, 1,993 % Verlust). Variante und Backend trennen diese Resultate; der vollständige exakte Splitjoin bestätigt die bestehenden Pairflags für alle 204 Fälle. `quality_pair_join_audit.csv` dokumentiert diesen Abgleich.

Technisch fehlende Ausführung ist davon getrennt: 37 negative Builds und 24 Policyausschlüsse erklären den Genericbestand; **alle 228 Native-unsupported-Fälle haben `part2_input_count_not_one`**. Der Nativebestand ist daher strukturell auf unterstützte Schnittstellen selektiert. Single-Tensor-Unterstützung und postgeplante YOLO-Erweiterung erlauben keine zufällige Missingnessannahme.

Die gespeicherten Graphberichte enthalten 2.111 Kandidaten mit topologischer Position, Boundarybytes, Tensoranzahl und analytischen Stageproxies. Alle 204 Completed-Fälle und 511 Quality-Splits lassen sich verknüpfen. Die neue Ableitung rechnet nur mit diesen vorhandenen Zahlen. Normierte Position `(boundary+1)/node_count` bezeichnet Topologie; separat gespeicherte FLOPsanteile sind analytische Schätzungen, keine Zeitanteile. Konstante Features erhalten unbekannte statt künstlich null gesetzter Korrelationen.

Die Zusammenhänge sind nicht universell: Bei RegNet/H10 korreliert der gespeicherte Stage1-FLOPsanteil mit Native-FPS mit **rho 0,995**, mit Generic-FPS mit **−0,453**. MobileNet/H8 hat für denselben Featuretyp Native-rho **−0,966**. Boundarybytes gegen Native-FPS reichen in den neun Klassifikationsgruppen von **−0,902 (RegNet/H10) bis +0,661 (MobileNet/H8)**. „Kleinere Schnittgröße ist immer schneller“ ist damit durch diese Gruppe von Beobachtungen nicht gestützt. Das gespeicherte modellübergreifend benannte Kalibrierprofil einer Prognose bleibt eine weitere Einschränkung; die Prognose wird nicht durch ihr Vorhandensein validiert. Alle Qualitäts- und Performancekorrelationen sind stratifiziert in `graph_associations.csv`; keine p-Wert-Auswahl und kein nachträgliches Training.

## F. Auffällige Fälle und alternative Erklärungen

Neun gezielte private Fallbelege wurden zu `inputs/ranking_path_evidence.csv` reduziert. Sie bestätigen bei den untersuchten Gegenfällen die vorbereitete Inputidentität, gebundene Engines und 1000 Abschlüsse pro Wiederholung. Damit sind einfache Count-/Inputverwechslungen keine gefundene Erklärung der großen Rangumkehr.

H10 verwendet im Nativepfad asynchrone Ausführung mit inflight8/queue3; Generic besitzt einen materialisierten Zwei-Worker-Pfad mit queue2. Bei YOLOv7/H8 steht b044 für Python-FIFO, b066 für den aktuellen C++-Dreistufenpfad mit postqueue4. Diese Unterschiede sind plausible Mechanismen, keine isolierten Ursachen. Generic als Ganzes wird nicht fälschlich „seriell“ genannt. Host-/Thermik-/Thread-/Zeitgleichheit ist nicht nachgewiesen. Die vorhandenen Telemetriebelege stützen keinen vollständigen kausalen Ausschluss alternativer Effekte.

Die sinnvolle Paperaussage ist deshalb enger und belastbarer: **Messendpunkt, Ausführungspfad, Vergleichsbaseline und Qualityfilter müssen bei der Auswahl gemeinsam betrachtet werden.** Positive Fälle, stabile große Fehlentscheidungen und kleine nicht aufgelöste Unterschiede gehören zusammen in die Darstellung. Ein globales `not_claim_ready` ersetzt diese Interpretation nicht; die Interpretation ersetzt umgekehrt keinen fehlenden Claim-Gate.

## Softwareprüfung und wissenschaftliche Reichweite

Die neuen Ableitungen besitzen Tests für Quotientenrichtung, unterschiedliche Regretnenner, doppelte Joins/Baselines, exakte zufällige Shortlisterwartung, Filtertransparenz, konstante Features, unveränderte Qualitysummen und deterministische Reproduktion. Die endgültigen tatsächlichen Testzahlen und Reproduktionsdateien stehen in `VALIDIERUNG.md` und `validation.json`. Originale bleiben als unveränderte kompakte Inputs erhalten.

Keine erneute 396er-Toolabnahme, Hardwareabnahme, Normal-GUI-Messung, Inferenz, Kompilierung, Energieaufnahme oder Qualitykampagne wurde ausgeführt. Drei Timing-/Energiereplikate bleiben drei Experimente; bestehende 60-s-Screenings werden nicht zu langen Finalmessungen. Die historische Quellensuche und laufende Archivierung sind separate Abschlussachsen, siehe `STATUS.md` und `HISTORISCHE_QUELLE.md`.
