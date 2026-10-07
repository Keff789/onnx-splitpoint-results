# YOLOv7: Native Completion, Performancekorrektur und Orin-Abgleich

Dokumentationsstand: **07.10.2026**. Dieser Nachtrag ergänzt die eingefrorenen
THESIS20-Ergebnisse; historische Messungen und Auswertungen bleiben erhalten.
Die neuen Angaben stammen aus dem bereitgestellten Bericht
„YOLOv7: Split-Reparatur und Orin-Abgleich“. Die Übernahme prüft dessen Tabellen
und Rechnungen, **nicht unabhängig die dort referenzierten neuen Rohreports,
Quellen, Telemetrie oder das Review-ZIP**. Der Bericht nennt keinen absoluten
Messzeitstempel; das Dokumentationsdatum ersetzt diesen nicht.

Bericht-SHA256:
`2ae5446d5114ea647a21ed2804ebb6ec28caab829952c58d4e045a5f49de23e5`.
[Datennachtrag und Provenienz](../results/evaluation/yolov7_native_completion_20261007/README.md).

## Ursache und Korrektur laut Bericht

Die langsamen H10-/DeepX-Splits verwendeten noch dichten CPU-Decode und
wiederholte Payload-/Quellprüfungen im seriellen Consumer-Tail. Der reparierte
Worktree verbindet attestierte YOLOv7-Rawhead-Verträge mit dem vorhandenen
Fast-Completion-Pfad und dem exakten Sparse-Decoder. Nur neue Module zu kopieren
hätte den zuvor implizit ausgewählten Strict-Pfad nicht umgestellt.

Im kontrollierten kurzen **H10-b066-Diagnosevergleich** sinkt der CPU-Abschluss
von **63.599 auf 6.614 ms/Bild (9.62×)**. Im Original entfallen 48.802 ms auf
dichtes Decoding und 7.829 ms auf den Payloadhash. Das instrumentierte gesamte
Taskfenster sinkt von 73.531 auf 19.073 ms/Bild (3.86×). Danach begrenzt der
beobachtete Producerzyklus von 18.919 ms die Pipeline; die serielle Consumerarbeit
beträgt 15.973 ms. H10 `inflight=8` betrifft den Prefix und schafft keinen
zusätzlichen Overlap innerhalb dieses Consumer-Tails. Die Submissionlatenz ist
keine isolierte NPU-Ausführungszeit. Diagnosen werden nicht als Final-FPS ausgegeben.

DeepX verwendet laut gebundener Runnerprüfung einen synchronen `engine.run()`/
`Run`-Aufruf mit eigener zusammenhängender Boundary-Kopie. Die frühere Vermutung
eines Python-Output-Pollingloops trifft auf diesen Runner nicht zu. Internes
SDK-Scheduling bleibt unbekannt. H8-b009/b044 verwenden Python-VStreams-Pfade;
H8-b066 überlappt drei Stufen. Ausgeführte Arbeit und Scheduling erklären den
Vergleich; eine allgemeine Überlegenheit von C++ gegenüber Python folgt nicht.

## Finale berichtete Performance

**Neun Splitkonfigurationen sind neu gemessen:** je drei getrennte Prozesse,
100 vollständig abgearbeitete Warmups und 1.000 fertige Tasks, einschließlich
Drain bis zum letzten Abschluss. Keine Stage-Instrumentierung in diesen
Finalrepeats; begleitende Telemetrie etwa 1 Hz. Die sechs optimierten Fulls mit
18 Repeats werden aus dem vorherigen Performanceauftrag wiederverwendet.
Drei zusätzliche aktuelle TRT-Full-Kontrollen bleiben separat und werden
nicht in die bisherigen Dreiermediane eingemischt.

