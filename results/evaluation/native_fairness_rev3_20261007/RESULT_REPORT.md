Revision 3 – begrenzter wissenschaftlicher Deltaabschluss
Stand: 2026-10-13T04:12:53.856198+00:00. Messungen, zentrale Übernahme und Datenarchiv abgeschlossen. Kompakte Reviewerlieferung verifiziert; Ergebnis-Git wird aktualisiert.

A) Wiederverwendung und Merge
340 vollständige Queuekohorten und 1.022 gültige alte Slots unverändert erhalten. Ein Teilpunkt besaß zwei gültige Slots. 55 Native-Punkte in Phase A normal importiert/projiziert, ohne sie neu aufzunehmen.

B) Tatsächliche Aufnahmen
256 neue gültige Slots auf 86 zuvor unvollständigen Punkten; 260 physische Starts, vier erhaltene Paketverlust-Fehlversuche und deren gezielte normale Retries. Ein separater Preflight scheiterte vor einem Sensorstart. Keine neue Performancekohorte und keine neue N5000-Auswertung.
DeepX-ResNet b119: ausschließlich repeat:1 ergänzt; repeat:0 und repeat:2 unverändert erhalten.
Kumulativ: 426 vollständige Punkte, 1.278 gültige Slots, 1.424 Starts, 146 fehlgeschlagene Starts, 0 laufende Starts, 0 fehlende Slots. Ein alter unterbrochener ungültiger Versuch wurde normal als fehlgeschlagen abgeschlossen; kein historischer Quellenabschluss wurde erfunden.

Regime | Setup | Modell | Punkte | gültig neu | Starts neu | fehlgeschlagen neu | Rest
generic_completed | orin_nx_hailo10_01 | mobilenet_v3_large | 17 | 51 | 51 | 0 | 0
generic_completed | orin_nx_hailo10_01 | regnet_x_1_6gf | 20 | 60 | 61 | 1 | 0
generic_completed | orin_nx_hailo10_01 | resnet50 | 19 | 57 | 59 | 2 | 0
generic_completed | orin_nx_hailo10_01 | yolo11l | 3 | 9 | 10 | 1 | 0
generic_completed | orin_nx_hailo10_01 | yolo26m | 3 | 9 | 9 | 0 | 0
generic_completed | orin_nx_hailo10_01 | yolo26s | 3 | 9 | 9 | 0 | 0
native | orin_nx_deepx_m1_01 | resnet50 | 3 | 7 | 7 | 0 | 0
native | orin_nx_hailo10_01 | resnet50 | 3 | 9 | 9 | 0 | 0
native | orin_nx_hailo10_01 | yolo11l | 5 | 15 | 15 | 0 | 0
native | orin_nx_hailo10_01 | yolo26m | 5 | 15 | 15 | 0 | 0
native | orin_nx_hailo10_01 | yolov7_paper | 5 | 15 | 15 | 0 | 0

C) Zentrale Ergebnisse
450 ursprüngliche Zeilen erhalten: 246 Native und 204 Generic. Alle 426 Queuepunkte normal energiegebunden; zusätzlich elf bestehende Energiepunkte außerhalb der Queue. Native 233 und Generic 204 energiezugelassen. Die 13 anderen Grenzfälle bleiben als zehn gesonderte Native-YOLO26s-Vergleichskontexte und drei historische H10-Classifier-Screenings sichtbar.
Performance unverändert: 240 Native-Dreierkohorten und sechs historische Einzelbeobachtungen; 204 Generic-Dreierkohorten. Normale Qualitätsbindungen: 244 Native und 204 Generic. Negative Qualitätsbefunde bleiben 26 Native und 17 Generic accuracy_loss.
Normale Performance-Claimflags: 235 Native und 204 Generic. Normale Native-Energiepaare: 340 claim_comparable, 56 ineligible_or_contract_mismatch. Energiezulassung, Qualitätsbefund und Vergleichsstatus bleiben getrennte Achsen; dies ist kein pauschaler Überlegenheitsclaim.
Energie-Lesetabelle in mJ/Task; ungerundete Joule-/Taskwerte und ursprüngliche Aggregation bleiben in Current. Rohenergie, normalisierte Vergleichsenergie und mean(N/E) bleiben getrennt.
Die diagnostische 21-Zellen-Abnahme bleibt separat. Die deskriptive YOLOv7/DeepX-FPS-Abweichung von −2,37 % bleibt ihr historischer Einzelbefund.

