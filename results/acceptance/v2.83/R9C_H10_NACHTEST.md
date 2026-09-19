# R9C H10-Nachtest – Abschlussbericht

**Technische Nachabnahme PASS.** Genau ein zusätzlicher normaler GUI-Workflow am17.09.2026: MobileNetV3 Large, `orin_nx_hailo10_01`, feste Boundary b135. **3/3 Nativezeilen akzeptiert, je100/100 Start→Top-k-Paare.** Der reparierte Capturepfad erzeugt beide Manifeste; der bestehende strikte Consumer-Join und der nachgelagerte GUI-Abschluss sind erfolgreich. Quality **FAIL** bleibt unverändert ein gültiger separater Befund.

Run: `${CONTROLLER_HOME}/Models/EvaluationRuns/r9c_h10_nachtest_20260917_133258/r9c_h10_nachtest_classification_20260917_133840`. Dauer **454,997s** ab GUI-Start; ein Dispatch, null Wiederholungen. Start vor dem realen Tk-Button persistent per flush/fsync reserviert; eigenes Journal1/1 verbraucht. Die ursprüngliche R9C-Matrix bleibt historisch8/9 technisch akzeptiert; ihr fehlgeschlagener H10-Run wurde nicht umgeschrieben.

## Ursache und Umsetzung

Der ursprüngliche eigene Einbaufehler war ein versehentlich in `_capture_raw_hailo10_sample` eingefügter ClassificationCompletion-Block mit undefiniertem `task_value`. Er ließ nach der erfolgreichen Messung den ungemessenen semantischen Dump scheitern. Die vier Zeilen waren bereits vor diesem Auftrag entfernt; der gemessene Top-k-Abschluss war erhalten. In diesem Auftrag **keine weitere Produktcodeänderung** und kein erneutes Anwenden des Fixes. Der neue normale Workflow bestätigt jetzt die zuvor fehlende reale GUI-Nachabnahme.

Eigene tasklokale Kopie des vorhandenen spawn-sicheren GUI-Helfers, eigener Runroot, Eintragjournal und Smokeprofil. Die Profiländerungen gegenüber R9C beschränken sich auf Name/ID/Zweck; bestehende Seeds, Margen, Eingabe-/Precisionverträge, Queue/Inflight und normale Registry blieben erhalten. Cancelgrenze auf1800s mit regulärem Produktcallback begrenzt; kein Cancel nötig. Die lokale Preview erzeugte keinen Run. Die aktuelle NX-Umgebung wurde aus dieser Sitzung übernommen.

## Mess- und Manifestnachweise

| Backend | Case | Mean ms | P50 ms | P95 ms | Completed FPS | Paare | Technik | Quality |
|---|---|---:|---:|---:|---:|---:|---|---|
| hailo10h_to_trt | b135 | 25.378450 | 26.216321 | 26.381196 | 310.020660 | 100/100 | PASS | FAIL |
| native_full_hailo10h | full | 9.168241 | 9.210503 | 9.336424 | 210.271714 | 100/100 | PASS | FAIL |
| native_full_tensorrt | full | 1.287758 | 1.286464 | 1.300421 | 774.830150 | 100/100 | PASS | PASS |

100 Frames /10 Warmup /1 Performancewiederholung. Mean/P50/P95 unabhängig aus den gespeicherten ganzzahligen monotonen Start-/Endpaaren neu berechnet; IDs eindeutig, Start≤Ende, je100 tatsächliche `classification_top1_top5`-Abschlüsse. FPS separat aus Abschlusszahl und Makespan berechnet. Reporterfelder und CSV stimmen numerisch; das tatsächliche GUI-Widget zeigt alle drei Zeilen mit passenden gerundeten Mean/P50/P95/FPS und n=100/100. Belege: `REQUEST_PAIRS_R9C.json`, `LATENZ_KLASSIFIKATION.csv`, `ACTUAL_EXPORT_WIDGET_VERIFICATION.json`.

