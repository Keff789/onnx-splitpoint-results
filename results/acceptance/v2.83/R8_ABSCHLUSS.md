# Abschlussbericht R8 – normale GUI-Produktintegration

Stand: 15.09.2026. Repository `${CONTROLLER_HOME}/ONNX-Splitpoint-Tool`, Version 2.83, Build `v2.83-r8-gui-product-integration`. Ausgangscommit `c5eb66eaa562728e9397a550570740d6a03e734d`; vorhandene R1–R7-Änderungen erhalten. Kein Commit/Push.

## Vier getrennte Abnahmezustände

| Achse | Ergebnis | Beleg und Grenze |
|---|---|---|
| Im Hauptrepo installiert | PASS | Source-/Installed-Verifier und reale Importpfade im Hauptrepo; kein gestarteter Kandidat. |
| Normale Config aktiviert | PASS | Stabile R6-Bytes normal gespeichert, Schema 14, Neustart ohne private Registry-/Collectorvariablen. |
| Lokal getestet | 678/678 Regressionen + 6/6 echte Tk-Tests PASS | Alle 647 R7-Knoten erhalten; neue R8- und echte Tk-Tests separat ausgewiesen. |
| Echter GUI-Smoke ausgeführt | TECHNISCH PASS, Qualität FAIL | Genau ein normaler Workflow: H8-MobileNet/b135, Full H8 + Full TRT + Split; drei Energiezeilen je 3/3. |

Der letzte Drain-/Fehlerstatusfix an Native-/SSH-Ausgabe entstand **nach** dem abgeschlossenen physischen Smoke. Dieser finale Code ist durch lokale reale Prozess-, Regressions- und Tk-Tests sowie den normalen GUI-Neustart geprüft. Es gab ausdrücklich keinen zweiten Hardwarelauf; die physische Abnahme wird nicht rückwirkend als Test dieser letzten Änderung ausgegeben.

## 1. Ursachen

1. Der R6-Erfolg band private Collectorbytes. Der ursprüngliche normale GUI-Lauf verwendete dagegen 342-mal den `.cargo/bin`-Collector; ohne `task_budget` griff die vorhandene Schutzpolicy dort nicht als neuer Produktdefault. R8 verbindet normalen Resolver, Snapshot und echten Spawn mit demselben absoluten Pfad und SHA256.
2. Standard selbst enthielt 1000/100/3. Zusätzlich verlor die Auflösung beim Ersetzen eines teilweise materialisierten Nativeblocks die fehlende `repetitions`-Angabe: Summary/effective meldete 1, der Native-Vertragsresolver ergänzte 3. Moduswechsel allein war damit keine ausreichende Reparatur.
3. SSH-Befehle und Native-JSON wurden in die Normalausgabe durchgereicht. Vollständige redigierte Diagnosen werden jetzt getrennt gespeichert. Eine späte Softwaregegenprüfung deckte zusätzlich auf, dass die bestehende 250-ms-Pipefrist bei langsamem Diagnoseschreiben bereits gepufferte Ausgabe abschneiden konnte. Endliche Queues werden nun vollständig geleert; geerbte offene Pipes bleiben begrenzt und melden rc70 statt falschem Erfolg.
4. Vollständige Energiezeilen, gültige logische Replikate und Collectorversuche sind unterschiedliche Mengen. Die Darstellung zeigt diese getrennt; historische fehlende Versuchszähler bleiben unbekannt. Die kleine Originalfixture reproduziert 24/183 gültige Replikate gegenüber 342/318 gestarteten/fehlgeschlagenen Versuchen.

## 2. Umsetzung und geänderte Dateien

39 Dateien gegenüber dem gesicherten R8-Start; vollständiges Inventar in `DIFF_INVENTAR_R8.json` und `R8_GEGEN_START.patch`.

