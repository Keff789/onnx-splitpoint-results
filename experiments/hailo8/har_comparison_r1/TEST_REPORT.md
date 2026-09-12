# Prüfbericht – Hailo8 HAR-Vergleich und Git R1

## Ausgeführt

**37 Offlineprüfungen bestanden, ohne Fehler oder Skips in der dokumentierten Auditumgebung.**

Der genaue finale Testumfang und seine Laufzeit stehen in `verification/offline_tests.log`
und `verification/offline_tests.xml`. Getestet werden:

- echte Python-Kindprozesse für Vorbereitung, beide SDK-Emulationskontexte und Vergleich;
- richtige Weitergabe bereits normalisierter NHWC-FLOAT32-Feeds, Form-/Dtype-/NaN-
  und Identitätsfehler, fehlende Stufen und Abbruchzustände;
- keine Build-/Optimierungs-/Speicher-API im Emulationsworker;
- Workflowsperre, Timeout, Prozessgruppenbereinigung und unveränderte Elternumgebung;
- originalgetreue Auswahl der 60 Hailo8-Text-/Nachweisdateien und der optionalen
  148 Qualitätssnapshot-Dateien aus den vorhandenen Originaluploads;
- echte lokale Git-Repositories samt lokalem Bare-Remote: explizite Auswahl, Commit
  und Push, unveröffentlichte fremde Commits, fehlende Bestätigung, falsches Ziel,
  vorab gestagte Dateien, Überschreibschutz, Modell-/Roharrayausschluss.

## Grenzen

**Kein echtes Hailo-SDK, keine realen HARs, keine neue Hailo-/CUDA-Ausführung und kein
GitHub-Push stehen in dieser Umgebung zur Verfügung.** Für numerische Prozessketten
werden synthetische ONNX-Runtime-/SDK-Antworten verwendet, die in einer isolierten
Test-Venv liegen; NumPy, Prozesse, Dateien, Locks, Archivierung und Git werden tatsächlich
ausgeführt. Die echten HAR-Methoden laufen erst auf Smartmirror2. Ihr Ergebnis wird bei
Fehlern als unvollständige Diagnose erhalten, nicht als bestandene Hardwareabnahme.

Der Kontrolltest der Originalarchive prüft echte bereits hochgeladene Dateien, keine
Modelle. Er überspringt sich außerhalb dieser Auditumgebung, wenn die Originaluploads
nicht vorhanden sind. In der dokumentierten finalen Paketprüfung liegen sie vor.