Split: `ok=true`, kein `error` oder `output_dump_error`. `native_outputs_manifest.json` und `native_fifo_boundary_manifest.json` vorhanden, ihre Bytes passen exakt zu den Hashes der Consumer-Attestierung. Status `exact_quality_native_engine_command_and_boundary_match`; Attestierung `local_files_rehashed_and_exact_command_join_verified`. `CAPTURE_CONSUMER_EVIDENCE.json` enthält die konkreten Pfade, Hashes und die gespeicherte Attestierung. Keine neue Diagnose-/Zusatzinferenz zur Prüfung dieser Belege.

Quality maximal32 Bilder,100 Bootstrap; zentrale Qualität4/4 Auswertungen abgeschlossen,2 FAIL und2 PASS, keine fehlenden Auswertungen. H10H Full und Split FAIL; TRT Full PASS. Keine Margin-/Seed-/Label-/Tensor-/Schwellenwertänderung. Kurze wiederholte Prepared-Input-Messungen sind keine Langzeit-/Energieabnahme oder allgemeine Freigabe aller Klassifikationsmodelle.

## GUI-Abschluss, Cleanup und Budgets

Normaler Enddialog: „Abgeschlossen mit Qualitätswarnungen. Native:3 erfolgreich,0 ausgeschlossen,0 fehlgeschlagen/blockiert,0 fehlend“. Dialog tatsächlich bestätigt, alle21 registrierten Jobs ohne lebenden Worker, GUI zerstört und Helfer Exitcode0. Normales Remote-Cleanup für generischen Run und markergebundenes Native-Runverzeichnis erfolgreich; Native-Cleanup rc0. Artefaktfinalisierung **846/846 PASS**, null fehlende Dateien/Hashabweichungen/Verifikationsfehler. Workflow-Interlock und H10-Plattformsperre anschließend exklusiv ohne Warten prüfbar und wieder freigegeben. Keine offenen Cleanupzustände. `GUI_CLEANUP.json`.

Produktpreflight **4 HITs,0 benötigte/ausgeführte/unvorhergesehene Kaltbuilds**. Null HEF/DXNN/TRT/Firmware-/Wrapperbuilds; Force AUS. Energie und Windowprobe AUS im Smokeprofil; normale Energie-/Collector-Konfiguration unverändert. Keine Poweränderung. Keine Rohdiagnose-/Direktinferenz, kein zweiter Workflow, keine H8-/DeepX-/YOLO-Nachmessung.

## Lokale Prüfungen und genaue Ergebnisse

- Tatsächliche Sandboxprobe: PASS, Exit0; ephemere Schreibzugriffe, TCP-Loopback und Tk erfolgreich. Normaler START.sh-Hostpreflight PASS.
- Finales R9C-Manifest und bereitgestellter Sourceindex vor Ausführung unverändert; Installedprüfung **PASS**, Exit0,2013 manifesteigene Dateien,70 lokale Benutzerprofile separat erkannt.
- `tests/test_v283_r9c_classification.py::test_h10_unmeasured_semantic_capture_has_no_task_completion_dependency`: **1 PASS,0 FAIL,0 SKIP**,0,74s pytest, Exit0. Test prüft normalen und diagnostischen Raw-Slot-Zweig lokal mit Fake-Session.
- Einmalige lokale Produkt-Spawnprobe: **PASS**, Exit0; Quality-Worker abgeschlossen, null Hardware-/GUI-Starts.
- Normale GUI-Preview: **PASS**, Exit0,0 Runs; Settings bytegleich. Tatsächlicher GUI-Workflow: **PASS technisch**, Exit0,3/3 Nativezeilen; Quality FAIL separat.
- Zeitpaar-/FPS-Rechnung: **3/3 PASS**. Reporter-CSV und reales GUI-Widget: **3/3 PASS**. Capturemanifeste/Consumer, GUI/Cleanup, Bestandserhaltung: **PASS**, alle Prüfkommandos Exit0.
- Nach der erlaubten Dokument-/Manifestpflege: Installedprüfung erneut **PASS**, Exit0. `git diff --check`: Exit0.

