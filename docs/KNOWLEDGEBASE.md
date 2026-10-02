# ONNX Splitpoint Tool – Knowledge Base

> **Kanonischer Pfad: `docs/KNOWLEDGEBASE.md`.** Diese Datei wird fortlaufend
> aktualisiert; ihre Historie liegt in Git. Keine neue Datei je Dokumentrevision.
> Toolversionen, Run-IDs und historische Revisionsangaben im Text bleiben erhalten,
> damit sich Befunde weiterhin dem richtigen Stand zuordnen lassen.
>
> **Evidenzstichtag dieser Fassung: 19.09.2026, R9H-Log bis 07:19:10 +02:00.**
> R9H ist damit noch nicht abschließend abgenommen. Dokumentierte Repo-/Gitstände
> sind datierte Beobachtungen vor der Veröffentlichung, keine Liveanzeige.
> Historische Verweise auf Begleitpakete sind Quellenreferenzen; nicht jedes dieser
> Pakete ist Teil dieses Repositories. Die vollständige fachliche KB bleibt erhalten;
> konkrete lokale Benutzernamen und der absolute Benutzerpfad sind abstrahiert.

## Aktueller Stand

| Feld | Maßgeblicher Arbeitsstand |
|---|---|
| Dokumentstand | **19. September 2026**; R9H-Nachweis nur bis **07:19:10 +02:00** |
| Grundlage | Vollständige REV4 vom 15.09. unverändert als historische Ausgangsdatei erhalten; wissenschaftliche Altbefunde bleiben bestehen |
<!-- KB_MERGE_CONTEXT_00 -->
abgeschlossenen R9B/R9C/R9E/R9G-Nachweise können jetzt dokumentiert und als getrenntes Evidence-Update
vorbereitet werden. R9H-Erfüllung, Sourcecheckpoint und zugehörige Schlussbelege erst nach Abschluss
und Prüfung sichern. Keine neue Reparaturrunde allein für die Knowledgebase. [E-REV5-GIT]
[E-REV5-R9G] [E-REV5-R9G-AUDIT] [E-REV5-R9H-LOG]

## Navigation

