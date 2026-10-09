---
title: "Energy Paper – IEEE TIM Planning & Knowledge Base"
project: "How Fast Is Fast Enough? Reference-Calibrated Energy Measurement for Edge-AI Inference"
status_date: "2026-09-30"
knowledgebase_version: "2026-09-30.1"
baseline_status_date: "2026-08-27"
update_scope: "Vollständige Offline-Neuauswertung, exakte Lastfenstermethode, Folgefälle, Ergebnis-/Messpfad-Plotnachlauf und Git-Evidence"
pause_test_tool: "jetson_pause_test_20260928_v1"
pause_test_status: "hardware_execution_complete_export_reviewed_mechanism_unresolved"
validation_tool: "pico_validation_v1.0.0-rc1"
validation_status: "software_release_candidate_hardware_acceptance_pending"
external_guidelines_last_checked_in_baseline: "2026-08-27"
preferred_journal: "IEEE Transactions on Instrumentation and Measurement"
workshop_precursor: "PARMA-DITAM 2027 / OASIcs"
canonical_workshop_paper: "How_Fast_Is_Fast_Enough_PARMA_DITAM_ResNet_IdleAware_v0.9"
canonical_analysis_tool: "common_reference_psd_tool_v0.7.3"
result_plot_tool: "tim_result_plot_post_v0.3.0"
result_plot_status: "results_only_review_generated_locally_not_Twix_deployed"
language: "de"
---

# Energy Paper – IEEE TIM Planning & Knowledge Base

## 0. Verwendung und aktueller Anschlussauftrag – 30.09.2026

Diese **vollständige** Fassung setzt die KB vom 29.09. fort. Kapitel 1–42 bleiben byteidentisch als historisch datierte Grundlage erhalten; aktuelle Ergänzungen stehen in 43–46. Frühere Pending-Angaben zu Sicherung, Vollbatch oder Pausentest sind dadurch überholt, nicht erneut auszuführen.

> Verwende diese KB als Projektgrundlage. Die große Messkampagne bleibt erhalten und wird nicht wiederholt. Vollbatch v0.2.0 und gezielter Folgeexport sind abgeschlossen. Die Lastfenstermethode in Kapitel 44 ist eine deterministische Offline-Auswertung, keine Erfassungssteuerung. Kevin bestätigt Aufnahme vor dem Benchmark und ungefähr zehn Sekunden Nachlauf; daraus keinen exakten universellen Zuschnitt ableiten. Ergebnis-/Plotnachlauf v0.3.0 liest nur den vollständigen Ergebnisexport, erbt Parent-Flags, behandelt die acht geprüften terminalen Telemetriezeilen als abgeleitete Präfixe und hält LLM-/Hailo-Fragen offen. Messpfadvergleiche sind run-gepaart mit eigenen Fenstern; keine synchrone isolierte Gerätegenauigkeit behaupten. Die vollständige KB/operativen Pfade bleiben privat; die kompakte Methodenevidence ist auf GitHub gesichert.

### 0.1 Aktueller Status

| Gegenstand | Stand und Grenze |
|---|---|
| Große alte Messkampagne | Weiterhin verbindliche Datenbasis. Keine Wiederholung. Wenige gezielte Tests und vollständige Offline-Neuauswertung sind erlaubt. |
| Sicherung | Neue Iterations- und Pausendiagnosen nach Nutzerprotokoll auf Twix/Sprite kopiert und inhaltlich geprüft; Git-Evidence ist davon getrennt. |
| Vollbatch | 16.834 NPY-Pfade bearbeitet, 16.826 Integrationen, acht terminale Telemetrie-Zeitachsenfehler, null ausstehend. Keine Wiederholung des 4,418-TB-Scans. |
| Rechenprüfung | 16.721 Legacy-Integrale reproduziert, 105 LLM-Abweichungen separat. Alle 9.106 Pico-Pfade integriert. 209.294 Fensterzeilen und 14.075 ursprüngliche Gruppen geprüft. |
| Lastfenster | Vollständige implementierte Definition in Kapitel 44: energiegewichtete 100-ms-Bins, Randmediane/P95, robuste Kontrastschwelle, 0,4/0,5/0,6, ≥200 ms Aktivität, interne Pausen bleiben. Kein Dauerfit. |
| Datenaufnahme | Manuell/benchmarkgesteuert vor dem Benchmark gestartet, nach Nutzerangabe ungefähr zehn Sekunden danach beendet. Kein Nachweis exakt gleicher Vor-/Nachläufe oder Clock-Synchronisation. |
| Determinismus | 14 Cache-Spuren identisch wiederholt; drei echte Arrays je fünf Durchläufe mit identischen Grenzen, max. Summationsdifferenz ca. 2,0e-11 J. Keine universelle Unverzerrtheitsbehauptung. |
| Acht Zeitachsenfälle | Fünf unterschiedliche Arrays plus drei Spiegelkopien. Nur letzte Zeile rückwärts bei gleichem P. Eng geprüfte Präfix-Ableitungen reproduzieren Legacy-Energie. Positive Zeitlücken bleiben bestehen. |
| LLM | 105 Mismatches gehören zur ~138-s-Kohorte; 300 ~136-s-Dateien reproduzieren. Historischer Ursprung nicht abschließend geklärt. Keine Universal-/Gainkorrektur. |
| Hailo Random Pattern | Frühere kleine Bursts können von höheren Schwellen verfehlt werden; Dauerreihe mit hohem Startniveau ohne sichere Anfangsgrenze. Kein erfundener Lastbeginn. |
| Ergebnisnachlauf | `tim_result_plot_post_v0.3.0`: nur bestehende Resultate, keine neue NPY-/Parquet-Integration. Ausgaben neu, alter Cache unverändert. Parent-Flags vererbt; >1-%-Empfindlichkeit in neuen Hauptkurven ausgeschlossen, alle Kandidaten erhalten. |
| Messgerätevergleich | Pico/u.RECS/Shelly/Jetson-Telemetrie/HailoRT soweit vorhanden, gleiche Serie/Run-ID. Pro-Paar-E/P/T-Verhältnisse, danach Mediane. Eigene Sensorfenster; keine isolierte Instrumentgenauigkeit. GPU-Sweeps enthalten hier nur Pico, NVML wird nicht erfunden. |
| Git | Neuer kompakter Freeze `energy-measurement/2026-09-30-offline-windows/`, Commit `5468c175e04c91fe7484a169ad8fc90ff24112fa`. Vorheriger Freeze und ONNX-Inhalte unverändert. |
| PSD/Common Reference | Eigener Tek-/Pico-Auswertungszweig bleibt unberührt; nur konkret importierte Energie-/Fenstertabellen wären gesondert zu aktualisieren. |

### 0.2 Nicht erneut ausführen / Quellenstatus

Keine neue Sicherungsrunde als Voraussetzung, kein neuer 45er-Sweep, kein erneuter Pausentest und kein pauschaler Rohdatenbatch. Die vorhandenen Ergebnisexporte erlauben den Plotnachlauf direkt hier; ein Twix-Aufruf ist nur zur lokalen Reproduktion nötig. Konkrete neue Ergebnisse nicht mit den alten YAML-Werten oder früheren Messprotokollen vermischen. Externe Venue-Regeln werden durch dieses Dokumentationsupdate nicht neu bestätigt.

---

# 1. Projektziel

Das Projekt untersucht, wie **Abtastrate, Integrationsdauer, Workload, Messsetup, analoge Bandbreite und Messgrenze** die Genauigkeit von Energie- und Leistungsmessungen für Edge-AI-Inferenz beeinflussen.

Die Kernfrage lautet nicht:

> Welche eine Abtastrate ist allgemein richtig?

Sondern:

\[
f_{\min,E}(T,\varepsilon,w,m,b),
\]

wobei:

- \(T\): Integrationsdauer,
- \(\varepsilon\): tolerierter Energiefehler,
- \(w\): Workload,
- \(m\): Messsetup beziehungsweise Messkette,
- \(b\): physikalische Messgrenze.

Die zentrale wissenschaftliche Aussage bleibt:

> Es gibt keine universelle Mindestabtastrate. Die erforderliche Rate ist eine Funktion des Messziels, der exakten Integrationsdauer, der Fehlertoleranz, der Workloaddynamik, der analogen Messkette und der Messgrenze.

---

# 2. Publikationsstrategie

> Übernommener Planungs- und Richtlinienstand aus [Q00], 27.08.2026. Die Datierung dieser Knowledge Base auf 21.09.2026 ist keine erneute Bestätigung der folgenden Venue-Regeln, Termine oder Bearbeitungszeiten. Vor Submission erneut offiziell prüfen.

## 2.1 Workshopfassung

**Venue:** PARMA-DITAM 2027, OASIcs  
**Workshop:** 18. Januar 2027, Glasgow  
**Submission Deadline:** 16. November 2026, 23:59 UTC  
**Notification:** 14. Dezember 2026  
**Camera Ready:** 7. Januar 2027  
**Format:** OASIcs, maximal zehn einspaltige Seiten ohne Titelseite und Literatur, Double Blind

Aktueller kanonischer Workshopstand:

```text
How_Fast_Is_Fast_Enough_PARMA_DITAM_ResNet_IdleAware_v0.9
```

Die Workshopfassung ist bewusst fokussiert auf:

- Jetson Orin NX auf u.RECS,
- vier Workloads,
- Common Reference,
- Rate-Duration-Matrix,
- PSD/Idle/Last,
- Tektronix-/PicoScope-Validierung,
- praktische 2-kS/s-Aussage.

Hailo-10 und x86 sollen nur dann in die Workshopfassung aufgenommen werden, wenn sie vor dem Freeze vollständig und methodisch sauber vorliegen. Sie sind **keine Voraussetzung** für die derzeitige PARMA-DITAM-Fassung.

## 2.2 Journalfassung

**Bevorzugtes Journal:** IEEE Transactions on Instrumentation and Measurement (TIM)

TIM passt fachlich, weil der Beitrag im Kern eine neue beziehungsweise erweiterte Methodik zur:

- Auswahl einer Messrate,
- Validierung von Messsetups,
- Verarbeitung und Darstellung zeitabhängiger Messsignale,
- Analyse von Messbandbreite und Messgrenzen,
- Erkennung systematischer Messfehler,
- reproduzierbaren Energiecharakterisierung

liefert.

Die Journalfassung darf keine bloß längere Workshopfassung sein. Sie muss die technische Evidenzbasis wesentlich erweitern.

### Zielzeitraum

Wenn die PARMA-DITAM-Fassung akzeptiert und veröffentlicht wird, ist die saubere TIM-Einreichung **nach Abschluss des Workshops**, realistisch im Februar oder März 2027.

TIM erlaubt technisch erweiterte Proceedings-Fassungen als Regular Paper erst nach Ende der Konferenz. Dafür sind nach aktuellem Autorenleitfaden unter anderem erforderlich:

- Cover Letter mit Erklärung der Proceedings-Erweiterung,
- separate `List of Extensions`, ausschließlich mit technischen Erweiterungen,
- Kopie des Proceedings-Papers,
- Zitation des Proceedings-Papers im Journalmanuskript,
- explizite Erklärung in der Einleitung, dass das Journalpaper eine Erweiterung ist,
- Klärung von Wiederverwendungs- und Copyrightfragen.

Eine TIM-Short-Paper-Einreichung ist hierfür ungeeignet, da Short Papers keine bereits veröffentlichen Proceedings-Inhalte wiederverwenden dürfen.

### Submission-Check für TIM

- IEEE Double-Column Transactions Template
- Regular Paper mit mindestens fünf Seiten
- selbstenthaltenes, unverschlüsseltes PDF unter 20 MB
- E-Mail und ORCID für jeden Autor
- zwei präzise EDICS auswählen
- Instrumentation-&-Measurement-Neuheit bereits in Abstract und Introduction klar benennen
- Related Work gezielt im I&M-Schrifttum positionieren
- bei Proceedings-Erweiterung alle oben genannten Zusatzdateien beilegen
- nach Einreichung PDF im System ansehen und explizit freigeben
- in den ersten zwei Monaten keine Statusanfrage an TIM senden

Planungsannahme für Feedback: typischerweise einige Wochen bis zur ersten Entscheidung; für den Projektplan konservativ vier bis acht Wochen vorsehen.

---

# 3. Autoren und Administration

| Autor | ORCID | Status |
|---|---|---|
| Kevin Mika | `0009-0005-2717-5147` | Corresponding Author wahrscheinlich Kevin |
| Joris Wachsmuth | offen | institutionelle E-Mail und ORCID klären |
| Florian Porrmann | `0000-0003-2401-7862` | vollständig |
| Jens Hagemeyer | `0009-0005-9943-8081` | vollständig |

Institution:

```text
CITEC – Bielefeld University
Inspiration 1
33619 Bielefeld
Germany
```

Offen:

- Joris’ institutionelle E-Mail
- Joris’ ORCID, falls vorhanden
- finale Autorenreihenfolge für TIM bestätigen
- Verantwortlichkeiten/CReDiT-Rollen für Journalfassung festhalten
- vor Einreichung prüfen, ob gegenüber PARMA Autoren hinzukommen oder entfallen

---

# 4. Source of Truth

## 4.1 Aktuelle Reihenfolge

**Geltungsbereich:** Die folgende ursprüngliche Hierarchie betrifft die Paper-/Common-Reference-Zahlen. Für September-Audit und neue PicoScope-Software gelten zusätzlich die thematisch getrennten Quellen aus Abschnitt 31; ein ungetesteter Release Candidate ersetzt keine validierten Messartefakte.

1. Neueste validierte Analyseartefakte aus `common_reference_psd_tool_v0.7.3`
2. `multi_workload_documentation_artifacts_review(2).zip` beziehungsweise vollständiges Multi-Workload-Artefaktpaket
3. Workshoppaper `How_Fast_Is_Fast_Enough_PARMA_DITAM_ResNet_IdleAware_v0.9`
4. Scope-Ergebnisbäume und Offset-Audits, insbesondere YOLO v0.6.3+
5. finale Masterarbeit von Joris als Hardware-, Kalibrier- und Messkampagnenbasis
6. ältere Tool- und Paperstände nur zur Historie

## 4.2 Kanonische lokale Ergebnisbäume

```text
~/common_trace_analysis/
├── gemm_fp16_common_reference_psd_v3/
├── tek_scope_comparison_gemmfp32_v1/
├── tek_scope_comparison_yolofp32_v1/
├── tek_scope_comparison_gemma3_4b_v1/
├── tek_scope_comparison_resnet50_v1/
└── edge_ai_multi_workload_v1/
```

Kompaktes Übergabepaket:

```text
~/common_trace_analysis/edge_ai_multi_workload_v1/
paper_artifacts/
multi_workload_documentation_artifacts_review.zip
```

## 4.3 Aktuelles Tool

```text
common_reference_psd_tool_v0.7.3
```

Kanonische Pythonumgebung:

```text
Python 3.10.12
NumPy 1.26.4
SciPy 1.13.1
Matplotlib 3.8.4
PyYAML 6.0.2
soxr 1.1.0
pyarrow 17.0.0
```

## 4.4 Separate Validierungssoftware – neu am 21.09.2026

`pico_validation_v1.0.0-rc1` ist der ausgelieferte **Software-Teststand**, nicht der neue kanonische PSD-Analyser und noch kein hardwarevalidiertes Referenzsystem. Details in Abschnitt 29. Er benötigt keinen geänderten Rust-Pico-Fork. `common_reference_psd_tool_v0.7.3` und seine Umgebung werden durch diesen Teststand nicht ersetzt. [Q12, Q13]

---

# 5. Begriffe und zwingende Unterscheidungen

## 5.1 Setup statt Path

Nutzerseitig und im Paper verwenden:

- **Tektronix setup**
- **PicoScope/INA225 setup**
- **u.RECS setup**

`measurement chain` bleibt zulässig, wenn ausdrücklich die analoge elektrische Kette gemeint ist:

- Shunt,
- Verstärker,
- RC-Filter,
- ADC,
- interne Mittelung.

## 5.2 Common Reference versus direkte Rate-Sweeps

**Common Reference:**

- niedrigere Raten werden aus derselben physischen hochauflösenden Ausführung rekonstruiert;
- identisches Fenster;
- isoliert Sampling-, Antialias- und Sampling-grid-offset-Effekte.

**Direkte Rate-Sweeps:**

- jede Rate stammt aus einer separaten physischen Ausführung;
- enthält Run-to-run-, Temperatur-, Fenster-, Range-, Instrument- und Akquisitionseffekte;
- darf nicht als kausaler reiner Samplingvergleich interpretiert werden.

## 5.3 Sampling-grid offset statt Phase

Der zeitliche Versatz eines langsamen Abtastrasters relativ zum gleichen Signal heißt:

- `sampling-grid offset`
- `unfiltered grid-offset reconstruction`

Nicht `phase`, da dies mit elektrischer Phasenverschiebung verwechselt werden kann.

## 5.4 Energie, zeitliche Signaltreue und Protokolldauer

Drei getrennte Fragen:

1. **Run-Level-Energie:** Welche Rate genügt für ein bekanntes Integrationsfenster?
2. **Transiententreue:** Welche Rate/Bandbreite ist nötig, um die Signalform zu rekonstruieren?
3. **Benchmarkprotokoll:** Wie lange muss ein real gestarteter Benchmark laufen, bis Startup und Fixed Overhead nicht mehr dominieren?

Diese drei Anforderungen dürfen nicht zu einer einzigen „optimalen Rate“ vermischt werden.

## 5.5 PSD-Begriffe

Welch-PSD:

```python
scipy.signal.welch(..., fs=rate_sps, scaling="density")
```

- Frequenzachse ist zyklische Frequenz \(f\) in Hz.
- DFT-Kern enthält bereits \(2\pi\).
- PSD-Einheit ist beispielsweise \(\mathrm{A^2/Hz}\) oder \(\mathrm{W^2/Hz}\).
- Es wird kein zusätzlicher kontinuierlicher Faktor \(1/(2\pi)\) oder \(1/\sqrt{2\pi}\) eingeführt.
- Die einseitige PSD-Verdopplung wird von SciPy behandelt.

Kumulative spektrale Verteilung:

\[
C(f)=\frac{\int_0^f S_{\mathrm{exc}}(\nu)\,d\nu}
{\int_0^{f_N}S_{\mathrm{exc}}(\nu)\,d\nu}.
\]

Die Ableitung nach linearer Frequenz ist die normalisierte lineare PSD:

\[
\frac{dC}{df}=\frac{S_{\mathrm{exc}}(f)}{\int_0^{f_N}S_{\mathrm{exc}}(\nu)\,d\nu}.
\]

## 5.6 Active, Idle und Additional/Excess PSD

Pro Workload:

\[
S_\mathrm{active}(f),\qquad S_\mathrm{idle}(f),
\]

\[
S_\mathrm{additional}(f)=\max(S_\mathrm{active}(f)-S_\mathrm{idle}(f),0).
\]

Die externen Idle- und Lastaufnahmen sind unabhängig. Die Zerlegung ist daher **deskriptiv**, nicht phasenkoherent und nicht kausal.

Zulässige Aussage:

> In diesem Frequenzbereich wurde unter Last zusätzliche Varianz gegenüber Idle beobachtet.

Nicht zulässig:

> Dieser Peak stammt zweifelsfrei von einem bestimmten Layer, Token oder Schaltregler.

## 5.7 Bedeutung von \(f_{95}\) und \(f_{99}\)

- \(f_{95}\): 95 % der workloadbezogenen Varianz liegen darunter.
- \(f_{99}\): 99 % der workloadbezogenen Varianz liegen darunter.
- Es handelt sich nicht um 95/99 % der verbrauchten elektrischen Energie.

## 5.8 Vorgegebene Arbeit versus zeitgesteuerter Abbruch – bestätigt am 21.09.2026

Kevin hat das historische Protokoll geklärt: Die **Samplerate-Sweeps waren iterationsbasiert**; die **Dauerreihen wurden nach einer festgelegten Zeit abgebrochen**. Die genauen effektiven `trtexec`-Optionen, Warm-up-Anteile und tatsächlich abgeschlossene Arbeit sind damit nicht rückwirkend für jeden Lauf belegt. [U01]

Bei vorgegebener Arbeit darf die Ausführungsdauer variieren. Gesamtenergie, `E / ausgegebene Sollzeit`, Leistung über die integrierte Sample-Zeitspanne und Innenleistung sind unterschiedliche Größen. Ein kürzerer realer Lauf ist nicht automatisch ein Messfehler. Eine vom Benchmark gemeldete abgeschlossene Arbeit muss von einer Kommandozeilen-Vorgabe getrennt bleiben; Energie pro Inferenz darf nicht blind durch angeforderte Iterationen berechnet werden.

## 5.9 Getrennte Zeitachsen und Statusbegriffe

Treiberseitig **zugewiesenes Intervall** ist nicht unabhängig kalibrierter ADC-Takt. Samplezeit, Recorder-Hostzeit, Zielrechner-Prozesszeit und UTC-Protokollzeit sind nicht ohne Synchronisationsnachweis gleichzusetzen. Eine erkannte Signalhülle ist kein garantierter Kernel-/Inferenzmarker. `overflow` im Pico-Callback bezeichnet Eingangsübersteuerung, nicht allgemein verlorene Transportdaten. [Q03, Q12]

Softwaretest-PASS, vollständig geschriebener Datensatz und metrologische/hardwareseitige Validierung sind getrennte Nachweisstufen. Gleiche Laufnummern an verschiedenen Raten sind keine kontrolliert gepaarten Versuche. [Q09, Q13]

---

# 6. Messsetups und aktuelle Plattform

## 6.1 Jetson/u.RECS

- NVIDIA Jetson Orin NX 16 GB
- u.RECS-Plattform
- Linux for Tegra 36.4.7
- JetPack 6.2.1
- MAXN-SUPER
- feste maximale Clocks
- Laborversorgung bei 19 V

## 6.2 PicoScope/INA225-Setup

- 20-mΩ-Shunt
- INA225
- bis 5 MS/s Acquisition
- differenzielle Strommesskette ungefähr 77 kHz Bandbreite
- Spannungs-/Strompfad für Jetson im bestehenden Projekt bereits verifiziert

## 6.3 u.RECS-Setup

- vergleichbare Shunt-/Filter-/INA225-Kette
- ADS7953, 12 Bit
- 2 kS/s
- der verifizierte Jetson-Spannungspfad gilt als ausreichende Grundlage

## 6.4 Tektronix-Setup

- breitbandige Stromzange als Referenzsetup
- Messraten bis 250 MS/s
- bei Raten über 5 MS/s bleibt das PicoScope bei 5 MS/s
- physikalische Aufnahmedauern werden zwischen Tektronix und PicoScope angeglichen

## 6.5 Messgrenzen

Für TIM müssen Messgrenzen explizit getrennt werden:

- Accelerator-/Rail-only
- Modulinput
- Host + Accelerator
- vollständiges System/DC
- AC/Wandmessung
- Vendor-Telemetrie

Unterschiede zwischen diesen Grenzen sind reale Systemanteile und keine reinen Instrumentfehler.

---

# 7. Aktuelle Jetson-Datenbasis

## 7.1 Same-Execution-Multi-Workload

Bei 5 MS/s:

| Workload | vollständige Paare |
|---|---:|
| GEMM-FP32 | 10 |
| YOLO-FP32 | 10 |
| Gemma3-4B | 10 |
| ResNet-50 FP32 | 9 |

Gesamt: 39 physische 5-MS/s-Paare.

## 7.2 Externe Idle-Basis

- 11 unabhängige Idle-Aufnahmen
- je 10 s
- insgesamt 110 s
- insgesamt 1.034 Welch-Segmente
- eine PSD pro physischem Run
- gleicher Run-Gewichtungsfaktor unabhängig von der Aufnahmezeit

## 7.3 Langzeitanker

- GEMM-FP16
- 13 beibehaltene hochaufgelöste Runs
- 104-s-Aktivfenster
- separate Protokolldauerstudie mit 15 Wiederholungen und 5–600 s

**Audit-Hinweis 21.09.:** Die Angabe „13 beibehaltene Runs“ stammt aus [Q00]. Beim alten Samplerate-Plotter wurde inzwischen eine 15→13-Trimmregel nachgewiesen (Abschnitt 27). Ob die Selektion des kanonischen Common-Reference-Langzeitankers dieselbe Herkunft hat, ist hier **nicht geprüft**. Provenienz und Selektionsregel vor dem nächsten Paper-Freeze kontrollieren; nicht allein wegen der gleichen Zahl 13 verwerfen oder neu bewerten.

---

# 8. Kanonische aktuelle Ergebnisse

> Unverändert übernommene numerische Basis aus [Q00]. Der September-Gegencheck betrifft andere bzw. gesondert ausgewiesene historische direkte Sweeps und deren Auswertungs-/Darstellungskette. Die folgenden Common-Reference-Zahlen wurden dabei nicht erneut aus ihren Primärartefakten berechnet.

## 8.1 2-kS/s-Rate-Duration-Ergebnis

Über alle vier Workloads und beide Messsetups:

- 1-%-Kriterium ab 1 s exakt begrenztem Fenster
- 0,5-%-Kriterium ab 5 s exakt begrenztem Fenster

Bei 100 ms steigt die konservative 1-%-Anforderung auf:

- 80 kS/s für das breitbandigere Tektronix-Setup
- 16 kS/s für das gefilterte PicoScope/INA225-Setup

Langzeitanker GEMM-FP16:

- 2 kS/s, 2 s: 0,761 %
- 2 kS/s, 5 s: 0,455 %
- 2 kS/s, 104 s: 0,112 %

## 8.2 Protokolldauer

Unabhängige reale Benchmarkkommandos benötigen je nach Workload ungefähr 50–200 s, um innerhalb von 3 % des 600-s-Mittelwerts zu liegen.

Das ist kein reiner Samplingeffekt, sondern enthält:

- Startup,
- Fixed Overhead,
- Timeout,
- Fenstererkennung,
- reale Run-to-run-Variation.

## 8.3 Workloadübergreifende Spektren

| Workload | \(f_{50}\) | \(f_{95}\) | \(f_{99}\) | Varianz über 77 kHz |
|---|---:|---:|---:|---:|
| GEMM-FP32 | 1,3 kHz | 374,2 kHz | 454,6 kHz | 15,24 % |
| YOLO-FP32 | 43,8 kHz | 363,5 kHz | 540,0 kHz | 37,99 % |
| Gemma3-4B | 1,6 kHz | 367,5 kHz | 645,6 kHz | 18,96 % |
| ResNet-50 FP32 | 24,5 kHz | 362,5 kHz | 514,9 kHz | 28,84 % |

Interpretation:

- GEMM und Gemma haben starke niederfrequente Anteile.
- YOLO ist am breitbandigsten und besitzt den höchsten Anteil über 77 kHz.
- ResNet liegt zwischen YOLO und den niederfrequenteren Lasten.
- Gemma besitzt den längsten hochfrequenten Restschwanz.

## 8.4 Active versus Idle

Gesamte Active/Idle-Stromvarianz:

| Workload | Active/Idle |
|---|---:|
| GEMM-FP32 | +11,42 dB |
| YOLO-FP32 | +7,75 dB |
| Gemma3-4B | +5,86 dB |
| ResNet-50 FP32 | +8,62 dB |

Weitere Aussagen:

- zwischen 100 Hz und 77 kHz liegen alle Workload-/Band-Kombinationen 21,9–41,7 dB über Idle;
- unter 100 Hz liegen YOLO und ResNet ungefähr auf Idle-Niveau;
- im Band 77–500 kHz werden Active- und Idle-Gesamtvarianzen vergleichbar: −1,34 bis +3,61 dB;
- dominante Workloadlinien stimmen dennoch nicht mit dem dominanten Idle-Liniensatz überein;
- die fünf stärksten zusätzlichen Peaks pro Workload sind bei der verwendeten Welch-Auflösung `load-only candidates`;
- dies ist deskriptiv und keine kausale Quellenzuordnung.

## 8.5 5-MS/s-Abdeckung

Für GEMM, YOLO und Gemma zeigen schnellere Tektronix-Aufnahmen:

- weniger als 0,015 % Varianz oberhalb der 2,5-MHz-Nyquist-Grenze einer 5-MS/s-Aufnahme.

Für ResNet ist diese Aussage noch nicht vollständig durch eine schnellere Serie bestätigt.

## 8.6 Direkte Rate-Sweeps versus Common Reference

Beispiel GEMM-FP32 bei 2,5 kS/s:

- direkte Tektronix-Medianabweichung zur direkten 5-MS/s-Serie: 3,483 %
- Same-Trace-Sampling-q95: 0,194 %
- direkte PicoScope-Medianabweichung: 3,424 %
- Same-Trace-Sampling-q95: 0,157 %

Schlussfolgerung:

> Mehrprozentige Trends direkter Rate-Sweeps können überwiegend aus separaten Ausführungen und Acquisition-Zuständen stammen und dürfen nicht automatisch dem Samplingintervall zugeschrieben werden.

---

# 9. Adaptive Tektronix-Nullpunktkorrektur

Bei der YOLO-Kampagne wurde eine falsch genullte Tektronix-Stromzange erkannt.

Kanonische Auditwerte:

- stabiler additiver Session-Shift: +111,917 mA auf die Tektronix-Workloadspuren
- geschätzte Unsicherheit/Rate-Streuung: 4,092 mA
- zehn Referenzraten
- 100 externe Idle-Paare
- hohe Konfidenz
- Rohwerte bleiben archiviert
- keine Gainkorrektur

Wissenschaftliche Kennzeichnung:

```text
post_hoc_workload_minus_external_idle_session_shift_not_independent
```

Nach Korrektur sinkt die rohe YOLO-Energieabweichung von ungefähr 10 % ratenweise typischerweise auf unter ungefähr 1 %.

Zwingende Regeln:

- Roh- und korrigierte Werte getrennt zeigen.
- Nie behaupten, dass die korrigierte Kampagne eine vollständig unabhängige absolute PicoScope-Validierung ist.
- Keine automatische affine Gainanpassung aus den Workloaddaten.
- Offsetkorrektur nur bei bestandenen Stabilitäts- und Sicherheitsgates.

Für TIM ist dies ein interessanter Methodenbeitrag zur automatischen Erkennung und transparenten Rettung einer fehlerhaften Messsession.

