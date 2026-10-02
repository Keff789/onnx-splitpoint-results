# ONNX Splitpoint Tool – Knowledge Base

> **Kanonischer Pfad: `docs/KNOWLEDGEBASE.md`.** Diese Datei wird fortlaufend
> aktualisiert; ihre Historie liegt in Git. Keine neue Datei je Dokumentrevision.
> Toolversionen, Run-IDs und historische Revisionsangaben im Text bleiben erhalten,
> damit sich Befunde weiterhin dem richtigen Stand zuordnen lassen.
>
> **Evidenzstichtag: 02.10.2026, THESIS20-Abschluss und Ergebnis-Audit.**
> Die planmäßige Erhebung ist abgeschlossen; die wissenschaftliche Auswertung
> und Vergleichsfreigabe sind noch nicht abgeschlossen. Aktuelle Aufgaben stehen
> ausschließlich in §12, die Übergabe in §16 und die neuen Befunde in §22.
> Frühere R9H-/Resume-/Startanweisungen sind datierte Historie, kein neuer Auftrag.
> Historische Quellenpakete und das private Abschlussarchiv liegen nicht automatisch
> in diesem Repository. Lokale Benutzerpfade bleiben abstrahiert.

## Aktueller Stand

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

<details>
<summary>Historischer Kopfstand vom 19.09.2026 – unverändert als damaliger Nachweis</summary>

| Feld | Maßgeblicher Arbeitsstand |
|---|---|
| Dokumentstand | **19. September 2026**; R9H-Nachweis nur bis **07:19:10 +02:00** |
| Grundlage | Vollständige REV4 vom 15.09. unverändert als historische Ausgangsdatei erhalten; wissenschaftliche Altbefunde bleiben bestehen |
<!-- KB_MERGE_CONTEXT_00 -->
abgeschlossenen R9B/R9C/R9E/R9G-Nachweise können jetzt dokumentiert und als getrenntes Evidence-Update
vorbereitet werden. R9H-Erfüllung, Sourcecheckpoint und zugehörige Schlussbelege erst nach Abschluss
und Prüfung sichern. Keine neue Reparaturrunde allein für die Knowledgebase. [E-REV5-GIT]
[E-REV5-R9G] [E-REV5-R9G-AUDIT] [E-REV5-R9H-LOG]


</details>

## Navigation

