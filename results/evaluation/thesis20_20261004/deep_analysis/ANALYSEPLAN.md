# Post-hoc-Analyseplan THESIS20

Erstellt am 2026-10-04T21:28:26.079980+02:00, vor den neuen Detailrechnungen. Explorative Planung nach Abschluss der Messkampagne; keine Präregistrierung und keine Hold-out-Auswahl. Bestehende Messwerte, Margen, Quality-/Claimgates und Auswahlrollen bleiben erhalten.

A. Alle Split-/Full-Vergleiche getrennt nach Vendor Full und TensorRT Full: absolute Werte, Quotientenrichtung Split/Full, Verteilung, schlechtester Fall, 408 deskriptive und semantisch belegte Teilmenge. 42 wiederverwendete Fulls zählen einmal; 16 Semantikgrenzen bleiben einzeln sichtbar. Sensitivität ohne die 21 TRT-Fulls mit historischem Attestorquellengap.

B. Generic als Native-Selektor innerhalb exakter Modell-/Setup-/Precision-/Task-/Endpunktgruppen. S=R_native/R_generic; L_R=1-R_selected/R_best und L_C=R_best/R_selected-1 getrennt. Spearman, Kendall tau-b, Konkordanz, Top1 und nichttriviale Shortlists; feste Identitätstieordnung. Neun Kombinationen dreier Generic-/Native-Replikate beschreiben Stabilität, keine neun unabhängigen Experimente oder CIs.

C. Historischer Rohoutputproxy und neue Completion auf denselben ursprünglichen Identitäten. Base/YOLO-Zusatz getrennt; keine Aufnahme kurzer Zusatzvorläufe in die 499er-Rohkohorte. Zeit, Runtime, Threads und Thermik sind nicht kausal kontrolliert.

D. Kalibrierte Full-System-Energie ohne Idleabzug: je Replikat E/N, E/T, N/T; Mittel der Einzelratios primär, gepoolte Ratio nur Sensitivität. Pareto und Auswahlstabilität innerhalb kompatibler Gruppen, Qualityverluste sichtbar. Algebraische Kopplung E/N=(E/T)/(N/T), keine unabhängige Kausalbestätigung durch inverse Korrelation.

E. Quality: Top1 und AP50:95 separat; absolute Prozentpunkte, relative Änderung, unveränderte Bootstrapintervalle und ursprüngliche Margen. Alle 39 Accuracyverluste auswerten. Gemessen/Buildfehler/Policy/unsupported je Scope getrennt. Vorhandene Graphfeatures gezielt aus kompakten Berichten prüfen, ohne ONNX-Export; fehlende Werte unbekannt lassen.

F. Konkrete positive, negative und Null-Gegenfälle: Counts/Fenster/Codepfade prüfen; Beobachtung und Erklärungshypothese auseinanderhalten. Kein neuer Messauftrag.

Primäre Kohorten: augmentierte technische 204 Paare; ursprüngliche 192; Qualitytransfer 201; reference_close mit und ohne gesonderte Transferzulässigkeit explizit bezeichnen. Sensitivität: Base/Augmentation, Qualityfilter, empirisch dominante Fälle, Median/Replikate, exakte Ties. Keine p-Wert-Suche und keine neuen Freigabeflags.

Lieferung: additive Scripts/Tabellen, höchstens sechs Hauptfiguren mit englischen Captions und PDF/SVG/Source-CSV, vollständiges Supplement, deutsche Interpretation, Claims mit Belegschlüsseln, fokussierte Ableitungstests und deterministische Reproduktion. Keine Inferenz, Messung, Kompilierung oder Wiederholung der Toolabnahme.
