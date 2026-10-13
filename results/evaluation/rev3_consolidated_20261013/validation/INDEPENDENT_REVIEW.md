# Unabhängige Prüfung der Twix-Offlineanalyse

Prüfdatum: 13. Oktober 2026. Ergebnis: **Die geprüften kompakten Daten, Paarzulassungen und numerischen Ergebnisse stimmen mit einer getrennten Nachrechnung überein. Die beschriebenen Archivgrenzen bleiben bestehen.**

Die Prüfung erfolgte durch einen getrennten Review-Agenten. Das Prüfprogramm `independent_check.py` verwendet ausschließlich die Python-Standardbibliothek und importiert weder Extraktions- noch Analysefunktionen der geprüften Implementierung. `INDEPENDENT_CHECKS.json` enthält Prüfzähler, nachgerechnete Ergebnisse und SHA-256-Werte aller verwendeten Eingaben, Tabellen, Methoden- und Implementierungsdateien. Der dort hinterlegte Skripthash bindet auch die Prüfimplementierung. Es wurden keine Messungen, Hardwarezugriffe oder Änderungen an Originaldaten vorgenommen.

Der Prüfumfang umfasst die Methodenbeschreibung, die Extraktions- und Reproduktionsskripte, ausgewählte ursprüngliche Current-Bindungen sowie die vollständige numerische Nachrechnung der unten genannten kompakten Ergebnisse. Dies ist keine unabhängige Wiederholung der Datenerhebung und keine vollständige erneute Sensorintegration oder Dataset-Auswertung.

## Nachgerechnete Ergebnisse

| Aussage | Unabhängig bestätigtes Ergebnis |
|---|---:|
| Eindeutige aktuelle Identitäten | 450: 246 Native, 204 Generic |
| Normal zugelassene Energiebeobachtungen | 437 Identitäten mit jeweils 3 Wiederholungen |
| Native schneller als technisch gebundenes Generic | 139 / 204 |
| Native mit niedrigerer Rohenergie als Generic | 154 / 198 |
| Native mit beiden Vorteilen | 134 / 198 |
| Median Native/Generic-FPS-Verhältnis | 1.3613348315788745 |
| Median Native/Generic-Rohenergieverhältnis | 0.755245694654413 |
| Streng zugelassene Split/Full-Energiepaare | 312 |
| Zusätzlich für Performance zugelassene Split/Full-Paare | 200 |
| Splits schneller als ihre schnellste zulässige Fullalternative | 44 / 132 |
| Splits energieärmer als ihre energieärmste zulässige Fullalternative | 60 / 188 |

Alle 204 Native/Generic-Paarungen wurden anhand der Identität, der technischen Gates und der kompakten exakten Performancehash-Bindungen geprüft. Für zugelassene Energievergleiche stimmen Kalibrierung, physischer Messumfang und Messfenster zwischen den Regimen überein. Die Prüfung bestätigt die 396 archivierten Full-Paarentscheidungen: Ein positives Claimflag allein genügt nicht. Die 28 Paare ohne zusätzliche semantische Zulassung bleiben ausgeschlossen. Die Performancepaare verlangen zudem beide Performancefreigaben. Ihre Beschränkung auf vorhandene strenge Energiepaarverträge ist konservativ und stellt keine vollständige Erfassung aller theoretisch möglichen Performancevergleiche dar.

Die schnellste und die energieärmste Fullalternative wurden für jeden Split getrennt neu ausgewählt. Alle sechs Kombinationen aus Qualitäts-/Provenienzfilter und Energiegrundlage wurden unabhängig nachgerechnet, einschließlich der 126 anschließenden Modell-/Setup-Optima:

| Auswahlfilter | Energiegrundlage | Schneller als schnellste Full | Energieärmer als energieärmste Full |
|---|---|---:|---:|
| Alle zugelassenen Fälle | Vergleichsenergie | 44 / 132 | 60 / 188 |
| Alle zugelassenen Fälle | Rohenergie | 44 / 132 | 75 / 188 |
| Beide reference_close | Vergleichsenergie | 44 / 123 | 57 / 171 |
| Beide reference_close | Rohenergie | 44 / 123 | 72 / 171 |
| Ohne administrative Receiptlücken | Vergleichsenergie | 38 / 115 | 60 / 171 |
| Ohne administrative Receiptlücken | Rohenergie | 38 / 115 | 75 / 171 |

Die bestehende Hostnormalisierung ändert bei 34 zugelassenen Split/Full-Paaren die Richtung des Energievergleichs. Nach erneuter Auswahl der jeweils energieärmsten Fullalternative ändern sich 15 Richtungen. Das sind verschiedene Bezugsgrößen; eine bloße Umrechnung bei unverändert ausgewählter Baseline würde die Sensitivitätsfrage nicht vollständig beantworten.

## Metriken, Unsicherheit und Interpretation

Die Nachrechnung bestätigt alle 1311 Sensorquotienten E/N und N/E, ihre Mittelwerte, die Umrechnung von J/Task nach mJ/Task sowie die getrennten Effizienzgrößen mean(N/E), 1/mean(E/N) und sum(N)/sum(E). Die Energieintervalle entsprechen der angegebenen zweiseitigen t-Rechnung mit drei Wiederholungen, df = 2 und t = 4.302652729749461. Diese nominellen Mittelwertintervalle quantifizieren Wiederholungsstreuung unter den Modellannahmen; systematische Kalibrierungsunsicherheit ist darin nicht enthalten. Sie sind keine Vorhersageintervalle und kein Signifikanztest für alle untersuchten Splitkandidaten.

