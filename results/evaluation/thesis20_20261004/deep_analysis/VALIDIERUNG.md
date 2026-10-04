# Tatsächliche Validierung der neuen Ableitung

Abgeschlossen 2026-10-04T21:53:18.703512+02:00. **31 Tests PASS, 0 übersprungen, 0 fehlgeschlagen im finalen Lauf** (`pytest-final.log`, 1,10 s). 13 Energietests, 11 Rangtests einschließlich des Äquivalenzabgleichs sämtlicher 126 ursprünglicher Gruppen, sieben Quality-/Graph-/Kohortentests. Zusätzlich 10 lokale Archiv-Epoch-/Linkprüfungen und acht Prüfungen des ausschließlich wartenden kleinen Folgekopiewegs (keine Hardwaretests).

Zwei vollständige neue Ableitungen mit denselben kompakten Eingaben in getrennte lokale Ausgabebäume lieferten **71/71 bytegleiche Dateien**: abgeleitete CSVs, PDF/SVG/PNG, Ergebniszusammenfassungen, Figureindex und Captions. Tatsächliche Endcodes: pytest=0, primäre Reproduktion=0, getrennte Reproduktion=0, Gesamtabnahme=0. Der dauerhafte Analyseprozess in `thesis20-deep-analysis-20261004` ist beendet. `validation.json` enthält die Maschinenzusammenfassung.

Befehle im kuratierten Paket:

```bash
THESIS20_SOURCE_ROOT="$PWD/source" PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider tests
PYTHONDONTWRITEBYTECODE=1 python scripts/reproduce.py
PYTHONDONTWRITEBYTECODE=1 python scripts/reproduce.py --output-root /tmp/thesis20-deep-reproduction
```

Für den tatsächlichen Controllerlauf wurden temporäre Test-/Matplotlib-/Reproduktionsausgaben ausschließlich unter dem separaten Analysebereich gehalten. Kein neuer Output entstand im Toolquellbaum. Historische Produktreader/-rangfunktionen bleiben unverändert; zusätzliche private Quellenprojektion benötigte nur gespeicherte kleine JSON/CSV-Berichte.

Ein erster Pakettest ergab 29 PASS/1 FAIL wegen einer nicht mitkopierten alten Pareto-Referenztabelle, nicht wegen eines veränderten Rechenergebnisses. Die unveränderte Tabelle wurde in `source/tables/within_stratum_pareto.csv` ergänzt; der vollständige finale Lauf besteht. Fehlversuch und Endcodes bleiben privat erhalten.

Visuell geprüft: alle fünf alten Figuren, alle sechs neuen Hauptfiguren und drei Supplements. Korrigiert wurden Full-Qualitymarker, vollständige Semantiklimits in Caption, Platz für YOLO-Replikatbereiche und die beiden beschrifteten RegNet-Auswahlfälle. Unabhängige Reviewprüfungen bestätigen ursprüngliche 5%-Reportingpolicy, alle 2.111 topologischen Positionen und Primärenergie aus E/N.

**Nicht ausgeführt:** Tool-Vollsuite/396er-Abnahme, reale Normal-GUI-Abnahme, Hardware-Smoke, Inferenz, neue Quality-/Bootstrapkampagne, Compiler/Enginebuild, Energieaufnahme. Der Auftrag schließt diese Schritte aus; Software-PASS ist keine Hardwarefreigabe. Bestehende Quality-CIs wurden nur gelesen. Keine kontrollierte Runtime-/Thread-/Thermikgleichheit nachträglich hergestellt.

Die Archivtests prüfen lokale Logik und gezielte Dateifälle. Sie ersetzen keinen noch laufenden gesamten Archivzielabgleich und keinen vollständigen Inhaltsnachweis des Roharchivs.


Zusätzliche Lieferprüfung direkt aus dem tatsächlich kuratierten Ergebnischeckout:
31 identische Tests erneut bestanden (keine neuen unabhängigen Testfälle gezählt),
71/71 Outputs in einem weiteren separaten Ausgabeordner bytegleich.

`git diff --cached --check` für neue Scripts/Tests und Ergebnisdokumentation: PASS.
Der ungefilterte Check meldet erwartete Formatbefunde: 4.330 SVG-Zeilen mit vom
Renderer erzeugtem Endraum, 12.331 CSV-Zeilen mit CRLF sowie eine unverändert
übernommene abschließende Leerzeile im ursprünglichen Rangmodul. Diese sind geprüft
und erhalten; kein pauschaler whitespace-PASS wird behauptet. Originale kompakte
Eingaben und Rangfunktionen wurden dafür nicht normalisiert. Alle 23 Dateien des
übernommenen Original-Inputmanifests stimmen mit ihren bestehenden SHAs überein.
