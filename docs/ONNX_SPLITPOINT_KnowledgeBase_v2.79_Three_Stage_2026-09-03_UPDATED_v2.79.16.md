# ONNX Splitpoint Tool – Knowledge Base v2.79.16

**Konsolidierter Stand:** 3. September 2026  
**Toolversion:** `2.79.16`  
**Build-ID:** `v2.79.16-guided-full-system-input-calibration`  
**Dokumentstatus:** aktuelle Arbeits- und Methodenreferenz  
**Releaseurteil:** `INSTALLATION_PASS_TARGETED_SMOKES_PASS_CALIBRATION_AND_E2E_PENDING`

Diese Fassung führt die konsolidierte v2.79.15-Knowledgebase auf v2.79.16 fort.
Sie integriert die reale Installation, den Paper-Split-Regressionstest, den
Hailo-10-UINT8-Hardware-Smoke, die neue geführte Full-System-Kalibrierung und
den implementierten zeilenlokalen Energy-Fehlervertrag des direkten,
non-variant Ausführungspfads. Überholte Freigabegates und
die fälschliche Weiterverwendungsfreigabe der alten Idle-Baselines wurden
korrigiert. Neue manuell zu pflegende Hash- oder Versiegelungsketten sind
weiterhin ausdrücklich nicht Teil des Arbeitsplans.

---

# 0. Kurzurteil

v2.79.16 ist auf `Smartmirror2` installiert. Der Installer meldete
`INSTALL_ACCEPTANCE=PASS` und `FINAL_STAGE=complete`. Der fokussierte
Paper-Split-Test bestand mit 14/14 Tests. Ein realer Hailo-10H-Smoke bestätigte
den neuen UINT8-Pfad mit UINT8-Eingang, UINT8-Ausgang, `InferModel`, Hotloop und
20/20 ausgeführten Inferences. Der Mittelwert von Part 1 lag bei 13,335 ms,
entsprechend ungefähr 75 FPS.

Damit sind Installation, Paper-Softwarepfad und der konkrete Hailo-10-UINT8-
Fix bestätigt. Noch nicht bestätigt sind:

1. ein zwischen den Jetsons abgeglichener und für die Kampagne festgelegter
   Power-Mode-/Clock-Vertrag;
2. die neue geführte Full-System-Eingangskalibrierung an realer elektronischer
   Last für alle drei Setups;
3. die danach zwingend neu aufzunehmenden M.2-Idle-Baselines;
4. die vollständige Hailo-10-Kette `P1 → FIFO → TensorRT P2` unter v2.79.16;
5. ein kleiner echter EvalRun mit Energy, Ergebnisfinalisierung und allen drei
   Setups;
6. das zeilenlokale Weiterlaufen bei einem real auftretenden modellbezogenen
   Native-Preflight- oder technischen Quality-/Contractfehler im direkten,
   non-variant Pfad.

Vor dem großen EvalRun ist genau **ein kleiner End-to-End-Eval-Smoke** sinnvoll.
Er soll mindestens `yolo26s/b024`, alle drei Setups, Native und Energy enthalten.
Der formale DeepX-Classification-Part1-Smoke kann in denselben kleinen Lauf
aufgenommen werden. Erst danach wird der große Lauf freigegeben. Es wird kein
absichtlich fehlerhaftes Modell konstruiert und keine weitere Releaseversion
präventiv begonnen.

Nicht vorgesehen sind:

- neue Hash-, Seal-, Signatur- oder Versiegelungsketten für Messwerte;
- zusätzliche InferModel-Jobparallelität als nachträgliche Hailo-10-
  Optimierung;
- präventive C++-Rewrites oder breite Runneroptimierungen;
- ein neuer großer Generic↔Native-Korrelationslauf;
- künstliche Splits, um je Modell zwingend drei Fälle zu erzeugen;
- mehrere serielle Splitstellen innerhalb eines Netzes;
- eine vollständige Wiederholung der Kampagne wegen einzelner Fehler.

---

# 1. Zweck und Evidenzpolitik

## 1.1 Ziel der Messkampagne

Ziel ist eine einmalige, ordentliche, nachvollziehbare und sinnvoll
wiederholbare Messkampagne. Das Tool soll jeden vorab festgelegten Pfad ehrlich
als erfolgreich, fehlgeschlagen, nicht unterstützt, nicht anwendbar oder
unvollständig ausweisen.

Normale Identitätsangaben bleiben erforderlich:

- Toolversion und Profil;
- Modell, Case und Setup;
- Backend, Richtung, Precision und Endpoint;
- Wiederholung, Messdauer, Work Units und Ergebnis;
- Quality-, Energy- und technischer Status.

Diese Angaben genügen für die Kampagne. Automatisch erzeugte Hashes dürfen als
interne Metadaten bestehen bleiben, sind aber kein Anlass, neue Hashbäume,
Manifeste, Signaturen oder Abnahmeketten zu bauen. Ein technisch gültiger
Messwert wird nicht allein wegen eines fehlenden Hilfs-Seals verworfen.

## 1.2 Statusklassen

| Status | Bedeutung |
|---|---|
| **historische Hardwareevidenz** | Reale Hardwaremessung einer exakt benannten älteren Toolversion. |
| **offline belegt** | Ausgeführter Source-, Contract- oder Pakettest ohne Aussage über reale Accelerator-Hardware. |
| **aktuell hardwarebelegt** | Mit der aktuellen Version erfolgreich auf dem Zielsystem ausgeführt. |
| **hardwareseitig offen** | Softwarepfad vorhanden, aber mit v2.79.16 noch nicht auf Zielhardware bestätigt. |
| **eingefroren** | Einstellung wird nach Sichtung der Ergebnisse nicht nachträglich optimiert. |
| **Legacy-Fixture** | Historisches Ergebnis nur für Regression oder Reconciliation, nicht als aktuelle Messung. |

Grundregel: Ein Offline-PASS ist kein Hardware-PASS. Eine abgeschlossene
Performancezeile ist kein automatischer Quality-PASS. Historische Ergebnisse
belegen die frühere Implementierung, nicht automatisch v2.79.16.

## 1.3 Ehrliche Terminalzustände

Ein geplanter Fall endet sichtbar als einer der folgenden Zustände:

```text
completed
failed
blocked
unsupported
quality_not_applicable
missing
```

Ein Quality-`FAIL` wird nicht aus der Toolvalidierung entfernt. Ein
`INCONCLUSIVE` wird nicht als PASS umgedeutet. Compiler-Rejects,
Runtimefehler, fehlende Single-Tensor-Grenzen und Multi-Tensor-Grenzen außerhalb
des Native-Scope werden transparent berichtet.

---

# 2. Wissenschaftlicher Umfang und eingefrorene Entscheidungen

## 2.1 Sieben Modelle

| Rolle | Modelle |
|---|---|
| Development | `resnet50`, `yolo26s`, `yolov7_paper` |
| Transfer/Evaluation | `mobilenet_v3_large`, `regnet_x_1_6gf`, `yolo26m`, `yolo11l` |

`yolo26x` ist nur ein optionaler Größen-/Stresstest. Es gehört nicht
automatisch zum finalen Umfang und dürfte nur vorab, nicht ergebnisabhängig,
als achtes Modell aufgenommen werden.

## 2.2 Eingefrorene methodische Entscheidungen

- produktiver Ranker: `cut_bytes_only`;
- aufsteigende Cut-Byte-Reihenfolge mit deterministischem Tie-Break;
- Stratified-Windows-Kandidatenauswahl;
- score-unabhängiger breiter Generic-Audit;
- B500 für Development, Screening und Compilerkalibrierung;
- Hailo: `balanced`, Optimization Level 1, B500, Kalibrationsbatch 8;
- DeepX: B500, EMA, Optimization Level 0;
- DeepX Classification: `imagenet_mean_std`;
- Detection: modellgebundener Letterbox-/Skalierungsvertrag;
- Native nur für hardwarekompatible Single-Tensor-Grenzen;
- Generic für Single- und Multi-Tensor-Grenzen an jeweils einem Splitpunkt;
- CPU-/ORT-Energie bleibt deaktiviert;
- Native-Full-Baselines gehören zur Performance-/Energy-Matrix;
- finale Detection-Accuracy verwendet bei Bedarf Official COCO/Pycocotools;
- 5.000 Validierungsbilder und 5.000 Bootstraps sind eine spätere finale
  Accuracy-Auswertung, kein Software- oder Smoke-Freigabeblocker.

Quality-Einstellungen werden nicht nach Öffnung der Resultate optimiert. Ein
realer Quality-Verlust ist zunächst ein Ergebnis, kein Anlass für einen neuen
Compiler-Sweep.

---

# 3. Integrierter Fragen- und Antwortkatalog

## 3.0 Antwortmatrix

| Nr. | Kurzantwort | Status | Noch zu tun |
|---:|---|---|---|
| 1 | Der exakte YOLOv7-`b066`-Hailo-8→TensorRT-Pfad erreicht historisch ungefähr 97 FPS. | beantwortet und eng hardwarebelegt | nur bei Regression erneut prüfen |
| 2 | Fairness entsteht durch gleiche Strata, Endpunkte und Messbedingungen; Low-Level-Code darf backend- und modellspezifisch sein. v2.79.16 fügt keine neue InferModel-Jobgruppe hinzu; die bestehende Inflight-Konfiguration und P1/FIFO/P2-Pipeline bleiben erhalten. | methodisch beantwortet; UINT8-Part1 hardwarebelegt | vollständige Hailo-10-Splitkette im kleinen Eval-Smoke prüfen; DeepX nur bei gemessenem Overhead optimieren |
| 3 | Die mit verifiziertem FS-Gain kalibrierte Full-System-Gesamtenergie vor optionalem Idle-Abzug ist primär; unskalierte u.RECS-Werte bleiben separat erhalten. M.2-Idle wird nur als sekundäre TensorRT-Full-Normalisierung abgezogen. | Softwarelogik belegt, reale neue Kalibrierung offen | Power Mode festlegen, FS-Kalibrierung und anschließend M.2-Idle je Setup; danach kleiner Native-Energy-Smoke |
| 4 | Hailo-8 und -10H verwenden dieselbe angeforderte Recipe, nicht notwendig identische resultierende Accuracy. | beantwortet | Receipts/Quality im Resultpack kontrollieren; kein Sweep |
| 5 | DeepX nutzt B500/EMA/Opt0 und Classification Mean/Std; die Herstellerlevels sind nicht numerisch vergleichbar. | Softwarefix belegt | formaler ResNet50-Part1-Smoke |
| 6 | Multi-Split bedeutet mehrere Tensoren an einem Splitpunkt und ist Generic-Scope. | vertraglich unterstützt | erfolgreichen realen Generic-Fall aus Resultpack referenzieren; nur falls nötig kurz nachmessen |
| 7 | Native ist maßgeblich für absolute Performance und Energy; Generic dient Screening und Ranking. | entschieden | separates Native+Energy-Finalprofil |
| 8 | Historische 24/24 Paare stützen Generic als Proxy auf der Single-Tensor-Schnittmenge; kein neuer Großlauf und keine Mindestzahl von mindestens zehn Paaren. | Methodenbeleg vorhanden | bis zu drei reale gemeinsame Cases je Modell ehrlich berichten |

## 3.1 Erreicht Native für YOLOv7 ungefähr 97 FPS?

**Ja, für den historischen Hailo-8-Referenzpfad ist das belegt.**

Der Paperfall verwendet:

```text
Case:            b066
Boundary:        mul_20
Shape:           [1, 512, 80, 80]
INT8-Datenmenge: 3.276.800 Byte = 3,125 MiB
```

