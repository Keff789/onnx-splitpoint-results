# Tatsächliche Validierung — 05.10.2026

**21 Tests bestanden in 4,63 s, keine übersprungen, keine fehlgeschlagen.**
Sieben Methoden-/Projektionsprüfungen und 14 Auswertungsprüfungen. Der vollständige
Offlineeinstieg reproduzierte alle Scores, Gruppenmetriken, Sensitivitäten und
beide Abbildungen in einem separaten Ausgabebaum: **27/27 Dateien bytegleich**
mit der gelieferten Ableitung. Beide Prozesse endeten mit Exitcode 0.

Die 27 Dateien umfassen zwei Score-/Verfügbarkeitsprojektionen, Fall-/Gruppen- und
Sensitivitätstabellen, globale Empfehlungen, Verifikations-/Ergebnis-JSON,
Figurequellen, vier PDF/SVG-Vektoren, zwei PNGs und Captions/Figureindex.
`validation.json` nennt die tatsächlich verglichenen Dateien. Die vier übernommenen
reinen Definitionen wurden bytegleich gegen den unveränderten Toolcommit v2.92.0
geprüft; ihre bereits dokumentierten SHAs stimmen.

Der Testumfang prüft insbesondere:

- Originalgewichte und Normierung über das vollständige Graphuniversum; 2.111
  historische Fit-/Fallback-/Bottleneck-/Streamwerte werden mit den vorhandenen
  Definitionen numerisch reproduziert (je nach Feld bis 1e-12 Toleranz).
- Richtung und Bytes/MB/MiB, exakte Identitätsjoins und keine Rückumrechnung in
  vermeintlich gemessenen Runtimeverkehr.
- Fehlendes Native-Handover trotz vorhandener generischer Felder; fehlende
  SystemSpec bleibt fehlend. Keine neue Parameteranpassung.
- Unveränderte 204/201/184-Kohorten, 192 Original-Raw-Identitäten und
  Generic-Completion-Regression 10/21; gleiche vollständige Vergleichsmengen.
- Ursprüngliche Tieordnung, Durchsatz-/Cycle-/Energienenner, Top-k-Tiegrenzen,
  analytische Zufallsauswahl gegen vollständige kleine Teilmengen und sichtbare
  Gruppen unter n=3. Globale Empfehlung ohne Nachrücken.

Beide Hauptfiguren wurden visuell geprüft. Bei der Energiegrafik wurden die
Fallbeschriftungen in die Zeichenfläche gelegt; ResNet/H8 b060 ist explizit als
Energieminimum bezeichnet. Caption und Quelltabelle trennen Performance-FPS und
Durchsatz aus dem eigenen Energiefenster. Der RegNet/H10-Cut-Verlust beträgt
22,751903… %; die Ergebnisprosa rundet korrekt auf 22,75 %.

Aus dem Methodenverzeichnis im Ergebnischeckout:

```bash
THESIS20_SOURCE_ROOT="$(cd .. && pwd)" PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider --basetemp /tmp/thesis20-methods-tests tests
PYTHONDONTWRITEBYTECODE=1 python scripts/reproduce_methods.py --source-root .. --output-root /tmp/thesis20-methods-reproduced
```

Frische Ausgabeziele wählen. Der tatsächliche Controllerlauf verwendete die
vorhandene Python-3.12-/NumPy-1.26.4-/Matplotlib-3.5.2-Umgebung und getrennte
Reportverzeichnisse. Tests, Matplotlibkonfiguration und Reproduktion schrieben
nichts in den Toolquellbaum oder eine laufende/eingefrorene Archivquelle.

Vor Übernahme der **bereits geprüften alten Vertiefung** wurden separat deren
31 vorhandene Tests wiederholt (31 bestanden in 1,18 s) und 71/71 alte Outputs
bytegleich reproduziert. Diese Prüfung ist kein weiterer neuer Methoden-Testfall.

Nicht ausgeführt: Toolvollsuite, reale Normal-GUI-/Hardwareabnahme, Inferenz,
Kompilierung, Kalibrierung, neue Quality-/Bootstrap- oder Energie-/Benchmarkkampagne.
Diese Schritte sind vom Auftrag ausgeschlossen. Software-PASS ist keine neue
Hardwarefreigabe, kein Hold-out-/Kausalnachweis und keine Roharchivabnahme.

Zusätzliche Lieferprüfung direkt aus dem kuratierten Ergebnischeckout, mit dem
relativen Standard-Quellpfad: erneut 27/27 Reproduktionsdateien bytegleich.
13 relative Dokumentlinks zeigen auf vorhandene Ziele. Der vorhandene kompakte
Privacy-/Größencheck meldet 0 fatale Befunde und 0 Reviewbefunde.

`git diff --cached --check` für neue Analyse-/Test-/Dokumentdateien besteht.
Der ungefilterte Check meldet 197 vom Renderer erzeugte SVG-Endräume und zwei
unverändert übernommene abschließende Leerzeilen in `system_model.py`/`units.py`.
Diese geprüften Formatbefunde bleiben erhalten, damit die Definitionskopien
bytegleich sind; kein ungefilterter Whitespace-PASS wird behauptet.
