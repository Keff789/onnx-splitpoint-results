# Arbeitsstand – THESIS20 wissenschaftliche Reviewableitung

## Revision 3 — 07.10.2026, Softwareabschluss des Offline-Zwischenstands

Die Generic-Dauererweiterung ist im Worktree integriert und gezielt geprüft.
Neun vorhandene Generic-Punkte benötigen neue Bestätigungen vor finaler Energie.
Der aktuelle Quellreview umfasst 80 Dateien; die private unvollständige
Paperableitung wurde gebaut und reproduziert. Neue Hardware bleibt am konkret
angefragten H10-STOP gebunden. [Details und Belegquellen](NATIVE_FAIRNESS_REV3_20261007.md).

## Revision 3 — 07.10.2026, unvollständiger Zwischenstand

[Aktuelle Daten und Prüfbefehl](../results/evaluation/native_fairness_rev3_20261007/README.md)
· [technischer Befund](NATIVE_FAIRNESS_REV3_20261007.md).
15 neue Native-Punkte, neun belegte Wiederverwendungen, neun Generic-Paare;
drei Full-Energiepunkte über die normalen Consumer zugelassen. 222 neue
Native- und 195 weitere Generic-Performancepunkte fehlen. Physischer H10-STOP
bleibt bestehen; konkrete einmalige Fortsetzungsfreigabe ist angefragt.
Keine Datenlöschung oder Speicherbereinigung. Historisches Archiv nur lesend;
neue Rohbelege in einem getrennten datierten Zweig hashgeprüft. Die folgenden
Blöcke dokumentieren frühere Stände und sind keine aktuelle Startfreigabe.

## YOLOv7-Completion-Nachtrag — 07.10.2026

Berichtsbasierte Fortschreibung: neun Splitkonfigurationen mit 27 neuen
Prozessrepeats, sechs weiterverwendete optimierte Fulls mit 18 Repeats und drei
separate aktuelle TRT-Full-Kontrollen. Die Median-/Quotientenrechnung wurde
geprüft; neue Rohreports, Quellen, Telemetrie und Review-ZIP wurden für diese
Übernahme nicht unabhängig nachgeprüft. [Detaillierter Befund](YOLOV7_NATIVE_COMPLETION_20261007.md)
und [Daten/Provenienz](../results/evaluation/yolov7_native_completion_20261007/README.md).

Laut Bericht ist der Worktree-Fix im regulären Startpfad eingebunden; die
Hardwaremessungen verwendeten isolierte Candidate-Runtimes. Offen bleiben
der Rollout außerhalb des Worktrees und Energie für alle 15 aktuellen Varianten
(`not_measured`/NA). Historische Joulewerte werden nicht als Energie der neuen
Implementierung übernommen. Der ungeklärte restliche TRT-Full-Abstand und eine
mögliche Zusammenführung der doppelt gemessenen Finitprüfung sind getrennte
Folgefragen, keine pauschalen Voraussetzungen für die Performanceauswertung.
H8-b009/b044-Regressionswerte und sämtliche älteren Ergebnisstände bleiben erhalten.
Dieser Dokumentationsnachtrag veröffentlicht keinen Toolrelease und startet keine
neue Hardware-/Energiekampagne. Die folgenden Standblöcke sind datierte Historie.

## Archivabschluss — 05.10.2026, 12:06 CEST

Die vorhandene Archivkette ist tatsächlich beendet: Originalfinalisierung,
eingefrorene Vertiefung und zusätzliche private Ranking-/Papersicherung melden
jeweils Exitcode 0 mit passendem Abschlussstatus. Die große YOLO-Kopie wurde nicht
wiederholt. Ihre 61.729 Epoch-Zeitabweichungen sind durch Dateibelege geklärt,
darunter sechs ausdrücklich begrenzte Dateien über der bisherigen 1-MiB-Prüfgrenze.
Die BASE-Ergänzung übertrug ausschließlich 4.784 zuvor fehlende Symlinks,
keine regulären Dateien. Der abschließende BASE-Vergleich enthält keine
Größen-/Typ-/Linkabweichung; vorhandene Zielzeitstempel gleich großer regulärer
Dateien wurden nicht umgeschrieben.