| Paket | Wesentliche Dateien | Umsetzung |
|---|---|---|
| A Collector/Schutz | `energy/config.py`, `collector.py`, `task_budget.py`, `run_modes_cli.py`, `workflow/start_snapshot.py`, `workflow/runner.py`, GUI-Panel | Idempotente enge Installation mit Backup, vorhandenen Locks, atomaren Writes und Rechte-/ACL-Erhalt. Absolute Pfad-/Bytebindung bis Spawn, Empfangsdiagnose normal aktiv. Bestehende persistente Budgetpolicy bei fehlender Policy ergänzt; explizites Disable sichtbar. Full/Split/Probe benutzen den eingefrorenen Registrybestand. |
| B Modus | `run_modes.py`, `native_execution_contract.py`, `gui/profile_editor.py`, Default-YAML und Profilschema | Standard 100/10/1, Final 1000/100/3; Qualität/Bootstrap 500 bzw. 5000; Energie 3 separat. Schema 14 migriert nur das bekannte Standardtuple. Customwerte, Warmup 0 und Frozen Resume erhalten; wirkliche Editorvariablen und Save/Reload korrigiert. |
| C Ausgabe | `log_utils.py`, `remote/ssh_transport.py`, `benchmark/remote_run.py`, `native_progress.py`, Fullrunner samt Ressourcenmirror | Kurze Fortschritte/Ursachen/Diagnosepfade; separate vollständige redigierte Diagnosen, eindeutige Parallelziele; Modell/Setup/Backend/Rep/Frames. Ausgabe-Nachlauf vollständig; offene Pipe führt begrenzt zu Fehler-Cleanup. |
| D Achsen | `workflow/evidence_status.py`, Energie-Summaryskript samt Mirror, GUI-Panel | Runtime, Vertrag, Qualität, Energie, Cleanup und Abschluss getrennt; logische Wiederholungen und Collectorversuche nicht vermischt. |
| E Release/Tests | neue drei R8-Testdateien und skalare Fixture; Releaseidentity, Release-/Updater-/Smokemetadaten, AGENTS, README, `docs/ARBEITSSTAND.md`, Sourceindex | Version 2.83 erhalten, R8-Build, Regressionen/GUI-Matrix/negative Queueprüfung und Abschlussdokumentation. |

Erwartungsänderungen alter Tests betreffen die neue Build-ID und damit verknüpfte Smoke-/Updater-Metadaten. Zusätzlich wurde in den vorhandenen Terminalfixtures der bereits beabsichtigte synthetische Provenanzstub am zweiten artifacts-Einstieg vervollständigt (R8-TEST.2); echte Lifecycleprüfungen und ihre Zeitgrenzen bleiben gleich. Kein R7-Knoten wurde entfernt, keine wissenschaftliche Akzeptanzgrenze verändert. Der kumulative Diff `KUMULATIV_GEGEN_c5eb66e.patch` enthält auch neue textuelle R1–R8-Source-/Testdateien. Ein bereits vor R8 vorhandenes binäres ZIP-Testfixture wird gemäß Lieferverbot nur mit SHA256 im Inventar genannt, nicht als Binärpayload beigefügt.

## 3. Normale Installation und Konfiguration

Verwalteter Collector: `${CONTROLLER_HOME}/.onnx_splitpoint_tool/collectors/r6-reviewed/urecs-data-collector`.

SHA256: `913c3f745a71809d85c1e98f56d0ca3265bb5e5492ad2b72407f7ce9bd8c3a46`.

Quelle sind die unveränderten vorhandenen R6-Abnahmebytes, kein Rustbuild. Originalcollector erhalten. Exakte Installation/Migration, Backups, Vorher/Nachher, Rechte und Idempotenz: `config_installation.json`, `config_idempotence.json`, `CONFIG_DIFF_R8.json`. Der zweite Installationsaufruf war ohne Änderung erfolgreich.