| Evidenz | Durchsatz |
|---|---:|
| Paper P1/Pipeline | ca. 95 FPS |
| C++-Reproduktion, Makespan | 95,301 FPS |
| v2.79 Resurrection Canary, image-/paperäquivalenter Makespan | 97,013 FPS |
| Three-Stage `p2_output` | 95,902 FPS |
| Three-Stage `completed_detection` | 95,889 FPS |
| archiviertes Three-Stage-Fixture, Median 3 × 1.000 Frames, Raw/P2-Pipeline-Endpoint | 97,077 FPS |
| dasselbe Fixture, `completed_detection` | 97,059 FPS |

Beim 95,902-/95,889-FPS-Beleg betrug das Verhältnis
`completed_detection / p2_output` 0,999869; im archivierten Drei-Wiederholungs-
Fixture lag der Median bei 0,999811. Damit ist gezeigt, dass der
contractgebundene Postpfad den Paperdurchsatz nicht wieder auf etwa 16 FPS
reduziert.

Der frühere Wert von ungefähr 16 FPS war kein Versagen der Splitarchitektur.
Damals lagen dichter Python-Decode, große Raw-Head-Materialisierung,
per-Frame-Hashing, JSON-Aufbau und weitere Evidence-Arbeit im Hotloop. Diese
Messung hatte einen anderen, wesentlich schwereren Endpoint.

Die Zahlen sind historische Hardwareevidenz. Für v2.79.16 sind zusätzlich 14
Paper-Split-Regressionstests bestanden. Das bestätigt den Software- und
Dispatchpfad, ist aber kein neuer Hardwaredurchsatzbeleg. Die alten Remote-
BenchmarkSet- und Cacheartefakte waren bereits bereinigt; der zunächst
versuchte Hardware-Replay endete daher vor jeder Inferenz.

## 3.2 Ist unterschiedlicher Low-Level-Code ein fairer Vergleich?

**Ja – sofern Messvertrag, Stratum, Endpoint und Bedingungen gleich sind.**
Fairness verlangt nicht identischen Low-Level-Code.

HailoRT, DeepX Runtime und TensorRT haben unterschiedliche APIs und sinnvolle
Optimierungsmechanismen. Ein fairer Vergleich erlaubt deshalb
backendspezifische Async-, Inflight-, Buffer- und Queue-Implementierungen.
Gleich bleiben müssen:

- wissenschaftliche Runnerrolle;
- Modell, Case und Splitboundary;
- Richtung und Precision-Vertrag;
- Setup und Backendzuordnung;
- Warmup-, Wiederholungs- und Messdauerpolicy;
- Endpoint und Completed-Work-Unit-Zählung;
- Quality- und Preprocessing-Vertrag;
- Full-System-Energy-Scope für Energievergleiche.

Absolute FPS zwischen Hailo-8, Hailo-10H und DeepX müssen nicht gleich sein.
Fair ist, dass jeder Native-Pfad seinen realistischen Steady State nutzt und
nicht unnötig durch Hostkopien, Python, Queueing oder serielles Postprocessing
gebremst wird.

Die aktuelle Konsequenz lautet:

- Hailo-8: kein Optimierungsbedarf belegt;
- Hailo-10H: UINT8 statt FLOAT32 an der HailoRT-Grenze; keine neue
  InferModel-Jobgruppe; bestehende Inflight-Konfiguration und
  P1/FIFO/P2-Überlappung bleiben erhalten;
- DeepX: bestehende P1/P2-Überlappung bleibt, erst bei gemessenem Mapping-/
  Copy-Overhead gezielt optimieren;
- kein vorsorglicher C++-Rewrite und kein weiterer Inflight-Sweep als
  Final-Run-Gate.

## 3.3 Ist die Energy-Messung einschließlich Idle-Abzug korrekt?

**Die Grundmethode ist bereit. Primär ist die kalibrierte Full-System-
Gesamtenergie vor einem optionalen M.2-Idle-Abzug.** Die u.RECS-Messung wurde
bereits im Rahmen von Joris'
Masterarbeit und durch die ergänzende TEK-Messung ausführlich verifiziert. Eine
erneute Methodenvalidierung ist nicht erforderlich.

Diese Methodenvalidierung ist eine vom Projekt vorgegebene, bereits bestehende
Evidenzgrundlage. Masterarbeit und TEK-Unterlagen waren nicht Teil des hier
geprüften Delivery Bundles; der aktuelle Audit prüfte ihre Toolintegration und
nicht die externe Validierungsstudie erneut.

Der optionale host-normalisierte Zusatzwert lautet:

```text
E_host,norm = max(0, E_FS,cal - P_M.2,idle,cal × t_aktiv)
```

Dieser Abzug gilt ausschließlich als zusätzliche Schätzung für **TensorRT
Full** auf einem Setup, in dem ein ungenutzter M.2-Accelerator mitversorgt wird.
Er gilt nicht für:

- Hailo-Zeilen;
- DeepX-Zeilen;
- Split-/Composed-Zeilen;
- Kalibrierungsfenster.

v2.79.16 skaliert bei verifiziertem Setupfaktor insbesondere
`energy_total_j` und `avg_power_w` vor jedem Baseline-Abzug. Die ursprünglichen
u.RECS-Werte bleiben separat als `full_system_input_unscaled_*` erhalten.
FPS und Energie müssen aus
demselben Hotloop und demselben Endpoint stammen. Für produktionsnahe
Detection-Claims ist `completed_detection` der primäre Energy-Endpoint.

Die drei vorhandenen Idle-Kalibrierungen bleiben als historische
Plausibilitätsevidenz erhalten. Nach dem Speichern eines neuen Full-System-
Gain-Faktors gehören sie jedoch zur alten Skalendomäne und werden von
v2.79.16 absichtlich invalidiert. Dann muss die M.2-Idle-Kalibrierung für das
betroffene Setup erneut ausgeführt werden; Details stehen in Abschnitt 9.

## 3.4 Werden Hailo-8- und Hailo-10H-HEFs mit vergleichbarer Qualität gebaut?

**Ja, beide verwenden dieselbe eingefrorene Policy:**

```text
preset              = balanced
optimization_level  = 1
calibration_items   = 500
calibration_batch   = 8
```

„Gleiche Qualität“ bedeutet hier gleiche Policy und denselben Datenvertrag,
nicht bitidentische Quantisierungsergebnisse unterschiedlicher Chips und
Compilerpfade.

Ein früherer Hailo-8-Canary brachte mit Optimization Level 2 keine Verbesserung:

| Hailo-8-Stufe | AP50:95 |
|---|---:|
| Level 1 | 0,41478 |
| Level 2 | 0,40984 |

Deshalb bleiben Level 1 und B500 eingefroren. Ein weiterer Level- oder
Kalibrationsgrößen-Sweep ist nicht vorgesehen.

## 3.5 Welche Quality-Einstellungen gelten für DeepX?

**Ja.** DeepX verwendet:

```text
calibration_items             = 500
calibration_method            = ema
optimization_level            = 0
classification_preprocessing  = imagenet_mean_std
```

Für Detection bleibt der detection-spezifische Letterbox-/`/255`-Pfad
unverändert. DeepX-Opt0 und Hailo-Opt1 sind nicht numerisch gleichzusetzen;
entscheidend ist die jeweils vorab festgelegte, geprüfte Backendpolicy.

In v2.79.14 konnte DeepX Classification Part1 trotz Profilwert auf
`current_scale_only` zurückfallen. v2.79.15 korrigierte genau diesen Pfad: Für
`imagenet_mean_std` wird das vorhandene Sub/Div-Build-ONNX materialisiert und
genau dieses Artefakt für Cache-Key und DX-COM-Compile verwendet. Detection und
der bewusst manuelle `current_scale_only`-Benchmarkpfad wurden nicht geändert.

Dieser v2.79.15-Fix bleibt Bestandteil von v2.79.16. Offen ist ein kleiner
formaler ResNet50-DeepX→TensorRT-Smoke. Er muss über den Evaluation-Workflow
laufen, nicht nur über den manuellen Benchmark-Tab, und kann in den
vorgesehenen kleinen End-to-End-Eval-Smoke integriert werden.

## 3.6 Was bedeutet „Multi-Split“ in dieser Arbeit?

**Multi-Split bedeutet mehrere Boundary-Tensoren an einem Splitpunkt.**

Es bedeutet nicht mehrere aufeinanderfolgende Splitstellen in einer Pipeline.
Der Generic Runner soll zeigen, dass ein einzelner Splitpunkt mit mehreren
Part2-Eingangstensoren verarbeitet werden kann. Mehrere serielle Splits sind
aus Zeit- und Scopegründen nicht Teil der Kampagne.

## 3.7 Welche Rolle haben Generic und Native?

| Runner | Hauptrolle |
|---|---|
| Generic | breites, score-unabhängiges Screening; Single- und Multi-Tensor-Boundaries; Feasibility, Ranking, Quality und Diagnose |
| Native | hardware-nahe Single-Tensor-Ausführung; primärer Pfad für Performance, Stage-Balance, Handoff, Full-Baselines und Energy |

Die Poststufe ist kein dritter wissenschaftlicher Runner, sondern die dritte
Pipelinephase des Native Runners.

## 3.8 Reicht die Generic↔Native-Korrelation als Methodenbeleg?

**Für die technisch kompatible Single-Tensor-Schnittmenge gibt es einen
ausreichenden historischen Methodenbeleg.** Der v2.77.1-Replay ergab:

```text
24/24 technische Generic↔Native-Paare
17/18 Paarordnungen korrekt
Hit@1: 6/6
Regret@1: 0
Hailo-8:   5/6
Hailo-10H: 6/6
DeepX:     6/6
```

Zulässige Aussage:

> Auf der geprüften technisch kompatiblen Single-Tensor-Schnittmenge bewahrt
> Generic die Native-Rangordnung hinreichend gut und kann dort als skalierbarer
> Screening-Proxy eingesetzt werden.

Nicht zulässig ist, Native-Ausführbarkeit oder Native-Rangordnungen für
Multi-Tensor-Splits daraus abzuleiten.

Für den aktuellen Datensatz werden pro Modell bis zu drei real vorhandene,
identische Single-Tensor-Cases in Generic und Native verwendet:

- drei vorhanden: drei messen;
- ein oder zwei vorhanden: alle vorhandenen messen und deskriptiv berichten;
- kein gültiger Fall: ehrlich `unsupported` beziehungsweise nicht vorhanden;
- keine künstlichen Splits;
- keine belastbare modellinterne Rangkorrelation bei weniger als drei Fällen.

Ein neuer Mindestumfang von zehn oder mehr Paaren ist kein Final-Run-Gate.

---

# 4. Aktuelle Toolarchitektur

## 4.1 Generic Runner

Der Generic Runner deckt den breiten ONNX-Kandidatenraum ab:

- Single- und Multi-Tensor-Grenzen an einem Splitpunkt;
- Feasibility und technische Lifecycle-Zustände;
- score-unabhängigen Audit und Ranking;
- Generic Quality und Diagnose;
- Auswahl der für Native geeigneten Single-Tensor-Schnittmenge.

## 4.2 Native Three-Stage

```text
P1:   Input/Preprocessing → Accelerator Part 1 → Boundary Queue
P2:   Boundary → TensorRT Part 2 → P2 Output Queue
Post: contractgebundene Ergebnisverarbeitung → Completed Endpoint
```

Für Klassifikation:

```text
P1 → P2 → classification_logits
Post = No-op
```

Die Trennung macht sichtbar, ob P1, P2, Handoff, Queueing oder Postprocessing
den Durchsatz begrenzt. Der nachhaltige Pipelinezyklus wird vom langsamsten
Serviceabschnitt bestimmt.

## 4.3 Endpunkte

| Endpoint | Verwendung |
|---|---|
| `p2_output` | technischer Vergleich, Stage-Balance, Handoff und Generic↔Native-Brücke |
| `completed_detection` | produktionsnaher Detection-Endpunkt nach contractgebundenem Postprocessing |
| `classification_logits` | terminaler Classification-Endpunkt; Top-1/Top-5 außerhalb des Timingfensters |