Korrigierte Auswertung, Auditarchive, gebundene externe Originale und gefrorene
Quellen-/Analysepakete sind gesichert und im jeweiligen Umfang am Ziel geprüft.
Die vollständigen neuen Ranking- und Paperverzeichnisse wurden anschließend
sequenziell privat gesichert: Copy-/Checksum-Prüfungen jeweils 0, Differenzlogs
leer, Quellen unverändert. Die 12 Paperdateien wurden zusätzlich unabhängig am
Ziel bytegleich geprüft. Das Manuskript ist nicht Bestandteil dieses Gitpayloads.

Grenzen: kein vollständiger Ziel-Inhaltschecksum des großen Bestandsarchivs;
BASE nach Größe/Typ/Linktext, Folgetransfers zusätzlich nach regulären mtimes und
Epoch-Ausnahmen nur bei gezielter Bytegleichheit. Eine historische
`native_output_endpoint.py` mit 21 Referenzen fehlt weiterhin. Das sind nicht
21 fehlende Messfälle. Aktuelle Belege sind `final-archive-status.json`, die
Phasenendcodes, die Deep-Abnahme und `ranking_and_private_paper_copy_verified`.
Die darunterstehenden datierten Übergabestände bleiben als Historie erhalten.

Lokale Archivguardtests: 8 + 8 + 6 bestanden; unabhängige Abschlussprüfung
bestanden im genannten Umfang. Keine Originale gelöscht, keine eingefrorenen
wissenschaftlichen Quellen überschrieben. Tool v2.92.0, Originalergebnisse und
Methodengrenzen unverändert. Keine neue Messung, Inferenz, Kalibrierung,
Quality-/Benchmarkkampagne, Modellkompilierung oder Hardware-/GUI-Abnahme.
Nächster Schritt: fachlicher Review der vorhandenen Paperarbeitsfassung.

## Zusätzlicher Methodenvergleich — Mainintegration 05.10.2026

Der [Offlinevergleich der Rangverfahren](../results/evaluation/thesis20_20261004/methods_comparison_20261005/README.md)
wurde am 05.10.2026 per Fast-Forward von `29d931274a398822b99f4b83ace1d6962caabdcb`
auf den geprüften Reviewcommit `9c9c1c5c059485c6bc9b2e8eae6d3d5d6006dc27` nach
`main` übernommen, normal gepusht und remote nachgelesen. Der Branch
`analysis/thesis20-ranking-methods-20261005` bleibt erhalten.
Historische Parameter sind aus den kleinen Originalmetadaten belegt; fehlende
Native-Handover-/GUI-Bindungen bleiben unverfügbar. Keine neuen Modellfits.

Technische Top1: Cut 5/21, Weighted 7/21, gespeicherter H10-Fit 5/21,
Cycle ohne Handover 7/21, gespeicherte Stream-FPS 6/21, gemessene Completion 10/21.
Negative Fälle, 204/201/184-Kohorten, Raw-Schnittmenge, globale ungemessene
Empfehlungen, Tie-/Replikat-/Energiesensitivitäten und zwei Vektorfiguren sind
reviewbar. Die bestehende Abnahme bleibt gültig: 21 gezielte Tests bestanden;
27/27 Outputs separat bytegleich. Vor Integration wurden alle 49 Paketdateien
gegen die eingefrorene Lieferung und die 27 vorhandenen Reproduktionsausgaben
nochmals bytegleich bestätigt; keine erneute Berechnung oder Messung.

Die englische Paperarbeitsfassung mit numerischer Belegmatrix und Literaturbezug
bleibt privat und ist nicht in diesem Gitpayload. Die tatsächlichen Archivendcodes
und der Zielabgleich werden separat geprüft; die Mainintegration ist keine
Gesamtarchivabnahme. Dieser Git-Schritt startet keinen Transfer und keine Hardware-/Normal-GUI-Abnahme,
Messung, Inferenz, Qualityrechnung, Kalibrierung oder Kompilierung.

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