Dauerhaft geändert wurden ausschließlich Collectorpfad/SHA in `hardware_setups.yaml` und `energy_config.yaml` sowie Schema 13→14 und Native-Standard 1000/100/3→100/10/1 in `run_modes.yaml`. Modus 0664 und vorhandene xattrs/ACLs blieben gleich. Kein bestehendes Profil oder altes Budget wurde ersetzt. Das zusätzliche normale Smokeprofil enthält nur die genehmigte Auswahl und das Smoke-Retrybudget 0; keine private technische Bindung.

Ursprüngliche GUI-Einstellungen wurden vor dem Smoke gesichert und nach regulärem Schließen byteidentisch wiederhergestellt. GUI-Neustart und ursprüngliche normale Profilauswahl: `GUI_RESTART_R8.json` / `gui_restart_r8.png`. Kein Sieben-Modell-Autostart. Die vorhandene `.venv` wurde verwendet; keine Abhängigkeiten wurden installiert oder aktualisiert und keine Venv-Konfiguration wurde geändert.

## 4. Softwaretests und tatsächliche Testgrenzen

| Prüfung | Ergebnis | Exitcode |
|---|---|---|
| regression | 678/678 PASS, 476.68s | 0 |
| real_tk | 6/6 PASS, 273.96s | 0 |
| focused_drain | 35/35 PASS, 8.19s | 0 |
| terminal_followup | 12/12 PASS, 53.86s | 0 |

Zwei vorherige Gesamtprüfungen: jeweils674 PASS/4 FAIL an der Zehn-Sekunden-Testschranke vorhandener Abschlussfixtures. Der beabsichtigte Provenanzstub verfehlte den artifacts-Einstieg; dort verursachten992 JSON-Ladevorgänge des gewachsenen3MB-Testcaches Verzögerung vor den Stages. Nach Vervollständigung des Stubs bestanden12/12 Terminaltests mit demselben Cache und anschließend die komplette678-Auswahl. Produktlogik und Testzeitgrenzen blieben unverändert. Beleg: TEST_FIXTURE_BELEG_R8.json.

Exakte Shellkommandos, Exitcodes, vollständige gesammelte Testknoten und Importpfade: `TEST_RESULTS_R8.json`, `TEST_HISTORY_R8.json`, `acceptance_r8_complete.json`. JUnit und Logs sind beigefügt. Frühere rote, übersprungene oder abgebrochene Versuche bleiben dokumentiert und zählen nicht als Abschluss-PASS.

- Portable neue Produktregressionen verwenden skalare Originalbelege und kontrollierte lokale Prozesse. Collector-/SSH-Hardwareblätter sind dort ersetzt; Auflösung, Budget, Prozesssteuerung und Berichtszähler bleiben echt. Die bewahrte647-Knoten-R7-Auswahl enthält ihre vorhandenen historischen Archivfixtures; diese private Abhängigkeit ist nicht Grundlage der normalen GUI-Integration.
- Die echte Tk-Matrix verwendet normale zentrale Konfiguration, tatsächliche Editor-/Panelvariablen und Callbacks, Standard→Final→Standard, Energie aus/an, Full/Split, Save/Reload, Custom217/0/2, Frozen1000/100/3, veraltete Summary, fehlenden/falschen Collector und persistenten Quellenstopp. Nur Dialogantworten und lokale Mess-/Hardwareprozessfixtures sind gesteuert. Full/Split/Probe teilen den echten Budgetpfad; der Probe-Beleg deckt den Collector-/Budget-Leaf ab, nicht einen neu durchlaufenen vollständigen Probe-Coordinator.
- Der zusätzliche echte GUI-Queue-/CPU-Prozess-/Report-/Terminaltest ist ausdrücklich **negativ**: Der vorhandene Produktscope verlangt ein Accelerator-Setup; das CPU-only-Minimalprofil erreicht technische FAILED-Projektion und ordentlichen Artefaktabschluss. Kein Resolver-/Queue-/Runner-/Parser-Ersatz, keine physische Hardware. Der beobachtende Popen-Wrapper ruft den echten Prozess unverändert auf. Dieser Test ist kein erfolgreicher Nativeworkflow; der positive normale Workflowbeleg ist der reale H8-Smoke.
- `--noconftest` erhält für die separate Tk-Prüfung normales HOME/Xauthority. Die anfänglichen drei SKIPs wegen isoliertem Test-HOME sind nicht als Abnahme gewertet.
- Der Source-Releaseindex wurde aus einer externen allowlist-basierten Dateiinventur erstellt, damit vorhandene Runtime-Symlinks nicht entfernt werden mussten. Diese Inventur wurde nicht installiert oder als Import-/Testkandidat verwendet. Abschließende Installedprüfung und sämtliche Produktimports beziehen sich auf das Hauptrepo.