[0. Dokumentführung](#dokumentfuehrung) · [1. Methode](#methode) · [2. Fragenkatalog](#fragen) · [3. Setups](#endpunkte) · [4. Releasefortschritt bis R8](#v30) · [5. DeepX-Historie](#deepx-full) · [6. Energie](#energie) · [7. Modellqualität](#deepx-r1-r2) · [8. Cache und Abschluss](#abschluss) · [9. Historisches Complete Set](#complete-set) · [10. Historischer .4-Auftrag](#v31-plan) · [11. Historische Abnahme](#gates) · [12. Aktuelle Aufgaben](#todo) · [13. Betrieb](#betrieb) · [14. Evidenz](#ablage) · [15. Klärungen](#grenzen) · [16. Übergabe](#uebergabe) · [17. Änderungen](#aenderungen) · [18. Codex-Betrieb](#codex) · [19. GUI-Teststandard](#gui-tests) · [20. Nachtauswertung/Plausibilität](#nacht-audit) · [21. R9A–H und aktuelle Grenzen](#r9fortschritt) · [Quellen](#quellen)

<a id="dokumentfuehrung"></a>
## 0. Dokumentführung und Quellenrang

REV5 schreibt die vollständige REV4 fort. Aktuelle Aufgaben stehen nur in §12, die aktuelle
Übergabe in §16 und die Fortschreibung nach R8 in §21. Methoden und historische Befunde in §§1–11
bleiben erhalten; spätere Ergebnisse erweitern deren Scope, sie schreiben keine Originalmessung um.
Die früheren .4-, R8- und Ein-Runden-Startanweisungen sind keine erneut auszuführenden Aufträge.

Primäre Ergebnisdateien haben Vorrang vor Reviews und Konsolen-/Chattext. Ein Auftrag belegt nur
Anforderungen, eine Sourceprüfung nur Sourceintegrität. Implementiert, normale Konfiguration,
lokal getestet, reale GUI-/Hardwareabnahme und wissenschaftliche Vergleichbarkeit bleiben getrennt.
Die bisherigen vier Abnahmeachsen gelten weiter. Testmengen verschiedener Runden sind überlappend
und dürfen nicht zu einer Gesamtzahl addiert werden.

Die Revision konsolidiert vorliegende Originalberichte und bereits ausgeführte Gegenprüfungen.
Sie zählt ausgewählte archivierte JUnit-Dateien neu, exportiert vorhandene reviewed Tabellen als
CSV und prüft Dokument-/Patchintegrität. Keine neue Produkttestsuite, Inferenz, GUI-, Energie-
oder Compileraktion. Roh-Parquets wurden auch in der R9G-Endprüfung nicht neu integriert.
Die Git-Abfragen betreffen nur veröffentlichte Repositorymetadaten, nicht Smartmirror2s Dateisystem.

**Evidenzstichtag:** R9H eval_02 ist im gelieferten Log laufend, nicht hier live beobachtet.
`host.log` ist der erste Versuch; `BEFUNDE_FUER_CODEX(1).json` beschreibt R9G-Vorfehler.
Weder Datei noch zeitlicher Abstand beweisen den Abschluss des zweiten Versuchs. Source, Liveprofile,
Venv, AGENTS.md, Manifeste und Caches während dieser Arbeit unangetastet lassen. [E-REV5-R9H-LOG]

### 0.1 Quellenstatus des vorherigen REV2-Abgleichs – historisch übernommen
<!-- KB_MERGE_CONTEXT_01 -->
| G6 | Nur ein tatsächlich noch benötigter vorab bestätigter H8-MISS, z.B. YOLO11l b064: gespeicherter Kontext bis ins reale Compilerkind, danach Reuse |

G5 verwendet den bestehenden Erwartungs-/Admissionpfad; ein unerwarteter MISS wird sichtbar, statt die kurze Runde heimlich in einen langen Build zu verwandeln. Nicht global `cache_verify_only` setzen, weil dann der normale Referenzpfad fehlt. Wenn G6 bereits warm ist, bleibt „aktueller normaler Kaltbuild nicht beobachtet“ ein benannter Scope; es wird kein vorhandenes HEF gelöscht oder per Force neu gebaut. Weitere wissenschaftliche Final-/Energieaufträge sind keine versteckten Voraussetzungen für Software-PASS. [E-2804-PLAN, §9]

<a id="todo"></a>
## 12. Einzige aktuelle Aufgabenliste – R9G-Endprüfung / R9H-Zwischenstand

Stand: 19.09.2026; R9H-Snapshot 07:19:10 +02:00. IDs aus R8 und den Folgeaufträgen bleiben erhalten;
neue Unterpunkte trennen frühere Erfolge von später neu gefundenen Integrationslücken. Dies ist
eine Dokumentlieferung, keine Aktualisierung der laufenden `docs/ARBEITSSTAND.md` auf Smartmirror2.
Ein historischer PASS bleibt auf seinen tatsächlichen Umfang beschränkt. [E-REV5-R9G-AUDIT]

### 12.1 Im belegten Umfang abgeschlossen / nicht wieder aufrollen

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

### 12.2 R9H-Ergebnis abwarten und gezielt schließen

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

### 12.3 Bekannte Grenzen / zurückgestellte Auswertung

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

<a id="betrieb"></a>
## 13. Betriebsregeln

**Fortgeltende Schutzregeln; die ausdrücklich genannten .4-Grenzen sind historisch:** GUI und laufende Workflows vor dem Update geordnet beenden. Der Installer erhält Tool-/Vendor-Venvs, Benutzerprofile, Run-Mode-/Hardware-Registry, vorhandene Overlays, Modell-/Qualitycache und Originalruns. Das Manifestfeld wird erst durch eine explizite Nutzeraktion ausgewählt. Kein Treiber-, System-CUDA-, DFC-, TensorFlow-, Torch- oder DeepX-Upgrade in v2.80.4.

`relaxed` bleibt auch für Final der vereinbarte Repro-/Cachemodus. Hailo balanced/Opt1/B500/Batch8, DeepX EMA/Opt0/B500, ImageNet-Mean/Std, Qualitätsmargen, Seed, AP-/Top-k-Definitionen und Bootstrapmethode bleiben gleich. Der vorgeschaltete Standarddurchlauf und der separate Finalumfang dürfen beim Resume nicht als identischer Run mit verändertem Profil vermischt werden.

Generische Energie bleibt aus. Native-Energie ist ein eigener Scope; Dauer und Replikate werden nicht still geändert. Vorhandene alte Fehlermeldungen oder PIDs sind keine aktuellen Betriebszustände. Primärfehler, erwartete Nichtrealisierbarkeit, technische Ausführung, Qualitätsentscheid und Cleanup werden separat gelesen.

### 13.0 Aktueller Betrieb während R9H

R9H arbeitet mit dem normalen Sourcebaum und den vorhandenen Vendorumgebungen. Solange Workflow
oder Supervisor noch aktiv sind, keine Source-/Profil-/Venv-/Collector-/Registry-/Manifeständerungen,
keine Cachelöschung und keine zusätzliche Hardwarerunde. Die jetzige KB-/Evidencevorbereitung findet
außerhalb des Hosts statt. Git-Dokumentation ist kein Anlass, den laufenden Arbeitsbaum anzufassen.
<!-- KB_MERGE_CONTEXT_02 -->
| „Ein Papervergleich mit97 FPS gilt auch für Full oder b044.“ | Nur bei übereinstimmendem b066-Graphschnitt und Messvertrag; sonst getrennte deskriptive Werte. |

<a id="uebergabe"></a>
## 16. Kompakte Übergabe – maßgeblich für die nächste Sitzung

**Stand:** v2.83, Runheader weiter `v2.83-r9b-request-latency`; R9G erfolgreich im technischen
1-Split-Umfang, aber nachgewiesene Energie-/Vergleichs-/Projektrestfehler. R9H eval_02 ab 06:43:23,
letzter hier vorliegender Eintrag 07:19:10 am 19.09.2026. Keine Endfreigabe und keine spätere
Livebeobachtung behaupten. `host.log` gehört eval_01, alte BEFUNDE-Datei R9G. [E-REV5-R9H-LOG]

<!-- KB_MERGE_CONTEXT_03 -->

**Git:** Ergebnisrepo live noch12.09. / 5636017; Source-Branches nur main/ef44c94 und Baseline/c5eb66e.
REV5+Evidencepatch vorbereitet, nichts gepusht. Während R9H keine Source-/Manifeständerung;
nach Supervisorende aktuellen Source- und Ergebnisstand getrennt und überprüfbar sichern.

<a id="aenderungen"></a>
## 17. Änderungsprotokoll

### 19. September 2026 – REV5: R9A–G, Energie-Endprüfung und R9H-Snapshot

Aktuelle Kopf-, Aufgaben-, Betriebs- und Übergabeabschnitte ersetzen die alten R8-Gegenwartsaussagen.
Wissenschaftliche Altabschnitte und Messwerte bleiben erhalten. Ergänzt: tatsächliche GUI-/Host-
<!-- KB_MERGE_CONTEXT_04 -->
Eine gemeinsame Falltabelle pro Modell/Boundary/Setup/Backend/Precision/Endpoint mit getrennten Spalten für Runtime, Outputvertrag, Quality, Wiederholungen/FPS, Energie-Replikate/J/W/J-pro-Frame, Cleanup, Artefaktbindung und Vergleichseignung. Technisch gültige Fälle nicht wegen eines fremden Fehlers unsichtbar machen; negative Werte nicht beschönigen.

Abschließend §12 mit **belegt abgeschlossen**, **offen wegen genauer Evidenzlücke**, **gezielter Reparaturverdacht** oder **korrektes negatives Ergebnis** fortschreiben. Bei Auffälligkeit zuerst vorhandene Logs/Outputs prüfen; nur den kleinsten benötigten Zusatztest formulieren. Kein großer Neulauf allein zur Beruhigung und keine Änderung des gerade laufenden Quellenbestands. [E-NIGHT-R8-USER]

<a id="r9fortschritt"></a>
## 21. Fortschreibung R9A–H und aktuelle Mess-/Aussagegrenzen

### 21.1 Entwicklungsfolge – unterschiedliche Belege nicht zusammenzählen

| Runde | Erreicht | Grenze |
|---|---|---|
<!-- KB_MERGE_CONTEXT_05 -->
Negative Compiler-/Outputbelege bleiben ausdrücklich diagnostic. Bereinigte öffentliche Kopien
benennen die Originalquelle und Redaktionen; eine Dokumentrevision ist kein neuer Hardware-PASS.
Nach R9H-Abschluss kommen dessen kurze Bilanz, aktive Eingabeverträge, tatsächliche Workloads,
Energie- und Latenzreplikate, finaler Source-/Test-/Installedstand und gegengeprüfte Restgrenzen dazu.
Kein `final`-/Release-Tag allein aufgrund eines laufenden Standard-Integrationslogs. [E-REV5-GIT]

<a id="quellen"></a>
## Quellen- und Fundstellenverzeichnis

Die Kennungen verweisen auf vorhandene Dateien beziehungsweise klar benannte Chatbeobachtungen. Innerhalb von ZIPs sind die angegebenen Pfade relativ zur Archivwurzel. Frühere KB-Begleitpakete enthalten die dort benannten Dokumente und read-only Projektionen. Das damalige REV3-Begleitpaket enthielt ausschließlich die aktualisierte KB, Änderungsnotiz, Textdiff und Dokumentprüfbericht, **nicht** die früheren Ergebnisarchive, Modelle oder erneut ausgeführte Projektionen.
<!-- KB_MERGE_CONTEXT_06 -->

Die zusätzliche öffentliche Auswahl liegt im Evidence-Patch unter docs/V283_STATUS_2026-09-19.md,
results/acceptance/v2.83/, results/evaluation/r9g_eval_20260918_171131/ und
diagnostics/v2.83_h10_output/. Die vollständige, um lokale Benutzerangaben bereinigte KB wird hier unter `docs/KNOWLEDGEBASE.md` gepflegt. Alte Quellenverweise
bleiben Referenzen auf die bisherigen Belegpakete; diese Lieferung dupliziert sie nicht vollständig.