`p2_output`-FPS dürfen nicht mit Energie eines
`completed_detection`-Hotloops kombiniert werden. Generic↔Native wird am
gleichen P2-/Modelloutput-Endpunkt verglichen; `completed_detection` wird
zusätzlich, aber getrennt berichtet.

## 4.4 Adapterfamilien

| Adapter | Modellfamilie / Vertrag |
|---|---|
| `classification_logits_noop` | ResNet50, MobileNetV3 Large, RegNet-X-1.6GF |
| `yolov7_anchor_multiscale_sparse` | drei YOLOv7-Heads, 80/40/20, Sparse Decode und eingefrorene NMS-/Geometriepolicy |
| `yolo26_decoded_nms_materialize` | bereits decodierter BN6-Output; kein zweites NMS |
| `yolo11_regcls_dfl16` | sechs Heads: drei DFL16-Regression und drei C80-Klassifikation; fail-closed bei unklarer Bindung |

Universell ist die contractgebundene Pipelinearchitektur, nicht ein
heuristischer Universaldecoder.

---

# 5. Quality-, Applicability- und Timingvertrag

## 5.1 Was außerhalb und innerhalb des Performancefensters liegt

**Preflight:**

- Modell-, Setup-, Boundary- und Outputvertrag binden;
- Dataset, Reference, Preprocessing und Adapter prüfen;
- Thresholds, Anchors, Strides und NMS-Policy festlegen;
- benötigte Artefakte und Cache-Zuordnung prüfen.

**Performancefenster:**

- P1 und P2;
- Queue-/Handoff-Arbeit;
- contractgebundener Fast-Postpfad;
- echte Framecompletion.

**Nicht im Performancefenster:**

- per-Frame-Hashes großer Outputtensoren;
- JSON-/Evidenzaufbau;
- langsamer Oracle;
- B500- oder Official-COCO-Evaluation;
- generische Contractsuche pro Frame.

**Postflight:**

- Counter und Completed Work Units prüfen;
- Fastpath stichprobenartig gegen Oracle beziehungsweise plausiblen Output
  absichern;
- Quality getrennt bestimmen;
- Abweichungen sichtbar fehlschlagen lassen.

## 5.2 Zustandsmodell für Quality

| Zustand | Bedeutung |
|---|---|
| `completed` | eindeutig gebundenes Quality-Ergebnis liegt vor |
| `blocked` | Quality wäre anwendbar, Build-/Runtimefehler verhindert sie |
| `quality_not_applicable` | der verbindliche Vertrag besitzt keinen anwendbaren Quality-Endpoint |
| `missing` | Quality wäre anwendbar und nicht blockiert, Evidenz fehlt |

`quality_not_applicable` ist weder PASS noch `missing`.

## 5.3 Historische 163 `Quality N/A`

Die 163 Fälle des v2.78.4-Fixtures waren für technische P2-Pfade ohne passend
gebundenen Completed-Task-Quality-Endpoint korrekt. Sie waren kein allgemeines
Qualitätsziel. Die Zustandsbilanz lautete:

```text
551 materialisierte Sollidentitäten
├── 386 completed Quality
├── 163 quality_not_applicable
├──   1 blocked
└──   1 missing
```

Für neue, vollständig gebundene Runs ist `Quality N/A = 0` wünschenswert, aber
nur wenn wirklich jeder Sollfall einen anwendbaren Quality-Endpoint besitzt.

---

# 6. Native-Performance und Runneroptimierung

## 6.1 Hailo-10H

Der Split-Runner verwendet bereits HailoRT-Async-Ausführung,
wiederverwendbare Binding-Slots, konfigurierbares Inflight und eine
Producer-/Consumer-Pipeline mit FIFO. Ein Rewrite ist nicht begründet.

Für den fairen Vergleich wird **keine zusätzliche InferModel-Jobparallelität**
eingeführt. Die bereits konfigurierte Inflight-Tiefe bleibt unverändert;
v2.79.16 ergänzt keine weitere Jobgruppe. Zusätzlich überlappen P1 und
TensorRT P2 über das FIFO. Der nachhaltige Pipeline-Durchsatz wird vom
langsameren Abschnitt einschließlich Handoff und Backpressure bestimmt. Das
entspricht derselben methodischen Betrachtung wie beim Hailo-8-Paperpfad.

Der Hailo-10-Input-A/B-Test zeigte für denselben HEF und genau einen
ausstehenden Job:

| Variante | Host-Input | Mean-Latenz Part 1 | Single-Job-FPS |
|---|---:|---:|---:|
| FLOAT32-Eingang | 4.915.200 Byte/Frame | 49,618 ms | 20,151 |
| HEF-nativer UINT8-Eingang | 1.228.800 Byte/Frame | 12,769 ms | 78,280 |

Die Outputs waren elementweise exakt identisch. UINT8 reduzierte die
Host-Inputdatenmenge um Faktor 4 und beschleunigte die einzelne Inferenz um
Faktor 3,885. Eine separat gemessene Referenzquantisierung von ungefähr
1,259 ms war nicht Teil der InferModel-Zeit. Deshalb verwendet v2.79.16 am
Hailo-10-Eingang und -Ausgang den HEF-nativen UINT8-Vertrag.

Der aktuelle Hardware-Smoke mit dem installierten v2.79.16-Code bestätigte:

```text
HAILO10_UINT8_HEF_SMOKE=PASS
runtime_api       = infer_model
quantized_inputs  = true
quantized_outputs = true
input dtype       = uint8
output dtype      = uint8
runs              = 20
mean              = 13,335 ms
min / max         = 13,107 / 13,442 ms
```

Dieser diagnostische HEF-Smoke lief mit Inflight 1. Das produktive v2.79.16-
Profil behält dagegen seine bereits vorhandene Inflight-Einstellung 8.
Die Closure fügte keine neue Jobgruppe oder zusätzliche Parallelitätsebene
hinzu; sie setzt das bestehende Profil auch nicht pauschal auf Inflight 1.

Die ungefähr 75 FPS dieses kurzen Smokes liegen nur rund 4 % unter dem A/B-
Wert und sind plausibel. Der Smoke führte echte Hailo-10-Part1-Inferenz aus,
war aber ausdrücklich diagnostisch und enthielt TensorRT P2 noch nicht. Die
vollständige Kette wird im kleinen Eval-Smoke geprüft.

## 6.2 DeepX

DeepX P1 läuft synchron, wird aber über zwei Threads und FIFO mit TensorRT P2
überlappt. Da die Runtime Ausgabepuffer wiederverwenden kann, wird die Boundary
besitzend materialisiert. Das ist korrekt, kann aber Hostkosten verursachen.

Vorgehen nur bei gemessenem Engpass:

1. Mapping-, Copy-, Queue- und Stagezeiten ansehen.
2. Bei relevantem Kopieranteil zuerst einen kleinen wiederverwendbaren
   Boundary-Buffer-Pool prüfen.
3. Erst danach verfügbare Async-/Batch-Fähigkeiten der Runtime untersuchen.
4. C++ nur erwägen, wenn kleine Maßnahmen den belegten Engpass nicht lösen.

## 6.3 Pragmatische Diagnosegrenzen

Diese Werte sind Engineering-Hinweise, keine neuen wissenschaftlichen
Abnahmegesetze:

| Prüfung | Hinweiswert | Reaktion bei Abweichung |
|---|---:|---|
| vollständige Wiederholungen | 3/3 | nur betroffene Zeile wiederholen |
| Durchsatz-CV | ungefähr ≤ 5 % | Ursache und Drift prüfen |
| Pipeline-Realisierung relativ zum Stage-Bottleneck | ungefähr ≥ 0,90 | Host-/Queue-/Post-Overhead lokalisieren |
| Handoff/Mapping/Copy | ungefähr ≤ 10 % des Bottleneck-Zyklus | kleinen backendlokalen Fix prüfen |
| `completed_detection_fps / p2_output_fps` | ungefähr ≥ 0,95 | bei deutlichem Postverlust Postpfad untersuchen |

Ein einzelner Hinweiswert löst keinen breiten Rewrite aus; entscheidend sind
reproduzierbare Telemetrie und materielle Auswirkung.

---

# 7. Generic↔Native-Vergleichsvertrag

Ein gültiges Vergleichspaar besitzt dieselben Werte für:

```text
model_id
case_id / Boundary
setup_id
backend
direction
precision / runtime precision identity
P2-/Modelloutput-Contract
Messphase und Wiederholungspolicy
```

Verglichen wird:

```text
Generic P2-/Modelloutput-Endpunkt ↔ Native p2_output
```

`completed_detection` ist ein zusätzlicher Anwendungsendpoint und wird nicht
in dasselbe Rankingstratum gemischt. Multi-Tensor-Ergebnisse des Generic Runners
werden nicht in Native-Rankings extrapoliert.

Der historische 24/24-Replay bleibt der Methodenbeleg. Der aktuelle Final Run
muss keine neue große Methodenstudie wiederholen. Die aktuelle Version soll
lediglich die real verfügbaren gemeinsamen Single-Tensor-Fälle sauber binden
und berichten.

---

# 8. Energy-Messvertrag

## 8.1 Primäre Messung

| Feld | Finaler Sollwert |
|---|---|
| Pfad | Native only |
| Modus | `measure` |
| Dauer | 60 s je Wiederholung |
| Wiederholungen | 3; mehr nur bei auffälliger Streuung |
| physischer Scope | `FS` |
| Fenster | `command` |
| Generic Energy | aus |
| CPU-/ORT-Energy | aus |
| Primärwert | mit verifiziertem FS-Gain kalibrierte Full-System-Energie, vor optionalem Idle-Abzug |
| Originalwert | unskalierte u.RECS-Felder bleiben separat als `full_system_input_unscaled_*` erhalten |

Die Messdauer ist ein aktives Command-Fenster. Collector und Workload müssen
erfolgreich sein; der Trace muss das Fenster abdecken und darf keine relevanten
Dropped Samples zeigen. Completed Work Units stammen aus demselben Hotloop.

`FS` und `native_only` beschreiben unterschiedliche Dinge:

- `FS` ist der physische Messumfang der u.RECS-Eingangsleistungsmessung;
- `native_only` ist der geplante Ausführungspfad, in dem der Collector gestartet
  wird.

Für das aktuelle Finalprofil bleibt Native Energy der vorgesehene primäre
Energiepfad. Falls ein Benutzerlauf jedoch Generic-Arbeit ausdrücklich in die
Energy-Auswahl einschließt, darf v2.79.16 dies nicht unbemerkt als
`native_only` auflösen. Der kombinierte Pfad muss sichtbar aktiviert werden
oder die Planung muss mit einem verständlichen Blocker abbrechen.

## 8.2 Optionale TensorRT-Full-Normalisierung

Nur für TensorRT Full darf zusätzlich ausgewiesen werden:

```text
P_host,norm = max(0, P_FS,cal - P_M.2,idle,cal)
E_host,norm = max(0, E_FS,cal - P_M.2,idle,cal × t_aktiv)
```

Dieser Wert ist eine gekennzeichnete Schätzung. Er ersetzt weder die
kalibrierte Full-System-Gesamtgröße noch die separat erhaltenen unskalierten
u.RECS-Felder und wird nicht für Accelerator- oder Splitzeilen verwendet.

## 8.3 Plausibilitätsprüfung je Zeile

- Setup, Modell, Case, Backend und Endpoint stimmen;
- drei gültige Wiederholungen mit ungefähr 60 s aktivem Fenster;
- `physical_scope = FS` und `window_label = command`;
- Collector-/Workloadstatus erfolgreich;
- keine relevanten Samples verworfen;
- Completed Work Units positiv und aus demselben Hotloop;
- näherungsweise `P ≈ E / t`;
- kalibrierte Primärwerte und separat erhaltene unskalierte u.RECS-Werte
  positiv und zwischen Wiederholungen plausibel;
