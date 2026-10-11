# Werkzeuge für Ablage und Reproduktion

## Katalog aktualisieren

Vom Repositorywurzelverzeichnis:

```bash
python3 energy-measurement/tools/catalog.py --repo .
```

Der Katalog liest Dateinamen und CSV-Kopfzeilen. Er erzeugt keine Messwerte oder neuen Plots. Keine Zusatzbibliotheken erforderlich.

## Erhaltung prüfen

```bash
python3 energy-measurement/tools/verify_layout.py --repo .
```

Prüft jede Datei des Ausgangs-Gitbaums am registrierten neuen Pfad gegen ihren vorhandenen Git-Blob. Auch vorherige Navigationstexte und die ursprüngliche Workflowdatei sind erhalten. Der unveränderte PARMA-Paperbaum wird vollständig verglichen.

## Eingefrorene Prüfer ausführen

```bash
python3 energy-measurement/tools/check_frozen.py --repo .
```

Dieser Lauf rekonstruiert das ursprüngliche Verzeichnislayout aus dem bereits lokalen Basiscommit ausschließlich in einem temporären Verzeichnis. Dort laufen die alten Prüfskripte mit ihren Originalpfaden. Das vermeidet Veränderungen an eingefrorenen Skripten/Manifesten. Keine Rohdaten-/Collector-Aufrufe, keine automatischen Installationen. Das TIM-Prüfskript läuft ebenfalls nur in einer temporären Kopie.

Paper-Builds bleiben an ihren bisherigen Paketaufrufen: `bash build.sh` in `papers/parma-v0.15.1/manuscript/` beziehungsweise `papers/tim-v0.3/`. Für die vollständige TIM-Ergebnisregeneration gilt weiterhin dessen README; sie ist für einen Ablageumbau nicht nötig.

Alte URLs auf einen festen Git-Commit/Tag bleiben unverändert. Alte direkte `main`-Pfade zu verschobenen Dateien werden nicht als weiter funktionsfähig behauptet: `path-map.csv` ordnet sie zu; der alte CURRENT-KB-Dateiname bleibt als Wegweiser erhalten. Neue Kataloge und angepasste aktive Navigationslinks verwenden die neuen Pfade.

Der Figure-5-Veröffentlichungsworkflow bleibt nach dem Umbau absichtlich **manuell auslösbar**, damit eine reine Pfadänderung keinen Release und keine Tagänderung auslöst.