| Setup | TRT Full FPS | Accelerator Full FPS | Split b009 FPS | Split b044 FPS | Split b066 FPS |
|---|---:|---:|---:|---:|---:|
| H8 | 51.781526 | 31.477269 | 42.851710 | 47.800201 | 112.492794 |
| H10 | 51.480597 | 12.314299 | 51.357901 | 64.500526 | 53.350448 |
| DeepX | 47.319602 | 22.945769 | 33.866133 | 48.790077 | 30.594221 |

Alle Werte sind Mediane der berichteten drei Repeats. Alle neun neuen Splits
tragen im Bericht `reference_close`. H8-/H10-Accelerator-Full behalten
`accuracy_loss`; die übrigen vier Fulls tragen `reference_close`. Eine neue
Qualitätskampagne oder unabhängige Prüfung dieser Labels wird hier nicht behauptet.

Die schnellste technisch vergleichbare Full-Alternative wird **vor** einer
Qualitätsfilterung bestimmt; hier ist dies auf allen drei Setups TRT Full.
Vier von neun Splitmedianen liegen darüber: H8-b066 **2.172450×**, H10-b044
**1.252909×**, H10-b066 **1.036321×** und DeepX-b044 **1.031075×**. Kleine
Quotienten über eins belegen keine statistisch gesicherte Überlegenheit.

Die TRT-Kontrollen weichen vom jeweils weiterverwendeten Median um −0.050 %,
−0.258 % und +0.254 % ab. Das stützt laut Bericht die begrenzte beobachtete
Stabilität; es sind keine sechs neuen Full-Abnahmen und keine Garantie identischer
Betriebszustände zu jedem Zeitpunkt. Die lokale Übernahme bestätigt rechnerisch
alle 15 Mediane, 18 Split/Full-Quotienten und neun historischen Quotienten unter
Berücksichtigung der sechs gedruckten Nachkommastellen.

## H8-Regression und endliche Paritätsevidenz

H8-b009 sinkt gegenüber seinem historischen Median um **9.40 %**, H8-b044 um
**10.59 %** und H8-b066 um 1.02 %. Diese Regressionen bleiben sichtbar. Die
historischen Wiederholungen liefen mit drei Runtimeinstanzen in einem Prozess;
die neue Kohorte verwendet drei Prozesse. Ihre Quotienten sind daher keine
vollständig kontrollierten historischen Kausaleffekte.

Bei b044 misst die kurze neue Diagnose zwei vollständige Finitprüfungen mit
zusammen **1.842 ms/Bild**. Ein NaN-/Inf-Loch in früh verworfenen Zeilen wurde
geschlossen; die doppelte Prüfung bleibt in der gemessenen Version bestehen.
Ohne gleich instrumentierten alten b044-Lauf wird nicht die gesamte Regression
dieser Guardarbeit zugerechnet. Eine spätere Zusammenführung der Prüfungen wäre
eine weitere Runtimeänderung mit eigenen Messwerten.

Der Bericht nennt fünf repräsentative Rawsets mit exakter Strict/Bound-dense/
Fast-Parität sowie unabhängigen Strict-Replay der 27 finalen Split-Sentinels.
Die Full-Sentinels bleiben erhalten. Das belegt im berichteten Umfang endliche
Ausgabeparität, keinen neuen COCO-Test und keine Bytegleichheitsprüfung jedes
Frames. Nicht disjunkte Testläufe werden nicht zu einer Gesamtsumme addiert;
drei NumPy-2-spezifische Tests wurden in der lokalen NumPy-1.26-Umgebung explizit
ausgelassen. Ein vollständig grüner Gesamttestlauf wird nicht behauptet.

**Korrektur der früheren H8-Quellenannahme:** Laut neuem Bericht bindet der
erfolgreiche historische H8-b066-Commandcontract `artifacts.native_three_stage`
ausdrücklich an
`453e6bff8ba5d7635614cc3eb3e56fcf53230b68857af4891384bbfbbb3ea7fa`.
Eine pauschal fehlende Bindung dieses konkreten Helpers ist daher nicht mehr
die Arbeitsannahme. Das gilt weder automatisch für b009/b044 noch als
unabhängiger Hashnachweis durch diesen Dokumentationsnachtrag.