- `full_system_current_scale_verified=true` und Faktor vor Baseline-Abzug
  angewendet;
- Idle-Korrektur nur bei TensorRT Full;
- auffälliger CV oder zeitliche Drift wird dokumentiert.

Nur eine ungültige oder auffällige Zeile wird nachgemessen. Zusätzliche
Wiederholungen werden nicht pauschal auf die gesamte Matrix ausgedehnt.

## 8.4 Zeilenlokale Fehler und Rohenergie

Der Lauf `biggerset_20260903_090110` zeigte den früheren Fehler eindeutig:

```text
native_energy_requested = true
native_energy_enabled   = true
physical_scope          = FS
execution_path          = native_only
benchmark_set_invalid:yolov7_ultralytics
transfer_attempted      = false
started_remote_count    = 0
started_performance_count = 0
energy measurements     = 0
```

Ein einzelner ungültiger YOLOv7-Preflight beendete damals die gesamte Native-
Stufe vor Transfer, Runtime und Collectorstart. Daher wurde trotz aktivierter
Energy-Option physisch keine Energie gemessen. Das war weder ein u.RECS- noch
ein Full-System-Scope-Problem.

Der in v2.79.16 implementierte Vertrag für den direkten, non-variant
Ausführungspfad lautet:

- modellbezogene Preflight-Fehler blockieren nur die betreffende Modellzeile;
- technische Quality-/Contract-Probleme werden der betreffenden Zeile
  zugeordnet;
- andere gültige Modelle dürfen Transfer, Performance, Native und Energy
  fortsetzen;
- echte Infrastrukturfehler wie nicht erreichbares u.RECS, SSH-/Authfehler,
  Plattform-Lock oder nicht initialisierbarer Collector bleiben global;
- kann eine technisch auffällige Zeile physisch ausgeführt werden, darf
  Rohenergie erfasst werden, wird aber nicht als qualifizierte Quality-Energie
  freigegeben.

Für diesen letzten Fall werden insbesondere folgende Statuswerte erwartet:

```text
energy_quality_qualified: false
energy_quality_status: raw_energy_quality_not_qualified
native_energy_after_technical_error: collect_raw_quality_unqualified
```

`raw_energy_quality_not_qualified` bedeutet hier physisch erfasst, aber nicht
für den Quality-Vergleich qualifiziert. Es bedeutet nicht unskaliert. Die
ursprünglichen Messkettenwerte sind separat an den
`full_system_input_unscaled_*`-Feldern erkennbar.

Kann eine Zeile gar nicht gestartet werden, bleibt sie ohne Energie und erhält
einen expliziten Grund, beispielsweise:

```text
Energy requested, not started:
Native preflight blocked by benchmark_set_invalid:yolov7_ultralytics
```

Dieser Vertrag ist offline getestet. Der unveränderte Variant-Koordinator wird
davon nicht erfasst und für diese Closure nicht beansprucht. Der reale kleine
Eval-Smoke muss noch zeigen, dass die gültigen Zeilen des tatsächlich genutzten
direkten Pfads weiterlaufen und Energie erfassen. Ein künstlich defektes Modell
wird für den regulären Mini-Eval nicht eigens erzeugt; tritt ein Zeilenfehler
natürlich auf, wird genau dieses Verhalten mitgeprüft.

---

# 9. Full-System- und M.2-Idle-Kalibrierung

## 9.1 Neue geführte Full-System-Eingangskalibrierung

v2.79.16 ergänzt einen setupbezogenen Gain-Abgleich der Full-System-
Eingangsmessung. Bei beiden Lastpunkten wird nicht mehr blind mit exakt 0,5 A
beziehungsweise 1,0 A gerechnet. Die GUI fordert den tatsächlich von der
elektronischen Last angezeigten Strom an:

Die elektronische Last wird als Stromsenke von `9V_20V_IN` auf der Lastseite
hinter R16 nach GND angeschlossen. Der 5-V-Header ist ausdrücklich ungeeignet,
weil sein Laststrom wegen des vorgeschalteten Wandlers nicht demselben
Stromsprung am Full-System-Eingangsshunt entspricht. Der Assistent schaltet
M.2 und Jetson für die Kalibriersequenz kontrolliert aus und stellt beide erst
nach der verpflichtenden 0-A-Bestätigung wieder her.

```text
Sollpunkt: 0,5000 A
Tatsächlich angezeigter Strom: [ 0,4978 ] A

Sollpunkt: 1,0000 A
Tatsächlich angezeigter Strom: [ 0,9963 ] A
```

Dabei gilt:

- die Felder sind mit 0,5000 A beziehungsweise 1,0000 A vorbelegt;
- Vorbelegung und Anzeige verwenden vier Nachkommastellen; vierstellige
  Ist-Stromwerte werden unterstützt. Das numerische Feld erzwingt technisch
  keine harte Obergrenze von exakt vier Nachkommastellen;
- der eingegebene Ist-Strom wird zusammen mit der tatsächlichen
  Lastspannung für Referenzleistung und Fit verwendet;
- der nominelle Sollpunkt bleibt zusätzlich in der Evidenz erhalten;
- `idle_before`, `idle_between` und `idle_after` bleiben Bestandteil des
  Ablaufs;
- Abbrechen beendet den Kalibrierpunkt kontrolliert;
- die elektronische Last muss vor der Wiederherstellung ausdrücklich wieder
  auf 0 A stehen;
- Hardwarezustände werden bei Erfolg beziehungsweise kontrolliertem Recovery
  wiederhergestellt.

Die reale Kalibrierung ist für alle drei Setups noch **PENDING**. Erst ein
bestandener Quality-Gate- und Save-Vorgang macht den jeweiligen FS-Faktor
produktiv.

## 9.2 Bisherige M.2-Idle-Messwerte

Die drei bisherigen setupbezogenen Kalibrierungen bleiben als historische
Plausibilitäts- und Vergleichswerte erhalten:

| Setup | Accelerator | FS ohne M.2 | FS mit M.2 | M.2-Idle-Delta |
|---|---|---:|---:|---:|
| `orin_nx_deepx_m1_01` | `deepx_m1` | 8,9373 W | 11,5602 W | 2,6229 W |
| `orin_nx_hailo8_01` | `hailo8` | 13,1897 W | 15,4068 W | 2,2171 W |
| `orin_nx_hailo10_01` | `hailo10` | 12,8263 W | 13,8969 W | 1,0706 W |

Alle drei damaligen JSONs melden:

```text
physical_scope   = FS
measurement_scope = full_system
status           = ok
saved            = true
restored_m2_on   = true
```

Die Kalibrierung war jeweils ein direkter Full-System-Off/On-Zyklus und ist
eine technische Baseline, kein Benchmark- oder Claimwert. Nach dem Speichern
des neuen Full-System-Gain-Faktors darf sie nicht unverändert weiterverwendet
werden: v2.79.16 entfernt dann absichtlich alte `idle_baseline_w`-,
`accelerator_idle_w`- und M.2-Idle-Evidenzfelder aus der alten Skalendomäne.
Für jedes erfolgreich neu kalibrierte Setup ist deshalb anschließend die
M.2-Idle-Kalibrierung erneut auszuführen.

## 9.3 Warum in den alten JSONs trotzdem ein `MB`-Feld vorkommt

Die drei Dateien enthalten in
`configuration_projection.energy_defaults.physical_scope` noch `MB`. Dieses
Feld ist ein Snapshot der damals vorhandenen Registry-Voreinstellung. Es ist
**nicht** der Scope der ausgeführten Kalibrierungsmessung. Die maßgeblichen
Top-Level-Felder der Messung lauten `physical_scope: FS` und
`measurement_scope: full_system`.

Seit v2.79.15 wird deshalb nur ein fehlender oder exakt alter `MB`-Default auf
`FS` gesetzt. Es werden nicht umetikettiert:

- historische Messergebnisse, die tatsächlich `MB` trugen;
- echte MB-/MiB-Bandbreiten- oder Größenangaben;
- ähnlich geschriebene benutzerdefinierte Werte.

Aus dem historischen `MB`-Projektionsfeld allein ist keine Wiederholung und
keine neue Hash-/Seal-Kette abzuleiten. Die nun erforderliche Wiederholung
entsteht ausschließlich durch den neuen FS-Gain-Faktor und den damit
verbundenen Wechsel der Skalendomäne.

## 9.4 Auffällig niedrige DeepX-Idle-Leistung

Der bisherige DeepX-Wert von 8,9373 W ohne M.2 liegt deutlich unter den
entsprechenden Hailo-Setups. Das kann durch reale Host-, Board-, Peripherie-,
Temperatur- oder Power-Mode-Unterschiede entstehen und ist nicht automatisch
ein Messfehler. Vor dem EvalRun werden deshalb auf allen drei Jetsons
`nvpmodel`-Modus und relevante Clock-/Governor-Einstellungen verglichen.
Insbesondere darf der DeepX-Jetson nicht unbemerkt in einem sparsameren Modus
laufen. Die Setups sollen denselben vorab festgelegten Power-Mode-Vertrag
verwenden; dynamische oder fixierte Clocks müssen konsistent dokumentiert sein.
Eine endgültige Interpretation erfolgt erst mit den drei neu skalierten
FS-/M.2-Idle-Werten; der alte DeepX-Wert bleibt bis dahin nur ein Hinweis.

---

# 10. Auditstand v2.79.16

## 10.1 Umgesetzter aktueller Stand

v2.79.16 übernimmt die tragfähige v2.79.15-Basis und schließt drei akute
Punkte, ohne eine neue Parallelitäts- oder manuell zu pflegende
Provenienzebene einzuführen:

1. Hailo-10 Native Split verwendet an den HEF-Grenzen native UINT8-Ein- und
   -Ausgaben mit VStream-spezifischer Quantisierung und Dequantisierung.
2. Die Full-System-Kalibrierung trennt die nominellen Sollströme von den
   tatsächlich eingegebenen Ist-Strömen; nur die Ist-Werte gehen in
   Referenzleistung und Fit ein.
3. Modellbezogene Preflight- und technische Quality-Fehler werden im direkten,
   non-variant Pfad zeilenlokal behandelt. Rohenergie kann, sofern die Zeile
   physisch läuft, als nicht quality-qualifiziert erhalten bleiben.

Zusätzlich wird der bereits vorhandene Wert
**producer_identity.preprocessing_contract_sha256** wertgleich an die
bereits verlangte Candidate-/Request-Top-Level-Stelle weitergereicht. Es wird
dafür kein neuer Hash berechnet. Der Variant-Koordinator blieb unverändert und
wird von dieser Closure nicht beansprucht.

Aus der bestehenden Plattform-Power-Basis bleiben wirksam:

- **m.2** ist der kanonische Registry-Default; nur der exakte Legacywert
  **m2** wird eng zu **m.2** migriert;
- **FS** und **command** sind die aktuellen Energy-Defaults; die davon
  unabhängige alte **MB**-Migration bleibt eng;
- eine vorhandene automatisierte Evidenzprüfung bleibt erhalten, ohne neue
  manuelle Manifest-, Hash-, Seal- oder Signaturarbeit einzuführen;
- der DeepX-Classification-Part1-Pfad verwendet bei **imagenet_mean_std** das
  materialisierte Sub/Div-Build-ONNX für Cache-Key und DX-COM-Compile.

## 10.2 Aktuelle Verifikation