Exakte relevante Befehle und Exitcodes stehen in `COMMANDS.json` und den einzelnen `*.command.json`; direkter JUnitbeleg in `direct_regression.xml`.

Die vollständigen1012 Produkt- und29 Tk-Tests wurden bewusst **nicht wiederholt**, da der Produktcode gegenüber dem finalen R9C-Stand identisch ist. Diese Zahlen bleiben historische R9C-Belege und werden nicht als neue Tests oder mit dem direkten Fall addiert. Keine Vollkampagne, neuen Energieaufnahmen, Numerik-/Compiler-/Klassifikationsarchitektur oder weitere Geräteabnahmen.

## Dateien, Erhaltung und Git

Im Repository geändert: `docs/ARBEITSSTAND.md` schließt ausschließlich die konkrete MobileNet/H10-GUI-Lücke; `SOURCE_MANIFEST.json` und `SHA256SUMS.txt` pflegen allein dessen bestehenden Eintrag. `AUFTRAGSDIFF.patch` enthält den vollständigen kurzen Auftragsdiff gegen die zu Beginn gesicherten Bytes. Alle übrigen Produktsourcebytes sind durch unveränderte Manifestzeilen plus erfolgreiche Installedprüfung belegt. Tasklokale Helfer, Profil, Journal und Nachweise liegen ausschließlich im neuen Ausgabeziel.

Version2.83, Build-ID `v2.83-r9b-request-latency`, Branch `codex/v283-nightfix-smokes`, HEAD `c5eb66eaa562728e9397a550570740d6a03e734d` unverändert. **81 bestehende Dateien bytegleich**, darunter Settings, normale Energie-/Runmodus-/Hardware-/Buildkonfiguration,70 Repositoryprofile sowie alte R9C-Journale/START-Marker, Originalprofil und Originalhelfer. Settings vor/nach GUI sha256 `787aca97090b18f6168c91b3e335d65746f2541982a8e935d786088f436f52aa`.

`git status --short` vor/nach identisch: 107 modifizierte und 41 unversionierte Einträge, bereits zu Beginn vorhanden. Vollständige Ausgabe: `GIT_STATUS_FINAL.txt`. `git diff --stat`: **107 files changed, 5131 insertions(+), 1530 deletions(-)**; das umfasst frühere Arbeiten und erfasst unversionierte Dateien nicht. Der konkrete Nachtestdiff betrifft nur die oben genannten drei Dateien. Kein Commit/Push/Reset/Autostart.

## Verbleibende Grenzen und nächste Handlung

Keine neuen technischen Laufzeitfehler. Im Reporter erschienen nichtfatale Matplotlib-Warnungen zur GUI-Verwendung außerhalb des Hauptthreads; Diagrammerzeugung, finaler Dialog und Artefaktabschluss waren erfolgreich. Keine Codekorrektur daraus abgeleitet.

Die technische Capture-Nachabnahme gilt nur für diesen MobileNetV3-Large/H10H-b135-Scope. Quality FAIL bleibt bestehen. H10-/YOLO26-Nulloutputs und DeepX-/YOLO26s-XYXY sind weiterhin offen und wurden nicht untersucht oder als erledigt markiert. Nächste Handlung: die gelieferten Nachweise prüfen; **kein weiterer automatischer Workflow**.

Lieferung: `ERGEBNISSE_R9C_H10_NACHTEST.zip` mit Bericht, direktem Test, Zeitpaaren, Manifesten, Consumer-/GUI-/Cleanupnachweisen, kurzen Diffs, Git- und Erhaltungsbelegen. Keine Modelle, Bilder, Roharrays, Secrets, Umgebungsdateien oder Compilerpakete. ZIP-Inventar und CRC-/Byteprüfung liegen separat bei.
