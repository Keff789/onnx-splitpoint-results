# Ergänzende Offlineanalyse der vorhandenen Rangverfahren

05.10.2026. Explorative Auswertung nach Kenntnis der bestehenden THESIS20-Ergebnisse;
keine Präregistrierung, kein Hold-out-Test und keine neue Optimierung. Die geprüfte
Vertiefung wurde vor Veröffentlichung dieser Ergänzung regulär nach `main`
übernommen. Die aktuelle Ergänzung bleibt zunächst auf einem Reviewbranch.

## Fragestellung und festgelegter Vergleich

Wie unterscheiden sich die vorhandenen Graphheuristiken, Kostenprognosen und
gemessenen Generic-Proxies bei der Auswahl unter denselben gemessenen Native-
Kandidaten? Welche Durchsatz- und Energiekosten hat die jeweilige Auswahl?
Die bekannte 10/21-Zahl betrifft Generic-Completion, nicht Cut Bytes.

Zuerst werden Methode, Einheiten, Rangrichtung, historische Parameter und Quellen
je Modell/Setup inventarisiert. Kleine eingefrorene Metadaten aus der Hauptkampagne
ergänzen vorhandene kompakte Projektionen. Die Definitionen aus `ranking_methods.py`,
`objective_scoring.py` und `SystemSpec.estimate_boundary` sind maßgeblich. Gewichte
werden nicht auf Native-Ergebnisse angepasst. Heutige GUI-Werte sind keine
historischen Einstellungen. Fehlende Runner-/Richtungs- oder SystemSpec-Parameter
ergeben eine dokumentierte Lücke, keinen Nullwert und keinen Ersatzdefault.

Die Vergleichsgruppen übernehmen exakt Modell, Setup, Richtung, Precision,
Vergleichsbackend, Endpunkt und Messgrenze der bestehenden Paarung. Technische
Menge, Qualitytransfer und beidseitige Referenznähe bleiben getrennt. Ein Verfahren
mit unvollständigen Werten erhält keine still verkleinerte Hauptvergleichsmenge.
Der alte Raw-Proxy wird nur auf seiner identischen Basisschnittmenge ausgewertet.
Gruppen mit weniger als drei Fällen bleiben sichtbar.

Rangkorrelationen, Top1/Top-k, Durchsatzverlust und Kapazitätsregret verwenden die
bestehenden Definitionen; siehe `EVALUATION_METHODS.md`. Originale deterministische
Tie-Regeln und zusätzliche Tie-Sensitivitäten werden getrennt ausgewiesen.
Bestehende drei Wiederholungen liefern deskriptive Auswahlstabilität; analytische
Zufallsauswahl ist eine Referenzrechnung und keine zusätzliche Messung.

Für Energie wird der ausgewählte Split mit dem energieärmsten gemessenen Split
derselben Gruppe verglichen. Energie stammt aus eigenen bestehenden E/N-Fenstern.
Keine Generic-Energie wird erfunden, keine Full-Baseline mehrfach als unabhängig
gezählt und kein Performance-FPS als Energienenner eingesetzt.

Separat wird der globale Gewinner im ursprünglichen Graphuniversum betrachtet:
ungemessene Empfehlungen bleiben ohne Performance-/Qualityaussage; es erfolgt
kein verborgenes Nachrücken. Boundarybytes sind eine Tensorabschätzung und kein
gemessenes PCIe-Volumen. UINT8-Payload, Float-Dequantisierung und Runtimekopien
bleiben verschiedene Größen.

## Lieferung und Schutz des Bestands

Eine kompakte additive Projektion, reproduzierbare Auswertung, gezielte Tests,
Quellenmatrix, Fall-/Gruppentabellen, Sensitivitäten und zwei Hauptabbildungen.
Die vorhandenen Ableitungen werden relativ referenziert; Primärdaten werden nicht
dupliziert. Reproduktion erfolgt in einem getrennten Ausgabebaum. Tool v2.92.0,
Originalergebnisse und eingefrorene Archivquellen bleiben erhalten.

Die laufende Archivwarteschlange bleibt unangetastet. Diese Ergänzung ist zunächst
lokal und im Git-Reviewbranch gesichert; ihre Archivübernahme steht separat aus.
Die parallel begonnene englische Paperarbeitsfassung bleibt ausschließlich lokal.