| Prüfung | Ergebnis | Reichweite |
|---|---|---|
| fokussierte v2.79.16 Release-Acceptance | 468 bestanden, 0 fehlgeschlagen | offline |
| Release-Smoke, Source-Manifest, Compileall und Shell-Syntax | PASS | offline |
| Source-Manifest | 1.264 Release-Dateien, PASS | offline |
| deterministisches Source-ZIP | 1.266 Mitglieder, CRC und Inhaltsvergleich PASS | offline |
| Installationssimulation bei gleicher Version | PASS; venv und Zusatzprofil erhalten | offline |
| geerbter 25-Test-Problem-Subset | pristine 13 PASS/12 FAIL; UPDATED 13 PASS/12 FAIL mit denselben Failed-Node-IDs | Regressionparität, kein Full-Suite-PASS |
| reale Installation auf Smartmirror2 | INSTALL_ACCEPTANCE=PASS; FINAL_STAGE=complete | Zielsystem, ohne Installer-Hardwareaktion |
| fokussierter Paper-Split-Test | 14/14 bestanden in 1,29 s | offline |
| Hailo-10H HEF-Smoke | 20/20 Inferences; UINT8-Ein-/Ausgang; InferModel | aktuelle Zielhardware, nur Part 1 |

Die 468/468 Tests bezeichnen ausschließlich die fokussierte
Release-Acceptance. Der geerbte Problem-Subset bleibt transparent bei 12
Fehlern. Identische fehlgeschlagene Test-IDs vor und nach der Closure belegen
für diesen Subset nur Regressionparität, nicht eine vollständig grüne
Gesamttestsuite.

Der reale Hailo-10H-Smoke meldete 13,335 ms Mittelwert, 13,107 ms Minimum und
13,442 ms Maximum. Das entspricht ungefähr 75 FPS und bestätigt den
integrierten UINT8-Part1-Pfad. Er bestätigt noch nicht die vollständige Kette
**P1 → FIFO → TensorRT P2**.

Die Installations-Evidenz des realen Zielsystems wurde unter
**v27916_install_acceptance_20260903_154343_058884999_781004.zip** erzeugt;
der ausgegebene SHA-256-Wert lautet
**c490e5d6b0610c90c3ea4addd50a9f1a291d81638e742866d94341ecdcb1703a**.
Diese Prüfsumme ist eine vorhandene Installationsangabe, keine neue
Kampagnenanforderung.

## 10.3 Bewusste Grenze der Freigabe

Das formale Statusfeld des UPDATED-Lieferpakets lautet
`SOFTWARE_PASS_HARDWARE_PENDING`. Nach der inzwischen real bestandenen
Installation und dem Hailo-10-Part1-Smoke verwendet diese Knowledge Base das
genauere Arbeitsurteil:

~~~text
INSTALLATION_PASS_TARGETED_SMOKES_PASS_CALIBRATION_AND_E2E_PENDING
~~~

Der Installer-PASS beweist die installierte Identität und fokussierten
Softwareverträge. Der Paper-Test ist offline. Der Hailo-10-Smoke führte echte
Part1-Inferenz aus, aber weder TensorRT P2 noch einen vollständigen
Evaluation-Workflow. Noch offen sind die reale Full-System-Kalibrierung, die
anschließende neue M.2-Idle-Kalibrierung, ein Full-Chain-Hailo-10-Lauf und ein
kleiner Energy-Eval mit vollständiger Finalisierung.

Die zunächst versuchten manuellen Paper-/Hailo-10-Full-Smokes scheiterten
bereits an bereinigten alten Remote- und Cachepfaden. Sie führten keine
Hardwareinferenz aus und sind deshalb weder PASS noch Gegenbeleg gegen v2.79.16.

## 10.4 Das Sieben-Modell-Profil ist kein automatisch fertiges Finalprofil

Das aktuelle Profil **complete_set_7models_v27916_b500_audit20.yaml** bleibt
ein Screening-/Auswahlprofil. Für den echten Kampagnenlauf ist die aufgelöste
Startzusammenfassung maßgeblich. Insbesondere dürfen Native, Energy,
Messdauer, Repeats und Case-Cap nicht nur aus dem Profilnamen abgeleitet
werden. Wenn Energy bewusst nur Native umfasst, ist **native_only** korrekt.
Wenn die Auswahl auch Generic Energy einschließt, muss der kombinierte Pfad
sichtbar aktiviert werden oder ein sichtbarer Planungsblocker entstehen.

## 10.5 Historische v2.79.15-Softwarebasis

v2.79.15 hatte als damaligen fokussierten Stand 322 bestandene Tests und einen
optionalen Skip. Es etablierte insbesondere FS-/command-Defaults, die enge
MB→FS-Migration und den DeepX-Classification-Part1-Mean/Std-Fix. Dieser Stand
bleibt als Entwicklungshistorie relevant, ist aber als aktuelle Freigabe durch
die v2.79.16-UPDATED-Acceptance mit 468/468 Tests und die oben dokumentierte
reale Installation abgelöst. Alte v2.79.15-Paketnamen, Prüfsummen und Gates
sind Archivangaben und keine aktuellen Arbeitsanweisungen.

---

# 11. Dauerhafte historische Evidenz

## 11.1 v2.78.4-Sieben-Modell-Langlauf

Der Lauf bleibt eine wertvolle Legacy-Fixture, war aber weder eine vollständige
Final-Accuracy- noch Native- oder Energy-Evaluation.

```text
Status: RECONCILED_WITH_REAL_GAPS
claim_eligible = false
final_evaluation_complete = false
native_enabled = false
energy.enabled = false
official_coco_enabled = false
```

| Kennzahl | Wert |
|---|---:|
| rohe normalisierte Repräsentationen | 1.087 |
| materialisierte erforderliche logische Identitäten | 551 |
| vorhandene logische Identitäten | 550 |
| fehlende materialisierte Identitäten | 1 |
| zusätzliche Mirror-/Repräsentationszeilen | 537 |
| primäre Quality-Ergebnisse | 386 |
| Quality-only-Companions | 21 |
| gesamte Quality-Population | 407 |
| Primary PASS / FAIL / INCONCLUSIVE | 198 / 135 / 53 |

Reale historische Lücken:

- `yolo11l / hailo10 / full`: Build-Hard-Timeout, Matrixzeile fehlt;
- `yolo11l / deepx_m1 / full`: kompiliert, Runtime fehlgeschlagen;
- `yolo11l / hailo8 / full`: Hard-Timeout plus Plan-/Scope-Diskrepanz.

Die Zahl 551 beschreibt die materialisierte Required-Matrix, nicht sicher den
vollständig eingehaltenen globalen Scope. Historische v2.78.4-Ergebnisse dürfen
als Parser-/Normalizer-/Reconciliation-Fixture dienen, aber nicht als
v2.79.16-Hardwareergebnis.

## 11.2 Weitere Native-/Adapterevidenz

| Evidenz | Ergebnis | Einordnung |
|---|---:|---|
| YOLOv7 Three-Stage-Parität | 32/32 exakt | historisch hardwarebelegt |
| YOLO26s Three-Stage-Parität | 32/32 exakt | historisch hardwarebelegt |
| YOLO26s `p2_output` | 152,702 FPS | historisch hardwarebelegt |
| YOLO26s `completed_detection` | 152,698 FPS | historisch hardwarebelegt |
| Hailo-10H Producer Smoke | 300/300, 34,659 FPS | Producergrundlage, kein vollständiger Finalpfad |
| DeepX Producer Smoke | 300/300, 40,493 FPS | Producergrundlage, kein vollständiger Finalpfad |
| YOLO11 Real-ORT-Parität | 16/16 PASS | Adaptergrundlage |
| v2.79.16 Hailo-10H HEF-Smoke | 20/20; UINT8 I/O; 13,335 ms | aktuell hardwarebelegter Part1-Smoke, noch keine vollständige Splitpipeline |

YOLO26 liefert bereits einen `[1,300,6]`-Output mit `xyxy`, Score und Klasse;
die Poststufe darf daher kein zweites NMS ausführen.

## 11.3 Biggerset-Lauf als Diagnosefixture

Der Lauf **biggerset_20260903_090110** ist analytisch nützlich, aber kein
claim-tragender Final Run. Im gewählten Satz befand sich versehentlich
**yolo26x**; dafür fehlte **regnet_x_1_6gf**. Das ist ein Auswahlfehler des
Laufs und kein Modell- oder Tooldefekt.

Der Debug-Pack zeigte neun technische Quality-Probleme:

- fünf Generic-Composed-Requests benötigten den bereits unter
  **producer_identity.preprocessing_contract_sha256** vorhandenen Wert auch
  an der verlangten Top-Level-Stelle; v2.79.16 reicht genau diesen Wert nun
  weiter, ohne einen neuen Hash zu berechnen;
- vier weitere Fehler gehörten zur versehentlich aufgenommenen
  YOLO26x-Referenz.

Der YOLOv7-Preflightfehler **benchmark_set_invalid:yolov7_ultralytics** führte
im alten Ablauf zu einem globalen Native-Abbruch vor Transfer und Collector.
Deshalb entstanden null Energiemessungen. Die zeilenlokale Korrektur dafür ist
im direkten, non-variant v2.79.16-Pfad offline geprüft; ihr realer
Mehrmodellnachweis steht noch aus.

Unabhängig davon registrierte der Lauf die Dateien
**reports/prediction_vs_benchmark.csv** und
**reports/validation_summary.csv**, bevor eine Legacy-Cleanup-Liste sie
entfernte. Der Finalizer endete deshalb mit
**artifact_index_registered_file_missing**. Dieser Finalisierungsbefund ist
nicht Teil der Drei-Punkte-Closure und muss im kleinen End-to-End-Smoke
explizit kontrolliert werden. Zusätzlich bleiben beobachtete Case-/Scope-
Diskrepanzen und uneinheitliche FPS-Projektionen zeilenweise zu prüfen.

---

# 12. Aktuelle TODO- und Gate-Matrix

## 12.1 Erledigt

| Thema | Status |
|---|---|
| v2.79.16 Installation | DONE – reale Installation: INSTALL_ACCEPTANCE=PASS, FINAL_STAGE=complete |
| v2.79.16 fokussierte Offline-Acceptance | DONE – 468/468 bestanden; kein Full-Suite-PASS |
| Paper-Split-Regression | DONE offline – 14/14 bestanden; historischer Hardwarewert ungefähr 95,9–97,1 FPS |
| Hailo-10H UINT8 | DONE für realen HEF-Part1-Smoke – 20/20, UINT8 I/O, InferModel, ungefähr 75 FPS |
| Hailo-10 Input-A/B | DONE – ungefähr 3,885-fach schneller und viermal weniger Inputbytes als FLOAT32; exakte Outputparität |
| FS-/command-Defaults | DONE im Code; enge MB→FS-Migration bleibt bestehen |
| m.2-Default | DONE; nur exakter Legacywert m2 wird zu m.2 migriert |
| Native-Preflight-/Quality-/Contract-Isolation | DONE und offline geprüft im direkten, non-variant Pfad; reale Mehrmodellprüfung offen |
| DeepX Classification Part1 | DONE im Code – Mean/Std-Sub/Div-Build-ONNX wird kompiliert und gecacht |
| Hailo-/DeepX-Qualitypolicy | DONE – Hailo balanced/Opt1/B500/Kalibrationsbatch 8; DeepX EMA/Opt0/B500 |
| Multi-Tensor-Vertrag | DONE im Generic-Vertrag; Native bleibt Single-Tensor |
| neue Hash-/Seal-Infrastruktur | bewusst nicht eingeführt |
| alte M.2-Idle-Werte | nur historische Plausibilität; nach neuer FS-Gain-Kalibrierung nicht produktiv weiterverwenden |

## 12.2 Muss vor dem Final Run erledigt werden

