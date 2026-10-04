# ONNX Splitpoint Tool – Knowledge Base

> **Kanonischer Pfad: `docs/KNOWLEDGEBASE.md`.** Diese Datei wird fortlaufend
> aktualisiert; ihre Historie liegt in Git. Keine neue Datei je Dokumentrevision.
> Toolversionen, Run-IDs und historische Revisionsangaben im Text bleiben erhalten,
> damit sich Befunde weiterhin dem richtigen Stand zuordnen lassen.
>
> **Evidenzstichtag: 04.10.2026, gemeinsame Auswertung und Quellabschluss.**
> Hauptkampagne, 192er-Completion und YOLO-Augmentierung sind technisch vollständig.
> Die gemeinsame lokale Ableitung führt Originalidentitäten und negative Ergebnisse
> fort. Aktuelle Aufgaben stehen in §12, die Übergabe in §16 und der Abschluss in §23.
> Frühere Resume-/Messanweisungen sind datierte Historie, kein aktueller Auftrag.

## Aktueller Stand

| Menge / Gegenstand | Live geprüfter Stand am 04.10.2026 |
|---|---|
| Maßgebliche Quellen | ursprüngliche Hauptkampagne; korrigierte Basisableitung vom 02.10.; separate 192er-Completion; finale YOLO-Zusatzkohorte mit Abschluss **17:54:23 CEST, Exitcode 0** |
| Historische Generic-Performance, Endpunkte getrennt | **527** Hauptmesszeilen + **37** negative Builds + **24** Policyausschlüsse = **588** Sollfälle; zwölf kurze YOLO-Vorläufe sind separat inventarisiert |
| Quality | **560** eindeutige N5000/B1000-Ergebnisse: **521 reference_close / 39 accuracy_loss**; keine neue Statistikrechnung |
| Native-Performance | **246** Fälle = **204 Splits + 42 Fullbaselines**, **738** gültige Wiederholungen; ursprüngliche **228 not_supported** bleiben terminal |
| Generic-Completed-Task | **204** Fälle = 192 + 12; **612** Wiederholungen und **612.000** gemessene Abschlüsse; Prepared Input bis tatsächliche Task-Completion |
| Native-FS-Energie | **246** vollständige Zeilen, **738** gültige Replikate; Primärenergie ohne Idleabzug; 21 vorhandene TRT-Full-Zusatznormalisierungen getrennt |
| Physische Aufnahmehistorie | Basis **705 = 702 gültig + 3 abgeschlossen ungültig**; YOLO **42 = 36 gültig + 4 abgeschlossen ungültig + 2 unbestätigt unterbrochen**; ein unabhängiger GUI-Funktionstest separat |
| YOLO-Abdeckung | zwölf Modell-/Setupgruppen mit mindestens drei technisch vergleichbaren Grenzen; neun ungemessene Standbyidentitäten sind keine offenen Pflichtfälle |
| Auswertungsreparaturen | F01/F02/F03/F05/F06 lokal abgeleitet; F04 durch separat beauftragte 192er-Completion und zwölf Zusatzfälle ergänzt. Primärdaten und historische Negativprojektionen bleiben erhalten |
| Rollen und Grenzen | Zusatzkohorte post-planned/development; `runtime_conditions_comparable=false` bleibt bestehen. 204 technische Paarungen, 201 nach bestehendem Qualitytransfergate, 0 Claims. Technische Gleichendpunktprüfung ist keine kausale oder Hold-out-Freigabe |
| Toolrelease | [Toolrelease v2.92.0](https://github.com/Keff789/ONNX-Splitpoint-Tool/releases/tag/v2.92.0), Maincommit `d164aad6d7c7ef68c1b371c49a1fdea0a3b27dd7`, annotierter Tag und beide Quellenarchive sind veröffentlicht und remote verifiziert |
| Roharchiv | Benutzertransfer läuft beim Abschluss weiter. Zusätzliche Bereiche sind sequenziell vorgemerkt; Originale bleiben vollständig erhalten. Kein pauschales „alles gesichert“ |
| Einstieg | [START_HERE](../results/evaluation/thesis20_20261004/START_HERE.md), [Paperbefunde](../results/evaluation/thesis20_20261004/PAPER_FINDINGS.md), [gemeinsame Auswertung](../results/evaluation/thesis20_20261004/README.md) |

**Entscheidung:** Keine erneute Inferenz, Qualityrechnung, Performance-/Energieaufnahme
oder Modellkompilierung. Die folgenden historischen Stände erklären die Entwicklung;
sie sind keine aktuelle Restplanung. Wissenschaftliche Einschränkungen werden fallbezogen
veröffentlicht und nicht durch positive Flags beseitigt.

<details>
<summary>Historischer Kopfstand und Entscheidung vom 02.10.2026</summary>

### Historischer Kopfstand vom 02.10.2026

| Feld | Maßgeblicher Arbeitsstand am 02.10.2026 |
|---|---|
| Run | `thesis_20splits_n5000_b1000_20260925_20260925_103745`; bestehender Run seit 25.09., selektiv vervollständigt, keine neue Gesamtuntersuchung |
| Messabschluss | Energiehelper am **02.10. 03:49:31** mit `rc=0`; Workflowabschluss **05:34:24 +02:00**, `finalization_status=pass` |
| Gesamtstatus | Gespeichert `partial`, `technical_status=partial`, `quality_decision=not_evaluated`; wissenschaftlicher Bericht `not_claim_ready`. Nicht als erneuter Messabbruch, aber auch nicht als pauschaler Paper-PASS lesen |
| Auswahl und Budgets | 7 Modelle × 20 `stratified_windows`-Grenzen, 3 Setups; Single-Tensorfilter AUS, Native nur unterstützte Teilmenge, kein Nachrücken. N5000/B1000/Seed20260710; Native1000/100/3; Energie FS/command60s×3; Retry2/Quellenfehlerbudget20; Force AUS |
| Generic | **527 Ergebniszeilen + 37 dokumentierte Buildfehler + 24 bestehende Policyausschlüsse = 588 Sollfälle**; keine unerklärte planmäßige Genericlücke |
| Zentrale Quality | **548 completed**, 509 `reference_close`, 39 `accuracy_loss`, **0 technische Auswertungsfehler**; negative Resultate bleiben gültige Ergebnisse |
| Native-Performance | **234 erfolgreiche Fälle = 192 Splits + 42 Full-Baselines**, insgesamt **702 Wiederholungen**; zusätzlich 228 `not_supported`, 0 fehlgeschlagene/fehlende unterstützte Fälle |
| Native-Energie | **234 vollständige Zeilen, 702 gültige Replikate**, 705 physische Collectorversuche einschließlich 3 erfolgreich ersetzter ungültiger Vorversuche |
| Plausibilität | Gespeicherte Energie-/Leistungs-/Work-Unit-Rechnung und Native-Medianaggregation konsistent; keine pauschal verdorbene Messkampagne nachgewiesen. Keine unabhängige Rohtrace-Neuintegration oder Neukalibrierung im Audit |
| Offene Hauptarbeit | F01–F06: Backendlabels, Native-Qualityauthority, sechs lokale TRT-Full-Numerikbelege, Generic↔Native-Messgrenze, Energie-/Rollenexport und Terminal-/Qualityprojektion; Details §12/§22 |
| Nachmessung | **Kein kompletter Neulauf begründet.** Zunächst vorhandene Originalbelege und lokale Auswertung korrigieren; zusätzliche Messung nur bei konkret belegtem Fehler oder tatsächlich fehlender benötigter Evidenz |
| Tool-/Sourcebeleg | Laut letztem Installations-/Startbericht **2.91.2 einschließlich lokaler Nachbesserungen**. Host-HEAD dort weiterhin `182092216dfaf4f3ad36460a883098548c83bd8f` mit uncommitteter Folgearbeit; kein aktueller Host-Livecheck durch dieses KB-Update |
| Gitabgrenzung | Veröffentlichung der lokalen Tool-Folgeänderungen ist im letzten Bericht **nicht belegt**. Ein Dokumentcommit im Ergebnisrepo ist kein Toolrelease, kein Sourcebackup des Hosts und keine neue Messabnahme |
| Quellen | Abschlussarchiv `THESIS20_FINAL_AUDIT_20261002_093035.tar.gz`, Ergebnis-Audit `THESIS20_ERGEBNISAUDIT_20261002.md` mit Einzelbelegen und Abschluss-/Installationsberichte; Quellenrang und Prüfgrenzen §0/§22 |

**Entscheidung:** Jetzt **nicht erneut Resume oder eine neue Kampagne starten**. Vorhandene
Messwerte, Requestidentitäten, Artefakte, gültige Replikate und negative Befunde erhalten.
Zuerst die nachgewiesenen Auswertungsfehler lokal korrigieren. „Erhebung vollständig“ ist
nicht gleich „alle Vergleichsaussagen freigegeben“. Dieses Update dokumentiert den Audit;
es implementiert keinen der neuen F01–F06-Fixes. [E-TH20-AUDIT] [E-TH20-ENERGY-END]
[E-TH20-ENERGY-REENTRY] [E-TH20-FOLLOWUP]


</details>

<details>
<summary>Historischer Kopfstand vom 19.09.2026 – unverändert als damaliger Nachweis</summary>

| Feld | Maßgeblicher Arbeitsstand |
|---|---|
| Dokumentstand | **19. September 2026**; R9H-Nachweis nur bis **07:19:10 +02:00** |
| Grundlage | Vollständige REV4 vom 15.09. unverändert als historische Ausgangsdatei erhalten; wissenschaftliche Altbefunde bleiben bestehen |
| Letzte breit belegte Integration | **R9G `r9g_eval_20260918_171131`: 7 Modelle / 1 Split**, 63/63 Nativezeilen, 6.300 Requestpaare, 77 Qualityresultate und 189/189 erfolgreiche Energieaufnahmen |
| Wichtige R9G-Grenze | Aufnahme/Arithmetic vollständig, aber Energie-/Performance-Taskgleichheit, Inputs und Reporterprojektionen teilweise inkonsistent; kein pauschaler wissenschaftlicher PASS |
| Aktueller Abnahmeversuch | **R9H eval_02 `r9h_eval_20260919_064323`**, Start 06:43:23; letzter vorliegender Eintrag 07:19:10, keine terminale Bilanz geliefert |
| Ziel des R9H-Runs | 7 Modelle / **3 Splits je Modell/Backend**, Standard 500/500, Native 100/10/1, Native-Energie FS/Command1s×3; keine bestätigten 105/315-Endzähler |
| Zielinstallation laut Runheader | `~/ONNX-Splitpoint-Tool`, Version 2.83, Build `v2.83-r9b-request-latency`; weitere R9C–H-Änderungen werden nicht allein von dieser unveränderten ID unterschieden |
| Architektur | Smartmirror2 = x86-Ubuntu-Controller; normale GUI/Orchestrierung lokal, Jetson/H8/H10/DeepX/TRT über bestehendes SSH |
| Quellcode-Git, live gelesen | Veröffentlichte Branches `main` → `ef44c944…`, `smartmirror2-v282-baseline` → `c5eb66e…`; kein veröffentlichter `codex/v283-nightfix-smokes`-Branch in der gelesenen Liste |
| Evidence-Git, live gelesen | `Keff789/onnx-splitpoint-results`, `main` → `5636017e5db3229862ba10c609b5f4b5f290e76b`, letzter Commit12.09.2026: Hailo8 GPU/fixed16 HAR |
| Lokaler Quellstand | Frühere Lieferungen weisen umfangreiche uncommittete Änderungen aus. Aktueller Host-HEAD/Index hier nicht live gelesen; Remote-Baseline ist kein Backup dieses Arbeitsbaums |
| Dokument-/Gitwirkung | REV5 und ein bereinigter, reviewbarer Evidence-Patch **hier erstellt**, kein Hostzugriff, Commit, Push, Tag, neuer Test oder Eingriff in R9H |

**Entscheidung:** Den laufenden R9H-Run und seinen Supervisor ungestört beenden lassen. Die
abgeschlossenen R9B/R9C/R9E/R9G-Nachweise können jetzt dokumentiert und als getrenntes Evidence-Update
vorbereitet werden. R9H-Erfüllung, Sourcecheckpoint und zugehörige Schlussbelege erst nach Abschluss
und Prüfung sichern. Keine neue Reparaturrunde allein für die Knowledgebase. [E-REV5-GIT]
[E-REV5-R9G] [E-REV5-R9G-AUDIT] [E-REV5-R9H-LOG]


</details>

## Navigation

[0. Dokumentführung](#dokumentfuehrung) · [1. Methode](#methode) · [2. Fragenkatalog](#fragen) · [3. Setups](#endpunkte) · [4. Releasefortschritt bis R8](#v30) · [5. DeepX-Historie](#deepx-full) · [6. Energie](#energie) · [7. Modellqualität](#deepx-r1-r2) · [8. Cache und Abschluss](#abschluss) · [9. Historisches Complete Set](#complete-set) · [10. Historischer .4-Auftrag](#v31-plan) · [11. Historische Abnahme](#gates) · [12. Aktuelle Aufgaben](#todo) · [13. Betrieb](#betrieb) · [14. Evidenz](#ablage) · [15. Klärungen](#grenzen) · [16. Übergabe](#uebergabe) · [17. Änderungen](#aenderungen) · [18. Codex-Betrieb](#codex) · [19. GUI-Teststandard](#gui-tests) · [20. Nachtauswertung/Plausibilität](#nacht-audit) · [21. Historie R9A–H](#r9fortschritt) · [22. Historischer THESIS20-Audit](#thesis20-audit) · [23. Gemeinsamer Abschluss](#thesis20-final) · [Quellen](#quellen)

<a id="dokumentfuehrung"></a>
## 0. Dokumentführung und Quellenrang

Diese Fassung führt die kanonische Knowledgebase einschließlich der REV5-Historie fort.
Aktuelle Aufgaben stehen nur in §12, die aktuelle Übergabe in §16, die historischen R9A–H-
Nachweise in §21, der historische THESIS20-Audit in §22 und der gemeinsame Abschluss in §23. Methoden und historische
Befunde bleiben erhalten; spätere Ergebnisse schreiben keine Originalmessung um. Frühere
.4-, R8-, R9H- und THESIS20-Fortsetzungsanweisungen sind keine erneut auszuführenden Aufträge.

**Historischer Quellenstatus des Updates vom 02.10.2026 (durch §23 fortgeschrieben):** bestehende Git-Fassung und gelieferter THESIS20-
Ergebnis-Audit mit seinen Falllisten sowie datierte Installations-/Start-/Abschlussberichte.
Der Audit stammt aus der vorherigen Ergebnisprüfung; hier werden seine Befunde dokumentiert,
nicht erneut als neue Hardware- oder komplette Rohdatenprüfung ausgegeben. F01–F06 sind offen,
solange kein späterer begrenzter Implementierungs-/Abnahmebeleg vorliegt. [E-TH20-AUDIT]
[E-TH20-FOLLOWUP] [E-TH20-KB-UPDATE]

Primäre Ergebnisdateien haben Vorrang vor Reviews und Konsolen-/Chattext. Ein Auftrag belegt nur
Anforderungen, eine Sourceprüfung nur Sourceintegrität. Implementiert, normale Konfiguration,
lokal getestet, reale GUI-/Hardwareabnahme und wissenschaftliche Vergleichbarkeit bleiben getrennt.
Die bisherigen vier Abnahmeachsen gelten weiter. Testmengen verschiedener Runden sind überlappend
und dürfen nicht zu einer Gesamtzahl addiert werden.

Die historische REV5 konsolidierte vorliegende Originalberichte und bereits ausgeführte Gegenprüfungen.
Sie zählt ausgewählte archivierte JUnit-Dateien neu, exportiert vorhandene reviewed Tabellen als
CSV und prüft Dokument-/Patchintegrität. Keine neue Produkttestsuite, Inferenz, GUI-, Energie-
oder Compileraktion. Roh-Parquets wurden auch in der R9G-Endprüfung nicht neu integriert.
Die Git-Abfragen betreffen nur veröffentlichte Repositorymetadaten, nicht Smartmirror2s Dateisystem.

**Historischer Evidenzstichtag 19.09.2026:** R9H eval_02 ist im damaligen gelieferten Log laufend, nicht hier live beobachtet.
`host.log` ist der erste Versuch; `BEFUNDE_FUER_CODEX(1).json` beschreibt R9G-Vorfehler.
Weder Datei noch zeitlicher Abstand beweisen den Abschluss des zweiten Versuchs. Source, Liveprofile,
Venv, AGENTS.md, Manifeste und Caches während dieser Arbeit unangetastet lassen. [E-REV5-R9H-LOG]

### 0.1 Quellenstatus des vorherigen REV2-Abgleichs – historisch übernommen

**In REV2 direkt gelesen:** das 236-Dateien-Archiv `har_and_git_evidence.zip`, seine originalen HAR-/Runtime-/Buildberichte, API-/HN-Snapshots, die zentrale Qualityübersicht und die bereits vorliegende Git-Konsole. Erneut nachgezählt: alle sechs Stufen-Top-k-Listen, Vorhersagewechsel sowie 123 Quality-Endzustände. Numerische Logitstatistiken und Feedgleichheit bleiben Angaben der auf Smartmirror2 ausgeführten Collector; es wurden hier keine fehlenden Roharrays rekonstruiert. [E-HAR-R1] [E-KB-REV2-CHECK]

**Übernommen, nicht neu als Originalprüfung ausgegeben:** die neueren .3-FIX1–FIX5-/v2.80.4-Lieferangaben und der separate YOLO11l/H10-5.000-Bilder-Abschluss aus der beigefügten KB. Die dort benannten Originalexporte bzw. das .4-Lieferpaket lagen diesem Dokumentabgleich nicht zusätzlich vollständig vor. Diese bereits dokumentierten Entscheidungen werden erhalten und nicht wieder als neue Testpflicht geöffnet. [E-KB-2804-INPUT]

**Historischer Chat-/Abnahmebefund:** frühere Sourcegegenproben, Hardwareläufe und Testzahlen in dieser Unterhaltung bzw. ihren Berichten. Sie werden mit Version und Scope zusammengefasst, nicht bei jeder KB-Revision neu ausgeführt oder zu einer kumulierten Testzahl addiert.

**In REV2 vorgeschlagen:** der vertiefende Diagnoseweg in §7.8 und im Begleitplan. Er wurde nicht ausgeführt und ist durch die nachfolgende Scopeentscheidung jetzt ausdrücklich zurückgestellt. Seine technische Beschreibung bleibt erhalten, nicht sein früherer Vorschlag als nächster Arbeitsschritt.

### 0.2 Quellenstatus und Verbindlichkeit der REV3

Grundlage dieses Updates sind die vollständig gelesene beigefügte REV2 und die unmittelbar vorausgehende Diskussion zur automatisierten Partitionierung ohne modellspezifisches Nachoptimieren. Der Nutzer hat deren Aufnahme in die Knowledgebase angefordert. Neue Texte zur Forschungsfrage, Stopregel, Folgearbeit und Dissertation sind eine dokumentierte Projektentscheidung, **keine zusätzliche experimentelle Evidenz**. [E-KB-REV2-INPUT] [E-SCOPE-REV3]

In REV3 wurden keine Ergebnisarchive erneut numerisch ausgewertet, keine Hersteller- oder Runtimeinternas neu geprüft, keine Builds oder Inferenzen ausgeführt und keine Git-Änderungen veröffentlicht. Die Dokumentprüfung sichert Erhalt der bestehenden Abschnitte, Ergebnistabellen und Verweise. Bei einem Konflikt zur früheren Priorisierung des separaten Diagnoseplans gelten für die aktuelle Arbeit §§1.6–1.11, 7.8 und 12 dieser Revision. Eine Wiederaufnahme benötigt einen neuen, ausdrücklich abgegrenzten Auftrag.

### 0.3 Historischer Quellenstatus der REV4 und damalige Datumsgrenzen

**Direkt in dieser Dokumentrevision herangezogen:** die vollständige beigefügte REV3; Original-R8-Abschluss, Configdiff, Arbeitsstand, GUI-Bedienung, Source-/Test-/Hardwareberichte aus `ERGEBNISSE_R8.zip`; R8-JUnit-Nachzählung; der konkrete R8-Starter; bereits erzeugte Gegenprüfungen und die Ergebnisübersichten der R1–R7-/Auto-Runden sowie der Läufe vom 13. und 15. September. Die eingegebenen Installations-/Git-/Codex-Konsolen sind historische Nutzerbelege. [E-CX-SETUP] [E-CX-R8] [E-R8-REVIEW] [E-R7-RUN] [E-REV4-DOC]

**Nicht neu ausgeführt:** komplette Produkttestsuiten, GUI-/SSH-/Hardwareaktionen, Roh-Parquet-Integration, Compiler-/Firmwarebuilds, Live-Git-Abgleich oder der gerade laufende Nachtlauf. Nur vorhandene Unterlagen werden konsolidiert; fehlende Roharrays und unbekannte Hostzustände bleiben unbekannt.

**Dokumentierte Projektentscheidungen:** sichtbare Codex-Tagesarbeit ohne wiederholte Berechtigungsabfragen; Ultra bei passenden schwierigen Aufgaben; echte kleine GUI-Smokes statt wiederholter Finalkampagnen; nach dem aktuellen Nachtlauf Qualitäts-/Performance-/Energieprüfung in §20. Das sind Arbeitsregeln und Folgeaufträge, keine neuen Messungen. [E-CX-PREF] [E-NIGHT-R8-USER]

**Externe Zusatzquelle:** Nur für allgemeine Codex-Begriffe wurde am 15.09.2026 die offizielle OpenAI-Dokumentation zu CLI, `AGENTS.md`, nicht-interaktiver Ausführung, Berechtigungen und Subagenten gelesen. Sie ersetzt nicht den beobachteten lokalen CLI-0.154.0-Stand oder den tatsächlich gestarteten Auftrag. [E-CODEX-OFFICIAL]

Historische „R1/R2“ aus September 8 in §§5/7 sind **DeepX-Preprocessing-Reihen**. Die neuen **Codex-R1–R8 ab September 14** sind andere Aufträge; deren Quellenkennungen beginnen mit `E-CX-`. Gleiche Kurznummern dürfen keine Ergebnisse vermischen.

<a id="methode"></a>
## 1. Verbindlicher wissenschaftlicher Leitpfad

### 1.1 Zweck und Fallauswahl

Das Werkzeug und die vorab festgelegte Methodik werden validiert, nicht nachträglich nur die günstigsten Kombinationen ausgewählt. Quality-`fail` entfernt einen Fall nicht aus dem Audit. `inconclusive` ist weder `pass` noch automatisch ein technischer Fehler. Compiler-Rejects, nicht unterstützte Schnittstellen, fehlgeschlagene Runtimes und fehlende Messungen behalten unterschiedliche, ehrliche Terminalzustände. [E-KB]

Der produktive Ranker bleibt **`cut_bytes_only`**, aufsteigend nach Cut-Bytes mit deterministischem Case-/Boundary-Tie-Break. Stratified-Windows-Auswahl und score-unabhängiger Generic-Audit bleiben erhalten. Kein neuer Ranking-Sweep, keine nachträgliche Grenzwertoptimierung und keine Auswahl der günstigsten Wiederholung zur Ergebnisverbesserung. [E-KB] [E-PLAN31]

### 1.2 Modellumfang und Rollen

| Methodische Rolle | Modelle |
|---|---|
| Development | `resnet50`, `yolo26s`, `yolov7_paper` |
| Transfer/Evaluation | `mobilenet_v3_large`, `regnet_x_1_6gf`, `yolo26m`, `yolo11l` |

`yolo26x` ist nur ein gesondert zu planender Größen-/Stresstest, nicht automatisch ein achtes Modell. Die Rollen sind die methodische Vorgabe aus der bisherigen Knowledge Base. Eine abweichende Rollenbelegung eines konkreten Diagnoseprofils wird als dessen effektive Konfiguration berichtet, nicht still rückwirkend geändert. [E-KB]

### 1.3 Eingefrorene Policies

| Bereich | Fortgeltender Vertrag |
|---|---|
| Generic | Single- und Multi-Tensor-Boundaries an **einer** Splitstelle |
| Native | Technisch kompatible Single-Tensor-Boundaries; keine erfundene Multi-Tensor-Unterstützung |
| Multi-Split-Begriff | Keine neuen seriellen Mehrfachsplitstellen innerhalb eines Modells |
| Hailo-Build | `balanced`, Optimization Level 1, 500 Kalibrierungsbilder, Kalibrationsbatch 8 |
| DeepX-Build | 500 Kalibrierungsbilder, `ema`, Optimization Level 0 |
| DeepX-Klassifikation | **`imagenet_mean_std`** für Modelle mit entsprechendem Referenzvertrag; `current_scale_only` nur ausdrücklich benannter Legacy-/A/B-Arm |
| Detection | Modellfamiliengebundene Vorverarbeitung, Decoder, NMS und Koordinatenrücktransformation |
| Energie | Primär kalibrierte Full-System-Eingangsgröße; Native-Full-Baselines eingeschlossen; keine ersatzweise Aktivierung generischer oder CPU-/ORT-Energie |
| Finale Qualitätsaussage | Soweit im Thesisvertrag beansprucht: 5.000 Validierungsbilder, 5.000 Bootstrap-Wiederholungen, Official COCO/Pycocotools für Detection |

**B500-Kalibrierung, B500-Qualitätsauswertung und ein 16-Bilder-Smoke sind verschiedene Rollen.** Dieselbe Zahl von Bildern macht Trainingskalibrierung und Validierung nicht zum selben Datensatz. Ein Standard-B500-Lauf ersetzt nicht automatisch den weitergehenden Finalvertrag mit 5.000 Bildern; bereits abgeschlossene Finalaufträge werden nicht nochmals als offen geführt. [E-KB] [E-PLAN31]

### 1.4 Vergleichbarkeit und Ranking

Fairness verlangt gleiche wissenschaftliche Strata, gebundene Inputs, passende Artefakte, Precision, Endpunkte, Work Units und Messbedingungen. Backendspezifische Low-Level-Implementierungen sind erlaubt; zusätzliche Parallelität darf nicht unbemerkt nur einem Backend zugutekommen. Hersteller-Optimization-Level sind nicht als numerisch äquivalente Qualitätsstufen zu interpretieren. [E-KB]

Drei natürliche, identische und vergleichbare Single-Tensor-Fälle pro Modell bleiben das Ziel für die vorgesehene modellinterne Generic↔Native-Korrelation. Weniger vorhandene Fälle werden ehrlich deskriptiv ausgewertet. Kein künstlicher Split und keine Vermischung unterschiedlicher Endpunkt-/Precisiongruppen, um die Mindestzahl zu erreichen. Ein Sieben-Modell-`Complete_Set` ist nicht automatisch ein hinreichendes Rankingexperiment. [E-KB] [E-V30, §8]

### 1.5 Final Quality ist kein impliziter Wechsel sämtlicher Messverträge

`Final Quality (Standard+)` erhöhte im beobachteten Nachtlauf Validierungsumfang und Qualitybootstrap auf jeweils 5.000; B500-Kalibrierung, balanced/Opt1/Batch8 und `relaxed` blieben unverändert. Die reale Profilquelle ist die aufgelöste Run-Mode-Konfiguration plus erhaltene explizite Profilwerte. Ein Modusname ersetzt weder Freeze-/Rollenprüfung noch den Energievertrag. Eine im Profil verbliebene Native-Energiedauer von 1 s wird durch diesen Namen nicht zu 60 s. [E-NIGHT-2803]

Die sieben Modelle wurden in den Diagnoseprofilen teilweise alle als `development` geführt. Das ist der archivierte tatsächliche Diagnoseumfang, keine rückwirkende Erfüllung einer ungeöffneten Hold-out-/Transferrolle. Weitere Ursachenprüfungen auf denselben 16 geöffneten Bildern sind Diagnose und kein neues unabhängiges Validierungsset.

**Fortschreibung ab R8:** Die oben beschriebene alte Standard-/Final-Semantik ist historisch. Seit R8 unterscheiden sich zusätzlich die Native-Performancebudgets: Standard **100/10/1**, Final **1000/100/3**. Ein Gesamtmoduswechsel soll diese drei Werte gemeinsam auflösen, sofern kein ausdrücklicher Nutzer-Override oder eingefrorener Resumevertrag vorliegt. Energie-Replikate bleiben separat drei; der Moduswechsel ist weiterhin **keine** implizite Verlängerung von 1 s auf 60 s und kein Wechsel des Kampagnenmodus von Development zu vorab eingefrorener Final-Evaluation. [E-CX-R8]

### 1.6 Forschungsfrage und Bedeutung von „einfach so“

Die Hauptfrage lautet:

> Wie gut lassen sich die untersuchten vortrainierten Netze mit dem entwickelten Werkzeug und einer vorab festgelegten Verarbeitungspolitik automatisiert partitionieren und auf heterogener Hardware ausführen – hinsichtlich Ausführbarkeit, Qualität, Performance und Energie?

„Einfach so“ bedeutet **nach Einrichtung der unterstützten Backends, mit den implementierten allgemeinen bzw. modellfamilienbezogenen Regeln und ohne zusätzliche manuelle Optimierung jedes einzelnen Evaluationsfalls**. Es bedeutet nicht ohne Kalibrierung, ohne korrekte Vor-/Nachverarbeitung oder ohne Backendkonfiguration. Die im festen Rezept vorgesehenen automatischen Compileroptimierungen gehören weiterhin zum untersuchten Verfahren. Ihre Verwendung ist kein nachträgliches manuelles Tuning. [E-SCOPE-REV3]

Nicht Gegenstand der Hauptauswertung ist, für jedes Netz durch Architekturanpassung, individuelles Quantisierungsrezept, Compilerparametersuche oder Nachtraining die bestmögliche Herstellerimplementierung zu finden. Die Resultate beschreiben die Reichweite und Grenzen der untersuchten Tool-/Backendkonfiguration, weder eine universelle Eigenschaft aller Compiler noch die maximal erreichbare Modellqualität.

### 1.7 Fehlerkorrektur, Ursachenanalyse und Tuning getrennt behandeln

| Kategorie | Beispiel / Abgrenzung | Konsequenz |
|---|---|---|
| Implementierungskorrektheit | Fehlende vorgeschriebene Mean/Std-Normalisierung; falsches Tensorlayout; fehlerhafte Referenzbindung oder Mess-/Ergebniszuordnung | Den konkreten Fehler korrigieren oder den betroffenen Fall als technisch fehlerhaft bzw. nicht auswertbar kennzeichnen. Kein gewöhnlicher Quantisierungsverlust und kein Quality-PASS daraus ableiten. |
| Ergänzende Ursachenanalyse | Bestehende HARs vergleichen; optimierte Floatstufe oder Integer-I/O bei unverändertem HEF untersuchen | Kann die Diskussion vertiefen. Keine automatische Pflicht allein wegen einer großen Accuracyabweichung; für die derzeitige Hauptaussage zurückgestellt. |
| Modellspezifische Optimierung | Andere Kalibrationsmengen, Layerpräzision, Opt-Level, individuelle Compilerrezepte, Architekturänderung oder Nachtraining nach Betrachtung der Ergebnisse | Nicht Teil der eingefrorenen Hauptauswertung. Nur als eigenständiges, vorab beschriebenes Folgeexperiment mit getrennten Artefakten und Validierungsdaten. |

Ein korrekt eingerichteter Compilerkontext, Cache-Reuse und wahrheitsgemäße Berichte bleiben notwendige Softwarearbeit. Sie ändern nicht allein das wissenschaftliche Buildrezept. Eine Fehlerkorrektur wird versioniert und ihr betroffener Auswertungsumfang nachvollziehbar neu geprüft; alte Messungen werden nicht rückwirkend zu Ergebnissen des reparierten Pfads. Die durch frühere Ergebnisse beeinflusste Entwicklung wird transparent berichtet, nicht nachträglich als ungeöffnete Evaluation bezeichnet. [E-SCOPE-REV3] [E-KB]

### 1.8 Stopregel und Abschlussbedingung

**Die Größe eines korrekt zugeordneten Qualitätsverlusts ist allein kein Auftrag für weitere Tests, Neubauten oder numerische Änderungen.** Ein vollständiger Qualitäts-FAIL bleibt ein abgeschlossenes negatives Ergebnis. Zusätzliche Prüfung ist nur für einen konkreten neuen Fehlerverdacht, einen nachgewiesenen eigenen Fehler, noch fehlende erforderliche Evidenz oder eine ausdrücklich gewünschte stärkere Aussage zu planen. Ein neuer Verdacht ist selbst noch kein Fehlernachweis. [E-SCOPE-REV3]

Bekannte Implementierungsfehler werden nicht aus Zeitgründen zu „Compilerverlust“ umbenannt. Ungültige Detectionausgaben sind technische/semantische Misserfolge und keine regulären niedrigen AP-Werte. Ein nicht realisierbarer Split, eine Runtimeblockade, ein Qualitäts-FAIL, ein INCONCLUSIVE und ein Cancel ohne Ergebnis behalten ihre unterschiedlichen Zustände. Insbesondere werden die 60 Cancel-Fälle aus §7.9 durch diese Entscheidung nicht zu abgeschlossenen Qualitätsvergleichen.

Abschlussziel der Hauptauswertung ist die vollständige, überprüfbare Bilanz der vorab festgelegten Fälle: gemessene Resultate oder konkret belegte Nichtausführbarkeit/technische Einschränkung; verbleibende Evidenzlücken sichtbar. Ein bislang nicht gestarteter Messauftrag wird nicht allein durch einen Platzhalter abgeschlossen. Für positiv beanspruchte Qualitäts-, Performance- oder Energieaussagen bleiben sämtliche zugehörigen Gates bestehen. **Vollständig dokumentierte Ergebnislage ist nicht gleich vollständige positive Freigabe.**

Keine Lockerung der Qualitätsmargen, kein Austausch der Referenz, keine nachträgliche Auswahl besserer Splits, Seeds, Wiederholungen oder privater GPU-HEFs aufgrund bereits betrachteter Ergebnisse. Vorhandene erfolgreiche technische und negative fachliche Nachweise behalten ihren Scope; keine identische Testschleife bis PASS.

### 1.9 Zwei Vergleichsperspektiven auf den Nutzen des Splittens

**Gegen die kanonische Full-Floatreferenz:** Wie viel Qualität erhält die gesamte heterogene Umsetzung? Diese Referenz bleibt für das bestehende Qualitätsgate maßgeblich.

**Gegen die vollständige Backendumsetzung:** Was verändert die untersuchte Partitionierung gegenüber der Full-Ausführung unter dem zugehörigen festgelegten Backendrezept? Dieser ergänzende Vergleich hilft, den Gesamtverlust gegenüber Float nicht pauschal dem Splitten zuzuschreiben. Er ersetzt nicht die kanonische Referenz und ist keine neue Akzeptanzgrenze. Gleiches Dataset, Task-/Endpointvertrag und passende Artefaktzuordnung bleiben erforderlich.

Beispiel aus den bereits dokumentierten zentralen MobileNet-Ergebnissen (§§7.2 und 7.9): CPU-Float **73,70 %**, Hailo8 Full **60,62 %**, Hailo8 → TensorRT b027 **71,58 %** auf denselben 5.000 Bildern. Der konkrete frühe Split liegt damit **10,96 Prozentpunkte über Hailo8 Full**, aber weiterhin **2,12 Prozentpunkte unter Float** und bleibt nach der unveränderten 1-pp-Regel FAIL. Das ist eine deskriptive Einordnung bereits vorhandener Werte, kein neues gepaartes Signifikanzresultat zwischen Full-Hailo8 und Split und keine allgemeine Aussage für alle Grenzen. [E-NIGHT-QUALITY]

Der Fall illustriert einen Nutzen und zugleich eine Grenze der automatischen Partitionierung. Weder wird der frühe Split nachträglich als einziger Fall ausgewählt, noch wird aus einem schlechten Full-HEF geschlossen, sämtliche Splitpunkte müssten genauso schlecht sein. Die vorhandene HAR-Fallstudie unterstützt eine begrenzte Diskussion; sie liefert keine additive kausale Aufteilung des gesamten Accuracyverlusts.

### 1.10 Zulässige Tuning-Aussage und Grenze zukünftiger Arbeit

Zulässig ist: **Modellspezifische Anpassungen könnten einzelne Ergebnisse verbessern; Wirksamkeit, erreichbarer Umfang und zusätzlicher Aufwand sind für die hier untersuchten Fälle nicht systematisch bestimmt.** Die Herstellerbeschreibung benennt mögliche Optimierungsverfahren, aber keine nachgewiesene Verbesserung unserer Modelle. [E-HAILO-OPT-DOC]

Nicht belegt sind Aussagen wie „mit ausreichend Aufwand werden alle Netze gut“, „Opt2/Opt3 ist immer besser“ oder „der gesamte Verlust ist ausschließlich Quantisierung“. Mehr Aufwand garantiert keinen Erfolg; die methodische Entscheidung gegen neue Sweeps hängt nicht davon ab, ob eine künftige Verbesserung möglich wäre. [E-SCOPE-REV3]

Eine später ausdrücklich beauftragte Optimierungsstudie muss vom jetzigen festen Rezept und Ergebnisbestand getrennt bleiben. Bereits geöffnete Fixed16- und Evaluationsbilder sind keine unabhängigen Daten zur Bestätigung einer anhand dieser Resultate ausgewählten Konfiguration. Historische Opt2-Diagnosen und die abgeschlossenen GPU-/HAR-Smokes werden nicht verschwiegen: **Ausgeschlossen ist zusätzliches systematisches Einzelfalltuning der Hauptauswertung, nicht die tatsächlich erfolgte Entwicklung und Diagnose.**

### 1.11 Formulierungsbaustein für die Dissertation

> Die Evaluation untersucht die automatisierte Partitionierung und heterogene Ausführung vortrainierter Netze mit einer vorab festgelegten, backendspezifischen Build- und Validierungspolitik. Die innerhalb dieses Verfahrens vorgesehenen automatischen Optimierungsschritte bleiben Bestandteil der untersuchten Verarbeitungskette. Eine darüber hinausgehende manuelle, modellspezifische Optimierung von Netzarchitektur, Quantisierung oder Compilerparametern ist nicht Gegenstand der Hauptauswertung.
>
> Qualitätsverluste, nicht realisierbare Partitionierungen und technische Ausführungsfehler werden als unterschiedliche Ergebnisse vollständig berichtet. Ergänzende Diagnosen dienen der Prüfung ausgewählter Verarbeitungsschritte und der begrenzten Einordnung beobachteter Abweichungen; sie stellen keine vollständige Ursachenanalyse sämtlicher Compiler- und Runtimeeffekte dar.
>
> Die Ergebnisse beschreiben damit die Leistungsfähigkeit und Grenzen des implementierten automatischen Verfahrens unter der untersuchten Konfiguration, nicht die maximal erreichbare Qualität individuell optimierter Implementierungen. Ob und mit welchem Aufwand modellspezifische Anpassungen die verbleibenden Verluste verringern können, bleibt zukünftiger Arbeit vorbehalten.

Dieser Baustein dokumentiert den vereinbarten Untersuchungsumfang, keinen neuen Messbefund. Die tatsächliche Toolentwicklung, frühere Diagnosen, Datenöffnung und die unverändert fortgeltenden Modellrollen bleiben in der Arbeit transparent. [E-SCOPE-REV3]

<a id="fragen"></a>
## 2. Fortgeschriebener Fragen- und Boundarykatalog

Die folgende Arbeitsübersicht führt die dauerhaft relevanten Antworten fort und ergänzt die neuen DeepX-/Complete-Set-Fragen. Historische Detailbegründungen bleiben unter [E-KB] erhalten.

| Frage | Kanonische Antwort / heutige Grenze |
|---|---|
| Erreicht Native die ungefähr 97 FPS der handimplementierten YOLOv7-Referenz? | Für den exakten historischen Hailo-8-Pfad `yolov7_paper/b066` sind rund 97,077 P2- und 97,059 Completed-Detection-FPS dokumentiert. Kein allgemeiner Wert für andere Splitpunkte oder v31. |
| Ist dieselbe Implementierung für alle Backends erforderlich? | Nein. Derselbe wissenschaftliche Vertrag ist erforderlich; passende native I/O-, FIFO- und Runtimepfade sind erlaubt. |
| Bestimmt die langsamste Stage die Pipeline-FPS? | Sie beschreibt den idealen Flaschenhals. Maßgeblich ist die direkt gemessene Makespan-Rate abgeschlossener Work Units; Handoff und Backpressure können zusätzlich begrenzen. |
| Sind Hailo-8 und Hailo-10H mit „gleicher Qualität“ gebaut? | Gleiche angeforderte Recipe und derselbe Datenvertrag, nicht garantierte gleiche Accuracy. |
| Was ist bei DeepX qualitätsrelevant? | B500, EMA, Opt0 und der zum Modell passende numerische Eingabepfad. R1/R2 zeigen, dass ein vorhandener korrekter Pfad durch eine falsche Profilwahl wirkungslos bleiben kann. |
| Muss DeepX jetzt einen neuen Preprocessor erhalten? | Nein. Der vorhandene v30-Sub/Div-Buildadapter funktioniert im R2-Smoke. Der bestätigte vorhandene Pfad wird regulär geroutet; aktuelle .4-Regressionen erhalten Full-/Part1- und Cachebindung. |
| Ist MobileNet durch den Fixed16-Smoke bestanden? | Technische Ausführung im benannten Scope; keine B5000-Freigabe. Neuere abgeschlossene Full-Quality-FAILs stehen in Abschnitt 7. |
| Beweist R2, dass die alten 6,6 Prozentpunkte Verlust vollständig verschwinden? | Nein. Der Mechanismus ist bestätigt; die quantitative Wirkung auf den alten 500er-Umfang ist nicht neu gemessen. |
| Müssen Top-k, Softmax oder Labels geändert werden? | R1 liefert dafür keinen Anlass: die geprüften Rohlogits, Produktiv-Top-k und Zuordnungen stimmen im getesteten Umfang überein. |
| Sind 55 unqualifizierte Energiezeilen 55 Messfehler? | Nein. Alle 55 haben drei gültige Replikate. Globale Matrixunvollständigkeit sowie lokale Quality-/Endpointgründe verhindern die Freigabe. |
| Ist M.2-Idle vom Primärergebnis abzuziehen? | Primär bleibt die kalibrierte, nicht idle-subtrahierte FS-Gesamtenergie. Eine separate TensorRT-Full-Normalisierung darf den gebundenen Idlewert zusätzlich ausweisen. |
| Braucht jedes Modell zwingend drei neue Splits? | Nein. Vergleichbare natürliche Fälle nutzen; unzureichende Kandidatenzahl kennzeichnen. |
| Ist ein `KNOWN_INFEASIBLE`-Split ein Cachefehler? | Nein, wenn exakte negative Compile-Evidenz vorliegt. Er bleibt ein erklärter nicht ausführbarer Planfall. |
| Darf eine alte Messung durch einen neuen Reporter zu `pass` werden? | Ein Zuordnungsfehler darf read-only erklärt werden. Messstatus, Payloads und wissenschaftliche Freigabe dürfen nicht erfunden oder umetikettiert werden. |
| Brauchen wir neue Hash-/Seal-/Datenbankebenen? | Nein. Vorhandene notwendige Identitäten weiterverwenden; teure globale Cache-Neuschreibvorgänge entfernen statt neue Systeme einzuführen. |
| Sind die 56 neuen .4-Anforderungen schon 56 bestandene Tests? | Nein. Geplante Anforderungen, parametrisierte Testfälle und tatsächliche Ausführungen unterscheiden; die .4-Verifikation nennt den belegten Umfang. |
| Ist Hailo8 GPU erst noch grundsätzlich zu testen? | Nein: Compute/XLA, ein echter MobileNet-Build und 32 Fixed16-Geräteinferenzen sind abgeschlossen. Offen ist nur ein gegebenenfalls neuer normaler .4-Integrationsscope, nicht dieselbe Diagnosewiederholung. |
| Bedeutet Parsed-HAR = Float, dass nur Quantisierung schadet? | Nein. Der Vergleich bis Quantized umfasst auch Float-/Graphoptimierungen und quantisierungsbegleitende Anpassungen; §7.7–7.8 trennen belegt und vorgeschlagen. |
| Ist Quantized-HAR = GPU-HEF nachgewiesen? | Nein: vier unterschiedliche Top-1-Vorhersagen auf 16 Bildern; RMS 0,39264502. |
| Macht Quality-FAIL den HEF-Cache kaputt? | Nein. Technische Verwendbarkeit und Qualitäts-/Claim-Eignung sind getrennt. |
| Sind HAR-Ergebnisse bereits im Git? | Laut übernommener erfolgreicher Push-Konsole ja, einschließlich `REPORT.md` und `CLAIM_BOUNDARIES.md`; spätere ausführliche Interpretation und KB-REV2/REV3 sind nicht Teil dieses benannten Commits. Ein neuer Dokumentpush ist nicht belegt. |
| Sind 225 GPU-Samples oder 203 Assembleraufrufe 225/203 unabhängige Tests? | Nein. Das sind zugeordnete Beobachtungen innerhalb desselben Builds. |
| Was heißt „Splitten einfach so“ in der Dissertation? | Automatisierte Ausführung nach Backendeinrichtung mit den festgelegten Regeln und Recipes, ohne manuelle Optimierung jedes Evaluationsfalls; nicht ohne Vorverarbeitung oder Kalibrierung. |
| Müssen wir einen großen Qualitätsverlust vollständig erklären, bevor er berichtet werden darf? | Nein. Korrekt ausgeführte und gebundene negative Ergebnisse sind berichtsfähig; stärkere Ursachenbehauptungen benötigen eigene Evidenz. Bekannte eigene Fehler bleiben technische Fehler. |
| Ist die vertiefte H8-Analyse jetzt noch ein aktiver Auftrag? | Nein. Optimierte Floatstufe, Integer-I/O- und weitere interne Ursachenprüfung sind zurückgestellte optionale Folgearbeit (§7.8), keine Voraussetzung für den Integrationsrelease oder die jetzige Hauptaussage. |
| Sind Fehlerkorrektur und Tuning dasselbe? | Nein. Den festgelegten Vertrag korrekt umzusetzen ist Pflicht; das Netz nach sichtbaren Ergebnissen individuell zu optimieren ist ein anderes Experiment. |
| Dürfen wir Verbesserungen durch Tuning in Aussicht stellen? | Nur als unbestimmte Möglichkeit zukünftiger Arbeit, nicht als Nachweis, dass alle Modelle oder Qualitätsmargen damit erreichbar sind. |
| Bedeutet ein besserer Split als das Full-HEF automatisch Quality-PASS? | Nein. Der ergänzende Backendvergleich ersetzt das unveränderte Gate gegen die kanonische Floatreferenz nicht. |
| Wann ist die Hauptauswertung abgeschlossen? | Wenn die vorab festgelegten Fälle nachvollziehbar mit Ergebnissen oder belegten Grenzen bilanziert sind und benötigte Nachweise für die tatsächlich beanspruchten Aussagen vorliegen; nicht erst, wenn alle Qualitätsfelder grün sind. |


Quellen: [E-KB] [E-V30] [E-R1] [E-R2] [E-PLAN31] [E-SCOPE-REV3].

### 2.1 Neue Kurzantworten ab Codex/R8

| Frage | Aktuelle Antwort |
|---|---|
| Ist Smartmirror2 ein Jetson? | Nein, x86-64-Linux-Controller; Jetsons sind SSH-Ziele. |
| Gibt die Codex-Installation diesem Webchat direkten SSH-Zugriff? | Nein. Codex läuft als eigener Agent auf Smartmirror2; Analyse/Plan hier, Ausführung dort, Bericht zurück. |
| Bedeutet `never` voller Zugriff oder unsichtbarer Hintergrundbetrieb? | Nein. Keine Genehmigungsdialoge; technische Sandboxgrenzen bleiben. Sichtbarer Vordergrund ist der Standard für Tagesaufträge. |
| Beweist `codex doctor` eine funktionierende Sandbox? | Nein. Ein tatsächlicher harmloser Befehl in der Sandbox muss funktionieren. |
| Ist ein grüner privater Collector-Smoke ein GUI-PASS? | Nein. Erst normaler Profil-/Registryresolver bis Spawn, Ergebnisimport und GUI-Abschluss nimmt die Produktintegration ab. |
| Ist R8 schon in der normalen Installation? | Ja, laut finalem Zielnachweis Hauptrepo und normale Config aktiviert; spätere Codeänderungen nicht behaupten. |
| Muss Standard auch Native verkleinern? | Ja: ab R8 100/10/1; Final 1000/100/3, Overrides sichtbar. |
| Ist H10 YOLO26 „gefixt“? | Diagnose-Binding ja; die Nulloutputs von b398/b364 nein. |
| Ist der aktuelle Nachtlauf bereits technisch sauber? | Noch unbekannt; Nutzer meldet laufend. Abschluss und tatsächlicher Plan fehlen. |
| Reichen 97 FPS allein als Plausibilität? | Nein. Historisches `yolov7_paper/b066`, gleicher Endpunkt, Work Units, Precision und Messvertrag müssen passen. |
| Bedeutet geringe AP, dass gemessene Zeit nicht existiert? | Nein. Die Beobachtung bleibt vorhanden; ein ungültiger Endpunkt erlaubt aber keinen gleichwertigen Completed-Task-Speedupclaim. |

<a id="endpunkte"></a>
## 3. Setups, Work Units und Endpunkte

### 3.1 Dokumentierte Arbeitsumgebung

Controller/GUI: `Smartmirror2` (**x86-64-Linux, kein Jetson**), Tool unter `~/ONNX-Splitpoint-Tool`, bestehende Tool-Venv `.venv`. Modell-/Ergebnisablage unter `~/Models`, lokale Buildartefakte unter `~/Models/BackendArtifacts`. Die beobachtete lokale Compiler-GPU ist eine GTX 1080 Ti; sie ist **nicht** das Jetson-Messgerät. [E-R1] [E-R2] [E-OVERNIGHT]

| Setup-ID | Messsystemrolle |
|---|---|
| `orin_nx_hailo8_01` | Jetson Orin NX mit Hailo-8 und zugehöriger FS-Messkette |
| `orin_nx_hailo10_01` | Jetson Orin NX mit Hailo-10H und zugehöriger FS-Messkette |
| `orin_nx_deepx_m1_01` | Jetson Orin NX mit DeepX M1 und zugehöriger FS-Messkette |

Die historische Bezeichnung `hailo10` in Pfaden ist von der normalisierten Architektur `hailo10h` zu unterscheiden. Konkrete IPs, Runtime-Venvs und Powerzustände aus der zugehörigen Konfiguration lesen, nicht aus alten Kommandozeilen erraten. [E-CS] [E-OVERNIGHT]

### 3.2 Physischer Output und abgeschlossene Aufgabe

Bei Detection bleiben `raw_head`, `decoded_pre_nms` und `decoded_nms` getrennt. Bereits dekodierte Boxen/Scores vor NMS sind noch nicht die abgeschlossene Detectionaufgabe. Umgekehrt darf ein nachweislich integrierter NMS-Endpunkt nicht ungeprüft ein zweites Mal NMS erhalten. [E-V30] [E-PLAN31]

`endpoints/completed_task/` ist zunächst die **Rolle eines Evidence-/Ausführungspfads**. Nicht jede dort archivierte Tensor-Datei ist deshalb bereits ein Post-NMS-Detektionsarray. Physische Ausgabe und Completionnachweis bleiben getrennte Verträge. [E-PLAN31, AP3]

Performance und Energie verwenden denselben gebundenen Arbeitsendpunkt. Die reale Nachverarbeitung muss innerhalb des beanspruchten Messfensters erledigt sein. Aufwendige Oracle-, Hash- und Dump-Arbeit darf in Vor-/Nachprüfungen liegen; die **eigentliche Aufgabe pro Frame** darf dadurch nicht aus dem Messfenster verschwinden. Ein Oracle-PASS außerhalb des Zeitfensters allein beweist keine zeitlich überlappende Three-Stage-Ausführung. [E-PLAN31, AP4]

### 3.3 Pipeline- und Energieraten

Die Pipeline-Rate wird aus abgeschlossenen Work Units und der tatsächlich beobachteten Wandzeit bestimmt. P1-FPS, P2-FPS, Cycle-FPS, interne DXRT-Throughputzahlen und Completed-Detection-FPS werden nicht austauschbar benannt. Für Energie sind die Work Units der konkreten Energieausführung maßgeblich, nicht eine aus früheren FPS hochgerechnete Ersatzanzahl. [E-KB] [E-PLAN31]

### 3.4 Compilerfamilien und erfolgreich geprüfte lokale Kontexte

| Familie | Tatsächlich geprüfte Umgebung | Ursprüngliche Blockade | Positiver Nachweis / Grenze |
|---|---|---|---|
| DeepX | Compilerlokales Torch-cu126-Overlay für GTX 1080 Ti / SM 6.1 | cu130-Paket ohne passende GPUarchitektur | R1/R2 und spätere reguläre Mean/Std-DXNN-Builds; nicht mit Hailo-TensorFlow vermischen |
| Hailo10H | DFC 5.3.0; TensorFlow 2.19.1; vorhandener Triton-ptxas 12.8.93 plus zugehörige libdevice | Systempfad zeigte auf CUDA-13-ptxas, der `sm_61` ablehnte | GPU/XLA und echter MobileNet-Build mit 327 zugeordneten Aktivitätsmessungen; Fixed16 technisch bestanden |
| Hailo8 | DFC 3.33.1; TensorFlow 2.18.0; separates CUDA-12.5.82-Overlay mit zwölf NVIDIA-Paketen | benötigte Runtimebibliotheken und passender ptxas/libdevice-Kontext fehlten | GPU/XLA, Modellbuild mit 225 positiven eigenen GPU-Samples, 203 Assemblierungen und Fixed16 bestanden |

Hailo10-Freigabe deckt Hailo8 nicht ab. Der späte Threadsetterfehler im ersten Smoke war ein Helferfehler; `DLOPEN_UNRESOLVED` in einem neutralen Diagnoseprozess bewies bei Hailo10 keine neun fehlenden Compute-Libraries. Dort funktionierten normale GPUoperationen bereits, bevor XLA durch die passende Assemblerwahl repariert wurde. Ein Component-View aus ptxas/libdevice ist kein vollständiges CUDA-Toolkit. [E-GPU-HISTORY] [E-H8-COMPUTE] [E-H8-BUILD]

Der neue Hailo8-Zusatzbestand blieb außerhalb der Venv:

```text
~/.onnx_splitpoint_tool/hailo/hailo8_cuda_20260912T062240Z_hx7b7hcq/
  overlay_manifest.json
  packages/
```

Das Manifest allein reicht nicht; die referenzierten Bibliotheken behalten. Der Diagnoseprozess wählte ihn explizit. Eine GUI-GPUpräferenz alleine überträgt diesen Pfad noch nicht. Die .4-Integration soll dafür die bestehende Konfigurations-/Resolverstrecke verwenden, ohne Parentumgebung, Hailo10 oder DeepX zu verändern. Hailo8-Hardwaretest: VStreams, HailoRT 4.20.0, FLOAT32-Host-Ein-/Ausgaben; Hailo10-InferModel-Details nicht ungeprüft übernehmen. [E-H8-RUNTIME]

<a id="v30"></a>
## 4. Releasefortschritt: Historie bis v2.80.4 und Weiterentwicklung bis R8

| Stand | Belegter Fortschritt und verbleibende Aussagegrenze |
|---|---|
| v2.79.30 | Historische positive fachliche Teilabnahme von DeepX-Full-Prüfübergängen, Merge und terminalem Abschluss; keine damalige Gesamtfreigabe |
| v2.79.33 | Force in 27 aktiven Nutzerprofilen ausgeschaltet; mitgelieferte Canary-Schalter wurden gesondert als Sourceauftrag verfolgt |
| v2.79.34 | Produktive Force-Einstiegspunkte bereinigt; Familienkontext, Diagnosebindung und Prozessbereinigung integriert. Auf Smartmirror2 laut originalen Abnahmen 2.561 Abnahme- und 388 Kurztests bestanden |
| v2.80 | Cacheprüfung ohne unnötigen SDK-Import, H8-Kindumgebung und Cleanup-/Archivabschluss korrigiert. Historisch je 2.659 Softwaretests aus Source und isoliertem Upgrade sowie 535 Kurztests bestanden; Wiederholungen nicht addieren |
| v2.80.1/.2/.3 | CPU-Referenzbindung, vollständige Remote-Abhängigkeiten, Buildbereitschaft, Native-Nichtstarts und Debugdiagnosen sind die fortgeltende .3-Basis; keine alten .2-Dateien zurückkopieren |
| v2.80.3 FIX1 | Umgebungsabhängigen Testfehler bei fehlendem Originalmodell isoliert; gezielte Reparaturabnahme PASS. Der vorherige Lauf hatte 3.122 bestandene Tests, einen Fehler und eine Deselektion; das ist kein vollständig grüner Erstlauf |
| v2.80.3 FIX2–FIX5 | Gezielte Folgekorrekturen für Referenzvorbereitung/Hardwarebindung und YOLO11l-Normalworkflow. Metadaten-/Source-PASS allein wurde nicht als Hardware-PASS gezählt |
| v2.80.3, 5.000-Bilder-YOLO11l | Normaler Workflow technisch abgeschlossen, vorhandene Artefakte wiederverwendet, vollständige Vorhersagen exportiert. Hailo-Qualitäts-FAIL bleibt bestehen |
| v2.80.4 | Liefert AP1/AP2/AP3 sowie Reuse-/Aussageabsicherung nach neuem Plan. Konkrete neue Testzahlen, erlaubte Nichtausführungen und Installerbelege ausschließlich aus der .4-Verifikation übernehmen |

Diese Zeilen sind ein Fortschrittsindex. Alte Testzahlen werden nicht als neue .4-Tests ausgegeben. Die auf Smartmirror2 tatsächlich gestartete Version ist aus ihrem Modul-/Source-Manifest festzustellen; gleiche sichtbare Versionsnummern können unterschiedliche ausdrücklich benannte FIX-Stände haben. [E-2804-CHAT] [E-2804-PLAN]

### 4.1 Force-Ursprung und zentrale versus explizite Profileinstellungen

Der Audit fand echte YAML-Booleans: `standard` und `smoke` Force aus, gespeichertes `final` Hailo/DeepX Force an. Der historische Resolver reproduzierte den Konfigurationshash von 16 alten Profil-Snapshots bis zum 3. September; die Force-Werte waren somit schon vor v32 in der Gesamtregistry vorhanden. **Die erste Schreibaktion ist unbekannt; daraus folgt keine bewusste Änderung durch den Nutzer.** [E-FORCE-AUDIT]

Bloßes Öffnen/Speichern korrekt typisierter `false`-Werte reproduzierte keine automatische Aktivierung. Dagegen waren `bool("false")` und das Überschreiben neuerer Dateien aus einem alten offenen Panel echte reproduzierte Robustheitsfehler, aber nicht als konkreter historischer Auslöser belegt. Die späteren typisierten Konfigurations-/Speicherfixes bleiben Regressionen. Der v34-Stand führte zusätzlich eine strengere produktive Force-Sperre ein; private nicht publizierende Einzelfalltests bleiben davon getrennt.

Bei `follow_tool_config=true` kommt Force aus dem ausgewählten zentralen Modus. Eine ausdrücklich im Evaluationsprofil gesetzte DeepX-Normalisierung kann dagegen einen zentralen Mean/Std-Default übersteuern. Daher immer **effektive Werte und ihre Quellen** prüfen. Alte Profiles erhalten bedeutet nicht, ihre alten Einstellungen seien automatisch korrekt. Ein vollständiger Reset ist nicht erforderlich; keine heimliche Profildateiumschreibung.

### 4.2 Fehlerketten und reale Übergangsnachweise v2.80–v2.80.3

| Beobachteter Fehler / Lernpunkt | Späterer enger Fix bzw. heutige Einordnung |
|---|---|
| H8-Overlay akzeptiert, aber Librarydirs nicht im Compute-Kindprozess | v2.80 überträgt bestehende `child_library_environment()` tatsächlich; später positiver realer H8-Computeumfang |
| Worker beendet, Remoteverzeichnis aber nicht gelöscht; trotzdem Cleanup=true | Prozess- und Stagingcleanup getrennt; Primärfehler erhalten; ZIP nur vollständig publizieren |
| v2.80: `quality_result_contract.py` fehlt in Remote-Closure | gesamten Paketbestand vor Importprüfung übertragen; sauberer Zielpaketbaum als Regression |
| Management-CPU-Referenz verlangt Generic-Kandidaten-IDs | eigene enge Referenzrolle berücksichtigen, keine Jetson-ID erfinden |
| v2.80.1: `management_cpu_reference_context_invalid:model_binding` | logische ID aus `model_id → model_name → model` statt ONNX-Pfad; falsche explizite IDs weiter ablehnen |
| übersprungenes TRT Full erscheint als Transferfehler/Missing | explizite negative Zeile `blocked_upstream_quality`, null Versuche, unveränderte Planidentität |
| Deferred-Build `partial` verschwindet hinter Stufe `ok` | betroffene Pflichtjobs mit Modell/Boundary/Backend/Primärgrund in Readiness übernehmen; gültige andere Jobs fortsetzen |
| null gestartete Splits erscheinen als `partial_repetitions` | belegte Nichtstarts von echten Teilmessungen unterscheiden; unbekannte Versuchszahlen nicht auf 0 raten |
| Debugexport verliert kleine CPU-Logs oder nennt großen gültigen Index beschädigt | kleine Prozessdiagnosen zulassen, Größenlimit von Syntax-/Integritätsfehlern trennen |
| v2.80.3-Nacht: plötzlicher Fortschritt nach Cancel | 63 ausgewertet und 60 Abbruchfolgen, nicht 123 berechnete Vergleiche; .4-Berichtsauftrag |

Die vollständige v2.80.1-Zielsoftwareabnahme meldete 2.832 unterschiedliche Tests; 708 Kurztests waren eine Teilmenge. Trotzdem scheiterte danach der echte Generator-/Referenzübergang an `model_binding`. **Große Testzahlen ersetzen somit keine passende realistische Pipelinefixture.** Die .2-Prüfung verwendete die sieben tatsächlichen BenchmarkSet-Kontexte; im .3-Nachtlauf wurden schließlich alle sieben CPU-Referenzen mit 5.000 Einträgen erzeugt. Bereits erfolgreiche Remote-/Vendor-Full-/Energieteilstufen sind von fehlender zentraler Qualitätsauswertung zu trennen. [E-RELEASE-AUDITS] [E-WORKFLOW-HISTORY] [E-NIGHT-QUALITY]

### 4.3 Fortschritt v2.81/v2.82 und Codex-R1–R8

Die Runden unten sind Reparatur-/Testaufträge innerhalb des Arbeitsstands v2.83; **R8 ist keine separate GUI-Versionsnummer**. Die aktuelle Build-ID unterscheidet die Revisionen. R1–R8 wurden zuletzt nicht committed; ein alter HEAD allein identifiziert deshalb nicht den getesteten Sourcebaum. Zahlen sind je Endstand, nicht zu einer Gesamtsumme zu addieren. [E-CX-SETUP] [E-CX-R8]

| Stand / Runde | Nachweis und Konsequenz |
|---|---|
| v2.81 → v2.82 | Implementationspläne adressierten produktive Quality-/Evidencepfade, ausgewählte Energy-Retries, generische Rollen/Ausschlüsse, Workspace und H10-Endpunkte. Die ursprünglichen Pläne sind keine Hardwarefreigabe. Der nächste reale Nachtlauf ist die konkretere Evidenz. |
| v2.82-Nacht `completsetdev_20260913_222455` | 61/63 Nativezeilen ausgeführt, zwei bekannte H8-Build-Ausschlüsse; 74 zentrale Entscheidungen (53 PASS, 18 FAIL, 3 INCONCLUSIVE); 60/61 vollständige Energiezeilen. H8-Reportweitergabe, H10-Nulloutputs und DeepX-Zweibilderfehler getrennt lokalisiert. [E-NIGHT-282] |
| Codex-R1 | H8-Wiederholungsfelder, Ausschluss-/Claimprojektion, Student-t und Captureplanung repariert. Hardware vor SSH an nicht beschreibbarem Produktlock blockiert. Private Softwaretests waren keine Produktintegration. [E-CX-R1] |
| Codex-R2 | H8 zwei CPU-Bildreferenzen + gespeicherte Nativeoutputs vollständig lokal validiert; H10-Resolver repariert und P1/Bridge/P2 untersucht; DeepX-XYXY-Fehler bestätigt. Energie 1/3; die zusätzliche Abbruchüberwachung verfehlte ihr Budget. 290 PASS/1 FAIL. [E-CX-R2] |
| Codex-R3 | 310 PASS, kein Skip; echte Fake-Prozesszähler sichern Start-/Retrygrenzen. Diagnoseablage aus Sourcebaum verlegt, DeepX-Diagnoseausgabe korrigiert. ACL-/Updaterproblem getrennt. Keine Hardware. [E-CX-R3] |
| R4 | Drei reale Collectorstarts: ein gültiger, zwei First-Sample-/Socketfehler; Budgetstopp korrekt, kein vierter Start. Keine Abnahme des Wiederanlaufs. [E-CX-R4] |
| R5 + Fortsetzung | Private Rustquelle geändert; zunächst `--offline` wegen fehlendem `visa-rs` blockiert, danach festgeschriebene Dependencies ausdrücklich erlaubt. 9 Rust-/13 UDP-/8 Startschutztests PASS; real eine gültige und eine unvollständige Aufnahme, fehlendes Endpaket sperrt weitere Ketten. [E-CX-R5] |
| Auto-Nacht-Vorbereitung 14./15.09. | Budgetweitergabe, Releaseidentität 2.83 und Installedprüfung weitergeführt, aber `ready:false`; 544 PASS/19 FAIL. Kein Nachtstart versucht. Separater Fallback war nicht eingerichtet. Überkomplizierte Freigabekette kostete den gewünschten Nachtlauf. [E-CX-AUTO] |
| R6 | 567 Produkttests, 11 Rust- und 21 UDP-Tests PASS; zwei lastfreie Diagnosen und drei Energie-Erstaufnahmen erfolgreich. Historische R5-Ursache bleibt offen. Collector/Registry/Profil weiterhin privat, keine vollständige GUI-Integration. [E-CX-R6] |
| GUI-Lauf `completsetdev_20260915_085558` | H8/H10-Storageprobe `rc=124`, danach lokaler Management-Shutdown unbewiesen/Quarantäne. Kein Energieausfall als Primärursache. [E-GUI-085558] |
| R7 | 647 PASS einschließlich 567 R6-Knoten. Storagevalidierung/Diagnosen, Managementabbruch und Primär-/Cleanupanzeige repariert. Isolierter Kandidat zunächst wegen fehlender Hostprozesssicht nicht übernommen; spätere Hostübernahme nötig. Historische Timeoutursache unbelegt. [E-CX-R7] |
| GUI-Lauf `completsetdev_20260915_124548` | Sieben Modelle/ein Split, Runtimeabschluss gut, 75 zentrale Qualityresultate. Normales Profil jedoch alter Collectorpfad/keine neue Budgetpolicy: 342 Hauptcollectorstarts, 24 gültige Einzelaufnahmen, **0/61 vollständige Zeilen**. [E-R7-RUN] |
| **R8** | Hauptrepo **und normale Config** integriert, Standardbudgets vereinheitlicht, echte Tk-/GUI-Abnahme und kompakte Ausgabe. **678 Regressionen, 6 Tk-Fälle, ein echter H8/MobileNet-GUI-Smoke mit 9/9 Energie-Erstaufnahmen**. Letzter Ausgabe-Drainfix nach Hardware nur lokal nachgeprüft. [E-CX-R8] |

### 4.4 Aktuelle Identität und endgültiger R8-Testscope

Version **2.83**, Build **`v2.83-r8-gui-product-integration`**. Normale GUI über `./start_gui.sh`; keine zweite R8-Installation. Finaler Hauptrepo-Import und Installedprüfung melden 1.994 Release-Dateien und 69 separat erhaltene Profile. R8 verändert 39 Dateien gegenüber seinem Startstand; kumulativer Git-Diff umfasst zusätzlich R1–R7. Ein kumulativer Textpatch enthält nicht automatisch jedes schon vorhandene binäre Testfixture oder alle lokalen Runtimeabhängigkeiten. [E-CX-R8] [E-R8-REVIEW]

Die letzte Ausgabekorrektur verhindert Abschneiden einer endlichen bereits eingelesenen Queue bei langsamen Diagnosehandlern. Eine wirklich offen bleibende geerbte Pipe führt begrenzt zu `pipe_drain_incomplete`/rc70 und kontrolliertem Cleanup. Lokal 35/35 gezielte Prozessfälle und danach 678/678 Regressionen; diese Teilmengen nicht addieren. Zwei frühere 674/4-Läufe scheiterten an einem unvollständig ersetzten Provenanzeinstieg in synthetischen Terminalfixtures; der Stub wurde an beiden beabsichtigten Stellen korrigiert, ohne Testzeitgrenzen zu erhöhen oder Produktchecks zu entfernen. [E-CX-R8]

Die anschließende neue Kampagne wird laut Nutzer ausgeführt. Ihre Beobachtungen dürfen die letzte Codeänderung real abdecken, sobald die konkreten Ergebnisse und Sourceidentitäten vorliegen; derzeit wird dieser Nachweis nicht behauptet. [E-NIGHT-R8-USER]

<a id="deepx-full"></a>
## 5. Historische DeepX-Full-Fehlerlokalisierung und fortgeltende Regressionen

Die nachfolgenden Versionen v26–v30 sind historische Quellenstände. Ihre Fehlerbeschreibungen sind keine neue .4-Aufgabenliste; spätere Korrekturen und heutige Gates stehen in Abschnitt 4 und 10–12.

### 5.1 Fehlerfolge v26 bis v30

| Stand / Befund | Ursache und dauerhafte Konsequenz |
|---|---|
| v26 Native Full: 3 versucht, 0 gültig, 0 Frames | `deepx_shared_prepared_input_manifest_missing`; tatsächliche Eingabe vor Wiederholungen auflösen und explizit weiterreichen. |
| v26 separater Full-Test | `decoded_pre_nms_values_invalid`; Runtime-Laden war nicht gleich abgeschlossene Detection. |
| v27 erste Kurzprobe | Verwendete eine bereits gelöschte temporäre Remote-Suite; kein Modelltest. Eigene isolierte Staging-Verzeichnisse statt alter Remote-Arbeitskopien. |
| v27 FIX1 | Staging erfolgreich; echte Rohausgabe zeigt den numerischen Auslöser. |
| v28 | Begrenzte Float32-Score-Randtoleranz umgesetzt; lokale Abnahme durch unnötigen `cv2`-Import blockiert. |
| v29 | Pillow ersetzt diesen unnötigen Import im vorbereiteten Full-Pfad; Software-Abnahme und echte Einzelbildprobe erfolgreich. |
| v29 normaler D-Lauf | 3 × 3.000 Frames erfolgreich berechnet, anschließend von separatem Semantik-/Quality-Prüfpfad abgelehnt. |
| v30 | Die fehlenden Pre-NMS-Übergänge, Merge- und Vorprüfungsregeln implementiert und offline positiv teilabgenommen. |

Quellen: [E-D26] [E-D29] [E-PROBE29] [E-V30].

### 5.2 Numerikregel – kein allgemeines Clipping

Der aufgezeichnete YOLO11l-Tensor ist Float32 mit Form `[1,84,8400]`. Alle 705.600 Werte sind endlich. Es gibt keine negativen Breiten/Höhen und keinen Klassenscore über eins; **21 Klassenscores** sind exakt `−2⁻²⁴ = −5,960464477539063e−8`. Die frühere strikt negative Prüfung verwarf deshalb den ganzen Output. [E-D26] [E-NUMERIK]

Die produktive Korrektur verwendet für entsprechend deklarierte Float32-Wahrscheinlichkeits-Scores eine absolute Randtoleranz `ε = 2⁻²³ ≈ 1,1920928955e−7`. Nur innerhalb dieser engen Randzone außerhalb `[0,1]` erfolgt eine Normalisierung auf **einer Verarbeitungskopie**. Größere Bereichsverletzungen, NaN/Inf oder unzulässige Boxgeometrie bleiben Fehler. Kein zusätzlicher Sigmoid, keine gelockerten NMS-Schwellen und keine geänderten AP-Margen. Historische Verträge werden nicht rückwirkend auf die neue Numerikregel umgeschrieben. [E-NUMERIK] [E-V30]

Die reale v29-Kurzprobe verarbeitet denselben Rohtensor bis zu zwei Detektionen. Die 21 negativen Originalwerte bleiben im gespeicherten Rohoutput erhalten. Das bestätigt die beabsichtigte Verarbeitungskopie, nicht die gesamte Detectionqualität. [E-PROBE29]

### 5.3 Warum v29 trotz erfolgreicher Inferenz noch rot war

Im normalen D-Lauf waren die drei Performanceprozesse erfolgreich, je 3.000 abgeschlossene Frames und kein Timeout. Der separate DeepX-Semantikdump behandelte `decoded_pre_nms` aber nicht wie der Messpfad und lieferte einen leeren Frozen-Vertrag. Der Merge erzeugte dadurch irreführende negative übergeordnete Postprocessingfelder. Unabhängig davon lehnte der zentrale DeepX-Loader den physischen Stage-Namen ab. Beides sind Integrationsfehler, nicht ein erneut fehlendes OpenCV oder ein weiterer GPU-Ausfall. [E-D29]

Die dort aufgezeichneten Full-Raten von ungefähr 20,960 / 20,957 / 21,408 FPS sind deshalb **diagnostische Werte eines damals nicht abgenommenen Fullpfads**. Die akzeptierten v29-D-Medianwerte DeepX→TRT `b003` 34,681 FPS und TensorRT Full 36,901 FPS gehören zu ihren konkreten erfolgreichen Nativepfaden, nicht zu einem neuen v31-Lauf. [E-D29]

### 5.4 Release-/Installationsbeleg v29

Der v29-Installationsnachweis auf Smartmirror2 dokumentiert `INSTALL_ACCEPTANCE=PASS`, `FINAL_STAGE=complete`, 1.130 Tests plus einen separat ausgeführten GUI-Test, insgesamt **1.131**. Die bestehende Venv und 26 Benutzerprofile blieben erhalten. Dieser abgeschlossene Zwischenstand bleibt historischer Nachweis; die heutige Aufgabe ist nicht, v29 erneut zu installieren. [E-INSTALL29]

<a id="energie"></a>
## 6. Energy- und Kalibrierungsvertrag

### 6.1 Primärgröße und physische Grenze

Primär ist die **kalibrierte, nicht idle-subtrahierte Full-System-Eingangsenergie** am u.RECS. `FS` beschreibt die physische Messgrenze; `native_only` die Workflowstufe. Diese Begriffe sind keine Alternativen. Für den direkten DC-Gain-Abgleich beschreibt die bisherige KB den 20-mΩ-Shunt R16 zwischen `Vsense_Input` und `9V_20V_IN` mit INA225; ein 5-V-Verbraucher hinter einem Wandler ist kein direkter Ersatz für denselben Eingangsstromsprung. Die konkrete sichere Hardwarebedienung folgt dem vorhandenen Aufbau und Kalibrierungsdialog. [E-KB, §6]

### 6.2 Geführter Gain-Abgleich bleibt die Methode

Der bestehende Ablauf umfasst geordnetes Abschalten von M.2 und Jetson, Stabilisierung, `idle_before`, nominal 0,5 A mit **Ist-Strom und Ist-Spannung**, `idle_between`, nominal 1,0 A mit Ist-Werten, `idle_after`, ausdrückliche Bestätigung `0 A / Output OFF`, Wiederherstellung und anschließend Fit/Gate. Es gilt `P_ref = I_actual × V_actual`; die nominale Sollzahl ersetzt nicht die tatsächliche Last. Für die beiden Lastpunkte werden die benachbarten Idlefenster gemittelt. [E-KB, §6]

Es bleibt ein enger DC-Gain-Abgleich, kein neues höhergradiges Kalibrierungsmodell. Die ursprünglichen unskalierten Werte bleiben getrennt auditierbar, beispielsweise in `full_system_input_unscaled_avg_power_w` und `full_system_input_unscaled_energy_total_j`. Ein verifizierter Faktor wirkt vor einem gegebenenfalls zulässigen separaten Idle-Abzug. [E-KB]

### 6.3 Fortschreibung gegenüber dem alten „Kalibrierung noch offen“

**Die pauschale alte TODO „FS-Gain erst noch aufnehmen und danach M.2-Idle“ ist für den späteren Lauf überholt.** Die 55 vorhandenen Energieaggregate des v29-Complete-Sets melden bereits verifizierte und angewendete FS-Gain-Faktoren vom 4. September. Für die 21 setup-lokalen TensorRT-Full-Zeilen melden sie zusätzlich verifizierte, angewendete neuere Idlewerte. [E-CS] [E-DOC]

| Setup | FS-Gain-Faktor laut Aggregaten | Aggregate mit verifiziertem/angewendetem Faktor | Separater M.2-Idlewert bei TensorRT Full |
|---|---:|---:|---:|
| DeepX | 0,9035075097 | 17/17 | 2,4350704536 W, angewendet bei 7/7 TRT-Full-Zeilen |
| Hailo-8 | 0,9136343897 | 19/19 | 2,0079536423 W, angewendet bei 7/7 TRT-Full-Zeilen |
| Hailo-10H | 0,8963972780 | 19/19 | 0,9667883103 W, angewendet bei 7/7 TRT-Full-Zeilen |

Diese Tabelle ist eine **read-only Zusammenfassung gespeicherter Runtime-Verifikationen**, keine neue metrologische Abnahme. Die vollständigen ursprünglichen Last-/Kalibrierungsdateien sind im verkleinerten Complete-Set-Debug-Pack nicht enthalten. Die FS-Verifikation nennt vorhandene lokale Evidencepfade und übereinstimmende erwartete/tatsächliche Datei-Hashes; daraus wird keine hier neu durchgeführte Prüfung der elektronischen Last konstruiert. [E-CS] [E-DOC]

Leere allgemeine `energy_calibration_manifest`-Felder bedeuten in diesem Paket nicht automatisch, dass gar keine Gain-Kalibrierung angewendet wurde: Die spezifischen `full_system_current_scale_*`-Felder dokumentieren sie separat. Diese Unterschiede dürfen im Bericht nicht miteinander verwechselt werden. [E-CS]

### 6.4 Historische Gategrenzen nicht still mit späteren Ist-Werten versöhnen

Die KB vom 3. September nennt als damalige Gain-Gates unter anderem mindestens 2 W Leistungssprung, höchstens 2 % Unterschied der Einzelfaktoren, höchstens 0,5 W Idle-Drift, höchstens 10 % Abweichung des Ist-Stroms vom Sollpunkt und einen Faktorbereich **0,90 bis 1,10**, einschließlich sicherer Wiederherstellung. Der spätere Hailo-10H-Aggregatwert 0,8963972780 liegt knapp unter dieser damaligen Untergrenze, wird vom späteren Lauf aber als verifiziert ausgewiesen. [E-KB, §6.3] [E-CS]

**Dokumentationsgrenze:** Ohne den zugehörigen ursprünglichen Kalibrierungsbeleg und seine effektive Gateversion wird hier weder eine geänderte Grenze erfunden noch die spätere Messung pauschal verworfen. Vor einem darauf gestützten metrologischen Claim den bereits vorhandenen Beleg heranziehen. Dies ist kein Auftrag zu blindem Neukalibrieren oder nachträglicher Grenzwertlockerung. Die älteren v14-Idlewerte bleiben historische Werte und werden nicht mit den späteren Zahlen vermischt.

### 6.5 Messdauer: 165 gültige Replikate sind keine 60-Sekunden-Abnahme

Die 55 geplanten Energiezeilen des v29-Complete-Sets enthalten **durchgehend `duration_s=1.0`**, FS und `command`. Alle Aggregate melden drei gültige Replikate und eine konfigurierte Lastdauer von 1 s. Tatsächliche Command-, aktive Fenster- und Collectorzeiten sind eigene Felder und können davon abweichen. [E-CS] [E-DOC]

Damit ist die Sammlung von **165 gültigen kurzen Replikaten** belegt, nicht ein neuer Langzeit-/Stabilitätsnachweis mit 60 s × 3. Der bereits früher dokumentierte längere Energie-Abnahmeumfang bleibt ein eigener Vertrags- und Konfigurationscheck vor dem Final-Lauf; die kurze Diagnosekonfiguration darf nicht unbemerkt als dessen Ersatz gelten. Messdauer, Zahl der gültigen Wiederholungen und tatsächliche Work Units vor dem Start prüfen. [E-KB15] [E-PLAN31]

### 6.6 Methoden- und Freigabeebenen

Die betrachteten Aggregate nennen `command_marker_window` als wissenschaftliche Primärmethode und `chapter4_legacy_window` als Shadow-Methode; die Primärgröße heißt `calibrated_input_energy_unsubtracted`. Ein Shadow-/A/B-Fenster wird nicht automatisch zur besseren Primärmethode gewählt. Bereits eingefrorene Methodenentscheidungen bleiben bestehen. [E-CS]

Die 55 erfolgreichen Energiezeilen sind trotzdem `raw_energy_quality_not_qualified`. Ein gespeicherter globaler Grund ist `incomplete_expected_native_matrix`; bei einzelnen Fällen kommen lokale Quality-/Endpointprobleme hinzu. Deshalb getrennt ausweisen: **Messung erfolgt**, **Replikate vollständig**, **Zeilenqualität bestanden**, **Paarung passend**, **Kampagnenmatrix vollständig**, **wissenschaftlich freigegeben**. Keine dieser Aussagen ersetzt die anderen. [E-V30, §7] [E-PLAN31, AP9]

### 6.7 Power-Mode und Idle-Fairness

Vor dem final beanspruchten Vergleich die tatsächlich verwendeten `nvpmodel`-/Clock-/Governor-Einstellungen, thermische Bedingungen und relevante Peripherie aller Setups dokumentieren. Ein niedriger DeepX-Idlewert ist allein kein Messfehler. Neue Gain-/Idlewerte oder schnelle Smokes beweisen noch keine identischen Powerbedingungen aller späteren Energiepfade. Vorhandene gültige Kalibrierungen nutzen; nur bei geänderter Messkette, ungültiger Bindung oder konkretem Problem gezielt neu aufnehmen. [E-KB] [E-PLAN31]

### 6.8 Spätere Nachtläufe sind neue, getrennte Energiebelege

Im v2.80.1-Lauf vom 10. September liefen 21 Vendor-Full-Kombinationen mit 63 gültigen Performancewiederholungen und 63.000 gemessenen Frames. Die Energie sammelte 21/21 ausführbare Planzeilen mit 63 gültigen Replikaten; die 63er-Gesamtmatrix blieb unvollständig. Die folgende Zwei-Split-Nacht hatte eine 84er-Matrix und ebenfalls 21 erfolgreiche Vendor-Full-Fälle. Diese verschiedenen Nenner nicht vermischen. Beide kurzen Energieumfänge waren Screening, kein neuer 60-s-×-3-Nachweis. [E-WORKFLOW-HISTORY]

Der am 12. September abgebrochene .3-Nachtlauf wartete dagegen noch in der zentralen Qualityphase; seine anschließende Native-/Energiestufe war im beobachteten Abschnitt nicht gestartet. Das ist kein Verlust früherer Energieresultate. Gleiche `MAXN_SUPER`-Namen auf den Setups bewiesen außerdem keine identischen tatsächlichen Clock-/TPC-Einstellungen; die beobachtete TPC-Maskenabweichung bleibt für konkrete Setupvergleiche zu erklären, ohne aus ihr allein eine Kernanzahl oder Defektursache zu raten.

### 6.9 Collector-Lebenszyklus, normale Integration und Quellenbudget bis R8

Der frühe Hostpfad beendete nach einem kurzen Command den Empfang ungefähr nach 13 s, obwohl `-d=17s -b=5s -e=5s` eine nominelle 27-s-Geräteaufnahme anforderte. Eine private Rustkorrektur wartete auf den regulären Protokollabschluss und begrenzte Fehlerpfade. Das allein bewies noch keinen stabilen Wiederanlauf: In der R5-Fortsetzung fehlten bei der zweiten Aufnahme Endpaket und ein Teil der empfangenen Counterspanne. Die vollständige alte Transportursache bleibt ungeklärt. **Warten/Drain verlängert nicht das primäre Command-Messfenster.** [E-CX-R4] [E-CX-R5] [E-CX-AUTO]

R6 ergänzte GO-/Datagramm-/Counter-/Ende-/Socketdiagnostik. Zwei Diagnosen und drei Energieaufnahmen funktionierten; der finale Kandidat lieferte bestätigte Protokoll-/Sourceabschlüsse. Diese Einzelquellenabnahme darf nicht auf alle Geräte oder Langzeitlast übertragen werden. Ein altes fehlendes Endpaket ist ein ungültiger damaliger Abschluss, kein unbegrenzter Beweis eines heute noch aktiven Geräts. Neue Zustandsdiagnosen müssen trotzdem ausdrücklich geplant und begrenzt sein; kein automatischer Budgetreset. [E-CX-R6]

**Seit R8 normal integriert:**

```text
Collector: ~/.onnx_splitpoint_tool/collectors/r6-reviewed/urecs-data-collector
SHA256:    913c3f745a71809d85c1e98f56d0ca3265bb5e5492ad2b72407f7ce9bd8c3a46
Config:    ~/.onnx_splitpoint_tool/hardware_setups.yaml
Spiegel:   ~/.onnx_splitpoint_tool/energy_config.yaml
Runmodi:   ~/.onnx_splitpoint_tool/run_modes.yaml  (Schema 14)
```

R8 hat die vorhandenen abgenommenen R6-Bytes kopiert, keinen weiteren Rustbuild durchgeführt. Originalcollector, Kalibrierung, Adressen, Venvs und Caches bleiben erhalten. Die enge explizite Installation nutzt vorhandene Locks, Backups, atomare Writes und Rechte-/ACL-Erhalt; zweiter Aufruf idempotent. Konflikt mit ausdrücklich anderem Collector ist kein Anlass für stillen Ersatz. Absolute Collectorpfad-/Bytebindung wird im Start-Snapshot eingefroren und vor Spawn geprüft. Full, Split und das gemeinsame Probe-Leaf verwenden denselben Energie-Registry-Snapshot. `URECS_RECEIVE_DIAGNOSTICS=1` wird produktseitig gesetzt; kein privater Terminalexport für normale neue GUI-Läufe nötig. [E-CX-R8-CONFIG] [E-CX-R8]

Fehlende `task_budget`-Policy erhält bei neuen aktiven, zentral konfigurationsfolgenden Läufen `enabled:true`, `max_retries:1`, `max_transport_failures:2` mit Herkunft `product_default`. Explizites `enabled:false` bleibt sichtbar ungeschützt, nicht still überschrieben. Frozen Resumes behalten den ursprünglichen Vertrag. Drei Sollreplikate mit maximal einem Retry ergeben höchstens sechs Ketten **je Zeile**, nicht sechs für die gesamte Kampagne. Ein unbewiesenes Sourceende sperrt weitere Starts derselben Messquelle auch über Full/Split/Probe hinweg; andere Quellen und bereits gültige Ergebnisse werden nicht erfunden oder gelöscht. Exakte Laufpolicy aus dem neuen Snapshot lesen. [E-CX-R8]

### 6.10 Mess- und Berichtszähler, Statistik und verbleibende Energieabnahme

Getrennt zählen: geplante Zeilen; logisch angeforderte Replikate; tatsächlich begonnene Preflightketten; tatsächliche Collectorstarts; Lastausführungen; gültige ausgewählte logische Replikate; vollständig verifizierte Ergebniszeilen. Ein Retry ist kein viertes unabhängiges Sollreplikat. Ein fehlender historischer Versuchszähler bleibt unbekannt. Der R8-Dialog zeigt Zeilen, gültige Replikate und Collectorversuche getrennt. [E-CX-R8]

Der R7-Standardlauf belegt 183 Sollreplikate, 159 zusätzliche Retries, 342 Collectorstarts, 24 gültige Einzelaufnahmen und keine vollständige 3/3-Zeile. Zusätzlich drei Aufrufe der getrennten Fensterprobe (einer gültig). Das ist kein Widerspruch zum früheren R6-PASS: normale GUI und privater Test verwendeten nicht dieselbe Collector-/Policybindung. R8 schließt diese Produktlücke mit neun realen Erstaufnahmen aus der normalen GUI. [E-R7-RUN] [E-CX-R8]

Der Student-t-Faktor für kleine Stichproben wurde in der Codex-Reihe korrigiert: bei n=3 und zweiseitigen 95 % rund **4,302653 statt 4,171205**. Historische Intervalle bleiben historische Ergebnisse; Neuberechnung aus vorhandenen Replikaten separat ausweisen, Mittelwerte und Rohtraces nicht ändern. Drei gültige kurze Aufnahmen sind weder ein belastbarer Langzeitstabilitätsnachweis noch automatisch ein Vergleichsclaim. [E-CX-R1] [E-CX-R2]

Aktuell fehlt noch die Auswertung des laufenden Nachtlaufs über alle tatsächlich beteiligten Messquellen. Eine erneut auftretende Quellsperre wird als fehlende nachfolgende Messung berichtet, nicht als erfolgreicher wissenschaftlicher Abschluss. Der optionale vollständige Window-Probe-Coordinator wurde in R8 nicht erneut hardwareseitig ausgeführt; nur gemeinsamer Binding-/Budgetpfad lokal geprüft. [E-CX-R8] [E-NIGHT-R8-USER]

<a id="deepx-r1-r2"></a>
## 7. Abgeschlossene Qualitätsbefunde und eng begrenzte Diagnosen

### 7.1 DeepX-Preprocessing: kein weiterer Adapterprototyp

Die historische R1/R2-Reihe bestätigte den vorhandenen Mean/Std-Sub/Div-Buildadapter. Für passende Klassifikationsmodelle bleibt `imagenet_mean_std` der normale Arm; ein explizites `current_scale_only` in einem Profil übersteuert einen Modusdefault und ist weiter als Legacy-/Diagnosewahl zu erkennen. Das Zurücksetzen eines zentralen Modus korrigiert keine explizite Nutzerprofilwahl.

R1: drei Klassifikationsmodelle; Native-/Quality-Feed und Outputs auf den jeweiligen 16 Hardwarebildern gleich. R2: zwei echte private neue Mean/Std-DXNNs, vier Adapterkontrollinputs pro Modell exakt gleich; MobileNet im kleinen A/B 11/16 → 12/16 gegenüber CPU 13/16, ResNet 12/16 → 15/16 gegenüber CPU 14/16. Kleine Nenner und Logitähnlichkeit belegen keine allgemeine Accuracyverbesserung oder B5000-Freigabe. Die alte Forderung, zuerst nochmals denselben R1/R2-Adapter-Smoke zu wiederholen, entfällt. [E-R1] [E-R2]

### 7.2 MobileNet: B5000-FAILs statt pauschal „Qualität offen“

Der .4-Plan dokumentiert für die bereits abgeschlossenen zentralen 5.000-Bilder-Aufträge folgende Top-1-Ergebnisse des jeweiligen bisherigen Artefakts:

| Variante | Top-1 | Differenz zur CPU | Entscheidung |
|---|---:|---:|---|
| Originale CPU-Referenz | 73,70 % | — | Referenz |
| Hailo8 Full, auf CPU gebautes HEF | 60,62 % | −13,08 pp | FAIL |
| Hailo10H Full, auf CPU gebautes HEF | 59,42 % | −14,28 pp | FAIL |
| DeepX Mean/Std Full | 71,72 % | −1,98 pp | FAIL |

Die Werte wurden zunächst aus Plan/Q5 fortgeführt. Im jetzigen REV2-Abgleich liegt der ursprüngliche zentrale Qualitätssnapshot im `har_and_git_evidence.zip` vor: Ergebniszustände, Identitäten und gespeicherte Aggregate wurden direkt gelesen. Keine neue Berechnung aus Rohvorhersagen und keine nachträgliche Erweiterung des damaligen .4-Build-Prüfumfangs. [E-NIGHT-QUALITY] Die früheren „MobileNet erst noch erstmals größer bewerten“-TODOs sind mit diesen benannten abgeschlossenen Befunden überholt. Die genaue interne Verlustursache und die B5000-Qualität eines anderen privaten GPU-HEFs sind andere Fragen. [E-2804-PLAN, §8.2]

Frühe MobileNet-Splits b027/b056 sind laut Plan deutlich besser als Full/b135, aber nicht automatisch innerhalb der Marge. Keine nachträgliche Beschränkung der Finalmatrix auf die besseren Grenzen. Ein Stufenvergleich benötigt die passende Float-P1-Referenz für genau dieselbe Boundary.

### 7.3 Hailo8 Fixed16: Runtime-PASS mit unterschiedlichen Accuracyzahlen

| Variante auf denselben 16 IDs | Top-1 | Top-5 |
|---|---:|---:|
| Original-ONNX | 13/16 | 14/16 |
| Compiler-ONNX | 13/16 | 14/16 |
| CPU-HEF, ausgeführt auf Hailo8 | 8/16 | 14/16 |
| Privates GPU-HEF, ausgeführt auf Hailo8 | 10/16 | 15/16 |

Die Q2-Terminalquelle meldet G3-PASS, sechs geänderte Top-1-Klassen mit zwei zusätzlichen richtigen Treffern und sauberen Abschluss. Original-/Compiler-ONNX sind auf der Probe numerisch identisch. Gleichheit betrifft die tatsächlich erfassten FLOAT32-VStreaminputs; interne UINT8-Puffer wurden nicht beobachtet. Input-QuantInfo: `qp_scale=0.01872340589761734`, `qp_zp=114`. Der Plan benennt 32 erfolgreiche Inferenzen und einen unabhängigen Labelvergleich aus Q1. Nur soweit Q1 tatsächlich verfügbar ist, wird dessen Recount in der .4-Verifikation unabhängig bestätigt. [E-2804-H8-Q2] [E-2804-PLAN, §1.3]

Keine Behauptung „GPU verbessert generell Accuracy“ und kein automatischer Austausch des produktiven CPU-HEFs. Der private Build behält seine eigene Artefakt- und Qualitätsidentität. Die laut Plan etwa 520,2 s CPU-Bauzeit und 528,8 s GPU-Bauzeit belegen keinen Speedup. Ein Component-View mit ptxas/libdevice ist kein vollständiges CUDA-Toolkit.

**Fortschreibung:** Die erste Emulation der vorhandenen Parsed-/Quantized-HARs ist ausgeführt; siehe §7.7. Das frühere `not_available` im Fixed16-Runtimebericht bleibt als damaliger Zustand unverändert. Die zusätzliche optimierte Floatstufe und die kontrollierte Integer-I/O-Ursachenprüfung wurden nicht ausgeführt und sind jetzt ausdrücklich als optionale Folgearbeit zurückgestellt (§7.8). Es folgt daraus weder eine neue GPU-/G3-Releasepflicht noch eine Voraussetzung zum Berichten der vorhandenen Negativergebnisse. [E-SCOPE-REV3]

### 7.4 Hailo10 Fixed16 separat halten

Der frühere v2.79.34-MobileNet-Test auf Hailo10 lieferte für CPU- und GPU-HEF jeweils 12/16 Top-1 und 15/16 Top-5 gegenüber ONNX 13/16 und 14/16. Beide HEFs wurden technisch ausgeführt; der echte Hailo10-GPU-Build war zuvor erfolgreich. Diese Zahlen gehören nicht zum neuen Hailo8-Test und werden nicht vermischt. [E-2804-CHAT]

### 7.5 YOLO11l/Hailo10H: 5.000-Bilder-Untersuchung abgeschlossen

| Variante | AP50:95, Skala 0–100 | Differenz zur CPU | Zentraler Entscheid |
|---|---:|---:|---|
| CPU-Referenz | 46,4781 | — | Referenz |
| TensorRT Full | 46,4609 | −0,0172 pp | PASS |
| Hailo10H Full | 45,0829 | −1,3953 pp | FAIL |
| Hailo10H → TensorRT, b062 | 45,3656 | −1,1125 pp | FAIL |

Vollständige CPU-/Kandidatenvorhersagen umfassen dieselben 5.000 Bilder; Fingerprints und AP-Reproduktion wurden geprüft. Der Normalworkflow lief technisch durch, verwendete vier passende vorhandene Artefakte ohne Cold Build und schloss Native-/Remote-Prozesse ab. Der Hailo-Punktentscheid unterschreitet bereits die unveränderte 1-pp-Marge; 0 tatsächlich ausgeführte Bootstraps im dokumentierten frühen FAIL-Pfad sind kein fehlender Inferenzlauf und kein berechnetes Konfidenzintervall. TensorRT wurde mit dem vorgesehenen Statistikpfad bewertet. [E-2804-QUALITY]

Die AP-Verluste betreffen viele Klassen; ein allgemeiner Decoderfix ist aus diesen Daten nicht nachgewiesen. Der historische 500-Bilder-Lauf zeigte für dasselbe Full-HEF bereits ähnliche Verluste: Full −1,3337 pp, Split −1,1486 pp. Der neue Umfang bestätigt den Befund, er repariert ihn nicht.

Der zentrale Qualitätsvertrag ist abgeschlossen ausgewertet. Der ursprünglich nicht verfügbare zusätzliche offizielle COCOeval-Bericht bleibt ausdrücklich getrennt; eine eventuelle Ergänzung verwendet vorhandene Vorhersagen und Originalannotation ohne neuen Hailo-Build oder Hardwarelauf. Eine allgemeine wissenschaftliche Freigabe sämtlicher Modelle/Backends folgt daraus nicht.

### 7.6 Historischer Opt2-Versuch und verbindliche Entscheidung

Die Results-KB vom 3. September dokumentiert für YOLOv7/Hailo8 AP50:95 41,478 bei Opt1 und 40,984 bei Opt2; Opt2 war rund 0,494 pp schlechter. Der Opt1-Wert ist zusätzlich im archivierten Paper-Primärergebnis enthalten; ein vollständiger zugehöriger Opt2-Rohbericht wurde im bereitgestellten Archiv nicht gefunden. Der Befund ist daher kein neuer direkter A/B-Nachweis für YOLO11l/Hailo10H.

Die Projektentscheidung bleibt dennoch eindeutig: balanced/Opt1/B500/Batch8 beibehalten, kein pauschaler Optimierungs- oder Kalibrationsgrößen-Sweep auf den Evaluationsmodellen. Der zwischenzeitlich vorgeschlagene Opt2/B1024-Neubau und automatische Opt3-Folgeversuch wurden nach dem historischen Abgleich verworfen. Das ist eine abgeschlossene Entscheidung, kein noch auszuführender Test. [E-2804-ABGLEICH]

### 7.7 Hailo8 HAR-R1: erste große Verluststelle lokalisiert

Primärquelle: `har_and_git_evidence.zip`, Run `hailo8_har_git_20260912T171411Z_x0j2t2o1`. Die beiden HAR-Stufen liefen mit DFC 3.33.1 auf der CPU, dieselben bereits geöffneten 16 Bilder und tatsächlich aufgezeichneten FLOAT32-NHWC-Feeds. Neue HEF-Builds, Optimierung, Hardwareinferenzen, Energie und Bootstrap: **nicht ausgeführt**. Parsed-Emulation dauerte laut Prozessbericht 13,75 s, Quantized-Emulation 31,30 s; daraus folgt keine Leistungskennzahl für Hardware. [E-HAR-R1]

| Stufe | Top-1 | Top-5 |
|---|---:|---:|
| Original-ONNX | 13/16 | 14/16 |
| Compiler-ONNX | 13/16 | 14/16 |
| Parsed-HAR / `SDK_NATIVE` | 13/16 | 14/16 |
| Quantized-HAR / `SDK_QUANTIZED` | 9/16 | 13/16 |
| Privates GPU-Build-HEF auf Hailo8 | 10/16 | 15/16 |
| Historisches CPU-Build-HEF auf Hailo8 | 8/16 | 14/16 |

| Vergleich | Max. absoluter Logitfehler | RMS | Mittlere Cosine | Top-1-Wechsel |
|---|---:|---:|---:|---:|
| Original → Compiler-ONNX | 0 | 0 | 1,0 | 0/16 |
| Compiler-ONNX → Parsed-HAR | 0,000009775 | 0,000001469 | ≈1,0 | 0/16 |
| Parsed-HAR → Quantized-HAR | 4,919190 | 0,701965 | 0,721879 | 5/16 |
| Quantized-HAR → GPU-HEF | 2,394485 | 0,392645 | 0,904432 | 4/16 |

Die Klassenlisten wurden erneut unabhängig nachgezählt. Logitstatistiken bleiben Resultate des ausgeführten Collectors, weil Roharrays nicht im ZIP liegen. Parsed und Compiler-ONNX besitzen auf allen 16 Bildern dieselben geordneten Top-5. Parsed → Quantized verliert vier zuvor richtige Entscheidungen, ein weiterer Wechsel bleibt falsch. Quantized → Hardware korrigiert zwei Antworten, verschlechtert eine und wechselt eine andere falsche Klasse. Ähnliche Trefferzahlen beweisen folglich keine gleiche Ausgabe. [E-KB-REV2-CHECK]

**Befund:** Die wesentliche Abweichung ist bereits im DFC-Übergang zur optimierten/quantisierten Darstellung vorhanden. Tool-ONNX-Anpassung und Parsing erklären sie in dieser Probe nicht. **Keine stärkere Behauptung:** Der Übergang umfasst mehr als reine Rundung; eine separate optimierte Floatdarstellung fehlt noch. Der API-Snapshot zeigt 101 Parsed- gegenüber 89 Quantized-HN-Layern. Das kann Transformations-/Fusionsfolgen widerspiegeln und ist allein kein Defektbeweis.

**Emulation → Hardware bleibt relevant abweichend.** Keine pauschale Bitgenauigkeitsannahme und keine Behauptung, dieser Rest sei bereits vollständig als Rundung erklärt. Bisher beobachtet: identische FLOAT32-Hostfeeds und QuantInfo, nicht die internen UINT8-Eingänge. HailoRT 4.20.0: Inputscale 0,01872340589761734 / ZP 114; GPU-HEF-Outputscale 0,06651347130537033 / ZP 75. CPU-HEF-Outputscale nicht stellvertretend verwenden. [E-H8-RUNTIME]

HARs sind laut ursprünglichen Buildpfaden dem privaten GPU-Build zugeordnet; ihre Hashes wurden erst bei dieser Emulation aufgenommen. Das bestätigt verwendete Dateien und damalige Unverändertheit, aber keine rückwirkende Byteattestation zum Buildzeitpunkt. Für den älteren CPU-Build liegt kein zugehöriges Quantized-HAR vor. Kein Übertragen der neuen HAR-Ursachenlokalisierung als vollständige Erklärung seines 5.000-Bilder-Verlusts.

### 7.8 Weitergehende Ursachenklärung – zurückgestellte optionale Folgearbeit

**Status seit REV3: ZURÜCKGESTELLT, nicht beauftragt, nicht ausgeführt.** Die technische Hailo8-Vorabprüfung und die erste HAR-Fallstudie sind abgeschlossen. Die vorhandenen Ergebnisse reichen für die begrenzte Aussage über das automatische Verfahren unter dem festen Rezept; eine lückenlose interne Ursachenerklärung wird für diese Hauptaussage nicht verlangt. Die zusätzliche Emulations-/Hardwareabweichung bleibt ausdrücklich unerklärt. Das ist weder ein pauschaler Runtime-Fehlerfreiheitsnachweis noch ein Beleg für ausschließliche Quantisierungsursächlichkeit. [E-SCOPE-REV3]

Der frühere Begleitplan `DIAGNOSEPLAN_Hailo8_Optimierung_Quantisierung_Runtime_2026-09-12.md` bleibt unverändert als optionale technische Skizze erhalten. Er ist **kein nächster Pflichtschritt**, kein .4-Releasegate und kein Abschlussgate der derzeitigen Hauptauswertung. Erst ein neuer ausdrücklicher Auftrag zur stärkeren Ursachenfrage würde folgende Schritte reaktivieren:

| Schritt | Unveränderte Artefakte / konkrete Kontrolle | Aussageziel |
|---|---|---|
| A | Vorhandenen Quantized-HAR in einer optimierten Floatdarstellung auswerten (`SDK_FP_OPTIMIZED`, Verfügbarkeit und Zustand in DFC 3.33.1 vorher prüfen) | Floatoptimierung von anschließender Quantisierungsverarbeitung trennen |
| B | Dasselbe GPU-HEF und dieselben 16 Arrays über FLOAT32- und explizit quantisierte UINT8-Ein-/Ausgaben vergleichen | Hostquantisierung, Rundung/Clipping, Layout und Outputdequantisierung isolieren |
| C, nur bei weiterem Rest | Zugängliche korrespondierende Emulator-Zwischenoutputs und QuantInfo untersuchen; Herstellerfall bei nicht zugänglichen inneren Hardwarewerten | Erste verbleibende materielle Abweichung eingrenzen |

Bei einer später ausdrücklich beauftragten Wiederaufnahme wäre die erste 2×2-I/O-Kontrolle auf höchstens 64 neue kurze Inferenzen begrenzt; sie ist jetzt nicht auszuführen und keine neue G3-/Compute-/Buildschleife. **Die tatsächliche HailoRT-Rundungsregel prüfen**, nicht `numpy.round` ungeprüft verwenden. Keine doppelte Normalisierung oder Quantisierung; Emulatorkontext muss seine Eingangsdomäne explizit erklären. Ohne zugängliche passende optimierte Floatrepräsentation bleibt diese Stufe `not_available` – keine automatische Neuoptimierung.

Ein Stufendump des Softwareemulators ist nicht automatisch ein Hardware-Layerdump des unveränderten HEFs. Zusätzliche Outputendpunkte durch Neucompilierung könnten das Mapping verändern und wären ein gesonderter Eingriff. Ein solcher Build ist nicht Bestandteil des aktuellen Vorschlags.

**Endregel auch für eine spätere Wiederaufnahme:** Ein auf festen Inputs und einem konkreten Artefakt unauffälliger Runtimevergleich erlaubt eine auf diesen Scope begrenzte Aussage, keine universelle Gleichheit. Bleibt der Rest unerklärt, wird er dokumentiert; kein Nachoptimieren bis PASS. Numerische RMS-/Cosinewerte liefern keine additiven Prozentanteile des Accuracyverlusts. Diese Diagnose blockiert weder die kleinen .4-Softwarefixes noch die Dokumentation der vorhandenen korrekt ausgewerteten negativen Ergebnisse. [E-DIAGNOSE-PLAN] [E-HAILO-OPT-DOC] [E-SCOPE-REV3]

### 7.9 Abgeschlossene Qualitypopulation des abgebrochenen Nachtlaufs

Im originalen zentralen Report: 123 Requests, 63 vollständig ausgewertet (**43 PASS, 18 FAIL, 2 INCONCLUSIVE**) und 60 ohne fertigen Qualitätsvergleich (**4 CancelledError, 56 QualityServiceClosedError**). Alle sieben CPU-Referenzprozesse waren erfolgreich mit je 5.000 Einträgen. ResNet hatte 19 abgeschlossene PASS-Aufträge; YOLO11l in dieser Nacht 10 PASS, 6 FAIL, 2 INCONCLUSIVE. Der separate spätere YOLO11l/H10-Umfang aus §7.5 bleibt seine eigene Quelle. [E-NIGHT-QUALITY]

MobileNet-H8 b027: 71,58 %; H10 b027: 72,22 % gegenüber CPU 73,70 %, jeweils außerhalb der unveränderten 1-pp-Marge. Frühere Generic-5.000-Diagnostik b056: H8 71,38 %, H10 71,42 %; nicht rückwirkend als im gecancelten Run zentral abgeschlossene b056-Aufträge deklarieren. Full/b135 und frühe Splitpunkte dürfen nicht zu einem einzigen „Hailo-Splitwert“ vermischt werden.

Ein früher Punktwert-FAIL mit vollständigen Vorhersagen und ausgelassenem Bootstrap ist im bestehenden Vertrag fertig ausgewertet; das CI bleibt `null`. Statistischer PASS, Point-FAIL und INCONCLUSIVE sind getrennt. Der Cancel ändert die 18 fertigen FAILs nicht und beweist keine späteren Ergebnisse für die übrigen Modelle.

### 7.10 Aufwand der zurückgestellten Vertiefung – keine neue Terminplanung

Die folgende grobe Einschätzung stammt aus der Scope-Diskussion, nicht aus gemessenen Laufzeiten. Sie nimmt eine mit dem Projekt vertraute Person, vorhandene Artefakte und erreichbare lokale Umgebungen an. Arbeitsanteile überlappen; sie sind nicht exakt addierbar. Unzugängliche Internas oder notwendige Herstellerunterstützung können den Aufwand wesentlich erhöhen. [E-SCOPE-REV3]

| Optionaler Zusatzumfang | Grobe Arbeitsaufwandsschätzung, kein Auftrag / keine Zusage |
|---|---|
| Vorhandene optimierte Floatstufe prüfen und vergleichen | Einige Stunden bis etwa ein Arbeitstag, sofern die Darstellung zugänglich ist |
| Float-/Integer-I/O-Gegenprobe mit exakter Quantisierung, Tests und Auswertung | Etwa ein bis drei Arbeitstage |
| Verbleibende interne Abweichung layerweise oder mit Herstellerhilfe erklären | Mehrere Tage bis Wochen; bei fehlenden Internas nicht verlässlich begrenzbar |
| Modellspezifische Tuningstudie über mehrere Netze und unabhängige Bestätigung | Eigenes Experiment über mehrere Tage bis Wochen, ohne Erfolgsgarantie |

Kurze Einzelinferenzen bedeuten nicht automatisch geringen Gesamtaufwand: Diagnoseimplementierung, versionsgebundene API-/Numerikprüfung, Absicherung und Interpretation sind zusätzliche Arbeit. Für die aktuelle Hauptfrage wird dieser Aufwand **nicht vor den Abschluss der regulären Auswertung gestellt**. Die Aufwandsschätzung ist keine Begründung, bekannte eigene Fehler zu ignorieren; sie erklärt die Entscheidung gegen eine weitergehende unbestellte Ursachen- und Optimierungsstudie.

### 7.11 Hailo10 YOLO26: reparierter Resolver ist kein reparierter Output

R2 korrigierte einen **Diagnose-Bindingresolver**, der eingebettete Artefaktevidenz mit einem vollständigen Binding verwechselte. Danach konnten vorhandene HEF/Bridge/TRT-Ausgaben verglichen werden. Generic und Native verwendeten im untersuchten Fall denselben Boundarypuffer. Die geprüften Quantisierungsschritte von ungefähr **3,492075 (YOLO26m)** bzw. **3,161274 (YOLO26s)** verlieren in der getesteten UINT8-Referenzkontrolle die kleinen Klassenscores. Diese Beobachtung ist enger als die ursprüngliche Vermutung eines bloßen Layoutfehlers, aber kein universeller Beweis eines bestimmten Compilerbugs. [E-CX-R2]

Für **YOLO26m b398 und YOLO26s b364** bleiben Nullausgaben offen: im v2.82-Nachtlauf jeweils 5.000, im R7-Standardlauf jeweils 500 leere Detektionslisten. Erfolgreiche Prozess-/Performanceausführung macht sie nicht zu gültigen Completed-Detection-Ergebnissen. Kein numerischer Produktfix, neuer präzisionsgeänderter HEF-Vertrag oder allgemeiner H10-Quality-PASS wurde in R2–R8 daraus erzeugt. Nach stabiler Ablaufabnahme ist genau diese begrenzte Output-/Qualitätsfrage wieder aufzunehmen; keine spontane Sigmoid-, Clipping-, NMS- oder Margenänderung. [E-NIGHT-282] [E-R7-RUN] [E-CX-R8]

### 7.12 DeepX YOLO26s: die zwei alten Fehlerbilder bleiben eigene Fälle

Full-YOLO26s scheiterte im 5.000er-Umfang an `000000052891.jpg` und `000000395801.jpg`: `ordered_xyxy_fraction`, anschließend kein zentraler Full-Qualityrequest. Die gezielten R2-Aufnahmen reproduzierten invertierte XYXY-Boxen mit positiven Scores; Padding als harmlose Ursache wurde nicht nachgewiesen. Ein separater Diagnose-Ausgabeadapterfehler wurde lokal korrigiert, nicht die native Geometrie. [E-NIGHT-282] [E-CX-R2] [E-CX-R3]

Im R7-Standardlauf bestand Semantik für 500/500 Bilder; die zwei bekannten Fehlerbilder waren **nicht in dieser Teilmenge**. Dadurch entstand erstmals im betreffenden Standardrun ein vollständiges zentrales Full-Ergebnis, das trotzdem Quality-FAIL ist. Das ist keine Reparatur des 5.000er-Falls. Beim neuen Nachtlauf Bildpopulation prüfen und, falls die beiden Fälle wieder betroffen sind, genau diese Ursache berichten. [E-R7-RUN]

### 7.13 H8 und Qualitätsdarstellung nach R8

Die Weitergabe der drei Felder `semantic_evidence_repetition_index`, `semantic_evidence_repetition_id` und `semantic_evidence_runtime_instance_id` sowie die passende Fehlerklassifikation wurden repariert. YOLOv7/b044 und YOLO11l/b062 bestehen im späteren R7-Run ihre nativen Semantik-/Vertragsprüfungen; zentrale Qualityentscheidungen bleiben davon getrennt. Kein neuer H8-Nachweisauftrag allein wegen späterer Collectorprobleme. [E-CX-R1] [E-CX-R2] [E-R7-RUN]

Die generische Numerik-/Annotationsprüfung kann von der zentralen Taskqualität abweichen. Im R7-Run: 29 `valid`, 19 `invalid`, acht `runtime_contract_only`; sieben generisch negative Fälle bei zentralem Quality-PASS. Das sind unterschiedliche Vergleichsachsen und kein pauschaler Beweis von 19 Runtimeabstürzen. R8 verbessert diese Trennung im Bericht, ohne bestehende wissenschaftliche Gates abzuschalten. [E-R7-RUN] [E-CX-R8]

### 7.14 Aktuelle Priorität der Qualitätsarbeit

Zuerst den laufenden Nachtlauf technisch und hinsichtlich Messvollständigkeit prüfen. Danach H10-Nulloutputs, den DeepX-Zweibilderfall und weitere tatsächlich beobachtete Qualityabweichungen priorisieren. Der Nutzer wünscht anschließend deren Prüfung; **das ist keine Erlaubnis für unbeschränkte Modelltuningsweeps**. Korrekt gebundene negative Ergebnisse können abgeschlossen bleiben. Eigene Implementierungsfehler weiterhin gezielt korrigieren; Daten-, Compiler- und Akzeptanzverträge nur in ausdrücklich getrennten Experimenten ändern. [E-CX-PREF] [E-NIGHT-R8-USER]

<a id="abschluss"></a>
## 8. Cache, Prozessgrenzen und terminaler Abschluss

Eine GPU-Buildpräferenz, GPU-UUID oder ein Overlaypfad sind Buildprovenienz, keine zusätzliche Modellcache-Identität. Der normale Builder prüft erst Modell-/Recipe-/Artefaktvertrag, dann positiven Cache bzw. genaue negative Compileevidenz. Nur ein tatsächlich erforderlicher Neubau benötigt den GPU-/Overlaykontext. Ein inzwischen fehlendes Overlay darf einen gültigen CPU-HEF-HIT nicht verhindern.

HEF, Receipt und Cachemetadata behalten ihre bestehenden atomaren Generationen-/Publikationsregeln; alte HEF-only-Bestände bleiben gegebenenfalls `legacy_unsealed`. Duplicate-/Generationauswahl bleibt deterministisch. Kein „neueste Datei gewinnen lassen“, kein Auswählen nach besserer Accuracy und kein automatisches Publizieren privater GPU-HEFs. Ein anderes tatsächlich verwendetes Artefakt braucht korrekt gebundene Runtime-/Qualityrequests. Identische Vorhersagen dürfen vorhandene mathematische Statistik wiederverwenden; fremde Hardwareprovenienz darf dabei nicht erfunden werden.

Bekannte `PARSER_UNSUPPORTED`-/`COMPILE_INFEASIBLE`-Fälle werden bei gleichem Vertrag nicht jede Nacht neu gebaut. Fehlender GPU-Kontext ist Infrastruktur und erzeugt keine dauerhafte negative Modellevidenz. `ABORTED_UNKNOWN` bleibt unvollständige Evidenz. Geänderte Splitauswahl muss alte/aktuelle Boundaries und erwartete Cold Builds erklären; ein neuer tatsächlich benötigter Split ist kein pauschaler Cacheverlust.

Der frühere globale Hashcache-Nachlauf ist als behobener und fortgeltend regressionspflichtiger Produktpfad dokumentiert. Keine zusätzliche Hash-/Seal-/Signatur-/Registryebene, kein neues Vollverzeichnis-Hashen und keine Metadatenarbeit in Native-Performancefenstern. Fehler beim Schreiben von Ergebnis oder Debug-ZIP dürfen kein finales Teilarchiv mit altem PASS publizieren. Primärfehler und Cleanupfehler bleiben getrennt.

Workflowlocks schützen aktive Prozesse und bleiben erhalten. Regulärer Cancel räumt eigene Worker/Supervisoren geordnet auf. Keine alten Chat-PIDs killen, keine Lockdateien als Cachefix löschen. Ein abgeschlossener Build ist noch kein Nachweis von Runtime, Qualität oder Energie.

### 8.1 Belegte Wiederverwendung und ehrlich begründete Neubauten

| Beobachtung | Belegter Scope |
|---|---|
| v2.80-Reusestarter zweimal je zwei frische Prozesse | Vier lokale exakte MobileNet-H10-CPU-HEF-HITs trotz GPUpräferenz; kein SDK-/Compilerdispatch, kein OS-Reboot-/Ganzworkflowclaim |
| BiggerSet v2.80 vom 10.09. 09:42 | 22 Hailo-HITs; 48 unterschiedliche TRT-Enginepfade wiederverwendet; sechs sinnvolle neue Mean/Std-DXNNs für Klassifikations-Full/Part1 |
| CompletSetDev v2.80.1 vom 10.09. 13:30 | 26 Hailo-HITs, 56 unterschiedliche TRT-Pfade; 13 DXNNs wiederverwendet, YOLOv7-Paper b044 neu nach `model_missing` |
| Zwei-Split-Nacht ab 10.09. 21:08 | 38 Hailo-HITs, ein H10-YOLO11-b064-Neubau, ein H8-Kontextfehler; 86 unterschiedliche TRT-HIT-Pfade, fünf TRT-Neubauten; sieben neue DeepX-P1-Boundaries |
| Drei-Split-Nacht ab 11.09. 21:35 | 49 Hailo-HITs ohne Compiler; 21 DXNNs wiederverwendet, sieben zusätzliche P1-Builds; 114 unterschiedliche TRT-HIT-Pfade und zwölf protokollierte Neubauten |

Zahlen gelten für ihren jeweiligen Log-/Snapshotumfang, nicht als zeitloses Cacheinventar. Wiederholte HIT-Logzeilen desselben Enginepfads wurden nicht zu neuen Artefakten addiert. Ein `MISS`, ein gestarteter Build und eine erfolgreich gespeicherte Generation sind verschiedene Zustände. Historische Receiptberichte können keinen heutigen Dateibestand garantieren. [E-REUSE-TARGET] [E-WORKFLOW-HISTORY] [E-NIGHT-2803]

In der letzten Nacht blieb H8/YOLO11 b064 wegen des damals noch nicht in den normalen Kontext eingebundenen Overlays blockiert. Hinzu kamen exakte negative späte YOLO26-Boundaries. Ein später bestandener privater H8-Smoke erzeugt weder dieses fehlende P1-HEF noch automatisch seine normale Profilbindung. Vor erneutem Kaltbuild den aktuellen tatsächlichen Bestand prüfen.

### 8.2 Modellcache ist nicht Qualitycache

Änderung nur des Buildgeräts oder Overlaypfads: kein neuer Modellvertrag. Wechsel von Validierung500/Bootstrap500 zu 5.000/5.000: vorhandenes HEF weiter nutzbar, aber nicht derselbe statistische Qualityauftrag. Wechsel DeepX `current_scale_only` → `imagenet_mean_std`: echter Build-/Numerikvertrag, alte DXNNs kein zulässiger HIT. Ein Quality-FAIL bleibt ein technisch verwendbares Artefakt mit eingeschränkter Qualitäts-/Claim-Eignung.

Im H8-CPU/GPU-Vergleich sind Cachepayload/Recipe gleich, die HEFs aber verschieden. Jede Runtime-/Qualityaussage bleibt an das tatsächlich ausgeführte HEF bzw. seine gebundenen Vorhersagen gekoppelt. Privates GPU-HEF nicht nach sichtbarer Fixed16-Accuracy automatisch bevorzugen oder über das bestehende Produktiv-HEF schreiben.

### 8.3 Finalisierung und Restzeit

Die alte JSON-Cache-Neuschreibschleife war anhand hoher Schreiblast und ständig wachsendem Cache belegt und wurde gezielt korrigiert. Spätere längere Finalisierungen bei 229.149 indizierten Pfaden sind nicht ohne gleiche Symptome erneut derselbe Bug. Nur quell-/prozessgestützte Diagnose, keine pauschale Cachelöschung.

In der .3-Nacht waren die langsamen Qualityabschlüsse ungefähr 22–23 Minuten pro Detectionvergleich; diese beobachtete Rate enthielt die vier Worker bereits. Sie wurde nicht als verlässliche Gesamt-ETA bestätigt: schnelle spätere Abbruchterminals dürfen die Rechnung nicht rückwirkend als normale Rechenabschlüsse verbessern. Unterschiedliche Taskarten, Cache-/Identitätskurzpfade und frühe Point-FAILs getrennt modellieren. [E-NIGHT-2803] [E-NIGHT-QUALITY]

### 8.4 R7/R8: Speicherprobe, Managementabschluss und Ausgabe

Run `completsetdev_20260915_085558`: H8/H10 meldeten `read-only statvfs probe could not run`, `rc=124` vor ungespeichertem Suiteupload. Frühere Prüfungen desselben Ablaufs hatten ungefähr 241/164 GiB frei bei rund 4,8 GiB Bedarf gemeldet. Das belegt eine fehlgeschlagene Probe, **nicht** „Festplatte voll“. Danach war Remotequieszenz bestätigt, lokaler Management-Shutdown nicht; deshalb Quarantäne. Historische Timeoutursache weiter ungeklärt. [E-GUI-085558]

R7 berücksichtigt beim lokalen Managementabbruch sowohl Benutzer-Cancel als auch terminalen `_stop_requested`-Fehler, verhindert neue Arbeiten und beendet eigene Worker vor dem Thread-Warten. Kontrollierte lokale Prozesse/negative Restthreadfälle sichern die Quarantäne weiterhin ab. Primärfehler und Cleanupfehler gemeinsam anzeigen. Ein isolierter Kandidaten-PASS wurde erst nach Hostprozessprüfung ins Hauptrepo übernommen; Sandboxsicht allein kann keine geschlossene Host-GUI belegen. [E-CX-R7]

R7 erhöhte unbeabsichtigt die Logflut durch vollständige SSH-Kommandos und doppelte JSON-Argumente. Im folgenden Run 30,7 MB / 218.838 Zeilen; 144 SSH-Diagnoseobjekte ungefähr 5,7 MB. R8 trennt kurze Fortschritts-/Fehlermeldungen von vollständigen redigierten Diagnosen und zeigt Modell/Setup/Backend/Rep/Frames. Ausgabeprojektion darf Parserdaten, Returncodes, Timeouts oder Cleanup nicht verändern. [E-R7-RUN] [E-CX-R8]

<a id="complete-set"></a>
## 9. Historisches Complete Set v2.79.29: Ergebnis- und Fehleranker

Historischer Run vom 7. September. Die folgenden damaligen Fehlerlokalisierungen bleiben für Regression und Provenienz erhalten. Wörter wie „offen“ in dieser historischen Darstellung beschreiben den v29/v30-Stand; aktuelle Aufgaben stehen ausschließlich in Abschnitt 12. Insbesondere die hier genannte normale GPU-/Profilintegration wurde danach weiterbearbeitet und ist kein Auftrag zur Rückkehr auf v31.

### 9.1 Referenzlauf und Zählebenen

Run: **`complete_set_20260907_161614`**, tatsächlich **v2.79.29**. Es sind nicht 13 unabhängige Native-Geräteausfälle. [E-V30, §4]

| Ebene | Tatsächlich dokumentiert |
|---|---:|
| Native-Ergebnisobjekte | 63 |
| Technisch erfolgreich | 55 |
| Nicht erfolgreich | 8 |
| Alte Erwartungszuordnung | 55 erfolgreich + 3 fehlgeschlagen + 5 fehlend |
| Alter Kompaktbericht | 68 Zeilen, weil fünf vorhandene Fehlerobjekte zusätzlich als fehlend erscheinen |
| Energie | 55 erfolgreiche Zeilen × 3 gültige kurze Replikate = 165 |
| Zentrale Qualitätsaufträge | 70, davon 69 abgeschlossen |
| Quality-Entscheidungen | 40 `pass`, 22 `fail`, 7 `inconclusive`, 1 `not_evaluated` |
| Setup-lokale `native_full_tensorrt`-Qualityaufträge | Alle 21 `pass` |

Nach read-only Ergänzung **eindeutiger fehlender Planidentität**, ohne Änderung von Messwerten oder Status, ergibt der Gegenversuch 63 vorhanden, 55 erfolgreich, acht erfolglos, null zusätzliche Missing-Zeilen. `matrix_complete` bleibt falsch. Diese Zahlen sind die v31-Replay-Erwartung, nicht das vorweggenommene Ergebnis eines neuen Hardwarelaufs. [E-V30-N] [E-PLAN31, AP1]

### 9.2 Verteilung der acht erfolglosen Native-Fälle

| Anzahl | Fallgruppe | Status gegenüber v30/v31 |
|---:|---|---|
| 1 | DeepX Full YOLO11l | Bekannte Semantik-/Quality-Integrationslücke; v30 adressiert sie. |
| 3 | DeepX-Splits YOLO11l `b062`, YOLO26m `b398`, YOLO26s `b364` | Falscher Compilerkontext verhindert benötigte Part1-Builds; v31 AP5/AP2. |
| 2 | Hailo-10H-Splits YOLO26m/YOLO26s | Frühere ungültige Ausgaben und fehlende Quality-Bindung; v31 AP6/AP2. |
| 2 | Hailo-8-Splits YOLO26m `b398`, YOLO26s `b364` | Exakt bekannte Unrealisierbarkeit; als erklärter Planfall behandeln, nicht blind neu bauen. |

Die zusätzlichen Hailo-8-Manifest-/Energieprobleme betreffen dagegen zwei **laufzeitseitig erfolgreiche** Detectionfälle. Sie sind nicht bereits durch die Beseitigung der obigen acht Fehler erledigt. [E-V30, §§5–7]

### 9.3 CS1 – DeepX-Compilerumgebung

Der fehlgeschlagene normale Build verwendet PyTorch `2.12.0+cu130` mit Architekturen ab `sm_75`, während die GTX 1080 Ti `sm_61` benötigt. Der dokumentierte Primärfehler ist `deepx_compiler_cuda_architecture_unsupported`, nicht bloß eine später fehlende DXNN-Datei. R2 bestätigt die funktionsfähige compilerlokale **cu126-Overlaystrategie** mit echten Builds, setzt sie aber explizit. Ihre automatische Wahl im normalen GUI-/Workflowstart bleibt offen. [E-V30, CS1] [E-R2]

AP5 muss den geeigneten Childkontext eindeutig auswählen und protokollieren, ohne globales GUI-`PYTHONPATH`, Runtime-Venvs oder andere Vendorprozesse zu verändern. Ein vollständiger gültiger Cache-Hit darf keine unnötige Compilerprüfung/-installation erzwingen. [E-PLAN31, AP5]

### 9.4 CS2/CS3 – Hailo-8-Manifest und Three-Stage-Energie

Betroffen: **YOLO11l `b062` und YOLOv7 `b044`**. Die benötigten Manifeste existieren unter `endpoints/completed_task/native_fifo_outputs/native_fifo_output_manifest.json`; ihre Bytes stimmen laut unabhängigem Replay mit Command und Consumer überein. Der Leser sucht aber den alten absoluten Remote-Pfad beziehungsweise nur flache Fallbacks. Es ist zunächst ein **Auflösungsfehler**, kein nachgewiesener beschädigter Hash. [E-V30, CS2]

AP3 löst nur zur Job-/Setup-/Case-/Precision-/Endpointrolle passende Collectionpfade auf und prüft danach Manifest und Payloads. Keine beliebige rekursive Suche, keine Auswahl nach jüngstem Datum, keine Vertragsumsiegelung. Bei reduzierten Fixtures ohne Payload nur den tatsächlich erreichbaren Manifestnachweis melden. [E-PLAN31, AP3]

Unabhängig davon kennt der Energieprüfer den Modus `native_three_stage_fast_oracle_outside_timing` noch nicht. AP4 muss den **bestehenden vollständigen Fast-/Oracle-Verifier** integrieren. Eine zusätzliche erlaubte Zeichenkette genügt nicht. Falscher Count, unpassender Messendpunkt, falsche Eingabe oder fehlende Oraclebindung bleiben blockiert. Die vorhandene Angabe `three_stage_concurrency_directly_measured=false` bleibt erhalten: Eine direkt gemessene Three-Stage-Überlappung ist für diese historischen Fälle damit nicht belegt. Eine Berichtsreparatur darf das Feld nicht auf `true` setzen. [E-V30, CS3] [E-PLAN31, AP4]

### 9.5 CS4 – Hailo-10H/YOLO26: kein kleiner Rundungsrest

| Ursprünglicher Befund | YOLO26m | YOLO26s |
|---|---:|---:|
| Maximaler absoluter Schnittstellenfehler | 622,1212 | 635,1461 |
| Mittlerer absoluter Fehler | 54,8500 | 51,7847 |
| Gültige Wahrscheinlichkeits-Scores im BN6-Output | 0 % | 0 % |
| Geordnete xyxy-Boxen | 73 % | 75 % |

Der Vorlauf hatte jeweils eine explizite TensorRT-Part2-Engine als Cache-Hit. Wegen `score_column_not_probability_like;coordinates_not_ordered_xyxy` wurde der Qualityexport aber korrekt geschlossen abgelehnt. Anschließend fehlt die entsprechende Binding; ein konventioneller Native-Lookup meldet dann `missing_native_trt_part2_engine`. Die spätere Meldung beweist **keine Löschung der vorher vorhandenen Engine**. [E-V30, CS4]

Offen bleibt die konkrete Layout-/Quantisierungs-/Bridge-Ursache. AP6 soll vorhandene Artefakte an HEF-Ausgang und vor/nach der Part2-Bridge erfassen, mit Namen, Shape, Datentyp, Scale/Zero-point sowie getrennten Box-/Scorekanälen. Keine blinde Clip-/Sigmoid-Korrektur, keine zweite Parallelitätsebene und kein vorsorglicher Engine-Neubau. Eine implementierte Diagnose ist noch keine Reparatur ihres Untersuchungsgegenstands. [E-PLAN31, AP6]

### 9.6 CS5/CS6 – Identität, Ausschlüsse und bekannte Unrealisierbarkeit

Drei DeepX-Splitfehler verlieren `setup_id` und `comparison_backend`, zwei Hailo10-Fehler `comparison_backend`. Dadurch entstehen die fünf Doppelplatzhalter und ungültige Energie-Ausschlüsse. AP1 hält die geplante Identität **vor** der Ausführung fest und bewahrt sie auch bei frühen Fehlern. Widersprüchliche oder mehrdeutige Zuordnungen werden nicht geraten. [E-V30, CS5]

Für Hailo-8/YOLO26 `b398`/`b364` ist `KNOWN_INFEASIBLE / COMPILE_INFEASIBLE / exact_deterministic_outcome` vorhanden. AP2 reicht dieses Ergebnis als nicht ausführbaren, aber vorhandenen Planfall weiter. Kein neues identisches Compileexperiment und keine künstliche Missing-Kaskade. Andere Splitpunkte wären eine bewusst anders geplante Kampagne, keine stille Reparatur dieses Audits. [E-V30, CS6] [E-PLAN31]

### 9.7 Weitere Qualitätsbefunde bleiben eigenständig

MobileNet-Hailo-Splitverluste sind ebenfalls groß: CPU 73,6 %, Hailo-8 59,6 %, Hailo-10H 59,2 % im alten B500-Lauf. **Die DeepX-R1/R2-Erkenntnis behebt diese Hailo-Pfade nicht automatisch.** Deren tatsächliche Eingabe-/Kalibrierungs-/Schnittstellenverträge bleiben bei anhaltendem Verlust gesondert zu prüfen. [E-V30, §6]

Bei Detection bleibt DeepX YOLO26m Full `inconclusive`; YOLO26s Full insgesamt `fail`. Ein ungefähr 0,61-pp-Verlust in AP 50:95 versteckt nicht die etwa 1,50 pp Verlust in AP75. Hauptmetrik und Guardrails zusammen lesen. Ebenso bleibt ein technisch funktionierender DeepX-D-Split mit unzureichend abgesicherter AP50/AP75-Nichtunterlegenheit `inconclusive`. Keine Statusänderung durch einen reinen Softwarefix. [E-V30] [E-D29]

### 9.8 CS7/CS8 – Intervalle und Kandidatenzahl

Bei frühem Verlust-Fail wurden `bootstrap_repetitions=0` und dennoch `ci_low=ci_high=delta` ausgegeben. **Das ist kein berechnetes Konfidenzintervall.** AP8 kennzeichnet die ausgelassene Unsicherheitsschätzung und hält die bestehende Punkt-/Gateentscheidung davon getrennt. Der anders begründete Fall `candidate_reference_identical` wird nicht pauschal damit gleichgesetzt. [E-V30, CS7] [E-PLAN31, AP8]

Das Complete-Set-Profil enthält `max_accepted_cases_per_model: 1`; die sieben ausgewählten Grenzen sind `b119`, `b135`, `b132`, `b062`, `b398`, `b364`, `b044`. Der Plan meldet zu wenige vergleichbare Kandidaten für Rankingtransfer. `insufficient_candidates` wird nicht zu `pass`, weil alle sieben Modellnamen vorkommen. Die erfolgreiche historische YOLOv7-`b066`-Abnahme deckt nicht automatisch `b044` ab. [E-V30, §8]

<a id="v31-plan"></a>
## 10. Historischer v2.80.4-Auftrag und fortgeltende Grenzen

**Historischer Auftrag aus REV3, nicht erneut starten.** Aktueller Produktstand R8 nach §§4.3–4.4; aktuelle Arbeit in §12. Die folgenden Tabellen erhalten die damalige Anforderung und ihre methodischen Grenzen.

| AP | Aktuelle Umsetzung / Abnahmevertrag |
|---|---|
| AP0 | Vollständige .3-FIX5-Basis erhalten; aktuelle Nachtmodulidentitäten und verfügbare Originalquellen separat dokumentieren |
| AP1 | Zentraldeskriptoren 512 MiB gesamt / 64 MiB pro Datei; freigegebene strukturierte Ergebnisse/Indizes 256 MiB pro Datei; keine spätere alte 2-/8-/32-MiB-Rückstufung |
| AP2 | Ausgewertet, abgebrochen und technisch fehlgeschlagen getrennt; fertige Resultate und beobachtete Qualitäts-FAILs erhalten |
| AP3 | Vorhandenes Hailo8-Manifest explizit im Run-Mode-Editor wählen; gleicher Resolver bis zur realen Compiler-Kindumgebung |
| AP4 | Rezept-Reuse von konkreter Artefakt-/Qualityidentität unterscheiden; bestehende Cacheverträge absichern |
| AP5 | Abgeschlossene H8-/H10-Smokes, HAR-R1 samt verbleibender Restabweichung, negative B5000-Resultate und Energieclaims korrekt beschriften; keine Wiederholung und keine aktive Erweiterung um die zurückgestellte optimierte Float-/Integer-I/O-Diagnose |
| AP6 | Eindeutige .4-Identität; finales Archiv prüfen, echtes isoliertes Upgrade und durchgehenden normalen Zielworkflow vorbereiten |

Die Scopepräzisierung in REV3 beauftragt **keinen zusätzlichen Produktcode**. Der .4-Kern bleibt Hailo8-Produktivkontext, Cancelzählung und Debuglimits einschließlich ihrer vorhandenen Erhaltungs-/Abnahmeregeln. Die vertiefte numerische Ursachenklärung ist weder in AP5 nachzurüsten noch als Voraussetzung zu behandeln. [E-SCOPE-REV3]

Die 56 IDs im Plan sind Prüfanforderungen, keine vorab bestandene Testzahl. Der tatsächliche Umfang einschließlich nicht verfügbarer Originalquellen steht in der Lieferung. Modelle, Bilder, Roharrays und CUDA-Wheels bleiben aus Debug-/Gitbelegen ausgeschlossen. Größere erlaubte JSON-Klassen ändern weder Pfadkonfinement noch Symlink-/Hash-/Atomaritätsregeln. Größenfehler sind `size_limit_exceeded` mit Ist- und Grenzgröße, nicht `json_invalid`.

### 10.1 Hailo8 im normalen Editor

Neben „Hailo8 compute for new builds“ stehen Manifestpfad, Dateiauswahl und lesende Prüfung. Ein fehlendes optionales Feld lässt die bisherige explizite Environment-Auswahl zu. „Explizit auswählen“ mit leerem Pfad bedeutet bewusst kein Overlay. Jobwert → Familienwert → bisherige explizite H8-Environment-Variable → kein Overlay. Ein Default enthält keinen maschinenspezifischen Pfad.

CPU verwendet den gespeicherten Pfad nicht und startet keine Overlay-/GPUprüfung. Lesende GUI-Prüfung ist keine GPU-/XLA-Messung. Sie prüft vorhandene Familie, ausgewählte Venv, Metadaten und Komponenten mit dem bestehenden Validator. Kein Paketdownload und keine Mutation von `os.environ` des GUI-Hauptprozesses. Hailo10, DeepX, Runtime und CPU-Referenz dürfen keine H8-Librarypfade erben. Benutzerprofile und Registrys werden beim Upgrade nicht still auf einen lokalen Overlaypfad umgeschrieben.

### 10.2 Abbruchzählung und ETA

Der dokumentierte Q5-Sollreplay enthält 123 terminale Requests: 63 fertig ausgewertet mit 43 PASS, 18 FAIL, 2 INCONCLUSIVE sowie 60 Abbruchfolgen (vier `CancelledError`, 56 `QualityServiceClosedError`). `completed_count` zählt weiterhin ausgewertete Ergebnisse. Terminal ist nicht gleich erfolgreich berechnet und Requestzahl ist nicht Hardwaremesszahl.

Eine Service-Closed-Ausnahme ist nur mit passendem vorangehendem Run-Cancel als Abbruchfolge einzuordnen; ohne diesen Kontext bleibt sie technischer Fehler. Früher entstandene technische Fehler werden durch späteren Cancel nicht gelöscht. Fertige Cache-/Berechnungsergebnisse bleiben beim Cancelrennen einmalig erhalten; unvollständige Shards veröffentlichen kein CI/PASS oder erfolgreichen Cacheeintrag. Der alte abgebrochene Run bleibt cancelled und unvollständig, seine 18 beobachteten Qualitäts-FAILs bleiben fail.

Abbruchterminals, Cachetreffer und frühe Punktentscheidungen gehören nicht in die mittlere Laufzeit eines vollständigen Detectionbootstraps. Hailo-GPU beschleunigt nicht automatisch zentrale CPU-Statistik. Workerzahl, Methode, Wiederholungen und Margen werden für eine angenehmere ETA nicht geändert. [E-2804-PLAN]

### 10.3 Was die langen Qualityaufträge tatsächlich tun

Die Referenz-/Kandidateninferenz erzeugt zunächst Vorhersagen. Der zentrale Service bindet dieselben Bild-IDs/Labels, berechnet Taskmetriken und gegebenenfalls gepaarten Bootstrap aus diesen bereits vorhandenen Vorhersagen. Bei 5.000 Bildern und 5.000 Resamples laufen nicht 25 Millionen erneute Modellinferenzen. Klassifikation verwendet Trefferzählungen; Detection benötigt wiederholte gewichtete Precision-/Recall-/AP-Auswertung auf vorbereiteten Matches. Die vier Worker bearbeiten dabei häufig Teilstücke eines Vergleichs, nicht vier unabhängige vollständige Vergleiche.

Der bestehende zentrale AP-Evaluator und ein separat angeforderter Official-COCOeval-Bericht sind verschiedene Belege. Early-Fail, identische Vorhersagen und ein exakter Qualitycache-HIT können den vollständigen Bootstrap vermeiden, ohne Metriken zu erfinden. GPU für Hailo-Neubauten beschleunigt diese Management-CPU-Statistik nicht. Algorithmische Beschleunigungen wären nur nach nachgewiesener Metrik-/Seed-/Entscheidungsparität zulässig, nicht durch spontanes Reduzieren des Statistikumfangs. [E-QUALITY-EXPLAIN]

Der tatsächliche alte Exportblocker betraf **123 gültige Requestdateien mit 35.157.419 Byte**, die ein 32-MiB-Summenbudget um 1.602.987 Byte überschritten. Kein VRAM-/Modell-/Datenträgerfehler. Die .4-Limits 512/64/256 MiB sind der beauftragte durchgängige Fix; diese Dokumentrevision bestätigt nicht selbst dessen neue Quellimplementierung.

<a id="gates"></a>
## 11. Historische .4-Abnahme und Übergang zum heutigen GUI-Teststandard

**Der folgende .4-Ablauf ist historische Planung.** Heute gilt §19: kleine Tests über normale GUI und reale Startbindung; kein erneuter .4-Installer, kein Finalprofil als Smoke und keine automatischen Hardwaretests allein durch Lesen der KB.

Nach der Softwarelieferung folgt eine zusammenhängende, begrenzte Abnahme mit einem Startablauf und gesammelt exportierten Ergebnissen. Bereits bestandene isolierte MobileNet-Compute-/Build-/Fixed16-Schritte werden nicht erneut vorgeschaltet. **Der normale Ablauf muss Zustände und vorhandene Ergebnisse korrekt binden und abschließen, nicht sämtliche Quality-FAILs in PASS verwandeln.** Die bestehenden technischen Quality-FIRST-/Endpointgates bleiben unverändert; eine blockierte Zeile bekommt ihren tatsächlichen Grund statt einer umgangenen Prüfung. Die zurückgestellte Ursachenanalyse ist kein zusätzliches Gate. [E-SCOPE-REV3]

| Gate | Ziel und korrekter Ausgang |
|---|---|
| G0 | .4 installieren und fokussierte/fortgeltende Softwaretests; Profile, Venv, Overlay, Registrys und Caches erhalten |
| G1 | Alten gecancelten Nachtlauf mit normalem .4-Exporter: 123 gültige Originalrequests / 35.157.419 Byte und 14 Referenzdiagnosen; keine zweite Nachsammlerpflicht |
| G2 | Kleine echte CPU-Qualityprozessfixture mit Cancel; disjunkte Zähler und beendete eigene Prozesse |
| G3/G4 | Gespeicherte H8-Auswahl in frischen Prozessen; bekannte CPU-HEFs trotz GPU-Präferenz wiederverwenden, null Compilerdispatch |
| G5 | Normaler begrenzter MobileNetV3- plus YOLO11l-Workflow mit je einem vorhandenen Split, Standard B500/Bootstrap500, Referenz → Consumer → Native → Bericht |
| G6 | Nur ein tatsächlich noch benötigter vorab bestätigter H8-MISS, z.B. YOLO11l b064: gespeicherter Kontext bis ins reale Compilerkind, danach Reuse |

G5 verwendet den bestehenden Erwartungs-/Admissionpfad; ein unerwarteter MISS wird sichtbar, statt die kurze Runde heimlich in einen langen Build zu verwandeln. Nicht global `cache_verify_only` setzen, weil dann der normale Referenzpfad fehlt. Wenn G6 bereits warm ist, bleibt „aktueller normaler Kaltbuild nicht beobachtet“ ein benannter Scope; es wird kein vorhandenes HEF gelöscht oder per Force neu gebaut. Weitere wissenschaftliche Final-/Energieaufträge sind keine versteckten Voraussetzungen für Software-PASS. [E-2804-PLAN, §9]

<a id="todo"></a>
## 12. Einzige aktuelle Aufgabenliste – Abschluss vom 04.10.2026

Die autorisierten Erhebungen und lokalen Auswertungskorrekturen sind abgeschlossen.
Es gibt keine offene planmäßige Messpflicht. Maßgeblich sind die Tabellen des gemeinsamen
Abschlusses und §23, nicht die früheren Restzahlen.

1. **Archiv:** laufenden Benutzertransfer und nachfolgende sequenzielle Ergänzung bis zum tatsächlichen Copy-/Lesenachweis verfolgen; verbliebene externe Evidenzlücken in der privaten Pfadkarte prüfen. Keine Originale löschen.
2. **Paper:** Rangtransfer je Modell/Setup/Precision/Endpunkt und die explizit deskriptiven Energiequoten aus den reproduzierbaren Tabellen verwenden. Keine kausale Laufzeitkontrolle oder Hold-out-Rolle behaupten.
3. **Vergleichsgrenzen:** die beiden negativen YOLO26s-Vendor-Fulls und fallbezogene Decoder-/Messgrenzen erhalten; keine neue Messung automatisch daraus ableiten.
4. **Veröffentlichung:** [Toolrelease v2.92.0](https://github.com/Keff789/ONNX-Splitpoint-Tool/releases/tag/v2.92.0), Maincommit `d164aad6d7c7ef68c1b371c49a1fdea0a3b27dd7`, annotierter Tag und beide Quellenarchive sind veröffentlicht und remote verifiziert. Der neue Quellenstand ist keine rückwirkende Versionszuordnung aller Messungen.

<details>
<summary>Historische Aufgabenliste des Ergebnis-Audits vom 02.10.2026</summary>

Die planmäßige Generic-/Quality-/Native-/Energieerhebung dieses Runs ist abgeschlossen.
Die früheren Ergänzungszahlen 152 Generic, 66 Quality und zwölf Nativefälle sind **erledigte
Zwischenstände**, keine aktuelle Restplanung. Offene F-Befunde unten sind noch nicht als
implementiert oder lokal behoben bestätigt. Der Dokumentauftrag startet keine Hardwarearbeit.
[E-TH20-AUDIT] [E-TH20-FOLLOWUP]

### 12.1 Abgeschlossen und zu erhalten

| Gegenstand | Belegter Abschluss / Grenze |
|---|---|
| Generic | 527 Messzeilen; 37 negative Buildbefunde und 24 `hailo_yolo26_static_part1_guard`-Policyausschlüsse erklären die übrigen 61 Sollfälle. Part2-only bleibt von Composed getrennt |
| Quality | 548 abgeschlossene Einzelresultate einschließlich 39 `accuracy_loss`. Keine Neuberechnung wegen falscher Backendlabels oder abgeleitetem `not_evaluated` |
| Native | 234 erfolgreiche Fälle / 702 Wiederholungen; 228 Multi-Input-Fälle korrekt nicht unterstützt. Kein Nachrücken oder erneuter Performanceauftrag zur Metadatenreparatur |
| Energie | 234 vollständige Zeilen / 702 gültige Replikate. Die drei ungültigen physischen Vorversuche bleiben historisch erhalten; ihre gültigen Ersatzversuche sind keine offenen Messungen |
| Reentry-/Quellresolverreparaturen | Der installierte Ergänzungspfad hat die fehlende Arbeit produktiv vervollständigt. Frühere 600-s-, Quellenalias-, Attempt-/Campaign- und ungestartete-Previous-Results-Blocker nicht ohne neuen identischen Befund erneut untersuchen |
| Historische negative Numerik | Frühere H10-YOLO26 b398/b364, H8-Rejects und HAR-/Quantisierungsbefunde bleiben eigene Artefakt-/Runbelege. Erfolgreiche andere Grenzen reparieren sie nicht rückwirkend |

### 12.2 Offene lokale Korrekturen und bedingte Zusatznachweise

| ID / Priorität | Konkreter Befund und nächste Aktion | Abnahme / neue Messung? |
|---|---|---|
| **F01 / P1 – Backendlabels** | 47 Qualityvergleichszeilen stammen aus `hailo10_to_tensorrt` auf H10, werden aber als `tensorrt` ausgegeben. Normalisierung und abhängige Gruppen-/Vergleichsberichte korrigieren | 47 Identitäten korrekt; echte TRT-Full-Companions und TRT→TRT unverändert. **Keine Messung/Statistikrechnung** |
| **F02 / P1 – Native-Authority** | 186/192 unterstützte Splits melden `native_split_quality_authority_eval_run_id_mismatch`, obwohl sechs sichtbare Run-IDs übereinstimmen und die aktuelle Authority gültig ist. Tatsächliche historische Authoritywahl/Writer nachvollziehen | Reguläre, nachvollziehbare neue Projektion; falsche Run-/Setup-/Requestbindungen bleiben negativ. **Zunächst keine Messung**, keine manuell positiven Flags |
| **F03 / P1 – lokale Full-Numerik** | YOLO26m/s × 3 Setups, TRT Full: Performance und exakte zentrale Quality vorhanden, lokale Numerik `numerical_similarity_metric_missing`. Vorhandene Outputs lokal prüfen | Sechs lokale Vergleichsbelege oder genaue Evidenzlücke; **nur falls benötigte Outputs auf dem Host fehlen** minimale gesonderte Outputdiagnose planen |
| **F06 / P1 – Terminal-/Qualitybilanz** | 61 legitime Ausschlüsse erscheinen als fehlende Pflichtquality; 29 davon im Lifecycle `materialized_not_terminal` (17 Build/12 Policy). 527 vorhandene Matrixeinträge tragen abgeleitet `not_evaluated` | Originale Ausschlussgründe und 548 Einzelentscheidungen korrekt projizieren. **Keine Nachmessung**, keine Nullscores oder erfundenen PASS-Zeilen |
| **F05 / P1 – Energieexport/Rollen** | 234 echte Beobachtungen vorhanden; 384 Split↔Full-Paare ohne Quoten. `energy_results.csv`/`claim_eligible_energy.csv` enthalten 527 Genericzeilen ohne Energiewerte | Aufnahmegültigkeit, diagnostische Paarbarkeit, Semantik und Claimrolle getrennt exportieren. Originale Screeningrolle erhalten. **Keine Energie-Wiederholung** |
| **F05-D / P1 – acht DeepX-Paare** | Acht Detection-Split↔Vendor-Full-Paare mit abweichenden Decoder-/NMS-Vertragskennungen | Primitive Verträge und Completionsemantik aus Originalen vergleichen; gleiche sichtbare Schwellenwerte beweisen keine Gleichheit. **Zunächst lokal** |
| **F04 / P2 – Generic↔Native-Endpunkt** | 192 Paare mit `generic_completed_task_measured=false`; 499 Generic-Splitprojektionen ohne belegte vollständige Taskzeit. Ursprüngliche Per-Case-Berichte suchen | Falls Zeiten vorhanden: Importfix. Falls wirklich nie gemessen und für Gleichendpunkt-Speedup benötigt: **kleinsten ergänzenden Generic-Completionumfang gesondert planen**. Keine Wiederholung von Native/Energie/Quality |
| **W01 / P2 – Accuracybeobachtung** | MobileNet/DeepX/b043 Top-1 66,60 % gegenüber b039 72,30 %, b056 72,28 %, CPU 73,70 %; gespeicherte Export-/Input-/Quantisierungsbelege prüfen | Noch **kein bewiesener Bug/Neumessauftrag**. Multi-Input-Grenze hat bewusst keinen Native-/Energiezwilling |
| **W02/W03 / P2 – Streuung** | Fünf auffällige Native-FPS-Fälle und drei YOLOv7-Full-Energieeffizienzfälle aus §22 prüfen | Vorhandene Timing-/Warmup-/Clock-/Thermalbelege zuerst. 5 % CV nur Sichtungsfilter, kein neues Gate; kein Best-of/Verwerfen schlechter Wiederholungen |
| **DOC/SOURCE / danach** | Tatsächlich installierten 2.91.2-Folgequellstand und korrigierte Auswertungsbelege getrennt sichern/veröffentlichen | Letzter Toolbericht meldet keinen Commit/Push. Dieses KB-Update veröffentlicht keine Toolquellen und ersetzt kein Hostbackup |

### 12.3 Abschluss- und Stoppregel

Zuerst F01/F02/F03/F06/F05 auf einer abgeleiteten Arbeitskopie über normale Reader,
Validatoren und Reporter prüfen; Primärwerte und historische Fehlversuche nicht überschreiben.
F04/W01–W03 entscheiden danach fallgenau zwischen lokalem Fix, gültigem negativem Ergebnis,
methodischer Grenze und wirklich benötigter Zusatzmessung. Kein allgemeines Refactoring,
keine neuen Hash-/Registrymechanismen, kein Force-Rebuild, keine Schwellenlockerung,
keine rückwirkende Hold-out-/Final-Rollenumdeklaration und keine automatische Startschleife.
Der vorbereitete Anschlussauftrag `AUFTRAG_LOKALE_AUSWERTUNGSKORREKTUREN.md` ist ein Auftrag,
**kein Implementierungs- oder Abnahmenachweis**. [E-TH20-FOLLOWUP]


</details>

<details>
<summary>Historische R9G-/R9H-Aufgaben und damalige Grenzen (19.09.2026)</summary>

### Historischer Aufgabenstand vom 19.09.2026 – keine aktuelle Start-/Restplanung

Stand: 19.09.2026; R9H-Snapshot 07:19:10 +02:00. IDs aus R8 und den Folgeaufträgen bleiben erhalten;
neue Unterpunkte trennen frühere Erfolge von später neu gefundenen Integrationslücken. Dies ist
eine Dokumentlieferung, keine Aktualisierung der laufenden `docs/ARBEITSSTAND.md` auf Smartmirror2.
Ein historischer PASS bleibt auf seinen tatsächlichen Umfang beschränkt. [E-REV5-R9G-AUDIT]

#### Historisch 12.1 Im belegten Umfang abgeschlossen / nicht wieder aufrollen

| ID / Thema | Status und genaue Grenze |
|---|---|
| GUI-01 / CODEX-SETUP | Normale Host-GUI samt Config/Snapshot/Queue/Capture/Consumer/Export/Cleanup in R9G vollständig durchlaufen; Agenten-Sandbox ist kein vollständiger Hostzugriff |
| EN-01…EN-03 / EN-04 | Normaler r6-reviewed Collector und Quellenbudget integriert; R9G 189/189 gültige Erstaufnahmen, kein Retry; frühere lokale Statistiktests erhalten. Taskgleichheit separat in §12.2 |
| MODE-01/02 | Standard 100/10/1 und Final 1000/100/3, Qualitätsbudget getrennt. Drei Splits sind keine drei Wiederholungen |
| LAT-01 | Detection bis erforderlichem Taskabschluss, Klassifikation bis Top-1/Top-5; TRT Full Prepared-Input-Pfad ergänzt; R9G 63 Reihen / 6.300 gepaarte Zeiten geprüft |
| BACKFILL-02 / H8-01 | H8-Nachrücken in realer GUI bis b021; R9G zusätzlich m/b038 ausgeführt; alte negative Kandidaten erhalten |
| H10-02 / automatischer Produktweg | Allgemeine Output-/Quantisierungsprüfung und Metadatenversorgung erlauben R9G-Ersatzwahl s/b021 und m/b038; **alte b364/b398-HEFs nicht numerisch repariert** |
| DeepX-Part1-/Part2-Reuse | Beide vorherigen Ketten bis zur realen Inferenz geprüft; FLOAT-No-op-Bridge über vollständige Bindingprüfung, keine pauschale Gleichhash-Ausnahme |
| BUILDER-R9E | HAR-Erhaltung bei Fehler, echte Phasen und Timeoutklassifikation fokussiert geprüft; 70 lokale/229 Hostfälle, 251 unterschiedliche Fälle, nicht neue Vollsuite |
| LOG-01/02 / CLEANUP-01 | R9G normaler Abschluss; spät drainende Pipes vom echten Hänger getrennt, kein neuer pauschaler Transport-/Collectorneubau |
| RELEASE-01/02 / TEST-FIXTURES | Frühere Installed-/Mirror-/Fixtureabnahmen behalten Scope. Die unveränderte Build-ID ersetzt keinen aktuellen Commit-/Patchbeleg |

#### Historisch 12.2 R9H-Ergebnis abwarten und gezielt schließen

| ID | Offener Nachweis | Abschlussbedingung |
|---|---|---|
| NIGHT-01 / R9H-ACCEPT | Zweiter 7-Modelle-/3-Splitrun noch ohne Endbelege | Letzter Runplan, finale Matrix, Pflichtresultate, tatsächliche 100/10/1-Kommandos, Native/Energie/Cleanup lesen; nominal105/315 nicht voraussetzen |
| EN-TASK-01 | R9G: neun TRT-Full-CLS-Kombinationen, 27 Energieaufnahmen noch trtexec | R9H-Energie nutzt wirklich denselben Prepared-Input-/Top-k-Task und zählt tatsächliche Abschlüsse |
| EN-PAIR-01 | R9G: sieben DeepX Full-/Split-Paare mit verschiedenen Eingabebildern | Neue gemeinsame deterministische Vergleichseingabe vor Dispatch; tatsächliche Inputs/Prepared-Feed vergleichen, alte Quellen nicht überschreiben |
| EN-ENDPOINT-01 | R9G: zwölf Detection-Split-Beobachtungen ohne vollständige Vergleichsendpunkte | Gebundene reale Completionnachweise korrekt projiziert, fehlende Identität weiterhin ehrlich unbekannt |
| EN-AGG-01 | R9G:20/21 TRT-Full-Normalisierungen abgelehnt | Aggregationsdefinition und Replikatbasis source-/datengebunden prüfen; Mittelwert(E/N) ≠ Mittelwert(E)/Mittelwert(N); keine Toleranzlockerung |
| REPORT-01/02 | Alte authority_missing trotz gültiger Authority; claim_ok; Generic-Energie als fehlend | Finale R9H-Projektionen trennen Runtime/Output/Quality/angefragte Energie und aktuelle/historische Diagnosen |
| CACHE-01 / CACHE-R9H | Neue TRT-MISSs mit source_onnx_mismatch/not_found/evicted_by_retention | Nach Run lokale/remote Identitäten und tatsächliche Neubauten vergleichen; weder alles als Cachedefekt noch als erwünschte Retention vorwegnehmen |
| EN-PLAUS-01 / PERF-02 | R9G-Werte arithmetisch geprüft; neue R9H-Werte noch nicht | Neue Einzelreplikate/Zeiten/Work Units, Endpunkte und Berichtskette prüfen, keine Neuaufnahme nur wegen Variabilität |
| GIT-RELEASE-01 | Veröffentlichtes Source-Repo nur Baselinebranches | Nach vollständigem Supervisorende exakten aktuellen Source-/Test-/Manifeststand sichern; keine alten R8-Tags auf spätere Dirty-Trees |
| KB-DEPLOY-01 | REV5 und Evidence-Patch vorbereitet | Prüfen und separat übernehmen; während R9H keine Source-/Manifeständerungen und kein Releaseetikett |

#### Historisch 12.3 Bekannte Grenzen / zurückgestellte Auswertung

| ID / Thema | Status und Handlung |
|---|---|
| DX-01 – DeepX Full YOLO26s | Zwei native XYXY-Fehler auf000000052891.jpg/000000395801.jpg weiterhin offen; nicht in R9G 500er-Menge. Nur begründete neue Diagnose, kein Blindtausch/Filter/Bildskip |
| H10-02 – ursprüngliche späte HEFs / höherpräziser Kandidat | Späte UINT8-Outputs ungeeignet; eigener 16-bit-Kandidat s/b364 endet R9E mit Allocatorfehler. Kein identischer Buildretry; m nicht mit diesem Rezept gemessen |
| QUALITY-01 | Gewöhnliche AP-/Accuracyverluste und einzelne Ähnlichkeitswarnungen dokumentieren, nicht bis PASS tunen. Technisch ungültige Ausgaben bleiben getrennt |
| PERF-01 – Paperanker | YOLOv7/H8-b066 mit gleichem Graph-/Completion-/Power-/Queuevertrag vergleichen; b044 und b021/b038 anderer Modelle sind kein Ersatz |
| RANKING-01 / SCI-01 | Drei Splits allein ergeben keine allgemeine Rankingaussage oder ausreichend vergleichbare Gruppen. Separate Forschungsfrage; keine pauschale Softwaregate |
| Energie-Screening / Langzeit | 1 s Lastsoll mit 2,21–4,38s Commandfenstern in R9G ist kein stationärer Dauerbetrieb. Mittelwerte/Streuung nutzbar, wissenschaftliche Gates bleiben |
| TRANSPORT-01 / EN-05 | Historische rc124-/R5-Endpaketursache nicht vollständig geklärt. Erfolgreiche neue Läufe beweisen keine alte Ursache; nur bei neuem Befund wieder öffnen |
| H8-HAR-/Opt-Tuning | Zurückgestellt nach bestehender Forschungsprämisse; keine neue Modell-/Layernamensausnahme oder Hasharchitektur |

**Reihenfolge:** R9H ungestört beenden → finale Einzelbelege aus beiden getrennten Versuchen lesen →
konkrete obige Nachweise schließen oder begründet offen halten → Source-/Evidencecheckpoint →
Performance/Paper/Qualitätsauswertung. Keine weitere allgemeine Reparaturschleife allein aus dieser KB.


</details>

<a id="betrieb"></a>
## 13. Betriebsregeln

**Fortgeltende Schutzregeln; die ausdrücklich genannten .4-Grenzen sind historisch:** GUI und laufende Workflows vor dem Update geordnet beenden. Der Installer erhält Tool-/Vendor-Venvs, Benutzerprofile, Run-Mode-/Hardware-Registry, vorhandene Overlays, Modell-/Qualitycache und Originalruns. Das Manifestfeld wird erst durch eine explizite Nutzeraktion ausgewählt. Kein Treiber-, System-CUDA-, DFC-, TensorFlow-, Torch- oder DeepX-Upgrade in v2.80.4.

`relaxed` bleibt auch für Final der vereinbarte Repro-/Cachemodus. Hailo balanced/Opt1/B500/Batch8, DeepX EMA/Opt0/B500, ImageNet-Mean/Std, Qualitätsmargen, Seed, AP-/Top-k-Definitionen und Bootstrapmethode bleiben gleich. Der vorgeschaltete Standarddurchlauf und der separate Finalumfang dürfen beim Resume nicht als identischer Run mit verändertem Profil vermischt werden.

Generische Energie bleibt aus. Native-Energie ist ein eigener Scope; Dauer und Replikate werden nicht still geändert. Vorhandene alte Fehlermeldungen oder PIDs sind keine aktuellen Betriebszustände. Primärfehler, erwartete Nichtrealisierbarkeit, technische Ausführung, Qualitätsentscheid und Cleanup werden separat gelesen.

### 13.0 Aktueller Betrieb nach gemeinsamem Abschluss (04.10.2026)

Keine Kampagne oder Messfortsetzung starten. Die Auswertung wurde außerhalb der
Primärbereiche ausgeführt, der Quellrelease regulär installiert und veröffentlicht.
Originale, historische Attempts, Profile und Caches bleiben erhalten. Archivkopien
laufen unabhängig und sequenziell nach dem Benutzertransfer; keine Quelländerung an
kopierten Messdaten und keine Löschung nach bloßer Größenprüfung. Weitere Paperarbeit
verwendet die abgeschlossenen Tabellen und die Grenzen aus §23.

<details>
<summary>Historische Betriebsanweisung vom 02.10.2026</summary>

### 13.0 Aktueller Betrieb nach THESIS20-Abschluss

Keine erneute Kampagnenfortsetzung allein für F01–F06. Lokale Reader-/Reporter-/Validator-
Nacharbeit erfolgt getrennt von Primärmessungen. Originalrun, Caches und Quellenbelege erhalten;
keine manuelle Gatefreigabe, keine neue Hasharchitektur und keine automatische Messschleife.
Ein eventueller kleiner Zusatzmessplan wird erst nach §12/F04 beziehungsweise nach konkreter
Evidenzlücke gesondert entschieden. Dieses Dokumentupdate ändert keine Hostdateien. [E-TH20-FOLLOWUP]


</details>

### 13.0a Historischer Betrieb während R9H (19.09.2026)

R9H arbeitet mit dem normalen Sourcebaum und den vorhandenen Vendorumgebungen. Solange Workflow
oder Supervisor noch aktiv sind, keine Source-/Profil-/Venv-/Collector-/Registry-/Manifeständerungen,
keine Cachelöschung und keine zusätzliche Hardwarerunde. Die jetzige KB-/Evidencevorbereitung findet
außerhalb des Hosts statt. Git-Dokumentation ist kein Anlass, den laufenden Arbeitsbaum anzufassen.

Nach Abschluss zuerst den letzten R9H-Run und die Versuchshistorie prüfen. Bei einem späteren Sourcecommit
nicht nur die unveränderte Build-ID nennen, sondern den tatsächlichen Commit/Arbeitsbaum/Patch und
finalen Installed-/Testumfang. Rohmodelle, private Profile und große Runs bleiben außerhalb des Public-Git.

### 13.1 Was auf Smartmirror2 bleiben muss

Ergebnis-Git ist kein Modellbackup. Für bereits vereinbarte Ausführung und mögliche Ursachenprüfung die ursprünglichen Nacht-, privaten Build-, Runtime- und HAR-Diagnoseordner sowie den **gesamten** H8-Overlaybaum erhalten. Besonders das lokale `runtime_arrays.npz` lag absichtlich nicht im kleinen Ergebnis-ZIP. Nur ein Manifest ohne referenzierte Bibliotheken oder ein Receipt ohne benötigtes Modell reicht nicht zur erneuten Ausführung.

Keine gleichzeitige Installation von .4, Venvänderung, GPUkompilierung und neue Ursachenprüfung. Neue Diagnose-Supervisoren nutzen die bestehenden Workflow-/Plattformlocks; keine alten PIDs oder Lockdateien aus Chatbeispielen löschen. Erfolgreiche private HAR-/HEF-Tests werden nicht durch Wechsel des Releaseetiketts ungeschehen.

<a id="ablage"></a>
## 14. Evidenzablage und dauerhafte Referenzen

Git erhält Code, Dokumentation, kleine Profile, Logs und ausgewählte strukturierte Ergebnisse. Modelle, Bildcorpora, HEFs/DXNNs/Engines, CUDA-Bibliotheken und Roharrays bleiben im gesicherten Originalbestand. Ein exportierter Ergebnisbericht ersetzt nicht die tatsächlich verwendeten Modelle oder Annotationen.

Das .4-Lieferpaket enthält den Planabgleich, konkrete Prüfprotokolle und Quellenindex. Original-Q1/Q3/Q5 werden nur als Originalfixture bezeichnet, wenn ihre Bytes tatsächlich verfügbar und geprüft sind. Abgeleitete kleine Cancel-Fixtures sind entsprechend benannt und ersetzen nicht den angeforderten Original-123-Request-Export. Ein Q2-Terminalreport ist keine unabhängig nachgezählte Q1-Rohdatei. Downloadfehler bleiben als Quellenlücke sichtbar.

Ein Replay schreibt neue Darstellung separat; vergangene `run_manifest`, Requests, Fingerprints und Qualitätsentscheidungen bleiben unverändert. Die alte kanonische KB vom 8. September ist die historische Quelle dieses Updates und bleibt als vorherige Fassung nachvollziehbar. Gleiche Dateinamen von Standalone-R1-Paketen beweisen keine gleichen Bytes.

### 14.1 Was der Git-Push tatsächlich gesichert hat

Die Nutzerkonsole belegt:

```text
Repository: Keff789/onnx-splitpoint-results
Branch: main
Commit: 5636017e5db3229862ba10c609b5f4b5f290e76b
GIT_PUSH=PASS
236 files changed
```

Das hochgeladene `har_and_git_evidence.zip` enthält denselben vorbereiteten **236-Dateien-Nachtrag**. Die Pushkonsole meldet genau diesen Auswahl-/Commitumfang; ihr diff-stat kürzt Dateinamen ab, weshalb daraus nicht jeder vollständige Pfad nochmals bytegenau rekonstruiert wird. Primär liegen die vollständigen Pfade und Bytes im Ergebnisarchiv. Ein neuer Liveabgleich des GitHub-HEAD war hier nicht verfügbar. Keine Aussage über unbekannte spätere Commits. [E-GIT-PUSH] [E-KB-REV2-CHECK]

**Ergebnisse und erste maschinell erzeugte Einordnung sind bereits gesichert:**

```text
results/hailo8/20260912_mobilenet_gpu/
  compute/
  build_metadata/
  runtime/
  har_emulation/hailo8_har_git_20260912T171411Z_x0j2t2o1/
    comparison.json
    comparison_request.json
    REPORT.md
    CLAIM_BOUNDARIES.md
    per_image.csv
    parsed_native/
    quantized/
experiments/hailo8/har_comparison_r1/
results/evaluation/completsetdev_20260911_213508/quality_snapshot/
```

`REPORT.md` enthält Stufentreffer, Maximal-/RMS-/Cosinewerte, Vorhersagewechsel und grundlegende Vergleichsgrenzen. `CLAIM_BOUNDARIES.md` nennt geöffnete Fixed16-Diagnose, späte HAR-Hashes und Cross-Build-Grenze. **Nicht Teil dieses Commits:** die erst danach geschriebene ausführliche Interpretation `AUSWERTUNG_Hailo8_HAR_Vergleich_2026-09-12.md`, KB-REV2 sowie diese REV3 und der nachfolgend zurückgestellte vertiefende Diagnoseplan. Eine Antwort im Chat wird nicht automatisch in Git geschrieben. Für spätere Dokumentcommits liegt in diesem Update kein neuer Nachweis vor.

### 14.2 Publikations- und Ablageregel

`build_metadata/` statt eines im Repository ignorierten `build/`-Verzeichnisses für kleine Receipts/Logs nutzen. Keine `git add .`- oder Force-Push-Anweisung als Standard. Neue Dokumentrevision neben Originalergebnisse legen, alte KB-Snapshots erhalten; Index/Claimstatus bewusst fortschreiben. Neu erzeugte Dokumente aus dieser Revision sind zunächst lokale Lieferdateien und **noch nicht gepusht**.

Der damalige Check meldete `fatal=0`, `review=159`, `PASS_WITH_REVIEW`: hauptsächlich lokale Pfade/private Adressen, zusätzlich eine heuristische password-like-Zeile in Diagnosesource. Das sind keine 159 fehlgeschlagenen Tests und auch keine vollständige Secret-/Lizenzfreigabe. Öffentliche Weitergabe bleibt eine bewusste Prüfung; keine Tokens/Schlüssel oder komplette lokale Arbeitsbäume ergänzen.

### 14.3 Quellcode-Git, Ergebnis-Git und neue Diagnoseablage getrennt

**Quellcode:** `Keff789/ONNX-Splitpoint-Tool`. Historischer `origin/main` beim Einrichten `ef44c94`; v2.82-Baseline `fdad47854c67e759050a184d8a2717642271ea45`, Tag `baseline-v2.82-smartmirror2-20260914`; darüber `c5eb66eaa562728e9397a550570740d6a03e734d` mit `AGENTS.md`. Branch `smartmirror2-v282-baseline` und Tag wurden laut Konsole erfolgreich gepusht. Danach Branch `codex/v283-nightfix-smokes`, R1–R8 uncommitted; **kein späterer Push belegt**. Das ist nicht der Ergebnis-Git-Commit `5636017…` aus §14.1. [E-CX-SETUP] [E-CX-R8]

**Lokale Arbeits-/Ergebnisausgaben:** `~/.local/share/onnx-splitpoint-codex/` mit eindeutigem Auftragsordner. Früheres `.codex_runs/` im Sourcebaum verursachte zehntausende unerwartete Verifierdateien und Symlinks; die Diagnoseablage wurde bewusst herausverlegt. Kein neuer Sourceausnahme-/Hashmechanismus, nur saubere Trennung von Produkt und Runtimeausgabe. [E-CX-R3] [E-CX-R8]

**Öffentliches Repository:** Keine `.venv*`, Liveprofile, `.codex/auth.json`, private Schlüssel/Tokens, Modelle, Bilder, HEFs/DXNNs/Engines, Vendorbibliotheken oder große Roharrays committen. Normale Runtime-Logs nicht pauschal ins Source-Git nehmen; ausgewählte redigierte Diagnosebelege gehören gegebenenfalls ins Ergebnis-Git. `.gitignore` wirkt nicht rückwirkend auf bereits versionierte Dateien. Frühere grobe Regexscans hatten False Positives bzw. sogar einen Syntaxfehler; „keine Kandidaten“ war dann kein belastbarer Secret-PASS. Vor erneutem öffentlichen Push den tatsächlich zu veröffentlichenden Bestand prüfen. [E-CX-SETUP]

R8 ist bereits installiert, aber sein kumulativer Textpatch ist **kein vollständiges Distributionsbundle**: ein schon vorhandenes binäres Testfixture wird nur referenziert. Künftige Releases müssen erforderliche Fixtures, Produktdateien und Konfigurationsmigrationsschritte vollständig enthalten; ein erfolgreicher bestehender Arbeitsbaum allein beweist keinen vollständigen frischen Installationspayload. [E-CX-R8]

Aktuelle KB-/Arbeitsstanddateien sind Dokumentartefakte, kein automatischer Git-/Hostupdate. Das Begleitpaket bewahrt die Ausgangs-KB byteidentisch, einen Textdiff und reine Dokumentprüfungen. Keine Änderungen am laufenden Run. [E-REV4-DOC]

### 14.4 Veröffentlichtes Git am 19.09.2026 und vorbereitete Sicherung

Live gelesener Evidence-HEAD: `5636017e5db3229862ba10c609b5f4b5f290e76b` vom 12.09.2026,
„Archive Hailo8 GPU evidence and fixed16 HAR comparison“. Veröffentlicht sind dort bisher unter
`results/acceptance/` v2.79.16/v2.79.29; kein v2.83-Verzeichnis. Bereits archivierte Hailo8-/HAR-
Dateien werden im vorbereiteten Nachtrag nicht erneut kopiert. [E-REV5-GIT]

Source-Branchliste: `main` bei `ef44c9446bb90a837637746ef8651bae552d126f`,
`smartmirror2-v282-baseline` bei `c5eb66eaa562728e9397a550570740d6a03e734d`.
Der lokale Arbeitsbranch ist in dieser Remote-Liste nicht veröffentlicht. Der heutige lokale
Host-HEAD/Index wurde nicht abgefragt; frühere Kumulativpatches sind keine bereits gepushten Commits.

Die Lieferung enthält einen **reviewbaren Evidence-Patch mit exakter Dateiliste**, keine Gitänderung.
Er ergänzt ausgewählte R8/R9B/R9C-Abnahmen, R9G-Ergebnisse und relevante negative H10/R9E-Belege.
R9H steht nur als Zwischenstand im öffentlichen Statusauszug; keine laufenden kompletten Logs als
finale Evidenz. Die vollständige private KB wird nicht blind ins öffentliche Repo übernommen;
der Public-Patch enthält einen bereinigten Statusauszug und Quellenzuordnung.

<a id="grenzen"></a>
## 15. Klärungen gegen wiederkehrende Fehlannahmen

| Verkürzung | Verbindliche Einordnung |
|---|---|
| „Für fertig müssen alle Qualitätsfelder grün sein.“ | Fertig ausgewertet kann korrekt FAIL sein; keine Margenlockerung oder Fallauswahl nach Ergebnis. |
| „123/123 terminal heißt 123 Qualitätsberechnungen.“ | Im Q5-Soll: 63 ausgewertet, 60 Abbruchfolgen; Requestzahl und unabhängige Hardwaremesszahl unterscheiden. |
| „Service geschlossen ist immer harmloser Cancel.“ | Nur mit passendem vorangehendem Run-Cancel; sonst technischer Fehler. |
| „GPU-HEF ist bei gleicher Recipe derselbe Qualitätsfall.“ | Konkrete Artefakt- und Vorhersageidentität zählt; keine fremden Ergebnisse übernehmen. |
| „GPU-Präferenz muss CPU-HEFs ersetzen.“ | Gültige vorhandene HEFs wiederverwenden, unabhängig vom Baugerät. |
| „Hailo8 hat jetzt 12/16 wie Hailo10.“ | H8: 8/16 CPU-HEF, 10/16 GPU-HEF; H10 historisch 12/16 für beide. |
| „Gleiche FLOAT32-Feeds beweisen gleiche interne UINT8-Puffer.“ | Interne UINT8-Puffer wurden in dieser H8-Probe nicht erfasst. |
| „Besseres Fixed16 rechtfertigt automatischen HEF-Tausch.“ | Kleine geöffnete Diagnoseprobe, kein allgemeiner Qualitätsvorteil und kein B5000-PASS. |
| „Opt2/B1024 sollten wir einfach nochmal versuchen.“ | Historischer Opt2-Befund und eingefrorene Transfer-/Evaluationspolicy schließen den pauschalen Sweep aus. |
| „Fehlender Debugexport ist ein Hailo-Modellfehler.“ | Q5 überschreitet das alte 32-MiB-Deskriptorsummenlimit mit gültigen Requests. |
| „AP-Fast-FAIL mit 0 Bootstraps ist nicht fertig.“ | Vollständige Vorhersagen und erlaubter früher Punktentscheid können abgeschlossen FAIL sein; kein fingiertes CI. |
| „Eine Sekunde × drei Replikate ist finale Energieabnahme.“ | Dauer-/Work-Unit-Vertrag und Scope bleiben zu prüfen. |
| „HAR-Emulation fehlt weiterhin vollständig.“ | R1 `SDK_NATIVE` und `SDK_QUANTIZED` sind ausgeführt; zusätzliche optimierte Floatstufe und Integer-I/O-Ursachenklärung sind nicht ausgeführt, aber ausdrücklich zurückgestellte Folgearbeit, keine aktuelle Pflicht. |
| „Alles nach Parsed ist reine Quantisierungsrundung.“ | Der tatsächliche Übergang umfasst Modell-/Floatoptimierung und Quantisierungsverfahren. |
| „9/16 Emulation und 10/16 Hardware sind nahezu identisch.“ | Vier verschiedene Top-1-Klassen und merkliche Logitabweichung; ähnliche Accuracy ist keine numerische Parität. |
| „Der spätere ausführliche Chattext ist mit dem Ergebniscommit gespeichert.“ | Automatischer Report und Grundgrenzen ja; spätere Interpretation/REV2/REV3 nein, solange kein weiterer Dokumentpush belegt ist. |
| „Ohne weitere Ursachenanalyse ist das negative Ergebnis nicht berichtsfähig.“ | Ein korrekt ausgeführtes und gebundenes negatives Resultat kann unter klaren Grenzen berichtet werden; eine stärkere Ursachenbehauptung ist eine andere Frage. |
| „Wir müssen alle Netze so lange verbessern, bis sie bestehen.“ | Nein. Bewertet wird das feste automatische Verfahren. Qualität, technische Misserfolge und Ausführbarkeit werden vollständig berichtet. |
| „Dann können wir bekannte Toolfehler als Compilerverlust stehen lassen.“ | Nein. Bekannte eigene Fehler korrigieren oder als technische Einschränkung kennzeichnen; kein regulärer Qualitätsverlust daraus machen. |
| „Mit genügend Tuning werden alle Netze gut.“ | Nicht belegt. Verbesserungen sind mögliche Folgearbeit mit unbestimmter Wirksamkeit und Aufwand, keine Garantie. |
| „Die Scopeentscheidung lockert die 1-pp-Marge oder den Messvertrag.“ | Nein. Qualitäts-, Daten-, Endpunkt-, Energie- und Claimregeln bleiben unverändert. |


### 15.1 Ergänzende Fehlannahmen aus der Codex-Reihe

| Verkürzung | R8-Einordnung |
|---|---|
| „Codex läuft auf dem Rechner, daher sind seine Tests automatisch realistischer.“ | Nein. Privater Candidate/Registry/Collector kann vom normalen GUI-Pfad abweichen; diese Lücke verursachte den R7-Energieausfall. |
| „Die Sandbox hat keinen Prozess gesehen, also ist die GUI aus.“ | Falsch. Begrenzte Prozesssicht ist kein Hostquieszenzbeleg; vorhandene Hostprüfung und Produktlocks nutzen. |
| „19 historisch genannte Tests dürfen rot bleiben.“ | Erst Ursache/Fixturevertrag klären; R6 behielt die Knoten und brachte sie mit echten Negativszenarien wieder zum Bestehen. |
| „Final muss vor jeder Ablaufänderung laufen.“ | Nein. Kleiner echter GUI-Smoke, passende negative Prozess-/Konfigurationstests; große Kampagne separat. |
| „Standard beeinflusst nur Qualitätsbilder.“ | Seit R8 zusätzlich Native 100/10/1; Final 1000/100/3. Historische Runs behalten ihre Werte. |
| „`Finished (warnings)` bedeutet unbrauchbar.“ | Runtime/Vertrag/Energie können vollständig sein, während Quality FAIL bleibt. Achsen einzeln lesen. |
| „1.440s im Fulljob sind eine einzelne TensorRT-Inferenz.“ | 24 min Gruppenlauf; typischerweise mehrere Modelle, Backends, Wiederholungen, Warmup und Completed-Task-Nachverarbeitung. |
| „Neun gültige R8-Aufnahmen beweisen sämtliche Energiepfade.“ | Nur H8/MobileNet/3 Nativezeilen und kurzer Messumfang; kein neuer H10-/DeepX-/Langzeitbeleg. |
| „Nacht läuft heißt Nacht technisch PASS.“ | Nur Startmeldung; Endbilanz und tatsächliche Scope-/Artefakt-/Collectorbindung fehlen bis zur Prüfung. |
| „Ein Timeout ist durch einen späteren guten Lauf kausal erklärt.“ | Nein. Erfolgreiche Wiederholung und aufgeklärte Ursache sind verschiedene Aussagen. |
| „Ein Papervergleich mit97 FPS gilt auch für Full oder b044.“ | Nur bei übereinstimmendem b066-Graphschnitt und Messvertrag; sonst getrennte deskriptive Werte. |

<a id="uebergabe"></a>
## 16. Kompakte Übergabe – maßgeblich für die nächste Sitzung

**Stand 04.10.2026:** Hauptkampagne, 192er-Completion und zwölf YOLO-Zusatzfälle
sind abgeschlossen. Keine Messfortsetzung starten. Einstieg ist
[START_HERE](../results/evaluation/thesis20_20261004/START_HERE.md); §23 beschreibt Quellen,
Korrekturen und Grenzen. Die ursprüngliche 20er-Auswahl und neun ungemessene Reserven bleiben unverändert.

**Gemeinsame Bilanz:** 527 historische Genericzeilen; 560 Quality; 246 Native/738
Wiederholungen; 204 Generic-Completion/612 Wiederholungen; 246 Energie/738 gültige
Replikate. 39 Accuracyverluste, 37 negative Builds, 24 Policyfälle und 228 unsupported
werden weiter ausgewiesen. Die alte `partial`-Projektion ist historische Workflowinformation,
keine aktuelle fehlende Messung.

**Release/Archiv:** [Toolrelease v2.92.0](https://github.com/Keff789/ONNX-Splitpoint-Tool/releases/tag/v2.92.0), Maincommit `d164aad6d7c7ef68c1b371c49a1fdea0a3b27dd7`, annotierter Tag und beide Quellenarchive sind veröffentlicht und remote verifiziert. Die zusätzliche Archivierung wartet auf
den laufenden Benutzertransfer; Privatquellen, Messquellstände und Rohdaten sind kein
öffentliches Gitpayload. Erst verifizierte Kopien gelten als gesichert.

**Wissenschaftliche Grenze:** technische Aufnahme vollständig, Vergleichsevidenz
fallbezogen, kein pauschaler wissenschaftlicher PASS. Keine nachträgliche Final-/Hold-out-
Umdeklaration. H8/b066 verwendet den aktuellen Prepared-Input-Dreistufenpfad und die
gebundene aktuelle Engine; historische 97 FPS sind kein automatisch gleicher Vergleich.

<details>
<summary>Historische Übergabe vom 02.10.2026</summary>

**Stand 02.10.2026:** Bestehender Run
`thesis_20splits_n5000_b1000_20260925_20260925_103745`, zuletzt installierter Stand laut
Lieferbericht 2.91.2 mit lokalen Folgepatches. Energie regulär am 02.10. um 03:49:31 beendet,
Finalisierung 05:34:24 +02:00. **Nicht noch einmal starten.** [E-TH20-ENERGY-END]

**Erhalten:** 527 Generic + 37 Buildfehler + 24 Policy = 588; 548 Quality (509 referenznah,
39 Accuracyverlust); 234 Native = 192 Splits + 42 Fulls mit 702 Wiederholungen; 228 unsupported;
234 vollständige Energiezeilen / 702 gültige Replikate aus 705 physischen Collectorversuchen.
Keine ungeklärte planmäßige Messlücke, aber **nicht wissenschaftlich pauschal freigegeben**.

**Jetzt offen:** F01 47 falsche H10-Backendlabels; F02 186 widersprüchliche Native-Authority-
Ablehnungen; F03 sechs lokale TRT-Full-Numerikbelege; F06 Terminal-/Qualityprojektion;
F05 Energie-/Paar-/Rollenexport einschließlich acht DeepX-Decodervergleiche. Zunächst lokale
Originalprüfung und gezielte Auswertungsfixes. **F04** separat: 192 Generic↔Native-Paare ohne
belegte gleiche Completionmessgrenze; Originalzeiten suchen, nur bei echter Lücke zusätzliche
Generic-Completionmessung für die gewünschte Aussage planen. W01–W03 sind Beobachtungen,
keine bereits bewiesenen Fehler. Details/Abnahmen ausschließlich §12 und §22.

**Grenzen:** 39 Accuracyverluste und zwei negative Vendor-Fulls YOLO26s/H8/H10 behalten.
Energie weiterhin als `screening_only`/`diagnostic_only`/nicht claimfähig gespeichert; technische
Gültigkeit nicht mit Claimrolle verwechseln. `partial` nicht allein den 228 unsupported zuschreiben.
Roh-Parquets, Kalibrierungsrohdaten, Tensorarrays und sämtliche Generic-Per-Case-Berichte fehlen
im kleinen Auditarchiv teilweise; dortiges Fehlen ist kein Nachweis fehlender Hostdateien.

**Betrieb/Git:** Keine neue Generic-/Native-/Energie-Gesamtrunde, keine neuen Hash-/Cache-
architekturen, kein Tuning bis PASS, keine automatische Fortsetzung für Reporterarbeit.
Quellcodeveröffentlichung separat: letzter Hostbericht nennt Basis `182092216dfaf4f3ad36460a883098548c83bd8f`
mit uncommitteter Folgearbeit. Nur die Knowledgebase wird mit diesem Dokumentupdate geändert;
kein lokaler Hostzugriff, Toolpatch oder Messstart. [E-TH20-AUDIT] [E-TH20-ENERGY-REENTRY]


</details>

<details>
<summary>Vorherige Übergabe (19.09.2026), nur historische Quellenzuordnung</summary>

### Historische Übergabe vom 19.09.2026 – damaliger R9H-Snapshot

**Stand:** v2.83, Runheader weiter `v2.83-r9b-request-latency`; R9G erfolgreich im technischen
1-Split-Umfang, aber nachgewiesene Energie-/Vergleichs-/Projektrestfehler. R9H eval_02 ab 06:43:23,
letzter hier vorliegender Eintrag 07:19:10 am 19.09.2026. Keine Endfreigabe und keine spätere
Livebeobachtung behaupten. `host.log` gehört eval_01, alte BEFUNDE-Datei R9G. [E-REV5-R9H-LOG]

**R9G:**63/63 Native, 42 Full + 21 Splits,6.300 Requestpaare,77 Quality = 40 PASS / 25 FAIL / 12 INCONCLUSIVE,
189/189 Energie;19.463 Dateien in Core+Nachtrag gegen Index geprüft. Roh-Parquets nicht neu integriert.
H8/H10 s/b021,m/b038: echte Ersatzinferenz statt Reparatur der alten späten HEFs. [E-REV5-R9G-AUDIT]

**R9H-Auftrag:** sieben Modelle, drei technisch verwendbare Splits je Modell/Backend nach normaler
Reihenfolge, Standard 500/500, Native 100/10/1, Native-Energie1s×3, Generic-Energie/Windowprobe aus.
Neue regulär fehlende Artefakte erlaubt, passende reuse, Force aus. 105/315 nur nominal, Plan lesen.
Bisherige Zwischenlogs belegen Auswahl, Cache/Transport und erste Benchmarks, nicht finale Energiefixes.

**Nachweise schließen:** TRT-CLS-Energieworkload inklusive Top-k, gleiche Vergleichseingaben,
zwölf Detection-Endpointprojektionen, korrekte Energieaggregation, stale Authority-/Anzeigenreste.
TRT-Retention-MISSs im fertigen Lauf einordnen. Keine Schwellwertlockerung. DeepX-Zweibilderfehler
und passende b066-Paper-/Rankingauswertung bleiben eigene Grenzen.

**Betrieb:** ein Hauptagent, kurze Kontextdatei, gezielte lokale Tests, normale Host-GUI-/GPUausführung,
keine privaten Bindings als notwendige Benutzerarbeit. Begrenzte iterative Versuche nach konkretem Fix,
kein Tuning bis PASS und keine neue Hash-/Cachearchitektur. Neu starten/fortsetzen setzt kein Budget zurück.

**Git:** Ergebnisrepo live noch12.09. / 5636017; Source-Branches nur main/ef44c94 und Baseline/c5eb66e.
REV5+Evidencepatch vorbereitet, nichts gepusht. Während R9H keine Source-/Manifeständerung;
nach Supervisorende aktuellen Source- und Ergebnisstand getrennt und überprüfbar sichern.


</details>

<a id="aenderungen"></a>
## 17. Änderungsprotokoll

### 4. Oktober 2026 – gemeinsamer THESIS20-Abschluss

Live geprüfter Messbestand, korrigierte Basis, vollständige 192er-Completion und YOLO-
Augmentierung zusammengeführt; Fallzahlen, Replikate und physische Aufnahmehistorie
getrennt bilanziert. Neue reproduzierbare Tabellen/Grafiken und Quellenrelease verknüpft.
Alte Aufgaben/Übergaben datiert erhalten, aktuelle §12/§16/§23 synchronisiert. Keine neue Messung.


### 2. Oktober 2026 – THESIS20 abgeschlossen; Ergebnis-Audit und lokale Nacharbeit

Kopfstand, aktuelle Aufgaben, Betriebsregel und Übergabe auf den abgeschlossenen THESIS20-Run
fortgeschrieben; bisherige R9G/R9H-Kopf-/Aufgaben-/Übergabetexte ausdrücklich historisch erhalten.
§22 ergänzt tatsächliche 527/548/234-Ergebnisbilanz, 702 gültige Energiereplikate aus 705
Versuchen, Rechen-/Plausibilitätsprüfung mit Grenzen und F01–F06/W01–W03. Korrektur der
verkürzten Deutung von `partial`; Messvollständigkeit, wissenschaftliche Vergleichbarkeit
und Claimrolle getrennt. Quellen-/Installations- und Toolveröffentlichungsgrenzen benannt.
Kein erneuter Lauf, kein Produktfix und keine neuen Messungen durch diese Dokumentänderung.
Vorheriger Repo-HEAD beim Lesen: `a18d03edaf1008d82e28f55187e5c2988e241a48`;
geänderter Gegenstand ausschließlich `docs/KNOWLEDGEBASE.md`. [E-TH20-KB-UPDATE]

### 19. September 2026 – REV5: R9A–G, Energie-Endprüfung und R9H-Snapshot

Aktuelle Kopf-, Aufgaben-, Betriebs- und Übergabeabschnitte ersetzen die alten R8-Gegenwartsaussagen.
Wissenschaftliche Altabschnitte und Messwerte bleiben erhalten. Ergänzt: tatsächliche GUI-/Host-
Integration, allgemeines Nachrücken und metadata-first Erstaufrufe, echte Bildlatenz/Top-k,
negativer H10-Präzisionskandidat, allgemeine R9E-Builderfixes, R9G 63/189 mit Endprüfung und den
konkret noch offenen Energie-/Input-/Projektionen. R9H ausdrücklich nur eval_02-Snapshot 07:19:10;
kein Schluss aus eval_01 oder einer alten Befunddatei. Live-Gitabgleich und getrennte private
KB/public Evidencevorbereitung dokumentiert. Kein neuer Test/Build/Run/Commit/Push. [E-REV5-DOC]

### 15. September 2026 – REV4: Codex, R1–R8, GUI-Integration und nächste Auswertung

Aus der unverändert erhaltenen v2.80.4-REV3 fortgeschrieben. Kopfstand/Übergabe/Aufgabenliste auf tatsächliches R8-Hauptrepo und normale Konfiguration aktualisiert; alte .4-Installationspflichten historisiert. Neue Quellenrang-/Statusregeln trennen implementiert, Hauptrepo, Config, lokale Tests, reale GUI und wissenschaftliche Vergleichbarkeit.

Codex-Installation auf x86-Smartmirror2, ChatGPT-Login, Gitbaseline/Branch, Sandbox-/Lock-/ACL-Erfahrungen, `AGENTS.md`, Ultra-Aufträge, sichtbare Tagesausführung und abgeschaltete automatische Nachtstarter als Betriebshistorie dokumentiert. Normale GUI-Testkette, klein begrenzter H8-Smoke, R8-Standard/Final-Budgets, Collector-/Policymigration und kompakte Logs aufgenommen. Der späte Pipefix bleibt nach Hardware nur lokal geprüft.

Die R4/R5-Endpaketprobleme, R6-Erfolg, R7-Storage-/Shutdownfehler und normale GUI-Energielücke sind getrennte Befunde. H10-Resolver versus offene Nulloutputs, DeepX-500-/5000-Bildgrenze und erhaltene H8-Nachweise präzisiert. Neue Nacht-/Performance-/Energieplausibilitätsaufgaben mit b066-97-FPS-Vergleich hinzugefügt. Nutzer meldet laufenden Nachtlauf; kein Endergebnis erfunden. R8-JUnit erneut gezählt, Quellen/Dokumentstruktur geprüft; keine neue Produkt-/Hardwareausführung oder Gitveröffentlichung. [E-REV4-DOC]

### 13. September 2026 – REV3: Untersuchungsumfang und Stopregel

Auf der unveränderten beigefügten REV2 fortgeschrieben. Forschungsfrage als automatisierte Partitionierung unter festgelegter Backend-/Build-/Validierungspolitik formuliert; „einfach so“ präzisiert. Implementierungsfehler, optionale Ursachenanalyse und modellspezifisches Tuning getrennt. Abschlusskriterium auf vollständige nachvollziehbare Ergebnisbilanz statt alle Fälle PASS festgelegt. Zusätzliche Hailo8-Optimized-Float-/Integer-I/O-Vertiefung ausdrücklich zurückgestellt und aus den aktiven Checkboxaufgaben entfernt; technische Skizze bleibt als optionale Folgearbeit erhalten.

Die ergänzende Vergleichsperspektive Split versus Full-Backend neben der kanonischen Floatreferenz aufgenommen, ohne neue Akzeptanzgrenze. Formulierungsbaustein für die Dissertation und zurückhaltende Aussage zu möglichem Tuningnutzen ergänzt; kein Erfolg für alle Netze garantiert. Grobe Aufwandsbereiche aus dem Chat als ungemessene, nicht beauftragte Planung eingeordnet. AP5, Abnahme, Fragenkatalog, Git-Dokumentstatus und Übergabe konsistent fortgeschrieben. Sämtliche vorhandenen Ergebnistabellen und deren Aussagegrenzen bleiben erhalten. Keine neue Messung, Produktimplementierung, Release-/Hardwareabnahme oder Gitveröffentlichung. [E-SCOPE-REV3] [E-KB-REV3-CHECK]

### 12. September 2026 – REV2 nach HAR-/Git-Abgleich

Auf der beigefügten .4-KB fortgeschrieben, nicht neu aus einem alten Release rekonstruiert. Quellenverfügbarkeit und .4-Implementierungsbehauptung getrennt. Forceherkunft, Familien-GPUkontexte, reale Release-/Workflow-Fehlerketten, Reuse-/Energie-/Nachtgrenzen ergänzt. Die Originalstufen des HAR-R1-Archivs erneut nachgezählt: 13/13/13/9/10/8 Top-1; erste große Abweichung und Restabweichung ehrlich getrennt. Noch ausstehende HAR-Emulationstexte auf den ausgeführten Stand berichtigt. Vertiefte Diagnose nur als neuer bedingter Vorschlag.

Gitcommit, 236-Dateien-Scope, tatsächlich gesicherten Report und nicht mitgespeicherte spätere Interpretation dokumentiert. Qualitäts-Cancelpopulation 63/60 direkt aus Original gelesen. Vorhandene Methoden-, YOLO11l-B5000- und Opt2-Entscheidungen erhalten; fehlende Originalexporte hierfür nicht erfunden. Kein Toolpatch, keine neue Messung, kein Push.

### 12. September 2026 – v2.80.4, übernommene Ausgangsrevision

Aktuelle Kopfidentität, Releasefortschritt und Aufgabenliste auf .3-FIX5/.4 fortgeschrieben; v31-Planaufträge historisiert. Hailo8/Hailo10-Fixed16 getrennt, MobileNet-B5000-FAILs aus dem neuen Plan eingeordnet, abgeschlossene YOLO11l-Qualität mit vollständigen Vorhersagen und historische Opt2-Entscheidung aufgenommen. Alte automatische Wiederholungs- und Optimierungsvorschläge gestrichen. Cancel-, Debugbudget-, Overlay-, Reuse- und Quellenregeln integriert. Originalergebniswerte und vorhandene wissenschaftliche Methodik unverändert.

### 8. September 2026 – konsolidierte Fortschreibung nach R2

Die bisherige v17-Kopfidentität wurde als historischer Stand abgelöst, nicht als aktuelle Installationsanweisung weitergeführt. Methodenrahmen, Fragen-/Boundarythemen, FS-Primärmessung, Generic-/Native-Scope, Rankinggrenzen und einfache Evidenzablage bleiben erhalten. [E-KB]

Neu integriert sind die v26–v30-DeepX-Full-Fehlerfolge, die unabhängige v30-Teilabnahme, der bestätigte Abschluss-Cachefehler und dessen enger Fix, die acht Complete-Set-Fehlergruppen beziehungsweise zusätzlichen Hailo8-Bindungslücken, korrekte Ergebnis-/Energie-/Qualityzähler und der aktuelle v31-Plan REV4 FINAL. [E-V30] [E-PLAN31]

R1/R2 ersetzen die allgemeine DeepX-Pre-/Postprocessing-Ursachensuche durch einen konkret bestätigten Build-/Profil-Normalisierungspfad. Die MobileNet-Klassifikationsqualität bleibt trotzdem offen: kleine Nenner, gleiche Bild-IDs, Logitähnlichkeit und Accuracy sowie historische B500-Werte sind jetzt ausdrücklich getrennt. Überzogene Aussagen zum bereits bewiesenen Anteil des B500-Gewinns sind eingegrenzt. [E-R1] [E-R2]

Zusätzlich wurden beim Dokumentabgleich die tatsächlich gespeicherten **1-s-Energieaufträge** und die spätere FS-Gain-/M.2-Idle-Anwendung aufgenommen. Nicht vorhandene ursprüngliche Kalibrierungsbelege werden nicht als hier geprüft ausgegeben; die Abweichung zwischen einer alten Gateuntergrenze und einem später verifizierten Faktor bleibt sichtbar. [E-CS] [E-DOC]

Diese Beschreibung betrifft das historische Dokumentupdate vom 8. September, nicht die neue .4-Softwarelieferung. Originale Messdaten und frühere Snapshots bleiben unverändert.

<a id="codex"></a>
## 18. Codex auf Smartmirror2 – Betriebs- und Übergabevertrag

### 18.1 Architektur und Aufgabenverteilung

```text
Chat hier: Originalruns analysieren, Ursachen/Hypothesen trennen, Auftrag schreiben
    ↓ Plan + relevante Ergebnisbelege
Smartmirror2 (x86-64): Codex CLI im bestehenden ONNX-Splitpoint-Repository
    ├─ Source lesen/ändern und lokale Tests
    ├─ normale Tk-/GUI-Integration prüfen
    └─ bestehender Splitpoint-Transport → Jetson/H8/H10/DeepX, u.RECS
    ↓ Abschlussbericht + tatsächliche Kommandos/Testlogs + vollständiger Diff
Gegenprüfung hier; Benutzer entscheidet über größeren Lauf / Veröffentlichung
```

Codex ist kein neu erfundener Benchmarkrunner. SSH, Profile, bestehende Lock-/Lease-/Cleanupmechanismen und Ergebnisimport bleiben Produktpfade. Diese Chat-Sitzung erhält durch die CLIinstallation **keinen direkten Hostzugriff**. Chatkontext/KB/Erinnerungen sind außerdem nicht automatisch der Kontext einer neuen Codex-Sitzung: den schriftlichen Auftrag und die relevanten Dateien ausdrücklich nennen. [E-CX-SETUP] [E-CX-PREF]

### 18.2 Tatsächlich beobachtete Installation und Git-Baseline

| Punkt | Belegter lokaler Stand / Grenze |
|---|---|
| Host | Smartmirror2, x86_64, Ubuntu 24.04; normaler lokaler Benutzer, SSH über MobaXterm und zusätzlich NX verfügbar |
| Tool | `~/ONNX-Splitpoint-Tool`, Python 3.12.3 und vorhandene `.venv` laut Einrichtung |
| Codex | `/usr/local/bin/codex`, **`codex-cli 0.154.0`** laut Konsole; kein späteres CLIupdate belegt |
| Installation | `npm install -g @openai/codex` zunächst EACCES, anschließend `sudo npm install -g @openai/codex` erfolgreich; **Codex selbst als normaler Benutzer**, nicht `sudo codex` |
| Node/npm | Zum Einrichtungszeitpunkt Node 18.19.1/npm 9.2.0; keine neue Empfehlung, diese Versionen festzuschreiben |
| Authentifizierung | `codex login status`: **Logged in using ChatGPT**; Credentials lokal, nie in Ergebniszip/Git/Chat kopieren |
| Konfiguration | `~/.codex/config.toml`; Projektpfad als `trusted` eingetragen. Trust ist kein Nachweis von Hardware-/Shellrechten |
| Erster Agent | `gpt-6-astra`, anfangs `xhigh` sichtbar; später Ultra ausdrücklich beauftragt |
| Ausgangsbaum | Kopierter Release ohne `.git`; bestehende öffentliche History eingebunden, Arbeitsdateien nicht durch alten GitHubstand ersetzt |
| Historische Referenzen | `ef44c94` alter main → `fdad478` v2.82-Baseline → `c5eb66e` AGENTS; Baselinebranch/tag gepusht, späterer Arbeitsbranch/R8 nicht als gepusht belegt |

Der Baseline-Tag ist `baseline-v2.82-smartmirror2-20260914`. Vor jedem neuen Auftrag **aktuellen** Branch, HEAD, Änderungen und Importpfade dokumentieren. Nicht für jeden Folgefix wieder von c5eb66e anfangen: Nachfolgende Aufträge müssen den zuletzt übernommenen geprüften Stand erhalten. Ein Branch schützt nicht vor einem gleichzeitigen anderen Prozess, der dieselben Arbeitsdateien verwendet. [E-CX-SETUP] [E-CX-R8]

### 18.3 Genehmigungsfreiheit, Sandbox und Hostprozesssicht

Der Nutzer will autorisierte Aufträge ohne ständiges Bestätigen von `ls`, `rg`, `cat` oder Testkommandos. Das gilt **innerhalb des definierten Auftrags**, nicht als pauschale Erlaubnis für neue Kampagnen, Systemänderungen oder Cachelöschung. Für die späteren Aufträge wurden verwendet:

```toml
approval_policy = "never"
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = true
```

Das ursprünglich eingerichtete benannte Profil hieß `splitpoint-unattended`; der R8-Starter setzt die entsprechenden Flags unmittelbar. **`never` heißt: keine technischen Genehmigungsdialoge, blockierte Aktionen liefern Fehler; es hebt die Sandbox nicht auf.** Netzwerkfreigabe ist nicht automatisch eine Beschränkung auf die Jetsons. Nach einer erlaubten SSH-Verbindung gelten remote die Rechte des SSH-Benutzers; die lokale Schreibbegrenzung macht Remoteaktionen nicht von selbst read-only. [E-CX-SETUP] [E-CX-R8-STARTER] [E-CODEX-OFFICIAL]

Zusätzliche Schreibpfade je Auftrag gezielt bestimmen: externer Ausgabeordner, benötigte Produktlocks, bei ausdrücklich erlaubter Configintegration `~/.onnx_splitpoint_tool`, bei echtem Workflow sein normaler Ergebnisbereich. R8 erhielt konkret **den Ausgabeordner, die normale Toolconfig und `~/Models/EvaluationRuns`** über `--add-dir`. Das ist weiter als die früher nur freigegebenen Lockordner und muss als bewusster Integrationsscope dokumentiert bleiben. Kein globales Home-/Filesystem-Writerecht als Standard. [E-CX-R8-STARTER]

**Tatsächliche frühere Blockaden:**

| Problem | Beobachtung / künftige Behandlung |
|---|---|
| Linux-Sandboxstart | `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`; `doctor` war vorher grün, `pwd` allein lief, weitere Reads eskalierten. Echten Ausführungscheck statt reiner Configprüfung verlangen. |
| AppArmor/Usernamespace | Beide beobachteten Sysctlwerte1; eine gezielte Hostprofilreparatur wurde vorgeschlagen, spätere Sandboxarbeit funktionierte. Vollständiger finaler AppArmor-Konfigurationsdiff liegt nicht vor; keine pauschale Sysctl-Deaktivierung dokumentieren. |
| Produktlocks außerhalb Repo | Schreibschutz auf `~/.onnx_splitpoint_tool/locks/workflow_platform_interlock.lock` blockierte vor SSH; nur passende erlaubte Pfade ergänzen, keine Locks löschen. |
| Versteckte Host-GUI | Sandbox konnte Prozessende nicht beweisen; R7 blieb im isolierten Kandidaten. Hostpreflight/Hostübernahme statt `ps` im eingeschränkten Namensraum als vollständigen Beweis verwenden. |
| ACL-/TMP-Konflikt | Usernamespace-/ACL-Metadaten führten zu `EINVAL`; eigener Ausgabebereich und isolierter Hostgegenversuch nötig. Nicht Produkt-Rechteerhalt abschalten. |
| Tk-/Displayzugriff | Reales HOME/Xauthority/Display muss erreichbar sein; Test-HOME kann GUItests überspringen. Ein Skip ist kein GUI-PASS. Nur kontrollierte Dialogantworten ersetzen, nicht den zu prüfenden Resolver. |

`-a never` allein repariert eine defekte Sandbox nicht. Kein `danger-full-access`, kein `--dangerously-bypass-approvals-and-sandbox`, kein passwortloses globales sudo als Standardlösung. Hostadministration, Dependencybeschaffung und private Collectorbuilds benötigen einen konkret erweiterten Auftrag. [E-CX-SETUP] [E-CX-R2] [E-CX-R3] [E-CX-R7]

### 18.4 AGENTS.md, Modelle und mehrere Agenten

`AGENTS.md` im Repositoryroot enthält dauerhafte Projektregeln. Die offizielle Dokumentation beschreibt deren Einlesen beim Start und verzeichnisbezogene Priorität; sie ist **keine OS-Berechtigung und keine garantierte Prozessüberwachung**. Lange KB nicht blind als AGENTS-Ersatz einkopieren; knappe Regeln und konkrete Verweise auf Plan/Arbeitsstand sind sinnvoller. [E-CODEX-OFFICIAL]

Dauerhaft beibehalten: Controllerrolle korrekt; Auftrag/Source/Tests zuerst lesen; keine unbeauftragte Scopeausweitung; Originaldaten und Liveprofile erhalten; Force OFF/Reuse vor Build; keine neuen Hash-/Cache-/Identitysysteme ohne Auftrag; bekannte negative Compileevidenz respektieren; keine numerischen Grenzen, Splits, Seeds oder Rezepte bis PASS optimieren; keine breiten Prozesskills/Locklöschung; keine Commits/Pushes ohne ausdrücklichen Auftrag; nach Test ehrlicher Bericht einschließlich NOT_RUN/BLOCKED. R8 ergänzt normalen GUI-/Confignachweis und fortgeschriebene Arbeitsliste. [E-CX-SETUP] [E-CX-R8]

**Modellentscheidung:** Für anspruchsvolle komponentenübergreifende Reparaturen und getrennte Reviews ist Ultra ausdrücklich gewünscht, nicht erst als letzte Rettung. Im konkreten R8-Starter steht `-m gpt-6-astra -c 'model_reasoning_effort="ultra"'`. Das ist die aufgezeichnete lokale Anforderung, keine zeitlose Zusage für jede CLI-/Kontoversion. Wirksame Einstellung in jeder Sitzung prüfen/dokumentieren. `xhigh` ist eine Reasoning-Einstellung, keine alternative Toolversion. [E-CX-PREF] [E-CX-R8-STARTER]

Ein Hauptagent besitzt Schreib- und Hardwareverantwortung. Zusätzliche Agenten können unabhängig lesend Source, Originalbefunde, Testabdeckung oder Patch prüfen. Nicht mehrere Agenten auf dieselbe Hardware/Messquelle schicken und keine konkurrierenden Änderungen derselben Dateien. Mehr Modellaufwand ersetzt keine passende reale Abnahme. [E-CX-PREF] [E-CODEX-OFFICIAL]

### 18.5 Sichtbare Tagesausführung und nachweisbares Ende

**Standard für Tagesaufträge:** sichtbare Terminalausgabe, genehmigungsfreie Ausführung des begrenzten Plans, eindeutige Abschlussantwort, Ergebnis-ZIP und offen gebliebene Punkte. Kein unsichtbarer Hintergrundprozess nur wegen `never`. `codex exec` ist nicht-interaktiv und kann trotzdem im Vordergrund mit `tee` laufen; `-o` speichert die Abschlussantwort, `--json` liefert bei ausdrücklich benötigter Maschinenanzeige Ereignisse. [E-CX-PREF] [E-CODEX-OFFICIAL]

Der folgende Auszug dokumentiert das R8-Startmuster, **kein jetzt auszuführender Auftrag während des Nachtlaufs**. Hostpreflight, vorhandene Locks, externer eindeutiger `$OUT` und Plan müssen vom Starter vorbereitet sein:

```bash
codex -C "$REPO" -m gpt-6-astra \
  -s workspace-write -a never \
  -c 'model_reasoning_effort="ultra"' \
  -c 'sandbox_workspace_write.network_access=true' \
  --add-dir "$OUT" --add-dir "$HOME/.onnx_splitpoint_tool" \
  --add-dir "$HOME/Models/EvaluationRuns" \
  exec --color never -o "$OUT/CODEX_ABSCHLUSS.md" \
  "$(cat "$OUT/START_PROMPT.txt")" 2>&1 | tee "$OUT/codex.log"
# Im echten Starter PIPESTATUS unmittelbar sichern:
# Codex-Exit und tee-Exit sind verschiedene Werte.
```

Der Nutzer hat die tatsächlich aufspringende GUI im R8-Smoke ausdrücklich begrüßt. Fertigen Resultatdialog mit OK und fertiges Workflowfenster mit Close bestätigen; aktive Haupt-GUI nicht schließen, solange Testcallbacks sie noch verwenden. Nach dokumentiertem gesamten Auftragsende regulär schließen; während einer laufenden Kampagne keine Testfenster als fertige Entwicklungssitzung behandeln. Ein Shellinterrupt beweist nicht das Ende des GUI-Prozesses. [E-CX-PREF] [E-CX-R8]

**Beendigungsnachweise getrennt:** Agentenprozess beendet/Exitcode; Sourceprüfung; normale Config aktiviert; lokale Testfälle; tatsächlich gestarteter GUI-/Hardwarelauf; dessen terminaler Bericht; Ergebnisarchiv. Ein `failed to record rollout items` betrifft zunächst die Codex-Verlaufsspeicherung; Produktstatus aus unabhängigen Reports lesen. Fehler nicht verschweigen, aber nicht automatisch als Benchmarkabsturz behandeln. [E-CX-R8]

### 18.6 Nachtbetrieb und Lehren aus dem gescheiterten Autostart

Der alte Ablauf meldete `UNATTENDED_STARTED=1`, obwohl nur die **Vorbereitung** gestartet war. Wegen ungeklärtem Collectorende schrieb Codex `NACHTSTART.json` mit `ready:false`; Supervisor endete als `BLOCKED_NO_NIGHT`. Kein Startversuchbeleg existierte, und der separat gelieferte Diagnosefallback war nicht eingerichtet. Das war eine nicht erfüllte Nutzeranforderung an den nächtlichen Ablauf, kein erfolgreich absolvierter Nachtlauf. [E-CX-AUTO]

Künftig: normale Kampagne bewusst starten und unabhängig von Modellaufrufen laufen lassen. Eine beauftragte Hintergrundvorbereitung braucht Live-/Abschlussstatus, Startnachweis des **Benchmarks**, Stopmöglichkeit und einen vorab ausdrücklich vereinbarten Fallback. Keine Erfolgsmeldung aus bloßem Supervisorstart und kein stiller Wechsel auf „ohne Energie“. Eine absolute Startgarantie trotz aktiver Jobs/defekter Konfiguration ist kein zulässiges Ziel. [E-CX-PREF]

Die lokale Benchmarkrechnung braucht keine dauernden Codex-Logchecks. Modellverbrauch entsteht bei Modellarbeit, nicht automatisch durch jede Stunde Jetsonrechnung; eine neue Logauswertung ist zusätzliche Modellarbeit. ChatGPT-Login und optionales APIbilling nicht aus einer bloßen Tokenzahl gleichsetzen. Diese KB legt keine aktuellen Tarife/Quoten fest; solche Angaben separat aus aktuellem Konto/Herstellerbeleg lesen. [E-CX-SETUP]

### 18.7 Lieferung und Übergabe an die nächste Reparaturrunde

Externer Ausgabeordner pro Auftrag; Abschlussbericht, genaue Kommandos/Exitcodes, Tests mit Knoten/Scopes, JUnit, Hauptrepo-Importpfade, Configdiff/Backups, GUI-/Hardwarebelege, vollständiger Patch einschließlich neuer notwendiger Dateien, Archiv-Inventar und fortgeschriebene Aufgabenliste. Originalruns nicht in-place neu exportieren. Keine Binaries, Credentials, großen Roharrays/Modelle oder Venvs im kleinen ZIP; ausgelassene notwendige Releasefixtures ausdrücklich referenzieren. [E-CX-R8]

Auftrag fortsetzen ist nicht neu entpacken/alles erneut ausführen. Bereits existierender Taskordner allein ist kein laufender Prozess; tatsächliche Start-/Endnachweise prüfen. Keine breiten `pgrep`-Matches auf bloße Promptzeichenketten als Beweis. Bei Nacharbeiten zuerst den konkreten letzten Stand und noch aktive eigene Prozesse feststellen, dann eng weitermachen. Während des laufenden Nachtlaufs keine schreibende Fortsetzung. [E-CX-PREF]


### 18.8 Präzisierte Betriebslehren aus R9A–H

Die späten R9G/R9H-Starter arbeiten nach Nutzerwunsch mit einem Hauptagenten und `xhigh`,
kurzer fortgeschriebener Kontextdatei, gespeicherten Kommando-/Fehlerlogs und knapper Anzeige.
Ultra ist möglich, aber keine Pflicht für jede Nachabnahme; zusätzliche Reviewer nicht automatisch starten.
Ein großes Kumulativdiff gehört in die Lieferdatei, nicht fortlaufend in den Terminal-/Modellkontext.

Arbeitsraumfreigabe, Netz, PID-Sicht, aktuelles NX-Display und GPU sind getrennte Fähigkeiten.
Verkürzte Resumeaufrufe verloren früher Schreib-/Netzfreigaben. Ein Host-Lockhelfer blieb wegen
einer unbeschränkten Sleep-Schleife zurück; die Lösung ist scoped ownership/finally/Shutdown,
nicht Löschen der Lockdatei. GPU-NVIDIA-Abfrage funktionierte auf dem Host, nicht im Codex-Sandbox-/dev.
Daher spätere Host-Supervision für normale GUI-/Builder-/Messaktionen, Agent für lokale Änderungen.

Wiederaufnahme nach Tokenlimit liest kurze Kontext-/Journaldaten und aktuelle Diffs, keine vollständigen
alten Millionentoken-Transkripte. Keine Budget-/Startmarker löschen. Ein fehlender Metadatenpfad
oder ungeprüfter Warmstatus wird nicht wieder als Aufgabe an den Nutzer zurückgegeben, wenn der
normale Resolver/Transport die erlaubte Beschaffung selbst leisten muss. [E-REV5-R9F] [E-REV5-R9G]

<a id="gui-tests"></a>
## 19. Neuer verbindlicher Teststandard: normale GUI statt privatem Erfolgsweg

### 19.1 Vier Abnahmeachsen und die notwendige Ablaufkette

Ein Fix an Config, Profilen, Budget, Workflow oder Ergebnisimport ist erst im für ihn benötigten Umfang abgeschlossen, wenn die **tatsächlich benutzte Installation** dieselben Entscheidungen ausführt wie der Test. [E-CX-R8]

| Achse | Minimaler eigener Nachweis |
|---|---|
| Hauptrepo installiert | Geänderte Dateien/Build-ID und reale Modulimports im normalen Toolbaum; externer Candidate allein reicht nicht. |
| Normale Config aktiviert | Tatsächlich verwendete Registry, Modus, Collector und Budget; notwendige Migration mit Backup/Diff/Idempotenz. |
| Lokal getestet | Fehler vor Fix reproduziert, positive/negative Regressionen, echte kontrollierte Prozessränder, finale Testmenge auf dem letzten Stand. |
| GUI-/Hardware abgenommen | Normales `start_gui.sh` → Profilwahl/Modus → Save/Reload/Summary → Frozen Snapshot → Queue → Runner → Ergebnisse → terminale Anzeige/Cleanup. |

Die GUItests müssen nicht blind jede externe Hardwarekomponente verwenden. Lokale Negativfälle ersetzen die physischen Blätter durch kontrollierte echte Prozesse. **Nicht ersetzt werden dürfen die für den Fehler maßgeblichen GUIvariablen, Resolver, Budgetweitergabe, Queue oder Ergebnisprojektion.** Ein privater XML-/JSONreport mit freihändig passenden Werten ist keine Ausführung dieser Kette.

### 19.2 R8-Matrix: was tatsächlich geprüft wurde

Echte Tk-Variablen/Callbacks/Eventloop, normale Konfiguration und die Übergänge **Standard → Final → Standard**, Energie an/aus, Full/Split, Speichern/erneut Laden, ausdrückliches217/0/2-Override, Warmup0, Frozen1000/100/3. Negative Fälle für veraltete Summary, fehlenden/falschen Collector und persistenten Source-Stopp. Geänderte Summaryquelle vor Start wird nicht still übernommen. [E-CX-R8]

Die separate Tk-Auswahl läuft mit normalem HOME/Xauthority (`--noconftest` im dokumentierten Testkommando). Frühe Skips wegen isoliertem Test-HOME zählen nicht als bestanden. Insgesamt final6/6; die tatsächlichen Knoten und Importpfade stehen im R8-Testbericht. Ein echter GUI-Queue-/CPU-Prozess-/Reporttest ist **negativ**, weil der vorhandene physische Scope ein Accelerator-Setup verlangt; geordneter Fehlerdialog und Artefaktabschluss bestehen, ein erfolgreicher CPU-only-Nativeworkflow wird damit nicht behauptet.

Portable lokale Tests prüfen u.a. tatsächliche Argumente am Spawn, Ketten-/Retryzähler und Source-Stopp über mehrere Zeilen. Prüfen von `max_retries` im YAML allein genügt nicht: nach Stop muss der reale Prozessstartzähler unverändert bleiben. Ein Startbereitschafts-/Versionscheck ersetzt auch keinen Last- oder Energieprozess.

### 19.3 Genau ein positiver kleiner GUI-Smoke in R8

| Feld | Tatsächlicher R8-Umfang |
|---|---|
| Start | `./start_gui.sh` im Hauptrepo; echte Profilwahl und einmaliger Startklick |
| Profil | `profiles/r8_gui_smoke_mobilenet_h8.yaml`, normales kleines Auswahlprofil mit `follow_tool_config:true`; keine private technische Registry |
| Modell/Boundary | MobileNetV3Large, b135 |
| Setup | `orin_nx_hailo8_01` |
| Nativezeilen | H8 Full, setup-lokales TensorRT Full, H8→TRT Split |
| Performance | Je 100 gemessene Frames,10 Warmup,1/1 Wiederholung |
| Quality | Höchstens500 Bilder/500 Bootstrap; vier Auswertungen, zwei außerhalb unveränderter Grenzen |
| Energie | Drei Replikate je Zeile;9/9 gültig,9 tatsächliche Erststarts,0 Fehlversuche/Retry |
| Artefakte | Vier warme Hits; keine MISS/UNKNOWN und kein Compilerdispatch |
| Zeitraum | Startklick20:04:14, Runanlage20:04:53, terminal20:17:15 am 15.09.; ungefähr13 min |
| Ergebnis | Technisch erfolgreich, Quality FAIL getrennt; regulärer Qualitätswarndialog und Artefaktabschluss PASS |
| Nicht enthalten | H10/DeepX-Messquellen, Mehrmodell-/Final-/Langzeitlauf, voller optionale Window-Probe-Coordinator |

Run-ID: `r8_gui_smoke_mobilenet_h8_20260915_200453`, unter dem R8-Ausgabeordner `gui_results/`. Die normalen GUIeinstellungen wurden nach dem Test wiederhergestellt; der Nutzer sieht anschließend wieder CompleteSetDev, nicht automatisch einen neuen gestarteten Lauf. Physische Rohdaten lokal, kleine Nachweise im Debugpack. [E-CX-R8]

### 19.4 Profilvertrag ab Schema 14

| Feld | Standard | Final Quality / Standard+ | Abgrenzung |
|---|---:|---:|---|
| Qualitätsbilder | 500 | 5.000 | Tatsächliches Task-/Datasetbudget und Abkürzungen aus Snapshot lesen. |
| Bootstrapbudget | 500 | 5.000 | Früher zulässiger Point-FAIL/Identitätsnachweis kann tatsächlich weniger Resamples ausführen; kein CI erfinden. |
| Native Frames | 100 | 1.000 | Anzahl pro Performancewiederholung, nicht Gesamtzahl über Backends. |
| Native Warmup | 10 | 100 | Nicht als gemessene Frames zählen. Explizite0 erhalten. |
| Native Performancewiederholungen | 1 | 3 | Bei n=1 kein Wiederholungs-CI aus erfundenen Replikaten. |
| Energie-Replikate | 3 | 3 | Eigenständiger Vertrag, keine Nebenwirkung der Performanceauflösung. |
| Energie-Dauer | Bestehender eigener Vertrag | Bestehender eigener Vertrag | Keine automatische1s→60s-Änderung. |
| Collector/Quellenschutz | Normale verwaltete Bindung | Dieselbe technische Bindung | Nicht nach Qualitypreset zwischen altem/neuem Binary wechseln. |

Die Migration ersetzt nur das bekannte historische Standardtuple1000/100/3. Individuelle Nativewerte und `execution_preset.overrides.native_performance` erhalten, Herkunft anzeigen. Gefrorene Resumes verändern nicht rückwirkend ihre ursprünglichen Messbudgets. Generische Benchmarkbudgets müssen ebenfalls zum ausgewählten Modus passen, sind aber nicht numerisch identisch mit Nativeframes. [E-CX-R8]

### 19.5 Testumfang, Ausgabe und Stopregeln für nächste Änderungen

Für kleine Fehler zuerst lokaler Reproducer/Regression. Bei verändertem GUI-/Configübergang echte Tk-Matrix; bei messungsrelevantem Integrationseingriff ein vorab begrenzter realer GUI-Smoke. Ein Modell/ein Split/ein Setup genügt häufig, beweist aber nur diesen Scope. Kein automatischer Final-/Sieben-Modelllauf als Test und keine neue Hardwareserie nur wegen eines Dokumentupdates.

Standardkonsole: Modell/Setup/Backend, Phase, aktuelle Wiederholung, Frames/Warmup, verstrichene Zeit und kompakte Fehlerursache. Vollkommandos, Base64, große JSONobjekte und umfangreiche Outputs in redigierte Diagnosefiles. Parser behalten die tatsächlichen Outputs; langsame Anzeige darf keine Bytes verlieren. Endliche Ausgabewarteschlange vollständig leeren, offen geerbte Pipes kontrolliert als Fehler beenden. [E-CX-R8]

Jede Änderung **nach** dem realen Smoke eindeutig nennen: welcher finale Sourcepunkt noch lokal geprüft wurde und welche physische Kette vorher lief. Nachlaufend erhöhte Testzahl ist keine rückwirkende Hardwareabnahme. Der aktuelle Nachtlauf kann neue End-to-End-Evidenz liefern; bis zu dessen Prüfung bleibt die Grenze offen. [E-NIGHT-R8-USER]


### 19.6 Iterative gemeinsame Abnahme statt endloser privater Vorprüfungen

Die nächste Kandidatenauswahl muss allgemeine technische Prüfurteile erhalten: verwendbar,
nachweislich ungeeignet, oder aktuell unbekannt/blockiert. Leere Einzelbildausgabe/Quality-FAIL
ist kein Nachrückgrund. Technisch gebunden ungeeignete native Quantisierung ist kein erfundener
Compilefehler. Ein erlaubter Cache-MISS führt zum regulären Build, nicht zum bequemeren späteren Hit.

Tests müssen den wirklichen Erstaufruf einschließen: Controller ohne hailo_platform, kein altes
Qualitybinding, kein Remote-Dateipfad, lokales HEF und konfiguriertes Ziel. Nur äußere SDK-/SSH-
Prozesse ersetzen. Normale temporäre Bereitstellung, vorhandener Reader und Cleanup bilden einen
Pfad, kein neues Framework. Positive GUI-Treiber müssen spawn-sicher sein; negative UNKNOWN-
Vorschau oder forced_cases-Pin dürfen keinen positiven Backfilltest ersetzen.

Nach konkret belegter Korrektur darf innerhalb des ausdrücklich genehmigten Gesamtbudgets ein
Nachtest erfolgen. Keine künstliche neue Einzelrunde für jedes Bindeglied, keine unbeschränkte
Rekursion, keine Wiederholung für bessere Qualität/Streuung. Der aktuelle R9H-Auftrag erlaubt
vier lokale Runden, zwei Smokes und zwei Evals; die dokumentierten Startzähler sind maßgeblich.

<a id="nacht-audit"></a>
## 20. Geplante Nachtauswertung: Technik, Quality, Performance und Energie

**Status: beauftragt für die Ergebnisprüfung nach Ende des laufenden Runs, noch nicht ausgeführt.** Die folgende Prüfreihenfolge ist eine aus dem Nutzerauftrag und den bisherigen Messverträgen abgeleitete Arbeitsanleitung, keine neue numerische Aussage über die laufende Kampagne. Zunächst bestehende Originaldaten verwenden; gezielte Zusatztests erst bei konkreter Lücke. [E-NIGHT-R8-USER]

### 20.1 A – tatsächlichen Umfang und technische Vollständigkeit feststellen

Zuerst Run-ID, Start/Ende, Build-/Sourceidentität, Profilquelle, eingefrorene Parameter, ausgewählte Modelle/Boundaries/Setups, Datensätze, Collectorpfad/-Bytes und Budgetpolicy aus Originaldateien lesen. Nicht aus dem Fenstertitel oder dem Namen „Final“ raten. Relevante Ausgangsstellen: `run_manifest.json`, `profile.yaml`, `profile_start_snapshot.json`, `effective_execution_plan.json`, `hardware_matrix.json`, `evaluation_workflow.log` und die resultierenden Energiepläne/Registry-Snapshots.

Dann je Ebene getrennt bilanzieren: geplante Fälle; belegte Ausschlüsse; nicht gestartete/fehlende Jobs; erfolgreich ausgeführte Wiederholungen; Outputverträge; technisch abgeschlossene zentrale Qualitätsaufträge; gültige Energie-Replikate/volle Zeilen; Cleanup; Artifactclosure. Null, `null`, fehlend, ausgeschlossene Zeile und negativer Qualityentscheid dürfen keine gemeinsame Fehlerzahl ergeben.

**„Workflow technisch sauber“** heißt hier: geplante zulässige Arbeiten laufen kontrolliert, echte Fehler/Negativergebnisse werden richtig berichtet, keine unerklärten Missing-/Import-/Cleanupfehler. Es heißt **nicht**, dass H10-Nulloutputs oder DeepX-Inversionen dadurch korrekte Modellresultate sind. Solche Fälle können den gültigen Vergleichsumfang einschränken, obwohl die Orchestrierung beendet ist. Laufweite positive Behauptung erst mit diesen Achsen und tatsächlich neuem Scope.

### 20.2 B – Output- und Qualitätsbefunde priorisieren

H10-YOLO26m/b398 und YOLO26s/b364 zuerst auf tatsächlich ausgeführte Ausgaben/Verträge prüfen; Bindingresolver bereits repariert, numerischer Output nicht. DeepX Full-YOLO26s auf enthaltene Bild-IDs und die zwei alten geometrischen Fehler prüfen. Weitere Qualitätsabweichungen nach Full-Floatreferenz **und** passender Full-Backendumsetzung strukturieren. Keine neue NMS-/Threshold-/Compilerwahl aufgrund besserer Werte im selben Evaluationsset.

PASS/FAIL/INCONCLUSIVE nach unverändertem Vertrag erhalten. Wiederholte 500er- und 5000er-Ergebnisse nicht als identische Population vergleichen. Eine reguläre Accuracyabweichung ist nicht automatisch ein Codefehler; eine falsch gebundene Referenz, fehlende Auswertung oder ungültige Detectionausgabe ist nicht nur „schlechte Quality“. Die Nutzerpriorität verschiebt sich nach stabiler Ausführung zu gezielter Aufklärung, nicht zu einem offenen Tuningauftrag. [E-CX-PREF] [E-NIGHT-R8-USER]

### 20.3 C – historischer Paperanker um97 FPS, nur bei passendem Vertrag

Die beigefügte Ausgangs-KB dokumentiert für den exakten historischen **Hailo8→TensorRT-Pfad `yolov7_paper/b066`** ungefähr **97,077 P2-FPS** und **97,059 Completed-Detection-FPS**. Das ist ein historischer Projektanker; dessen Rohbeleg/Paperversion wurde in diesem KB-Update nicht zusätzlich neu untersucht. Die beiden Raten nicht als dieselbe Metrik ausgeben. [E-KB-REV3-INPUT, §2]

Vor einem Zahlenvergleich eine Zuordnungstabelle erstellen:

| Vergleichsfeld | Erforderlicher Abgleich |
|---|---|
| Modell | `yolov7_paper`, Originalgraph/Weights, Eingabeform/-auflösung, Preprocessing und Datenvertrag |
| Split | b066 muss demselben Graphschnitt/Boundarytensor entsprechen; ähnliche Nummer oder b044 ist kein Match |
| Hardware | Hailo8 und passendes Orin-NX-System; Power-/Clock-/TPC-/Temperatur-/Lastzustand dokumentieren |
| Artefakte | HEF, P2-Engine, Recipe/Precision, Tensorlayout/QuantInfo und echte ausgeführte Identitäten |
| Pipeline | P1/P2/CPU-Nachverarbeitung, FIFO-/Queue-/Inflightwerte, Überlappung/Batchgröße und Work Units |
| Endpunkt | Raw head, pre-NMS, P2-Ausgang oder wirklich Completed Detection; NMS/Decode/Transfers im gleichen Timingvertrag |
| Statistik | Warmup, Zahl gemessener Frames, Wiederholungen, Start/Endmarker und Aggregationsregel |

**b066 nicht ausgewählt:** Der Nachtlauf hat den direkten97-FPS-Vergleich nicht geprüft. Vorhandene passende historische Daten verwenden oder später separat einen kleinen, ausdrücklich genehmigten Vergleich mit vorhandenen Artefakten ansetzen. Nicht während des laufenden Runs die Boundary umstellen und nicht nachträglich nur die beste Boundary in der Hauptauswertung berichten.

**b066 passend ausgewählt:** P2- und Completionrate jeweils separat vergleichen, absolute/relative Abweichung angeben und Differenzen erst mit Endpoint-/Pipeline-/Powerdaten erklären. Keine erfundene pauschale ±10%-Freigabe. Nicht auf97 FPS hinoptimieren oder eine andere Nachverarbeitung aus dem Messfenster entfernen, nur um den Referenzwert zu treffen.

### 20.4 D – übrige Performancewerte prüfen

Für jede betrachtete Replikation zunächst Arbeitsendpunkt und gemessene Work Units N sowie Zeit T identifizieren. Rein rechnerischer Check bei passender Einheit:

```text
Throughput [Frames/s] = tatsächlich abgeschlossene Frames / gemessene Sekunden
```

Gemeldete FPS gegen Originalzählung und Zeit prüfen, Warmup nicht im N, Sekunden/Millisekunden nicht vermischen. Eine ganze Full-Gruppe ist kein Einzelmodell: im R7-Run dauerte H8+TRT-Full26:23 min für sieben Modelle ×zwei Backends ×drei Replikate, insgesamt42.000 gemessene Frames plus4.200 Warmup. Die Anzeige von1440 s waren24 min, keine Stunde und keine einzelne GPUoperation. [E-R7-RUN]

Für YOLOv7 Full-TRT nannte der R7-Nachweis `prepared_input_h2d_engine_d2h_sync_decode_class_aware_nms`:1.000 Frames / 65,70 s ≈ 15,22 FPS. Das ist ein anderer Messumfang als der b066-P2-/Pipelined-Referenzwert. Diese Zahl ist ein historischer Diagnoseanker, keine neue aktuelle Performanceabnahme. GPUkernelzeit, H2D/D2H, Synchronisation, Decode und NMS getrennt, soweit vorhandene Zeitmarken es erlauben. Fehlende Unterzeit nicht schätzen und als Messung ausgeben. [E-R7-RUN]

Weitere Konsistenzprüfungen: Ausreißer und Streuung pro Replikation, Reihenfolgeeffekte/Erwärmung, parallele Jobs, Throttling/Clocks; Full versus Split auf demselben Setup; gleiche Referenzrollen auf unterschiedlichen Setups; tatsächlich verwendetes Cacheartefakt und Kalt-/Warmstart; Datentyp/Layout/Batch/Inflight; Fast-/Oraclearbeit innerhalb bzw. außerhalb der Messung. Bei einer Pipeline ist die langsamste Stage ein idealisierter Flaschenhals **unter vergleichbaren Work Units und stationären Bedingungen**; echte Makespan/Backpressure/Anlauf-/Auslaufkosten können abweichen. Kein automatischer Defekt aus grob unterschiedlichen Stagezahlen.

Inverse FPS sind nicht generell Einzelanfragelatenz, besonders bei Überlappung. Keine Addition von FPS; keine Gleichsetzung TensorRT-`trtexec`-Enginebenchmark mit vollständiger Anwendung. Für n=1 nur deskriptiv, kein erfundenes Replikat-CI. Hohe FPS bei leeren/ungültigen Outputs sind eine existierende Zeitbeobachtung, aber kein gleichwertiger erfolgreicher Task-Speedup.

### 20.5 E – Energie- und Leistungswerte plausibilisieren

Je Ergebniszeile und tatsächlich ausgewählter logischer Wiederholung prüfen:

1. **Messkette/Skalierung:** richtiger u.RECS-Kanal und FS-Messpunkt; gebundene Gain-/Kalibrationsdatei; unskalierte/korrigierte Größen getrennt; keine doppelte Skalierung. Vorhandene historische Gain-/Gatefrage aus §6.4 nur anhand ihres Originalbelegs klären, nicht blind neu kalibrieren.
2. **Trace/Transport:** First Sample, kontinuierliche Counter/Rate, erkannte Samplelücken, Endpaket/Source-close und tatsächliche Dauer. Collector-rc0 allein reicht nicht. Empfangsdiagnostik ist ein Beleg, keine Garantie bei fehlenden Rohtraces.
3. **Fenster:** Commandmarker und vollständige Abdeckung; Collector-Vorlauf/-Nachlauf/Drain nicht als Inferenzenergie einrechnen. Das konfigurierte1-s-Lastsoll, tatsächliches Commandfenster und ungefähr27-s-Aufnahme sind drei verschiedene Zeiten.
4. **Work Units:** tatsächlich beobachtetes N dieser Energieausführung, gleicher Endpunkt wie der beanspruchte Performancevergleich. Keine Hochrechnung aus früheren FPS oder Übernahme der1.000 Performanceframes, wenn die Energieausführung16 Frames erledigte.
5. **Replikatauswahl:** Sollreplikate, einzelne Retries, ausgewählter gültiger Versuch und volle3/3-Zeile; Quelle persistent gesperrt/NOT_RUN getrennt. Kein Zusammenfügen fremder Modelle, Runs oder Konfigurationen zu einer Dreierserie.
6. **Einheiten/Rechnung:** Joule, Watt und Sekunden; Wh nur mit korrekter3.600-Umrechnung; Mittelwert/Integral über dasselbe Fenster. Nichtfinite oder negative rohe Gesamtenergie, unpassende Counts und identische verdächtige Werte über fremde Fälle gezielt prüfen.
7. **Fairness:** FS primär ungekürzt; M.2-Idleabzug nur in dafür gebundener separater Normalisierung, nicht vom Primärergebnis oder nochmals von bereits normalisierten Zahlen abziehen. Power-/Clock-/Thermalzustände und Referenzsetup beachten.

Rechenidentitäten **nur für dasselbe Fenster und dieselben Work Units**:

```text
E_total [J] ≈ Integral P(t) dt über das freigegebene Fenster
P_mean [W] = E_total / T
E_per_frame [J/Frame] = E_total / N
Frames_per_joule = N / E_total
E_per_frame = P_mean / (N/T)
```

Die letzte Gleichheit verbindet die **Energieausführung** mit deren eigener Rate, nicht automatisch mit den separat gemessenen Native-Hotloop-FPS. Bei kurzen Commands können Initialisierung/Transfers/Prozessaufwand einen großen Anteil ausmachen; das ist zuerst ein Unterschied der Messgrenze, nicht zwingend ein Rechenfehler. Ob eine längere Last für einen wissenschaftlichen Claim nötig ist, folgt aus Vertrag/Unsicherheit, nicht dem Etikett „Final Quality“.

Scope des späteren Berichts: technische Aufnahmegültigkeit, numerische Plausibilität, Vergleichbarkeit und Claimfreigabe einzeln. Fehlen Roh-Parquets, zunächst nur gespeicherte Postprocessing-/Markerbelege geprüft nennen; eine unabhängige Neuintegration bleibt NOT_RUN. Grenzwerte aus existierender Policy verwenden, keine universellen Hardware-Wattgrenzen erfinden.

### 20.6 Ergebnisformat und Entscheidung nach der Auswertung

Eine gemeinsame Falltabelle pro Modell/Boundary/Setup/Backend/Precision/Endpoint mit getrennten Spalten für Runtime, Outputvertrag, Quality, Wiederholungen/FPS, Energie-Replikate/J/W/J-pro-Frame, Cleanup, Artefaktbindung und Vergleichseignung. Technisch gültige Fälle nicht wegen eines fremden Fehlers unsichtbar machen; negative Werte nicht beschönigen.

Abschließend §12 mit **belegt abgeschlossen**, **offen wegen genauer Evidenzlücke**, **gezielter Reparaturverdacht** oder **korrektes negatives Ergebnis** fortschreiben. Bei Auffälligkeit zuerst vorhandene Logs/Outputs prüfen; nur den kleinsten benötigten Zusatztest formulieren. Kein großer Neulauf allein zur Beruhigung und keine Änderung des gerade laufenden Quellenbestands. [E-NIGHT-R8-USER]

<a id="r9fortschritt"></a>
## 21. Historische Fortschreibung R9A–H und damalige Mess-/Aussagegrenzen

**Datierter Stand vom 19.09.2026.** Die aktuelle THESIS20-Bilanz steht in §22;
diese historischen Scopegrenzen werden weder gelöscht noch als aktueller Neustartauftrag verwendet.

### 21.1 Entwicklungsfolge – unterschiedliche Belege nicht zusammenzählen

| Runde | Erreicht | Grenze |
|---|---|---|
| R9A/Nachabnahme | Backendnachrücken und FPS-Endpunkte; lokale Fehler am Cachezähler, Build-ID und Testimport behoben | GUIabnahme zunächst durch Bedienhelfer/Lock/Display blockiert; nicht rückwirkend PASS |
| R9B/Restabnahme | Gepaarte Requestlatenzen; H8-Wrapper real gebaut, DeepX Part1/P2-Verträge geprüft, H8b021 wirklich ausgeführt | Klassifikation zunächst Hostoutput ohne Top-k; ursprüngliche Zwischenversuche bleiben unvollständig |
| R9C/H10-Nachtest | Klassifikation wirklich bis Top-1/Top-5; TRT Full im vorhandenen Prepared-Input-Hotloop; H10Capturefix anschließend real geprüft | Letzter H10-Smoke3/3 / 300 Paare, keine neue Vollqualitäts-/Energiemessung; ursprüngliche R9C-Matrix bleibt8/9 |
| R9D/Hostbuild | Lokaler DFC-Präzisionsvertrag; Hostoptimierung quantisierten HAR gespeichert | Sandbox hatte keine GPU; anschließender Hostversuch durch Gesamtfrist vor HEF abgeschnitten |
| R9E | Einmal Compile-only aus quantisiertem HAR; allgemeine HAR-/Phasen-/Timeoutfixes lokal geprüft | Compile-only89,57 s/Exit2: auto_spatial_reshape_from_activation3_to_concat23, Agent infeasible. Kein HEF, kein GUI-Output-PASS |
| R9F/Readertransport | Allgemeine Output-Eignung, Metadatenbeschaffung einschließlich temporärem HEF-Transfer und Auswahlplan-Vereinigung |805 fokussierte Tests; zwei HEFs wirklich remote gelesen; komplette GUI-/Enginekette noch offen bis R9G |
| R9G | Gemeinsame iterative Host-GUIrunde; letzter Eval63/63 Native,189/189 Energie,6.300Paare; Ersatzgrenzen real | Restfehler in Energie-Taskgleichheit/Inputs/Projektion erst durch vollständigen Nachtrag sichtbar |
| R9H | Restfixauftrag mit7 Modellen / 3 Splits; zweiter Run06:43:23–07:19:10 im verfügbaren Log in Arbeit |Keine finale lokale Rundenlieferung oder abschließenden Einzelbelege übergeben; Ziele nicht als Ergebnis ausgeben |

### 21.2 R9G ist die bestätigte gemeinsame Ausgangsbasis – mit Grenzen

Run `r9g_eval_20260918_171131`, Standard 500 Bilder/500 Bootstrap und Native 100/10/1.
Alle 42 Full- und 21 Splitzeilen sind technisch abgeschlossen und besitzen je 100 echte Requestpaare.
Mean/P50/P95 wurden aus 6.300 Paaren nachgerechnet. Die 77 zentralen Qualityresultate umfassen
56 primäre Fälle plus 21 setup-lokale TRT-Full-Referenzvergleiche.40 PASS / 25 FAIL / 12 INCONCLUSIVE sind
keine neuen unabhängigen Runtimefehler. [E-REV5-R9G-AUDIT]

Nachrücken liefert für H8/H10 s/b021 und m/b038, während DeepX bei b364/b398 bleibt. Die alten
H10-Ausgaben sind weiterhin ungeeignet. Ein Ersatzlauf misst eine andere Boundary; technische
Verwendbarkeit und gemessene AP-Verluste bleiben getrennt. R9G-H10s/b021: 170,17 Completed-Task-FPS,
65,29 ms mittlere Bildlatenz,40,10 AP / INCONCLUSIVE; H10m/b038: 104,43 FPS,105,85 ms,43,69 AP / FAIL.
Eine Performancewiederholung ist keine Speedup-Konfidenzfreigabe. [E-REV5-R9G-AUDIT]

### 21.3 Messgrenzen und Energiearithmetik

Pipeline-FPS ist der Durchsatz abgeschlossener Tasks, P2-FPS ist die Zwischenstufen-Ausgaberate.
Bildlatenz ist die Zeit desselben Requests ab vorbereitetem Tensor vor Admission bis zum
geforderten Taskabschluss (Detection einschließlich erforderlichem Decode/NMS, Classification Top-k).
Warteschlangen/Transfers innerhalb dieses Fensters sind enthalten, vorgelagertes JPEG-/Kameraladen
nicht. Niemals 1000/FPS als Ersatz für echte Requestpaare verwenden oder alte Hostoutputzeiten
nachträglich zu Top-k-Latenzen machen. [E-REV5-R9C]

189/189 R9G-Energieaufnahmen sind anhand gespeicherter Einzelarithmetik, Kalibrierfaktoren,
Fenster-/Markerbindungen, exakten Work Units und Empfangsprotokollen geprüft. Keine Roh-Parquet-
Reintegration. Beobachtete Leistung 14,57–21,25W, Commanddauer 2,21–4,38s, CV J/Work 0,21–4,21%.
Streuung dokumentieren, nicht zu einer neuen Messpflicht aufblasen; Scheduling nur als mögliche
Einflussgröße, nicht als bewiesene Ursache behaupten. [E-REV5-R9G-AUDIT]

J/Work Unit stammt jeweils aus E_i/N_i derselben Aufnahme. Die berichtete mittlere Effizienz kann
als 1/Mittelwert(E_i/N_i) definiert sein; sie ist weder automatisch Mittelwert(N_i/E_i) noch ein
Quotient aus separaten Performance-FPS und Leistung. Auch Mittelwert(P_i) und Summe(E_i)/Summe(T_i)
haben unterschiedliche Gewichte. Prüfungen müssen die tatsächlich deklarierte Aggregation und
Replikatbasis respektieren, nicht Toleranzen erhöhen, bis eine falsche Identität passt.

Die kurzen Commandfenster bleiben Screening und keine stationäre Dauerbetriebsenergie. Auch
26 Nativezeilen mit Quality-PASS bleiben unter bestehender Screeningpolicy nicht wissenschaftlich
qualifiziert; `energy_quality_qualified=0` ist deshalb nicht vollständig ein Defekt.35/42 Vergleiche
überschreiten die bestehende Dauertoleranz; das ist eine Vergleichsgrenze, kein Anlass für Gate-Lockerung.

### 21.4 Warum R9H noch benötigt wird

R9G hat 27 TRT-Full-Klassifikations-Energieaufnahmen mit trtexec statt dem neuen Top-k-Task;
sieben DeepX Full/Split-Inputpaare unterscheiden sich; zwölf Detectionprojektionen verlieren
Vergleichsendpunkte;20/21 TRT-Full-Normalisierungen werden trotz konsistenter Einzelreplikate
abgelehnt;21 Splitrows tragen gültige Authority und zugleich den alten Missingfehler.
Die Genericmatrix hat56 Runtime-erfolgreiche Rows, aber36 contract_fail_or_unavailable,
14 numerical_similarity_failed und6 screening_only. Diese Achsen nicht additiv als Runtimefehler zählen.
R9H soll genau diese produktiven Dispatch-/Projektionsstellen korrigieren und mit drei Splits prüfen.
Die endgültige Sourceursache der Aggregationsabweichung und die Erfüllung aller Fixziele bleiben
bis zur R9H-Lieferung offen. [E-REV5-R9G-FINDINGS] [E-REV5-R9H-PLAN]

### 21.5 Snapshot R9H am 19.09.2026

`eval_02/r9h_eval_20260919_064323` startet 06:43:23 und das vorliegende Log endet 07:19:10.
Drei echte Kandidaten je Modell sind in Vorbereitung/Ausführung, nicht nur Shortlistlabel:
MobileNet[27,56,135], ResNet[2,60,119], YOLO11l[62,64,65], YOLO26m[38,398,399] plus[40,41],
YOLO26s[21,364,365] plus[23,24], RegNet[23,52,132], YOLOv7[9,11,44]. Bei YOLO26 ist
accepted=5 die modellweite Vereinigung verschiedener Backendfälle, noch kein Beweis fünf
Splits je Backend. Finale Zuteilung und Pflichtnenner erst aus der Schlussmatrix entnehmen.

Alle sieben Benchmarksets/der gemeinsame Cachepreflight sind im Ausschnitt abgeschlossen;
MobileNet/ResNet/YOLO11l haben jeweils drei Remotegruppen beendet. YOLO26m startet gerade.
Native- und Energieabschluss des zweiten Versuchs sind nicht enthalten. TRT-Preflight führt
auch not_found/source_onnx_mismatch/evicted_by_retention; dazu keine aktuelle Cachelöschung oder
pauschale Reusefreigabe ableiten. Das separate host.log zeigt den ersten Versuch bis Finalisierung;
Grund einer Korrektur zwischen beiden ist hier unbekannt. [E-REV5-R9H-LOG]

### 21.6 Evidence- und Freigabeabschluss

Jetzt abgeschlossene Belege selektiv sichern, nicht komplette alte Lieferbündel duplizieren.
Rohmodelle, HEFs, DXNNs, TRT-Engines, Arrays, Rohtraces und private Profile bleiben im lokalen Archiv.
Negative Compiler-/Outputbelege bleiben ausdrücklich diagnostic. Bereinigte öffentliche Kopien
benennen die Originalquelle und Redaktionen; eine Dokumentrevision ist kein neuer Hardware-PASS.
Nach R9H-Abschluss kommen dessen kurze Bilanz, aktive Eingabeverträge, tatsächliche Workloads,
Energie- und Latenzreplikate, finaler Source-/Test-/Installedstand und gegengeprüfte Restgrenzen dazu.
Kein `final`-/Release-Tag allein aufgrund eines laufenden Standard-Integrationslogs. [E-REV5-GIT]

<a id="thesis20-audit"></a>
## 22. Historischer THESIS20-Audit vom 02.10.2026

**Stichtag 02.10.2026.** Dieser Abschnitt schreibt den früheren R9G/R9H-Stand für die
aktuelle THESIS20-Kampagne fort, ohne alte Versuche rückwirkend als bestanden auszugeben.
Grundlage ist der abgeschlossene Audit des gelieferten 101-Dateien-Archivs
`THESIS20_FINAL_AUDIT_20261002_093035.tar.gz`. Die Zahlen sind Auditbefunde aus vorhandenen
Resultaten, keine im Knowledgebase-Update neu erzeugten Messungen. [E-TH20-AUDIT]

### 22.1 Auswahl, tatsächliche Erhebung und produktive Vervollständigung

Run: `thesis_20splits_n5000_b1000_20260925_20260925_103745` unter
`~/Models/EvaluationRuns/`. Ursprünglicher Start 25.09.2026 10:37:45 +02:00 mit 2.91.0;
selektive Vervollständigung mit lokal installiertem 2.91.1/2.91.2 und dokumentierten
Nachbesserungen. Die Run-ID und die ursprüngliche ausgewählte Untersuchungsmenge blieben
maßgeblich. N5000 bedeutet 5.000 Validierungsbilder, B1000 hier 1.000 Bootstrapziehungen;
das ist nicht der unabhängige Accelerator-Kalibrierumfang B500. [E-TH20-2910]
[E-TH20-2911] [E-TH20-2912]

| Modell | Ausgewählte Genericgrenzen | Unterstützte Native-Splits je Setup | Qualityresultate | `accuracy_loss` |
|---|---:|---:|---:|---:|
| MobileNetV3 | 20 | 17 | 87 | 22 |
| ResNet50 | 20 | 19 | 87 | 0 |
| RegNet-X 1.6GF | 20 | 20 | 87 | 0 |
| YOLO11l | 20 | 2 | 66 | 1 |
| YOLO26m | 20 | 3 | 65 | 5 |
| YOLO26s | 20 | 2 | 69 | 7 |
| YOLOv7 Paper | 20 | 1 | 87 | 4 |
| **Summe** | **140** | **64** | **548** | **39** |

64 unterstützte Splitgrenzen × 3 Setups = 192 Native-Splitfälle. Dazu kommen 42 Fulls
(je sieben Vendor Full und TensorRT Full auf drei Setups): insgesamt 234 erfolgreiche
Performancefälle mit 702 Wiederholungen. Die übrigen 228 Nativeplanzeilen sind Multi-Input
und `not_supported`. Diese Teilmenge ist nicht durch eine Nativequote aufgefüllt worden.
Generic, Quality, Native und Energie haben unterschiedliche Zählebenen; ihre Counts nicht addieren.

Die Original-Genericmatrix ist vollständig erklärt: 527 vorhandene Zeilen, 37 negative
Buildbefunde, 24 statische Hailo-Part1-Policyausschlüsse. Letztere betreffen auf H8/H10
YOLO26m b290/b303/b325/b340/b373/b393 und YOLO26s b256/b284/b291/b308/b345/b360.
Policyausschluss ist kein neu gemessener Compiler-Reject; Part2-only ist kein erfolgreicher
Composed-Fall. Kein aktueller Auftrag, diese Grenzen freizuschalten oder zu ersetzen.

Die echten produktiven Ergänzungen haben die zuvor fehlenden YOLO26-Genericdaten, lokalen
Qualityrequests und zwölf letzten Nativefälle geschlossen. Die Energie lief vom ersten
`ROW_START` am 01.10. 10:15:50 bis zur letzten Zeile am 02.10. 03:49:23; der Helper endete
03:49:31 mit `rc=0`. Anschließend Reporterstellung/Inventarisierung und Finalisierung bis
05:34:24. Der Audit bestätigt 234 vollständige Energieaggregate, nicht nur 234 geplante Zeilen.
[E-TH20-ENERGY-END] [E-TH20-AUDIT]

### 22.2 Behobene Ablaufprobleme – nicht erneut zu pauschalen Messaufträgen machen

Die Liefer-/Startberichte dokumentieren folgende eng begrenzte Reparaturen; die spätere
produktive Vervollständigung belegt den tatsächlich erreichten Ablauf, nicht die globale
Fehlerfreiheit jeder möglichen Konfiguration:

| Problem | Dokumentierter Reparatur-/Folgenachweis |
|---|---|
| YOLO26-Part1-Quellenmehrdeutigkeit | Reguläre ONNX-Quelle gemäß Manifest statt Konkurrenz mit `part1_hailo_identity`; beide Modellblöcke danach real ausgeführt |
| Native-Subset/Validator/Energieprovenienz | Tatsächliche Part2-Eingänge durchgereicht; Multi-Input nicht unterstützt; Validatorabschluss statt 600-s-Abbruch; vorhandene Quellenfelder konsistent weitergegeben |
| Eigene Preflight-/Generate-Aliasänderungen blockieren Reentry | Ursprüngliche Bindungen und belegte Writeroutputs getrennt geprüft; Reuseentscheidungen attemptlokal statt Überschreiben alter Entscheidungsbelege |
| Langsamer Reuse | Redundantes Durchlaufen sämtlicher 257.313 Indexpfade je übersprungener Stufe beseitigt; im Folgelog Wiederverwendung in Sekunden statt rund 95–100 s pro Übergang |
| YOLO26s-Referenz wechselt beim Harnessrefresh | Refresh vor Schedule; gespeicherte Originalreferenz kontrolliert wiederhergestellt, ohne Geräteinferenz auf Verdacht; alle 548 Qualityrequests abgeschlossen |
| Native Full verwechselt Attempt und Kampagne | Logische Run-ID und physischer Attemptpfad getrennt; sechs zuvor fehlende TRT-Full-Performances später real abgeschlossen |
| Vendor-Full-Nachbindung ausgelassen | Metadatenarbeit auch bei bereits fertiger Performance; negative Semantik bleibt negativ |
| Unvollständige Energie-Restagerollen | Tatsächlich benötigte Originaldateien wiederbereitgestellt; zweimal 222/222 Artefakt-only-Prüfung, zweiter Eintritt ohne Transfer; später 638 Bindungen/234 Attestierungen bestanden |
| Ungestartete Previous Results blockieren aktuellen Energieplan | Alter Nullstart vollständig belegt; aktuelle Commands weiterhin strikt geprüft; produktive Energieaufnahme danach gestartet und abgeschlossen |

Diese Scopebelege ersetzen keine noch offenen **Auswertungsbefunde F01–F06**. Insbesondere
„vorhandene Messungen wiederverwendet“ garantiert nicht, dass sämtliche abgeleiteten Labels,
Authorityzustände oder Claimtabellen bereits richtig sind. [E-TH20-2911]
[E-TH20-2911-REENTRY] [E-TH20-2912] [E-TH20-GENERATE-REENTRY]
[E-TH20-ENERGY-REENTRY]

### 22.3 Energie- und Performanceplausibilität des gelieferten Bestands

Alle 234 Energiezeilen enthalten je drei gültige Replikate; 705 physische Collectorversuche
entsprechen 702 gültigen logischen Replikaten plus drei verworfenen ungültigen Vorversuchen.
Betroffen: RegNet/DeepX/b001 (Replikat 2, nullbasiert), MobileNet/H10/b068 (Replikat 0) und
YOLO26s/TRT Full auf DeepX-Setup (Replikat 0). Gültige Ersatzversuche erhalten; kein Best-of
und keine erneute Aufnahme dieser bereits vollständigen Zeilen.

Für alle 702 ausgewählten Replikate stimmen die gespeicherten Beziehungen `P=E/T_aktiv`,
`E_pro_WorkUnit=E/N`, `WorkUnits_pro_Joule=N/E` und die einmalige Kalibrierfaktoranwendung.
Auch die Aggregate entsprechen ihren Replikaten. Dokumentierte Completioncounts,
Commandfenster, Quellenabschlüsse und Traceprüfungen sind konsistent; ausgewählte gültige
Replikate melden null verlorene Samples. Unterschiedliche protokollierte Tracebindungen
und nicht überlappende gespeicherte Workloadfenster sind geprüft, nicht die Rohtraces neu gehasht.

| Größe | Befund aus gespeicherten Resultaten |
|---|---|
| Mittlere Full-System-Leistung je Zeile | 14,41–32,69 W |
| Mittlere Energie je Zeile | 890,62–2.056,37 J |
| Mittlere Energie je abgeschlossenem Work Unit | 0,01559–2,25588 J |
| Tatsächliches aktives Commandfenster | Im Mittel etwa 61,41–63,54 s; nicht pauschal durch das Lastsoll 60 s teilen |
| Nativeaggregation | Alle 234 veröffentlichten `fps_makespan` sind exakt der Median ihrer drei Wiederholungen; 702 verschiedene Runtime-Instanz-IDs |
| Native-FPS-CV | Median etwa 0,41 %, Maximum 8,54 % |
| Energieintegral-CV | Median etwa 0,17 %, Maximum 2,01 % |
| Joule/Work-Unit-CV | Median etwa 0,26 %, Maximum 7,49 % |

Primärgröße bleibt **kalibrierte FS-Eingangsenergie ohne Idleabzug**. Die separate
Idlenormalisierung der 21 TRT-Full-Baselines nicht nochmals abziehen oder mit Primärwerten
vermischen. Energieeffizienz verwendet `N/T` des Energiecommands, nicht automatisch die
separat gemessenen Native-Hotloop-FPS.

**Prüfgrenze:** Keine Roh-Parquet-Neuintegration, Neukalibrierung, erneute AP-Berechnung
oder unabhängige Kontrolle der physischen Messverdrahtung. Rohtraces, Kalibrierungsrohdaten,
vollständige Tensorarrays/Predictioncorpora, alle ursprünglichen Generic-Per-Case-Berichte
und der endgültig installierte Produktquellstand sind im kleinen Auditarchiv nicht vollständig
enthalten. Interne Konsistenz ist kein neuer absoluter metrologischer Genauigkeitsnachweis.
[E-TH20-AUDIT]

### 22.4 Auswertungsfehler und Vergleichsgrenzen, nicht bereits repariert

**F01:** 47 H10-Primärqualityresultate werden in `task_quality_reference_comparison.csv`
als TensorRT gelabelt. Beispiel MobileNet/b119: tatsächliches H10 Top-1 58,44 %, tatsächlicher
Generic-TRT-Fall auf dem DeepX-Setup 73,70 %. Primärquelle/Request/Setup erhalten und nur die
Projektion korrigieren. Die 21 echten TRT-Full-Companions sind keine falschen H10-Labels.

**F02:** 186 unterstützte Native-Splits mit portablem Authority-Run-ID-Mismatch trotz
übereinstimmender sichtbarer IDs und aktuell gültiger Authority. Historisch bleibt
`native_stage_workflow_version_mismatch` gespeichert. Das ist ein widersprüchlicher
veröffentlichter Zustand, **noch keine abschließend lokalisierte Writerursache**. Reguläre
Bindungsprüfung anhand der Originale; keine 186 Neumessungen und keine manuell positiven Flags.

**F03:** Sechs TRT-Fulls YOLO26m/s × 3 Setups besitzen vollständige Performance und exakt
zugeordnete zentrale `reference_close`-Quality, aber lokale Numerik `unavailable` wegen
`numerical_similarity_metric_missing`. Vorhandene Outputs lokal auswerten. Zwei Vendor-Fulls
YOLO26s/H8/H10 bleiben davon getrennt semantisch negativ und `accuracy_loss`.

**F04:** 192 Generic↔Native-Paare bestehen den Prüfpunkt `generic_completed_task_measured`
nicht. Bei 499 Generic-Splitbeobachtungen zeigt die Projektion Rohendpunkte
`classification_logits`/`p2_output`, nicht belegte vollständige Taskzeiten. Ob die benötigten
Completionzeiten in ursprünglichen Per-Case-Berichten vorhanden sind, bleibt zu prüfen.
„Generic-Proxy sagt Native-Komplettdurchsatz vorher“ und „Native ist bei identischem Endpunkt
X-mal schneller“ sind unterschiedliche Aussagen. Fehlende Taskzeit nicht aus Stageproxies erfinden.
Ranking auf der ausgewählten 20er-Matrix von globalem Graphoptimum trennen; etwa 133 deklarierte
RegNetgrenzen sind kein spontaner Auftrag für 113 neue Messungen. Eine Nativegrenze bei YOLOv7
beziehungsweise zwei bei YOLO11l/YOLO26s begrenzen Rangkorrelation unabhängig vom Reporterfix.

**F05:** 234 echte Energiebeobachtungen sind vorhanden, aber 384 Split↔Full-Paare haben keine
ausgefüllten Energiequoten. `energy_results.csv` und `claim_eligible_energy.csv` projizieren
527 Genericzeilen ohne Energiewerte; „Energy eligible: 527“ ist deshalb irreführend. Alle
234 Originalenergiezeilen tragen `screening_only=true`, `diagnostic_only=true`,
`claim_eligible=false`; effektive Genericrolle `development`, Native-Energierolle teils `unknown`.
Technische Messgültigkeit, diagnostische Paarbarkeit, Semantik und wissenschaftliche Freigabe
getrennt ausgeben; keine rückwirkende Final-/Hold-out-Umdeklaration. Acht DeepX-Detection-
Split/Vendor-Full-Paare haben abweichende Decoder-/NMS-Vertragskennungen: Vertragsinhalte
prüfen, weder Gleichheit noch Fehler allein aus Kennungen ableiten.

**F06:** Die 61 ausgeschlossenen Genericfälle werden weiter als fehlende Pflichtquality
gezählt. Nur 32 sind terminal, 29 noch `materialized_not_terminal` (17 Build/12 Policy).
527 vorhandene Matrixeinträge tragen abgeleitet `quality_decision=not_evaluated` trotz
vorhandener Einzelentscheidungen. Korrekte Terminal-/Qualityprojektion statt Nachmessjobs.
**Daher ist die alte Kurzdeutung „partial nur wegen 228 unsupported“ ausdrücklich unvollständig.**
Es bestehen weitere Bindungs-, Semantik-, Rollen-, Scope- und Projektionsgrenzen.
[E-TH20-AUDIT] [E-TH20-FOLLOWUP]

### 22.5 Negative Resultate, Beobachtungsliste und Entscheidung über Zusatzmessung

39 `accuracy_loss` sind abgeschlossene negative Resultate, keine technischen Fehler. Die
aktuellen Detection-AP50:95-Werte sind endlich (etwa 0,3233–0,4668); kein neuer AP=0-/Nulloutput-
Zusammenbruch im auditierten aktuellen Bestand. Größere Hailo-Verluste, etwa MobileNet Full
CPU 73,70 % / H8 60,62 % / H10 59,42 % Top-1, nicht durch Tuning oder neue Margen verschönern.

W01: MobileNet/DeepX/b043 Top-1 66,60 % gegenüber benachbarten b039 72,30 % und b056 72,28 %.
Der auffälligere lokale Einbruch begründet zunächst Quellen-/Input-/Quantisierungsprüfung,
keinen nachgewiesenen Produktfehler. Diese Multi-Input-Grenze hat bewusst keinen Nativezwilling.

W02: Native-Streuungsfälle ResNet/H10 b067/b081, MobileNet/H10 b027/b039,
YOLOv7/DeepX b009. W03: Energieeffizienzstreuung YOLOv7/TRT Full auf DeepX- und H8-Setup
sowie YOLOv7/DeepX Full. Teilweise variiert vor allem die abgeschlossene Arbeitsmenge,
nicht das Energieintegral. Vorhandene Timing-/Clock-/Thermal-/Warmupbelege zuerst lesen;
5 % CV ist nur ein Sichtungsfilter, kein neuer Ausschlusswert. Schlechtere Wiederholungen erhalten.

**Nächster Schritt:** §12 lokal bearbeiten. Danach je Befund ausweisen: lokal behoben,
gültiges negatives Ergebnis, methodische Grenze oder exakt benötigte Zusatzmessung.
Aktuell keine physische Messung eindeutig als verdorben nachgewiesen; kein vollständiger
Neulauf gerechtfertigt. Bedingte Generic-Completion-/Outputdiagnosen sind keine automatisch
freigegebene neue Kampagne. [E-TH20-AUDIT] [E-TH20-FOLLOWUP]

<a id="thesis20-final"></a>
## 23. Gemeinsame Auswertung und Veröffentlichung am 04.10.2026

### 23.1 Vier Quellenbereiche und drei Evidenzebenen

Die korrigierte ursprüngliche Hauptauswertung, 192er-Completion, zwölf YOLO-Zusatzfälle
und augmentierte Vereinigung bleiben eigene Ansichten. Fullbaselines werden einmal
gezählt. Auswahl erfolgt anhand Fall-/Request-/Attempt-/Vertragsbindungen, nicht nach
Dateizeit oder bestem Ergebnis. Die 527 historischen Genericzeilen umfassen 499 Rohoutput-Splits und 28 Completed-Fulls.
204 technische Paarungen sind von 201 Qualitytransferfreigaben und 0 wissenschaftlichen
Claims getrennt; gültige zentrale Qualityentscheidungen erzwingen keine Paarfreigabe.
Die kleinen veröffentlichten Eingaben enthalten keine
Modelle, Tensorpayloads, Bilder, privaten Pfade oder Zugangsdaten.

Historische Workflowstatusfelder (`partial`, `not_evaluated`) bleiben unverändert.
Die auditierte Messmatrix ist vollständig. Wissenschaftliche Vergleichsfreigabe bleibt
separat: Screening-/Developmentrollen, unkontrollierte Zeit-/Thread-/Thermikbedingungen
und gültige Accuracyverluste verhindern pauschale kausale oder Hold-out-Aussagen.

### 23.2 Abgeschlossene lokale Korrekturen

- F01: 47 H10-Labels korrigiert; echte TensorRT-Fälle erhalten.
- F02: 186 historische Authoritykonflikte durch reguläre Originalbindungen erklärt; falsche Run-/Setup-/Requestbindungen bleiben negativ.
- F03: sechs TRT-Full-Numerikbelege aus gespeicherten Outputs erfolgreich nachgeprüft. YOLO26s-Vendor-Full H8/H10 bleiben echte negative numerische Ergebnisse.
- F06: 588 Sollfälle regulär bilanziert; 61 terminale Ausschlüsse und alle Qualityentscheidungen aus Originalen projiziert. Die 45 historischen `quality_missing_or_unbound`-Zeilen entsprechen **21 negativen Builds und 24 Policyausschlüssen**, nicht 45 offenen Qualityjobs.
- F04: ursprüngliche Generic-Rohoutputzeiten bleiben getrennt; die später autorisierte Completion ergänzt 192 Basis- und zwölf Zusatzpaare ohne erneute Native-/Qualitykampagne.
- F05: alle 246 Energiebeobachtungen und tatsächlichen Workcounts sichtbar; primäre FS-Energie bleibt unsubtrahiert. Die lokal gebundene Originaloutputprüfung bestätigt 20/24 neue semantische Split–Full-Paare; mit 372/384 Basisvergleichen ergibt das 392/408. Vier neue und zwölf historische Grenzen bleiben erhalten. Alle wissenschaftlichen Claim-Gates bleiben unverändert.

### 23.3 Aufnahmegeschichte und H8/b066

Die physische Quellenhistorie erklärt 705 Basis- und 42 Zusatzversuche. Bei den zwei
unbestätigten Unterbrechungen wurde kein physischer Reset behauptet. Einmalige
Wiederanlauffreigaben und der separat gültige Funktionstest bleiben eigene Diagnosen.
Das Energieretrybudget wurde ausschließlich für die drei offenen H8-Zeilen von zwei auf
fünf erhöht, verbrauchte Versuche mitgezählt; keine ungültigen Aufnahmen wurden nachträglich PASS.

H8/b066 misst Prepared Input bis vollständig abgeschlossenes Detectionergebnis im
aktuellen Dreistufenpfad, mit aktuell gebundener Engine und eingefrorener Nachverarbeitung.
Keine Gleichsetzung mit historischen Paperzeiten anderer Engine-/Messgrenzen. Die zwölf
Zusatzfälle sind post-planned/development; neun Reserven bleiben ungemessen.

### 23.4 Reproduktion, Release und noch laufendes Archiv

Die gemeinsame Auswertung verwendet vorhandene Reader/Reporter und Rangfunktionen.
Rechenprüfungen beziehen sich auf gespeicherte Count-/Makespan-/Markeraggregate, nicht
auf erneute Hardwaremessung, Bootstraprechnung oder Neukalibrierung. Jede Abbildung hat
eine kleine Eingabetabelle. Rangtransfer bleibt innerhalb zulässiger Modell-/Setup-/
Precision-/Endpunktgruppen; n=3 macht Top3 trivial. Accuracyverluste bleiben in der Gesamt-
ansicht, eine referenznahe Teilansicht ist explizit gekennzeichnet.

[Toolrelease v2.92.0](https://github.com/Keff789/ONNX-Splitpoint-Tool/releases/tag/v2.92.0), Maincommit `d164aad6d7c7ef68c1b371c49a1fdea0a3b27dd7`, annotierter Tag und beide Quellenarchive sind veröffentlicht und remote verifiziert. Die Messquellcheckpoints werden zusätzlich privat erhalten;
der aktuelle Release versieht historische Messungen nicht rückwirkend mit neuer Provenienz.

Der bestehende Benutzertransfer kopiert die Hauptkampagne direkt in den gemounteten
Roharchivwurzelbaum. Die Ergänzung wartet in einer dauerhaften Sitzung und kopiert danach
192er-Completion, vollständige YOLO-Arbeit, korrigierte Basis, gezielt gebundene externe
Artefakte und diesen Abschluss sequenziell. Der Kopiervorgang ist beim Publikationsstand
**noch nicht vollständig abgeschlossen**; Pfadkarte und Transferlogs liegen privat.
Keine lokale oder Remoteoriginaldatei wird gelöscht.

<a id="quellen"></a>
## Quellen- und Fundstellenverzeichnis

Die Kennungen verweisen auf vorhandene Dateien beziehungsweise klar benannte Chatbeobachtungen. Innerhalb von ZIPs sind die angegebenen Pfade relativ zur Archivwurzel. Frühere KB-Begleitpakete enthalten die dort benannten Dokumente und read-only Projektionen. Das damalige REV3-Begleitpaket enthielt ausschließlich die aktualisierte KB, Änderungsnotiz, Textdiff und Dokumentprüfbericht, **nicht** die früheren Ergebnisarchive, Modelle oder erneut ausgeführte Projektionen.

**[E-KB]** `ONNX_SPLITPOINT_KnowledgeBase_CANONICAL_v2.79.17_2026-09-03.md`, aus der File Library herangezogene kanonische Vorgängerfassung. Insbesondere Dokumentführung/Evidenzklassen, wissenschaftlicher Leitpfad und Fragenkatalog, Energie/Kalibrierung, Backend-/Fairnessregeln, historische Claim-Map, Evidenzablage und Übergabestand. Historische Fassung bleibt unverändert; sie ist nicht als neue Datei diesem Paket beigelegt.

**[E-KB15]** `ONNX_SPLITPOINT_KnowledgeBase_v2.79_Three_Stage_2026-09-03_UPDATED_v2.79.15.md`, historischer Hinweis auf FS/command und den längeren 60-s-×-3-Abnahmeumfang. Die späteren v17-Klarstellungen zu Gain-/Idle-Skalendomänen haben gegenüber früheren pauschalen Wiederverwendungsaussagen Vorrang.

**[E-V30]** `ABNAHME_v2.79.30_und_Complete_Set_v2.79.29.md`, §§1–3 für Release-/Testumfang, §4 für Zähler/Closure, §§5–8 für CS1–CS8 und Qualität/Energie.

**[E-V30-N]** `ABNAHME_v27930_NACHWEISE.zip`, unter dem Archivpräfix `v27930_audit/evidence/`, insbesondere `independent_packaging.json`, `independent_targeted.log`, `terminal_closure_smoke_fast.json`, `terminal_closure_smoke_strict.json`, `independent_complete_replay.json`, `independent_hailo_replay.json`, `BEFUNDE_Complete_Set_v27929.json` und `independent_supervisor_diagnostic.json`. Beschreibt die bereits ausgeführte unabhängige Abnahme, keine neue Ausführung bei diesem KB-Update.

**[E-CS]** `complete_set_20260907_161614_debug_pack.zip`, insbesondere `reports/native_producer_summary.json`, `reports/native_stage_concise_summary.json`, `reports/native_evidence_status.json`, `quality_management/central_quality_summary.json`, `reports/artifact_index_closure.json` und `reports/native_energy_measurements/native_producer_energy_results.json`. Dort: `rows[*].row.duration_s`, `rows[*].run.energy_aggregate`, `full_system_current_scale_*`, `accelerator_idle_*`, Primär-/Shadow-Methode und Replikatzähler.

**[E-PLAN31]** `IMPLEMENTATIONSPLAN_v2.79.31_Complete_Set_Integration_und_Qualitaetsdiagnostik_REV4_FINAL.md`, verbindlicher Auftrag; AP0–AP11, §§16–20 für 103 geplante Prüfgruppen, Gates und Freigabe. Maßgeblich für die Umsetzung, nicht als bereits erfüllte Evidence zählen.

**[E-PLAN30]** `IMPLEMENTATIONSPLAN_v2.79.30_DeepX_Full_Normalworkflow_REV2.md`, ursprünglicher Sollstand für Full-Prüfübergänge und terminalen Abschluss. Bereits erfüllte Aufgaben in v31 als Regression erhalten, nicht nochmals als neue offene Diagnose erfinden.

**[E-R1]** `deepx_prepost_smokes_r1_20260908T080238Z_vo3whdeu.zip`: `collection_summary.json`, je Modell `analysis.json`, `cpu/cpu_result.json`, `cpu/graph.json`, gespeicherte `cpu/cpu_*.npz` und `remote/native_*.npz`/`quality_*.npz` sowie Split-/Kalibrierungsbeobachtungen. Herkunftsrun `complete_set_20260907_161614`.

**[E-R1-A]** `AUSWERTUNG_DeepX_PrePost_Smokes_R1.md`, vorhandene Auswertung und Scopegrenzen.

**[E-R1-LOCK]** `deepx_prepost_smokes_r1_20260908T065807Z_dct6j689.zip`, einzig `collection_summary.json`: blockierter Start, leere Modellliste. Dazu die im Chat gezeigte Lock-/Prozessbeobachtung. Kein Modelllauf.

**[E-R2]** `deepx_meanstd_ab_r2_20260908T084314Z_wwtqdejm.zip`: `collection_summary.json`, je Modell `analysis.json`, `build/build_summary.json`, `build/adapter_ort_parity.json`, Compilerprotokolle und `remote/arm_a_*.npz`/`arm_b_*.npz`. CPU-Gegenpopulation aus den exakt passenden R1-Bild-IDs.

**[E-R2-A]** `AUSWERTUNG_DeepX_MeanStd_AB_R2.md`, vorhandene A/B-Auswertung und ausdrücklich offene B500-/RegNet-/Splitgrenzen.

**[E-R2-PKG]** `DeepX_MeanStd_AB_Smoke_R2.zip` und zugehörige `README.md`/`TEST_REPORT.md`; Scope, Staging, Lock-Preflight und Diagnoseabgrenzung.

**[E-D26]** `v27926_DeepX_YOLO11l_Diagnose.md` und `v27926_acceptance_d_yolo11l_b003_deepx_gpu_20260907_101443_debug_pack(1).zip`; ursprüngliche Eingabe-, Postprocessing-, Matrix- und Energiefehler.

**[E-NUMERIK]** `deepx_full_probe_v27927_fix1_20260907T104449Z_2_jd9v0e.zip`, insbesondere `results/deepx_output_value_probe.json` und Rohoutput-NPZ; außerdem `PRUEFBERICHT_2.79.28.md` und `PRUEFBERICHT_2.79.29.md` für die begrenzte Numerik-/Importkorrektur.

**[E-D29]** `v27929_acceptance_d_yolo11l_b003_deepx_gpu_20260907_151417_debug_pack.zip` und `v27929_D_diagnose/DIAGNOSE_v27929_D_Normalworkflow.md`: reale Replikate, fehlende Semantik-/Completionintegration und zentrale Qualityannahme.

**[E-INSTALL29]** `v27929_install_acceptance_20260907_125759_497558239_2858752.zip`, `full_console.log` und `dedicated_acceptance.log` im benannten Installationsverzeichnis.

**[E-PROBE29]** `deepx_full_probe_v27929_20260907T130020Z_jjl3xxus.zip`, `results/deepx_output_value_probe.json` und `collection_summary.json`; ergänzend `v27929_auswertung/vergleich_FIX1_v27929.json` für den bereits dokumentierten Rohtensorvergleich.

**[E-ABSCHLUSS]** `v27929_Nachlauf_nach_finished_Codestellen.txt`, `v27929_afterrun_inspect/QUELLBELEGE_Hash_Cache_Nachlauf.md` und die im Chat gezeigten Prozess-/Dateistatistiken vom 7. September, zusammen mit dem tatsächlichen Closure-Bericht aus [E-CS].

**[E-OVERNIGHT]** `_latest_evaluation_workflow(20260908-070755).log`, interner Run `complete_set_20260908_030632`, Version v30. Maßgeblich sind die im Inhalt stehenden Zeitstempel, nicht allein der Exportdateiname.

**[E-CHAT]** Im vorliegenden Gespräch eingefügte Konsolenausgaben und Nutzerentscheidung zum Overnight-Artefaktlauf, insbesondere die nachgereichten Bias-Correction-Zeilen bis 09:32:52 sowie die MobileNet-Rückfrage. Es wird kein nicht hochgeladener Endabschluss ergänzt.

**[E-DOC]** Im Begleitpaket `checks/document_evidence_checks.json` und `checks/energy_existing_evidence_projection.json`. Read-only Abgleich archivierter R1-/R2-NPZs, gleicher Bild-/Labelpopulationen, R2-Zähler sowie der 55 vorhandenen Energieaggregate; außerdem reine Dokumentzählung der 103 geplanten Gruppen. Keine neue Inferenz, keine neue Kalibrierung, kein wissenschaftlicher PASS.

**[E-2804-CHAT]** Projektunterhaltung vom 8.–12. September 2026: v33 Force-OFF, v34/v2.80-Abnahmen, .3-FIX1–FIX5-Zielausgaben und Hailo10-MobileNet-Build/Runtime. Terminal-/Testzahlen gelten nur für ihren benannten Lauf; Zusammenfassungen ersetzen keine neue Originalprüfung.

**[E-2804-PLAN]** `IMPLEMENTATIONSPLAN_v2.80.4_Hailo8_GPU_Produktivpfad_Quality_Cancel_und_Debuglimits(1).md`, 12. September 2026, AP0–AP6, 56 geplante Prüfanforderungen. Insbesondere §1.3 H8-Fixed16, §5 Q5-Cancel-Soll und §8.2 MobileNet-B5000-Werte. Planrolle und tatsächlich verfügbare Originalnachweise unterscheiden.

**[E-2804-H8-Q2]** `Eingefügter Text(20260912-121049).txt`, tatsächliche H8-Runtime-Konsole; im Bundle als `Q2_terminal_report.json` abgeleitet, Run `hailo8_mobilenet_runtime_8FehkBqO`. Der Quellenindex kennzeichnet separat, ob Q1 `runtime_evidence(1).zip` für unabhängigen Recount verfügbar war.

**[E-2804-QUALITY]** `v2803_yolo11l_quality5000_6yzd81fj.zip`, vollständiger Ergebnisexport `v2803_quality5000_export_zu5ufxbf.zip`; Lauf `v2803_yolo11l_quality_5000_20260912_084434`. Nachgereichter Export bestätigt vollständige kanonische CPU-/Kandidatenvorhersagen, Identitäten und AP-Reproduktion; verändert den ursprünglichen Run nicht.

**[E-2804-ABGLEICH]** `ABGLEICH_Hailo_Qualitaet_2026-09-12.md` und `onnx-splitpoint-results-main(4).zip`: frühere KB `docs/ONNX_SPLITPOINT_KnowledgeBase_v2.79_Three_Stage_2026-09-03_UPDATED_v2.79.16.md`, §3.4, Opt1/Opt2; Paper-Level1-Primärbericht und v29-Complete-Set-Qualität. Opt2-Rohbericht nicht gefunden; kein erfundener direkter YOLO11l-A/B-Test.

**[E-2804-SOFTWARE]** Zugehörige v2.80.4-Lieferung: finaler Source-Manifest-/Archivabgleich, konkrete Software-/Upgradeprüfung und Quellenindex. Diese Dateien bestimmen, welche .4-Tests tatsächlich gelaufen sind. Zielhardware wird dadurch nicht automatisch abgenommen.


## Zusätzliche Quellen der REV2

**[E-KB-2804-INPUT]** Unveränderte hochgeladene `ONNX_SPLITPOINT_KnowledgeBase_CANONICAL_v2.80.4_2026-09-12(1).md`, ursprüngliche 578 Zeilen. Trägt u.a. die neueren .3-FIX5/.4- und separaten YOLO11l-/Opt2-Aussagen. Keine neue Originalprüfung dieser nicht zusätzlich gelieferten Release-/Qualityarchive in REV2.

**[E-HAR-R1]** `har_and_git_evidence.zip`; `results/hailo8/20260912_mobilenet_gpu/har_emulation/hailo8_har_git_20260912T171411Z_x0j2t2o1/`: `comparison.json`, `comparison_request.json`, `REPORT.md`, `CLAIM_BOUNDARIES.md`, `controller_summary.json`, `parsed_native/api_and_model.json`, `quantized/api_and_model.json` und Stufenergebnisse. SDK 3.33.1; HARpfade aus ursprünglichem GPUbuild, Hashes erst beim HAR-R1 erfasst.

**[E-H8-COMPUTE]** Im selben Archiv `results/hailo8/20260912_mobilenet_gpu/compute/`: Paket-/Overlaymanifest, Venvinventare, tatsächliches Computeergebnis und ptxas-Trace. Historischer Lauf `hailo8_gpu_test_20260912T062240Z_hx7b7hcq`.

**[E-H8-BUILD]** Im selben Archiv `.../build_metadata/`: ursprünglicher Request, CPU- und privates GPU-Receipt, Builderargumente, Phasen, eigene GPUaktivität, Compilerlog, Supervision. Lauf `hailo8_mobilenet_gpu_20260912T083456Z_a_10a8wv`. Historischer CPUzeitvergleich zusätzlich im bereits erstellten H8-Modellbuild-Abnahmebericht; kein neuer kontrollierter Zeitbenchmark.

**[E-H8-RUNTIME]** Im selben Archiv `.../runtime/{comparison.json,runtime_request.json,results/runtime_result.json}`; tatsächliche HailoRT-4.20.0-/VStreammetadaten und 32 abgeschlossene Inferenzen. Runtime-Roharrays nur mit Pfad/Hash referenziert, nicht im ZIP. Run `hailo8_mobilenet_runtime_8FehkBqO`.

**[E-NIGHT-QUALITY]** Im selben Archiv `results/evaluation/completsetdev_20260911_213508/quality_snapshot/quality_management/central_quality_summary.json` und sieben Referenzstatus/-logs, dazu alle 123 Requestdateien. 43/18/2 fertige Qualityentscheidungen; 4/56 Cancel-Ausnahmearten. Alte Datei bleibt technisch `failed`; neue Dokumentprojektion beschreibt ihren belegten Cancelkontext ohne Originalumschreibung.

**[E-NIGHT-2803]** `evaluation_workflow(20260912-050559).log`, `evaluation_workflow(20260912-054051).log`, `profile(2).yaml`, `run_manifest(3).json`; bereitgestellte Auswertungen unter `night_current_20260912/`. Beobachteter Lauf `completsetdev_20260911_213508`; aktueller Snapshot und historische Beendigung nicht gleichsetzen.

**[E-FORCE-AUDIT]** `AUSWERTUNG_Force_Ursprung_v27932_2026-09-09.md`, `force_audit_analysis_20260909/REPLAY_FORCE_ORIGIN.json`, ursprüngliche Registry und Verlauf. Ein gespeichertes true belegt keine bewusste Nutzeraktion.

**[E-GPU-HISTORY]** Ursprüngliche GPU-/Toolchainarchive und die im Chat erzeugten Abnahmen: `AUSWERTUNG_Hailo_GPU_Rechensmoke_R1_2026-09-09.md`, `AUSWERTUNG_Hailo_GPU_FIX1_und_v27933_2026-09-09.md`, `AUSWERTUNG_Hailo_Toolchain_2026-09-09.md`, Hailo10-XLA-R2- und v34/v2.80-Build-/G3-Abnahmen. Historische Familientests, kein neuer .4-Hardwarelauf.

**[E-RELEASE-AUDITS]** `ABNAHME_v2.79.31_Implementierung_REV4_2026-09-08.md`, `ABNAHME_v2.79.34_Hailo_GPU_und_Artefaktvorbereitung_2026-09-09.md`, `ABNAHME_v2.80_Hailo_Environment_Cleanup_und_Reuse_2026-09-09.md` sowie `v2801_target_review_20260910/`-Zielabnahme. Eigene vs. gelieferte Tests, Software-/Hardware-Scope und fehlende Auditabhängigkeiten bleiben wie dort dokumentiert.

**[E-WORKFLOW-HISTORY]** `biggerset_v280_analysis_20260910/`, `completsetdev_v2801_review_20260910/` und `review_v2802_overnight_20260911/`: Originalfehlerquellen, zugehörige Reports und gezielte Replays. Keine nachträgliche Messfreigabe aus einem Reportfix.

**[E-REUSE-TARGET]** `v280_target_review_20260910/independent_review.json` und die zwei originalen `v280_hailo_reuse_*`-Archive. Vier frische Controllerprozesse für genau den gebundenen MobileNet-H10-Request.

**[E-QUALITY-EXPLAIN]** `quality_explanation_20260912/AUSWERTUNG_Qualitaetsauftraege_und_Debugexport_2026-09-12.md`, damals gegen Run-Modulprüfsummen abgeglichene `quality_service.py`/`quality_metrics.py` und der reale Cancel-Snapshot. Neue .4-Implementierung in diesem KB-Update nicht neu ausgeführt.

**[E-GIT-PUSH]** `Eingefügter Text(20260912-171533).txt`, finale Pushbestätigung und Commit-ID; inhaltlich zugehöriger 236-Dateien-Payload `har_and_git_evidence.zip`. Keine automatische Aussage über den späteren Remote-HEAD.

**[E-DIAGNOSE-PLAN]** Früherer Begleitplan `DIAGNOSEPLAN_Hailo8_Optimierung_Quantisierung_Runtime_2026-09-12.md`. Vorgeschlagene zusätzliche Stufe `SDK_FP_OPTIMIZED` mit lokaler Verfügbarkeitsprüfung, versionsgebundene Integer-I/O-Kontrolle und bedingte innere Diagnose. Nicht implementiert oder ausgeführt. **Seit REV3 ausdrücklich zurückgestellte optionale Folgearbeit; keine aktive Abnahme-/Dissertationspflicht.** Die Originaldatei bleibt unverändert; aktuelle Priorisierung nach [E-SCOPE-REV3] und §12.

**[E-HAILO-OPT-DOC]** Externe Herstellerbeschreibung, Hailo Model Zoo `docs/OPTIMIZATION.rst`, Introduction und Optimization Workflow; abgerufen am 12.09.2026. Belegt die begriffliche Trennung Full-Precision- und Quantisierungsoptimierung, keine konkrete Ursache unseres Modells und keine API-Freigabe für DFC 3.33.1. URL zur Quellenauflösung:

```text
https://github.com/hailo-ai/hailo_model_zoo/blob/master/docs/OPTIMIZATION.rst
```

**[E-KB-REV2-CHECK]** Im vorherigen REV2-Update erzeugtes `evidence/SOURCE_AUDIT.json`, `GIT_STATUS.json`, `QUALITY_SNAPSHOT_COUNTS.json` und `DOCUMENT_CHECKS.json`. Read-only Archiv-/Text-/Klassen-/Dokumentabgleich; keine DFC-/ORT-/Hardwareausführung und keine Repositoryänderung. Begleitdiff dokumentiert sämtliche Änderungen zur unveränderten Eingabe-KB.


## Zusätzliche Quellen und Entscheidungen der REV3

**[E-KB-REV2-INPUT]** In diesem Auftrag beigefügte `ONNX_SPLITPOINT_KnowledgeBase_CANONICAL_v2.80.4_2026-09-12_REV2(1).md`, 845 Zeilen. Unverändert erhalten; vollständige Textgrundlage dieser Fortschreibung. Historische Mess- und Releaseaussagen werden daraus übernommen, nicht als neu ausgeführte Prüfungen bezeichnet.

**[E-SCOPE-REV3]** Unmittelbar vorausgehende Projektdiskussion und anschließender Nutzerauftrag zur Aufnahme in die KB: Forschungsfrage „wie gut funktioniert das Splitten eines Netzwerks einfach so mit meinem Tool“, Einwand gegen tiefe Einzelnetzoptimierung, Frage nach Aufwand und zulässiger Tuning-Future-Work-Aussage. Dokumentiert wird die danach bestätigte Abgrenzung: festes automatisches Verfahren bewerten; korrekte Negativergebnisse erhalten; eigene Fehler nicht dem Compiler zuschreiben; vertiefte Hailo8-Ursachenklärung zurückstellen; keine Verbesserung aller Netze garantieren. Die genannten Aufwandsbereiche sind grobe Chat-Planungsschätzungen, keine Messdaten. Dokumentiert am 13. September 2026; kein nachträglicher experimenteller Nachweis.

**[E-KB-REV3-CHECK]** `REV3_DOCUMENT_CHECKS.json`, `REV2_to_REV3.diff` und `AENDERUNGEN_KB_v2.80.4_REV3_2026-09-13.md` im REV3-Begleitpaket. Prüfen ausschließlich die Textfortschreibung, den unveränderten Eingabestand, bestehende Ergebnisabschnitte, Überschriften, Verweise und die konsistente Zurückstellung. Keine ONNX-/DFC-/Runtime-/Hardwareausführung, kein Produktpatch und kein Gitpush.


## Zusätzliche Quellen und Entscheidungen der REV4

Die folgenden Kennungen trennen historische Messungen, diese Dokumentgegenprüfung und aktuelle Aufträge. Externe Ergebnisarchive bleiben in der Unterhaltung/Originalablage; das neue KB-Paket enthält keine Modelle, Binaries, großen Roharrays oder vollständigen Diagnosearchive. Ausgewählte R8-Berichte liegen unter `evidence/`. Dies ist keine automatische Veröffentlichung privater Hostkonfiguration nach GitHub.

**[E-KB-REV3-INPUT]** Aktuell vom Nutzer beigefügte `ONNX_SPLITPOINT_KnowledgeBase_CANONICAL_v2.80.4_2026-09-13_REV3(2).md`. Vollständig gelesen, byteidentisch unter `historie/` erhalten. Ausgangspunkt für Methodik, historische HAR-/Kalibrationsbefunde und rund97,077/97,059 FPS unter `yolov7_paper/b066`. Die damalige Paper-Rohquelle wurde in diesem Update nicht zusätzlich neu geprüft.

**[E-CX-SETUP]** Nutzerkonsole/Projektgespräch vom 14.–15.09.2026: Architekturkorrektur Smartmirror2=x86, CLIinstallation 0.154.0, Node/npm/Git/Python, ChatGPT-Login, `codex --help`, `doctor`, Sandboxfehler und tatsächliche Folgeausführungen; Gitbaseline-/Tag-/Branch-Push und anschließender Arbeitsbranch. Konkrete historische Terminalausgaben im Gespräch; daraus keine aktuelle automatische Remoteverbindung oder unbekannte spätere Commits ableiten.

**[E-CX-PREF]** Nutzerentscheidungen derselben Unterhaltung: Evalanalyse hier und Implementationsauftrag an lokalen Codex; keine wiederholten Berechtigungsfragen; Ultra nutzen, wenn sinnvoll; ein Hauptverantwortlicher für Hardware; sichtbare Tagesausführung; kleine Tests durch echte GUI ausdrücklich bevorzugt; keine langen Finalprofile als Workflow-Smoke; Qualityoptimierung zunächst zurückgestellt; fortlaufende Liste offen/erledigt. Keine zusätzliche Hardwarefreigabe allein durch diese KB.

**[E-NIGHT-282]** `completsetdev_20260913_222455_debug_pack(1).zip`, `AUSWERTUNG_v2.82_Nachtlauf_20260913_222455(1).md` und vorhandene Gegenprüfung im R1-Planpaket. Counts61/63 Native,74Quality,60/61Energie; H8-Feldweitergabe, H10-Nulloutputs und DeepX-Bild-IDs. Im aktuellen KB-Update als vorhandene Analyse/Evidenz übernommen, kein erneuter vollständiger Rohreplay.

**[E-CX-R1]** `v283_fix_smoke_results.zip`, `ABSCHLUSSBERICHT.md`, Berichte/Patch/Testprotokolle; bestehende Gegenprüfung aus `Codex_v283_Fortsetzung_R2/`. Reporter-/Scope-/Student-t-/Capturefixes und vor SSH blockierter Hardwaretest. Nicht mit der DeepX-Preprocessing-R1 vom 08.09. verwechseln.

**[E-CX-R2]** `ERGEBNISSE_R2.zip` / `ABSCHLUSSBERICHT_R2.md`, `H8_BEFUND_R2.md`, `H10_BEFUND_R2.md`, `DEEPX_BEFUND_R2.md`, `ENERGIE_BEFUND_R2.md` und zugehörige Gegenprüfung. H8 unabhängige CPUreferenz, H10-Resolver/Quantisierungskontrolle, native XYXYfehler und überschrittene damalige Beobachterstopregel.

**[E-CX-R3]** `ERGEBNISSE_R3.zip`, Abschluss-/Test-/Installedberichte und vorliegende R3-Gegenprüfung. 310 Testfälle, lokale Budgetprozesszähler, Diagnoseausgabepfad/ACLkonflikt; keine realen neuen Energiemessungen.

**[E-CX-R4]** `ERGEBNISSE_ENERGIE_R4.zip`, `ABSCHLUSSBERICHT_ENERGIE_R4.md`, Test-/Nachtstartberichte und vorhandener Zeitachsenabgleich. Drei reguläre Starts, einer gültig, danach Stop; Host-/Geräteaufnahmezeitunterschied als konkrete Diagnosebasis, keine abschließende Transportursache.

**[E-CX-R5]** `ERGEBNISSE_R5(2).zip`, `ERGEBNISSE_R5_FORTSETZUNG.zip`, Build-/UDP-/Hardwareberichte und vorhandene Gegenprüfungen. Offline-Dependencyblocker, private Rustkorrektur und Fortsetzung mit zugelassener festgeschriebener Dependencybeschaffung; zweite reale Aufnahme ohne vollständigen Sourceabschluss, keine dritte Kette.

**[E-CX-AUTO]** `ERGEBNISSE_AUTO.zip`, insbesondere `ABSCHLUSSBERICHT.md`, `COLLECTORBEFUND.md`, Testberichte und die vom Nutzer gezeigten `NACHTSTART.json`/Supervisor-/Startversuchabfragen. `ready:false`, CodexExit0, kein Nachtstart und kein eingerichteter separater Fallback. Quellen- und Nachtstartprobleme der14./15.09. nicht mit dem nun gemeldeten laufenden R8-Nachtlauf verwechseln.

**[E-CX-R6]** `ERGEBNISSE_R6.zip`, `ABSCHLUSSBERICHT_R6.md`, `ABENDSTART_VORBEREITET.md`, JUnit/Test-/Collector-/Hardwareberichte; vorliegende `r6_independent_review/GEGENPRUEFUNG_R6.md`. 567 Produktfälle,11 Rust/21 UDP,2 Diagnosen + 3 Energieaufnahmen; private technische Bindung, keine normale GUIintegration.

**[E-GUI-085558]** `completsetdev_20260915_085558_debug_pack.zip`, Primärfehler/Workflowprotokoll und `jobs/p01_unresolved_cleanup_quarantine.json`; Gegenprüfung `Codex_v283_GUI_R7/GEGENPRUEFUNG_GUI_RUN.md`. Storageprobe rc124 auf H8/H10 und anschließender lokaler Managementabschluss; keine kausal gesicherte Festplatten- oder Collectorursache.

**[E-CX-R7]** `ERGEBNISSE_R7.zip`, `ABSCHLUSSBERICHT_R7.md`, `GUI_STARTBINDUNG.md`, Testnachweise/Patches und `r7_review_actual/GEGENPRUEFUNG_R7.md`; kontrollierte Hostübernahme im Gespräch. 647 Tests im Kandidaten, späterer normaler R7-Run belegt Benutzung des R7-Builds. Alter Storage-Timeout nicht ursächlich geklärt.

**[E-R7-RUN]** `completsetdev_20260915_124548_debug_pack.zip`, `AUSWERTUNG_v2.83_R7_20260915_124548.md` und Begleitpaket `Auswertung_R7_Run_20260915_124548.zip`. 61/63 Native,75 Quality,342 Hauptcollectorversuche/24 gültig/0 volle Zeilen, Laufzeitblöcke, falsche technische Collector-/Budgetbindung und Logflut. Diese Tabellen wurden früher aus dem Originalpack ermittelt; diese KB führt sie als vorhandene Auswertung fort und führt den mehrstündigen Run nicht erneut aus.

**[E-CX-R8]** `ERGEBNISSE_R8.zip`, `ABSCHLUSSBERICHT_R8.md`, `TEST_RESULTS_R8.json`, `acceptance_r8_complete.xml`, `junit_r8_gui_verified.xml`, `source_final.json`, `HARDWARE_RESULTS_R8.json`, `GUI_SMOKE_DEBUG_R8.zip` und Config-/GUIbelege. Aktuelle Hauptinstallation, 678/6-Fälle, normale Config und genau ein positiver realer H8-GUI-Smoke. Im Dokumentupdate erneut gelesen und JUnit gezählt; keine neue Ausführung. Das Hardwarepack wurde in der vorherigen R8-Gegenprüfung unabhängig inventarisiert; hier keine neue Roh-Parquet-Integration.

**[E-CX-R8-CONFIG]** Im R8-Ergebnis: `CONFIG_DIFF_R8.json`, `config_installation.json`, `config_idempotence.json`, Source-/Importnachweise. Normale Registry/Energiespiegel, verwaltete R6-Bytes, enge Schema 14-/Standardtuplemigration und Backups. Konfiguration nur im dokumentierten Zustand, nicht als Liveabfrage während des Nachtlaufs.

**[E-CX-R8-GUI]** Im R8-Ergebnis: `GUI_BEDIENUNG.md`, `GUI_RESTART_R8.json`, `GUI_RESTART_VISIBLE_SUMMARY_R8.txt`, tatsächliches Smokeprofil und Start-/Hardwarebelege. Originales CompleteSetDev nach Abschluss wiederhergestellt; der spätere Nutzer meldet einen davon gesonderten gestarteten Nachtlauf.

**[E-CX-R8-TRACKER]** `ERGEBNISSE_R8.zip:ARBEITSSTAND.md`, die dokumentierte Kopie von `docs/ARBEITSSTAND.md` mit Zuständen, Verlauf und Abnahmegrenzen. Im Begleitpaket als damaliger Snapshot unter `evidence/` erhalten; neue Aufgaben in §12 dieser REV4. Keine automatische Überschreibung der Hostliste während des Runs.

**[E-CX-R8-STARTER]** `ONNX_Codex_v283_GUI_Integration_R8.zip:START_R8.sh`, `host_preflight.py` und Auftrag. Tatsächliche Anforderung `gpt-6-astra`, `model_reasoning_effort="ultra"`, `workspace-write`, `never`, Netzwerk sowie drei zusätzliche Schreibwurzeln; sichtbarer `codex exec`-Aufruf. Anforderung und Teststub sind keine eigenständige Garantie modellinterner Verteilung.

**[E-R8-REVIEW]** Vorherige unabhängige Gegenprüfung `r8_current_review/GEGENPRUEFUNG_R8.md`, `INDEPENDENT_CHECKS_R8.json`:112 inventarisierte äußere Dateien,775 im GUI-Debugpack,678/6Testknoten,647 R7 erhalten und9 tatsächliche Collectoraufrufe. Diese vorhandene Prüfung wird zitiert; bei diesem Dokumentupdate wurde nur die explizit im Quellenprüfbericht angegebene Teilprüfung erneut ausgeführt.

**[E-NIGHT-R8-USER]** Aktueller Nutzerauftrag vom 15.09.2026: KB einschließlich Codex/GUItests aktualisieren; „Der Nachtlauf läuft“; nach technischer Abschlussprüfung Hailo10-YOLO26 und weitere Qualityfragen, historischen passenden97 FPS-Vergleich, weitere Performance- und Energieplausibilität prüfen. **Noch keine Run-ID, kein Profilfreeze und keine Abschlussdaten dieses Nachtlaufs übergeben.** Der erwartete positive Verlauf ist eine Hoffnung/Prüfabsicht, kein Ergebnis.

**[E-CODEX-OFFICIAL]** Offizielle OpenAI-Dokumentation, am 15.09.2026 aufgerufen; nur zur knappen allgemeinen Begriffs-/CLIeinordnung, keine Benchmarkevidenz. Die Ausgangs-URLs leiten teilweise auf ChatGPT Learn um:

```text
https://developers.openai.com/codex/noninteractive/
https://learn.chatgpt.com/docs/non-interactive-mode
https://developers.openai.com/codex/guides/agents-md/
https://learn.chatgpt.com/docs/agent-configuration/agents-md
https://learn.chatgpt.com/docs/agent-approvals-security
https://learn.chatgpt.com/docs/agent-configuration/subagents
https://learn.chatgpt.com/docs/cli/reference
```

**[E-REV4-DOC]** Begleitdateien `AENDERUNGEN_REV4.md`, `REV3_to_REV4.diff`, `DOKUMENTPRUEFUNG_REV4.json`, `evidence/QUELLENPRUEFUNG_REV4.json`; reiner Dokument-/Quellen-/JUnitabgleich. Quellenrang, alle alten Methoden-/Ergebnistabellen, historische Abschnittsfolge, neue eindeutige Anker und interne Referenzen werden geprüft. Keine Source-/Hardwareausführung, keine Datenänderung, keine Remoteveröffentlichung.

## Zusätzliche Quellen und Entscheidungen der REV5

| ID | Quelle / Reichweite |
|---|---|
| E-REV5-BASE | Unveränderte vollständige REV4 vom15.09.2026; historische Tabellen/Methoden erhalten, frühere Belegpakete weiterhin Referenz |
| E-REV5-R9B | ERGEBNISSE_R9B_RESTABNAHME_FORTSETZUNG.zip: fortsetzung/ABSCHLUSSBERICHT.md, GUI_COVERAGE.json, acceptance.xml; frühere separate Gegenprüfung |
| E-REV5-R9C | ERGEBNISSE_R9C.zip final_acceptance.xml/final_gui.xml; ERGEBNISSE_R9C_H10_NACHTEST.zip ABSCHLUSSBERICHT.md; Latenz-/Captureeinzelbelege in früherer Gegenprüfung |
| E-REV5-R9E | ERGEBNISSE_R9E_FIXES_TESTS.zip: COMPILE_STATUS.json, compile_only/SDK_RESULT.json, ABSCHLUSS_FIX.md, lokale 70er / Host-229erJUnit; unabhängiger R9E-Review |
| E-REV5-R9F | ERGEBNISSE_R9F_READER_TRANSPORT.zip: letzte Reader-/Auswahl-/Softwarelieferung; normale vollständige Ausführung erst in R9G |
| E-REV5-R9G | ERGEBNISSE_R9G.zip eval_02/GUI_RESULT.json und local_52o_a8ia/host_tests/tests.xml; erster Versuch/Kumulativdiff nicht mit zweitem Ergebnis gleichsetzen |
| E-REV5-R9G-AUDIT | R9G_Final_Review/AUSWERTUNG_FINAL.md, PRUEFUNG_FINAL.json, vorhandenes Workbook; ursprünglicher debug_core plus debug_nachtrag_20260918_225653_2333399.zip |
| E-REV5-R9G-FINDINGS | R9G_Final_Review/BEFUNDE_FUER_CODEX.json; source_run r9g_eval_20260918_171131. Kein R9H-Fehlernachweis |
| E-REV5-R9H-PLAN | ONNX_Codex_v283_R9H_Abnahme3.zip / AUFTRAG; vorgesehener Umfang, kein Erfüllungsbeleg |
| E-REV5-R9H-LOG | _latest_evaluation_workflow(20260919-051919).log: Header06:43:23, letzter Eintrag 07:19:10+02:00; host.log separat eval_01. Dateinamenzeit nicht als Laufstart interpretieren |
| E-REV5-GIT | Über GitHub-Connector gelesene Repo-/Commit-/Branch-/Verzeichnisstände am 19.09.2026; in GIT_UPDATE.md dokumentierte Basiskommit- und README-Blobidentität |
| E-REV5-DOC | DOKUMENTPRUEFUNG_REV5.json im Begleitpaket: Erhalt historischer Abschnitte, Patchdateiliste, Quellen-/Privacyprüfung und lokale Patch-Anwendbarkeit; keine neue Produkt-/Hardwareabnahme |

Die zusätzliche öffentliche Auswahl liegt im Evidence-Patch unter docs/V283_STATUS_2026-09-19.md,
results/acceptance/v2.83/, results/evaluation/r9g_eval_20260918_171131/ und
diagnostics/v2.83_h10_output/. Die vollständige, um lokale Benutzerangaben bereinigte KB wird hier unter `docs/KNOWLEDGEBASE.md` gepflegt. Alte Quellenverweise
bleiben Referenzen auf die bisherigen Belegpakete; diese Lieferung dupliziert sie nicht vollständig.

## Zusätzliche Quellen und Entscheidungen – THESIS20, 02.10.2026

Diese Quellen wurden in der Unterhaltung geliefert beziehungsweise im Ergebnis-Audit erzeugt.
Dateinamen/Pfade sind Fundstellen, **keine Behauptung, dass die vollständigen privaten Pakete
mit diesem Knowledgebase-Commit im Repository veröffentlicht werden**. Bei Pfaden unter `Run/`
ist die oben genannte THESIS20-Runwurzel gemeint. Die bisherigen Quellen bleiben erhalten.

| Kennung | Quelle und Aussagegrenze |
|---|---|
| E-TH20-AUDIT | `THESIS20_FINAL_AUDIT_20261002_093035.tar.gz`, 101 reguläre Dateien; daraus am 02.10. erstellter `THESIS20_ERGEBNISAUDIT_20261002.md` und `THESIS20_ERGEBNISAUDIT_20261002.zip`. Einzelwerte/Counts und Projektionswidersprüche geprüft; keine neuen Messungen, Rohtrace-Neuintegration oder neue AP-Rechnung |
| E-TH20-AUDIT-DETAIL | Im Auditpaket: `belege/Energie_Originalabschlussfelder.json`, `belege/energy_arithmetic_checks.json`, `belege/native_186_identity_contradictions.json`, `belege/Scientific_Report_Originalkopf.txt`; `tabellen/quality_backend_label_mismatches_47.csv`, `Native_8_semantische_Faelle.csv`, `Generic_Native_192_Vergleichspaare.csv`, `generic_missing_61_lifecycle_audit.csv`, `quality_losses_39_correct_source_labels.csv`, `Energie_234_Zeilen.csv` und übrige Fall-/Streuungstabellen |
| E-TH20-ENERGY-END | `_latest_evaluation_workflow(20261002-071104).log`, tatsächlicher letzter Eintrag 02.10. 05:34:24 +02:00; Energie `ROW_END 234/234` 03:49:23, Helper `rc=0` 03:49:31. Primärer Ergebnisnachweis zusätzlich `Run/reports/native_energy_measurements/native_producer_energy_results.json`; Workflow-Returncode allein bestätigt nicht sämtliche Replikat-/Claimfelder |
| E-TH20-2910 | Releaseabschluss 25.09.2026 (`ABSCHLUSS(1).md`): 2.91.0, `main`/Tag damals auf `182092216dfaf4f3ad36460a883098548c83bd8f`, effektiver 20er-Profilvertrag N5000/B1000 und Single-Tensorfilter AUS. Datiertes Releaseprotokoll, kein heutiger Host-Livecheck |
| E-TH20-2911 | Lokaler Vervollständigungsabschluss 29.09., `ABSCHLUSSBERICHT(10).md`: manifestgebundene Quellen, Native-Teilmenge, Validator/Energieprovenienz, selektiver Ergänzungseinstieg und Diagnoseexport. Damaliger Plan ist historisch, nicht heutiger Restumfang |
| E-TH20-2911-REENTRY | Abschluss `thesis20_resume_preflight_fix_2.91.1_f7yt3xf8/ABSCHLUSSBERICHT.md`: Preflight-Metadaten gegen Originalbindungen, Reentry und Reuse-Verwaltungszeit. Überlappende Testzahlen nicht addieren |
| E-TH20-2912 | `~/Reports/thesis20-restabschluss-20260930/ABSCHLUSSBERICHT.txt`: Harness-/Referenzrefresh, Full-Run-ID, Vendor-Nachbindung, vollständige Restagerollen, zweimal 222/222 Artefakt-only. Keine damalige produktive Messung und kein Commit/Push |
| E-TH20-GENERATE-REENTRY | `~/Reports/thesis20-generate-reentry-20260930/ABSCHLUSSBERICHT.txt`: tatsächliche Writerdifferenzen, attemptlokale Reuseentscheidung, integrierter Wiedereintritt und produktiver tmux-Start 30.09. 23:08:51. Startbericht ist kein Kampagnenabschluss |
| E-TH20-ENERGY-REENTRY | `~/Reports/thesis20-energy-reentry-20261001/ABSCHLUSSBERICHT.txt` (`ABSCHLUSSBERICHT(2).txt` im Chat): enger Nullstart-Previous-Results-Fix, 28 integrierte Abnahmekriterien, 638 Artefaktbindungen/234 Attestierungen, produktiver Start 01.10. 09:21:51 und erstes gültiges Replikat. Letzter dokumentierter lokaler Stand 2.91.2 mit uncommitteter Folgearbeit, kein Commit/Push/Tagwechsel |
| E-TH20-FOLLOWUP | `AUFTRAG_LOKALE_AUSWERTUNGSKORREKTUREN.md` aus dem Auditpaket: zunächst lokale F01–F06-/W01–W03-Nacharbeit, keine produktive Fortsetzung und keine neuen Hardware-/Compiler-/Collectorstarts. Noch kein Erfüllungsbeleg |
| E-TH20-KB-UPDATE | Nutzerauftrag vom 02.10.2026, den aktuellen Stand und offene Punkte in `docs/KNOWLEDGEBASE.md` fortzuschreiben. Dokumentationsänderung, keine zusätzliche wissenschaftliche Evidenz oder Freigabe neuer Messungen |
