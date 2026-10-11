# Änderungen TIM v0.2 gegenüber v0.1

## Inhaltliche Neuausrichtung

- Neuer Titel: **Beyond Sampling Rate: Reference-Based Energy Measurement Across Edge-AI Platforms**.
- Hailo wird zum zentralen Journalergebnis: Karteninput, u.RECS, HailoRT und skalierte AC-Beobachtung; anschließend Dauer- und Spektralbetrachtung.
- Jetson dient als explizit zitierte, kompakte Referenz aus PARMA v0.15.1. Hailo-Ergebnisse werden nicht mehr fälschlich dem PARMA-Manuskript zugeschrieben.
- Drei Forschungsfragen zu realer Messpfadübereinstimmung, Energie gegenüber zeitlicher Struktur und Ausführungsprotokoll ersetzen die vorherige Mischung aus Ergebnissen und geplanten Arbeiten.
- Related Work verbindet Vergleichbarkeit, Kalibrierung/zeitliche Auflösung und Telemetrie. Es ist keine bloße Aufzählung gelesener Arbeiten.
- Planungstabellen, Statusabsätze und technische Erweiterungsversprechen sind in den separaten Arbeitsstand verschoben. Wissenschaftliche Grenzen bleiben im Paper.

## Statistik und finale Ergebnisbasis

Die Änderungen sind explizit gegen den finalen PARMA-Stand abgeglichen; sie
werden nicht als neue physische Messungen dargestellt:

| Punkt | Bisheriger TIM v0.1 | TIM v0.2 |
|---|---|---|
| Hauptrekonstruktion | Reduktion auf 1 MS/s | Direkte native 5-MS/s-Rekonstruktion |
| FP16-Hauptkohorte | 13 ausgewählte Aufzeichnungen | Alle 15; 960 numerische Fälle je Energierate |
| FP16-Spektrum | Unterschiedlich lange Aktiv-/Idle-Auszüge als Hauptfall | All-15, matched_4s_4s; geeignete Robustheitsbelege im Artefakt |
| 2-s persistentes 1%-Minimum | 2 kS/s | 16 kS/s; der feste 2-kS/s-Punkt bleibt bestanden |
| Direkte Gruppenabweichung | Mittel gegen Mittel der Mediane | Mittel gegen gleich gewichtetes Mittel der Gruppenmittel |
| Hailo-LLM maximale Gruppenabweichung | 33,09% | 24,30%; Änderung der Kennzahl, keine Verbesserung der Messung |
| Messgerätezentrum | Quotient der Gruppenmediane | Median der individuellen Paarabweichungen |
| Nicht reproduzierter FP16-Einzelmaximalwert | 1,071% | Nicht als finale Hauptaussage verwendet; 50 S/s quantilweise bestanden, 85 S/s alle untersuchten Fälle |

## Zusätzliche Auswertung vorhandener Ergebnisse

Die gepaarten Hailo-Beobachtungen werden für alle zehn angeforderten Dauern
zusammengeführt und gleichzeitig nach E, P=E/T und T ausgewertet. Bei variablem
YOLO und 5-s-Anforderung liegt der HailoRT-Median für P etwa 0,7% niedriger,
für E aber etwa 10,3% niedriger; die Spannenabweichung beträgt etwa −9,7%.
Die vorhandenen Intervalle unterscheiden sich. Das ist keine gemessene
Verzögerung der Telemetrie und keine nachträglich angepasste Integration.
Bei 300 s sind Energie- und Mittelwertunterschied beide unter 1% im Betrag.
Die vollständigen Kurven einschließlich der übrigen Dauerstufen werden gezeigt.

Diese Verknüpfung ist aus bereits gespeicherten Messausgaben berechnet. Es
wurden keine neuen Rohdaten, Kalibrierfaktoren, Zeitverschiebungen oder
Hardwareergebnisse ergänzt. Variabler Lastfall und LLM-Streuung bleiben
sichtbar, obwohl sie weniger günstige Messsituationen zeigen.

## Darstellung

Der geprüfte Build umfasst **zehn statt fünfzehn IEEE-Seiten insgesamt**, mit
sieben nummerierten Abbildungen und vier Tabellen. Die IEEE-Zweispaltigkeit,
Grundschrift und Seitengeometrie bleiben erhalten. Alte komplexe Figuren
und Wiederholungen der PARMA-Kurven entfallen. Für den 300-s-Hailo-Vergleich
werden zwei übersichtliche Median-Diagramme mit explizit getrennten Skalen
verwendet; Perzentile und sämtliche Paarwerte bleiben im Quellenpaket.

## Prüfung und Dateikonsistenz

Die numerischen Generatoren, separaten Standardbibliotheksprüfungen,
Quellenzuordnung und Methoden sind Bestandteil der Lieferung. Geprüft werden
4416 einzelne Paarzeilen, 300 Paargruppen, 100 Dauergruppen und zwölf direkte
Ratenserien. Die 30 300-s-Zentralwerte/Quantilzeilen stimmen mit dem finalen
PARMA-Quellenpaket überein. 79 übernommene Dateien im ursprünglichen `data/`-
Verzeichnis sind byteidentisch erhalten; ergänzte Pausendaten sind an ihren
Repository-Commit und Git-Blob gebunden. Nicht benötigte ältere Binärarrays
aus dem größeren PARMA-Paket werden nicht zusätzlich dupliziert.

Das Manuskript und das Quellenpaket verwenden denselben LaTeX-Text, dieselben
Tabellen und dieselben Abbildungen. Die Prüfberichte unterscheiden Export-
Reproduktion von Rohsignal-Reproduktion. Noch fehlende Journalbausteine stehen
in `TIM_ARBEITSSTAND_UND_OFFENE_EVIDENZ.md`, nicht als erledigte Ergebnisse.