## Orin-Konfiguration und verbleibender Full-Abstand

Laut Bericht stimmen Orin NX 16GB, L4T 36.4.7, Kernel und aktive
`MAXN_SUPER`-Definition überein. Die erfassten Lastsamples zeigen CPU 1984 MHz,
GPU 1173 MHz und OC-Zählerdeltas null. Das widerlegt die einfache Annahme eines
sichtbar abweichenden Leistungsmodus, garantiert bei 1 Hz aber keinen lückenlosen
Takt- oder Throttlingverlauf. **EMC bleibt ungemessen.** Unterschiedliche
konfigurierte Lüfterprofile sind kein bewiesener Geschwindigkeitsgrund.

DeepX liegt in den aktuellen TRT-Kontrollen 7.61 % unter H10, entsprechend
1.604 ms mehr pro fertigem Task. Gleiche ONNX-/Buildoptionen und unterschiedliche
Enginebytes lösen die Ursache nicht auf; interne Tactics, Layerplatzierung,
Timingcache und Buildzeitpunkt-Takte fehlen. Die separate Python-Loaderprobe
zeigt unterschiedliche CUDART-Versionen, ist jedoch keine rückwirkende
Beobachtung aller Messprozesse oder des H8-C++-SO. H8 und DeepX teilen dort
die CUDART-Version trotz unterschiedlicher FPS. Eine einzelne Ursache des
Full-Abstands ist damit weiterhin nicht belegt.

## Energie, Nutzung und übertragbare Arbeitsregeln

**Für alle 15 aktuellen Varianten ist Energie `not_measured`/NA.** Alte Joulewerte
gehören zu ihren historischen Implementierungen und dürfen nicht mit den neuen
FPS als gemeinsamer Betriebspunkt exportiert werden. Kein Energiegewinn wird
aus dem Durchsatz abgeleitet. Der separate historische H8-Vorherstand bleibt
bei zwei gültigen Repeats, fünf Starts und drei Transportfehlern; die neue
Performancearbeit hat laut Bericht weder Energie gestartet noch Budgets geändert.

Die regulären Startpfade des korrigierten Worktrees wählen den Fix laut Bericht
bereits. Hardwareabnahme erfolgte in isolierten Candidate-Runtimes; ein globaler
Rollout in installierte gemeinsame Gerätestände und eine allgemeine GUI-Abnahme
sind damit nicht erledigt. Dieser Ergebnisrepo-Nachtrag ist kein Toolrelease.

Für die Prüfung nativer Pfade ergeben sich folgende Arbeitsregeln, keine
pauschalen Leistungsbefunde für andere Modelle:

- Den tatsächlich ausgewählten Modus und importierten Code prüfen. Eine vorhandene
  Optimierung oder ein neuer Dateihash belegt nicht deren Verwendung.
- End-to-end bis zur echten Completion messen. Backend-FPS, asynchrones Enqueue
  und konfiguriertes `inflight` ersetzen keinen Overlap- oder Abschlussnachweis.
- Pipelinearbeit nach Stufen profilieren; überlappende, inklusive und exklusive
  Intervalle nicht doppelt addieren. Historische und neue Kohorten explizit trennen.
- Prüfarbeitskosten gezielt verlagern, ohne Finitprüfung, NMS, Pufferownership,
  Taskdefinition oder ehrliche Sentinelkennzeichnung abzuschwächen.
- Negative Resultate und Regressionen erhalten. Energie bleibt an dieselbe
  Implementierung und denselben Betriebszustand gebunden wie der Vergleich.

Andere Modellfamilien bleiben laut berichteter statischer Scopeprüfung strict;
Klassifikation ist separat. Der YOLOv7-Befund begründet weder einen allgemeinen
H10-/DeepX-Hardwarebefund noch eine erneute Gesamtmesskampagne.
