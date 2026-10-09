---
title: "Energy Paper – Current Consolidated Status"
project: "How Fast Is Fast Enough? Reference-Calibrated Energy Measurement for Edge-AI Inference"
status_date: "2026-10-01"
full_baseline: "../Energy_Paper_TIM_KnowledgeBase_2026-09-30.md"
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

## 1. Verbindliche Datengrundlage

- Die mehrwöchige Messkampagne wird nicht wiederholt.
- Der 4,418-TB-Offlinelauf ist abgeschlossen; keine erneute Gesamtrechnung.
- Common Reference / Same Trace trägt die Aussage zum isolierten Sampling- und Grid-Offset-Effekt.
- Direkte Samplerate-Sweeps sind separate physische Ausführungen und enthalten Session-,
  Reihenfolge-, Grundlast-, Temperatur-, Fenster- und Akquisitionseinflüsse.
- PSD/Common Reference bleibt ein eigener, unveränderter Zweig.

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

Nicht zulässig:

- historische Sweeps nachträglich auf null korrigieren;
- Vorlaufleistung als unabhängig verifizierten elektrischen Nullpunkt behandeln;
- VDD_IN als absolute Kalibrierreferenz ausgeben;
- aus GEMM FP16 universelle Gleichheit von 2 kS/s und 5 MS/s ableiten;
- Hailo Random Pattern mit pro Run ausgewählter Hüllenschwelle darstellen.

## 10. Aktuelle TODOs

1. Rohdatensicherung der zwei kontrollierten Sessions abschließen.
2. `tim_figures_v1.1.0` auf Twix ausführen und visuell freigeben.
3. GPU-Daten nach Eingang auswerten und Snapshot aktualisieren.
4. Finales Paper-Figurenset und Captions einfrieren.
5. Danach Manuskriptintegration; kein weiterer GEMM-FP16-Gegenlauf nötig.