## 5. Einziger tatsächlicher GUI-/Hardwarelauf

Einstieg: **`./start_gui.sh` im Hauptrepo**, echte GUI-Profilwahl und genau einmal Start. Keine Collector-/Registry-Umgebungsüberschreibung, keine Queue-/Hardware-/Transportmocks.

- Profil: `profiles/r8_gui_smoke_mobilenet_h8.yaml`, eigene normale Kopie mit `follow_tool_config:true`.
- Modell: MobileNetV3Large; Split b135; Setup `orin_nx_hailo8_01`; Full H8, setup-lokales Full TensorRT, Split H8→TRT.
- Budget: Standard 100/10/1, Qualität/Bootstrap höchstens 500, Energie 3 je Zeile, maximal 9 Starts, Retry 0, optionale Methodenvergleichsprobe über normales Feld aus.
- Startklick 15.09.2026 20:04:14; terminal 20:17:15, ca. 13 Minuten und damit unter 30 Minuten. Runanlage 20:04:53.
- Run: `gui_results/r8_gui_smoke_mobilenet_h8_20260915_200453` unter CODEX_OUTPUT.
- Warmmatrix 4 HIT, keine MISS/UNKNOWN, kein Compilerdispatch. Force Rebuild aus; keine gelöschten Artefakte.

| Ergebnisachse | Tatsächlicher Befund |
|---|---|
| Runtime | vollständig, technische Statusachseok |
| Output-/semantischer Vertrag | vollständig; drei Nativezeilenok, jeweils100/10 und 1/1 gültige Performancewiederholung |
| Qualität | FAIL: zwei von vier zentralen Auswertungen außerhalb unveränderter Grenzen; keine fehlende Auswertung |
| Energie | drei von drei Zeilen vollständig verifiziert, je 3/3; insgesamt 9/9 gültige logische Replikate |
| Collector/Quelle | neun tatsächliche Starts, null fehlgeschlagene Versuche, keine Retries/Transportfehler; neun bestätigte Protokollenden und Source-close-Belege |
| Cleanup/Abschluss | regulärer terminaler Workflow, Artefaktabschluss PASS ohne Verifikationsfehler |
| GUI | echter Dialog **„Abgeschlossen mit Qualitätswarnungen“**, Screenshot `gui_terminal_r8.png` |

Exakte erzeugte Collectorargumente, Snapshot-/Bytebindung, Cachebelege und Statusdaten: `HARDWARE_RESULTS_R8.json` sowie echtes `GUI_SMOKE_DEBUG_R8.zip` (Produktdebugexport). Die kurzen Aufnahmen bleiben Screening, keine finale Langzeitenergie oder wissenschaftliche Energie-Freigabe. Das konfigurierte innere Lastsoll bleibt 1 s; der unveränderte vorhandene Collectorvertrag enthält zusätzlich Vor-/Nachlauf und Vorbereitung (z.B. reale Argumente `-d=17s -b=5s -e=5s`). Das ist keine R8-Verlängerung des Messvertrags.