| Gate | Aktion | Bestanden, wenn |
|---|---|---|
| G0 – Power-Mode-Vertrag | nvpmodel, Clock-/Governor-Policy und relevante Systemzustände auf allen drei Jetsons vergleichen und für die Kampagne festlegen | Unterschiede sind beseitigt oder ausdrücklich dokumentiert; besonders niedriger DeepX-Idlewert eingeordnet |
| G1 – FS-Gain je Setup | geführte Full-System-Eingangskalibrierung an realer elektronischer Last für Hailo-8, Hailo-10H und DeepX durchführen | Soll- und Ist-Ströme getrennt; Quality Gate PASS; Save bestätigt; Registry zeigt verifizierten Faktor |
| G2 – M.2-Idle neu | nach festgelegtem Power Mode und jedem gespeicherten FS-Faktor die M.2-Idle-Kalibrierung desselben Setups erneut aufnehmen | neue Baseline gehört zur neuen Skalendomäne und zum Kampagnen-Power-Mode; Restore erfolgreich; plausibler Off-/On-Unterschied |
| G3 – genau ein Mini-Eval | mindestens yolo26s/b024 auf allen drei Setups mit Native und Energy ausführen; ResNet50/DeepX möglichst im selben Lauf ergänzen | vollständiger direkter End-to-End-Pfad startet und endet kontrolliert |
| G4 – Mini-Eval-Abnahme | Hailo-10 Full Chain, Energy und Finalisierung prüfen | P1→FIFO→TensorRT P2 läuft; Energie ist positiv; full_system_current_scale_verified=true; CSV-Reports existieren; Finalizer endet ohne artifact_index_registered_file_missing |
| G5 – Energy-Plan | effektiven Energy-Plan gegen die bewusste Auswahl prüfen | Native-only bleibt nur bei bewusster Native-only-Wahl; ausdrücklich gewählte Generic Energy wird kombiniert geplant oder sichtbar blockiert |
| G6 – Finalprofil und Kandidaten | eigenes Finalprofil speichern und reale Single-Tensor-Fälle kontrollieren | sieben korrekte Modelle einschließlich RegNet; 0/1/2/3 reale Fälle transparent; Native measure; 60 s; 3 Repeats; FS/command; keine unbeabsichtigte yolo26x-Zeile |

Nach G0–G6 ist der große EvalRun freigegeben.

## 12.3 Nur bei konkretem Befund

Die UPDATED-Testanleitung empfiehlt zusätzlich einen separaten direkten
Mehrmodell-u.RECS-Smoke mit absichtlich ungültiger Native-Preflight-Zeile.
Aus Komplexitätsgründen wird kein künstlicher Defekt in den normalen Mini-Eval
eingebaut. Der fehlende reale Isolationsnachweis bleibt damit ein bewusst
akzeptiertes Restrisiko und kein Final-Run-Gate; der Vertrag ist durch die
fokussierte Offline-Acceptance belegt. Tritt im Mini- oder Final Run natürlich
ein entsprechender Native-Preflight- oder technischer Quality-/Contractfehler
auf, muss geprüft werden, dass unabhängige Zeilen weiterlaufen. Falls später
eine vollständige Hardware-Closure verlangt wird, genügt dafür ein einzelner
enger separater Smoke, keine neue Toolversion.

| Auslöser | Gezielte Reaktion |
|---|---|
| natürlicher modellbezogener Native-Preflight- oder technischer Quality-/Contractfehler im direkten non-variant Pfad | prüfen, dass nur die betroffene Zeile blockiert ist und gültige unabhängige Zeilen weiterlaufen |
| Hailo-10-Full-Chain fällt trotz bestätigtem UINT8-Part1 deutlich zurück | P2-, FIFO-, Handoff- und Quantize/Dequantize-Telemetrie prüfen; keine neue InferModel-Parallelität ohne neuen Auftrag |
| DeepX Mapping/Copy > ungefähr 10 % oder Pipelineeffizienz deutlich < 90 % | zuerst Buffer-Pool, danach gegebenenfalls Async/Batch prüfen |
| vor v2.79.15 mit Scale-only gebauter DeepX-Classification-Split | nur betroffene Zeilen neu bauen und messen |
| materieller reproduzierbarer Quality-Verlust | konkrete Backend-/Modellzeile untersuchen, kein pauschaler Quality-Sweep |
| valide MobileNet-/RegNet-Single-Tensor-Fälle werden vom Native-Planer nicht erzeugt | kleinen Planner-/Contract-Fix ergänzen oder ausdrücklich Native-unsupported berichten |
| Dissertation beansprucht praktisch ausgeführten Multi-Tensor-Fall, Resultpack enthält keinen | einen kurzen repräsentativen Generic-Fall ergänzen |
| YOLOv7-/YOLO11-Zeile fehlt oder ist ungültig | nur den fehlenden Ziellauf nachholen |
| Energy-CV/Drift auffällig | ein bis zwei zusätzliche Wiederholungen nur dieser Zeile |
| Energy ist angefordert, aber null Messungen starten | expliziten Nichtstartgrund, Planpfad und globale versus modelllokale Ursache prüfen |
| registrierte Ergebnis-CSV fehlt bei der Finalisierung | Cleanup-/Artifact-Index-Zuordnung eng korrigieren und nur Mini-Eval wiederholen |
| ein Hardware-Smoke schlägt fehl | enger Fix und nur betroffenen Smoke beziehungsweise betroffene Zeilen wiederholen |

Hinweis: Der aktuelle Runtime-Contract erzeugt automatisch vor allem ResNet-
und YOLO-Verträge. MobileNet/RegNet werden erst nach Sichtung realer
Single-Tensor-Kandidaten zu einem Fixpunkt; das ist kein pauschaler
Releaseblocker.

## 12.4 Optional, kein Final-Run-Blocker

- finale Accuracy-Tabelle mit 5.000 Bildern und 5.000 Bootstraps, falls die
  Dissertation sie benötigt;
- Ausgabe der maximalen acceleratorassoziierten Full-System-Aktivleistung und
  ihres Deltas zur Idle-Baseline;
- weitere Peak-/P99-Ausgaben aus vorhandenen Rohtraces;
- zusätzliche Generic↔Native-Paare aus Forschungsinteresse;
- Wartungsbereinigung alter Test-/Statusdokumentation nach der Kampagne.

## 12.5 Aus dem Scope gestrichen

- neue Messwert-Hash-, Signatur-, Seal- oder Versiegelungsartefakte;
- weitere Kalibrierungsrunden ohne konkreten Fehler, nachdem der einmalige
  v2.79.16-FS-Gain und die zwingend danach neue M.2-Idle-Baseline je Setup
  erfolgreich aufgenommen wurden;
- nachträgliche Umbenennung echter historischer MB-Messungen in FS;
- breiter neuer Generic-vs-Native-Performance- oder Korrelationslauf;
- Zwang zu drei gemeinsamen Splits je Modell;
- serielle Mehrfachsplitpunkte;
- Native-Unterstützung für Multi-Tensor-Grenzen;
- präventive Hailo-/DeepX-Runnerrewrites;
- zusätzliche parallele InferModel-Jobs;
- pauschal höhere Compiler-Qualitystufen;
- unbeabsichtigte Generic-Energy-Messung; ausdrücklich gewählte Generic Energy
  bleibt dagegen als kombinierter Pfad oder sichtbarer Planungsblocker zulässig;
- vollständige Kampagnenwiederholung wegen einzelner Fehler.

---

# 13. Finalprofil und Final-Run-Abnahme

## 13.1 Effektive Startkonfiguration

Vor dem Start wird nicht nur der Profilname, sondern die **aufgelöste effektive
Konfiguration** geprüft:

```text
tool_version                                = 2.79.16
execution_preset.overrides.native_enabled   = true
native_producers.enabled                    = true
native full baselines                       = true für die vorgesehenen Backends
common single-tensor cases                  = bis zu 3 real vorhandene Fälle je Modell
screening cap 1                             = nicht unverändert übernehmen
execution_preset.overrides.energy_enabled   = true
energy.requested_native_energy              = true
native_producers.energy.enabled             = true
native_producers.energy.mode                = measure
native_producers.energy.duration_s          = 60
energy measurement repeats                 = 3
energy.measurement_path                     = native_only nur bei bewusster Native-only-Auswahl
physical_scope                              = FS
window_label                                = command
energy.enabled / energy.generic_enabled     = false / false
full_system_current_scale_verified          = true je Setup
m2_idle_baseline                            = nach FS-Gain neu aufgenommen
hailo10 native split I/O                    = HEF-native UINT8 / UINT8
hailo10 profile inflight                    = bestehender Wert 8 unverändert
hailo10 HEF diagnostic smoke inflight       = 1
hailo10 zusätzliche Jobgruppen              = keine
deepx classification prep                   = imagenet_mean_std
hailo preset / opt / B                      = balanced / 1 / 500
deepx method / opt / B                      = ema / 0 / 500
```

Das scheinbare `energy.enabled = false` ist dabei beabsichtigt: Dieser
Top-Level-Schlüssel steht für Generic Energy. Die eigentliche Kampagnenmessung
wird über `native_producers.energy.enabled = true` und
`energy.requested_native_energy = true` aktiviert.
Wenn im konkreten Lauf Generic Energy ausdrücklich ausgewählt wurde, gelten
diese Native-only-Zeilen nicht: Dann muss die effektive Planung den
kombinierten Pfad ausweisen oder sichtbar blockieren.

Zusätzlich prüfen:

- sieben Modelle wie in Abschnitt 2;
- reale, nicht künstlich erzeugte Splitauswahl;
- Native nur für kompatible Single-Tensor-Fälle;
- passende Full-Baselines;
- korrekter Endpoint je Zeile;
- YOLOv7-Qualitätspfad verwendet den vorgesehenen Dequantisierungsvertrag,
  nicht einen ungewollten Cast-only-Claimpfad;
- zu jedem Setup sind verifizierter FS-Gain und die danach neu aufgenommene
  Idle-Kalibrierung zugeordnet;
- nvpmodel und Clock-/Governor-Policy entsprechen dem dokumentierten
  Setupsvertrag;
- das Modellset enthält RegNet und nicht versehentlich YOLO26x.

## 13.2 Abnahme je Ergebniszeile

Messzeilen und Fehler-/Ausschlusszeilen werden nicht vermischt.

### Abgeschlossene Messzeile

Eine abgeschlossene Messzeile ist technisch verwendbar, wenn:

- Modell, Case, Setup, Backend, Richtung und Variante stimmen;
- Build und Runtime für die beanspruchte Messung erfolgreich sind;
- der Endpoint eindeutig ist;
- Work Units positiv und konsistent sind;
- Warmup und Messfenster nicht vermischt wurden;
- Quality-Applicability und Quality-Status eindeutig sind;
- Energy nur dann als gemessen ausgewiesen ist, wenn der richtige Hotloop
  tatsächlich gestartet wurde;
- bei Energy FS/command, ungefähr 60 s und ein vollständiger Trace vorliegen;
- full_system_current_scale_verified=true ist und der Faktor vor einem
  zulässigen Baseline-Abzug angewendet wurde;
- keine unzulässige Idle-Korrektur angewandt wurde;
- Wiederholungen vollständig sind oder die Abweichung dokumentiert ist.

Kann eine physisch ausgeführte Zeile trotz eines technischen Quality-Problems
Rohenergie liefern, bleibt diese sichtbar, aber mit
energy_quality_qualified=false,
energy_quality_status=raw_energy_quality_not_qualified und
native_energy_after_technical_error=collect_raw_quality_unqualified. Sie ist
damit keine quality-qualifizierte Vergleichszeile.

### Fehler- oder Ausschlusszeile

Eine fehlgeschlagene oder ausgeschlossene Zeile ist kein verwertbarer
Messwert. Sie ist dennoch vollständig dokumentiert, wenn:

- ein ehrlicher Terminalstatus und konkreter Grund vorliegen;
- keine künstlichen FPS-, Leistungs- oder Energiewerte erzeugt werden;
- bei angeforderter, aber nicht gestarteter Energy ein konkreter
  energy_not_started_reason vorliegt;
- ein modellbezogener Native-Preflight- oder technischer Quality-/Contractfehler
  im direkten non-variant Pfad keine unabhängigen Zeilen blockiert.

