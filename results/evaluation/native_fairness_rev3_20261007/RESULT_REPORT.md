# Revision 3 – Ergebnisbericht (laufende Ausführung)

Stand: 2026-10-07T12:23:12.971674+00:00

**Noch kein Abschlussbericht.** Audit und fokussierte Korrekturen sind umgesetzt; die erforderlichen Nachmessungen und normalen Quality-/Energiebindungen werden weitergeführt. Fehlende aktuelle Messungen bleiben sichtbar. Keine Datenlöschung, Verschiebung, Retention oder Speicherbereinigung wurde durchgeführt. Der historische Sprite-Zweig bleibt unverändert.

## Lesende Archivprüfung und historische Generic-Nutzung

Der tatsächlich gemountete Sprite-Bestand wurde anhand seiner Manifeste, aller 246 Native-Commandbindungen und ausgewählter benötigter tatsächlicher Artefakte geprüft. Das ist keine Vollhashprüfung sämtlicher Archivpayloads. Das vorhandene historische Review-ZIP bestand unabhängig den mitgelieferten Prüfer: 6.281 Payloadhashes, 27 Splitrepeats, 18 Fullrepeats und drei getrennte Fullkontrollen. Prüfgrenzen und Zugriffszuordnungen stehen in `ARCHIVE_VERIFICATION.json` und `INPUT_AVAILABILITY.json`.

Die Nutzungstabelle `LEGACY_GENERIC_USAGE.csv` unterscheidet 204 historische Completed-Punkte von 20 Raw-Referenzzeilen und weiteren Verweisen. Der allgemeine Streaming-/Multi-Tensor-Pfad einschließlich `generic`, `native_fifo` und `NativeTRTSession` wird weiter benötigt. Entfernt wurden ausschließlich 197 nachweislich unerreichbare Zeilen aus drei DeepX-P2-Duplikaten; die ursprünglichen Quellen und der AST-Nachweis bleiben erhalten. Die reproduzierte 24/23-Queueprobe belegt keine bestimmte Fehlergröße der historischen 1.000-Task-Läufe.

## Code und gezielte Abnahme

Verlustfreier Queueabschluss und tatsächliche Completionzählung; eindeutige DeepX-Eingabedomänen ohne Boundary-Wertecache; keine standardmäßige label-/scoregetriebene P2-Mappingwahl; gemeinsame kanonische Timinginputs; funktionale Completion im Timer, Nachweisarbeit und strikter eigener Sentinel außerhalb des Performancetimers. NaN/Inf in verworfenen Kandidaten bleiben Fehler. YOLO11/26-Formate verwenden ihre eigenen gebundenen Decoder. Der Student-t-Fallback verwendet die vorhandene geprüfte Quantilroutine; die 246 historischen Collector-A/B-Intervalle waren bereits korrekt.

Die fokussierten Testläufe, tatsächlichen gespeicherten Outputs und negativen Fälle sind getrennt in den Abnahmereceipts dokumentiert; überlappende Testläufe werden nicht zu einer erfundenen Gesamtsumme addiert. Keine allgemeine GUI-Abnahme, keine Treiber-/Clock-/Firmwareänderung, kein Modell-/Engine-Neubau.

Originalfreeze: 223 Dateien in `IMPLEMENTATION_FREEZE.json`. Spätere eng begrenzte Paket-/Deployment-Ergänzungen sind separat gehasht und AST-abgegrenzt. Der Native-Energiepfadfix für DX/H10 ist mit 109 fokussierten Tests und unverändertem Nichtenergie-AST lokal abgenommen, aber noch nicht deployt; die ursprünglichen Quellen und Messungen bleiben separat erhalten.

## Aktuelle Beobachtungen

15 priorisierte YOLOv7-Native-Punkte besitzen je drei getrennte Prozesse mit 100 Warmups und 1.000 fertigen Tasks. H10-Hailo-Full mit acht tatsächlich offenen SDK-Requests wurde nach vorab festgelegter Regel ausgewählt; die Ein-Slot-Kontrolle bleibt getrennt. Die Tabelle zeigt technische Beobachtungen, noch keine pauschale wissenschaftliche Freigabe.

