# TIM Figures 1.1.0 — Methoden- und Darstellungsentscheidungen

## Datenbasis

Der Plotter liest ausschließlich den mitgelieferten, hashgebundenen Ergebnis-Snapshot der
abgeschlossenen Offline-Neuauswertung. Keine Rohmessung, keine neue Integration, keine
Kalibrieränderung. Alle endlichen Kandidaten mit positiver Dauer bleiben erhalten.

## Konsolidierte Paper-Fenster

Eine vorab festgelegte, serienweise Regel ersetzt den früheren Alt/Neu-Papervergleich:

- Default: `envelope_0.5`, also NPY-basierte Signalhülle.
- LLM: `envelope_0.5`; historische YAML/NPY-Provenienz wird im Paper nicht als Alt/Neu-Plot diskutiert.
- Hailo Random Pattern: `reported_legacy`, weil die automatische Hülle frühe Bursts beziehungsweise
den Aufnahmebeginn nicht robust bestimmt.

Die Auswahl ist nicht ergebnisabhängig und wird in `tables/paper_window_policy.csv` ausgegeben.
Legacyplots bleiben nur als Audit/Supplement erhalten.

## Heatmaps und Einheiten

- N/A wird hellgrau und mit `N/A` dargestellt.
- Qualitäts-/Quellnotizen erhalten einen kleinen Eckpunkt; keine flächige Schraffur.
- Dauerwerte erscheinen als µs/ms/s, Abtastraten als S/s, kS/s oder MS/s.
- Farbsättigung beschneidet nur die Farbskala, nicht die CSV-Werte.
- Direkte Sweeps sind separate Ausführungen und kein isolierter Samplingfehler.

## Kontrollierter GEMM-FP16-Test

Zwei komplementäre Sechs-Läufe-Sessions verwenden dieselbe Engine, 250 Queries,
120-s-Prozesspausen und entgegengesetzte Rate-Reihenfolgen. Der Plotter enthält:

- positionsbalancierte Effekte mit deskriptivem Intervall;
- direkten historischen Sweep versus kontrollierten Diagnosetest.

Keine rückwirkende Offset- oder Driftkorrektur wird auf historische Daten angewandt.
Pico und VDD_IN besitzen unterschiedliche Messgrenzen und sind nicht hardwarezeitsynchron.

## Zusammenfassungsmetriken

- Samplerate: Energie relativ zum festen 2-kS/s-Median derselben Serie.
- Dauer: pro Run E/T relativ zum 600-s-Median derselben Serie.
- Wiederholungsstreuung: Populationsstandardabweichung / Betrag des Mittelwerts.
- q95: empirisches 95. Perzentil der absoluten Einzelergebnisabweichung zum festen Serienbezug.
- Persistente Übereinstimmung: Kriterium muss am genannten und an allen folgenden beobachteten
Rasterpunkten erfüllt sein; keine Interpolation, keine Genauigkeitsspezifikation.

## Messpfadvergleich

Paarung nur über gleiche Serie und `record_id`. Eigene Fenster, unterschiedliche Messgrenzen
und Glättungen bleiben erhalten. Die Ausgaben sind beobachtete Ergebnisunterschiede, keine
synchronisierte isolierte Gerätefehlerprüfung.

## Reproduzierbarkeit und GPU-Nachtrag

Gleiche Datenbytes, Codeversion und Umgebung liefern dieselben Teilnehmer und Statistiken.
Neue GPU-Messungen erfordern zuerst einen neuen Offline-Ergebnisexport und Snapshot; danach
wird eine neue Plotversion erzeugt. Der bestehende Freeze wird nicht überschrieben.