---

# 10. Entscheidung zum Unsicherheitsbudget

Projektentscheidung vom 27. August 2026:

> Kein umfangreiches neues GUM-/Monte-Carlo-Unsicherheitsbudget und keine zusätzliche breit angelegte Kalibrierkampagne.

Begründung:

- der u.RECS-Spannungspfad für Jetson wurde bereits verifiziert;
- der wissenschaftliche Kern liegt in empirischer Referenzvalidierung, Common Reference, Rate-Duration, PSD und automatischer Fehlererkennung;
- zusätzliche Messbürokratie ohne unmittelbaren Erkenntnisgewinn soll vermieden werden.

Für TIM verwenden:

- empirisch validierte Fehlergrenzen,
- beobachtete Setup-Übereinstimmung,
- Sampling-induzierte Fehlerverteilungen,
- Run-to-run-Streuung,
- Offset- und Kalibrier-Audits,
- klare Randbedingungen und Threats to Validity.

Nicht behaupten:

- vollständige GUM-Konformität,
- vollständig SI-rückführbare erweiterte Unsicherheit jedes Messpfads,
- vollständige komponentenweise Unsicherheitspropagation.

Zulässige Terminologie:

- `empirically validated error bounds`
- `observed setup agreement`
- `sampling-induced energy error`
- `run-to-run variability`
- `setup-specific calibration and validation`

---

# 11. Empfohlene TIM-Story

## 11.1 Kernframing

Vorgeschlagene Journalstory:

> Eine reference-calibrated, duration- and boundary-aware measurement methodology for heterogeneous Edge-AI accelerators, validated across an integrated edge SoC/GPU and an M.2 NPU, with optional extension to an x86/discrete-GPU/NVML setup.

Der Beitrag ist **kein reines Accelerator-Ranking**. Heterogene Plattformen dienen dazu, die Übertragbarkeit einer Messmethodik zu testen.

## 11.2 Mögliche Titel

1. **How Fast Is Fast Enough? Reference-Calibrated Energy Measurement Across Heterogeneous Edge-AI Accelerators**
2. **Sampling-Rate and Boundary-Aware Energy Measurement for Heterogeneous Edge-AI Inference**
3. **Reference-Calibrated Energy and Telemetry Validation for Edge-AI Accelerators**
4. **Measurement-Rate Selection for Heterogeneous Edge-AI Systems: From Integrated SoCs to M.2 NPUs**

Titel erst nach Hailo-Ergebnissen einfrieren.

## 11.3 Journal-Forschungsfragen

### RQ-J1 – Übertragbarkeit der Messrate

Wie verändert sich:

\[
f_{\min,E}(T,\varepsilon)
\]

zwischen:

- Jetson Orin NX,
- Hailo-10 M.2,
- optional x86/NVIDIA-dGPU?

### RQ-J2 – Messgrenze und Host-Overhead

Wie unterscheiden sich:

- Accelerator-only,
- Host-only,
- Host + Accelerator,
- Modul-/Systeminput,
- Wall Power?

Wie stark verändert die gewählte Messgrenze das Effizienzranking?

### RQ-J3 – Workload- und Plattformdynamik

Welche Frequenzprofile, Idle-/Last-Anteile und kurzen Burstmuster treten auf den verschiedenen Beschleunigerklassen auf?

### RQ-J4 – Vendor-Telemetrie

Wie gut stimmen Vendor-Telemetrie und externe Referenzmessung überein?

- Jetson: INA3221 / `tegrastats` / jtop
- Hailo: verfügbare Hailo-Counter, falls vorhanden
- x86 optional: NVML / `nvidia-smi`

### RQ-J5 – Automatische Qualitätskontrolle

Können systematische Messfehler wie Probe-Zero, fehlende Paare, Dauerabweichung, Cache-Staleness und unzureichende Welch-Segmente automatisch erkannt, gekennzeichnet und reproduzierbar behandelt werden?

---

# 12. Technische Erweiterungen gegenüber PARMA-DITAM

Diese Matrix bildet den Kern der späteren TIM-`List of Extensions`.

| Workshopbeitrag | TIM-Erweiterung |
|---|---|
| Jetson Orin NX als einzige Acceleratorplattform | Hailo-10 als zweite materielle Beschleuniger- und Messklasse |
| eine Modul-/Jetson-Messgrenze | Hailo accelerator rail, Host, Host+Accelerator und Systemgrenzen |
| vier Jetson-Workloads | gemeinsame Jetson-/Hailo-Workloads plus plattformspezifische Workloads |
| Jetson Rate-Duration-Matrix | plattformübergreifende \(f_{\min,E}(T,\varepsilon)\)-Flächen |
| Jetson PSD und Idle/Last | Hailo PSD, Burststruktur, Idle/Last und High-Rate-Abdeckung |
| Tektronix/PicoScope/u.RECS-Validierung | zusätzliche M.2-Rail-Validierung und Host-Overhead-Zerlegung |
| Jetson-Telemetrie als Vergleich | Hailo-interne Telemetrie, falls verfügbar; optional NVML |
| adaptive Tek-Zero-Salvage | generalisierte, setupübergreifende automatische Messqualitätsprüfung |
| Workshopartefakte | erweiterte Journalartefakte mit Plattform-, Boundary- und Telemetriematrix |
| kurze Discussion | umfassende Transferability- und Boundary-Analyse |

Zusätzliche technische Extensions müssen klar als **neue Daten, Methoden oder Auswertungen** nachweisbar sein; bloß mehr Erklärung reicht für TIM nicht.

---

# 13. Hailo-10 – Minimal notwendige Journalerweiterung

## 13.1 Plattform einfrieren

Vor dem Journalrun eindeutig dokumentieren:

- exaktes Hailo-10-Modul und Formfaktor,
- Hostplattform, aktuell wahrscheinlich Xavier NX + Hailo-10; vor Run bestätigen,
- Hailo Runtime/SDK/Compiler-Version,
- Betriebssystem und Kernel,
- HEF-Modellversion,
- Precision und Quantisierung,
- Power-/Performance-Mode,
- Anzahl Contexts,
- Batch/Inflight-Konfiguration,
- Kühlung und Temperaturzustand.

## 13.2 Messgrenzen

**Planungsziele aus der Ausgangs-KB, kein Vollständigkeitsnachweis bereits vorhandener Hailo-Daten.** Das September-Plotarchiv enthält keine neuen getrennten Hailo-U/I-Rohdaten und der Pico-RC implementiert keinen neuen HailoRT-Telemetriepfad.

Mindestens:

1. Hailo-Accelerator-Rail
2. Host ohne Hailo-Dynamik beziehungsweise Host-Idle
3. Host + Hailo kombiniert

Optional:

4. DC-Systeminput
5. AC-Wandinput

## 13.3 Gemeinsame Workloads

Mindestens ein zwischen Jetson und Hailo identisch definierter Workload:

- vorzugsweise YOLO,
- identische Eingangsgröße,
- identische Preprocessingdefinition,
- gleiche Datensätze beziehungsweise deterministische Inputs,
- klar getrennte Inferenz- und Postprocessinggrenzen.

Zweite gemeinsame Workloadklasse nach Möglichkeit:

- ResNet-50 oder anderes Klassifikationsmodell.

## 13.4 Betriebsarten

Für denselben Workload:

- kontinuierlicher maximaler Durchsatz,
- deterministische Burst-/Pause-Sequenz,
- optional Einzelinferenz/Event-Level.

## 13.5 Messprogramm

Pro relevanter Konfiguration:

- mehrere physische Wiederholungen,
- hochauflösende gemeinsame Referenzspur,
- 2-kS/s-/niedrige-Rate-Rekonstruktion,
- Rate-Duration-Matrix,
- Active-/Idle-PSD,
- Accelerator-only-, Host- und Combined-Energie,
- Energie pro Inferenz,
- Durchsatz,
- Wiederholbarkeit,
- Host-Overhead,
- High-Rate-Abdeckung.

## 13.6 Minimaler Hailo-Erfolg für TIM

Die TIM-Fassung ist bereits ohne x86 sinnvoll, wenn Hailo-10 liefert:

- mindestens eine saubere zweite Beschleunigerklasse,
- mindestens einen gemeinsamen Workload,
- mindestens zwei Messgrenzen,
- Common Reference und PSD,
- Host-Overhead,
- reproduzierbare Artefakte,
- klare Transferanalyse gegenüber Jetson.

---

# 14. x86/NVIDIA – optionale dritte Plattform

## 14.1 Rolle

x86 ist für TIM **optional, aber wertvoll**.

Es ergänzt:

- diskrete GPU statt SoC oder M.2-NPU,
- PCIe-Slot/PEG-Messung,
- deutlich höheren Leistungsbereich,
- NVML/`nvidia-smi` statt Jetson-Telemetrie,
- neue Messgrenzen und Update-/Mittelungseffekte.

## 14.2 Go/No-Go-Regel

x86 nur vollständig aufnehmen, wenn:

- Hailo-10 bereits stabil und ausgewertet ist,
- Messhardware für Slot-/PEG-Leistung belastbar verfügbar ist,
- das x86-Paket die Journalabgabe nicht wesentlich verzögert.

Sonst:

- x86 nur als Pilot/Discussion/Future Work,
- TIM mit Jetson + Hailo einreichen.

## 14.3 Minimaler x86-Versuch

- eine NVIDIA-dGPU,
- externe GPU-Board-Level-Messgrenze,
- NVML/`nvidia-smi` parallel,
- mindestens ein gemeinsamer YOLO- oder ResNet-Workload,
- kontinuierlich und Burst,
- zeitliche Update-/Mittelungseigenschaften von NVML,
- Energie- und PSD-Vergleich.

---

# 15. Empfohlener TIM-Paperaufbau

## I. Introduction

- Problem: Rate und Telemetrie werden ohne Messgrenze/Dauer berichtet.
- TIM/I&M-Neuheit klar benennen.
- Workshopbeitrag zitieren und Erweiterung erklären.
- Journalbeiträge präzise aufzählen.

## II. Related Work and Measurement Taxonomy

- Edge-AI-Energiemessung
- Messgrenzen
- externe versus Vendor-Telemetrie
- Sampling, interne Mittelung, Polling versus Informationsrate
- I&M-Literatur stärker als im Workshoppaper

## III. Measurement Objectives and Error Definitions

- Energieintegral
- \(f_{\min,E}(T,\varepsilon)\)
- Run-Level, Event-Level, Transiententreue
- Messgrenzen und Idlebehandlung
- empirisch validierte Fehlergrenzen statt vollem GUM-Budget

## IV. Reference-Calibrated Methodology

- Common Reference
- Anti-Alias und Grid Offsets
- hierarchische Statistik
- direkte Sweeps versus Same Trace
- PSD, kumulative Verteilung und Frequenzbänder
- Idle-/Last-Zerlegung
- adaptive Qualitätskontrollen und Offset-Salvage

## V. Systems and Measurement Setups

- Jetson/u.RECS
- Hailo-10 + Host
- optional x86/dGPU
- Messgrenzen
- Vendor-Telemetrie
- Trigger, Synchronisation, Wiederholungen

## VI. Jetson Multi-Workload Baseline

- Workshopresultate kompakt, aber vollständig
- vier Workloads
- Rate-Duration
- PSD/Idle
- direkter versus Common-Reference-Vergleich

## VII. Hailo-10 Results

- Accelerator-/Host-/Combined-Energie
- Common Reference
- Rate-Duration
- PSD und Burst
- Host-Overhead
- gemeinsamer Modellvergleich

## VIII. Cross-Platform Transferability

- \(f_{\min,E}\)-Vergleich
- Worst-Case-Hüllkurve über Plattformen
- Workload- versus Plattformabhängigkeit
- Messgrenzeneinfluss

## IX. Vendor-Telemetry Validation

- Jetson-Telemetrie
- Hailo-Counter, falls vorhanden
- optional NVML
- Updateperioden, Mittelungsfenster, Verzögerung, Bias

## X. Discussion and Threats to Validity

- empirische statt vollständiger metrologischer Unsicherheitsanalyse
- Setup-spezifische Spannungskalibrierung
- unabhängige Idle-Aufnahmen
- Offset-Salvage ist teilweise nicht unabhängig
- keine kausale Peakzuordnung ohne Marker
- Plattform- und Modellabdeckung

## XI. Conclusion

- keine universelle Rate
- praktische Entscheidungsregel
- Übertragbarkeit und Grenzen

---

# 16. Paper-Artefakte für die Journalfassung

## 16.1 Pflichtgrafiken

1. Cross-platform measurement-boundary overview
2. Jetson/Hailo rate-duration comparison
3. Platform-conservative \(f_{\min,E}\)-envelope
4. Accelerator-only versus host+accelerator energy
5. Cross-platform PSD and cumulative variance
6. Active/idle frequency-band comparison
7. Vendor telemetry versus external setup
8. Direct sweeps versus Common Reference

## 16.2 Wahrscheinliche Supplement-/Journaldetailgrafiken

- lineare PSD-Feinstruktur
- dominante Peakfamilien
- Active/Idle-PSD und Ratio
- Offset-/Zero-Audit
- per-run Scatterplots
- Common-Reference-Matrizen für mehrere Toleranzen
- High-Rate-Coverage

## 16.3 Tabellen

- Plattform- und Setupinventar
- Messgrenzen
- gemeinsame Workloadmatrix
- Rate-Duration-Sufficiency
- \(f_{50}/f_{95}/f_{99}\) und Bandanteile
- Host-Overhead
- Energy per inference / throughput / repeatability
- Telemetrieabweichung
- automatische Qualitätsflags
- List of Extensions

---

# 17. Verbindliche Arbeitsprinzipien

1. **Keine manuell eingetragenen Ergebniszahlen**, wenn sie aus Artefakten erzeugt werden können.
2. Rohdaten werden nur lesend verarbeitet.
3. Unvollständige, leere oder ungepaarte Runs werden dokumentiert und übersprungen.
4. Caches beruhen auf Quellenfingerabdrücken.
5. Direkte Rate-Sweeps und Common Reference bleiben strikt getrennt.
6. Unterschiedliche Tek-/Pico-Raten werden über gleiche physikalische Dauer verglichen.
7. Active-only- und Active-minus-Idle-Ergebnisse bleiben strukturell getrennt.
8. Workloadbezogene PSD nur mit gültiger Idle-Referenz behaupten.
9. Korrigierte Tek-Zero-Werte nie als unabhängige absolute Validierung verkaufen.
10. Keine automatische Gainkorrektur aus Workloaddaten.
11. Relative Niedrigstromfehler immer zusammen mit mA/W/J-Kontext berichten.
12. Keine kausale Peakzuordnung ohne synchrone Marker.
13. Keine Universalrate behaupten.
14. Kein umfangreiches neues GUM-/Monte-Carlo-Programm.
15. Keine neue Messbürokratie ohne direkten Beitrag zur TIM-Story.
16. Neue Plattformen mit derselben Methodik auswerten, nicht lediglich gegen alte Grenzwerte „bestehen lassen“.
17. **Neue Hauptfenster nicht auf eine geschätzte Solldauer zurechtschieben.** Legacy-Vergleiche bleiben getrennt und versioniert.
18. Vollständige qualitätsgültige Wiederholungen als Hauptstatistik; kein unmarkiertes 5.–95.-Perzentil-Trimming und kein automatisches Entfernen von Lauf 0.
19. Quellenlabels, Werte, Einheiten, Messgrenzen und Fensterdefinitionen gemeinsam anhand stabiler Schlüssel verwalten.
20. Aufnahme und schwere Offline-Analyse trennen; Versuchsreihenfolge, Pausen, tatsächliches Benchmarkkommando und Status dokumentieren.
21. Rohkanäle, exaktes zugewiesenes Intervall, Fehler und fehlgeschlagene Versuche erhalten. Softwarezähler nicht als unabhängigen Hardware-Kontinuitätsbeweis ausgeben.
22. Neue PicoScope-Validierung zunächst separat testen. Alte Rust-Installation, Treiber, Kalibrierfaktoren, Engines und Rohdaten nicht als Nebenwirkung verändern.
23. Hardwareabnahme von Joris bleibt erforderlich; synthetischer 5-MS/s-Test und Software-PASS ersetzen sie nicht.

---

# 18. Zulässige und unzulässige Claims

## Zulässig

- 2 kS/s erfüllen auf der untersuchten Jetson/u.RECS-Plattform über vier Workloads und beide Setups das hierarchische 1-%-Kriterium ab 1 s und 0,5 % ab 5 s.
- Für kurze Fenster steigen die notwendigen Raten stark und setupabhängig.
- Workloads besitzen deutlich verschiedene spektrale Verteilungen.
- 5 MS/s erfassen für GEMM, YOLO und Gemma mehr als 99,985 % der beobachteten Tektronix-Varianz unterhalb 2,5 MHz.
- Die analoge INA225-/RC-Messkette begrenzt die sichtbare Dynamik stärker als die 5-MS/s-Samplinggrenze.
- Direkte Rate-Sweeps können von Run- und Acquisition-Effekten dominiert werden.
- Ein stabiler Tektronix-Nullpunktfehler kann adaptiv erkannt und transparent korrigiert werden.

## Nur mit Limitation

- korrigierte YOLO-Tek/Pico-Übereinstimmung: post hoc und nicht vollständig unabhängig;
- Active-minus-Idle: zusätzliche Varianz, keine kausale Quellenzerlegung;
- Peakfamilien: deskriptiv, keine Zuordnung zu Tokens/Frames/Layern ohne Marker;
- ResNet >2,5-MHz-Abdeckung: noch nicht vollständig bestätigt.
- September-Pilot: 16 ausgewählte historische Spuren, nicht die vollständige Population; Innenbeschnitt verändert die Messgröße.
- Weniger FP32-Gesamtenergie bei gleichzeitig höherer Innenleistung beschreibt die geprüften Spuren, beweist aber weder kürzere reale GPU-Laufzeit noch Sampleverlust.
- Neue PicoScope-Version: softwareseitig getestet, Hardwareabnahme ausstehend; die Fehlerursache historischer Sweeps ist damit nicht abschließend geklärt.

## Nicht zulässig

- „2 kS/s sind allgemein für Edge AI ausreichend.“
- „\(f_{95}\) enthält 95 % der Energie.“
- „Die Peakfrequenz X ist sicher die Inferenzfrequenz.“
- „Tektronix bestätigt PicoScope unabhängig“, wenn der Tek-Offset aus Pico-/Idle-Daten korrigiert wurde.
- „Das Paper liefert ein vollständiges GUM-konformes Unsicherheitsbudget.“
- „Hailo ist energieeffizienter“, bevor Messgrenze, Hostanteil und Workloadvergleich sauber definiert sind.
- „Höhere Pico-Abtastrate misst grundsätzlich zu wenig Leistung“ oder ein universeller Korrekturfaktor aus den direkten Sweeps.
- „Sampleverlust ist bewiesen“ aufgrund des synthetischen −0,274-%-Gegenbeispiels oder fehlender Nullsamples.
- „Die Ursache ist sicher GPU-Abkühlung“ ohne entsprechende Zustands-/Zeitnachweise.
- „u.RECS hat bei Hailo etwa 40 % Fehler“ allein aus dem falsch beschrifteten Dauerdiagramm.
- „15 Wiederholungen in der Streuungsstatistik“, wenn tatsächlich nur 13 nach Trimming verwendet wurden.
- „Rust-Collector und SDK sind gepatcht/hardwarevalidiert“ aufgrund der separaten Python-RC-Auslieferung.

---

# 19. Priorisierte Arbeitspakete

## WP-PROTOKOLL – aktuelle Priorität 28.09.2026

- [x] Neue Chat-/SetupInfo-Angaben und Protokollunterschiede dokumentieren.
- [x] Nur lesende Auswertungshilfe und abgesicherten Legacy-Starter bereitstellen; lokale Softwarebelege erhalten.
- [ ] Auf Memmert den vorhandenen Jetson-Zeitlauf prüfen und Review-ZIP zurückgeben.
- [ ] Aktuellen Quell-/Binarystand, ursprünglichen Messaufruf, Typ/Umgebung und Timed-Skript sichern.
- [ ] Falls Bedingungen bestätigt: separaten Iterationspilot unter unveränderter Kette starten.
- [ ] Energie, Dauer, E/T, Innenfenster und Wiederholungen vergleichen; keine Kausalursache vorwegnehmen.

## WP-PICO – RC-Abnahmeplan vom 21.09.2026, weiterhin getrennt/offen

- [x] Alte Tool-Kette auditieren; Befunde von offenen Ursachen trennen.
- [x] 1.620 Ergebnis-YAMLs, 16-Spuren-Pilot und 33 Ergebnisabbildungen gegenprüfen.
- [x] Separate PicoScope-Validierung `v1.0.0-rc1` ausliefern; Software-/Releasebelege archivieren.
- [x] Hardware-Testplan und Review-Export für Joris bereitstellen.
- [ ] Übernahme/Version bei Joris bestätigen; tatsächliches Pico-Modell, Seriennummer und Messgrenze festhalten.
- [ ] U/I-Smokes bei 2 kS/s und 5 MS/s; Benchmark-Einzellauf und Abbruchtest.
- [ ] Nach bestandenen Vorprüfungen: balancierter 16-Läufe-Kontrollpilot.
- [ ] Joris’ Review-Paket prüfen; Legacy-, neue Fenster- und Same-Trace-Ergebnisse vergleichen.
- [ ] Erst danach größere Kampagne, Integration in ursprüngliche Tools oder Paperkorrekturen entscheiden.

Die folgenden WP0–WP6 bleiben der längerfristige Plan aus [Q00]; erledigte Schritte anderer Projektphasen wurden hier nicht ohne Beleg nachgetragen.

## WP0 – PARMA-DITAM einfrieren

- [ ] v0.9 intern vollständig reviewen
- [ ] Joris E-Mail/ORCID klären
- [ ] Double-Blind-Version erzeugen
- [ ] offizielle OASIcs-Metadaten aktualisieren
- [ ] Submission bis 16. November 2026
- [ ] nach Acceptance Camera Ready bis 7. Januar 2027

## WP1 – TIM-Framing und Related Work

- [ ] IEEE-TIM-Templateprojekt anlegen
- [ ] I&M-Neuheit im Abstract/Intro formulieren
- [ ] gezielte TIM-/Measurement-/I2MTC-Related-Work-Matrix erstellen
- [ ] erste `List of Extensions` als lebendes Dokument anlegen
- [ ] Titelkandidaten bewerten

## WP2 – Hailo-10-Setup einfrieren

- [ ] exaktes Modul und Host bestätigen
- [ ] Software-/Runtime-/HEF-Versionen einfrieren
- [ ] Messgrenzen dokumentieren
- [ ] gemeinsames YOLO-Modell festlegen
- [ ] optional ResNet-Modell festlegen
- [ ] kontinuierlichen und Burstmodus definieren

## WP3 – Hailo-10-Messkampagne

- [ ] Idle
- [ ] Accelerator-only
- [ ] Host-only beziehungsweise Hostbaseline
- [ ] Combined
- [ ] mehrere physische Wiederholungen
- [ ] 5-MS/s-Referenz
- [ ] Common Reference
- [ ] PSD/Idle/Last
- [ ] High-Rate-Coverage
- [ ] Energie pro Inferenz und Durchsatz

## WP4 – Cross-Platform-Analyse

- [ ] Jetson/Hailo gemeinsame Rate-Duration-Matrix
- [ ] Worst-Case-Hüllkurve
- [ ] Messgrenzenvergleich
- [ ] Host-Overhead
- [ ] Workload-/Plattform-PSD-Vergleich
- [ ] Transferability-Aussagen mit klaren Grenzen

## WP5 – x86-Go/No-Go

Entscheidung erst nach einem Hailo-Pilot:

- [ ] Messhardware verfügbar?
- [ ] NVML-Vergleich realistisch?
- [ ] gemeinsamer Workload verfügbar?
- [ ] Zeitgewinn größer als Verzögerungsrisiko?

Wenn nein: x86 als Future Work.

## WP6 – TIM-Manuskript und Artefakte

- [ ] Journaloutline schreiben
- [ ] Workshoptext nicht bloß aufblasen
- [ ] neue technische Resultate zentral platzieren
- [ ] alle Journalgrafiken automatisieren
- [ ] Supplement/Review-Bundle erzeugen
- [ ] Cover Letter vorbereiten
- [ ] List of Extensions finalisieren
- [ ] Proceedings-Paper beilegen und zitieren
- [ ] TIM Submission nach Workshopabschluss

---

# 20. Decision Gates

## Gate P – neue separate RC-PicoScope-Messreihe

Dieses Gate betrifft die in Abschnitt 29 implementierte Python/PS4000A-Kette. Es ist kein Nachweis über Joris’ bestehende Legacy-Aufnahmen. Der jetzige Protokollvergleich verwendet die Bedingungen/Startprüfungen aus Abschnitt 35; eine erfolgreiche Legacy-Serie gilt nicht als bestandenes RC-Gate.

**Noch nicht bestanden.** Geräte-/Kanalprüfung, zwei U/I-Smokes, Benchmark-Einzellauf, Fehler-/Abbruchverhalten und ausreichend freier Rohdatenspeicher müssen auf Joris’ Hardware belegt sein. `126 PASS` und `capture complete` allein genügen nicht. Ein nicht bestandener Vorprüfungsschritt stoppt den Pilot. Keine parallele Nutzung desselben PicoScope durch alte Aufnahme oder GUI. [Q12, Q13]

## Gate A – Ist Hailo ausreichend für TIM?

**Go**, wenn:

- gemeinsamer Workload funktioniert,
- Accelerator-/Host-/Combined-Grenzen vorliegen,
- Referenzspur und Wiederholungen valide sind,
- Rate-Duration und PSD erzeugt werden können,
- Cross-Platform-Transferanalyse möglich ist.

Dann ist x86 optional.

## Gate B – Soll x86 aufgenommen werden?

**Go**, wenn:

- Hailo bereits fertig ist,
- externe GPU-Leistungsmessung sauber möglich ist,
- NVML einen echten zusätzlichen I&M-Fall liefert,
- Journalabgabe nicht wesentlich verzögert wird.

## Gate C – Journal-Freeze

TIM-ready, wenn:

- Hailo-Erweiterung technisch deutlich über PARMA hinausgeht,
- List of Extensions vollständig ist,
- alle Claims aus Artefakten ableitbar sind,
- Manuskript klar im I&M-Scope positioniert ist,
- keine ungeklärten Messkorrekturen zentrale Resultate tragen,
- Hailo-/Jetson-Messgrenzen vergleichbar dokumentiert sind,
- alle Autoren einen vollständigen Reviewdurchlauf abgeschlossen haben.

---

# 21. Aktuelle offene Fragen für den neuen TIM-Chat

**Zuerst aktuelle Protokollfragen:** Was zeigen die neuen Jetson-100-s-YAMLs und die vier gezielten Leistungsfolgen? Welcher tatsächliche Messaufruf, Mess-Typ und Szenariostand wurden verwendet? Stimmen Engine und Inferenzoptionen zwischen Timed-Skript und Iterationskommando überein? Bleibt bei unveränderter Kette ein Trend im Gesamt- oder Innenfenster? Wie sehen gespeicherte Dauer und tatsächlicher Prozessabschluss aus? Die neue Ergebnis-ZIP ist noch nicht eingetroffen.

**Separat offene RC-Fragen:** Übernahme/Version, echtes Pico-Modell und Kanal-/Probe-/Messgrenze, Hardware-/Abbruch-Smokes und exakter Prozess-/Samplezeitbezug sind weiter nicht durch einen RC-Hardwarebeleg bestätigt. Joris’ aktuelle Arbeit erfolgt laut SetupInfo mit `measurement_suite.py`; daraus keinen RC-Einsatz ableiten.

**Bisherige Journalfragen (weiterhin offen, soweit nicht anderweitig belegt):**

1. Welcher endgültige Titel und welche I&M-Kernneuheit sollen im Abstract stehen?
2. Welcher Hailo-10-Host ist verbindlich?
3. Welches YOLO-Modell ist auf Jetson und Hailo exakt gemeinsam nutzbar?
4. Welche Hailo-Rails können getrennt erfasst werden?
5. Gibt es Hailo-interne Telemetrie, die sinnvoll verglichen werden kann?
6. Welche Burstsequenz ist deterministisch und plattformübergreifend?
7. Ist ResNet als zweiter gemeinsamer Workload realistisch?
8. Wann fällt das x86-Go/No-Go?
9. Welche TIM-EDICS passen exakt?
10. Welche vier bis sechs Journalgrafiken tragen die Hauptstory?

---

# 22. Empfohlener erster Arbeitsauftrag im neuen Chat

**Aktueller Anschlussauftrag:**

> Prüfe den von Kevin auf Memmert erzeugten Review-Export des neuen Jetson-GEMM-FP32-100-s-Sweeps. Trenne neue Zeitläufe, historische iterationsbasierte Jetson-Sweeps und RTX-A6000-GPU-Ergebnisse. Zeige alle Wiederholungen, E, T, E/T und Gesamt-/Innenfenster. Prüfe erhaltene Typ-/Umgebungsangaben und aktuelle Quell-/Binarystände. Erst nach Originalaufruf-/Optionsvergleich einen separaten Iterationslauf mit der unveränderten vorhandenen Kette starten. Die bekannte unpassende Kalibrierung begrenzt absolute Aussagen und kann bei Offsets auch relative Trends verändern. Keine NPYs löschen oder bereits gemessene Ordner erneut befüllen. Die RC-Abnahme bleibt ein eigener späterer Schritt.

**Bisheriger Auftrag für die Journalplanung (danach weiter verwendbar):**

> Erstelle auf Basis dieser Knowledge Base einen konkreten IEEE-TIM-Paperplan mit:  
> 1. einer präzisen Journalstory und drei Titelvarianten,  
> 2. einem Abschnitt-für-Abschnitt-Outline im IEEE-Transactions-Format,  
> 3. einer `List of Extensions` gegenüber PARMA-DITAM v0.9,  
> 4. einem minimalen und einem idealen Hailo-10-Messprogramm,  
> 5. einer x86-Go/No-Go-Entscheidungsmatrix,  
> 6. einer priorisierten TODO-Liste ohne vollständiges GUM-/Monte-Carlo-Unsicherheitsbudget.

---

# 23. Externe Richtlinien – Stand 27. August 2026