| Setup | Backend/Fall | FPS-Median | Drei Einzelwerte |
|---|---|---:|---|
| DeepX | deepx_to_trt/b009 | 35.472676 | 35.724656, 35.289224, 35.472676 |
| H10 | hailo10h_to_trt/b009 | 51.388163 | 51.395949, 51.388163, 51.351127 |
| H8 | hailo8_to_trt/b009 | 44.958257 | 44.958257, 44.806189, 45.065791 |
| DeepX | native_full_deepx/full | 23.187602 | 23.113314, 23.418438, 23.187602 |
| H10 | native_full_hailo10h/full | 33.230241 | 33.230345, 33.230241, 33.229521 |
| H8 | native_full_hailo8/full | 32.071261 | 32.050399, 32.148957, 32.071261 |
| H8 | native_full_tensorrt/full | 53.055325 | 53.020658, 53.055325, 53.113827 |
| H10 | native_full_tensorrt/full | 52.829333 | 52.854182, 52.593198, 52.829333 |
| DeepX | native_full_tensorrt/full | 48.445944 | 48.445944, 48.607604, 48.443481 |
| DeepX | deepx_to_trt/b044 | 49.000352 | 49.181253, 48.893354, 49.000352 |
| DeepX | deepx_to_trt/b066 | 30.196948 | 30.330966, 30.196948, 29.952035 |
| H10 | hailo10h_to_trt/b044 | 69.780112 | 69.283451, 69.780112, 69.902457 |
| H10 | hailo10h_to_trt/b066 | 53.082615 | 53.050563, 53.082615, 53.390764 |
| H8 | hailo8_to_trt/b044 | 50.379765 | 50.357437, 50.379765, 50.509013 |
| H8 | hailo8_to_trt/b066 | 112.775574 | 112.468341, 112.775574, 112.798660 |

Alle neun ersten Generic-Paare sind abgeschlossen und bestehen die normalen technischen Paarprüfungen. Ihre Einzelrepeats, echten Prozessidentitäten, Eingaben und Gates stehen in `current_results/generic_current.json` und `generic_repeats.csv`. Eine technische Paarfreigabe ersetzt keinen Qualitytransfer. Request-Latenz wurde im vorhandenen Generic-Completed-Einstieg nicht erfasst und wird nicht aus 1/FPS erfunden.

## Energie

Die erste b009-Gruppe endete regulär mit belegter Ressourcenfreigabe: zehn physische Starts, neun sensorisch gültige logische Wiederholungen, ein verworfener H10-Transportversuch. Die normale Ergebnisprüfung lehnt DX/H10 ab: ihr Energiezweig erzwingt strict statt der gemessenen Fast-Completion und liefert keine passenden frischen Completionmarker. Diese Daten sind diagnostische Aufnahmen, keine Joulewerte der neuen Performance. Der kleinste belegte Energiepfadfix wird gezielt abgenommen.

H8 b009 besteht die normale dreifache Energie-/Completionprüfung und den späteren Quality-Join. Die ursprüngliche Erfassungspolicy bleibt jedoch diagnostisch und erlaubt keine nachträgliche finale Claim-Promotion. Tatsächliche Counts 2.712/2.706/2.707, kalibrierte Energien 1.612,698841/1.612,649660/1.616,417421 J, Mittel der E/N-Werte 0,595910431 J/Task. Sensorintervalle, tatsächliche Arbeitszeiten, E/N und N/E sowie Student-t-Intervalle stehen in `current_results/energy_acquisitions.json`. Keine alten Watt-/Joulewerte werden auf neue FPS übertragen.

Drei qualifizierte Full-Punkte wurden inzwischen mit je drei 60-s-Repeats abgeschlossen und über die korrigierten regulären Consumer `collect_native_energy` und `scientific_energy_rows` zugelassen. Der Reportfix verhindert, dass ein diagnostisches A/B-Shadow-Flag fälschlich den Primärwert überschreibt; explizit diagnostische alte Erfassungen bleiben ausgeschlossen. Die aktuelle Projektion prüft genaue Performance-Summarys, alle tatsächlichen Prozess-/Rohreportbindungen, Energieaggregate und beobachtete Completionmodi.

| Setup/Full | Rohes FS-Mittel E/N (J/Task) | Mittel N/E (Tasks/J) | Repeats |
|---|---:|---:|---:|
| DeepX Vendor | 0,689874383 | 1,449540153 | 3 |
| H8 Vendor | 0,549843563 | 1,818699641 | 3 |
| DeepX TRT | 0,613181286 | 1,630862555 | 3 |

