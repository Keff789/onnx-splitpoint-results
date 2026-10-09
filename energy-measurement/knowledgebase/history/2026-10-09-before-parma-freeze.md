---
title: "Energy Paper – Current Consolidated Status"
project: "How Fast Is Fast Enough? Reference-Calibrated Energy Measurement for Edge-AI Inference"
status_date: "2026-10-09"
full_baseline: "Energy_Paper_TIM_KnowledgeBase_2026-09-30.md"
latest_review: "knowledgebase/2026-10-09-offline-robustness.md"
offline_sensitivity_tool: "energy_paper_checks.py v1.0.1"
full_consolidated_artifact: "Energy_Paper_TIM_KnowledgeBase_2026-10-01.md"
canonical_analysis_tool: "common_reference_psd_tool_v0.7.3"
result_plot_tool: "tim_figures_v1.1.0"
language: "de"
---

# Energy Paper – konsolidierter aktueller Status

Diese Datei ist der aktuelle operative Einstieg und konsolidiert die Nachträge nach der
vollständigen KB vom 30.09. Die alte Langfassung bleibt der historische Detailbestand; bei
Widerspruch gelten die Entscheidungen hier. Eine vollständige konsolidierte Langfassung
`Energy_Paper_TIM_KnowledgeBase_2026-10-01.md` wurde parallel erzeugt.

## 0. Neuester Anschlussstand – 09.10.2026

Die [Offline-Robustheitsprüfung](knowledgebase/2026-10-09-offline-robustness.md) ist jetzt
für alle **118 Scope-Quellspuren / 59 Paare** abgeschlossen. Die geprüften kompakten
[Ergebnisse und Skripte](2026-10-09-offline-robustness/README.md) sind gesichert.
Der historische Detailbestand und die ursprünglichen Paper-Ergebnisse werden dadurch
nicht überschrieben. Der Dateiname dieses operativen Einstiegs bleibt für bestehende Links erhalten.

- Die realen Scope-Rateordner heißen `5000000` ohne `Sps`. Der anfängliche Nullfund lag
  an der zu engen Pfadannahme des Zusatzskripts, nicht an nachgewiesen fehlenden Rohdaten.
- Vorverarbeitung auf 1 MS/s ist für die anschließende Zielratenrekonstruktion nicht
  allgemein wirkungslos: acht punktuelle Wechsel an 0,5 % oder 1 %, vier Änderungen
  persistenter Minima bei diesen Toleranzen. Kleine Referenzintegraländerungen reichen
  als Gleichwertigkeitsbeleg nicht aus.
- **2 s / 2 kS/s besteht das einzelne 1-%-Kriterium.** Die persistente Mindest­rate
  des neuen Rasters ist trotzdem **16 kS/s in beiden Pfaden**, da 9,4 kS/s knapp über
  1 % liegt. Die ursprünglichen 2 kS/s sind damit nicht rasterunabhängig bestätigt.
- Die getrennte FP16-Prüfung bestätigt 50 S/s für Q95 < 1 % und 85 S/s für alle
  geprüften Fälle auch mit allen 15 Aufzeichnungen. Die spektralen 125/160-kS/s-Grenzen
  bleiben bei gleichen Welch-Segmentzahlen und alternativen Idle-Blöcken erhalten.
- Noch offen: konkrete Ursache der Unterschiede zum ursprünglichen Fenster-/Phasenraster,
  historischer FP16-Auswahlgrund und Umfang der in 51 Scope-Spuren markierten
  Strommodell-Extrapolation. Der beigefügte Archivhelfer exportiert dafür bereits
  vorhandene Auditfelder und gezielte Vergleiche; keine erneute Rohdatenauswertung nötig.
- **Paperumfang bleibt konstant:** bestehende Methodensätze präzisieren und Werte ihrer
  jeweiligen Auswertung zuordnen; zusätzliche Prüftabellen in der Evidence halten.

## 1. Verbindliche Datengrundlage

- Die mehrwöchige Messkampagne wird nicht wiederholt.
- Der 4,418-TB-Offlinelauf ist abgeschlossen; keine erneute Gesamtrechnung.
- Common Reference / Same Trace trägt die Aussage zum isolierten Sampling- und Grid-Offset-Effekt.
- Direkte Samplerate-Sweeps sind separate physische Ausführungen und enthalten Session-,
  Reihenfolge-, Grundlast-, Temperatur-, Fenster- und Akquisitionseinflüsse.
- Die ursprünglichen PSD/Common-Reference-Ergebnisse bleiben ein eigener archivierter Zweig;
  der unabhängige Zusatzcheck vom 09.10. ergänzt die Robustheitsbewertung.

## 2. Lastfenster und Paper-Politik