D) Archiv
Datenarchiv verifiziert am bestehenden Sprite-Ziel archive:revision3 (echter SSHFS-Mount). 614 alte Checkpoint-Gruppen / 141.648 Einträge unverändert erhalten; zwei zusätzlich vorhandene normale Receipts mit 4.175 Dateien ohne erneute Kopie eingebunden. Neu übertragen: 161 Gruppen / 47,765 Dateien / 15,415,013,057 Bytes. Gemeinsamer Datencheckpoint: revision3:/archive_publication/checkpoint_20261013T044820Z, 777 gebundene Gruppen / 193,588 Dateieinträge. Manifest-SHA256: 94118442b70a435938e48bdc40d3a05a7930abf840dd62d8be05872e91842ac5.
Alle ausgewählten Messruns, Fehlversuche und direkten aktuellen Import-/Qualitätsreferenzen gedeckt; historische und aktuelle Fassungen bleiben getrennt hashgebunden. ARCHIVE_COMPLETION_RECEIPT.json und die normalen archive_receipts belegen die tatsächlichen Zielhashprüfungen. Kompakte Reviewerlieferung: revision3:/review_package/delta_closeout_20261013/REV3_DELTA_ABSCHLUSS_20261013.zip (3,950,469 Bytes), SHA256 301070f953ce51e61ad37b586ef0a61427ecb17a7a34bbc9640509d450c37ede; 204 enthaltene Originaldateien bytegeprüft und Paket normal archiviert. Dies ist eine Metadatenlieferung; Rohdaten bleiben im vollständigen Datenarchiv. Der abschließende Metadatencheckpoint bindet zusätzlich Ergebnis-Git und Lieferreceipt.

E) Bedienung und Software
Tatsächlich benutzter normaler Batch-Resumeaufruf:
source:controller/.venv/bin/python -I -B revision3:/operations/token_saving_batch_20261009/batch.py resume
Der Batch ruft die normale installierte complete-evaluation-Schnittstelle auf; die exakten Originalparents und wissenschaftlichen Produktionsbindungen stehen in SCIENTIFIC_DELTA_PROFILE.json. Drei gültige Repeats, 60-s-Lastfenster, bestehende Warmup-/Workunit-/Kalibrierungs-/Sampling-/Drainregeln, Force-Rebuild false.
Rein lesender Statusaufruf:
source:controller/.venv/bin/python -I -B revision3:/operations/token_saving_batch_20261009/batch.py status
Installierte Version 2.94.0 und Remote main: db729b9fcde00e4bcadf9200d43282977d7bf1cc. Erforderliche gezielte Recovery-/Importkorrekturen sind getestet, regulär committed, gepusht und installiert. Kein neuer Release. Datenhelperkorrekturen samt Vorfassungen und Reviews sind separat dokumentiert.

Belege: revision3:/operations/token_saving_batch_20261009/delta_abschluss_20261012
DELTA_RESULT_TABLE.csv: alle 450 Ergebniszeilen; DELTA_CENTRAL_RESULTS.json: Werte/Quellen/Qualität; DELTA_JOURNAL_BALANCE.json und FINAL_DELTA_COUNTER_REVIEW.json: sämtliche Slot-/Attemptabgleiche.
Nach Archiv- und Ergebnis-Git-Abschluss endet dieser Auftrag. Keine weitere Messgruppe freigegeben.
