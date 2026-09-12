# Hailo8: vorhandene HAR-Zwischenstände vergleichen und Ergebnisse ins Git sichern

**Eigenständiger Diagnose-/Sammelstarter, R1 vom 12.09.2026.** Keine Änderung am Tool;
keine Abhängigkeit vom noch gebauten Release 2.80.4. Auf Smartmirror2 ausführen.

## Start

Das Paket nach `~/Downloads` entpacken. Keine parallele Messung, keine Toolinstallation
oder Venv-Änderung; GUI vorher schließen. Ein bestehender Workflow-Lock wird respektiert.

```bash
(
  set -e
  cd "$HOME/Downloads"
  unzip -n Hailo8_HAR_und_Git_R1.zip
  cd Hailo8_HAR_und_Git_R1
  bash ./run.sh --push
)
```

Es wird zuerst tatsächlich die **Inference-Emulation der vorhandenen HARs** versucht.
Anschließend werden die existierenden Nachweise plus neue Berichte gesammelt,
geprüft, angezeigt und nach Eingabe **`PUSH`** committed und gepusht.
Ohne `--push` erfolgen weder Commit noch Push; der kuratierte Nachtrag wird nur kopiert.
Ein fehlgeschlagener/unvollständiger HAR-Versuch wird klar negativ berichtet und darf
als solche Diagnose nach Bestätigung mit den erfolgreichen alten Belegen archiviert
werden. Ein Benutzerabbruch startet hingegen keinen anschließenden automatischen Push.

## Feste Ausgangsdateien

Build:

`~/Downloads/hailo8_mobilenet_gpu_20260912T083456Z_a_10a8wv`

Darin laut originalem Buildergebnis:

- `build/parsed.har`
- `build/quantized.har`

Runtime:

`~/Downloads/hailo8_mobilenet_runtime_8FehkBqO/runtime`

Insbesondere wird `results/runtime_arrays.npz` benötigt (ca. 37 MiB). Diese Rohdatei
liegt absichtlich **nicht** im kleinen `runtime_evidence.zip`. Sie muss im lokalen
Runtimeordner erhalten sein. Fehlende HARs/Arrays führen zu einem verständlichen
Fehlerbericht, niemals zu einem automatischen Neubau oder zu geratenen Ergebnissen.

Der Starter archiviert exakt die bereits ausgewerteten drei Original-ZIPs:

- `~/Downloads/hailo8_gpu_test_20260912T062240Z_hx7b7hcq.zip`
- `~/Downloads/hailo8_mobilenet_gpu_20260912T083456Z_a_10a8wv.zip`
- `~/Downloads/hailo8_mobilenet_runtime_8FehkBqO/runtime_evidence.zip`

Zusätzlich optional: der bekannte `quality_snapshot.zip` im Downloadordner oder unter
`~/Downloads/v2803_quality_snapshot_*/quality_snapshot.zip`. Es werden dessen unveränderte
Qualitätsresultate, 123 Requests, Referenzdiagnosen, Profile und Zusammenfassungen
übernommen, nicht das große repetitive Workflowlog. Ein fehlender Snapshot ist im Index
sichtbar und blockiert die Hailo8-Sammlung nicht. Eine abweichende neuere Messung wird
nicht fälschlich unter diesem historischen Stand einsortiert.

## Tatsächlicher numerischer Test

1. Originaler Buildauftrag, private HEF-Identität und die vorhandene Runtimekette werden
   gegeneinander geprüft. Lokale Berichte müssen den Originalarchivbytes entsprechen.
2. Die bereits erfassten FLOAT32-NHWC-VStreams-Eingaben werden aus dem anhand seines
   vorhandenen Hashes und seiner Größe geprüften Runtime-Dump gelesen. **Keine erneute
   Normalisierung, Quantisierung oder Bildauswahl.** Beide tatsächlichen Feedarrays
   und die beiden logischen Feedarrays müssen übereinstimmen.
3. Original- und Compiler-ONNX werden mit diesen Eingaben lokal in ONNX Runtime auf der
   CPU berechnet: 16 Bilder pro Graph. Ihre Top-k-Ergebnisse und die gespeicherten
   HEF-Top-k-Ergebnisse müssen den bisherigen Fixed16-Bericht reproduzieren.
4. In **separaten Prozessen der unveränderten Hailo8-DFC-Venv**:
   - `parsed.har`: `InferenceContext.SDK_NATIVE`;
   - `quantized.har`: `InferenceContext.SDK_QUANTIZED`.
   Jeweils `ClientRunner(har=..., hw_arch="hailo8")`, dann `runner.infer_context(...)`
   und `runner.infer(...)`. Die API-Signaturen und der Modellkontext werden erfasst;
   fehlt ein erwarteter Kontext, wird nicht still auf eine andere Emulationsart gewechselt.
5. Die vorhandenen GPU-HEF-Hardwareausgaben werden mit der quantisierten Emulation
   verglichen. Zusätzlich entstehen Maximalfehler, RMS, Logit-Cosine, Top-k und eine
   bildweise Übersicht über die verfügbaren Stufen. **Keine neuen HEF-Inferenzen.**

Die Emulation läuft bewusst auf der Management-CPU. Das ist keine neue GPU-Build-
oder Performanceprüfung. Sie benötigt keine neue Hailo8-Overlaykonfiguration und
keinen Jetson. TensorFlow-Threads und CPU-Auswahl werden ausschließlich in den
Diagnosekindprozessen gesetzt, vor dem SDK-Import. Arbeits-/Cache-/Temporärdateien
liegen in einem neuen privaten Diagnoseordner. Die vorhandenen Venvs bleiben erhalten.

### Was nicht aufgerufen wird