Geprüfte offizielle Quellen:

- IEEE Transactions on Instrumentation and Measurement – Scope
- IEEE TIM – Information for Authors
- PARMA-DITAM 2027 – Workshopseite und Important Dates

Bei späterer Einreichung müssen die TIM-Regeln erneut geprüft werden, insbesondere:

- Template und Dateigröße,
- EDICS,
- Overlength-Regeln,
- Proceedings-Extension-Anforderungen,
- Open-Access-Kosten,
- Editorialsystem.

---

# 24. Kurzfassung für interne Besprechungen

**Aktuelles Ergänzungsbriefing, 28.09.2026:** Joris’ RTX-A6000-Sweeps verwenden 100-s-Abbruch und zeigen laut Chat/Bild keinen vergleichbaren Hochratenabfall. Historische Jetson-Sweeps waren iterationsbasiert; Hailo hatte direkte Laufzeitvorgaben. Die unveränderte GPU-Pico-/INA-Kette wurde an Jetson zurückgebaut; ein ebenfalls zeitbegrenzter GEMM-FP32-Lauf ist laut Kevin fertig, aber hier noch nicht numerisch geprüft. Kevin übernimmt die Tests. Jetzt alte Kette und Profile unverändert lassen, Zeitlauf auswerten, anschließend gezielten Iterationspilot getrennt aufnehmen. Falsche absolute Kalibrierung nicht „wegignorieren“, sondern dokumentiert auf relative Diagnose begrenzen und additive/signalabhängige Effekte offenlassen.

**Historisches Ergänzungsbriefing, 21.09.2026:** Die historischen direkten Sweeps mischen separate Ausführungen mit einer teilweise erzwungenen Fensterlänge; zusätzlich wurden Plotterfehler gefunden. Bei FP32 erklärt der Rand-/Lastdaueranteil das Vorzeichen der Energieänderung in den geprüften Spuren, bei FP16/INT8 bleiben Niveauunterschiede auch im Inneren. Ein gemeinsamer verursachender Ratenfehler ist nicht bewiesen. Die Daten bleiben erhalten. Eine separate Python/PS4000A-Validierung liegt mit 126 bestandenen Softwaretests vor; Joris soll nun die Hardware-Smokes und danach einen kleinen balancierten Pilot durchführen. Original-Rust, Kalibrierungen und die kanonischen Common-Reference-Zahlen wurden nicht ersetzt.

**Übernommene wissenschaftliche Kurzfassung aus der Ausgangs-KB:**

> Die Workshopfassung zeigt auf Jetson/u.RECS über GEMM, YOLO, Gemma und ResNet, dass 2 kS/s für exakt begrenzte Run-Level-Energie ab 1 s das 1-%-Kriterium und ab 5 s das 0,5-%-Kriterium erfüllt. Kurze Ereignisse benötigen deutlich höhere Raten. Workloads besitzen stark unterschiedliche Spektren, und die analoge Messkette begrenzt die Transientensicht stärker als die 5-MS/s-Samplinggrenze. Die TIM-Fassung soll diese Methodik technisch auf Hailo-10 übertragen, Accelerator-/Host-/Systemgrenzen trennen, Host-Overhead und Telemetrie vergleichen und die plattformübergreifende Übertragbarkeit von \(f_{\min,E}(T,\varepsilon)\) untersuchen. x86/NVML ist eine wertvolle, aber optionale dritte Plattform. Ein vollständiges GUM-/Monte-Carlo-Unsicherheitsbudget ist ausdrücklich nicht geplant; verwendet werden empirisch validierte Fehlergrenzen und transparente Setup-Limitationen.


---

# 25. September-Audit – Datenbasis und bestätigtes Protokoll

## 25.1 Anlass und Prüfumfang

Ausgangspunkt war die GEMM-FP32-Figur aus Joris’ Masterarbeit: Mit zunehmender nomineller Abtastrate sinkt im Hochfrequenzbereich die **integrierte Gesamtenergie**. Der anfängliche Ausdruck „Leistung sinkt“ war dafür zu ungenau. Die Tabelle „Energie pro Sample“ darf nicht als Fehlerbeleg dienen; sie nimmt bereits rechnerisch ungefähr mit `1/fs` ab. Auch die rechte Abweichungsgrafik hat nur einen internen Bezug auf den Mittelwert der Ratenmediane, keine unabhängige Referenz. [Q03]

Geprüft wurden zunächst die Original-Snapshots [Q01, Q02] und relevante Dateien des fest referenzierten `percyjw-2/pico-sdk`-Commits `a864a9014f5fce4006f90d4f0ccbfeacaa043e72`. Später kamen Metadaten, ausgewählte reale Leistungsfolgen und Ergebnisabbildungen hinzu. Die Zuordnung jeder historischen Aufnahme zu einem damaligen Build/Commit und vollständigen Kommando ist nicht nachträglich gesichert.

**Bestätigung durch Kevin [U01], inzwischen präzisiert durch [U03]:** Die hier auditierten historischen Jetson-Samplerate-Sweeps waren iterationsbasiert. Dies gilt nicht pauschal für Hailo oder die späteren GPU-/Jetson-Zeitläufe (siehe 32.2). Bei den Dauerreihen wurde nach einer festgelegten Zeit abgebrochen. Die in alten Aufrufbeispielen stehenden `trtexec --iterations=100/200/400` sind keine erhaltenen Completion-Logs aller historischen Versuche. Eine tatsächlich kürzere Berechnung bleibt gerade bei vorgegebener Arbeit eine plausible, nicht automatisch fehlerhafte Erklärung.

## 25.2 Historischer Datenbaum auf Twix

Basispfad:

```text
/homes/jwachsmuth/power_measurements/
├── durations_without_filter/
│   ├── gemm/fp16/fp16/{5s,...,300s,...,600s}/<Lauf>/
│   ├── gemm/int8/int8/...
│   ├── random_pattern_yolo_durations_adjusted/
│   ├── static_msmt_37W_vergleich/
│   ├── static_msmt_37W_vergleich_estimated_voltage/
│   └── yolo/
├── sweep_without_filter/
│   ├── gemm/{fp32,fp16,int8}/<Rate>Sps/<Lauf>/
│   ├── static_msmt_37W/<Rate>Sps/<Lauf>/
│   ├── llm/
│   ├── random_pattern_yolo/
│   └── yolo/
├── hailo_durations/
├── hailo_sweep/
└── tek_scope_comparison/
```

Die doppelte Ebene `fp16/fp16` ist real, kein Tippfehler. Die vier überprüften direkten Reihen enthalten jeweils 27 Ratenordner von 50 S/s bis 5.000.000 S/s und 15 Läufe (IDs 0–14): **405 pro Reihe, insgesamt 1.620**. Für diese vier Reihen wurden alle 1.620 YAMLs exportiert, ohne protokollierte Exportfehler. [Q05, Q06]

Der native Ordnerbestand beginnt bei 50 S/s. Noch niedrigere Werte in einer Abbildung dürfen nicht automatisch als separate native Aufnahmen interpretiert werden; der Plotter kann virtuelle niedrige Raten aus gespeicherten Spuren erzeugen. [Q01, Q03]

`oscilloscope.npy` ist hier eine gespeicherte Leistungsfolge, nicht automatisch ein Archiv getrennter Roh-U/I-Kanäle. Die alte Pipeline löscht Parquet-Dateien nach Auswertung; möglicherweise andernorts vorhandene Rohbackups sind nicht geprüft. Eine `invalid_runs_35`-Datei ist eine Zählerdatei aus `.touch()`, nicht 35 erhaltene Fehlmessdateien; auf der FP16-Dauerebene ist sie nicht ausschließlich dem 300-s-Unterordner zuzurechnen. [Q01, Q04, Q05]

## 25.3 Umfang der drei Datenprüfungen

| Prüfung | Inhalt | Was sie nicht liefert |
|---|---|---|
| 300-s-FP16-Audit [Q04] | 15 reale historische Läufe bei **2 kS/s**, überall `use_voltage: false`, ausgegebene Dauer 302 s | Kein Samplerate-Vergleich; kein Nachweis des Spannungspfads der anderen Sweeps |
| Metadaten-Sweep [Q06, Q07] | 1.620 YAMLs, vier Reihen, 108 Gruppen; überall `use_voltage: true` | Keine erneute Integration aller großen Spuren; keine verifizierte Hardwarezeit |
| NPY-Pilot [Q08, Q09] | Vier Reihen × zwei Raten (2 kS/s, 5 MS/s) × Lauf-IDs 0 und 7 = 16 historische Spuren; ca. 37,06 GB auf Twix seriell gelesen | Keine neue Aufnahme und keine Vollprüfung aller 1.620 Leistungsfolgen; keine getrennten U/I-Werte im Export |

Der Pilot scannt 4.632.756.224 Samples auf Twix und exportiert Fensterstatistiken sowie vollständige 0,1-s-Aggregate. Die Nachanalyse liest diese Exporte, nicht erneut die entfernten Rohdateien. Der gesamte in den Metadaten erfasste NPY-Bestand beträgt etwa 1.017,12 GB; ein erneuter Vollscan ist nicht der aktuelle nächste Schritt. [Q07–Q09]

## 25.4 300-s-FP16-Dauerreihe – nicht mit dem Sweep vermischen

Die alte Energie wird bei allen 15 Läufen bis auf maximal ca. `3,04 × 10^-10 J` reproduziert. Ausgegeben werden jeweils 302 s; die integrierte Zeitspanne beträgt bei 2 kS/s 301,9995 s. Der Durchschnitt der vollständigen Fenstermittelwerte liegt bei ca. 36,212 W, nach je 5 s Randbeschnitt bei ca. 36,571 W. Die entfernten zehn Sekunden haben zusammen ca. 25,736 W Mittelwert. Das zeigt niedrigere Randleistung, **keine automatisch korrigierbare 0,99-%-Fehlmessung**. Lauf 0 liegt auch im Innenfenster niedriger. [Q04]

`use_voltage: false` bedeutet: Die Leistungsauswertung nutzt die Spannungsschätzung. Es bedeutet nicht zwingend, dass nie ein Spannungskanal aufgenommen wurde. Der spätere Ausschluss der Spannungsschätzung als Erklärung betrifft die vier direkten Sweeps mit `use_voltage: true`, nicht diese Dauerreihe.

---

# 26. Auditbefunde – belegte Defekte versus offene Ursachen

## 26.1 Befundmatrix des historischen Codes

Die folgenden Befunde gelten für die bereitgestellten Snapshots. Sie sind **nicht durch Auslieferung des Python-RC im Original-Rust-Code behoben**. Quellen und nummerierte Originalauszüge stehen in [Q03, Q07, Q09, Q11].

| ID | Stelle / Befund | Bedeutung für den beobachteten Trend |
|---|---|---|
| A01 | `pico_osc_communication.rs`: zugewiesene Rate nur protokolliert; Auswertung nutzt Wunschrate. Rust-Wrapper verkürzt `SampleConfig` auf ganzzahlige S/s. | Zeitbasis-/Metadatenfehler belegt. Reale Fehlzuweisung in den alten Messungen nicht nachgewiesen; exakte hohe ns-Intervalle erklären nicht schon durch Rundung den ganzen Trend. |
| A02 | Pico-Handler skaliert und schreibt synchron in Parquet; ZSTD-Level 15; keine belastbaren Streamsegment-/Kontinuitätsmetadaten. | Engpass-/Unterbrechungsrisiko und Nachweislücke. Tatsächliche Verluste oder Überlastung nicht belegt. 80 MB/s bei zwei Float64-Kanälen und 5 MS/s sind rechnerische Anwendungsdaten, nicht gemessene USB-/Diskrate. |
| A03 | `measurement_suite.py` übernimmt ggf. einmalige Dry-Run-Dauer und übergibt `int(duration_override + 2)`; `fit_start_stop_to_duration()` passt Grenzen an. | Gleiche ausgegebene Dauer wird teilweise hergestellt, statt unabhängig nachgewiesen. Unterschiedliche reale Lastdauer oder Samplelücken können danach mehr Idle-/Randanteil im Fenster erzeugen. |
| A04 | `data_reading_types.rs`: `overshoot_time` im Fensteriterator nicht in jedem Zweig zurückgesetzt. | Reproduzierbarer Zustandsfehler, z. B. 0,08 statt 0,1 J bei synthetischem 1-W-/25-S/s-Signal. Kein belegter Grund des Hochratenabfalls. |
| A05 | Dauer `N/fs`, Trapezintegration über `N−1` Intervalle. | Inkonsistente Bezeichnung. Bei hohen Raten zu klein und mit falscher Ratentendenz als Erklärung des Prozentabfalls. |
| A06 | `data_actions.rs`: `max_frame_energy`/`idle_frame_energy` im geprüften `dont_cut`-Pfad vertauscht. | Ergebnisfeldfehler nach der Integration; Energie nicht dadurch geändert. Cut-Pfad hat andere Rückgabereihenfolge. Diese alten Felder nicht blind zur Idle-Korrektur nutzen. |
| A07 | Virtueller Sweep rundet effektive Rate erneut auf eine ganze Zahl; weiterer Randfall bei Filter-Cutoff an Nyquist. | Separate Offline-Auswertungsdefekte, keine universelle Erklärung nativer Hochratenaufnahmen. |
| A08 | `TekMeasurement`: Einheitenfehler im Spannungsschätzungszweig. | Separater Tek-Pfad, nicht Ursache des hier geprüften direkten Pico-U/I-Sweeps. |
| A09 | Firmware-Analyzer liest `_idx` und verwirft Sequenzinformation. | Nachweislücke eines anderen Pfads; nicht als Pico-Sampleverlust ausgeben. |
| A10 | `skip_power_calculation`: erfolgreicher Capture-only-Zweig läuft ohne Fortschritt in derselben Schleife weiter. | Gemockter Test reproduziert zweiten identischen Capture-Aufruf. Alte Capture-only-Entkopplung nicht ungeprüft aktivieren. |
| A11 | Collector verwirft Benchmark-stdout (`Stdio::null()`), prüft erhaltenen Exitstatus nicht auf Erfolg. | Historische Ausführungs-/Completion-Belege fehlen; Kürzung, Fehlende und reale Laufzeit nicht ausreichend unterscheidbar. |
| A12 | Alte Aufnahme → Analyse → Bereinigung → nächste Aufnahme, blockierend. | Analysedauer kann die Pause verändern; dadurch möglicher Zustandskonfounder. Tatsächliche historische Pausen/Temperaturen fehlen. |

Die beiden zusätzlichen Darstellungsbefunde – Perzentiltrimming und Hailo-Quellenlabels – sind in Abschnitt 27 gesondert erläutert.

## 26.2 Synthetischer Fehlermechanismus – nicht zur Hardwareursache hochstufen

Im ersten Audit wurde ein Python-Port des konstanten Rust-Zahlenpfads mit absichtlich entfernten Lastsamples geprüft: 36 W Last, 10 W Idle, 97 s Last, 2.000 S/s, 776 entfernte Samples = 0,388 s. Energie sinkt von ca. 3.491,469 J auf 3.481,907 J, also **−9,561 J / −0,274 %**, während beide Ausgaben weiterhin **97,0 s** melden. Das demonstriert „Sampleverlust + erzwungene Fensterlänge“ als möglichen Mechanismus. Es beweist **keinen tatsächlich verlorenen Pico-Sample**. Die zehn Tests des ersten Audits prüfen solche Reproduktionen und sind keine Hardwareabnahme. [Q03]

Für feste Indexgrenzen wäre ein falsches `fs` ein proportionaler Energiefehler. Nach nachträglicher Fensteranpassung gilt dieser einfache Faktor nicht mehr allgemein; kein blindes Umskalieren aller historischen Energien.

## 26.3 Nach Datenprüfung zurückgestufte oder ausgeschlossene Erklärungen

**Spannungsschätzungsmodell:** Für die vier direkten Sweeps scheidet es nach ihrer gespeicherten Konfiguration aus (`use_voltage: true`). Dieser Status ist kein Kalibrier- oder Kanalzuordnungsnachweis. [Q06]

**Abschließende Trapezintegration:** Die 16 historischen Energien werden bis auf maximal **6,4543146 × 10^-6 J**, also rund 6,45 µJ, reproduziert. Das ist gegenüber Unterschieden von Joule bis Dutzenden Joule vernachlässigbar. Die vollständigen Bin-Aggregate sind intern konsistent. Damit erklärt ein allgemeiner abschließender Summationsfehler den geprüften Trend nicht. Kalibrierung, Zeitbasis und Kontinuität werden dadurch nicht bestätigt. [Q08, Q09]

**Universeller lastunabhängiger Skalierungsfehler:** Als alleinige Erklärung unzureichend, weil Lasten und Wiederholungen unterschiedlich reagieren. Signal- oder zustandsabhängige Geräte-/Softwareeffekte bleiben möglich.

**Thermik/Abkühlung:** Plausible Hypothese angesichts Wiederholungs- und Vorlaufunterschieden sowie des sequenziellen Ablaufs, keine Diagnose. Auch Grundlast, Takte, Kühlung, Messketten-Offset, reale Lastdauer und Aufnahmeeffekte sind offen. Keine nachträgliche Offset- oder Vorlaufsubtraktion ohne eigenen Nachweis.

**Zeitstempel:** YAML-mtime darf nicht als Aufnahmezeit verwendet werden. Beispielsweise liegen die FP32-YAMLs innerhalb von ca. 37 Minuten, während die Summe allein ihrer 405 × 97-s-Fenster ca. 10,9 Stunden beträgt. Verarbeitung/Kopieren ist damit naheliegend, der konkrete Ablauf aber nicht belegt. [Q07]

---

# 27. Quantitative historische Befunde und Plot-Gegencheck

## 27.1 Vier direkte Sweeps – alle 15 Wiederholungen je Rate

Die folgende Tabelle stammt aus `summary.json/comparisons` in [Q07], abgeleitet aus [Q06]. Je Gruppe werden Mediane verwendet. Leistung hier: gespeichertes `E / duration`. An den beiden verglichenen Raten ist die ausgegebene Dauer innerhalb jeder Reihe gleich. **2 kS/s ist nur die gewählte Vergleichsrate, keine als richtig nachgewiesene Referenz.**

| Reihe | YAML-Dauer [s] | E bei 2 kS/s [J] | E bei 5 MS/s [J] | E/T bei 2 kS/s [W] | E/T bei 5 MS/s [W] | Änderung |
| --- | --- | --- | --- | --- | --- | --- |
| GEMM FP32 | 97 | 3.487,365 | 3.474,576 | 35,952 | 35,820 | -0,367 % |
| GEMM FP16 | 104 | 3.445,544 | 3.369,054 | 33,130 | 32,395 | -2,220 % |
| GEMM INT8 | 105 | 3.333,244 | 3.249,956 | 31,745 | 30,952 | -2,499 % |
| Statischer Vergleich | 102 | 3.861,692 | 3.858,999 | 37,860 | 37,833 | -0,070 % |


Alle 1.620 Dateien enthalten `use_voltage: true`; `jetson_results`, `shelly_results` und `firmware_results` sind in diesem Export überall `null`. Ein paralleler Instrumentvergleich ist damit für diese vier Sweeps nicht verfügbar. Ordner-/YAML-Raten und `duration = (stop−start+1)/fs` sind intern konsistent, nicht unabhängig verifiziert.

Der Rückgang ist nicht streng monoton. Bei FP16 liegt z. B. der 5-MS/s-Median wieder etwas über dem 4-MS/s-Median. Bei gleicher nomineller Rate 5 MS/s sind die frühen GEMM-Laufnummern teilweise deutlich höher; FP16-Lauf 0 hat ca. 3.457,430 J, Lauf 7 ca. 3.377,782 J, der Gruppenmedian aber ca. 3.369,054 J. **Ein Einzelwert von Lauf 7 ist nicht der 15-Läufe-Median.** [Q07]

## 27.2 16-Spuren-Pilot – Innenfenster und Gesamtfenster

Leistung hier: erneut integriertes `E / ((N−1)/fs)`; nicht exakt dieselbe Nennerkonvention wie im historischen YAML-Überblick. Die winzige Konventionsdifferenz erklärt den beobachteten Effekt nicht. Änderungen jeweils 5 MS/s gegenüber 2 kS/s, deskriptiv nach Lauf-ID, **kein gepaarter statistischer Versuchsplan**. [Q08, Q09]

| Reihe | Lauf-ID | Gesamtfenster | Je 5 s Rand entfernt | Je 10 s Rand entfernt |
| --- | --- | --- | --- | --- |
| GEMM FP32 | 0 | -0,164 % | +1,066 % | +1,159 % |
| GEMM FP32 | 7 | -0,288 % | +0,920 % | +0,980 % |
| GEMM FP16 | 0 | +0,488 % | +1,026 % | +1,074 % |
| GEMM FP16 | 7 | -1,675 % | -2,505 % | -2,563 % |
| GEMM INT8 | 0 | -0,279 % | -0,664 % | -0,691 % |
| GEMM INT8 | 7 | -2,403 % | -2,465 % | -2,470 % |
| Statischer Vergleich | 0 | -0,100 % | -0,099 % | -0,098 % |
| Statischer Vergleich | 7 | -0,077 % | -0,076 % | -0,077 % |


**FP32:** Bei beiden untersuchten Laufnummern wechselt die Änderung das Vorzeichen, sobald genügend Rand abgeschnitten wird. Lauf 7: Innenleistung bei je 10 s Randbeschnitt **36,670975 → 37,030452 W**, also **+0,980 %**, obwohl im Gesamtfenster **−0,288 %** stehen. Das beschreibt verschiedene Fenster/Messgrößen, keine Korrektur der ursprünglichen Gesamtenergie.

Die Energiezerlegung mit jeweils fünf Sekunden Rand lautet exakt bis auf Rundung:

| FP32-Lauf-ID | ΔE Innen [J] | ΔE beide Ränder [J] | ΔE Gesamt [J] |
| --- | --- | --- | --- |
| 0 | +34,021 | -39,737 | -5,716 |
| 7 | +29,356 | -39,379 | -10,023 |


Die sichtbare FP32-Lastphase in 0,1-s-Aggregaten dauert bei 2 kS/s ca. **94,6 s (Lauf 0)** bzw. **94,5 s (Lauf 7)**, bei 5 MS/s jeweils ca. **93,1 s**. Die alte YAML meldet stets 97 s. Eine explorative Schwellenprüfung bei 25/50/75 % des Kontrasts liefert ähnliche Grenzen. Das ist eine signalbasierte Beschreibung auf YAML-Zeitachse, **keine unabhängig gemessene Benchmarkdauer**. Die iterationsbasierte Ausführung macht reale Laufzeitänderung plausibel. [Q09, U01]

**FP16/INT8:** Lauf 7 sinkt auch im Innenfenster; ein alleiniger äußerer Randfehler genügt hier nicht. Bei FP16 ist Lauf 0 dagegen im Inneren höher als bei niedriger Rate. Bei gleicher Rate 5 MS/s sinkt der 10-s-beschnittene Innenmittelwert zwischen Lauf 0 und 7 bei FP16 von **34,173269 auf 33,060996 W (−3,255 %)**, bei INT8 von **32,487237 auf 31,950948 W (−1,651 %)**.

Im Vorlauf 0–4 s liegen bei FP16 ca. **8,377 gegenüber 7,699 W**, bei INT8 ca. **8,096 gegenüber 7,521 W** vor. Der Unterschied beginnt somit bereits vor hoher Last. Messketten-Offset und veränderte Grundlast sind prüfenswerte Alternativen, aber weder voneinander getrennt noch als Ursache bewiesen. Der statische Vergleich ändert sich deutlich weniger. [Q09]

## 27.3 Vollständiges bereitgestelltes Plotarchiv

[Q10] enthält **33 einseitige PDFs**: neun Jetson-Samplerate-Figuren, 18 Jetson-Dauerfiguren (neun Paare) und sechs Hailo-Dauerfiguren (drei Paare). `Hailo/samplerates` ist leer. Es sind Ergebnisabbildungen, **kein vollständiger neuer Rohdatenexport**. Das Review [Q11] sichtet alle Seiten und extrahiert Text/Vektorgeometrie; keine OCR. 108 Mediane und 108 dargestellte relative Standardabweichungen wurden zusätzlich gegen die vier verfügbaren YAML-Reihen geprüft.

Zusätzliche Medianenergieänderungen von 2 kS/s auf 5 MS/s aus der **PDF-Vektorgeometrie**, nicht aus neu gelieferten Primär-YAMLs: LLM ca. **−1,696 %**, Random-Pattern YOLO **−0,429 %**, YOLO FP32 **−1,014 %**, YOLO FP16 **−0,201 %**, YOLO INT8 **−0,047 %**. Zusammen mit Abschnitt 27.1 bestätigt dies unterschiedliche Effektgrößen, keine universelle monotone Skalierung. [Q11: `data/rate_comparison.csv`]

Die Dauer-Boxplots zeigen `E/T`; die Abweichungsbalken vergleichen dagegen Medianenergien. Bei unterschiedlichen Zeitfenstern sind relative Energie- und Leistungsabweichungen nicht gleich. Unterschiedliche Messgrenzen sind zusätzlich getrennt zu halten. `pre_adjustment` und `adjusted` sind getrennte Auswertungsstände ohne ausreichend mitgelieferte Transformationsprovenienz; nicht stillschweigend zu einer neuen kanonischen Fassung vereinigen.

## 27.4 Belegtes Trimmen im alten Samplerate-Plotter

`plot_sweep.py` entfernt Werte außerhalb des 5.–95. Perzentils **vor** der Statistik, nicht nur aus der sichtbaren Darstellung. In allen 108 überprüften Gruppen bleiben **13 statt 15 Werte**: 216 von 1.620 Werten entfallen. Auch der auffällige erste 5-MS/s-Lauf 0 wird in allen drei GEMM-Reihen entfernt. [Q11]

| 5-MS/s-Reihe | Relative σ, alle 15 | Relative σ, 13 getrimmt | Reduktion der ausgewiesenen Streuung |
| --- | --- | --- | --- |
| GEMM FP32 | 0,101 % | 0,089 % | 12,0 % |
| GEMM FP16 | 0,673 % | 0,209 % | 69,0 % |
| GEMM INT8 | 0,547 % | 0,125 % | 77,1 % |


Diese Angaben nutzen die im Review reproduzierte relative Standardabweichung des alten Plotters; keine nachträglich behauptete Konfidenzgrenze oder vollständige Messunsicherheit. Die Gruppenmediane bleiben in diesen geprüften Gruppen unverändert. **Der Medianabfall entsteht deshalb nicht erst durch das Trimming**, die ausgewiesene Wiederholungsstreuung wird jedoch erheblich kleiner. Standard- bzw. Quartilsabweichung bezeichnet Wiederholungsstreuung, nicht die Abweichung von einer unabhängigen Referenz. [Q11]

Neue Hauptstatistik: alle qualitätsgültigen Wiederholungen, Quellen-/Run-ID erhalten. Optionale getrimmte Zusatzansicht muss ihre Auswahl und Ausschlüsse ausweisen. Gleiche Zahl 13 im Common-Reference-Langzeitanker ist allein kein Nachweis derselben Auswahlregel (siehe Abschnitt 7.3).

## 27.5 Belegte Hailo-Quellenvertauschung

`plot_duration_sweep.py` baut Balkenwerte in Quellenreihenfolge auf, Labels später jedoch aus einem `set`. In den Hailo-Figuren lautet die Wertefolge nach dem mitgelieferten Plotter **u.RECS → Shelly → Hailo**; die gedruckten Labels variieren:

| Hailo-Figur | Gedruckte Labels von links nach rechts |
|---|---|
| GEMM | Hailo, Shelly, u.RECS |
| Random-Pattern YOLO | Shelly, u.RECS, Hailo |
| YOLO | u.RECS, Hailo, Shelly |

Im Random-Pattern-YOLO-Dauerdiagramm bei 300 s trägt der zweite Balken ca. **+39,818 %** das Label „u.RECS“, gehört nach der Wertebildung aber zu **Shelly**. Der erste Balken ca. **+0,185 %** gehört zu u.RECS und trägt „Shelly“. **Keinen ca. 40-%-u.RECS-Fehler aus dieser Figur zitieren.** Die Aussage ist anhand des gelieferten Plotters und der PDF geprüft; endgültige korrigierte Hailo-Zahlen/Plots benötigen die entsprechenden Original-YAMLs. [Q11]

Nicht nur Labels sortieren: Werte und Namen gemeinsam aus expliziten Quellen-Schlüsseln erzeugen. Die gezeigten Jetson-Abweichungsplots passen zwar in ihrer Reihenfolge, der gemeinsame Code ist trotzdem nicht robust.

---

# 28. Entscheidungen für die Fortsetzung und das Paper

> Historischer Planungsstand vom 21.09.2026. Die aktuelle operative Priorität während Joris’ Urlaub ist der getrennte Legacy-Protokollvergleich aus Abschnitt 35. RC-Hardwareabnahme bleibt ausstehend.

## 28.1 Bestätigte Entscheidungslage

Kevin hat die Implementierung freigegeben, den Fokus ausdrücklich auf **PicoScope** gelegt und Joris für die Hardwaretests vorgesehen: zunächst die Kette testfertig bauen, dann an Joris zum Prüfen übergeben. Es gibt noch keine Rückmeldung einer bestandenen Abnahme. [U02]

Der erarbeitete Arbeitsweg lautet:

1. Historische Messungen, Originaltools und Kalibrierung unverändert archivieren; Einschränkungen dokumentieren statt Daten pauschal verwerfen.
2. Einen getrennten Validierungsstand herstellen und softwareseitig testen; keine automatische Installation in Joris’ laufende Umgebung.
3. Nach Hardware-Smokes einen kleinen kontrollierten Pilot aufnehmen, nicht vorsorglich alle Modelle und Raten erneut messen.
4. Unterschiedliche Fenster auf **derselben** neuen Rohaufnahme und zusätzlich Same-Trace-Ratenreduktionen vergleichen.
5. Erst anhand der Abnahme/Pilotdaten über Integration in ursprüngliche Tools, größere Wiederholungen und Manuskriptänderungen entscheiden.

