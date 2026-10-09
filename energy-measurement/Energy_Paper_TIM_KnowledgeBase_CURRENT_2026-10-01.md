---
title: "Energy Paper – Current Consolidated Status"
project: "How Fast Is Fast Enough? Reference-Calibrated Energy Measurement for Edge-AI Inference"
status_date: "2026-10-09"
canonical_parma_version: "0.15.1"
latest_review: "knowledgebase/2026-10-09-parma-v0151.md"
full_baseline: "Energy_Paper_TIM_KnowledgeBase_2026-09-30.md"
language: "de"
---

# Energy Paper — aktueller Einstieg

**Verbindlicher PARMA-Stand: v0.15.1.** Die Entscheidungen aus der Manuskriptrevision haben Vorrang vor den älteren Empfehlungen zur Paper-Auswahl und -Darstellung.

- [Aktuelle Manuskriptentscheidungen und PARMA/TIM-Abgrenzung](knowledgebase/2026-10-09-parma-v0151.md)
- [Öffentliches Figure-5-Artefakt: vollständige Paare, Quantile und Generator](publications/parma-v0.15.1/README.md)
- [Scope-/FP16-Robustheitsprüfung](knowledgebase/2026-10-09-offline-robustness.md)
- [Vorheriger operativer Einstieg, unverändert archiviert](knowledgebase/2026-10-09-before-parma-freeze.md)
- [Langfassung der Messmethoden und operativen Pfade](Energy_Paper_TIM_KnowledgeBase_2026-09-30.md)

## Paper und Ergebnisbasis

PARMA bleibt Jetson-only; Hailo und die breitere Instrumentierungsstudie bleiben für TIM. Die Hauptauswertung nutzt native Scope-Rekonstruktion und alle 15 FP16-Aufzeichnungen. Die Revisionsgeschichte steht nicht im Haupttext. RQ3 verbindet Benchmarkdauer und reale Messpfade.

Die bisherige Tabelle 5 ist jetzt eine Median-Punktabbildung. Vollständige Q05/Q95 und die 315 Paarvergleiche aus 105 Ausführungen sind im Artefakt erhalten. Variable YOLO bleibt als Kontrastfall. Eigene Sensorfenster, Skalierungen und unterschiedliche elektrische Grenzen bleiben offengelegt; kein intrinsisches Genauigkeitsranking.

## Abgeschlossen / getrennt nachzuverfolgen

Die Scope-Detailarchivierung wurde mit Commit 9b4208c97420b1621a14b7dc91f051985e65e6f5 abgeschlossen. Keine erneute Rohdaten-Gesamtrechnung und kein neuer Messlauf für diese Manuskriptrevision. Frühere Angaben, die Detailarchivierung sei noch auszuführen, sind überholt.

Rohdatenbackup, GPU-Nachtrag, ungeklärte historische Implementierungsprovenienz und das TIM-Programm bleiben eigenständige Aufgaben. Ein vorbereitetes Zitier-/Zenodo-Metadatenpaket ist keine vergebene DOI. Publikationsstatus und tatsächliche Release-Links stehen im jeweiligen Artefakt-README; keine Proceedings-Annahme oder Artifact-Evaluation behaupten.