Aus diesem belegten Vertrag wird keine pauschale Zeilenlokalität beliebiger
Runtime- oder Workloadfehler abgeleitet.

## 13.3 Abnahme des Resultpacks

Die Kampagne ist auswertbar, wenn:

1. jeder geplante Pfad einen ehrlichen Terminalzustand besitzt;
2. Full-, Generic- und Native-Zeilen nicht verwechselt werden;
3. Multi-Tensor-Fälle nur Generic zugeordnet sind;
4. gemeinsame Generic↔Native-Fälle exakt dieselbe Boundary verwenden;
5. Performance, Quality und Energy getrennt, aber eindeutig gebunden sind;
6. historische Fixtures nicht als v2.79.16-Hardwaremessung ausgegeben werden;
7. Ausschlüsse, Zeilenblocker und Energy-Nichtstartgründe explizit in der
   Ergebnistabelle stehen;
8. `reports/prediction_vs_benchmark.csv` und
   `reports/validation_summary.csv` nach der Finalisierung physisch vorhanden
   und im Artifact-Index konsistent registriert sind;
9. falls im direkten non-variant Pfad ein modellbezogener Native-Preflight-
   oder technischer Quality-/Contractfehler auftritt, dieser keine
   unabhängigen Modellzeilen global beendet;
10. der Run einen eindeutigen Abschlussstatus besitzt und nicht nach
    erfolgreicher Messarbeit am Legacy-Cleanup scheitert.

Einzelne Quality-Fails oder technisch unsupported Fälle machen die gesamte
Kampagne nicht ungültig. Ungültige Messzeilen werden gezielt wiederholt;
unbequeme, aber gültige Ergebnisse bleiben erhalten.

---

# 14. Reportinganforderungen

## 14.1 Pflichtfelder pro Messzeile

Mindestens menschenlesbar ausgeben:

```text
tool_version
profile_id / run_id
timestamp
model_id
case_id
setup_id
backend
direction
variant: full | generic_split | native_split
precision / runtime precision identity
boundary tensor(s)
measurement_endpoint
repeat index
duration_s / completed_work_units
fps
technical_status
quality_applicability / quality_status
energy_requested / energy_started
energy_not_started_reason
energy_quality_qualified / energy_quality_status
native_energy_after_technical_error
energy_scope / energy_window
full_system_current_scale_verified
full_system_current_scale_applied / full_system_current_scale_factor_applied
avg_power_w / energy_total_j  # kalibrierte FS-Primärwerte
full_system_input_unscaled_avg_power_w
full_system_input_unscaled_energy_total_j
optional_host_normalized_value
exclusion_reason
```

Automatische interne IDs oder Hashes dürfen zusätzlich enthalten sein, sind
aber keine manuell zu pflegende Kampagnenpflicht.

## 14.2 Stage- und Endpointmetriken

Wenn verfügbar:

```text
P1 mean / P50 / P95
P2 mean / P50 / P95
Post mean / P50 / P95
P1→P2 queue wait
P2→Post queue wait
handoff / mapping / copy
p2_output_fps
completed_detection_fps
completed_to_p2_ratio
classification_logits_fps
```

Diese Felder dienen vor allem der Diagnose, ob ein Runner optimiert werden muss.
Fehlt ein Diagnosequantil, ist eine ansonsten vollständige Messzeile nicht
automatisch unbrauchbar.

## 14.3 Geplante zusätzliche Aktivleistungszeile

Als zusätzliche, interessante Systemmetrik soll aus dem vorhandenen
Full-System-Trace ausgegeben werden:

```text
full_system_active_power_max_w
full_system_active_power_delta_vs_idle_w
```

Der erste Wert ist die maximale beobachtete, mit dem verifizierten FS-Faktor
kalibrierte Full-System-Eingangsleistung im aktiven Messfenster. Der zweite
Wert ist ihr Delta zur setupbezogenen, in derselben Skalendomäne aufgenommenen
Full-System-Idle-Baseline. Beide Größen umfassen neben dem M.2-Accelerator auch
Lastfolgen in Jetson-CPU, RAM, PCIe, Spannungswandlung und sonstiger
Peripherie. Das ist eine faire und interessante Systembetrachtung, darf aber
nicht als isolierte maximale M.2-Device-Leistung bezeichnet werden.

Diese Ausgabe ist eingeplant, aber noch kein implementierter oder
freigabeblockierender v2.79.16-Pflichtwert. Rohtrace, Messfenster, Peak-
Definition und Aggregation müssen bei einer späteren Ergänzung sichtbar
bleiben.

## 14.4 Aggregation

- keine Best-of-Auswahl einzelner Wiederholungen;
- Median beziehungsweise vorab festgelegte Aggregation verwenden;
- Streuung/CV sichtbar machen;
- 1–2 zusätzliche Wiederholungen nur bei auffälliger Zeile;
- Mirror- oder Companion-Zeilen nicht als zusätzliche unabhängige Messungen
  zählen;
- Quality-only-Companions getrennt von Performance-Sollidentitäten zählen.

---

# 15. Stop-, No-Go- und Risikoregeln

## 15.1 Materielle Stop- und Ausschlussgründe

- die effektive Konfiguration nicht der beabsichtigten Messung entspricht;
- Modell, Case, Setup, Backend oder Endpoint falsch gebunden ist;
- der Energy-Collector oder eine globale Infrastrukturkomponente nicht
  initialisiert werden kann;
- ein modellbezogener Native-Preflight- oder technischer Quality-/Contract-
  Fehler im direkten non-variant Pfad auftritt; dann wird nur diese Zeile
  nach dem belegten Closure-Vertrag ausgeschlossen;
- Completed Work Units fehlen oder nicht zum Hotloop gehören;
- das Energy-Fenster nicht `FS`/`command` ist;
- Energy angefordert war, aber weder eine Messung noch ein konkreter
  Nichtstartgrund vorliegt;
- der setupbezogene Full-System-Faktor nicht verifiziert ist oder die
  M.2-Idle-Baseline noch aus der alten Skalendomäne stammt;
- relevante Samples fehlen oder der Trace das Fenster nicht abdeckt;
- eine falsche Idle-Korrektur verwendet wird;
- ein unbekannter Outputvertrag heuristisch statt fail-closed verarbeitet wird;
- Warmup, Build, Quality-Oracle oder Evidenzaufbau im Performancefenster landen;
- registrierte Pflichtreports nach der Finalisierung fehlen.

Global bleiben nur echte globale Ursachen wie u.RECS-/SSH-/Authfehler,
ungültige globale Konfiguration, Plattform-Lock oder nicht initialisierbarer
Collector. Zeilenlokalität ist für modellbezogene Native-Preflight- und
technische Quality-/Contractprobleme im direkten non-variant Pfad belegt;
beliebige Runtime- oder Workloadfehler werden daraus nicht pauschal abgeleitet.

Ein Lauf wird **nicht** allein wegen eines fehlenden zusätzlichen Hilfs-Hashes,
Seals oder einer nicht gebauten neuen Versiegelungsschicht verworfen.

## 15.2 Nach Öffnung der Resultate nicht tun

- Qualitystufe wechseln, um einen FAIL zu verbessern;
- Splitpunkte künstlich ergänzen oder austauschen, um eine gewünschte Zahl zu
  erreichen;
- unerwünschte, aber gültige Zeilen entfernen;
- Endpoint oder Scope nachträglich umetikettieren;
- historische Ergebnisse als aktuelle Releaseevidenz deklarieren;
- die komplette Kampagne wiederholen, wenn nur einzelne Zeilen betroffen sind.

## 15.3 Technische Risiken

**TensorRT-Portabilität:** Engine und Setup müssen zusammenpassen. GPU-Modell,
Compute Capability, TensorRT-/CUDA-/Treiberstand, Graph, Boundary und Precision
sind bei Wiederverwendung zu kontrollieren.

**Hailo-10H-Umgebung:** Vendor-Stack von inkompatiblen User-Site-Paketen
isolieren; etablierte Umgebung verwenden:

```bash
export PYTHONNOUSERSITE=1
source ~/venvs/hailo10/bin/activate
```

**Outputreihenfolge:** Detection-Heads über Rolle, Shape, Geometrie und Vertrag
binden, nicht über Dateiname oder zufällige Runtime-Reihenfolge.

**MobileNet/RegNet Native:** Erst reale Kandidaten prüfen. Fehlende automatische
Runtime-Verträge sind gegebenenfalls ein kleiner Planerfall oder ein ehrlicher
Native-Ausschluss, kein Grund für eine breite Toolrunde.

**Power-Mode-Vergleich:** Der historische niedrige DeepX-Idlewert darf erst
nach Abgleich von nvpmodel, Clock-/Governor-Policy, Temperatur und Peripherie
interpretiert werden.

**Bereinigte Remote-Artefakte:** Alte Pfade in Cache- oder Smoke-Kommandos sind
keine dauerhafte Fixture-Garantie. Ein fehlendes altes BenchmarkSet belegt
keinen aktuellen Runnerfehler; der reguläre Mini-Eval muss seine Artefakte
neu und vollständig erzeugen.

---

# 16. Empfohlene Thesisformulierungen

## 16.1 Runnerrollen und Multi-Tensor

> Der Generic Runner untersucht einzelne ONNX-Splitpunkte einschließlich
> Multi-Tensor-Boundaries. Der Native Runner misst die hardwarekompatible
> Single-Tensor-Schnittmenge und ist für Performance- und Energiemessungen
> maßgeblich. Mehrere serielle Splitstellen sind nicht Gegenstand der
> Kampagne.

## 16.2 Fairness

> Die Backends verwenden dieselbe wissenschaftliche Messrolle, dieselben
> Endpunkt- und Datenverträge sowie dieselbe Wiederholungspolicy, dürfen aber
> ihre jeweiligen Runtimeprimitive effizient nutzen. Fairness bedeutet daher
> vergleichbare Messbedingungen und einen realistischen Steady State, nicht
> identischen Low-Level-Code oder gleiche absolute FPS.

## 16.3 Generic als Screening-Proxy

> Auf der historisch geprüften technisch kompatiblen Single-Tensor-
> Schnittmenge bewahrte Generic die Native-Rangordnung hinreichend gut. Generic
> wird deshalb als skalierbarer Screening-Proxy verwendet. Diese Aussage wird
> nicht auf Multi-Tensor-Splits oder deren Native-Ausführbarkeit extrapoliert.

## 16.4 Three-Stage

> Die getrennte Instrumentierung von P1, P2 und Postprocessing zeigt, ob der
> Durchsatz vom ersten Accelerator, vom TensorRT-Tail, vom Handoff oder von der
> Aufgabenvervollständigung begrenzt wird. Der Pipelinezyklus folgt dem
> langsamsten Serviceabschnitt; Queuezeiten zeigen zusätzliche Backpressure.

## 16.5 Quality und Performance

> Performance und Quality sind an dieselben Artefakte und Contracts gebunden,
> werden aber nicht im selben Timingfenster ausgeführt. So bleibt die
> semantische Absicherung erhalten, ohne den Hotloop durch Referenzdecoder,
> große Output-Hashes oder Evidenzaufbau zu verfälschen.

## 16.6 Energy

> Die primäre Energiegröße ist die mit dem verifizierten Setupfaktor
> kalibrierte Full-System-Gesamtenergie desselben Native-Hotloops vor einem
> optionalen Idle-Abzug. Die ursprünglichen unskalierten u.RECS-Werte bleiben
> separat erhalten. Der setupbezogene M.2-Idle-Abzug wird ausschließlich als
> zusätzliche TensorRT-Full-Normalisierung ausgewiesen. Physische Erfassung
> und Freigabe für einen quality-qualifizierten Vergleich bleiben getrennt.

## 16.7 Acceleratorassoziierte maximale Systemleistung