Das Ziel ist **nicht eine möglichst flache Kurve**, sondern nachvollziehbare Arbeit, Zeitachse, Kanalwerte, Fenster und Fehlerstatus. Keine neue breit angelegte Kalibrierkampagne und kein GUM-/Monte-Carlo-Programm; Entscheidung aus Abschnitt 10 bleibt bestehen.

## 28.2 Geeignete Dokumentation der historischen Sweeps

> Die hier untersuchten historischen Jetson-Samplerate-Sweeps wurden mit vorgegebenen Iterationszahlen, die Jetson-Dauerreihen mit zeitgesteuertem Abbruch durchgeführt. Hailo und spätere GPU-/Jetson-Zeitläufe sind davon ausdrücklich getrennt (siehe Abschnitt 32.2). Die historische Auswertung passte erkannte Messfenster an eine geschätzte Dauer an. Unterschiede zwischen Abtastratengruppen können daher neben Abtast- und Auswertungseffekten auch unterschiedliche Ausführungsdauern und Betriebszustände enthalten und werden nicht als isolierter Abtastratenfehler interpretiert.

Zusätzlich die beiden Plotterprobleme, tatsächliche Stichprobenzahl und den Status der gemessenen bzw. geschätzten Spannung nennen. Originale und korrigierte Darstellungen getrennt versionieren. Innenmittelwerte nicht als „korrigierte Gesamtenergie“ ausgeben. Die Hailo-Labelkorrektur ist keine Neukalibrierung.

## 28.3 Nicht erledigte Ursachenklärung

Weiterhin offen sind die Beiträge von realer Laufzeit, Initialisierung/Warm-up, Startzustand, Temperatur/Takt/Kühlung, Grundlast/Offset, nativer Ratenkonfiguration und gegebenenfalls unsichtbaren Aufnahmeunterbrechungen. Der neue Softwarestand kann diese Fragen besser untersuchen, **beweist aber keine davon allein durch seine Existenz oder synthetische Tests**.

Die Common-Reference-Methodik bleibt sachlich von nativen separaten Sweeps getrennt. Ihre übernommene Zahlenbasis wird nicht pauschal ersetzt; Herkunft der Fenster und ggf. Wiederholungsselektion vor dem Paper-Freeze kontrollieren. Hailo-/x86-Plattformerweiterungen sind dadurch weder abgeschlossen noch aufgehoben.

---

# 29. Tatsächlich ausgelieferte PicoScope-Validierung v1.0.0-rc1

## 29.1 Architekturentscheidung und Status

**Ausgeliefert:** `pico_validation_v1.0.0-rc1.zip` [Q12].

```text
Alte Kette (unverändert):
measurement_suite.py
  → Rust-Collector / Rust-Pico-Wrapper
  → Parquet → Rust-power_calculations → alte Plotter

Neue separate Validierung:
pico.py capture / campaign
  → native PS4000A-Bibliothek über Python ctypes
  → begrenzter RawWriter → zwei ADC-Dateien + JSON/Blockbelege
  → Offline-Analyse → Report / historischer Neuplotter
```

**Wichtige Abweichung vom zuvor erstellten Umbauplan [Q11]:** Ein Patch beider Originalprojekte einschließlich Rust-SDK-Fork war geplant. Tatsächlich wurde stattdessen eine **separate Python-Implementierung direkt auf der PS4000A-API** gebaut. Die Original-ZIPs liegen byteidentisch unter `originals/`. Es wurde kein Rust-Collector gepatcht, kein neuer Rust-SDK-Fork ausgeliefert und kein nativer Rust-Gesamtbuild nachgewiesen. Die neue Kette ist später integrierbar, aber kein Drop-in-Update der alten Installation. [Q12, Q13]

Der Versionszusatz **rc1** bedeutet hier: zur beschriebenen Hardwareabnahme vorbereitet, nicht als hardwarevalidiertes Messsystem freigegeben. `common_reference_psd_tool_v0.7.3` bleibt ein separates Projekt.

## 29.2 Dateien und Funktionen

| Teil | Tatsächliche Dateien / Einstieg | Implementierter Umfang |
|---|---|---|
| CLI und Vorprüfung | `pico.py`, `pico_validation/config.py`, `common.py`, `verify_package.py` | Konfiguration, Platzhalter-/Budget-/Integritätsprüfung; Hardwareaufnahme nur mit `--arm`; keine Überschreibung bestehender Ausgabeordner |
| Native Pico-Anbindung | `pico_validation/driver.py` | PS4000A über `ctypes`, Geräte-/Kanalprüfung, zugewiesenes ganzzahliges ns-Intervall statt nur gerundeter Rate |
| Aufnahme und Speicherung | `capture.py`, `storage.py` | Kurzer Callback, Kopie in begrenzten Puffer, eigener Writer, keine laufende Kompression; zwei rohe int16-ADC-Kanäle; Fehler-/Blockbelege |
| Benchmark | `benchmark.py`, `benchmark_target.py` | Lokal/SSH, Startfreigabe nach Samples/Vorlauf, stdout/stderr, Status, Zielzeit, Abbruch/Watchdog, angeforderte und gemeldete Arbeit getrennt |
| Kampagne | `campaign.py`, `examples/gemm_counterbalanced_16.json` | Seed/Plan, ausgewogene Ratenblöcke, dokumentierte Pause, begrenzte Attempts, eigene Verzeichnisse, keine Inline-Analyse |
| Neue Numerik | `analysis.py` | Blockweise U/I/P-Umrechnung und Statistik, korrekte Intervallspanne, mehrere Fenster, kein Zurechtschieben der Hauptfenster auf Schätzdauer |
| Legacy-Vergleich | `legacy_reference.py`, `pico_validation/legacy_reference.py`, `legacy_numeric_port.py` | Separater eingeschränkter Python/Numba-Port des alten Zahlenpfads; keine Behauptung nativen Rust-Replays |
| Reports / alte YAMLs | `report.py`, `legacy_report.py`, `replot_legacy.py` | Alle qualitätsgültigen Wiederholungen, feste Quellenlabels, Energie/Leistung getrennt, keine doppelte Capture-ID |
| Übergabe | `pack_results.py`, `docs/JORIS_TESTPLAN.md` | Kleine Review-ZIP, keine Roh-ADC-/NPY-/Parquet-Inhalte, Ausschlussmanifest und Abnahmeplan |

Sensor-/Probe-Faktoren und alte Kalibrierformeln werden offline übernommen, **nicht neu kalibriert**. Andere Aufnahmequellen (Tektronix, Shelly, Firmware, HailoRT) wurden nicht implementiert oder verändert. Ein allgemeines Benchmarkkommando ist kein neuer Hailo-Telemetrieadapter.

## 29.3 Zeitbasis, Rohdaten und Fehlerstatus

Die beiden int16-Kanäle ergeben bei 5 MS/s rechnerisch **20 MB/s rohe ADC-Nutzwerte**; dies ist keine gemessene USB-Durchsatzgarantie. Die Rohkanäle bleiben erhalten, Leistung wird offline berechnet. Kanalbereiche, Offsets, Probe-Faktoren, Geräteangaben und zugewiesenes Intervall werden dokumentiert. Kein automatisches Löschen nach Analyse.

Puffer-/Writer-/API-Fehler, Übersteuerung, Autostop und fehlende Daten erzeugen `invalid` statt stiller Wiederverbindung. Ein harter Kill kann unvollständige Verzeichnisse ohne abschließende `capture.json` hinterlassen; diese sind keine akzeptierten Läufe. Kampagnen nutzen einen äußeren Prozess-Watchdog, doch harte native/Dateisystemhänger sind nicht als universell beherrscht nachgewiesen.

Softwareindex, Callback-Abstände, Dateigröße und Hash sichern die eigene Verarbeitung ab. Sie beweisen **keine verlustfreie Hardware-/USB-Lieferung vor dem Callback** und keinen unabhängig kalibrierten ADC-Takt. Ringpufferindex ist kein absoluter Hardware-Samplezähler. [Q12: Architektur und Dateiformat]

**Wichtige Ergebnisdateien des neuen Formats:**

```text
capture_start.json       Capture-ID und unveränderter Konfigurations-Snapshot
acquisition_setup.json   Gerät, ADC-Bereich, Profil und zugewiesenes Intervall
host_events.jsonl        monotone Recorder-Ereignisse
raw/A.i16le              Stromsensor-Kanal, signed int16 little endian
raw/B.i16le              Spannungskanal, signed int16 little endian
raw/blocks.jsonl         Block-/Index-/Statusbelege
benchmark/result.json   Prozessstatus/Zielzeit, keine reine Inferenzzeit
benchmark/stdout.log    vollständige Benchmark-Standardausgabe
benchmark/stderr.log    vollständige Benchmark-Fehlerausgabe
capture.json            Abschluss complete/invalid, Summen, Hashes, Qualitätsstatus
analysis_v1_.../         bins.csv und result.json der jeweiligen Analyse
```

`benchmark/` entsteht nur bei konfiguriertem Kommando. Die beiden Rohdateien haben keine NPY-Header; lesbar z. B. als `dtype='<i2'`. Neue Fensterindizes sind `start_index` **inklusiv**, `stop_index_exclusive` **exklusiv**. Alte YAML-`start_stop_idx` waren dagegen beide inklusiv; beim Vergleich nicht unverändert übernehmen.

`state: complete` heißt nur, dass die implementierten Anwendungsprüfungen keinen Fehler gefunden und den Datensatz abgeschlossen haben. Die Flags für unabhängige Hardwarekontinuität, Hardwarezeitbasis, exakte Kommando-/Sample-Zuordnung und wissenschaftliche Referenzvalidierung bleiben im RC **false**. `--allow-invalid` und `--no-verify-hashes` ermöglichen nur ausdrücklich gekennzeichnete Diagnose; daraus entsteht kein normaler gültiger Reportpunkt. [Q12: `docs/DATEIFORMAT.md`]

## 29.4 Hauptfenster und zwei verschiedene Legacy-Wege

- `full_capture`: komplette gelieferte Spur; Trapeze über N−1 Intervalle.
- `detected_envelope`: signalbasierte Hülle mit dokumentierter Bin-/Schwellenregel; interne Pausen bleiben erhalten. Keine erzwungene Dauer; kein garantierter Kernelmarker.
- `explicit_sample_time_window`: explizite Grenzen auf Samplezeitachse, nicht still geclippt.
- `interior_trim_*`: zusätzliche Innenleistungsdiagnose, nicht Ersatz für Gesamtenergie.

Der neue Detektor nutzt ein Perzentil von **Zeitbin-Mittelwerten** zur Signalpegelbestimmung. Das ist etwas anderes als das entfernte Perzentiltrimming über **physische Wiederholungen**. Konstanten Signalen wird kein erfundenes Lastfenster zugewiesen; sehr kurze/seltene Spitzen können vom automatischen Detektor verfehlt werden. `primary_window: null` verlangt Sichtprüfung oder eine fachlich begründete Fensterwahl.

**`legacy_duration_fit_comparison`:** alte Längenanpassungsregel auf den **neuen** Detektorgrenzen; kein identischer alter Gesamtalgorithmus.

**`legacy_reference.py`:** separat portierter alter konstanter ungefilterter Pico-Zahlenpfad mit gemessener Spannung und `dont_cut=True`, einschließlich bewusst erhaltener historischer Eigenheiten für Reproduktion. Python/Numba, kein Rust-Binary, keine allgemeine Firmware-/Parquet-/CLI-Emulation. Große Replays benötigen Numba und eine zusätzliche Float64-`power.npy` (8 Byte/Sample); Platzprüfung erforderlich.

Offline-Ratenvergleich: gemeinsame Dezimierung der ADC-Paare mit mehreren **sampling-grid offsets**, ohne Antialiasfilter und gegen identische Endpunkte der hochratigen Spur. Dies reduziert Unterschiede separater physischer Ausführungen, ersetzt aber weder native Niedratenaufnahme noch unabhängige Referenz. Alte Code-/Dokumentationsnamen mit „phase“ werden wissenschaftlich als grid offset bezeichnet.

## 29.5 Benchmarkmodi und Synchronisationsgrenzen

`fixed_work`: Erfolgreicher Prozessabschluss wird geprüft. Angeforderte Arbeit bleibt eine Vorgabe; tatsächlich erledigte Arbeit ist nur bekannt, wenn der Benchmark sie meldet. Ein eigener Benchmark kann strukturiert an `PICO_WORK_RESULT_PATH` berichten. Vollständige `trtexec`-Logs werden behalten; keine erledigte Arbeit aus `--iterations` erfinden und keine versteckten Dauer-/Warm-up-Optionen anhängen.

`fixed_time`: Zielstarter fordert SIGINT nach definierter Ziel-Prozesszeit an. Frühes Ende, notwendige SIGTERM-/SIGKILL-Eskalation oder Watchdog-Ende sind keine regulär abgeschlossenen Zeitläufe. Das ist nicht automatisch ein samplegenaues wissenschaftliches [0,T]-Integrationsfenster.

**Kein zusätzlicher aufgezeichneter Hardwaremarker in rc1.** Kanal A bleibt Stromsensor, B bleibt direkte Spannung. Eine Prozesszeit enthält u. a. Initialisierung/Warm-up/Abschluss und ist keine reine Inferenzzeit. Remote-, Recorder- und Sample-Zeitachsen sind nicht hardware-synchronisiert. Die alten externen `timed_engine_execution.sh`-/`random_pattern.sh`-Dateien lagen nicht vor und wurden nicht als geprüft übernommen.

## 29.6 Unterstützter Implementationsumfang und Voraussetzungen

Linux/POSIX, Little Endian, Python **ab 3.10**; lokale Softwaretests laut Beleg mit **3.13.5**, nicht mit jeder erlaubten Version. NumPy für Analyse/Tests; Matplotlib/PyYAML für Bilder/historische YAMLs; Numba optional für große Legacy-Replays. `gcc` nur für das synthetische C-Testdoppel.

Direkter Adapter für **4224A, 4424A und 4824 über PS4000A**. Diese Liste ist implementierte Auswahl, **keine Liste hardwaregeprüfter Geräte**. Vorlagen erwarten 4224A; tatsächliches Gerät/Seriennummer von Joris bestätigen lassen. Keine automatische Umdeutung anderer API-Familien oder PicoConnect/4444.

Die passende native Herstellerbibliothek und USB-Berechtigung müssen auf Joris’ Rechner bereits vorhanden sein. Kein Hersteller-SO/DLL im Paket, keine Treiberinstallation, kein `sudo`, keine globale Aktualisierung seiner Umgebung. Bei mehreren Geräten feste Seriennummer bevorzugen. Lokale Konfigurationen kopieren statt Paketbelege überschreiben. [Q12]

## 29.7 Belegte Softwaretests – keine Hardwarefreigabe

Im ausgelieferten Testbeleg: **126 Tests, 0 Failures, 0 Errors, 0 Skips**, ca. 15,017 s in der damaligen Umgebung. Release-QA aus frisch entpacktem ZIP: erneut **126/0/0/0**, ca. 15,720 s; 56 manifestierte Dateien geprüft. Dies sind zwei Durchläufe derselben Suite, **nicht 252 unterschiedliche Tests**. [Q12, Q13]

Abgedeckt: Umrechnung/Konfiguration; kompiliertes C-Testdoppel der PS4000A-ABI; synthetischer 5-MS/s-Datenfluss bis Disk; Queue-/API-/Clipping-/Schreibfehler; lokale echte Kindprozesse; lokal nachgebildeter SSH-Transport; Kampagnen-CLI/Attempts; Fenster/Numerik/Hashes; Quellenlabels/alle Wiederholungen; Export-/Integritätsregeln.

Zusätzliche Regression mit echten historischen Ergebnis-YAMLs: **1.620 Dateien, 108 Gruppen, jeweils alle 15 Wiederholungen**, maximale Medianabweichung zum vorherigen Audit **0,0 J**. Es wurden nicht erneut alle NPYs oder elektrische Messwerte überprüft. [Q12: `test_evidence/historical_replot_regression.json`]

**Nicht durchgeführt:** echtes PicoScope/USB, native Herstellerbibliothek zusammen mit Gerät, elektrischer Skalierungsabgleich, Langzeit-/USB-Durchsatzabnahme, Feldtest auf Twix/Jetson, realer SSH-Netzwerklogin/-abbruch und nativer Rust-Gesamtbuild. Ein synthetisch passender ABI-Test kann gemeinsame Fehler von Implementierung und Testdoppel nicht ausschließen. Die Hardwaretests sind ausdrücklich Joris’ nächste Aufgabe. [Q12, Q13]

---

# 30. Übergabe an Joris – historischer RC-Abnahmeplan vom 21.09.2026

> Weiter gültiger Plan für einen späteren RC-Test, nicht der aktuelle operative Auftrag: Joris ist inzwischen laut Kevin im Urlaub. Kevin setzt vorerst den Vergleich mit der vorhandenen Legacy-Installation fort (Abschnitte 32–35). Ein RC-Hardwaretest wurde nicht neu bestätigt.

## 30.1 Reihenfolge der Abnahme

**Stand: vorgesehen, noch keine Ergebnisrückgabe von Joris.** Die vorhandenen Twix-Analysen waren historische Datenprüfungen, keine Hardwareabnahme dieses RC. Das Paket wurde zum Download bereitgestellt; Versand/Installation/Testbeginn bei Joris ist nicht durch ein Ergebnis belegt. [U02, Q12, Q13]

| Stufe | Prüfumfang | Freigaberegel |
|---|---|---|
| P0 | Paketintegrität, eigene Umgebung, synthetische Selftests | Ergebnis separat speichern; fehlende/ausgelassene Tests nicht als vollständiges PASS ausgeben |
| P1 | Gerät/API/Seriennummer, U/I-Kanalbelegung, Messgrenze, Faktoren und freier Platz | Vor jedem echten Stream; kein anderer Prozess darf gleichzeitig das PicoScope benutzen |
| P2 | U/I-Smoke ohne Benchmark bei 2 kS/s und 5 MS/s | Elektrische Werte plausibel, direkte U/I-Kanäle, Intervall/Fehler/Dateischluss nachvollziehbar; ggf. kein Lastfenster bei konstantem Eingang ist korrekt |
| P3 | Einzelner Benchmark mit geprüftem Kommando und Logs | Samples/Vorlauf vor Freigabe, Exit/Completion/Zielzeit/Nachlauf nachvollziehbar; unbekannte Arbeit bleibt unbekannt |
| P4 | Kontrollierter Abbruch und Fehlerverhalten | Beendigung/`invalid`/erhaltene Belege; kein stilles Weitermessen oder Überschreiben |
| P5 | Balancierter 16-Läufe-Pilot | Erst nach P0–P4; nicht auf bloßes `16 complete` reduzieren |
| P6 | Review-Paket und Laborvermerk | Hardwarekriterien einzeln bewerten; nicht ausgeführte Prüfungen `pending`/`not_performed` lassen |

Das ausführliche Originalverfahren steht in `docs/JORIS_TESTPLAN.md`, die ausfüllbare Vorlage in `docs/hardware_acceptance_template.json` in [Q12]. Kein riskantes Kabelziehen als notwendige Fehlertestmethode voraussetzen.

## 30.2 Konkrete Pilotkonfiguration

Zwei bestehende Modelle **GEMM FP32 und FP16**, Raten **2 kS/s und 5 MS/s**, **vier Wiederholungen pro Kombination = 16 Aufnahmen**. Ausgewogene Zweierblöcke, dokumentierter Seed `20260921`, Standardpause **30 s**, standardmäßig ein Versuch pro Planposition; optional begrenzte Retries. Die Pause ist ein Pilotparameter, **kein Nachweis thermischen Gleichgewichts**. [Q12]

Beispiele enthalten sichtbare Platzhalter für Host/Engine sowie Angaben, die physisch bestätigt werden müssen. Keine heimlichen Engine-Neubauten, Kalibrieränderungen, anderen Messbereiche oder Taktmodi im gleichen Vergleich. Telemetriepfade werden gelesen, keine Betriebsmodi durch die Testsoftware gesetzt. Umfang ist ein Diagnosepilot, kein abschließender plattformübergreifender Genauigkeitsnachweis.

Bei voreingestelltem 200-s-Aufnahmebudget verlangen acht Hochratenläufe rechnerisch ca. **35,2 GB Rohbudget inklusive 10 % Reserve**, zusätzlich **2 GiB feste Reserve** und kleine Niedratenanteile. Das ist eine Budgetrechnung für zwei int16-Kanäle, nicht die ca. 37,06 GB der alten 16-NPY-Prüfung. Legacy-Float64-Dateien benötigen zusätzlichen Platz. Keine numerische Auswertung zwischen Aufnahmen; erst danach `analyze`/`report`.

## 30.3 Einstieg im richtigen Arbeitsverzeichnis

Alle relativen Befehle **im entpackten Paketordner** ausführen. Der Beispielpfad ist eine Empfehlung, keine Behauptung einer bereits installierten Kopie auf Twix oder bei Joris.

```bash
cd ~/energy_analysis/pico_validation_v1.0.0-rc1
python3 verify_package.py
python3 pico.py selftest --out "$HOME/pico_selftest_$(date +%Y%m%d_%H%M%S)"
```

Danach Konfiguration kopieren und vor Gerätezugriff prüfen:

```bash
cp examples/pico_jetson_ina225_smoke.json local_smoke.json
# local_smoke.json: Gerät/Seriennummer, Kanal-/Probe-Faktoren und Messgrenze prüfen.
python3 pico.py doctor --config local_smoke.json --probe-device
```

`doctor --probe-device` öffnet und schließt das Gerät, startet aber keinen Stream. Nicht parallel zu alter Aufnahme oder Pico-GUI. Nach Freigabe nach Testplan:

```bash
RUN="$HOME/pico_smoke_$(date +%Y%m%d_%H%M%S)"
python3 pico.py capture --config local_smoke.json --out "$RUN" --arm
python3 pico.py analyze "$RUN"
python3 pack_results.py "$RUN" --out "${RUN}_review.zip"
```

Die separate 5-MS/s-Smoke-Vorlage, Benchmark-/Fixed-Time-Beispiele und der 16er-Plan liegen unter `examples/`. `host: null` bedeutet lokale Ausführung auf dem Aufnahmerechner, nicht automatisch auf dem Jetson. Ohne `--arm` startet keine neue Aufnahme. Bestehende Plan-/Capture-Ausgabeordner nicht zur erneuten Aufnahme wiederverwenden.

## 30.4 Rückgabe und Auswertungsentscheidung

`pack_results.py` exportiert Logs, JSON/CSV und kleine Bilder, **keine ADC-/NPY-/Parquet-Rohdaten**. Standardlimits: 16 MiB pro Datei und 256 MiB gesamt; Ausschlüsse stehen in `BUNDLE_MANIFEST.json`. Rohdaten unverändert bei Joris behalten. Hostnamen, Pfade und Benchmarkausgabe vor Weitergabe auf vertrauliche Inhalte prüfen. Ein separates Reportverzeichnis außerhalb des Kampagnenbaums separat exportieren. Kein automatischer Versand durch das Tool. [Q12]

Bei der Rückgabe zuerst Software-/Konfigurationsidentität und Hardwareabnahme prüfen; dann Lastgrenzen/Prozessprotokolle, U/I/P-Innen-/Randwerte und Wiederholungsverlauf. Neue Hauptfenster, `legacy_duration_fit_comparison`, tatsächlichen Legacy-Port und Same-Trace-grid-offset-Analyse nicht verwechseln.

Wenn nur Gesamtfenster differieren, wird der Rand-/Protokolleinfluss konkreter. Bleiben Innenunterschiede bei gleicher Rate oder veränderten Startzuständen, diese gesondert untersuchen. Besteht bei vergleichbaren Bedingungen weiterhin ein nativer Rateneffekt, gezielt eine unabhängige Referenz-/Zeit-/Kontinuitätsprüfung planen. Ein kleiner/unauffälliger Pilotunterschied beweist nicht automatisch Fehlerfreiheit. Keine universelle Korrektur und keine große Wiederholung ohne diese Entscheidung.

---

# 31. Provenienz, Versionshistorie und Übergaberegeln

## 31.1 Bestätigte Nutzerangaben aus diesem Chat

**[U01] Versuchsprotokoll, 21.09.2026:** Kevin bestätigt auf die Frage nach den Iterationen: „Bei den samplerates schon. Bei den Laufzeiten nicht, da hab ich nach einer festgelegten Zeit abgebrochen“. Diese Aussage klärt den damaligen Versuchstyp, nicht jeden historischen effektiven Aufruf oder Completion-Zähler. **Nachtrag 28.09.:** Durch [U03] ist ihr Geltungsbereich auf die historischen Jetson-Sweeps einzugrenzen; nicht auf spätere GPU-/Jetson-Zeitläufe oder Hailo verallgemeinern.

**[U02] Implementierungsauftrag, 21.09.2026:** Kevin bittet, die Implementierung zu beginnen, das Tool testfertig zu bauen und Joris zum Testen zu geben; Fokus ausdrücklich PicoScope. Die spätere tatsächliche Auslieferung ist die in Abschnitt 29 dokumentierte separate Python-Kette. Kein Beleg einer bereits erfolgten Installation oder Hardwareabnahme bei Joris.

Diese Aussagen sind Gesprächsquellen ohne eigene Datei-Hashes. Nicht mit Dateizeitstempeln oder Hardwaretestbelegen gleichsetzen.

## 31.2 Quellenregister

Die folgenden Dateien lagen für dieses Update tatsächlich vor. SHA-256 bezeichnet genau die lokale Datei, nicht ein ungeprüftes entferntes Repository. Berichtsarchive enthalten Ableitungen; Primär-YAMLs und historische Pilotexporte sind gesondert identifiziert. Detail-JSONs und Originalquellstellen innerhalb der Archive bleiben die Zahlen-/Codeprovenienz. Das Original-Plotarchiv ist keine neue Rohdatenquelle.

**[Q00] `Energy_Paper_TIM_KnowledgeBase(3).md`**  
Hochgeladene Ausgangs-KB; Planungs- und Zahlenstand 27.08.2026.  
SHA-256: `917722cb5e0a93987bb7dcab12f4e4bc9b0e31a58ee82393b8456a3a2b1ef29b`

**[Q01] `masterarbeit-helper-scripts-master.zip`**  
Original-Snapshot: Messsteuerung, Rust-Auswertung und Python-Plotter.  
SHA-256: `37a7c227987ede4430cba7b8e3d8f440681de127b6327c1610c47db1e8c27de9`

**[Q02] `urecs-data-collector-master.zip`**  
Original-Snapshot: Collector und fest referenzierter Rust-Pico-Wrapper.  
SHA-256: `f1ce0645e47b4e691f5aa662cdd9700ef3aacb3c140c7df9a1fc43167d1a30e5`

**[Q03] `urecs_samplerate_audit.zip`**  
Erstes Softwareaudit; Quellstellen und zehn Reproduktionstests, keine Hardwareprüfung.  
SHA-256: `6534c12160d38d933dd1298719021342e329694d23e2829cbaf93380ff768eb8`

**[Q04] `sweep_audit.json`**  
Auf Twix ausgeführter Audit der 15 GEMM-FP16-300-s-Läufe bei 2 kS/s.  
SHA-256: `037db24658ea8883d2bcd9f7e316c5368a9c6cc4f94571f3c537be60a509e754`

**[Q05] `power_measurement_structure_20260921_112838.txt`**  
Verzeichnisstruktur der Samplerate-Reihen und Beispiel-YAML aus der Dauerreihe.  
SHA-256: `ee1c74072339f5943f1057007d261957c250d811a0381add73fdb55a8e654127`

**[Q06] `urecs_sweep_metadaten_20260921_114344_ae34c1a4.zip`**  
1.620 originale Ergebnis-YAMLs und Dateimetadaten aus vier direkten Sweeps.  
SHA-256: `73895d6c0728364c0d8de1d8ea7d510bc09b596b82d78939a0f0cf3c77c8a9b6`

**[Q07] `urecs_sweep_analysis_20260921.zip`**  
Metadatenanalyse, Tabellen, 16-Spuren-Auswahl und Pilotprogramm.  
SHA-256: `dae09b9924f41b4ff2464eabcae03d7aa77551a3b76be5131df66d36cd4ff511`

**[Q08] `urecs_trace_pilot_20260921_104248Z_3b24c032.zip`**  
Auf Twix erzeugte 16-Spuren-Fensterstatistiken und 0,1-s-Aggregate; keine NPY-/U/I-Rohdaten.  
SHA-256: `65546af61114cafcf774ba5a09fd05eb67b94cb7fc05da7f9637997be3deea98`

**[Q09] `urecs_trace_pilot_befunde_20260921.zip`**  
Pilot-Nachanalyse, Zahlenzerlegung, Diagramme und Reproduktionsskripte.  
SHA-256: `473ef3a34892492e04ecc79bf072f53e1b4cc5623c6fcbf8606cdad0e231fc1a`

**[Q10] `power_measurements_plots.zip`**  
33 Ergebnis-PDFs; keine neuen Rohmesswerte; Hailo/samplerates leer.  
SHA-256: `8287a80d4ac56ef92b75c1de524946a8517f9ecc8578d2ac358cb77bd823945e`

**[Q11] `urecs_full_review_20260921.zip`**  
Plot-Gegencheck, YAML-/Vektorvergleich, zusätzliche Softwarefehler und damaliger Umbauplan.  
SHA-256: `5af6c81a5fe39d4b65f069585d57270c0a65f9a497506195452563bc18d4beb3`

**[Q12] `pico_validation_v1.0.0-rc1.zip`**  
Tatsächlich ausgelieferte separate Python/ctypes-PicoScope-Validierungskette; keine Rust-Patches.  
SHA-256: `73049522cb9e8183290f25d5afcbc787ba167789da943d43e4639c1e8e81f6cb`

**[Q13] `pico_validation_release_qa.json`**  
Ausgelieferter Releasebeleg: ZIP-Hash, Integritätsprüfung, erneute 126 Tests aus frischer Entpackung; Hardware false.  
SHA-256: `8ef860fc90c2660868fc93e34c9fdbb056990c3cd5610438893ecd6c1769e0e6`



**Besonders wichtig – exakter Softwarestand für Joris:**

```text
pico_validation_v1.0.0-rc1.zip
SHA-256: 73049522cb9e8183290f25d5afcbc787ba167789da943d43e4639c1e8e81f6cb
Releasebeleg: pico_validation_release_qa.json
Hardwareabnahme: pending
Original-Rust-Projekte geändert: false
```