Die deterministische NPY-Auswertung verwendet energiegewichtete 100-ms-Bins, Randmediane,
P95-Lastpegel, feste 0,4/0,5/0,6-Schwellen, mindestens 200 ms Aktivität und die Hülle vom
ersten bis zum letzten qualifizierten Abschnitt inklusive innerer Pausen. Kein Dauerfit.

Paper-Auswahl:

- Default: `envelope_0.5`, NPY-basierte Lastfenster.
- LLM: ausschließlich neue NPY-basierte Ableitung; kein Alt/Neu-Vergleich im Paper.
- Hailo Random Pattern: `reported_legacy`, historisches explizites Fenster.
- Keine Auswahl nach Kurvenrichtung, Streuung oder Ergebnisgröße.
- Fehlende Werte bleiben N/A; kein stiller Ersatz durch Legacywerte.
- Keine rückwirkende Offset-, Gain-, Drift-, Zeit- oder Temperaturkorrektur.

## 3. Fixed-Window-Prio-A

Für GEMM FP16, GEMM INT8, LLM, YOLO FP32 und YOLO INT8 wurden bei 2 kS/s, 250 kS/s
und 5 MS/s identische 20–80-s-Fenster ausgewertet, jeweils alle 15 Wiederholungen. Die
historischen Mehrprozenttrends bleiben teilweise bestehen und sind damit nicht allein durch
unterschiedliche äußere Hüllengrenzen erklärbar. Gleichzeitig verschiebt sich das Vorlaufniveau
bei den auffälligen Reihen in ähnlicher Richtung. Daraus wird kein automatischer Nullpunktabzug
abgeleitet.

## 4. Kontrollierter komplementärer GEMM-FP16-Test

Zwei vollständige Sechs-Läufe-Sessions verwendeten dieselbe Engine, 250 Queries,
`--useSpinWait`, 120 s Prozessende-zu-Prozessstart-Pause und komplementäre Ratefolgen:

```text
Session 1: 2 kS/s, 5 MS/s, 5 MS/s, 2 kS/s, 2 kS/s, 5 MS/s
Session 2: 5 MS/s, 2 kS/s, 2 kS/s, 5 MS/s, 5 MS/s, 2 kS/s
```

Jede Sequenzposition enthält über beide Sessions einmal jede Rate. Der rohe Medianeffekt der
Pico-Lastleistung wechselte mit der Reihenfolge von −0,508 % auf +0,441 %. Im additiven
Session-/Positionsmodell:

| Größe | balancierter Effekt 5 MS/s − 2 kS/s |
|---|---:|
| Pico-Leistung im festen Lastfenster | −0,061 % |
| Pico Last minus Vorlauf | −0,204 % |
| Jetson VDD_IN Last | +0,009 % |
| TensorRT-Laufzeit | −0,030 % |

Die Intervalle sind diagnostisch, kein metrologisches Unsicherheitsbudget. Der Versuch belegt
keine universelle Gleichheit aller Raten, zeigt aber, dass der historische Mehrprozenttrend nicht
stabil an die konfigurierte Rate gebunden ist.

## 5. Stromsignaldrift

In beiden Sessions steigen Pico-Vorlauf- und Pico-Lastleistung vom ersten zum sechsten Lauf
nahezu parallel um ungefähr 0,7 W. Last-minus-Vorlauf ist deutlich stabiler; VDD_IN und
TensorRT zeigen keinen vergleichbaren Trend. Der Mechanismus ist nicht identifiziert. Ein
reiner mehrprozentiger Shunt-TCR ist wegen der nahezu lastunabhängigen absoluten Verschiebung
keine bevorzugte Erklärung. Weitere Mechanismustests sind optional und derzeit keine
Voraussetzung für den Paperstand.

## 6. Plotsoftware und Hauptfiguren

`tim_figures_v1.1.0` liest nur den eingefrorenen Ergebnissnapshot. Änderungen:

- hellgraues N/A statt erfundener Nullwerte;
- kleine Notizmarker statt flächiger Schraffur;
- lesbare Achsen als s/ms und S/s/kS/s/MS/s;
- Paperübersichten nur mit der konsolidierten Fensterpolitik;
- kontrollierte GEMM-FP16-Effektfigur;
- historischer direkter Sweep versus kontrollierter Diagnosetest;
- vollständige Joris-Familien weiter als Supplement/Audit.

Empfohlene Hauptfiguren:

1. kanonische Common-Reference-/PSD-Hauptfigur;
2. kompakte direkte-Sweep-Übersicht mit Nicht-Kausalitätscaption;
3. direkter historischer Sweep versus kontrollierter GEMM-FP16-Test;
4. Dauerübersicht der Lastleistung;
5. optional run-gepaarter Messpfadvergleich bei 300 s.

## 7. GPU-Nachtrag