Normale zusätzliche eigene Produktwrites erfolgten unter `~/Models/EvaluationRuns/RemoteBenchmarkRuns` nur in frischen r8_gui_smoke-Läufen sowie eigenen normalen Lock-/Indexeinträgen. Originalruns wurden nicht verändert. Rohdaten bleiben im eigenen Run; die Lieferung enthält keine Modelle, Binaries oder großen Roharrays.

Der zunächst beendete Launcher-Shellprozess hatte Exit 1 nach kontrolliertem Interrupt; das war **kein** Workflowfehler und kein Beleg des GUI-Fensterschlusses. Anschließend wurden ausschließlich die eigenen fertigen Fenster regulär geschlossen und ihre ursprünglichen Einstellungen wiederhergestellt. Der Workflowstatus stammt aus den abgeschlossenen Produktreports, nicht aus dem Shellstatus.

## 6. Bewusst nicht ausgeführt / verbleibende Grenzen

- Kein zweiter Hardware-Smoke nach dem späten Drainfix: im Auftrag maximal ein Lauf. Diese Änderung ist lokal realprozess-/Tk-geprüft, physisch nicht erneut geprüft.
- Kein Full-/Final-/Nachtlauf, keine Langzeitenergie, kein Ranking mit mehreren Splits.
- Keine H10-/DeepX-Hardwareabnahme oder neue Numerikdiagnose. H10-Bindingresolver und offene YOLO26-Nulloutputs bleiben getrennt; beide alten DeepX-XYXY-Fälle bleiben offen.
- Keine Accuracyoptimierung, keine geänderten Margen, Seeds, Datensatz-/Bildauswahl oder Compilerrezepte zur Verbesserung eines Ergebnisses.
- R8-GUI-CPU.1: positiver lokaler CPU-only-Full/Split-Workflow durch vorhandenen physischen Scope blockiert; als negative GUI-Endzustandsprüfung dokumentiert, nicht durch Architekturumbau umgangen.
- Kein neuer vollständiger Window-Probe-Coordinator-E2E-Test; gemeinsamer Collector-/Budget-/Quellenstopppfad lokal geprüft, optionale physische Probe im Smoke ausdrücklich aus.
- Historische Transport-/Endpaketursachen bleiben offen. Der heutige Erfolg erklärt nicht rückwirkend frühere Fehler und nimmt nicht alle drei physischen Quellen ab.

## 7. Git, Integrität und Lieferung

Kumulativer `git diff --stat`: **61 files changed, 2158 insertions(+), 754 deletions(-)**. `git status --short` enthält 86 Einträge einschließlich der absichtlich vorhandenen R1–R7-Änderungen und untracked Fixtureverzeichnisse. R8 allein: 39 geänderte/neue Dateien.

Exakter Endstatus: `git_status_after.txt`; `git diff --stat`: `git_diff_stat_after.txt`. Hauptcommit unverändert. Die uncommitted R1–R7-Dateien wurden nicht als R8-Neuänderungen ausgegeben. `R8_GEGEN_START.patch` wurde mit `git apply --check` gegen die gesicherte Baseline geprüft.

Die Ergebnis-ZIP enthält Bericht, fortgeschriebenen Arbeitsstand, Test-/Config-/Importnachweise, beide Diffs, JUnit/Logs, GUI-Screenshots und das kleine echte Debugpaket. `ZIP_INHALT_R8.json` protokolliert Inhalt, Größen und SHA256; CRC-/Pfad-/Suffixprüfung erfolgreich. Das unveränderte Collectorbinary selbst wird nicht mitgeliefert.

## 8. Empfohlener nächster Schritt

Die normale GUI mit dem ursprünglichen CompleteSetDev-Profil verwenden und vor einem gewünschten neuen Lauf die aufgelöste Summary prüfen. Es wurde kein weiterer Lauf eingeplant oder automatisch gestartet. Qualitätsarbeit, H10-/DeepX-Numerik und Langzeitenergie bleiben eigene spätere Aufträge.