## 31.3 Priorität bei Widersprüchen

Ein späterer Datenbefund ersetzt eine frühere Hypothese **nur in seinem geprüften Geltungsbereich**: `use_voltage: true` im Sweep hebt nicht `false` in der 300-s-Dauerreihe auf; Innenleistung eines Pilotruns ist nicht der Median aller Wiederholungen; ein Plotlabel ist kein verlässlicher Quellenbeleg, wenn der Plotter die Zuordnung vertauscht. [Q04, Q06, Q09, Q11]

Für den **Implementationsstatus** haben [Q12, Q13] Vorrang vor dem älteren Umbauplan [Q11]. Rust-/SDK-Patches sind geplant gewesen, aber nicht ausgeliefert. Für Hardware-PASS wäre ein neuer expliziter Hardwarebeleg erforderlich; Software-/Releasebelege können ihn nicht ersetzen.

Für **kanonische Common-Reference-/Paperzahlen** bleibt die Hierarchie aus Abschnitt 4 maßgeblich; die Audit-Ergänzung ändert sie nicht von Hand. Neue experimentelle Erkenntnisse nur mit Dateiname, Toolversion, Messgrenze, Fensterregel und Status übernehmen.

## 31.4 Historischer Änderungsstand 2026-09-21.1

Version **2026-09-21.1**, Ausgangsdatei [Q00] mit `status_date: 2026-08-27`. Ergänzt wurden bestätigtes Versuchsprotokoll, historische Datenstruktur, schrittweise Evidenzlage, Code-/Plotterbefunde, differenzierte FP32/FP16/INT8-Interpretation, tatsächlicher RC-Implementationsumfang, Testgrenzen und Joris-Abnahmeplan. Die bisherigen wissenschaftlichen Ergebniszahlen wurden nicht manuell verändert.

Fristen, externe Richtlinien, ein späterer Paperstand und Hardwareergebnisse wurden in diesem Dokumentationsupdate nicht neu recherchiert oder erfunden. Die dokumentierten 126 Tests wurden aus vorhandenen Releasebelegen übernommen und hier nicht nochmals als Hardware-/Softwaretest ausgeführt. Quellen-/Hash- und Tabellenkonsistenzprüfungen dieses KB-Updates sind davon getrennt.

Das Begleitpaket enthält diese vollständige Markdown-KB, die unveränderte Ausgangs-KB, ein Änderungsprotokoll, einen Textdiff, ein Quellenmanifest und die Dokumentationsprüfungen. Es dupliziert weder die großen Rohdaten noch sämtliche Software-/Auditpakete. Bei einem neuen Chat die **vollständige neue KB** hochladen; bei konkreter Zahlen-/Codeprüfung zusätzlich das jeweils referenzierte Paket bereitstellen.

---

# 32. Update 28.09.2026 – RTX A6000, Jetson-Rückbau und Protokollfrage

> Historischer Zwischenstand der Revision 1. Ergebnisse des damals noch offenen Zeit-/Iterationsvergleichs stehen jetzt in Abschnitt 38. Keine erneute Messung aus diesen früheren Plänen ableiten.

## 32.1 Quellen und Status

Neue Primärangaben sind die von Kevin eingefügten Messenger-Ausschnitte vom **22.–25.09.2026**, die aktuelle Aufgabenstellung, die einzelne angehängte GPU-Bildschirmabbildung und **`SetupInfo.md`**. Die strukturierte Quellennotiz im Updatepaket ist eine redaktionelle Extraktion der Chatnachrichten, kein vollständiger Messenger-Rohexport. [U03–U05, Q15–Q16]

**Die neue Jetson-Messreihe ist laut Nutzer abgeschlossen; ihre numerischen Ergebnisse wurden hier noch nicht gelesen.** Sie liegen auf dem Laborrechner, nicht automatisch auf Twix oder im Chat. Die GPU-Figur liefert nur einen qualitativen Hinweis auf fehlenden systematischen Hochratenabfall und geringe Wiederholungsstreuung. Weder Rohdatenvollständigkeit noch „alle 15 Werte im Plot verwendet“ oder absolute Kalibriergültigkeit lassen sich daraus bestätigen. Die genaue FP16-/FP32-Zuordnung der einen hochgeladenen Bildschirmabbildung bleibt offen; im Chat wurden beide GPU-Reihen als getrennte Fotos erwähnt.

Aktueller Diagnoseweg: **zuerst den bestehenden Jetson-100-s-Lauf mit Joris’ aktuellem Setup und bestehenden Ergebnisdateien auswerten; anschließend iterationsbasierten Vergleich unter möglichst unveränderten Bedingungen. Nicht gleichzeitig auf den separaten RC-Collector wechseln.** Dies ist eine lokale methodische Reihenfolgeentscheidung für diesen Vergleich, keine Rücknahme des RC-Abnahmeplans. [U05]

## 32.2 Korrektur der bisherigen Pauschalaussage „Samplerates = Iterationen“

Die frühere Nutzerbestätigung [U01] ist für die **historischen Jetson-Sweeps** zu lesen, nicht für alle Plattformen und spätere Messkampagnen. Neu maßgeblich ist diese Differenzierung:

| Datenkohorte | Arbeits-/Abbruchkriterium nach aktueller Quellenlage | Was nicht daraus folgt |
|---|---|---|
| Historische Jetson-Samplerate-Sweeps, Grundlage des 21.09.-Audits | Iterationsvorgabe, z. B. GEMM-FP32 `trtexec --iterations=100 --useSpinWait` | Keine nachträglich bestätigte feste Ausführungsdauer oder exakte Completion-Zahl pro Run |
| Jetson-Dauerreihen | Nach vorgegebener Zeit abgebrochen | Kein iterationsgleicher Vergleich und kein automatisch exaktes Inferenz-Zeitfenster |
| RTX-A6000-GEMM-FP32/FP16-Samplerate-Reihen, 24./25.09. | Externer Abbruch nach 100 s; 15 Wiederholungen je Rate nach Joris | Kein Benchmark mit derselben erledigten Arbeit wie beim historischen Jetson-Sweep |
| Neuer Jetson-GEMM-FP32-Samplerate-Lauf, gestartet 25.09. | Ebenfalls 100-s-Abbruch, zum Anschluss an GPU-Protokoll | Noch kein hier geprüftes Ergebnis; kein belegter RC-Hardwaretest |
| Hailo-Messungen im beschriebenen `hailortcli`-Arbeitsablauf | Laufzeit direkt im Benchmarkkommando angegeben, laut Joris keine Iterationsvorgabe in diesem Aufruf | Nicht automatisch dasselbe wie externer Prozesskill; keine allgemeine Beschränkung aller HailoRT-Versionen/APIs |
| Geplanter Jetson-GEMM-FP32-Vergleich nach Urlaubübergabe | Joris’ dokumentierter Iterationsaufruf, ohne äußeren 100-s-Abbruch | `--iterations=100` ist keine unabhängige Bestätigung von exakt 100 abgeschlossenen Inferenzen |

Joris begründet das neue GPU-Zeitprotokoll damit, keine passende Iterationsanzahl suchen zu müssen. Der neue Jetson-Zeitlauf sollte methodisch daran anschließen. **Ein technischer Zwang zum Timeout oder eine zu große unvermeidliche Iterationszahl wurde nicht genannt.** [U03]

**GPU = RTX A6000, nicht Jetson.** Die GTX 960 wurde davor als Funktions-/Bootprüfung des Aufbaus verwendet; ihre Funktion ist kein Beleg der späteren A6000-Messgrenze. [U03, U04]

## 32.3 Einordnung der neuen Beobachtung

Die GPU-Figur zeigt nach Nutzer/Joris keinen vergleichbaren monotonen Hochratenabfall wie die alten Jetson-GEMM-Reihen. Das unterstützt die Untersuchung des Benchmarkprotokolls, **beweist aber nicht „Iterationsmodus verursacht den Fehler“**: Plattform, Betriebszustände und Sitzung unterscheiden sich ebenfalls.

Der Rückbau der gleichen Pico-/INA-Messkette an den Jetson ist deshalb diagnostisch wertvoll. Innerhalb dieses Aufbaus lassen sich Zeitabbruch und Iterationsvorgabe sinnvoller vergleichen als GPU gegen historischen Jetson. Dennoch müssen Engine, Inferenzoptionen, Tool-/Kalibrierstand, Abtastraten, Messbereiche, Spannungspfad und Zustand/Pausen dokumentiert bleiben. Zwei nacheinander gemessene Serien sind noch kein vollständig randomisierter, thermisch kontrollierter kausaler Nachweis.

„50 S/s reicht nicht“ ist als Joris’ Beobachtung aus der Figur zu dokumentieren, **nicht** als neuer universeller Fehlergrenzennachweis. Toleranz, Fenster, tatsächliche Werteauswahl und unabhängige Referenz fehlen dafür. Die vorhandenen Common-Reference-Ergebnisse in Abschnitt 8 bleiben unverändert.

## 32.4 Noch offene Auswertung des neuen Jetson-Laufs

Zu prüfen sind zunächst alle tatsächlichen nativen Ratenordner und Ergebnis-YAMLs: Anzahl/IDs, Energie, ausgegebene Dauer, `E/T`, Typ/Spannungspfad/gegebenenfalls explizites Szenario, Streuung **ohne** Perzentil-Ausschluss und interne Vergleiche zu 2 kS/s. Auch die Laufnummern und niedrigen Raten müssen im Bericht bleiben.

Danach die vorhandenen Leistungsfolgen für **2 kS/s und 5 MS/s, jeweils IDs 0 und 7** prüfen: alte Energie reproduzieren, 1/5/10-s-Innenfenster und 0,1-s-Verlauf aus allen Samples vergleichen. Das sind vier ausgewählte Folgen, kein Vollscan der gesamten neuen Kampagne. Nur in YAMLs vorhandene Werte werden als bekannt ausgegeben. Samplezeit/Hardwarekontinuität bleiben ohne unabhängige Belege unverifiziert.

Ein neuer Quellcode-/Binary-Snapshot auf Memmert ist nötig, da Joris am 22.09. das Szenariohandling geändert hat. **Die älteren hochgeladenen ZIPs dürfen nicht als aktuelle Memmert-Produktionsversion ausgegeben werden.** Ein heutiger Snapshot ist umgekehrt noch kein rückwirkender Buildnachweis des Zeitlaufs.

---

# 33. Setup-, Kalibrier- und Messgrenzeninformationen aus der Übergabe

## 33.1 Shelly-/Versorgungsvergleich

Joris nennt **100 mA und 3.500 mA** als die tatsächlich herangezogenen Kalibrierpunkte; der Rest sei Verifikation. Der Chat enthält weder die vollständigen Messwerte noch alle Fits/Koeffizienten und deren eindeutige Zuordnung zu Jetson, Hailo und GPU. Zweipunktfit und Verifikationspunkte im Paper getrennt kennzeichnen. [U04]

Für die Setup-Vorschau wurden ungefähr **70 W Shelly AC raw bei Jetson** und **20 W bei Hailo** als passend bestätigt. Kevin nennt ein **TTi-Doppelnetzteil**; Joris berichtet einen ständig laufenden Lüfter. Der hohe Versorgungsanteil wird im Gespräch als plausible Erklärung vermutet. **Leerlaufaufnahme, Erwärmung und Wirkungsgrad wurden damit nicht gemessen.** Eine separate Idle-Messung der tatsächlich angeschlossenen Versorgung, bei definierten Kanälen/Lasten und gleichem AC-Messumfang, bleibt offen.

Joris nennt außerdem Jetson **79 %** und Hailo **75 %**. Bezugslast, Roh-/Basisbehandlung und Zuordnung dieser Zahlen sind im Chat nicht eindeutig. Diese Angaben bleiben berichtete Werte mit offener Definition; nicht aus anderen Plotbalken stillschweigend „passend rechnen“ oder als allgemeine Netzteilwirkungsgrade veröffentlichen.

**Keinen 50-%-Shelly-Sensorfehler aus einer AC/DC-Differenz ableiten.** Messgrenzen, Versorgungsgrundlast und lastabhängige Verluste sind nicht dasselbe wie ein Instrument-Gain-/Offsetfehler. Für das Paper `AC raw` und eine modell-/baselinebezogene Vergleichsgröße mit genauer Transformationsdefinition auseinanderhalten. „Calibrated“ nicht ohne Erklärung mit „AC-Sensor repariert“ gleichsetzen.

## 33.2 GPU-Benchsetup und Hostanteil

Am 22.09., 14:00, meldet Joris beim GPU-Benchsetup circa **30 W Shelly-Differenz** mit annähernd 1:1-Skalierung; der Rechner war eingeschaltet und idle. Das ist als **berichtete Setup-/Host-/Versorgungsdifferenz** aufzunehmen. Ein reiner Hostverbrauch oder reiner Shelly-Offset wurde nicht unabhängig isoliert. Kein pauschaler 30-W-Abzug außerhalb der betreffenden Konfiguration.

Beim frühen Hardwaretest war laut Chat die als Mainboard-/PEG-Stromverbindung bezeichnete Verbindung nicht angeschlossen. Anfangs sollte nur geprüft werden, ob das System bootet; später lief die GTX 960 und wurde durch die A6000 ersetzt. Die Aussagen enthalten keinen vollständigen endgültigen Verdrahtungsplan. **Vor `GPU board power` müssen Slot-12-V, Slot-3,3-V und Zusatzversorgung einschließlich der tatsächlichen Einspeisung/Messstelle geklärt sein.** Eine anfängliche Bootprüfung ist keine Freigabe der gesamten Messgrenze. [U04]

## 33.3 Geänderte Kalibrierungsprofile und Jetson-Rückbau

Joris berichtet am 22.09., 13:58, ein neues Handling mehrerer Szenarien im `power_calculation`-Tool; externe Konfigurationsdateien seien langfristig sinnvoll. Für Jetson fehlten im damaligen aktuellen Programm noch Korrekturfaktoren. **Das ist eine datierte Entwicklungsangabe, keine pauschale Widerlegung der kalibrierten historischen Jetson-Daten.** Aktuelle Source, aufgerufene Binaries und Datenkohorten müssen getrennt überprüft werden.

Der am 25.09. begonnene Jetson-Zeitlauf verwendet laut Nutzer die **unveränderte GPU-Messkette**. Der Nutzer stuft die Kalibrierung für diesen Jetson-Test als falsch ein. Folgerungen für den Protokollvergleich:

- Keine Kalibrier-/Messbereichs-/Hardwareänderung zwischen Zeit- und Iterationsserie; bewusst beibehaltenen Iststand dokumentieren.
- Plattformname, `--picoscope-measurement-type` und `--measurement-environment` sind verschiedene Größen. **Nicht allein wegen Jetson automatisch `INA225`/`jetson` auswählen**, ebenso wenig `INA225NVGPU`/`nvgpu` aus der vermuteten Herkunft raten.
- Originalaufruf und gespeicherte Metadaten abgleichen. Der Szenarioname ist in älteren YAML-Formaten nicht gespeichert; ein fehlender Wert darf nicht geraten werden.
- Ein für alle Punkte gleicher positiver Faktor kürzt sich in normierten Trends. Bei einem angenommenen affinen Leistungsmodell `P' = aP+b` gilt dagegen `ΔP'/P' = aΔP/(aP+b)`. Kanaloffsets bei der U×I-Bildung, Nichtlinearität, Sättigung oder Pegelschwellen können sogar darüber hinaus wirken.
- Daher: zunächst **relative Diagnose in bestehender Skalierung**, keine absoluten W/J- oder Effizienzclaims. Auch „falsche Kalibrierung ist immer egal“ wäre zu weitgehend.

## 33.4 Einordnung des separaten Python-RC

Die Übergabe beschreibt die bestehende **`measurement_suite.py` → Rust-Collector → `power_calculations`**-Kette. Es gibt in diesen neuen Chatbelegen keine Bestätigung, dass Joris `pico_validation_v1.0.0-rc1` installiert, abgenommen oder für die GPU-/Jetson-Läufe verwendet hat. Die 126 RC-Softwaretests und der historische Audit bleiben gültige frühere Softwarebelege; **Hardwarestatus des RC bleibt pending**. [Q12, Q13, Q15]

---

# 34. Memmert – konkrete Betriebsübergabe aus SetupInfo

## 34.1 Rechner und Pfade

| Zweck | Angabe aus SetupInfo / Chat | Einordnung |
|---|---|---|
| Aufnahmerechner | `jwachsmuth@memmert`, alternativ `jwachsmuth@129.70.144.168` | Befehle für Collector/Suite hier, nicht auf Twix oder direkt auf dem Jetson starten |
| GPU-Benchrechner | `joris@10.42.0.210`; von Memmert `ssh bench` | Nicht mit dem Jetson gleichsetzen |
| Jetson NX an u.RECS | `nx@10.42.0.44` | Ziel für den aktuellen GEMM-Test |
| Messdaten laut SetupInfo | `/media/jwachsmuth/satassd/power_measurements` | Reale Existenz prüfen |
| Messdaten laut Chat | `/media/satassd/power_measurements/...` | Kann Alias/abweichender Mount sein; nicht blind als identisch ausgeben |
| Collector-Source | `/media/jwachsmuth/dataRec/RustroverProjects/urecs-data-collector` | Aktueller Git-/Datei-/Binary-Stand separat sichern |
| Skripte und Analyzer | `/media/jwachsmuth/dataRec/PycharmProjects/data_analysis` | Hier `uv run ...` ausführen |
| Neuer Jetson-Zeitlauf | `<Messdatenbasis>/jetsonMeasurements/samplerates/gemm/fp32` | Nutzer meldet abgeschlossen; Ergebnisse noch nicht im Chat geprüft |
| Jetson-GEMM-Engine | `/home/nx/hpc/pwgemmnet-fp32.engine` | Existenz und Hash vor Iterationslauf prüfen, nicht neu bauen |
| TensorRT-Programm | `/usr/src/tensorrt/bin/trtexec` auf Jetson | Installierte Version/Optionen mit `--help` erfassen |

Passwörter stehen ausschließlich in der vom Nutzer gelieferten Original-`SetupInfo.md` und werden hier nicht dupliziert. Das Updatepaket enthält nur eine entsprechend bereinigte Textkopie; Hash und Name der vollständigen Originalquelle bleiben dokumentiert. Keine Zugangsdaten in Shellargumente, Messkonfigurationen, Review-ZIPs oder öffentliche Paperartefakte kopieren.

## 34.2 Weitere übergebene Dateien

Jetson: `~/CLionProjects/untitled` ist laut SetupInfo das Interfaceprogramm zur Übertragung der HailoRT-Leistungsmessung. Weitere Skripte: `~/hailoexec.sh`, `~/idle_gpio_trigger.sh`, `~/llm_launch.sh`, `~/random_yolo_execution.sh`, `~/modelfile`; Modellordner `~/hpc` und `~/yolo`.

Benchsetup: ebenfalls `~/CLionProjects/untitled`, hier als Interface zur Übertragung von `nvidia-smi`-Leistung; Startskripte ähnlich zum Jetson, ONNX-/Engine-Dateien im Home-Verzeichnis. „Ähnlich“ ist kein Beleg identischer Argumente oder identischer Dateien. [Q15]

## 34.3 Tool-Bedienung

Alle Benchmarks werden laut SetupInfo durch `measurement_suite.py` in einer **tmux-Sitzung** durchgeführt. Skripte mit **`uv run [skript.py]`** starten; das bestehende Projekt-Environment wird verwendet. Kein separates venv-Aktivieren erforderlich. Vorhandene tmux-Sitzungen prüfen und nicht pauschal beenden. Beim Plotten auf einem Headless-Host statische Dateien statt benötigter GUI verwenden.

Samplerate-Auswahl erfolgt über bestehende Ordner **`<Abtastrate>Sps`** im neuen Messpfad. Duration-Auswahl erfolgt separat über **`<Laufzeit>s`**. Die beiden Modi nicht mischen. Die CLI-Dokumentation der Umgebungs-/Mess-Typ-Werte ist laut Joris teilweise unvollständig; deshalb tatsächlichen Aufruf und Source sichern.

Dokumentierte Optionen für die Samplerate-Suite:

```text
--command "ssh <ZIEL> <BENCHMARKBEFEHL>"
--measurement-path <MESSORDNER>
--run-count 15
--picoscope
--picoscope-use-measured-voltages
--pico-samplerate-sweep
--picoscope-measurement-type <INA225|INA225NVGPU>
--measurement-environment <nvgpu|jetson|m.2|static>
```

Die spitzen Klammern beschreiben Optionen, **keine einzutippenden Literale**. Mess-Typ und Szenario müssen vom echten Originalaufruf stammen. ASCII-Anführungszeichen verwenden, nicht die typografischen Anführungszeichen des SetupInfo-Beispiels.

Für Duration-Sweeps dokumentiert SetupInfo zusätzlich `--picoscope-samplerate 2000 --shelly --nv-gpu --duration-sweep`; das beschreibt den Bench-Aufruf und wird nicht ungeprüft für den Pico-only-Jetson-Test übernommen. Bei einem Benchmarkskript, dessen letzter Parameter die Laufzeit ist, wird dieser beim Duration-Sweep weggelassen, weil die Suite ihn ergänzt. Für den jetzigen iterationsbasierten **Samplerate**-Vergleich wird kein 100-s-Argument angehängt.

## 34.4 Datenerhalt statt blindem Speicherfreimachen

> Ergänzung Revision 2: Die abgeschlossene Memmert-Jetson-Kopie wurde inzwischen unter Kevins Home auf Sprite archiviert und laut Nutzer erfolgreich per rsync-Prüfsummenlauf verglichen. Lokale Freigabe der alten FP32-NPYs wurde daraufhin ausdrücklich beauftragt; kein automatischer Freibrief zur Löschung neuer Iterations-/Pausenrohdaten. Details in 41.

SetupInfo beschreibt Joris’ bisheriges Vorgehen: Daten nach einem Durchlauf sichern, dann Platz freimachen, bislang unter anderem durch Löschen der `.npy`-Dateien. **Diese historische Betriebsnotiz ist keine automatische Löschfreigabe für die jetzt benötigten Diagnose-Rohdaten.**

Für Kevin: Ergebnisse und insbesondere `oscilloscope.npy` des 100-s-Laufs unverändert erhalten. Einen neuen Geschwisterordner für den Iterationsversuch verwenden. Freien Platz vor Start prüfen. Ein Metadaten-/Review-ZIP mit YAMLs und Statistiken ist **kein vollständiges Rohdatenbackup**. Kein `rm *.npy`, kein automatisches Rebuild, kein Überschreiben des abgeschlossenen Laufordners.

Die bestehende Legacy-Suite kann Parquet-Dateien selbst nach der Auswertung löschen; das wird durch einen unveränderten Wiederholungsaufruf nicht automatisch behoben. Für direkte U/I-Rohdatensicherung später explizit den dafür geprüften Aufnahmepfad wählen, nicht den bekannten Capture-only-Schleifenfehler aktivieren.

---

# 35. Diagnoseauftrag und Copy-&-Paste-Helfer vom 28.09.2026

> Historische Bedien-/Planungshistorie. Die tatsächlich benötigten FIX1/FIX2-Korrekturen und die Durchführung sind in 38/41 ergänzt. Der 45er-Lauf wurde bereits abgeschlossen; diese Startbefehle jetzt nicht nochmals verwenden.

## 35.1 Gewählte Vergleichsstrategie

Zuerst alle Metadaten des fertigen Jetson-100-s-Sweeps plus vier ausgewählte Leistungsfolgen lesen. Danach **drei bereits vorhandene Raten (2 kS/s, 250 kS/s, 5 MS/s), 15 Wiederholungen = 45 Aufnahmen** iterationsbasiert aufnehmen. Dies ist ein gezielter Diagnosevorschlag, nicht eine schon durchgeführte neue Kampagne und nicht automatisch der komplette 27-Raten-Sweep.

Bei angenommenen 100 s je Versuch entsprächen 45 Lastphasen etwa 75 Minuten; hinzu kommen ein möglicher Dry-run, Aufnahmevor-/nachlauf und Legacy-Inline-Auswertung. Joris’ Einschätzung der Laufzeit des Iterationsaufrufs ist ausdrücklich **ungetestet**. Keine garantierte Endzeit oder exakte Speichergröße behaupten.

Neu ausgeliefert wird **`jetson_ab_20260928.zip`**, Hilfsversion **1.0.0**, mit `jetson_ab.py`, wiederverwendetem numerischem `trace_core.py`, Tests, README und konkreten Befehlen. Es ist **kein neuer Messcollector**: Analysepfad nur lesend; Startpfad ruft nach Prüfungen und Operatorbestätigung die lokale Legacy-Suite auf.

## 35.2 Analysefunktionen

- Liest native `<Rate>Sps/<numerische Lauf-ID>/results.yaml` und prüft erwartete IDs, Typ/Rate, endliche positive E/T-Werte, fehlende Dateien und explizite Metadaten.
- Berichtet Energie, YAML-Dauer und E/T getrennt, mit Median, Mittelwert, Quartilen und getrennt bezeichneter Populations-/Stichprobenstandardabweichung. Keine 5.–95.-Perzentil-Selektion über Wiederholungen.
- Prüft bei 2 kS/s und 5 MS/s standardmäßig IDs 0 und 7 aus den gespeicherten NPYs; benutzt die ursprünglichen inklusiven Grenzen und 1/5/10-s-Innenfenster. Im abgeschnittenen Speicherformat werden fehlende Grenzen ausdrücklich als solche behandelt.
- Prüft YAML-Hashes und NPY-Größe/mtime vor/nach Scan, aber bezeichnet dies nicht als Hardware-Kontinuitätsbeleg. Nichtendliche Werte oder ungültige Grenzen werden nicht durch Nullen/Clipping repariert.
- Sichert aktuelle ausgewählte Source-Dateien, Git-Zustand und auffindbare Binary-Hashes getrennt. Keine Behauptung, der aktuelle Build sei garantiert der Aufnahmebuild.
- Schreibt ausschließlich neue Berichtsordner/ZIPs unter `~/energy_analysis/jetson_ab_reports/`, außerhalb des Quellbaums. Kein Aufruf des möglicherweise weiterhin trimmenden alten Plotters.

## 35.3 Startschutz und unveränderte Konfiguration

Der Starthelfer sucht die echte Original-Suite-Zeile des exakten 100-s-Quellordners in Bash-History/tmux und lässt sie ausdrücklich auswählen. Er exportiert nicht die kompletten Historien. Alternativ `--baseline-command-file` mit der echten, vollständig aufgelösten Startzeile. **Ist sie nicht auffindbar, wird vor dem Messstart gestoppt; die SetupInfo-Platzhalter sind kein Ersatz.**

Er überprüft vorhandene Zielgruppe/IDs, Pico-only-/gemessene-Spannung-Modus, expliziten Mess-Typ und Szenario gegen verfügbare YAML-Felder. Der Originalaufruf muss zum Jetson-Ziel und zum dokumentierten 100-s-Timed-Helper mit derselben Engine passen. Ein unbestätigter SSH-Alias, ein anderes Modell, ein unbekanntes Default-Szenario oder ein Capture-only-/Duration-Sweep wird nicht automatisch umgedeutet.

Vor Messstart werden lokale Programme/CLI, SSH-/Enginezugang, Engine-Hash, Ziel-`trtexec --help`, mögliche aktive Messprozesse und freier Speicher geprüft. Das tatsächlich im Originalaufruf genannte Timed-Skript wird gelesen und für den Vergleich angezeigt. Andere Inferenzoptionen (SpinWait, Warm-up, Transfers, CUDA-Graph, Streams/Batch) und umgebungssetzende Skriptteile müssen geprüft werden. Erst mit **`GLEICH`** und **`START`** wird die neue Messung freigegeben.

Die aktuelle Legacy-Kette bleibt einschließlich ihrer Inline-Analyse/Fensterlogik erhalten. Zusätzliche Filter-/Fensteroptionen des Originalaufrufs werden übernommen. Ein gegebenenfalls alter `--duration`-Planungswert wird entfernt, damit die Suite die Dauer des neuen Iterationsbefehls durch ihren üblichen Dry-run bestimmen kann. Das ist keine Vorgabe, den neuen Benchmark nach 100 s zu beenden.

Neue Messdaten: Geschwisterordner `fp32_iterations100_gpu_chain_<UTC>_<ID>`. Neue Protokoll-/Sourcebelege separat im Home. Nur Ratenordner plus eine Manifestdatei im Messwurzelordner, damit die Legacy-Suite keine fremden Unterordner als Raten interpretiert.

Auf dem Jetson entsteht eine eigene Loghülle unter `/home/nx/energy_analysis/jetson_ab_logs/<ID>/`. Sie startet Joris’ dokumentierten Befehl ohne externen 100-s-Abbruch und behält stdout/stderr sowie Prozessanfang/-ende/Exitcode für jeden Aufruf einschließlich Dry-run. Der Logging-Vorlauf ist eine ausdrücklich dokumentierte Zusatzinstrumentierung, kein exakter Hardwaremarker. Bei einem Abbruch nicht einfach erneut starten, bevor verbleibende Prozesse auf Memmert und Jetson geprüft wurden.

## 35.4 Joris’ Iterationskommando und trtexec-Semantik

Aus SetupInfo, dort als etwa 100 s **ungetestet** markiert:

```bash
/usr/src/tensorrt/bin/trtexec --loadEngine=/home/nx/hpc/pwgemmnet-fp32.engine --iterations=100 --useSpinWait
```

Dieses Kommando wird für den historischen Anschluss zunächst wörtlich übernommen. **Keine unbemerkte Ergänzung von `--duration=0` oder `--warmUp=0`.** Solche Optionen könnten für eine separat definierte exakte Arbeitsvorgabe sinnvoll sein, wären aber eine zusätzliche Protokolländerung.

NVIDIA dokumentiert für TensorRT 10.x `--iterations` und `--duration` als Mindestvorgaben, wobei die längere Bedingung erfüllt wird; standardmäßig werden auch Warm-up und eine Mindestdauer verwendet. Die lokal installierte Version muss per Hilfe/Log bestätigt werden. Deshalb angeforderte Iterationen, gemeldete abgeschlossene Arbeit, Prozesszeit und Samplefenster getrennt protokollieren. [W01]

