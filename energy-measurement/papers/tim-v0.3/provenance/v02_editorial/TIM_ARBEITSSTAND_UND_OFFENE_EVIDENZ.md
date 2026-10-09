# TIM-Arbeitsstand und offene Evidenz — v0.2, 09.10.2026

## Jetzt umgesetzt

Der gelieferte TIM-v0.1-Entwurf ist zu einer zusammenhängenden Journalfassung
überarbeitet. Der Haupttext erzählt keine Entstehungs- oder Reparaturgeschichte.
Er beginnt mit Messgröße und Messgrenze, führt über den realen Hailo-Messpfad-
und Dauervergleich zu Fluktuationen und schließt mit der Ausführungsvalidierung.
Die finale Jetson-Studie wird als Ausgangspunkt zitiert, nicht erneut ausgebreitet.

Übernommen und geprüft sind native 5-MS/s-Scope-Ergebnisse, all-15-FP16,
Median individueller Paarabweichungen und konsistente Ratengruppenmittel.
Hailo ist nicht mehr fälschlich als bereits im PARMA-Manuskript enthalten
beschrieben. Die 300-s-Messwerte stehen in übersichtlichen Diagrammen; volle
Perzentile bleiben im Artefakt. Neu zusammengestellt ist der gemeinsame Verlauf
von Energie-, Leistungs- und Spannenabweichung über alle zehn Hailo-Dauerstufen.
Dafür wurden vorhandene Ergebnisse aggregiert, keine Rohsignale neu integriert.

## Was noch nicht durch die Überarbeitung erledigt ist

Das neue PDF ist ein lesbarer **Arbeitsentwurf**, nicht die Bestätigung einer
abgeschlossenen TIM-Einreichung. Die folgende Liste steht absichtlich nicht als
mehrseitiger Plan im Manuskript. Wissenschaftlich entscheidende Aussagegrenzen
stehen aber weiterhin dort.

| Thema | Belegt / vorhanden | Nächster zweckmäßiger Schritt | Konsequenz ohne Zusatzbeleg |
|---|---|---|---|
| Finale GPU-Erweiterung | Eingangsbestand enthält ältere direkte GPU-Reihen; kein neuer finaler Export im Auftrag | Den tatsächlich neuen GPU-Export samt Messgrenze und Ausführung einbinden, sobald er vorliegt | Keine GPU-Zahlen, NVML-Daten oder Gesamtboardgrenze erfinden |
| Hailo-Modell-/HEF-/Runtime-Zuordnung | Serienlabels und Erfassungsparameter; Bindungen teilweise unvollständig | Vorhandene Build-/Startprotokolle konkret den verwendeten Serien zuordnen | Nur innerhalb der jeweiligen Serie vergleichen; keine gematchte Effizienzrangliste |
| Hailo-Same-Trace-Energieprüfung | Native Spektren und direkte Energie-/Dauerausgaben | Prüfen, ob vorhandene native Aufnahmen für dieselbe Endpunkt-/Offset-/Quantilregel nutzbar sind; gezielt auswerten, keinen pauschalen Gesamtscan starten | Kein Hailo-f_min aus Jetson oder aus f99 ableiten |
| Host-/Karten-/Systemzerlegung | Karteninput und skalierte AC-Beobachtung | Zuerst vorhandene Messgrenzen/Versorgungen prüfen; für quantitative Anteile kompatible, zeitlich zugeordnete Komponentenmessungen nachweisen | AC/Karte-Differenz ist keine Hostleistung und kein Hostanteil |
| Dynamische Telemetrie | Gepaarte Mittelwerte, Energie und Spannen für zehn Anforderungsdauern | Vorhandene Zeitstempel und Marker auf Updateperioden, Mittelung und Versatz prüfen; nur bei Bedarf gezielter Test | Kein gemessener Lag, keine Event-Coverage und keine physikalische Updatefrequenz aus Aggregaten |
| Gematchter Continuous-/Burstbetrieb | Variable-YOLO-Reihen und separater Inter-Run-Pausentest | Entscheiden, ob diese stärkere Journalfrage beibehalten wird; dafür geplantes Aktivitätsmuster und tatsächlich erledigte Arbeit nachweisen | Variabler Lastfall ist kein nachgewiesen gematchter Burstvergleich, Pausentest kein Schedule-Energieoptimum |
| Proceedings-Abgrenzung / Rechte / Archivierung | PARMA-Author-Manuskript v0.15.1, Git/Tag laut Terminalprotokoll; noch keine publizierte Proceedings-Zitation | Vor Submission tatsächlichen Publikationsstand, technische Erweiterungsliste, Rechte und finale Artefaktversion festhalten | Keine angenommene Akzeptanz, DOI, Submission oder Rechtefreigabe behaupten |

## Priorisierung

Zuerst sollten die vorhandenen Hailo-Ausführungsbelege und der kommende finale
GPU-Datenstand geklärt werden. Parallel lässt sich die Hailo-Same-Trace-Prüfung
als begrenzte Offlineaufgabe auf vorhandenen Aufnahmen vorbereiten. Eine neue
mehrwöchige Messkampagne, ein universelles GUM-Budget oder sämtliche früheren
Erweiterungsideen werden durch diese Revision **nicht** stillschweigend zur
Pflicht erklärt. Hostzerlegung, kontrollierte Burstvergleiche und dynamische
Telemetrie brauchen eine ausdrückliche Scope-Entscheidung und passende Evidenz,
bevor entsprechende Ergebnisansprüche ergänzt werden.

Der jetzige Manuskriptanspruch ist enger: reale, grenzensensitive Messpfad-
vergleiche auf Jetson und Hailo, dauerabhängige Trennung von Energie und
Mittelwert, spektrale Einordnung sowie kontrollierte Protokollbeobachtungen.
Unter diesem Anspruch bleiben die genannten fehlenden stärkeren Nachweise
sichtbare Grenzen, keine ausgefüllten Ergebnisplatzhalter.

## Verbindlicher Schreibstil

Befund → Bedeutung → notwendige Einschränkung. Nicht Absatz für Absatz ein
Logbuch, keine historische Alt/Neu-Geschichte, keine langen Koeffizientenreihen.
Die passende Hardwarebeschreibung und wesentliche Kalibrierschritte bleiben
im Haupttext. Vollständige Werte, Regeln, Quellpfade und Zusatzprüfungen stehen
im Artefakt. Keine Auswahl nur günstiger Workloads oder Fenster.

## Operativer Stand

Diese Lieferung erzeugt und prüft lokale Dateien. Sie ändert den bestehenden
PARMA-Freeze nicht und legt keinen TIM-Commit, Tag, GitHub-Release oder Zenodo-
Eintrag an. Der vorangegangene PARMA-Push ist vom aktuellen TIM-Arbeitsstand
getrennt; dessen fehlende GitHub-Release-Anhänge werden dadurch nicht erzeugt.