Keine `optimize`, `compile`, `translate_*`, `save_har` oder `save_hef`-Methoden;
keine Paketinstallation, keine SSH-Verbindung zum Accelerator, keine Energiemessung,
kein Bootstrap und kein Upload von Modellen/HARs. Der SDK-Interpreter muss dieselbe
DFC-Version melden wie im ursprünglichen HEF-Receipt.

Die bisher gelieferte Runtime-Evidence belegt die HAR-Emulations-API noch nicht: der
reale SDK-Emulationsaufruf wird **erst mit diesem neuen Test** ausgeführt. Offline-
Tests benutzen dafür ausdrücklich einen synthetischen SDK-Ersatz, nicht reale HARs.

## Aussagegrenzen

- HAR-Pfade sind aus dem ursprünglichen Buildbericht gebunden; deren aktuelle
  Fingerprints werden jetzt zusätzlich erfasst. Das ersetzt keinen damals nicht
  vorhandenen HAR-Inhaltsnachweis. Originaldateien werden vor/nach der Diagnose geprüft.
- Es werden die HARs des **GPU-Builds** ausgewertet, nicht ein rekonstruierter CPU-HAR.
- Quantisierte Emulation und Hardware werden nicht ungeprüft als bitgenau gleich
  vorausgesetzt. Ein numerischer Unterschied ist ein Befund, kein automatisch bewiesener
  Programmfehler und kein Grund für geänderte Qualitätsgrenzen.
- Die 16 Bilder sind bekannte Developmentdiagnostik, kein neuer Hold-out und keine
  größere/finale Qualitätsfreigabe. Originalberichte werden nicht überschrieben.

## Budgets und Ergebnisse

Die Vorbereitung mit den 32 lokalen ONNX-Referenzinferenzen hat fünf Minuten Budget;
je HAR-Stufe zehn Minuten; die abschließende Statistik zwei Minuten. Dazu kommen
Dateiprüfung, gegebenenfalls fünf Sekunden Prozessbereinigung und Git. Die Budgets
sind Schutzgrenzen, keine Laufzeitprognose. Alle 15 Sekunden erscheint ein Heartbeat.

Ergebnisse unter `~/Downloads/hailo8_har_git_<Zeit>_<Zufall>/`:

- `har_comparison/REPORT.md` und `comparison.json`;
- `har_comparison/per_image.csv`;
- phasenweise SDK-/Prozessberichte und Logs;
- `har_and_git_evidence.zip`: ausschließlich der kuratierte Text-/Ergebnisumfang;
- Rohfeeds und neue Emulationsarrays bleiben nur im privaten Diagnoseordner.

Bei vollständiger Ausführung: `HAR_COMPARISON_STATUS=diagnostic_evaluated`. Das bedeutet
**nicht** Quality-PASS. Bei fehlenden Quellen/API-/SDKfehlern steht `incomplete` plus
Primärfehler. Die bisher erfolgreichen Compute-/Build-/Hardwarebelege bleiben gültig.

## Sicherung im bestehenden Ergebnisrepository

Ziel ist `~/onnx-splitpoint-results` mit geprüftem `origin` auf
`Keff789/onnx-splitpoint-results`. Der Starter verändert keine Remote-Konfiguration,
zieht keine Branches um und führt weder Pull/Rebase noch Force-Push aus.

Kuratierte Hailo8-Berichte:

`results/hailo8/20260912_mobilenet_gpu/`

Build-JSONs/-Logs stehen unter `build_metadata/`, nicht unter dem von Git ignorierten
`build/`. Neue Diagnoseskripte stehen unter `experiments/hailo8/har_comparison_r1/`.
Qualitätssnapshot optional unter
`results/evaluation/completsetdev_20260911_213508/quality_snapshot/`.

**Keine `.har`, `.hef`, `.onnx`, `.npy`, `.npz`, Bilder, CUDA-Pakete oder ZIPs werden
in den Repositorybaum übernommen.** Nur eine konkrete, geprüfte Textdateiliste wird
vorgemerkt. Bereits vorhandene, bytegleiche Dateien werden erkannt; Konflikte werden
nicht überschrieben. Bereits vorgemerkte fremde Änderungen führen zum Stopp.

Das vorhandene `scripts/check_before_commit.py` wird auf genau den kuratierten
Nachtrag angewendet. Originalprotokolle enthalten lokale Adressen und Pfade: diese
Reviewhinweise prüfen, insbesondere bei einem öffentlich sichtbaren Repository.
Nach `PUSH` muss der lokale Ausgangscommit dem Remote-Branch entsprechen. Bereits
anderweitig angesammelte ungesendete Commits werden nicht versehentlich mitveröffentlicht.
Es wird nur der neu geprüfte Commit an die entsprechende Branch gesendet, ohne Tags
oder andere Branches. Fehlendes Netzwerk/Auth/abweichender Remote-Stand ergibt STOP;
Diagnose und lokale Dateien bleiben erhalten.

Git-Semantik: https://git-scm.com/docs/git-commit (`--only`, `--pathspec-from-file`)
und https://git-scm.com/docs/git-push (expliziter Commit/Refspec, kein Force).

### Nur Git erneut versuchen – ohne HAR-Wiederholung

Vor einem bereits erstellten Commit:

```bash
bash ./run.sh --publish-existing "$HOME/Downloads/hailo8_har_git_<vorhandener_Ordner>" --push
```

Der Starter gibt den genauen Pfad aus. Nach einem bereits erstellten, aber nicht
gepushten Commit das Repository/Netzwerk prüfen und den ebenfalls ausgegebenen
konkreten Git-Push normal wiederholen; dafür keine erneute HAR-Diagnose starten.