## 35.5 Copy-&-Paste-Einstieg

ZIP zuerst ins Home-Verzeichnis auf Memmert kopieren; vollständige Befehle stehen im Helferpaket. Im dort bestehenden Analyseprojekt:

```bash
cd /media/jwachsmuth/dataRec/PycharmProjects/data_analysis
uv run python "$HOME/energy_analysis/jetson_ab_20260928/jetson_ab.py" analyze
```

Zuerst Bericht/Fehler und aktuelle Metadaten prüfen. Danach, in einer eigenen tmux-Sitzung, ohne gleichzeitige RC-/Kalibrier-/Hardwareumstellung:

```bash
cd /media/jwachsmuth/dataRec/PycharmProjects/data_analysis
uv run python "$HOME/energy_analysis/jetson_ab_20260928/jetson_ab.py" start-iterations
```

Der Helfer gibt nach dem Durchlauf den passenden `analyze --protocol iterations100 --source <tatsächlich neuer Pfad>`-Befehl und einen Kopierbefehl für Ziel-Benchmarklogs aus. Keine fest erfundene Lauf-ID oder Ausgabedatei verwenden. Bei einer Stopmeldung zuerst deren fehlende Evidenz beheben, nicht die falsche Kalibrierung durch eine geratene ersetzen.

## 35.6 Interpretationsregeln nach Rückgabe

| Ergebnis | Zulässige nächste Schlussfolgerung |
|---|---|
| Neuer Jetson-100-s-Lauf ohne Hochratenabfall | Qualitativer Anschluss an GPU-Beobachtung; Protokolleinfluss plausibler, aber noch keine isolierte Ursache |
| Abfall erscheint beim gleichen aktuellen Jetson-Aufbau wieder im Iterationslauf | Stärkerer Zusammenhang mit Arbeits-/Zeitprotokoll; Prozesszeit, Innenleistung, Ränder und Startzustand prüfen |
| Beide neuen Jetson-Reihen ohne Abfall | Historischer Zustand/Tool-/Sitzungseinfluss wird prüfenswerter; Iterationen allein nicht als Ursache bestätigt |
| Beide neuen Reihen zeigen Abfall | Timeout allein erklärt ihn nicht; Niveau-/Fenster-/Aufnahmekette weiter eingrenzen |
| Energie ändert sich, aber E/T und/oder Innenleistung nicht gleich | Energie-, Prozessdauer- und Fenstermischung nicht zu einer pauschalen Leistungsbehauptung zusammenziehen |
| Typ/Szenario/Inferenzoptionen unterschiedlich oder Source-Zuordnung fehlt | Kein sauber isolierter A/B-Protokollvergleich; zuerst Provenienz klären |

Ein erneuter Timeout-Block nach einem auffälligen Iterationsblock kann einen späteren Zustands-/Reihenfolgecheck unterstützen. Er ist **nicht automatisch gestartet oder bereits geplant ausgeführt**. Die methodische Kernaussage bleibt: direkte separate Sweeps und Same-Trace/Common-Reference untersuchen unterschiedliche Effekte.

---

# 36. Neue Quellen, offene Punkte und Versionsstand

## 36.1 Quellenzusatz

**[U03]** Vom Nutzer eingefügte Chatnachrichten vom 24./25.09. zu GPU/Jetson, 100-s-Abbruch, Rückbau, RTX A6000 und Hailo-Laufzeitprotokoll. Keine nachträglich rekonstruierte Completion-Tabelle.

**[U04]** Vom Nutzer eingefügte Chatnachrichten vom 22./23.09. zu Zweipunktkalibrierung, Verifikation, Shelly-/Versorgungskette, Szenariohandling und frühem GPU-Hardwaretest.

**[U05]** Aktueller Auftrag: Joris im Urlaub; Kevin übernimmt, fertigen Jetson-Zeitlauf prüfen und Iterationsmessung vorbereiten/starten. Messkette nach Nutzer unverändert von GPU übernommen; Kalibrierung für Jetson nicht gültig. Durchlaufstatus als Nutzerangabe, nicht als hier verifiziertes Dateiergebnis.

**[Q14]** `Energy_Paper_TIM_KnowledgeBase_2026-09-21.md`, vollständige vorherige Fassung, Version `2026-09-21.1`. Diese, nicht die ältere August-Fassung, ist die Basis des jetzigen Updates.

**[Q15]** `SetupInfo.md`, aktueller Nutzerupload, 67 logische Textzeilen in der bereitgestellten Darstellung. Konkrete Rechner-/Pfad-/CLI-Übergabe; Kommentare zur unvollständigen CLI-Doku, Datenlöschung und teilweise falschen Plotlabels sind als Quellenangaben erhalten. Bereinigte Kopie im Updatepaket, Passwörter nicht dupliziert.

**[Q16]** Nutzerbild `7d9803f8-a5f9-4bb3-870b-10b7fbcb087f.png`, 1280×506 Pixel. Qualitative GPU-Sweep-Abbildung; genaue Modellzuordnung offen. Keine hier aus Pixeln erzeugte neue Zahlenreferenz.

**[W01]** NVIDIA, *Performance Benchmarking using trtexec*, TensorRT 10.x, Abschnitt *Duration and Number of Iterations*, am 28.09.2026 abgerufen: https://docs.nvidia.com/deeplearning/tensorrt/10.x.x/performance/benchmarking.html . Externe technische Semantikquelle, nicht Quelle der Nutzer-Messergebnisse und kein Nachweis der installierten Jetson-Version.

Die SHA-256-Werte der lokalen Quelldateien und des neuen Helfers sind im Quellenmanifest des Updatepakets enthalten. Die Chatquellen besitzen keinen behaupteten Originaldatei-Hash; `NEUE_QUELLEN_NOTIZ.md` ist als redaktionelle Ableitung gekennzeichnet.

## 36.2 Priorität und noch fehlende Belege

- Die präzisierte Protokollmatrix in Abschnitt 32 ersetzt die frühere allgemeine Formulierung „alle Samplerates iterationsbasiert“ nur hinsichtlich ihres Geltungsbereichs. Historische geprüfte Zahlen bleiben unverändert.
- `SetupInfo.md` und heutige Source-/CLI-Abzüge beschreiben Joris’ aktuelle Arbeitsumgebung, nicht automatisch den 21.09.-ZIP-Stand. Der RC bleibt ein unabhängiges Paket.
- Neue Jetson-/GPU-YAMLs, geplottete volle Stichprobe, aktueller Kalibrierprofil-/Koeffizientenstand, tatsächliches Timed-Skript und Benchmark-Completionlogs bleiben bis zur Rückgabe offen.
- Die GPU-Messgrenze und Netzteil-/Hostbaselines sind noch nicht unabhängig belegt. Berichtete 70/20/30 W und 79/75 % nicht zu neuen kanonischen Wirkungsgraden zusammenführen.
- Keine neue Messung, SSH-Verbindung oder Hardwareprüfung wurde allein durch dieses Dokumentationsupdate als ausgeführt bestätigt.

## 36.3 Versionshistorie 2026-09-28.1

Vollständige Fortschreibung von [Q14]. Ergänzt: datierte Protokollkorrektur, RTX-A6000-Identität, Jetson-Rückbau/Zeitlauf, Zweipunkt-/Verifikationsangabe, Versorgungs-/Shelly-/Hosthinweise mit Unsicherheiten, aktuelle Memmert-Übergabe, sichere Daten-/Konfigurationsregeln, getrennte alte Kette versus RC und konkrete lokale Analyse-/Startbefehle.

Der aktuelle Abschnitt 0 und Anschlussauftrag wurden entsprechend umgestellt. Ältere Prioritäten bleiben zeitlich als 21.09.-Stand markiert. Kanonische Common-Reference-/PSD-/Tek-Zero-Werte wurden nicht geändert. Venue-/Submissionregeln wurden nicht erneut geprüft; deren ältere Prüfdatierung bleibt bestehen. Neue Resultate des aktuellen Jetson-Zeitlaufs oder einer noch nicht erfolgten Iterationsmessung wurden nicht erfunden.


## 36.4 Verifizierte neue Quelldateien

| Kennung | Datei | SHA-256 |
|---|---|---|
| Q14 | `Energy_Paper_TIM_KnowledgeBase_2026-09-21.md` | `ff1b729404bf9829a5fb4138a53616ff220d5c941bf75c7abb9d6f137600483f` |
| Q15 | `SetupInfo.md` | `77adfcf2bb9d2e299e919ddb006aece28bb965cc8ee254e8091c0ffe868d8621` |
| Q16 | `7d9803f8-a5f9-4bb3-870b-10b7fbcb087f.png` | `afcf8ddcdaa1b72354be4a10f6532a3fa198528e03259e3a3817649f0dc62b28` |

Die Hashes kennzeichnen die vorliegenden Originalbytes. Der Q15-Hash bezieht sich auf die vertrauliche Originalnotiz; im Updatepaket liegt nur eine ausdrücklich redigierte Fassung ohne Passwörter. Die redaktionelle Chatnotiz ist keine als Original ausgegebene Chatdatei.

---

# 37. Verbindlicher Arbeitsrahmen – Klarstellung und aktueller Auftrag

## 37.1 Bestandsdaten sind die Basis, nicht zu ersetzende Vorversuche

Kevin hat ausdrücklich klargestellt: Die fast zweimonatige Kampagne wird **nicht erneut aufgenommen**. Die alten Daten müssen weiter verwendet werden; die vorgesehenen Grafikkartenmessungen ergänzen sie im bisherigen Stil. Joris ist nach Nutzerangabe in ungefähr vier Wochen nicht mehr verfügbar, Kevin hat keine Kapazität für eine neue Großkampagne. [U06]

Das verbietet **keine** wenigen Hardwaretests zur Ursachenklärung. Der zuvor erzeugte Nachtrag `ENTSCHEIDUNG_UND_BEFUNDE.md` [Q24] war insofern zu eng interpretiert. **Eine vollständige Offline-Neuauswertung der betroffenen Bestände inklusive Neuerzeugung der Grafiken ist ausdrücklich akzeptiert.** Erwartung „einige Stunden bis vielleicht ein Tag“ ist eine Nutzer-/Planungsabschätzung, keine vorab belegte obere Rechenzeitgrenze. Berechnung und Entwicklung/Prüfung der Fensterregel getrennt budgetieren.

Der aktuelle Auftrag [U07] lautet: Knowledgebase vollständig fortschreiben und den kleinen Pausentest konkret vorbereiten. Neue Quellen/Zahlen mit Provenienz ergänzen; historische Dateien nicht überschreiben. Weder pauschaler Gain-/Offset-/Thermikabzug noch Trimmen unbequemer Wiederholungen. Kein neues umfassendes GUM-/Monte-Carlo-Programm.

## 37.2 Vorgehen nach dem Test

1. Sechs gezielte Pausen-Testläufe bei konstanter Rate plus ausdrücklich ungewerteter Konditionierung, Temperatur-/Takt-/Benchmarkprotokolle.
2. Die Resultate dienen der Ursachenklärung und der Auswahl einer belastbaren Auswertungsregel, **nicht** als Ersatz oder Korrekturfaktor aller alten Messungen.
3. Vollständige versionierte Offline-Auswertung der relevanten direkten Jetson-/Hailo-/GPU-Reihen. Metadaten-/Rohverfügbarkeit, Profile, Protokolle und Messgrenzen vorher katalogisieren. Resume/Cache nach Quellenfingerabdruck, keine ständigen Gigabyte-Neuscans für jeden Plot.
4. Legacy, neue operational definierte Last-/Prozessfenster und Innenfenster getrennt ausgeben. Interne Burstpausen behalten; mehrkanalige Zeitzuordnung nicht aus gleichen Indizes erfinden.
5. Betroffene Diagramme gemeinsam regenerieren (richtige Quellenlabels, alle gültigen Wiederholungen, Energie/Dauer/Leistung separat). PSD nur bei einer tatsächlich betroffenen Abhängigkeit neu rechnen.

Die vorhandenen NPY-Leistungsfolgen erlauben neue Fenster und Integration, aber keine Rekonstruktion verlorener Samples oder beliebiger kanalweiser Kalibrierfaktoren. Wo alte ungefitte Grenzen mangels Logs nicht rekonstruierbar sind, neue Detektion als neue, versionierte Regel deklarieren. Keine Auswahl der Fenster nach dem gewünschten Vorzeichen.

---

# 38. A/B- und Fenster-Gegencheck – jetzt abgeschlossene Mess- und Auswertungsstände

## 38.1 Zeitlauf, Profilalias und Helferkorrekturen

Der vollständigere Zeitreview [Q19] enthält 405 YAMLs/27 native Raten/je 15 Wiederholungen sowie vier geprüfte Spuren (2 kS/s und 5 MS/s, Lauf 0/7). Der ältere Review `081008Z_86abc93c` war ein Metadaten-Zwischenstand ohne NPY-Scan; seine YAMLs/Quellsnapshots sind identisch, kein zweiter unabhängiger Versuch.

Alle Zeit-YAMLs: `measurement_environment: NvGpu`, `oscilloscope_results.msmt_type: INA225`, `use_voltage: true`. Der native Aufruf war `INA225NVGPU/nvgpu`. Im aktuellen Analyzer ordnen die Stringparser `ina225` und `ina225nvgpu` beide dem Analyzer-Enum `INA225` zu; die Umgebung bleibt getrennt. **Der Collector unterscheidet die zwei Namen weiterhin und wählt andere Bereiche/Offsets. Nicht den Aufnahmeparameter umschreiben.** [Q18, Q19]

FIX1 (`1.0.1-fix1`) behob den Fehlalarm `nvim measurement_suite.py`: ein Editor ist kein Aufnahmeprozess. FIX2 (`1.0.2-fix2`) prüft die belegte Analyzer-Aliaszuordnung plus die eingefrorenen Quellen/Binaries. Kein Patch des Collectors oder der Kalibrierung. Für alle Aufrufe die bestehende uv-Projektumgebung über `--directory /media/jwachsmuth/dataRec/PycharmProjects/data_analysis` wählen; aus `~` ohne Projekt war NumPy nicht verfügbar.

Zeitlauf: Median E/T im vorhandenen 102-s-Fenster 35,245648 W bei 2 kS/s gegenüber 36,812596 W bei 5 MS/s; Medianenergie +4,445793 %. Lauf 0: Innenleistung nach je 10 s Beschnitt 36,164 → 36,292 W (+0,353 %); Lauf 7: 36,156 → 38,146 W (+5,505 %). Das erste Hochratenereignis verhält sich anders als spätere derselben Rate. Keine allgemeine positive Ratenkalibrierung daraus ableiten.

## 38.2 Durchgeführter 45-Läufe-Iterationsversuch

Primärdatenbasis: [Q20, Q21], Auswertung [Q22].

```text
Memmert:
/media/jwachsmuth/satassd/power_measurements/jetsonMeasurements/samplerates/gemm/
fp32_iterations100_gpu_chain_20260928_121829Z_e0c5787c/

Lokaler Ablauf-/Quell-/Logplan:
/home/jwachsmuth/energy_analysis/jetson_ab_reports/
iteration_plan_20260928_121829Z_e0c5787c/

Jetson-Logs:
/home/nx/energy_analysis/jetson_ab_logs/20260928_121829Z_e0c5787c/
```

45 Ergebnisse, jeweils IDs 0–14 bei 2000/250000/5000000 S/s. **46 Targetprotokolle = ein Dry-run plus 45 Aufnahmen**, nicht 46 gewertete Messungen. Jeweils Exit 0, TensorRT PASSED und 100 Queries in der Timing-Trace sowie eine Warm-up-Query; Queries nicht automatisch als Einzelbilder ausgeben (Input `512x2048x14x14`). Die Source-/Binary-Snapshots stimmen im A/B-Export überein; das beweist nicht rückwirkend jeden historischen Build.

Die Aufnahmefolge war **5 MS/s ×15 → 250 kS/s ×15 → 2 kS/s ×15**. Das Diagramm sortiert die Raten anders. Datei-mtime ist kein Ersatz für diese Logzuordnung.

| Rate | Nachgelagerte Analyse, Median [s] | Voriges Prozessende bis nächster Start, Median [s] | TensorRT-Zeit für 100 Queries, Median [s] |
|---:|---:|---:|---:|
| 5 MS/s | 101,322 | 121,196 | 97,4798 |
| 250 kS/s | 5,458 | 21,614 | 109,554 |
| 2 kS/s | 0,072 | 16,172 | 111,334 |

**Belegt:** Die sequenzielle Nachauswertung verlängert die tatsächlichen Benchmarkpausen ratenabhängig. Zudem werden dieselben 100 Queries in TensorRTs eigener Zeitbasis unterschiedlich schnell erledigt (bei 2 kS/s ca. 14,2 % länger). **Nicht belegt:** welche Temperatur-/Takt-/Power-Limit-Änderung dies vermittelt; die alten Logs enthalten keine entsprechende Zeitreihe. Prozesspause bedeutet nicht garantiert völlige elektrische Inaktivität.

Aussagekräftige Übergänge: erster 5-MS/s-Lauf nach nur 11,112 s Prozesspause noch 109,525 s TRT; späterer 5-MS/s-Lauf 7 nach 120,863 s Pause 97,358 s. Erster 250-kS/s-Lauf nach 120,624 s Pause 97,632 s, späterer Lauf 7 derselben Rate nach 21,502 s Pause 109,765 s. Das spricht gegen einen ausschließlich momentanen Raten-Skalierungsfehler, beweist aber keinen einzelnen thermischen Mechanismus.

## 38.3 Ergebnis der vollständigen Neuintegration ohne Dauerzwang

[Q23] enthält die auf Memmert ausgeführte reine Offline-Integration aller 45 NPYs (72,27 GB). Die hier vorliegenden Ergebnis-JSONs/Hashes wurden gegen Plan und Original-YAMLs abgeglichen [Q25]. Das sind keine neuen Aufnahmen. Die ursprünglichen Detektorgrenzen wurden im aktuellen Fall aus Indizes, protokollierter Detektordauer und dem bekannten symmetrischen Fit rekonstruiert; bei anderen historischen Reihen ist dies ohne Logs nicht pauschal möglich.

Alle Wiederholungen eingeschlossen; numerische Angaben in unveränderter NvGpu-Skalierung. Zeitspanne = `(N−1)/fs`, nicht die alte Dauerbezeichnung `N/fs`.

| Rate [S/s] | n | Legacy-Energie [J] | Energie ohne Dauerzwang [J] | Median Zeitspanne ohne Dauerzwang [s] | Relative ungezwungene Energie zu 2 kS/s |
|---:|---:|---:|---:|---:|---:|
| 2000 | 15 | 3585.775574 | 3998.095334 | 111.198500 | +0.000000 % |
| 250000 | 15 | 3599.480124 | 3942.563416 | 109.470708 | -1.388959 % |
| 5000000 | 15 | 3708.508000 | 3679.184790 | 97.344281 | -7.976562 % |

Je Größe wird der Median aus den 15 Einzelwerten gebildet. Median(E)/Median(T) ist nicht allgemein Median(E/T). Die korrekt pro Lauf berechneten Leistungsmediane ohne Dauerfit betragen **35,959884 / 36,054903 / 37,786808 W** für aufsteigende Raten. Die alte Energie wird mit maximal **5,603988 × 10⁻⁸ J** Differenz reproduziert.

**Kernbefund:** Derselbe 45er-Bestand zeigt im erzwungenen 100-s-Fenster **+3,422758 %**, im operationalen Detektorfenster ohne Dauerzwang **−7,976562 %** bei 5 MS/s gegenüber 2 kS/s. Der Fenstereinfluss auf die Richtung ist damit numerisch belegt. Das ist kein Beweis einer 8 % besseren Messgenauigkeit oder einer kausal ratenbedingt um 8 % effizienteren GPU. 2 kS/s ist nur interne Vergleichsgruppe.

Die ungezwungenen Signalfenster liegen bis auf maximal etwa 0,189819 s bei der jeweiligen TRT-Timing-Trace. Das stützt reale Laufzeitvariation, ist aber weder ein genauer GPU-Kernelmarker noch ein Beweis des ADC-Takts oder lückenloser USB-Aufnahme. Das alte Integral war innerhalb seiner Grenzen numerisch korrekt; die Gleichsetzung seines festen Fensters mit der vollständigen 100-Query-Arbeit war nicht belastbar.

**Abgeschlossen:** diese 45 Dateien ohne Fit neu integriert. Nicht aus einem älteren Abschnitt erneut zur gleichen Nachrechnung auffordern. Daten-/Logarchive behalten.

## 38.4 Weiterhin offene Identität und Warnungen

Logs nennen **Orin**, **TensorRT 10.3.0**, **7619 MiB Device Global Memory** und eine Engine-Kompatibilitätswarnung für ein anderes Gerätemodell sowie unstabile GPU-Compute-Zeit. Daraus weder sofort einen exakten Modul-SKU noch eine bewiesene Fehlerursache ableiten. Frühere 16-GB-Plattformangabe und aktuelles Gerät getrennt führen; Modell-/OS-/Engine-Identität im kleinen Test nur lesen und dokumentieren, nicht mitten im Vergleich neu bauen oder Betriebsmodi ändern.

Die TensorRT-Banner-„Application Clock Rates“ sind laut Log ausdrücklich keine aktuellen Taktraten. Der Collector meldete in der 250-kS/s-Gruppe ganzzahlig 249999 S/s, während die YAML 250000 nutzt. Diese Rundungs-/Metadatenabweichung nicht als unabhängige Taktmessung oder Erklärung des Prozenttrends behandeln; kein manueller 249999-Faktor.

---

# 39. PSD/Common Reference – abgegrenzter Analysezweig

Kevin stellt klar: Die PSD-Arbeit lief über die Tektronix-/PicoScope-Daten und ein anderes Softwarewerkzeug, nicht über die jetzt diskutierten Samplerate-Energie-Boxplots. Dies entspricht der bestehenden Projekttrennung in 4–8.

- **Tek-/Pico-Spektren:** eigener `common_reference_psd_tool_v0.7.3`-Zweig, Signalspuren/paired Aufnahmen und eigene Fenster-/Idlebehandlung. Kein automatischer Defekt dieser Spektren durch den Dauerfit in Joris' anderem Energiepfad. Keine pauschale Neuberechnung oder Änderung von PSD-, Tek-Zero-, Bandbreiten- oder Common-Reference-Grenzwerten.
- **Same-Trace/Common Reference:** verschiedene Raster aus derselben physischen Spur bei gleichen Grenzen. Nicht gleichzusetzen mit dem Zustand/Pauseneffekt separater nativer Ausführungen. Keine universelle absolute Gerätekalibrierung daraus ableiten.
- **Gemischte Artefaktpakete:** Ein unter PSD/Paper gespeicherter Bericht kann importierte Dauerstudien-/Energietabellen enthalten. Betroffene importierte Tabellen und den gesonderten GEMM-FP16-Langzeitanker auf tatsächliche Herkunft prüfen, ohne deswegen sämtliche Tektronix-Spektren anzuzweifeln.

Die neu zulässige vollständige Neuauswertung bezieht sich vorrangig auf **betroffene direkte Samplerate-/Dauer-/Telemetrie-Energieauswertungen**. Eine erneute PSD wird nur notwendig, wenn ihre verwendeten Signalgrenzen/Quellwerte nachweislich geändert werden. Andere Software allein garantiert keine absolute Fehlerfreiheit, der hier belegte Defekt rechtfertigt aber keine unbelegte Übertragung auf diesen anderen Analysezweig.

---

# 40. Kleiner Pausentest – konkret vorbereitet, Ergebnisse ausstehend

## 40.1 Fragestellung und Plan

**Bei konstant 2 kS/s und identischer Engine:** Führt die lange Pause zu einer kürzeren Timing-Trace/höheren Innenleistung, ähnlich den vorherigen Hochratenläufen? Wie verhalten sich dabei gelesene Temperaturen und aktuelle Frequenzwerte? Ein unveränderter Ratenparameter trennt den Pausenfaktor von dessen früherer Kopplung an die Rate.

Umfang: **sechs gewertete Testausführungen (drei je Bedingung) plus eine eigene, ungewertete Konditionierung** derselben 100 Queries. Diese zusätzliche Ausführung ist im Plan/Log markiert und wird nicht in die 3+3-Statistik aufgenommen. Keine weiteren stillen Dry-runs; internes TensorRT-Warm-up bleibt unverändert.

Vorab festgelegte gemischte Reihenfolge der Pausen **vor** den sechs Testläufen:

```text
Konditionierung → 20 s → Test 1 → 120 s → Test 2 → 120 s → Test 3
               → 20 s → Test 4 → 20 s → Test 5 → 120 s → Test 6
```

Dies ist ein dokumentierter gemischter Plan, nicht nachträglich als großer randomisierter kausaler Versuchsplan auszugeben. Initiale Zustandsunterschiede und Carry-over bleiben sichtbar; Konditionierung ist kein thermisches Gleichgewicht. Drei Werte pro Bedingung sind diagnostisch, keine allgemeine Signifikanzgarantie.

## 40.2 Umsetzung und absichtliche Änderungen

Paket **`jetson_pause_test_20260928_v1.zip`**, Version 1.0.0. Die vorhandene native Legacy-Collector-Binary wird **einmal kontinuierlich** bei 2000 S/s gestartet. Die neue kleine Python-Steuerung bestimmt ausschließlich die Ausführungsfolge/Pausen auf dem Jetson und die nachgelagerte Analyse. Kein Rust-Patch, kein SDK-/Treiberupdate, kein Wechsel auf den nicht hardwareabgenommenen Pico-RC. Keine Nutzung des fehlerhaften `skip_power_calculation`-Schleifenpfads.

**Bewusst anders als beim 45er-Sweep:** kontinuierlicher Collector statt Öffnen/Schließen je Lauf, keine Zwischenanalyse, monotone Pausensteuerung auf dem Zielrechner und 1-Hz-Telemetrie. Das ist die gezielte Protokollvariation, nicht ein unbemerkt anderer Versuchsablauf. Unverändert: Engine-Hash, Benchmarkoptionen, Hardware, Messprofil, Probe-Faktoren, Collector/Analyzer-Quell-/Binary-Stand.

```text
Collector: INA225NVGPU / nvgpu / X10 / X10 / 2000 S/s
Engine: /home/nx/hpc/pwgemmnet-fp32.engine
Engine SHA-256: fa18c8ed8042ba56e159e7f5dd4856f7a01621c67248002fbdd975d71f9df0ca
Benchmark: /usr/src/tensorrt/bin/trtexec --loadEngine=<obige Engine> --iterations=100 --useSpinWait
```

Pause: Ende des vorigen Kindprozesses bis Startanforderung des nächsten auf `time.monotonic_ns()` des Jetson. Tatsächliche Abweichung wird protokolliert; >0,5 s außerhalb des Sollabstands wird nicht als regulär zeitlich kontrollierter Lauf weiterverwendet. Keine Shell-/Hash-/Auswertungsarbeit zwischen den Benchmarks außer kleinen Logs und kontinuierlicher Telemetrie. Je Benchmark 240-s-Watchdog, insgesamt 40 Minuten; Watchdog/Fehler → unvollständiger Diagnoseversuch, keine automatischen Retries.

Der native Collector-Aufruf enthält `-d=1s`: Nach dem **geprüften** alten `main.rs` ist das die Mindestwartezeit vor dem Warten auf das SSH-Kommando, kein Abbruchlimit. Das Zielskript fügt selbst 5 s Nachlauf hinzu. Collector-Startsignal wird geprüft; es ist kein unabhängiger Hardware-Samplemarker.

## 40.3 Zustandsdaten, Fenster und unveränderte Skalierung

Nur lesend und einmal pro Sekunde: thermische Zonen, CPU `scaling_cur_freq`, devfreq `cur_freq`, verfügbare Lüfterdrehzahlen. Zusätzlich eigenes `tegrastats --interval 1000`, falls vorhanden; nur dieser eigene Prozess wird beendet. Keine pauschalen Stop-/Killkommandos und kein Setzen von Takt, Governor, Lüfter oder Power Mode. Nicht lesbare Werte bleiben ausdrücklich fehlend; ohne lesbare Temperatursensoren kein Start. [W02]

Die Quell-Parquetspalten `voltage` und `current` bleiben erhalten. Sie sind bereits vom Collector probe-/offsetskaliert, **keine ADC-Rohcodes**. Offline-Leistung wie im aktuellen Analyzer:

```python
power = voltage * (current + 0.002755526) * 38.45601442
```

Keine neu behauptete elektrische Jetson-Kalibrierung. Diese Formel ist nur für die gehashte vorhandene NvGpu-Konfiguration übernommen. Primärer Diagnoseausgang ist die unabhängig protokollierte TRT-Timing-Trace bei 100 gemeldeten Queries; kein Energieeffizienzvergleich pro Einzelbild.

Sekundär: sieben plausible signalbasierte Hüllen im kontinuierlichen Verlauf, ohne Dauerfit. Binmittel 0,1 s, Glättung 0,5 s, primäre Kontrastschwelle 50 % zwischen 10./80. Perzentil, Sensitivitäten 40/60 %, kurze Brücken bis 1 s, Phasen mindestens 20 s. Zuordnung über Reihenfolge plus Dauer-/Abstandsplausibilität, **keine exakte Hardware-Synchronisation**. Bei Ambiguität bleiben Energiezuordnungen offen; Logs und komplette Verlaufsmittel bleiben erhalten. Innenfenster je 10 s Randbeschnitt zusätzlich.

Zielprozess- und Telemetriezeiten teilen dieselbe monotone Zieluhr. Pico-Samplezeit ist nicht damit hardwaregekoppelt. Legacy-Collector garantiert weiterhin keine nachgewiesene verlustfreie USB-Erfassung und keine unabhängig kalibrierte Hardwarezeit. Zustandstelemetrie kann selbst geringe Last erzeugen; sie ist zwischen den Bedingungen gleich, ihre Rückwirkung aber nicht separat quantifiziert.

## 40.4 Ausführung auf Memmert

ZIP zuerst ins Home von `jwachsmuth` kopieren; Befehle in tmux. Paket liegt neben FIX2, nichts überschreiben:

