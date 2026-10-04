# Figureplan und Review

Alle sechs Hauptfiguren sind tatsächlich als PDF/SVG und PNG-Vorschau erzeugt; `figure_index.json` und `CAPTIONS.md` enthalten die englischen Captions und die exakten Source-CSVs. Standardbreite 7,2 Zoll für zweispaltige Darstellung, Schriften 7–9 pt; Diagramme 2/5/6 können bei einspaltiger Verwendung als einzelne Panels gesetzt werden, statt die gesamte Schrift zu halbieren. DejaVu Sans, weißer Hintergrund, dezentes Raster und H8/H10/DeepX Blau/Orange/Grün folgen dem vorhandenen PSD-/THESIS20-Stil. Setupmarker sind zusätzlich Kreis/Quadrat/Dreieck; keine PSD-Messwerte übernommen.

1. `fig01_coverage_matrix`: gesamte Modell-/Setupabdeckung, unterschiedliche Nenner lesbar; Basis/Zusatz separat.
2. `fig02_split_full_benefit`: alle Split/Full-Energie- und Durchsatzquotienten, getrennte Fulltypen, Quality-/Semantikmarker. Die algebraische Kopplung wird im Text erklärt.
3. `fig03_selection_and_stability`: alle 21 Ranggruppen, L_R und neun Replikatkombinationen. L_C separat in Tabelle, damit Nenner nicht vermischt werden.
4. `fig04_yolo_fixed_candidates`: alle zwölf Gruppen mit drei festen Grenzen, beide Runner, beobachtete Min/Max, Zusatzmarker. Keine geglätteten Kurven.
5. `fig05_energy_choices`: stabiler großer Trade-off, gleicher Gewinner und instabile kleine Differenz nebeneinander. Alle anderen Gruppen im Supplement.
6. `fig06_regnet_counterexample`: analytischer Stageanteil und tatsächliche Runner-Rangumkehr; Beschreibung von Codepfaden bleibt ausdrücklich Erklärungshypothese.

Supplement: alle 39 Qualityverluste mit vorhandenen Intervallen (`supp01`), Raw/Completion auf gemeinsamen ursprünglichen Kandidaten (`supp02`), sämtliche 21 Energiegruppen mit Fulls (`supp03`). Vollständige Zahlen-/Filter-/Replikattabellen begleiten alle Figuren. Keine Mainaussage beruht ausschließlich auf einer ausgewählten spektakulären Gruppe.

## Bewertung der fünf bisherigen Figuren

Alle fünf bisherigen PNGs, Erzeugungsscript und Figureindex wurden gelesen/visuell geprüft. Sie bleiben unverändert im veröffentlichten Ausgangsrelease.

| Bisherige Figur | Stärken | Grund der neuen Ergänzung |
|---|---|---|
| fig01 coverage | korrekte getrennte Bestandszählung | aggregiert Setups je Modell; neue Matrix legt Gruppen und Zusatznenner offen |
| fig02 completed ratio | Quotient Native/Generic klar, Zusatzmarker | Quotient allein beantwortet weder Full-Nutzen noch Auswahlverlust |
| fig03 YOLO rank transfer | kleine Stichproben und triviales Top3 korrekt | neue Darstellung ergänzt tatsächliche Raten und Replikatstabilität, nicht nur rho |
| fig04 energy tradeoffs | saubere Gruppenfacetten, E-Fenster-FPS | neue Analyse ergänzt Fullreferenzen, konkrete Gewinner und Filter-/Replikatsensitivität |
| fig05 quality/variability | CV und negative Quality erhalten | gemeinsame Quality-X-Achse beantwortet nicht Top1/AP-spezifische Änderungen; neuer Supplementforest zeigt originale Intervalle und Prozentpunkte |

Visuelle Prüfung: Achsenrichtung, Einheiten, Nenner, additive Marker, Min/Max-vs-CI und Layout geprüft. Unabhängiger Review entdeckte fehlende Qualitykennzeichnung der Fullmarker sowie eine unvollständige Aufzählung semantisch begrenzter Modelle im Supplement; beide wurden korrigiert. Ein zusätzlicher exakter Qualityjoin bestätigte alle 204 Paare; im Qualityforest werden Full-Companions ausdrücklich als Full beschriftet. SVG-Schrift bleibt editierbar; PDF bettet TrueType ein. Endgültige Satzbreite und Publisherfonts sind Aufgabe des Paperlayouts, kein wissenschaftliches Freigabeflag.
