# Arbeitsstand – THESIS20 wissenschaftliche Reviewableitung

## Integration und Navigation — 05.10.2026

Die geprüfte Vertiefung wurde zuerst per Fast-Forward von `e7bd8d8…` auf
`82f0a257…` nach `main` übernommen, normal gepusht und remote nachgelesen.
31 vorhandene Tests bestanden (1,18 s); die separate Reproduktion war in 71/71
Dateien bytegleich. [Prüfbefehle und Grenzen](THESIS20_INTEGRATION_20261005.md).

Danach wurden Root-README, [Repositorykarte](REPOSITORY_MAP.md) und KB-Einstieg
ergänzt. Historische Pfade und Datentabellen bleiben erhalten. URECS/PSD/TIM
bleiben ein eigener Bereich. Die kleine Navigation wird getrennt committet.

Normal-GUI-/Hardwareabnahme: nicht ausgeführt. Keine neue Messung, Inferenz,
Qualityrechnung oder Kompilierung. Tool v2.92.0, Collectorregeln und Budgets
bleiben unverändert. Der neue Offline-Methodenvergleich wird separat reviewbar;
die englische Paperarbeitsfassung bleibt lokal. Die Archivqueue läuft unverändert.

## Historischer Lieferstand — 04.10.2026

04.10.2026. Additive Dokumentation im Ergebnisreviewbranch. Der veröffentlichte
Toolcheckout und seine `docs/ARBEITSSTAND.md` bleiben entsprechend diesem Auftrag
bytegleich auf v2.92.0; dieser neue Ergebnisarbeitsstand verändert keinen Toolrelease.

Abgeschlossenes Arbeitspaket: post-hoc-Auswertung der vorhandenen Messungen nach
Fragen A–F, Sensitivitäten zu Kohorten/Quality/Replikaten/Fullprovenienz, sechs
Haupt- und drei Supplementfiguren, Claim-Evidence-Matrix und reproduzierbares
Reviewpaket. Kleine allein auswertungsbezogene Darstellungsreparatur an einem
Legacy-Energiefeld ist additiv mit Vorher/Nachher dokumentiert.

Softwareprüfung: fokussierte Ableitungstests und bytegleiche Gesamtreproduktion,
exakte Endbilanz in `deep_analysis/VALIDIERUNG.md`. Archivkorrekturen
wurden separat durch lokale Link-/Zeitstempeltests geprüft; keine erneute Toolabnahme.

Reale Normal-GUI-Abnahme/HW: nicht ausgeführt und nicht behauptet. Keine Inferenz,
Energieaufnahme, Kompilierung oder Qualitykampagne gestartet. Bestehende Collector-
Schutzregeln, Modi/Budgets und Originalergebnisse bleiben unangetastet.

Archiv: bestehende Queue gezielt nach SSHFS-Zeitfehlern fortgesetzt; completion192
Copy/Verify 0; große YOLO-Kopie aktiv, ursprüngliche Finalisierung wartet. Kein
Gesamt-PASS. Historische Attestorquelle weiterhin nicht gefunden. Neue Analyse
wird erst gefroren und anschließend nach Abschluss aller bisherigen Writer klein
additiv archiviert. Keine doppelte BASE-Kopie, keine Löschung.

Nächster Schritt: wissenschaftlicher Review der konkreten Claims/Figuren;
vorhandene Archivendcodes prüfen. Kein automatischer neuer Hardwareauftrag.