```bash
unzip -n "$HOME/jetson_pause_test_20260928_v1.zip" -d "$HOME/energy_analysis"

uv run --no-sync --directory /media/jwachsmuth/dataRec/PycharmProjects/data_analysis \
  python "$HOME/energy_analysis/jetson_pause_test_20260928_v1/pause_test.py" verify

uv run --no-sync --directory /media/jwachsmuth/dataRec/PycharmProjects/data_analysis \
  python "$HOME/energy_analysis/jetson_pause_test_20260928_v1/pause_test.py" selftest

uv run --no-sync --directory /media/jwachsmuth/dataRec/PycharmProjects/data_analysis \
  python "$HOME/energy_analysis/jetson_pause_test_20260928_v1/pause_test.py" run --arm
```

Vor `run`: keine laufende Aufnahme, Paket/Sourcen/Binaries/Engine passend, lesbare Telemetrie und mindestens 2 GiB lokal frei. Kein globales Nachinstallieren von NumPy oder anderen Bibliotheken; Joris' bestehende Umgebung verwenden. Nach `--arm` ist **START** die ausdrückliche Startfreigabe. Keine erneute History-Auswahl/`GLEICH` erforderlich, da derselbe inzwischen belegte Zustand eingefroren ist.

Planungsdauer ca. 20–25 Minuten bei bisherigen Benchmarklaufzeiten, kein fest zugesagter Endzeitpunkt. Ein kontinuierlicher 2-kS/s-Stream liefert zwei Float64-Nutzkanäle mit 32 kB/s (vor Kompression), etwa 40 MB bei 20 Minuten. 2-GiB-Platzprüfung enthält große Reserve, keine mehrere-Hundert-GiB-Forderung wie beim 45er-Hochratenlauf.

Neue Ergebnisse lokal unter `<Messdatenbasis>/jetsonMeasurements/pauseTests/pause_<UTC>_<ID>/`; Targetlogs unter `/home/nx/energy_analysis/pause_tests/pause_<UTC>_<ID>/data/`. Nach Abschluss werden Logs kopiert, die Offline-Auswertung und PNGs erzeugt und die Review-ZIP als `Upload:` ausgegeben. Keine neuen Tests bei `fetch`/`analyze`/`pack`; diese Befehle dienen der Nachbearbeitung des tatsächlich ausgegebenen Ordners.

## 40.5 Softwareprüfung und Hardwarestatus

34 registrierte Tests: **33 bestanden; 0 Errors/Failures; 1 native Polars-Parquet-Prüfung mangels installiertem Polars in dieser Umgebung übersprungen**. Numerik-/Reportlauf mit klar gekennzeichnetem gemocktem Parquet-Reader sowie sieben tatsächlichen lokalen Test-Kindprozessen geprüft. Zusätzlich 46 originale historische TRT-Logs mit dem neuen Parser erfolgreich gelesen. Auf Memmert kann die vorhandene Polars-Umgebung den nativen Roundtriptest ausführen; `run` prüft die Abhängigkeiten vor Start. Belege in `TEST_OUTPUT.txt`, `TESTERGEBNISSE.md` und `test_evidence/` des Pakets.

**Noch nicht durchgeführt:** dieser Pausentest auf Memmert/Jetson, echte SSH-/Pico-/USB-Hardwareabnahme der neuen Steuerung, Temperatur-/Taktdiagnose aus neuen Messungen. Die Softwaretests sind kein Beweis des vermuteten Zustandsmechanismus. Bestehende direkte Messungen mit FIX2 sind real; sie sind aber kein Test des jetzt neuen Pausenskripts.

---

# 41. Archiv, Provenienz und nächste Auswertungsentscheidung

## 41.1 Speicherorte und bestätigte Freigabe

Altdaten Joris: `/homes/jwachsmuth/power_measurements/` via Twix. Am 28.09. Memmert-Jetson-Daten zusätzlich unter **Kevins** `/homes/kmika/power_measurements/memmert_archive_20260928/jetsonMeasurements/` archiviert. Terminalausgabe zeigt `/homes/kmika` als NFS von `sprite.TechFak.Uni-Bielefeld.DE`. Transfer: 11.149 reguläre Dateien, 264,62 GB; der Nutzer bestätigt anschließenden `rsync -rlcn`-Prüflauf ohne Unterschiede/Fehler, Log `~/energy_analysis/jetson_archive_check_20260928_124952.txt`. Das leere Log allein ist ohne den bestätigten erfolgreichen Aufruf kein unabhängiges Backup-Zertifikat.

Danach hat Kevin vollständige lokale Freigabe des alten abgeschlossenen FP32-Zeitlaufs verlangt. Der gelieferte Befehl entfernt dessen lokale `.npy`, **behält YAMLs/Ordner** für die Baselineprüfung. Keine hier vorliegende konkrete Löschabschluss-Ausgabe behaupten. Die Archivkopie bleibt vollständig; falls lokal NPYs fehlen, aus dem Archiv lesen, nicht erneut messen.

Die spätere Iterationsreihe `...121829Z_e0c5787c` wurde **nach** dieser Sicherung erzeugt. Ihr vollständiges Rohdatenbackup ist durch Ergebnis-ZIPs nicht bewiesen und gesondert sicherzustellen. Gleiches gilt für den jetzt erst geplanten Pausentest. Compact Reviews enthalten keine komplette Rohdatensicherung; keine automatische Löschung.

## 41.2 Interpretation nach Pausentest

- Lange Pause geht bei derselben Rate mit kürzerer TRT-Zeit und dem entsprechenden Leistungs-/Temperatur-/Taktverlauf einher: Zustandseinfluss wird konkret gestützt. Nur soweit tatsächliche Telemetrie es trägt von Temperatur-/Taktmechanismus sprechen.
- Kein konsistenter Unterschied: Pause allein erklärt die früheren Zusammenhänge nicht ausreichend. Keine große Wiederholungsmessung automatisch daraus ableiten.
- Ungültige Pausentoleranz, andere Engine oder fehlende plausible Signalzuordnung: Teilbefunde/Logs behalten, keine saubere kontrollierte Energiegegenüberstellung behaupten.

In allen Fällen bleiben die alten Messreihen die Datenbasis. Neue Fensterenergie und Legacy-Fenster als unterschiedliche Messgrößen behandeln, nicht den neuen Zahlenwert als universelle Ratenkorrektur einsetzen. PSD-Basis getrennt lassen. Der nächste große Arbeitsschritt ist eine einheitliche Offline-Auswertung, nicht eine neue Hardwarekampagne.

## 41.3 Quellenzusatz und Nutzerentscheidungen

**[U06]** Nutzerklarstellung: einzelne Hardwaretests sind erlaubt; alte Daten müssen weiterverwendet werden, keine Wiederholung der Kampagne. Vollständige Neuauswertung aller betroffenen Grafiken ist möglich. PSD lief über andere Tek-Scope-/Softwarekette.

**[U07]** Aktueller Auftrag: vollständige Knowledgebase aktualisieren und den Test mit den Pausen konkret vorbereiten. Kein Beleg seiner bereits erfolgten Hardwareausführung.

**[W02]** NVIDIA, Tegrastats Utility, Jetson Linux Developer Guide r36.2, am 28.09.2026 technisch herangezogen: https://docs.nvidia.com/jetson/archives/r36.2/DeveloperGuide/AT/JetsonLinuxDevelopmentTools/TegrastatsUtility.html . Bedeutung von GR3D_FREQ und thermischen Zonen; keine Quelle für Nutzermessergebnisse, keine Behauptung des aktuell installierten BSP-Stands.

Die folgenden SHA-256 kennzeichnen tatsächlich vorhandene lokale Original-/Artefaktdateien. Berichte sind Ableitungen; die Primärlogs/-YAMLs/-Reintegrationsausgaben bleiben separat benannt. Der alte Entscheidungsnachtrag [Q24] wird hinsichtlich der Hardwaretest-Beschränkung durch U06/U07 ersetzt, nicht als neue aktuelle Sperre kopiert.

**[Q17] `Energy_Paper_TIM_KnowledgeBase_2026-09-28.md`**  
SHA-256: `4a70958e7b5f8fc439366007019fe7b4c6c840f82490be570c8bee92b96bcfd6`

**[Q18] `jetson_ab_20260928_fix2.zip`**  
SHA-256: `2a65f2effa20118db00060f56ec2f8b76e989b97e757dbf1f553a3ffebef8faa`

**[Q19] `jetson_timeout100_review_20260928_082244Z_a7280c89.zip`**  
SHA-256: `9f858870d41c6a6c8346378db698e5d034ea42492317c2a74427a8c6eb1e3c9e`

**[Q20] `jetson_iterations100_prozesslogs_UjUd0fLq.tar.gz`**  
SHA-256: `3190b1f8343e2977ad2e170f9f5c6a450ee31ed727b4814d10f084d7ed9c3359`

**[Q21] `jetson_iterations100_review_20260928_154623Z_051c4270.zip`**  
SHA-256: `aaf1f45c31b63bff9191b1888fc9d7fe1336921929c9c498bdff0e02b8645e65`

**[Q22] `jetson_ab_review_20260928.zip`**  
SHA-256: `3d56bc20f0ae959530bf0b6eba697a5df2400d9b8e8139074a8854dc69cfd007`

**[Q23] `jetson_unforced_review_20260928_175640Z_331inc_w.zip`**  
SHA-256: `492604f238444cf9f7a78e483b0bfd4f059984d37e8730698b674a7cada588be`

**[Q24] `energy_paper_bestandsauswertung_20260928/ENTSCHEIDUNG_UND_BEFUNDE.md`**  
SHA-256: `e546b1526fdbed7dfa9bc6a80e751ce4eb342c0291ddf2372db73d31b3204d2b`

**[Q25] `energy_paper_bestandsauswertung_20260928/EXPORTPRUEFUNG.json`**  
SHA-256: `24b327f09a9b6566191acc51866a7a8aea6cd0e94a19a9a3d50e3dd0ff81685b`

**[Q26] `jetson_pause_test_20260928_v1.zip`**  
SHA-256: `70fd7471930ff74ff9443800e6d3c596f7c9bb99428cf99f35c48e50217ae0a5`

**[Q27] `Eingefügter Text(20260928-104945).txt`**  
SHA-256: `8b869d101c947e4824dcd7a8fa03e8343d2fc68c93288da7a4eba6c5e3d2db55`

## 41.4 Versionsstand und Abgrenzung dieses Updates

Version **2026-09-28.2** basiert auf der vollständigen Revision 1 [Q17]. Aufgenommen sind die seitdem real zurückgegebenen FIX2-/Zeit-/Iterations-/Archiv-/Unforced-Befunde, die korrigierte Umfangsentscheidung, die PSD-Abgrenzung und das neue Pausentestpaket [Q26]. Der aktuelle Anschlussauftrag in Abschnitt 0 ist ersetzt; frühere Tagespläne sind als historische Zwischenstände markiert. Abschnitt 8/9 und die wissenschaftlichen Basiszahlen sind unverändert.

Dieses Dokumentationsupdate führt weder die alte NPY-Reintegration erneut noch eine echte neue Hardwaremessung aus. Neu ausgeführt wurden ausschließlich lokale Softwaretests des Pausentestpakets und Dokument-/Provenienzprüfungen. Die vollständige Bestands-Neuauswertung ist erlaubt und vorgesehen, aber noch nicht pauschal als fertig deklariert. Nicht bestätigte Zugriffe, thermische Ursachen, FPGA-/GPU-Konfigurationen, zukünftige Paperannahme oder neu geprüfte Publikationsfristen werden nicht ergänzt.


---

# 42. Hardware-Pausentest – Rückgabe und Review am 29.09.2026



Bei **unveränderter nomineller Abtastrate von 2 kS/s**, derselben Engine und einer kontinuierlichen PicoScope-Aufnahme unterscheiden sich die Ergebnisse nach 20 und 120 Sekunden Prozesspause deutlich. Nach langer Pause beginnen die Läufe kühler, TensorRT erledigt dieselben 100 Queries schneller, die aufgezeichnete Innenleistung ist höher und die Energie im signalbasierten Lastfenster geringer. Der Pauseneinfluss ist damit in diesem Versuch demonstriert; ein Abtastratenwechsel ist dazu nicht erforderlich. Die konkrete thermische/elektrische Begrenzung ist nicht identifiziert.

Quelle der Messdaten ist Q29 (im Review P01). Q30 dokumentiert die Ausführung; Q31 ist byteidentisch mit dem Kurzbericht im ZIP. Die Nachprüfung ist ein Export-/Log-/Bin-/Telemetrieaudit, **keine neue Aufnahme und keine erneute Integration der nicht mitgelieferten Parquet-Rohkanäle**. Quellen-IDs werden in `QUELLEN.json` aufgelöst.

## 1. Vollständigkeit und Ausführung

- Ein ungewerteter Konditionierungslauf (ID 0), sechs gewertete Läufe (IDs 1–6); Reihenfolge der vorangehenden Pausen: 20, 120, 120, 20, 20, 120 Sekunden.
- Sieben unabhängige Benchmark-Prozesslogs melden jeweils Exitcode 0, PASSED, 100 Queries in der Timing-Trace und eine Warm-up-Query. Queries werden nicht mit Einzelbildern gleichgesetzt.
- Genau ein protokollierter Streamstart bei 2000 S/s; Collector-Exitcode 0, `Writer Flushed`, Target `complete`.
- 34 Softwaretests auf Memmert bestanden, einschließlich des vorher mangels Polars ausgelassenen Parquet-Roundtrips. Das bestätigt keinen universellen Hardware-/Kalibrierstatus.
- Alle 43 im Exportmanifest enthaltenen Dateien passen zu ihren SHA-256-Angaben; ZIP-CRC unauffällig. Der einzelne hochgeladene REPORT ist identisch mit dem archivierten REPORT.
- 1147 Sysfs-Telemetriezeilen und 1142 Tegrastats-Zeilen vorhanden. Alle tatsächlich abgefragten Sysfs-Sensoren liefern Werte. Es wurde jedoch kein Lüfter-/EMC-/Throttlezähler erfasst; `unavailable: []` ist kein Vollständigkeitsnachweis aller denkbaren Sensoren.
- Engine-Hash und die geprüften Collector-Quellen stimmen mit dem vorigen Iterationsversuch überein. Laufbefehle und Profil INA225NVGPU/nvgpu, X10/X10 bleiben im Export konsistent.

Die Pause ist Ziel-Prozessende → nächster Ziel-Prozessstart auf der monotonic clock, nicht die Zeit zwischen zwei Hardwaretriggern. Maximaler protokollierter Abstand vom Pausensoll: **0.000156 s**. Die Millisekundenangabe ist Scheduling-Evidenz, keine kalibrierte metrologische Zeitunsicherheit.

## 2. Hauptstatistik – drei Läufe pro Bedingung

| Größe | 20 s Pause | 120 s Pause | Änderung lang gegen kurz |
|---|---:|---:|---:|
| TRT-Timing-Trace für 100 Queries | 105.302 s | 96.150 s | -8.691 % |
| Energie im signalbasierten Lastfenster | 3836.719 J | 3646.687 J | -4.953 % |
| Innenleistung (je 10 s Rand entfernt) | 36.110 W | 38.168 W | +5.701 % |
| Mittlere Leistung im gesamten Lastfenster | 36.048 W | 37.947 W | +5.268 % |

Es sind **Mediane jeweils der pro Lauf berechneten Größen**. Quotient aus Medianenergie und Mediandauer ist nicht automatisch Medianleistung. Die Lastenergie schließt die vorangehende Wartepause nicht ein: Daraus folgt **keine** Empfehlung, 120 s Pause zur Minimierung der Gesamtenergie des Ablaufs einzufügen. Die vorhandene NvGpu-Skalierung am Jetson ist weiterhin nicht unabhängig elektrisch validiert.

## 3. Temperatur und einzelne Wiederholungen

Starttemperatur = Median der Sysfs-GPU-Temperaturen in den letzten 5 s vor dem Benchmark-Prozessstart. Spitzenwert = größter während dieses Prozesses abgefragter GPU-Wert (1-Hz-Stichprobe). Kein unterstellter, exakt synchroner Inferenzbeginn.

| ID | Pause [s] | TRT [s] | Energie [J] | Innen-P [W] | GPU vor Start [°C] | GPU-Maximum [°C] |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 20 | 104.197 | 3756.169 | 36.110 | 72.468 | 95.031 |
| 2 | 120 | 96.150 | 3632.732 | 37.993 | 58.781 | 93.656 |
| 3 | 120 | 96.043 | 3646.687 | 38.168 | 58.218 | 93.656 |
| 4 | 20 | 105.302 | 3836.719 | 36.423 | 73.562 | 95.031 |
| 5 | 20 | 107.508 | 3866.799 | 35.876 | 75.968 | 95.093 |
| 6 | 120 | 96.331 | 3674.906 | 38.314 | 59.031 | 93.718 |

Jeder lange-Pause-Lauf ist in dieser Folge schneller als jeder kurze-Pause-Lauf. Die Temperaturen vor dem Start trennen sich ebenfalls: kurze Pause etwa 72,5–76,0 °C, lange Pause etwa 58,2–59,0 °C. Unter Last erreichen die kurzen Pausen rund 95 °C, während die langen Läufe ihre Arbeit bei Maxima um 93,7 °C beenden. Das sind Beobachtungen, **keine experimentell isolierte reine Temperatureinwirkung**. Vorherige Läufe, thermische Vorgeschichte und andere Zustände bleiben Teil des kleinen Versuchs.

Die zehn im TensorRT-Log aufgezeichneten Mittelwerte für aufeinanderfolgende Gruppen von zehn Queries machen die Verlangsamung innerhalb eines Laufs sichtbar. Beispiel ID 4 (20 s): 942,751 → 1140,000 ms; ID 3 (120 s): 917,626 → 1036,040 ms. Auch die langen Läufe werden zum Ende hin langsamer, nur später und weniger stark. Kein Start-/Stopfehler des Pico-Auswertungsfensters kann diese unabhängig protokollierten TensorRT-Latenzen erzeugen. Abbildungen: `figures/gpu_latenz_zehnergruppen.png`, `figures/gpu_temperatur_pro_lauf.png`. Originalauszüge mit Member-Zeilennummern: `evidence/EVIDENZ.md`.

## 4. Frequenzen: ein wichtiger Gegenbefund

**Alle 1147 Sysfs-Zeilen zeigen dieselben gelesenen GPU-/CPU-Werte:** GPU `cur_freq` 1 173 000 000 Hz, CPU `scaling_cur_freq` 1 984 000 000 Hz. Auch die übrigen abgefragten devfreq-Werte bleiben konstant. Die aufgenommenen Tegrastats-Zeilen enthalten `GR3D_FREQ` als Aktivitätsprozent, aber keine angehängte GPC-Frequenz. Der Test hat somit **keine Absenkung dieser Frequenzanzeigen nachgewiesen**. Ein Lüfterkanal wurde nicht gefunden/aufgezeichnet; daraus darf nicht „kein Lüfter vorhanden“ oder „Lüfter defekt“ abgeleitet werden.

Externe technische Einordnung W03, klar getrennt von P01: NVIDIA unterscheidet Software-DVFS, Firmware-/Hardware-Throttling und elektrische OC-Ereignisse; bei hardwareseitigen Ereignissen muss das Host-OS nicht benachrichtigt werden. Die veröffentlichte Standardtabelle r36.4.4 nennt 99 °C für softwareseitiges GPU-Throttling, **nicht** eine hier automatisch anzunehmende 95-°C-Schwelle. Die lokal geladenen Trip-Points, Grenzwerte und ausgelösten Zustände liegen nicht im Export. Daher: ein temperatur-/zustandsabhängiger Leistungsabfall ist sehr gut gestützt, eine konkrete thermische Schaltschwelle oder ein bestimmter Throttlingmechanismus ist **nicht bewiesen**. Keine Schutzgrenzen verändern.

## 5. Zusätzliche On-board-Plausibilisierung

Tegrastats enthält eine von der Pico-Auswertung getrennte Leistungsanzeige `VDD_IN`. Nach W04 wurde die Zahl **vor** dem Schrägstrich als aktueller Messwert verwendet, nicht der laufende Mittelwert nach dem Schrägstrich.

Für jedes Benchmark-PROZESSfenster ohne die ersten und letzten 10 s wurde der arithmetische Mittelwert der verfügbaren ca. 1-Hz-VDD_IN-Messwerte berechnet. Die Mediane dieser drei Laufmittelwerte sind:

- 20 s Pause: **35,060540 W**
- 120 s Pause: **36,779797 W**
- Relativer Unterschied: **+4,903682 %**.

Das zeigt dieselbe Leistungsrichtung wie der Pico-Innenvergleich. Die Zeitfenster und Messgrenzen sind nicht identisch; dies ist **keine absolute Kalibrierbestätigung und keine synchrone Vergleichsintegration**. Die Beobachtung ergänzt die TensorRT-Zeitbelege gegen eine alleinige Erklärung durch eine Amplitudenverzerrung des Pico-Pfads.

## 6. Robustheit der Fenster und Prüfung der Energieexporte

Die sieben Haupthüllen wurden anhand der vollständigen exportierten 0,1-s-Mittelwerte erneut detektiert; ihre Grenzen stimmen mit RESULT überein. Die maximale absolute Differenz zwischen Hüllzeitspanne und TensorRT-Timing-Trace ist **0,068400 s**. Das stützt die Zuordnung, beweist aber keine hardware-synchrone Randdefinition oder vollständige USB-/ADC-Kontinuität.

| Schwellenanteil des Last-/Idle-Kontrasts | Medianenergie 20 s [J] | Medianenergie 120 s [J] | Lang gegen kurz [%] |
|---:|---:|---:|---:|
| 0.4 | 3838.330524 | 3647.896754 | -4.961370 |
| 0.5 | 3836.719262 | 3646.686735 | -4.952995 |
| 0.6 | 3833.466268 | 3640.838156 | -5.024907 |

Drei vorab vorgesehene Detektorschwellen liefern also rund −5 %, ohne Vorzeichenwechsel. Alle 21 Hüllintegrale und 21 Innenintegrale sind mit den vollständigen Bin-Summen und den Grenzen ihrer unbekannten ersten/letzten Rohsamples vereinbar. Die zwei Endpunkte werden beim Trapezintegral jeweils halb gewichtet; diese fehlende Binneninformation wurde begrenzt statt als bekannt eingesetzt. Das ist keine erneute Rohdatenintegration und kein 95-%-Konfidenzintervall.

Die erhaltene Originaldatei auf Memmert liegt unter:

```text
/media/jwachsmuth/satassd/power_measurements/jetsonMeasurements/pauseTests/pause_20260928_195147Z_ca304a17/raw/usb_osc_data.parquet
```

Gemeldete Quelldateigröße: 3 731 381 Byte (komprimierte Parquet-Datei). Gemeldeter SHA-256: `251a33864d7d56435c104dfa97b07e9813b3283dfd832dee53c279f08da3f15b`. Die Rohbytes waren nicht im Review enthalten, daher wurde dieser Rohhash hier nicht unabhängig neu gebildet.

Die Rohdatei `raw/usb_osc_data.parquet` wurde ausdrücklich aus dem ZIP ausgeschlossen. RESULT nennt deren Größe und Hash; die Originalbytes verbleiben auf Memmert und sind separat zu archivieren. Der erfolgreiche Test dieses Legacy-Collectors ist keine Hardwareabnahme von `pico_validation_v1.0.0-rc1`.

## 7. Konsequenz für Altbestand und Paper

Der konkrete Kontrollversuch zeigt: Ein Ratenwechsel ist nicht nötig, um einen realen Unterschied von Laufzeit und Lastenergie in ähnlicher Richtung wie im ungezwungenen Iterationssweep zu erzeugen. Zusammen mit den früher protokollierten ratenabhängigen Analysepausen und dem auf denselben 45 Spuren nachgewiesenen Vorzeichenwechsel durch die Fensterregel entsteht eine belastbare Erklärung für einen wesentlichen Störeinfluss des direkten Sweep-Protokolls.

Dies erklärt nicht automatisch jeden historischen Trend oder dessen gesamten Betrag. Keine pauschale −5-%- oder −8-%-Korrektur aller Daten, keine erdachte thermische Normalisierung und keine nachträgliche Entfernung früher/wärmerer Läufe. Der neue Pausentest umfasst nur drei Wiederholungen je Bedingung in einer Sitzung. Die erste Konditionierung stellt weder ein thermisches Gleichgewicht noch identische Ausgangszustände aller Testläufe her.

**Arbeitsentscheidung:** Keine Wiederholung der Gesamtkampagne. Bestehende Messspuren bleiben die Datenbasis. Jetzt eine versionierte Offline-Fensterauswertung und Regeneration aller betroffenen direkten Energie-/Dauerdiagramme. Die separate Tek-/Pico-PSD-/Common-Reference-Kette und ihre kanonischen Zahlen bleiben unangetastet, soweit keine konkret importierten Energie-/Fenstertabellen betroffen sind.

Für eine präzise Benennung der Begrenzung wäre ein rein lesender Abzug der aktuellen thermischen Trip-Points, Cooling-Zuordnungen und verfügbaren OC-Zähler sinnvoll. Er ersetzt keine historischen Zählerdifferenzen und erfordert keinen weiteren Benchmark. Kein solcher Abzug und keine neue Messung wurden in diesem Review gestartet. Eine vollständige Neuauswertung des Altbestands ist weiterhin vorgesehen, nicht bereits ausgeführt.

## 8. Wiederholung der Nachprüfung

`review_pause.py` liest das Original-Review-ZIP und schreibt nur abgeleitete Prüfdateien. Beispiel:

```bash
python3 review_pause.py /pfad/pause_20260928_195147Z_ca304a17_review_20260928_201115Z_11725b2b.zip /neuer/pruefordner
```

NumPy wird benötigt. `QA.json`, `data/summary.json`, `data/crosscheck_previous_iteration.json` und `QUELLEN.json` dokumentieren genaue Herkunft, Prüfungen und Einschränkungen. Es wurde kein Statistik-P-Wert aus sechs sequenziellen Läufen als allgemeiner Kausalbeweis verwendet.

## 42.9 Quellen und Statuswechsel

Die Energie-/Temperatur-/Timing-Angaben kommen aus dem real zurückgegebenen Experiment, nicht aus Herstellerbeispielen. Externe W03/W04 erklären Begriffe und Mechanismen, nicht die lokale Trip-Point-Konfiguration. Der Hardwarebefund betrifft den unveränderten Legacy-Collector und den neuen Pausenstarter, nicht den separaten Python-/PS4000A-RC.

**[Q28] `Energy_Paper_TIM_KnowledgeBase_2026-09-28_v2.md`**  
SHA-256: `86995f26ef7a02767c1a2a0b0c159ecc4271c85a9ddf19a77c1cacf4ec1e4147`

**[Q29] `pause_20260928_195147Z_ca304a17_review_20260928_201115Z_11725b2b.zip`**  
SHA-256: `d88c9881cec4b03e6d70fedb44863547253ce1368fe6de6c79539b81bf979114`

**[Q30] `Eingefügter Text(20260929-071306).txt`**  
SHA-256: `d83a6f38d5919b6805fc906145a095aa9e2dff52be5f9677ac0cb4f43b36e718`

**[Q31] `REPORT.md`**  
SHA-256: `accf99c7127cc7cb7a2b01f45ed752a89a194ca437eb348e19114fdd260cbcca`

**[Q32] `jetson_pause_review_20260929/ANALYSE_PAUSENTEST.md`, `data/summary.json`, `QA.json` und `evidence/EVIDENZ.md`:** abgeleitete Nachprüfung des Q29-Exports. Quellbytes und Manifestangaben sind im Review dokumentiert. Kein zusätzlicher Benchmark und kein Rohdatenersatz.

**[W03] NVIDIA Jetson Linux Developer Guide r36.4.4, Platform Power and Performance – Orin:** thermische/elektrische Managementmechanismen, Hardware-Throttling und Standard-Trip-Tabelle; abgerufen 29.09.2026.

**[W04] NVIDIA Jetson Linux Developer Guide r36.4.4, Tegrastats Utility:** Bedeutung von VDD-Instantan-/Durchschnittswerten und GR3D-Prozent/Frequenz; abgerufen 29.09.2026. URLs im Quellenmanifest des Reviewpakets.

**Versionsstand 2026-09-29.1:** vollständige Fortschreibung von Q28. Abschnitt 0 aktualisiert, Abschnitt 42 ergänzt. Historische Kapitel 1–41 und damit insbesondere die kanonischen Common-Reference-/PSD-/Tek-Zero-Werte sind byteidentisch beibehalten. Kein weiterer Hardwaretest gestartet; keine Aufnahme-/Auswertungssoftware auf Memmert geändert. Der alte sechsteilige Pausenplan ist abgeschlossen.


---

# 43. Abgeschlossene Vollauswertung und Folgeprüfung – 29./30.09.2026

## 43.1 Datenbasis und Prüfstatus

[N01] ist der **vollständige** v0.2.0-Ergebnisexport, nicht der Pilot. 17.221 manifestierte Dateien wurden geprüft, 16.834 Dateipfade sind vollständig abgearbeitet. Die eigentliche NPY-Integration lief auf Twix; die exportierten Werte wurden anschließend hier geprüft. Der Umfang enthält Sensoren und Kopien, nicht 16.834 unabhängige Experimente. 2.327 identische YAML-/Sensor-/NPY-Kopienpaare dürfen nicht gepoolt werden.

Die größte Legacy-Differenz bei den 16.721 reproduzierenden Dateien ist 6,65 µJ. Die 45 rekonstruierten alten ungezwungenen Detektorfenster reproduzieren die vorherige Diagnose bis ungefähr 3e-10 J. Die acht Dateifehler betreffen Telemetrie, nicht Pico; 105 Legacy-Mismatches sind lokalisiert. Der erfolgreiche Rechenlauf ist keine pauschale elektrische/physikalische Paperfreigabe. [N01,N02]

## 43.2 Größerer Gewinn bei den kurzen Dauerläufen

Beispiel historisches Jetson GEMM FP16, Pico, jeweils 15 Wiederholungen, vorhandene Skalierung:

| Vorgabe [s] | Legacy-P [W] | Hüll-P [W] | Legacy-Spanne [s] | Hüll-Spanne [s] |
|---:|---:|---:|---:|---:|
| 5 | 19,947 | 34,343 | 6,9995 | 3,0 |
| 20 | 30,534 | 35,203 | 21,9995 | 18,0 |
| 100 | 35,343 | 36,339 | 101,9995 | 98,1 |
| 300 | 36,224 | 36,577 | 301,9995 | 297,9 |
| 600 | 36,497 | 36,662 | 601,9995 | 598,2 |