Zusätzliche GPU-Messungen werden in ungefähr zwei Wochen erwartet. Danach:

1. Rohdaten sichern;
2. gleiche Offline-Fenstermethode ausführen;
3. neuen vollständigen Ergebnisexport erzeugen;
4. neuen Plot-Snapshot versionieren;
5. Plotsoftware in einem neuen Ergebnisordner ausführen.

Ein Neustart des eingefrorenen Plotpakets allein entdeckt keine neuen Rohdaten.

## 8. Sicherung und Evidence

Öffentliche kompakte Evidence liegt unter
`energy-measurement/2026-10-01-controlled-rate-test/` mit Fixed-Window- und komplementären
Tabellen, QA, Quellenhashes und `verify.py`. Git und Review-ZIPs ersetzen kein Rohdatenbackup.

Die Scope-/FP16-Zusatzprüfung liegt unter
[`2026-10-09-offline-robustness/`](2026-10-09-offline-robustness/README.md).
Die hochgeladenen Zusammenfassungen und FP16-Einzelergebnisse sind dort enthalten.
`archive_energy_checks.py` ergänzt auf Twix die lokalen Laufmetadaten, kompakte
Record-/Fenster-Audits und die kritischen Vergleichsvektoren. Die vollständige große
Scope-ZIP und die Original-Records bleiben im Laborarchiv; ihr Transfer ins Git ist
nicht erforderlich. Der lokale Detail-Export ist erst nach dessen erfolgreichem
Aufruf und Commit gesichert, nicht bereits durch diese KB-Änderung.

Noch operativ auszuführen: beide neuen `baselineRateTests`-Sessionordner mit
`archive_baseline_rate_tests_to_sprite_20261001.sh` von Memmert in das Sprite-gestützte
`/homes/kmika` kopieren und per `rsync --checksum` prüfen. Vor erfolgreicher Prüfung auf
Memmert nichts löschen.

## 9. Zulässige Claims

Zulässig:

- Die Lastfensterdefinition ist Teil der Messgrößendefinition.
- Direkte Sweeps enthalten mehr als den Samplingeffekt.
- Der kontrollierte GEMM-FP16-Test zeigt einen balancierten rateassoziierten Rest nahe null.
- Der historische Mehrprozenttrend ist kein stabiler deterministischer Rateeffekt des
  kontrollierten Protokolls.
- Common Reference bleibt die Basis für isolierte Sampling-/Grid-Offset-Aussagen.
- Die zusätzliche Scope-Prüfung weist eine Empfindlichkeit gegenüber dem gesamten
  5→1-MS/s-Verarbeitungspfad und dem endlichen Auswerteraster nach.

Nicht zulässig:

- historische Sweeps nachträglich auf null korrigieren;
- Vorlaufleistung als unabhängig verifizierten elektrischen Nullpunkt behandeln;
- VDD_IN als absolute Kalibrierreferenz ausgeben;
- aus GEMM FP16 universelle Gleichheit von 2 kS/s und 5 MS/s ableiten;
- Hailo Random Pattern mit pro Run ausgewählter Hüllenschwelle darstellen.
- Aus der Erhaltung des Referenzintegrals die Gleichwertigkeit späterer Zielratenintegrale ableiten.
- Einen bestandenen einzelnen Ratenpunkt als persistentes Minimum ausgeben.
- Den Zusatzcheck als exakte Reproduktion der ursprünglichen Table 2 oder als neue
  absolute Hardwarekalibrierung bezeichnen.

## 10. Aktuelle TODOs

1. Lokale Scope-Detailmetadaten mit `archive_energy_checks.py` ergänzen und committen;
   danach Extrapolationsanteile aus den vorhandenen Audits prüfen.
2. Ursprüngliche Fenster-/Offset-/Interpolationsregeln gegen das Zusatzraster abgleichen;
   insbesondere 2 s / 9,4 kS/s und kurze Gemma3-4B/Tek-Fenster. Keine passende Rasterlage
   nachträglich anhand günstiger Ergebnisse auswählen.
3. Historischen Grund für FP16-IDs 2–14 dokumentieren. Die Wirkung von IDs 0/1 ist
   geprüft; der neue Check reproduziert den früher genannten Maximalfehler 1,071 % nicht.
4. Manuskript innerhalb der bestehenden Länge präzisieren; ursprüngliche Ergebnisse und
   Zusatzcheck nicht vermischen. Kein weiterer FP16-Hardware-Gegenlauf nötig.

Die operativen Punkte vom 01.10. (Backup der kontrollierten Sessions, Plotfreigabe auf
Twix, GPU-Nachtrag und finales Figurenset) bleiben separat nachzuverfolgen. Diese
Scope-Rückgabe bestätigt oder verneint deren Abschluss nicht.