Die vorhandene normale TRT-Vergleichskorrektur bleibt separat: 0,561263320 J/Task und 1,781724572 Tasks/J nach gebundenem Accelerator-Idleabzug. Sie ersetzt die rohe Systemenergie nicht. Tasks/J ist stets das Mittel der drei N/E-Werte, nicht der Kehrwert des mittleren E/N. H8 behält unabhängig vom Energie-PASS seine Qualityklasse `accuracy_loss`. `current_results/ENERGY_PROJECTION_VERIFICATION.json` dokumentiert positive und negative exakte Zuordnungsprüfungen.

Der anschließende erste H10-TRT-Energieversuch meldete Silence-Timeout ohne bestätigtes Protokollende. Die normale physische Quarantäne bleibt bestehen; H8-TRT wurde deshalb vor Collectorstart abgewiesen. Eigene Messprozesse sind laut terminalem Besitznachweis beendet. Der konkrete reguläre H10-Fortsetzungsplan liegt unter `operations/recovery_full_h10_20261007`; die Schutzfunktion fordert eine ausdrückliche Einzelfreigabe nach diesem STOP, die angefragt und noch offen ist. Erfolgreiche Full-Repeats werden nicht wiederholt. Ein isolierter Nullstart-Recoveryfix wird zusätzlich gegen eine vollständige vierteilige Fallidentität geprüft; er setzt keine Quarantäne oder Zähler zurück.

Die fehlende Generic-Completed-Daueraufnahme wird als begrenzte Erweiterung desselben Executors und der normalen Collector-/Reportpfade implementiert. Die ursprüngliche Lücke bleibt in `generic_final/ENERGY_GAP.json` dokumentiert. Bisherige neue Prüfungen nutzen synthetische CPU-/Sensorfixtures und sind ausdrücklich keine Hardwareenergie. Wegen geänderter gemeinsamer Workersteuerung werden die neun Generic-Punkte nach dem endgültigen Bundle einmal neu bestätigt; weitere 195 starten erst mit diesem Stand. Persistente STOPs, Startketten und Budgets bleiben erhalten.

## Nachmessumfang und offene Arbeiten

Die belegte Matrix enthält 237 betroffene Native-Performancepunkte und neun verifizierte Performancewiederverwendungen; drei zusätzliche DeepX-Vendor-Fulls benötigen nur neue Energie. Die Änderung tatsächlicher Prepared-Raster betrifft 168 Klassifikations-Splits; die zentrale 5.000-Bilder-Quality verwendet bereits kanonische Inputs. Neun TRT-Klassifikations-Fulls benötigen wegen eines zusätzlichen Timed-Dispatch neue Performance. Neun Hailo-/DeepX-Klassifikations-Fulls besitzen diesen Ausführungs-/Artefaktgleichheitsbeleg und werden unter Erhalt ihres ursprünglichen Messprotokolls wiederverwendet. Die aktuelle Sicht enthält 15 neue Native-Punkte, neun Wiederverwendungen und 222 noch fehlende neue Performancepunkte.

Offen sind die verbleibenden Native-/Generic-Messungen, passende erlaubte Energie, finale normale Quality-/Provenienzbindungen, alle abhängigen Rankings und Abbildungen, das Ergebnis-Git-/Knowledgebase-Update, die private LaTeX-Ableitung und das kompakte selbstprüfbare Reviewpaket. Aktuelle Statuswerte und exakt nächste zulässige Befehle stehen in `STATUS.md`; die 450-Zeilen-Fairnessmatrix ist `FAIRNESS_MATRIX.csv`.

Die bestehende relative Qualityregel von fünf Prozent bleibt unverändert. 1.000 Tasks desselben Bildes sind keine 1.000 unterschiedlichen Bilder oder unabhängigen Sitzungen. Kleine beobachtete Vorteile werden nicht als statistisch bewiesene Überlegenheit bezeichnet.

## Neue Archivierung

Alle abgeschlossenen Native-Performancegruppen, die drei bisherigen Energiegruppen und die neun Generic-Punkte einschließlich Fehlversuchen sind im neuen Zweig `diss_results_native_fairness_rev3_20261007` kopiert und per Ziel-/Quellhash geprüft. Originale wurden nicht verschoben oder gelöscht. Einzelne Kopierreceipts stehen in `archive_receipts/`. Große historische Modell-/Engine-/Sensorpayloads bleiben außerhalb des öffentlichen Ergebnis-Gits.
