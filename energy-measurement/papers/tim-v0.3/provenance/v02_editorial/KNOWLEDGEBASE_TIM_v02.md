# Energy Paper — TIM v0.2 Anschlussstand (09.10.2026)

PARMA v0.15.1 bleibt als Jetson-zentrierter Manuskriptfreeze unverändert.
Sein Git-Stand `85eb488587a51659239c45d966f930f7c7b72a6e` ist Referenz für
diesen lokalen TIM-Entwurf. Der Git-Push erzeugt nicht automatisch alle
GitHub-Release-Anhänge; laut Nutzerprotokoll fehlte dafür gh.

TIM trägt nun den Arbeitstitel **Beyond Sampling Rate: Reference-Based Energy
Measurement Across Edge-AI Platforms**. Autoren unverändert: Kevin Mika,
Joris Wachsmuth, Florian Porrmann, Jens Hagemeyer. Der Haupttext verwendet
Hailo-Messpfade und Spektren als Journalerweiterung, Jetson native/all-15 als
kompakte Ausgangsbasis. Alte Aussagen, Hailo sei bereits PARMA-Hauptergebnis,
sind entfernt. Einheitlicher verständlicher Schreibstil; keine historische
Revisionsgeschichte oder langen Planungsabschnitte im Paper.

Statistik: Median individueller Paarabweichungen; Gruppenmittel gegen das
gleich gewichtete Mittel der Gruppenmittel. Alle 15 FP16-Aufzeichnungen,
native Scope-Rekonstruktion. Hailo-LLM-Gruppenabweichung 24,30%, nicht der
alte gemischte 33,09%-Wert. Keine Messwerte rückwirkend korrigiert.

Neu aus vorhandenen Ergebnisexporten aggregiert: Hailo E/P/T-Paarvergleich
für alle zehn angeforderten Dauern. Variable YOLO bei 5 s: etwa −0,7% mittlere
Leistungsabweichung, −10,3% Energieabweichung und −9,7% Spannenabweichung.
Endpunkte bleiben sensorabhängig; kein gemessener Telemetrie-Lag. Vollständige
Kurven und ungünstige Fälle bleiben erhalten.

Lieferumfang: PDF, cleanes LaTeX, kuratiertes Ergebnis-Quellenpaket samt
Generatoren, unabhängiger Zahlenprüfung und Methoden. 10 IEEE-Seiten insgesamt,
7 Abbildungen, 4 Tabellen. 79 übernommene data-Dateien unverändert. Es wurden
keine neuen Rohdatenintegrationen oder Messungen ausgeführt.

Offene stärkere Journalansprüche stehen in
`TIM_ARBEITSSTAND_UND_OFFENE_EVIDENZ.md`: finaler GPU-Export, Hailo-Ausführungs-
bindung, eigene Hailo-Same-Trace-Prüfung und je nach finalem Scope Hostzerlegung,
gematchte Bursts und dynamische Telemetrie. Nicht als bereits erfüllt ausgeben;
keinen pauschalen neuen Vollscan oder GUM-Kampagne daraus ableiten.

Diese Knowledgebase-Datei ist Teil der lokalen Lieferung. Der Online-KB-Einstieg
wurde durch diesen Bearbeitungsschritt nicht überschrieben. Kein TIM-Release,
keine DOI, keine Submission behauptet.