[0. Dokumentführung](#dokumentfuehrung) · [1. Methode](#methode) · [2. Fragenkatalog](#fragen) · [3. Setups](#endpunkte) · [4. Releasefortschritt bis R8](#v30) · [5. DeepX-Historie](#deepx-full) · [6. Energie](#energie) · [7. Modellqualität](#deepx-r1-r2) · [8. Cache und Abschluss](#abschluss) · [9. Historisches Complete Set](#complete-set) · [10. Historischer .4-Auftrag](#v31-plan) · [11. Historische Abnahme](#gates) · [12. Aktuelle Aufgaben](#todo) · [13. Betrieb](#betrieb) · [14. Evidenz](#ablage) · [15. Klärungen](#grenzen) · [16. Übergabe](#uebergabe) · [17. Änderungen](#aenderungen) · [18. Codex-Betrieb](#codex) · [19. GUI-Teststandard](#gui-tests) · [20. Nachtauswertung/Plausibilität](#nacht-audit) · [21. Historie R9A–H](#r9fortschritt) · [22. THESIS20-Abschluss/Audit](#thesis20-audit) · [Quellen](#quellen)

<a id="dokumentfuehrung"></a>
## 0. Dokumentführung und Quellenrang

Diese Fassung führt die kanonische Knowledgebase einschließlich der REV5-Historie fort.
Aktuelle Aufgaben stehen nur in §12, die aktuelle Übergabe in §16, die historischen R9A–H-
Nachweise in §21 und der THESIS20-Abschluss samt Audit in §22. Methoden und historische
Befunde bleiben erhalten; spätere Ergebnisse schreiben keine Originalmessung um. Frühere
.4-, R8-, R9H- und THESIS20-Fortsetzungsanweisungen sind keine erneut auszuführenden Aufträge.

**Quellenstatus dieses Dokumentupdates:** bestehende Git-Fassung und gelieferter THESIS20-
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
<!-- KB_MERGE_CONTEXT_01 -->
| G6 | Nur ein tatsächlich noch benötigter vorab bestätigter H8-MISS, z.B. YOLO11l b064: gespeicherter Kontext bis ins reale Compilerkind, danach Reuse |

G5 verwendet den bestehenden Erwartungs-/Admissionpfad; ein unerwarteter MISS wird sichtbar, statt die kurze Runde heimlich in einen langen Build zu verwandeln. Nicht global `cache_verify_only` setzen, weil dann der normale Referenzpfad fehlt. Wenn G6 bereits warm ist, bleibt „aktueller normaler Kaltbuild nicht beobachtet“ ein benannter Scope; es wird kein vorhandenes HEF gelöscht oder per Force neu gebaut. Weitere wissenschaftliche Final-/Energieaufträge sind keine versteckten Voraussetzungen für Software-PASS. [E-2804-PLAN, §9]

<a id="todo"></a>
## 12. Einzige aktuelle Aufgabenliste – THESIS20-Ergebnisaudit, 02.10.2026

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

### 13.0 Aktueller Betrieb nach THESIS20-Abschluss

Keine erneute Kampagnenfortsetzung allein für F01–F06. Lokale Reader-/Reporter-/Validator-
Nacharbeit erfolgt getrennt von Primärmessungen. Originalrun, Caches und Quellenbelege erhalten;
keine manuelle Gatefreigabe, keine neue Hasharchitektur und keine automatische Messschleife.
Ein eventueller kleiner Zusatzmessplan wird erst nach §12/F04 beziehungsweise nach konkreter
Evidenzlücke gesondert entschieden. Dieses Dokumentupdate ändert keine Hostdateien. [E-TH20-FOLLOWUP]

### 13.0a Historischer Betrieb während R9H (19.09.2026)

R9H arbeitet mit dem normalen Sourcebaum und den vorhandenen Vendorumgebungen. Solange Workflow
oder Supervisor noch aktiv sind, keine Source-/Profil-/Venv-/Collector-/Registry-/Manifeständerungen,
keine Cachelöschung und keine zusätzliche Hardwarerunde. Die jetzige KB-/Evidencevorbereitung findet
außerhalb des Hosts statt. Git-Dokumentation ist kein Anlass, den laufenden Arbeitsbaum anzufassen.
<!-- KB_MERGE_CONTEXT_02 -->
| „Ein Papervergleich mit97 FPS gilt auch für Full oder b044.“ | Nur bei übereinstimmendem b066-Graphschnitt und Messvertrag; sonst getrennte deskriptive Werte. |

<a id="uebergabe"></a>
## 16. Kompakte Übergabe – maßgeblich für die nächste Sitzung

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

<details>
<summary>Vorherige Übergabe (19.09.2026), nur historische Quellenzuordnung</summary>

### Historische Übergabe vom 19.09.2026 – damaliger R9H-Snapshot

**Stand:** v2.83, Runheader weiter `v2.83-r9b-request-latency`; R9G erfolgreich im technischen
1-Split-Umfang, aber nachgewiesene Energie-/Vergleichs-/Projektrestfehler. R9H eval_02 ab 06:43:23,
letzter hier vorliegender Eintrag 07:19:10 am 19.09.2026. Keine Endfreigabe und keine spätere
Livebeobachtung behaupten. `host.log` gehört eval_01, alte BEFUNDE-Datei R9G. [E-REV5-R9H-LOG]

<!-- KB_MERGE_CONTEXT_03 -->

**Git:** Ergebnisrepo live noch12.09. / 5636017; Source-Branches nur main/ef44c94 und Baseline/c5eb66e.
REV5+Evidencepatch vorbereitet, nichts gepusht. Während R9H keine Source-/Manifeständerung;
nach Supervisorende aktuellen Source- und Ergebnisstand getrennt und überprüfbar sichern.


</details>

<a id="aenderungen"></a>
## 17. Änderungsprotokoll

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
<!-- KB_MERGE_CONTEXT_04 -->
Eine gemeinsame Falltabelle pro Modell/Boundary/Setup/Backend/Precision/Endpoint mit getrennten Spalten für Runtime, Outputvertrag, Quality, Wiederholungen/FPS, Energie-Replikate/J/W/J-pro-Frame, Cleanup, Artefaktbindung und Vergleichseignung. Technisch gültige Fälle nicht wegen eines fremden Fehlers unsichtbar machen; negative Werte nicht beschönigen.

Abschließend §12 mit **belegt abgeschlossen**, **offen wegen genauer Evidenzlücke**, **gezielter Reparaturverdacht** oder **korrektes negatives Ergebnis** fortschreiben. Bei Auffälligkeit zuerst vorhandene Logs/Outputs prüfen; nur den kleinsten benötigten Zusatztest formulieren. Kein großer Neulauf allein zur Beruhigung und keine Änderung des gerade laufenden Quellenbestands. [E-NIGHT-R8-USER]

<a id="r9fortschritt"></a>
## 21. Historische Fortschreibung R9A–H und damalige Mess-/Aussagegrenzen

**Datierter Stand vom 19.09.2026.** Die aktuelle THESIS20-Bilanz steht in §22;
diese historischen Scopegrenzen werden weder gelöscht noch als aktueller Neustartauftrag verwendet.

### 21.1 Entwicklungsfolge – unterschiedliche Belege nicht zusammenzählen

| Runde | Erreicht | Grenze |
|---|---|---|
<!-- KB_MERGE_CONTEXT_05 -->
Negative Compiler-/Outputbelege bleiben ausdrücklich diagnostic. Bereinigte öffentliche Kopien
benennen die Originalquelle und Redaktionen; eine Dokumentrevision ist kein neuer Hardware-PASS.
Nach R9H-Abschluss kommen dessen kurze Bilanz, aktive Eingabeverträge, tatsächliche Workloads,
Energie- und Latenzreplikate, finaler Source-/Test-/Installedstand und gegengeprüfte Restgrenzen dazu.
Kein `final`-/Release-Tag allein aufgrund eines laufenden Standard-Integrationslogs. [E-REV5-GIT]

<a id="thesis20-audit"></a>
## 22. THESIS20: abgeschlossene Erhebung und noch offene Auswertung

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

<a id="quellen"></a>
## Quellen- und Fundstellenverzeichnis

Die Kennungen verweisen auf vorhandene Dateien beziehungsweise klar benannte Chatbeobachtungen. Innerhalb von ZIPs sind die angegebenen Pfade relativ zur Archivwurzel. Frühere KB-Begleitpakete enthalten die dort benannten Dokumente und read-only Projektionen. Das damalige REV3-Begleitpaket enthielt ausschließlich die aktualisierte KB, Änderungsnotiz, Textdiff und Dokumentprüfbericht, **nicht** die früheren Ergebnisarchive, Modelle oder erneut ausgeführte Projektionen.
<!-- KB_MERGE_CONTEXT_06 -->

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