> Die maximale Aktivleistung wird als Full-System-Wert und optional als Delta
> zur setupbezogenen Idle-Baseline berichtet. Sie umfasst neben dem
> Accelerator auch hostseitige CPU-, RAM-, PCIe- und Wandlungsanteile und ist
> deshalb eine System-, nicht eine isolierte M.2-Rail-Messung.

## 16.8 YOLOv7-Learning

> Der korrekte YOLOv7-`b066`-Split reproduzierte historisch ungefähr den
> Paperdurchsatz. Der zwischenzeitliche Einbruch auf rund 16 FPS entstand durch
> einen anderen, evidenzlastigen Completed-Task-Hotloop. Der contractgebundene
> Sparse-Decode und die getrennte Poststufe stellten bei vollständiger Parität
> ungefähr 95,9 Completed-Detection-FPS wieder her.

---

# 17. Maßgebliche aktuelle Artefakte

| Artefakt | Rolle |
|---|---|
| `ONNX-Splitpoint-Tool_v2.79.16_COMPLETE_DELIVERY_BUNDLE_UPDATED.zip` | installierte aktuelle Lieferung mit den drei Closure-Punkten |
| `ONNX-Splitpoint-Tool_v2.79.16_COMPLETE_DELIVERY_BUNDLE(2).zip` | ältere Pre-Closure-Basis mit 260 Tests; nicht mit dem installierten UPDATED-Paket verwechseln |
| `ONNX-Splitpoint-Tool_v2.79.16_SOURCE.zip` | im Bundle enthaltene aktuelle Source-Distribution |
| `AUDIT_SUMMARY.md` und `ONNX-Splitpoint-Tool_v2.79.16_FINAL_VERIFICATION.json` | fokussierte Acceptance 468/468 und maschinenlesbare Softwaregrenzen |
| `TESTANLEITUNG_2.79.16.md` | Installations-, Kalibrierungs- und Smoke-Anleitung |
| `complete_set_7models_v27916_b500_audit20.yaml` | Generic-Screening-/Auswahlprofil, nicht unverändert als Finalprofil verwenden |
| `hailo10_input_format_ab_20260903_131242.json` | Hailo-10 FLOAT32↔UINT8-Input-A/B |
| `/home/nx/v27916_hailo10_uint8_hef_smoke/report.json` | realer v2.79.16-Hailo-10-Part1-UINT8-Smoke auf dem Zielsystem |
| `tests/test_v279_native_three_stage.py` und `tests/test_v2791_concurrent_three_stage_normal_runner.py` | aktuell ausgeführter 14/14-Paper-Split-Offline-Test |
| `biggerset_20260903_090110_debug_pack.zip` | Diagnosefixture für globalen Preflight-Abbruch, fehlende Energie und Finalizerproblem |
| `m2_idle_power_calibration_deepx.json` | historische DeepX-Idle-Plausibilität vor dem neuen FS-Gain |
| `m2_idle_power_calibration_Hailo8.json` | historische Hailo-8-Idle-Plausibilität vor dem neuen FS-Gain |
| `m2_idle_power_calibration_hailo10.json` | historische Hailo-10H-Idle-Plausibilität vor dem neuen FS-Gain |
| `tests/fixtures/v2793/yolov7_b066_three_stage_report.json` | archivierter enger YOLOv7-Three-Stage-Hardwarebeleg |
| `tests/test_v276_cross_runner_reporting.py` und `onnx_splitpoint_tool/workflow/cross_runner_reporting.py` | Generic↔Native-Brückenbeleg und Vergleichsvertrag |
| diese Knowledge Base | aktuelle verbindliche Arbeits- und Methodenreferenz |

Das aktuelle UPDATED-Bundle besitzt lokal den SHA-256-Wert
`2790932b717e8dbea312c1c0a081ed47ba52aaad8c770657b3365f823a1b713c`.
Das eingebettete Source-ZIP besitzt
`2f0b2ee8432a2cde1db59326967acdc6fd51fa7339490739d9cb74b9f948e375`.
Das ältere hochgeladene `(2)`-Basisbundle besitzt dagegen
`f0ceedc927dece32e28feb5d112dfeef4dc506765b5c670af9941c04941420e8`;
sein eingebettetes Pre-Closure-Source-ZIP besitzt
`cae8e8074f8ef76cfe077616d063c1978ae61319d09226512edbe35cb4296863`.
Diese vorhandenen Paketidentitäten werden nur dokumentiert; daraus entsteht
keine neue Messwert- oder Bediener-Hashpflicht.

Ältere v2.79.2–v2.79.15-Debugpakete bleiben gegebenenfalls Archivmaterial,
sind aber keine aktuellen Arbeitsanweisungen.

---

# 18. Kompakte Release- und Entscheidungsfolge

| Stand | Dauerhaft relevante Aussage |
|---|---|
| v2.77.1 | historischer Generic↔Native-Methodenbeleg mit 24/24 technischen Paaren |
| v2.78.4 | Sieben-Modell-B500-Langlauf als wertvolle, aber unvollständige Legacy-Fixture |
| v2.79-Linie | Native Three-Stage, contractgebundene Adapter und korrekte Endpointtrennung wiederhergestellt |
| v2.79.14 | bewusst einfache direkte FS-Off/On-Idle-Kalibrierung pro Setup |
| v2.79.15 | FS-/command-Defaults und enge MB-Migration; DeepX Classification Part1 Mean/Std korrigiert; Software-PASS |
| v2.79.16 UPDATED | Hailo-10 Native Split mit HEF-nativem UINT8-I/O; Soll-/Ist-Strom in der FS-Kalibrierung; modelllokale Native-Preflight-/Quality-/Contract-Isolation im direkten non-variant Pfad; fokussierte Acceptance 468/468, reale Installation und Hailo-10-Part1-Smoke PASS |

Die detaillierten Zwischenpatch- und Fehlerchroniken sind nicht mehr Teil der
aktiven Knowledge Base. Bei Bedarf liegen sie in den alten Audit- und
Releaseartefakten.

---

# 19. Aktueller Übergabestand

```text
Aktuelle Version:       2.79.16 UPDATED
Build-ID:               v2.79.16-guided-full-system-input-calibration
Releaseurteil:          INSTALLATION_PASS_TARGETED_SMOKES_PASS_CALIBRATION_AND_E2E_PENDING
Installation:           Smartmirror2 PASS; fokussierte Acceptance 468/468
Paper:                  14/14 offline PASS; Hardwaredurchsatz historisch
Hailo-10:               HEF-Part1 UINT8 20/20 PASS; Full Chain offen
Kalibrierung:           FS-Gain real offen; danach neue M.2-Idle-Baselines
Energy:                 FS / command; Native-only nur bei bewusster Auswahl
Quality:                Hailo balanced/Opt1/B500; DeepX EMA/Opt0/B500/Mean-Std
Scope:                  Generic Single+Multi-Tensor; Native Single-Tensor
Fehlerisolation:        Native-Preflight/Quality/Contract, direct non-variant, offline PASS
Akzeptiertes Restrisiko: separater Hardware-Smoke mit künstlich ungültiger Zeile nicht als Pflichtgate
Nicht vorgesehen:       neue Hash-/Seal-Ketten, neue InferModel-Parallelität, serielle Multi-Splits
Nächster Schritt:       G0–G6 aus Abschnitt 12; genau ein Mini-Eval, dann großer Run
```

---

# 20. Änderungsprotokoll dieser Knowledge Base

## 3. September 2026 – Aktualisierung auf v2.79.16 UPDATED

- aktuelle Version und Build-ID auf v2.79.16 fortgeschrieben;
- reale Installation mit INSTALL_ACCEPTANCE=PASS und FINAL_STAGE=complete
  dokumentiert;
- 468/468 fokussierte Acceptance-Tests, 14/14 Paper-Offline-Tests und den
  realen Hailo-10H-UINT8-Part1-Smoke mit 20/20 Inferences aufgenommen;
- Hailo-10-FLOAT32↔UINT8-A/B einschließlich exakter Outputparität und
  ungefähr 3,885-fachem Part1-Vorteil dokumentiert;
- klargestellt, dass v2.79.16 keine zusätzliche InferModel-Jobgruppe einführt
  und die bestehende Inflight-Konfiguration sowie P1/FIFO/P2-Struktur erhält;
- tatsächliche vierstellige Lastströme, Sollstrom-Evidenz, kontrollierten
  Abbruch und die drei unveränderten Idle-Phasen der FS-Kalibrierung
  dokumentiert;
- alte M.2-Idle-Werte zur historischen Plausibilität herabgestuft und ihre
  zwingende Neuaufnahme nach gespeichertem FS-Gain festgehalten;
- direkten, non-variant zeilenlokalen Energy-Fehlervertrag,
  Raw-unqualified-Status und konkrete Nichtstartdiagnose integriert;
- Generic-Composed-Feldweitergabe als Wiederverwendung eines vorhandenen
  Contractwerts statt neuer Hashbildung eingeordnet;
- Biggerset-Lauf als Diagnosefixture aufgenommen: YOLO26x statt RegNet, neun
  technische Quality-Befunde, null Energy nach globalem YOLOv7-Preflight und
  fehlende registrierte Reports nach Legacy-Cleanup;
- veralteten v2.79.15-Installations- und Inflight-Sweep-Gateplan ersetzt;
- genau einen Mini-Eval vor dem großen Lauf sowie Power-Mode-Abgleich,
  vollständige Hailo-10-Kette, positive Energy, Scale-Bindung und
  Finalizer-/CSV-Prüfung als verbleibende Gates festgelegt;
- Power-Mode-Festlegung vor die neue M.2-Idle-Baseline gezogen und den
  absichtlich fehlerhaften Mehrmodell-Hardware-Smoke als bewusst akzeptiertes
  Restrisiko statt widersprüchliches Pflichtgate eingeordnet;
- kalibrierte FS-Gesamtenergie als Primärwert und die separat erhaltenen
  `full_system_input_unscaled_*`-Felder eindeutig unterschieden;
- altes Pre-Closure-Bundle `(2)` und maßgebliches installiertes UPDATED-Bundle
  ausdrücklich getrennt;
- maximale acceleratorassoziierte Full-System-Aktivleistung als geplante
  zusätzliche Systemmetrik aufgenommen, ausdrücklich nicht als reine
  M.2-Rail-Leistung;
- keine neue manuelle Hash-, Seal-, Signatur- oder Versiegelungspflicht
  eingeführt.

## 3. September 2026 – konsolidierte v2.79.15-Fassung

- Kopfstand und Audit auf v2.79.15 aktualisiert;
- vollständigen Fragenkatalog als Abschnitt 3 integriert und beantwortet;
- pragmatische Kampagnenprämisse ohne neue Hash-/Seal-Ketten verankert;
- Energy-Vertrag auf `FS`/`command`, 60 s × 3 und Native only präzisiert;
- drei konkrete Idle-Kalibrierungen mit Messwerten aufgenommen;
- das alte `MB`-Projektionsfeld in den Kalibrierungs-JSONs eingeordnet;
- DeepX Classification Part1-Fix dokumentiert;
- Hailo-/DeepX-Qualitypolicy eingefroren;
- Multi-Split eindeutig als Multi-Tensor an einem Splitpunkt definiert;
- Drei-Split-Zwang entfernt und durch „bis zu drei real vorhandene Fälle“
  ersetzt;
- aktuelle DONE-/MUST-/CONDITIONAL-/OPTIONAL-/OUT-OF-SCOPE-Matrix erstellt;
- geliefertes Sieben-Modell-Profil klar vom noch zu speichernden Finalprofil
  getrennt;
- alte v2.79.2–v2.79.14-Debugchroniken, R1–R8-Arbeitskataloge, doppelte
  Handoffs, erledigte Checklisten und überholte Gates entfernt;
- dauerhafte historische Evidenz kompakt erhalten.