Die 444 dreifach beobachteten FPS-Werte entsprechen jeweils dem Median. Sechs historische Native-Full-Einzelwerte sind gekennzeichnet und liefern keine neuen Performanceclaims. Die neun Kreuzquotienten zweier Dreierkohorten wurden als Spannweitensensitivität nachgerechnet. Sie dürfen nicht als neun unabhängige Replikate interpretiert werden. Auch Paare mit gemeinsamem Fullreferenzwert sind abhängig.

Alle 770 Paretoentscheidungen wurden durch erneute Dominanzsuche innerhalb der vollständigen Modell-, Setup-, Runner-, Backend-, Präzisions-, Eingabe-, Completion- und Messvertragsgruppen bestätigt. Die Fronten verwenden FPS und Rohenergie; Qualität ist ein gesonderter Filter und keine ungenannte dritte Paretoachse. Alle 420 Spearman-Zusammenhänge wurden durch eigene Rangbildung mit Mittelrängen bei Bindungen nachgerechnet. Konstante Merkmale erhalten keinen Korrelationswert. Die Beschreibung als nachträgliche, deskriptive Assoziationen ohne Kausal- oder Generalisierungsnachweis ist angemessen.

Die Pipelineprojektion enthält 720 eindeutige Wiederholungsidentitäten und keine als fehlend ausgewiesenen direkten Bindungen. Ausgewählte ursprüngliche Rohreports wurden im Methodenreview auf die Feldbedeutung geprüft. Das Prüfprogramm bestätigt hier Vollständigkeit und Identitäten, nicht die vollständige Extraktion jedes Timingfelds aus allen Rohreports. H10-Asynchronlatenz, effektiver Durchsatzzyklus und Queuewartezeit bleiben unterschiedliche Größen; überlappende Workerzeiten und mögliche Completion-/Postprocessing-Aliase werden nicht zu Gesamtprozenten addiert.

Die getrennte YOLOv7-/DeepX-Abnahme ergibt aus den gespeicherten Werten −2.371055149976631 % FPS und +0.3598078449767561 % Energie gegenüber ihrem historischen Kontext. Sie bleibt ein diagnostischer Einzelwert außerhalb der 450 wissenschaftlichen Identitäten. Der unbekannte kanonische RGB-Hash und die Untauglichkeit eines historischen Mittelwert-CI als Abnahmetest werden ausdrücklich benannt.

## Erhaltene negative Befunde und Archivgrenzen

Alle 43 aktuellen accuracy_loss-Zeilen und die 13 Fälle ohne normale Energiezulassung bleiben erhalten. Die Analyse ersetzt negative Qualität nicht durch ältere positive Beobachtungen. Funktionale Ausgabeparität und datasetbasierte Qualität werden sachgerecht getrennt.

Bei 17 aktuellen MobileNet-/DeepX-Native-Identitäten fehlt die erwartete Byteversion einer administrativen Quality-Join-Receipt. Die vorhandenen alternativen Receipts schließen diese Lücke nicht. Für alle 56 untersuchten direkten Joins stimmen jedoch die referenzierten normalen Ergebnis- und Validierungsblätter exakt mit Current überein. Die Analyse kennzeichnet die 17 Fälle und ihre Generic-Paarungen; die Sensitivität ohne diese Identitäten wurde nachgerechnet. Ein unbeschränkter Nachweis einer lückenlosen Provenienzkette wäre weiterhin unzulässig. Hinzu kommt der erklärte fehlende historische Full-Producer-Quellhash mit 21 Referenzen.

Die 16 kompakten Eingabedateien stimmen mit ihrem Manifest überein. Eine solche Prüfung beweist weder die Vollständigkeit des gesamten Roharchivs noch die physikalische Kalibrierung. Historische Kohorten bleiben eigenständig; ein numerisch gleicher Altwert beweist keine identische Beobachtung oder identische Dateiversion. Die auf Twix ausgeführte Archivkopie und das vollständige private Extraktionsreplay haben eigene Belege und sind nicht als Ergebnis dieses unabhängigen kompakten Prüfprogramms auszugeben.

## Reproduktion dieser Prüfung

Mit Python 3 aus einem beliebigen Arbeitsverzeichnis:

```text
python3 PATH_TO_REVIEW/independent_check.py --package PATH_TO_PACKAGE --output INDEPENDENT_CHECKS.json
```

`PATH_TO_PACKAGE` bezeichnet das Verzeichnis mit `inputs/`, `results/`, `scripts/` und `METHODS.md`. Der erwartete Status lautet `PASS_COMPACT_ARITHMETIC_WITH_DECLARED_ARCHIVE_LIMITS`. Das Programm verwendet keine Netzwerkdienste und benötigt keine zusätzlichen Python-Pakete. Bei Veränderungen der verwendeten Dateien müssen die Prüfung und ihre Hashbelege erneuert werden.
