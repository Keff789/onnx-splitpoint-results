# Änderungen TIM v0.3 gegenüber v0.2 — 09.10.2026

## Verbindlicher Richtungswechsel

TIM ist die eigenständig vollständige Journalerweiterung der PARMA-Arbeit.
Der Leser muss das Konferenzmanuskript nicht zuvor lesen. Der Recap ist die
wissenschaftliche Grundlage und bleibt im Haupttext; die Journalneuheit entsteht
zusätzlich aus den technischen Erweiterungen, nicht aus der längeren Erklärung.
Die Richtung »Jetson nur knapp zitieren, Hailo an dessen Stelle« ist aufgehoben.

## Im Paper wieder ausgebaut

- Vollständige Rekonstruktionslogik: unveränderte Ausführung/Endpunkte,
  Phasenversatz, Energiefehler, zweistufiges Q95, Maximum über Messpfade/Workloads
  und persistentes Minimum gegenüber einem einzelnen bestandenen Arbeitspunkt.
- Native Jetson-Ergebnisse für alle neun Dauern; eigene 2-kS/s-Abbildung sowie
  die 1-%- und 0,5-%-Entscheidungen in einer kompakten Tabelle.
- Alle 15 FP16-Aufzeichnungen: lange Energieintegration und Fluktuationsabdeckung
  stehen als zwei unterschiedliche Messziele unmittelbar nebeneinander.
- Der Jetson-Praxisvergleich steht mit allen sieben Workloads und drei Messpfaden
  im Journal. Die Mediane bleiben übersichtlich als Punktdiagramm dargestellt.
- Dauerabhängigkeit und direkte Rate-Sweeps sind für beide Plattformen sichtbar,
  statt Jetson hier nur durch einen Verweis abzudecken.

## Bewusst erhalten

Die v0.2-Diagramme und numerischen Ergebnisse zu Hailo DC/Telemetrie/AC,
Energie/Leistung/Intervallspanne, Spektren, Dauer und zum Pausentest bleiben
bestehen. Auch der Related-Work-Text und der ausdrücklich gelobte Hardwareabsatz
sind unverändert. Keine erneute Hinwendung zum Messprotokollstil; keine historische
Alt/Neu-Geschichte, langen Koeffiziententabellen oder offenen Arbeitspläne im Haupttext.

## Ergebnisbasis

Unverändert: native 5-MS/s-Rekonstruktion, 59 physische Paare, all-15-FP16,
Mediane individueller Paarabweichungen, eigene Sensorfenster, gespeicherte
Skalierungen und gleich gewichtete Ratengruppenmittel. Alle 81 Dateien im
Datenverzeichnis sind unverändert. Die zusätzlichen Darstellungen selektieren
bereits vorliegende Werte; keine Messung, Rohdatenintegration oder PSD-Neuschätzung.

## Umfang und Prüfungen

13 IEEE-Seiten einschließlich Literatur statt zehn Seiten; zehn nummerierte
Abbildungen und vier Tabellen. Unveränderte Grundschrift und Seitengeometrie.
Der Umfang ist kein künstliches Ziel: zusätzliche GPU-Ergebnisse werden später
an der passenden Stelle eingebaut, ohne dafür die Grundlage erneut zu entfernen.

Regeneration, unabhängige Zahlenprüfung und frischer Build des schlanken Projekts
werden in `metadata/BUILD_AND_PACKAGE_QA.json` dokumentiert. Die erneute
Policy-Prüfung steht in `metadata/TIM_EXTENSION_POLICY_20261009.md`.
