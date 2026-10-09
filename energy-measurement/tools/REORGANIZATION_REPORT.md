# Umbauprüfung

Ausgangscommit: `85eb488587a51659239c45d966f930f7c7b72a6e`. Migrationswerkzeug v1.0.0.

- 2994 vorherige Repositorydateien am registrierten Ziel bytegenau und mit gleichem Modus erhalten.
- 573 bisherige Dateien haben einen neuen Erhaltungs-/Ablagepfad.
- PARMA-Paket unverändert; 210 Dateien aus dem bereitgestellten TIM-v0.3-Paket hinzugefügt.
- 551 Bild-/Tabellendateien im Katalog; 814 lokale Links in den neuen Einstiegen geprüft.
- 1 aktive Navigations-/Workflowdateien angepasst; ihre vorherigen Inhalte separat erhalten.
- Keine Rohdatenintegration, keine neue Messung, keine Umdeutung numerischer Ergebnisse.
- Keine Tags umgehängt. Kein Release-/DOI-Schritt.

Die Datei- und Linkprüfung ist eine Ablageprüfung, kein neuer wissenschaftlicher Validierungsclaim. Historische interne Dokumentationslinks sind im ursprünglichen Commit lesbar. Alte pfadabhängige Prüfer laufen über `check_frozen.py` in einem temporären Originallayout.