Mediane werden aus den jeweils pro Lauf berechneten E/T-Werten gebildet. Der Dauereinfluss auf **mittlere Lastleistung** ist in diesem Beispiel viel kleiner als beim erweiterten Legacy-Fenster. Das beweist keine allgemein ausreichende dreisekündige Benchmarkdauer und keine irrelevante Initialisierungsenergie. Ende-zu-Ende-Energie und Lastenergie sind verschiedene Größen. Originaltabellen in N02 bleiben erhalten.

Samplerate-Effekte verschwinden nicht automatisch: historische Jetson-FP16-/INT8-Neuhüllenänderung 5 MS/s gegen 2 kS/s ca. −2,250/−2,379 %; GPU-FP32/FP16 ca. −0,558/−0,070 %; neuer Zeitlauf +4,566 %. Der 45er-Diagnosevergleich ergibt für die **neue** Hülle −8,029 %, für den **rekonstruierten ursprünglichen** Detektor −7,977 %. Diese Größen nicht gleichsetzen. [N02]

## 43.3 Acht terminale Telemetrie-Zeilen

Der kleine Folgeexport N03 enthält elf Originalarrays und 14 Cache-Binfolgen, 25 manifestierte Dateien. In allen acht vorher fehlgeschlagenen Telemetriepfaden liegt genau ein negativer Zeitschritt am Ende; der letzte Leistungswert ist gleich dem vorherigen. Fünf Arrays sind verschieden, drei sind Kopien. Rücksprung 0,019–2,353 ms, außerhalb der historischen Integrationsgrenzen. Der untersuchte Collector-Code hängt beim Abschluss die letzten Werte mit einer Empfänger-Zeit an; dies passt zum Muster, ohne jeden historischen Build rückwirkend zu beweisen.

Die eng geprüfte **abgeleitete Sicht ohne genau die letzte Zeile** reproduziert alle acht historischen Integrale bis max. 1,46e-11 J. Originale werden weder sortiert noch verändert. Positive Lücken bis 38,132 s bleiben ungeklärt und markiert. Diese acht Resultate dürfen als hashgebundene Overlays in einen Ergebnisnachlauf eingehen, nicht als globale Reparaturregel sämtlicher Zeitstempel. Die HailoRT-Folge bleibt wegen fehlendem Lastkontrast ohne neue Hülle. [N04]

## 43.4 LLM und Hailo bleiben begrenzt offen

LLM: 85 S/s/Lauf 0 liefert aus der Leistungsfolge 4093,480084 J versus 4131,370045 J in der YAML. Verschiedene Summationsreihenfolgen reproduzieren die Differenz; selbst das maximal energiereiche gleichlange verschobene Fenster erreicht den YAML-Wert nicht. Sieben Gruppen mit je 15 Läufen und ca. 138 s haben Mismatches, die übrigen 300 Dateien mit ca. 136 s nicht. Kein einfacher nachgewiesener Rundungs-/Startindexfehler. Historische Ursache bleibt offen, neue Werte nicht als verifizierte alte Zahlen ausgeben. [N04]

Hailo Random Pattern: 1 MS/s/Lauf 13 wird bei f=0,4 von 12,1 bis 94,6 s erkannt, E=145,424 J; bei f=0,5/0,6 erst ab 37,6 s, E=100,749 J. Das ist Detektorempfindlichkeit, kein 44-%-Sensorfehler. Die 100-s-Dauerspur hat schon am Capture-Anfang einen höheren Pegel. Weder niedrigere Einzelschwelle noch pauschaler Nachlaufabzug beweisen die wahre Grenze. Originale explizite Fenster bleiben als historische Definitionsgröße nutzbar, neue Hauptgrenzen nur bei ausreichender Evidenz. [N04]

## 43.5 Joris-Abbildungsregister

Das alte Archiv N05 enthält 94 Dateien: 62 PDFs, 19 PNGs, acht EPS, ein JPG, drei ODS und eine Setupnotiz. 33 PDFs sind der direkte Kernergebnisbestand (neun Jetson-Samplerate, 18 Jetson-Dauer, sechs Hailo-Dauer), dazu vier statische Vergleiche und fünf Detailansichten. Fotos/Schemata, SINAD/Kalibrierung und PSD sind nicht automatisch neue Integrationsplots. Native Hailo-/GPU-Sweeps können ergänzt werden. Virtuelle 1/5/10/25-S/s-Werte lassen sich nicht aus bloßen Ergebnisaggregaten rekonstruieren und werden im Ergebnisnachlauf nicht erfunden. [N04,N05]

# 44. Vollständige Lastfenstermethode v0.2.0 und Aufnahmeabgrenzung

**Nutzerklarstellung [U08,30.09.2026]:** Die Aufnahme wurde ohnehin manuell beziehungsweise durch das Benchmarkingtool gesteuert, vor dem Benchmark gestartet und ungefähr zehn Sekunden danach beendet. Diese Aussage trennt Erfassung und nachträgliche Fensterauswertung. Sie wird nicht zu einem exakt bekannten Startversatz, einem festen 10-s-Abzug oder einer synchronen Uhrbeziehung für alle Sensoren aufgewertet. Originale vollständige Vor-/Nachläufe bleiben die Quelle. **Ein Randalarm des Leistungsdetektors beweist deshalb nicht, dass die Aufnahme tatsächlich erst nach Benchmarkbeginn gestartet wurde.** Er kennzeichnet zunächst eine ungeklärte signalbasierte Grenze, etwa bei verschiedenen Vor-/Nachlaufpegeln; eine unvollständige Datenerhebung wird daraus nicht pauschal behauptet.

Die folgende Dokumentation wird aus N04 unverändert inhaltlich übernommen; nur die Überschriftennummerierung wird für diese KB angepasst:

Stand: 30.09.2026. Geprüft wird der tatsächlich ausgelieferte Code aus `tim_offline_reanalysis_v0.2.0.zip`, nicht ein nachträglich verbesserter Detektor. Quellcodeauszüge und Hashes stehen in `evidence/CODE_BELEGE.md`. Produktionscode und Cache auf Twix wurden durch diesen Review nicht geändert.

## 44.1 Geltungsbereich und Messgröße

Die Fenster werden **offline aus den gespeicherten Leistungsfolgen** bestimmt. Sie haben die ursprüngliche Datenerhebung nicht gesteuert. Das Ergebnis ist die Energie einer operational definierten Signalhülle, nicht automatisch Energie exakt synchron markierter Inferenzen. `oscilloscope.npy` enthält bereits skalierte Leistung; es wird keine neue U/I-Kalibrierung angewendet.

Das frühere Fenster wird zusätzlich an seinen gespeicherten inklusiven Indizes integriert. Der separate Diagnosebestand besitzt außerdem rekonstruierte ursprüngliche Detektorgrenzen. Diese drei Fensterarten sind verschiedene Größen und bleiben unterscheidbar.

## 44.2 Bildung der Detektionsspur

Für gleichmäßig abgetastete Spuren gilt für ein Originalintervall:

`dE[i] = (P[i] + P[i+1]) / (2 * fs)`.

Binränder werden bei angefordert 0,1 s erzeugt und mit `np.rint` auf reale Sampleindizes gerundet; Anfang und letzter Sampleindex sind eingeschlossen. Die Mittelwerte sind `Binenergie / tatsächliche Binzeit`. Es wird nicht nur jeder k-te Leistungswert betrachtet. Bei 85 S/s sind die einzelnen Binzeiten beispielsweise nicht alle exakt 0,1 s.

Die Energie eines gewählten uniformen Fensters ist das Trapezintegral der Originalsamples zwischen den ausgewählten Indizes. Die Zahl der Zeitintervalle ist N−1. Der 100-ms-Raster bestimmt die Lage der Detektorgrenzen, nicht eine garantierte Zeitunsicherheit. Die Zeitbasis bleibt die gespeicherte nominelle Rate.

Bei `(t,P)`-Spuren gilt stattdessen das Integral der stückweise linear interpolierten Leistung auf den gespeicherten Zeitstempeln. Eine native Auflösung gröber als 0,1 s wird markiert; Interpolation erzeugt keine neue Messinformation. Rückwärtssprünge führen in v0.2.0 zum Stopp; gleiche Zeitstempel bleiben als Nullzeitintervalle mit Hinweis erhalten. Es gibt keine automatische Synchronisierung zwischen Sensoren.

## 44.3 Pegel und Kontrast pro Spur

Für eine Spur mit Zeitspanne T wird pro Seite eine Randlänge `edge = min(2 s, T/5)` verwendet. Nur vollständig im Randbereich liegende Bins gehen ein. Mindestens zwei Bins pro Rand sind nötig. Bei T < 1 s oder weniger als acht Bins wird kein Lastfenster freigegeben.

Es seien `m_pre` und `m_post` die Mediane der Rand-Binmittel:

- Idle-Niveau: `B = min(m_pre, m_post)`.
- Oberes Niveau: `H = percentile(bin_means, 95)`; bei der verwendeten NumPy-Implementierung der Standard-Perzentilalgorithmus.
- Kontrast: `D = H - B`.
- Randstreuung: `s = 1.4826 * max(median(abs(pre - m_pre)), median(abs(post - m_post)))`.
- Erforderlicher Kontrast: `max(1e-9 W, 0.005 * max(abs(H), abs(B), 1e-6 W), 6*s)`.

Nur ein **streng größerer** Kontrast als diese Grenze wird akzeptiert. Eine Vor-/Nachlaufdifferenz größer als `max(0.1*D, 6*s)` erhält einen eigenen Hinweis. Die Wahl des kleineren Randpegels setzt voraus, dass wenigstens eine Seite eine brauchbare niedrige Basis liefert; das wird nicht als bekanntes physikalisches Idle bewiesen.

Das P95 bezieht sich auf Zeitbins innerhalb **einer** Spur. Es entfernt weder Originalsamples aus der Energie noch Wiederholungen aus der Statistik.

## 44.4 Aktivsegmente und Hülle

Drei vor dem Vollbatch festgelegte Schwellen werden gerechnet:

`theta_f = B + f * D`, mit `f = 0.4, 0.5, 0.6`.

Ein Bin muss strikt über der Schwelle liegen. Ein zusammenhängender Abschnitt muss mindestens 0,2 s dauern (numerische Vergleichstoleranz 1e-10 s). Die Hülle beginnt am Anfang des ersten qualifizierten Abschnitts und endet am Ende des letzten. **Alle internen Pausen bleiben im Integral enthalten.** Es wird weder die Summe nur der hohen Bins noch das energiemaximale Fenster gesucht.

Hauptkandidat ist f=0,5. f=0,4/0,6 sind Sensitivitätsvarianten, keine Optimierung und kein Konfidenzintervall. Es wird nicht nachträglich die Variante mit der flachsten Abtastratenkurve gewählt.

Eine Hülle erhält Randflags, wenn ihr Abstand zum Aufnahmebeginn/-ende unter 0,5 s liegt oder einer der beiden Randmediane über der betreffenden Schwelle liegt. Eine solche Hülle wird nicht automatisch als Hauptfenster freigegeben. Stationäre Reihen verwenden ausdrücklich das alte Referenzintervall; es wird kein Aktivitätswechsel erfunden.

Bei drei vorhandenen randgültigen Varianten wird eine Energiebereichsbreite >1 % der absoluten f=0,5-Energie als `envelope_energy_sensitive_gt1pct` markiert. **Dieser Hinweis sperrt den Hauptkandidaten im v0.2.0-Code nicht automatisch.** Er ist eine zusätzliche Prüfflagge; `primary_window` ist keine allgemeine Paperfreigabe.

## 44.5 Innenfenster, Summation und Qualität

Von jeder Hülle werden, soweit möglich, mindestens 1, 5 oder 10 s pro Seite abgeschnitten; die Grenzen werden nach innen auf bestehende Binränder gesetzt und die wirklichen Zeiten ausgegeben. Die Energiesumme bleibt das Integral an diesen Grenzen.

Die ursprüngliche v0.2.0-Ausgabe vererbte die Randflags nicht an die Innenfenster. Der Vollreview vom 29.09. hat das als **Berichtskorrektur** berücksichtigt (1.587 Zeilen, 225 Gruppen). Für den endgültigen Plotter müssen Qualität der Ausgangshülle und Quellenfehler auch die Innenfenster und Gruppenfreigabe bestimmen. Die Integrale selbst werden durch diese Flag-Korrektur nicht geändert.

Legacy-Rechenabweichungen über `max(2e-6 J, 1e-7 * abs(E_legacy))` sperren neue Hauptwerte im bestehenden Code. Das betrifft 105 LLM-Dateien. Diese Sperre wird in diesem Review nicht umgangen.

## 44.6 Was deterministisch und wiederholbar heißt

Es gibt keinen Zufallsstart, kein Training, keinen Fit auf gewünschte Ergebniskurven und keinen nachträglich ausgesuchten Einzelgrenzwert je Run. Jede Spur wird unabhängig aus ihren eigenen Bins mit denselben Regeln ausgewertet. Metadaten wie stationäre Reihe und nominelle Rate gehen explizit ein. Unterschiedliche tatsächliche Dauern liefern selbstverständlich unterschiedliche Grenzindizes.

Praktisch gilt: **gleiche Quelldatei + gleiche Zeitbasis/Metadaten + gleiche Code-/Bibliotheksversion → gleiche Regelentscheidung**. Rechenreihenfolge und Umgebung können Gleitkommasummen im letzten Stellenbereich beeinflussen; bitweise Gleichheit über beliebige Architekturen/Versionen ist nicht behauptet. Sehr knappe Schwellwertgleichheiten sind daher grundsätzlich Randfälle.

Im aktuellen Review:

- 14 exportierte Cache-Spuren lieferten beim erneuten Aufruf derselben Detektorlogik identische Grenzen, Schwellen und Flags.
- Drei echte mitgelieferte Originalarrays wurden je fünfmal verarbeitet: 64, 257, 4.096 und 1.048.576 Samples je Block, davon die letzte Variante zweimal.
- Bei allen Varianten waren die Grenzindizes identisch; maximale Energiedifferenz durch Blockgröße etwa 2,0e-11 J. Die zwei identischen Wiederholungsaufrufe lieferten identische Ergebnisobjekte.

Diese Tests belegen die geprüften Fälle, nicht die Richtigkeit jeder Lastgrenze aller 16.834 Pfade. Sie sind getrennt von Hardware-/Zeitbasis-/Kalibrierabnahmen.

## 44.7 Was vergleichbar ist – und was nicht automatisch fair ist

**Gleiche Regelbehandlung:** dieselben Zeitparameter und relativen Schwellen; keine unterschiedliche Auswahl, um bestimmte Plattformen, Raten oder Wiederholungen besser aussehen zu lassen. Für unterschiedliche Leistungsskalen wird die Schwelle relativ zum jeweiligen Kontrast bestimmt.

**Keine Garantie der Unverzerrtheit:** Eine adaptive Hülle ist ein signalabhängig ausgewähltes Fenster. Kleine Bursts, langsame Rampen, hohe Startleistung, wechselnder Duty-Cycle oder native Telemetrieglättung können bewirken, dass bei verschiedenen Signalen nicht dieselbe Ablaufphase getroffen wird. Auch eine konstante additive Pegelverschiebung ist wegen der relativen Kontrast-Sicherheitsprüfung nicht in jeder denkbaren Situation vollständig neutral.

**Zwischen Sensoren:** In v0.2.0 bestimmt jeder Messpfad seine eigene Hülle. Zwei gleich bezeichnete Hüllen sind damit nicht automatisch dasselbe physikalische Zeitintervall. Ein Gerätefehlervergleich benötigt abgestimmte Zeitfenster, passende Run-Paare und klar benannte Messgrenzen. Ohne diese Zuordnung sind es Abweichungen fensterspezifischer Ergebnisse, keine isolierten Instrumentfehler.

**Zwischen separaten Ausführungen:** Derselbe Detektor entfernt nicht deren Temperatur-, Pausen- oder Laufzeitunterschiede. Der Pausentest und die Common-Reference-Analyse behandeln diese Fragen gesondert.

## 44.8 Belegtes Gegenbeispiel zur universellen Tauglichkeit

Hailo Random Pattern, 1 MS/s, Lauf 13:

| f | Schwelle [W] | Start [s] | Ende [s] | Hüllenergie [J] |
|---:|---:|---:|---:|---:|
| 0,4 | 1,996463 | 12,1 | 94,6 | 145,424180 |
| 0,5 | 2,129836 | 37,6 | 94,6 | 100,748985 |
| 0,6 | 2,263209 | 37,6 | 94,6 | 100,748985 |

Hier liegen frühe kleinere Aktivitätsanteile unter den höheren Schwellen. Interne Pausen werden erhalten, **aber nur zwischen den erkannten äußeren Segmenten**. Die Grenze ist deterministisch und trotzdem als vollständige Ablaufgrenze problematisch. Auch die 0,4-Variante ist damit nicht automatisch die wahre Grenze. Der Fall braucht eine begründete Ablauf-/Burstregel oder eine ausdrücklich begrenzte historische Fensterauswertung.

## 44.9 Formulierung für das Paper

> Aus archivierten Leistungsfolgen wurde ein vorab parametrisierter, deterministischer Detektor auf zeitgewichteten 100-ms-Mittelwerten angewandt. Die resultierende Signalhülle umfasst den ersten bis letzten mindestens 200 ms anhaltenden Aktivbereich und behält interne Pausen. Die Grenzen werden nicht an eine Soll- oder Dry-run-Dauer angepasst. Energie, tatsächliche Fensterdauer und mittlere Leistung werden getrennt berichtet. Eine dreistufige Schwellwertsensitivität und Rand-/Zeitachsenprüfungen kennzeichnen unzuverlässige Grenzen. Die Hülle ist eine operationale Messdefinition und ersetzt keine hardware-synchronen Prozessmarker.

Das ist eine methodische Beschreibung, keine pauschale Validitätsfreigabe aller Ergebnisgruppen.

# 45. Ergebnis-/Plotnachlauf v0.3.0 – Implementationsumfang und Gerätepaarung

## 45.1 Kein neuer Rohdatendurchlauf

`tim_result_plot_post_v0.3.0` verarbeitet ausschließlich den hashgebundenen vollständigen Ergebnis-ZIP N01 und acht kleine bereits geprüfte Ableitungen aus N04. Keine Erfassungssoftware, keine Kalibrierung, kein neuer Detektor und kein NPY-/Parquet-Lesezugriff. Der v0.2.0-Cache auf Twix wird nicht verändert. Sämtliche Ausgaben in einen neuen Ordner; kein Überschreiben früherer Reports.

Die dreiteilige Ergebnisgeschichte bleibt unterscheidbar: `reported_legacy` (YAML-Wert und ausgegebene Dauer), `legacy` (reintegrierte alte Indizes/N−1-Spanne), `envelope_0.5` (neue Signalhülle), plus diagnostisches `envelope_0.5_trim10s`. Alle anderen Schwellen/Kandidaten bleiben tabellarisch verfügbar.

## 45.2 Qualitätsregeln dieses neuen Berichtstands

1. Ausgangshüllen-Randflags werden an alle Innenfenster vererbt. Dies behebt den im Vollreview gefundenen Gruppierungsfehler, ohne Integrale zu verändern.
2. `envelope_energy_sensitive_gt1pct` sperrt **hier neu** Hauptkurven der Hüllen/Innenfenster. In v0.2.0 war das nur eine Warnung. Originale und Kandidaten bleiben; diese Selektion ist offenzulegen, nicht als Wahrheit sämtlicher ausgeschlossener Fälle auszugeben.
3. Quellen-/Legacy-Mismatches sperren neue primäre Werte. Originale YAMLs werden separat mit Hinweis gezeigt, nicht versteckt.
4. Acht geprüfte terminale Präfixresultate werden ausschließlich im neuen Ergebnisbaum importiert. Keine Originaldaten-/Cachemutation, positive Zeitlücken nicht repariert.
5. Alt-/Neu-Hüllkurven vergleichen dieselben zulässigen Run-IDs je Gruppe. Innenfenster können wegen Mindestlänge weniger Werte haben; IDs/n stehen dabei. Samplerate-Endpunkte mit unterschiedlich vielen gültigen Teilnehmern bleiben verschiedene Gruppen, keine neuen gepaarten Experimente.
6. Keine Perzentiltrimmung physischer Wiederholungen, kein Pooling von Archivkopien. Bei n<2 keine als exakt null verkaufte Streuung. Alle Kandidaten, Gründe, Gap-Warnungen und Teilnehmerzahlen bleiben in CSVs.

## 45.3 Messgerätevergleich ist enthalten – mit ausdrücklicher Reichweite

Run-Paarung erfolgt nur bei **gleicher Serie und `record_id`**. PicoScope ist der Vergleichsbezug. u.RECS, Shelly, Jetson-Telemetrie und HailoRT werden einbezogen, soweit im Bestand vorhanden. In den vorhandenen GPU-GEMM-Sweeps gibt es im aktuellen NPY-Plan nur Pico; es werden keine NVML-Daten erfunden.

Je Paar werden Energie, mittlere Leistung und Fensterdauer verglichen: `100*(Wert_sensor/Wert_pico - 1)`, danach Median dieser Paarquotienten. Ein positiver Pico-Bezug ist nötig. Nicht ein Quotient unabhängig gebildeter Gruppenmediane mit möglicherweise anderen Teilnehmern.

**Diese Ausgaben sind beobachtete Setup-/Messpfadergebnis-Abweichungen bei eigenen Sensorfenstern, keine isolierten Gerätefehler oder synchronisierte absolute Kalibrierprüfung.** Die Fenster stammen aus den jeweiligen historischen Regeln oder separater Detektion; gemischte AC-/DC-/Modulgrenzen, Glättung, Zeitlücken und gespeicherte Kalibrierprofile wirken mit. Keine automatische Shelly-AC/DC-Transformation, keine neue Gainkorrektur.

Für einen streng zeitsynchronen Gerätefehlervergleich wäre ein gesondert belegter Zeitachsenabgleich und identisches physikalisches Fenster notwendig. Die neue ungefähr zehnsekündige Nachlaufangabe liefert diesen nicht. Energie-, Leistungs- und Dauerdifferenz werden daher gemeinsam verfügbar gemacht; die Grenzen stehen auch auf den Abbildungen.

## 45.4 Ausgaben und Bedienung

PNG/PDF-Abbildungen, optional SVG, eine lesbare Grafik pro Metrik. Native Samplerate-Boxplots, Wiederholungsstreuung, interner Mittelwertbezug; Energie-/Dauer-/Leistungskurven; Messpfadniveau und gepaarte E/P/T-Abweichungen. CSV-Register ordnet alte Abbildungsfamilien zu, ohne eine pixelidentische Rekonstruktion zu behaupten. Signal-Detailgrafiken ohne vorhandene Vollspur, synthetische Niedraten, PSD/SINAD/Kalibrierung/Fotos bleiben unverändert.

Der Nachlauf wurde hier auf dem Nutzerexport ausgeführt. Er ist keine Remote-Ausführung auf Twix. Für dortige Reproduktion:

```bash
env -u PYTHONPATH -u PYTHONHOME PYTHONNOUSERSITE=1 MPLBACKEND=Agg \
  "$HOME/venvs/common-trace/bin/python" -u \
  "$HOME/energy_analysis/tim_result_plot_post_v0.3.0/postprocess.py" run
```

Der vollständige Eingangsreview ist im Paket vorbelegt. `--input` erlaubt einen anderen Dateipfad desselben Inhalts. Ergebnisse neu unter `~/energy_analysis/tim_offline_reanalysis/plot_post/`. Keine erneute Python-/Bibliotheksinstallation und kein unqualifiziertes Systempython mit der bekannten NumPy/Matplotlib-Inkompatibilität.

Die Ausgabe enthält `INDEX.html`, `REPORT.md`, `POLICY.json`, `SUMMARY.json`, Tabellen, Abbildungsregister und Manifest. Dieser Ergebnisstand ist ein nachvollziehbarer Review, keine pauschale Finalfreigabe aller Paperfiguren. Das bereits abgeschlossene Vollbatch wird nicht erneut gestartet.

## 45.5 Tatsächlicher Lauf- und Prüfbeleg

Der Ergebnisnachlauf ist auf dem vorhandenen Nutzerexport abgeschlossen: **495 Diagramme**, jeweils PNG und PDF, also 990 Grafikdateien. Diese Zahl enthält Serien-/Quell-/Fenstervarianten, keine 495 neuen Experimente. Dazu 229.453 tabellarische Fenster-/Legacy-Zeilen, 15.561 Gruppen, 27.667 Geräte-Paarzeilen mit mehreren Fenstervarianten und getrennten Quellen, davon 25.833 unter der jeweiligen Regel akzeptiert; 1.894 Gerätegruppen. Ein Paarzähler ist keine Anzahl unabhängiger physischer Wiederholungen.

34 lokale Softwaretests bestanden, keine Fehler/Skips; dieselbe Suite aus dem frisch entpackten Paket nochmals bestanden. Alle 209.294 bestehenden Originalintegrale blieben exakt erhalten. Alle akzeptierten Paarquotienten und 1.894 Paargruppenmediane unabhängig geprüft; sämtliche PDF-/PNG-Dateien lesbar, repräsentative PDFs gerendert und visuell geprüft. Nicht jede Kurve ist dadurch physikalisch abschließend freigegeben. Der Datenstand zwischen beiden Darstellungsläufen ist CSV-byteidentisch; der zweite Lauf kennzeichnet zusätzlich leere/gesperrte Diagramme ausdrücklich als fehlende freigegebene Werte, nicht als Nullergebnisse.

Es wurden keine NPY-/Parquet-Rohwerte neu gelesen und kein Twix-Cache verändert. Der abschließende `tim_result_plot_release_qa_20260930.json` bindet Tool und Ergebnis-ZIP mit SHA-256. Die lokalen Python-/Bibliotheksversionen stehen darin; bitweise Portabilität aller Gleitkommazahlen über beliebige Umgebungen ist nicht behauptet.

# 46. Neue Provenienz, Git-Sicherung und verbleibende Aufgaben

## 46.1 Git-Evidence

Repository: `Keff789/onnx-splitpoint-results` (öffentlich). Neu: `energy-measurement/2026-09-30-offline-windows/`.

Commit: **`5468c175e04c91fe7484a169ad8fc90ff24112fa`**, Parent **`0699bef06209bbd6e73722ae2e3d386787964103`**. Neun neue Dateien, keine Löschung oder Änderung vorheriger Evidence. `main` wurde ohne Force aktualisiert. Die neue methodische Dokumentation, Befundzahlen, exemplarischen Dauer-/Endpunkttabellen und Quellenfingerabdrücke sind publiziert. Der Methodentext unterscheidet v0.2.0-Detektion und v0.3.0-Berichtspolitik.

Die vollständige KB, operative Host-/Homepfade, Originalreview-ZIPs und Rohwerte bleiben privat. Der Git-Blob-Identitätsprüfer ist kein Ersatz für Rohbackups; Originalarchive sind zusätzlich mit SHA-256 benannt. Aus dem öffentlichen Snapshot folgt keine unabhängige Messgerätevalidierung.

## 46.2 Quellenzusatz

[U08] Aktuelle Nutzerangabe zur manuellen/benchmarkgesteuerten Erfassung, ungefährem Vor-/Nachlauf sowie Auftrag KB, weitere Git-Evidence und paralleler Plotnachlauf einschließlich Gerätevergleich. Keine neue Datenerhebung damit behauptet.

[N01] Vollständiger v0.2.0-Review `v0.2.0_preflight_8pxojcp1_review_20260929_220252_9c06eb.zip`.
[N02] Gegencheck `tim_full_review_20260929.zip`.
[N03] Primärer Folgeexport `tim_focus_review_20260930_045511Z_2f186d16.zip`.
[N04] Folgeanalyse und Methodendokumentation `tim_focus_review_20260930.zip`.
[N05] Altes Abbildungsarchiv `power_measurements_plots(1).zip`.
[N06] Unverändertes Integrationstool `tim_offline_reanalysis_v0.2.0.zip`.
[N07] Neuer Ergebnisnachlauf `tim_result_plot_post_v0.3.0.zip` und zugehörige Ausführungs-/Prüfbelege im Begleitpaket.

Die SHA-256-Werte stehen im Quellenmanifest des KB-Updates. Acht Overlays stammen aus den tatsächlichen N03-Arrays/N04-Ergebnissen und sind an N01 gebunden. Die hier publizierten Ergebnistabellen verwenden keine fiktiven U/I-Rohwerte. Neue Plotzahlen verändern nicht rückwirkend die archivierten YAMLs.

## 46.3 Nicht als erledigt ausgeben

Die genaue historische Ursache der 105 LLM-YAML/NPY-Abweichungen, eine universell gültige Burstfensterpolitik sowie synchrone Sensorzeitfenster bleiben offen. Keine neue automatische Temperatur-/Ratenkorrektur. Die Vollsicherung der neuen Rohordner ist nach Nutzerlogs erledigt; der Plotnachlauf benötigt keine weitere Kopie. Quellenbestände und aktuelle Rohkopien nicht löschen.

Die kanonischen Tek-/Pico-PSD-/Common-Reference-Zahlen einschließlich Tek-Zero-Korrektur sind unverändert. Künftige Änderungen nur bei konkret belegter Tabellenabhängigkeit. Der separate PicoScope-RC bleibt von diesem Legacy-/Offline-Workflow getrennt; kein stilles Upgrade seines Hardwarestatus.

## 46.4 Dokumentationsprüfung

Die Kapitel 1–42 der KB vom 29.09. sind byteidentisch übernommen; aktueller Status und Kapitel 43–46 ergänzen, statt alte Belege zu überschreiben. Methodendokumentation wurde vollständig übernommen und nur überschriftsweise eingebettet. Es wurden keine Publikationsfristen oder externen Richtlinien neu recherchiert. Neu geprüft sind der Ergebnisnachlauf, seine Auswahl-/Paarungsregeln und die tatsächlich erzeugten Artefakte; Details und Testanzahl im aktuellen Prüfbeleg.
