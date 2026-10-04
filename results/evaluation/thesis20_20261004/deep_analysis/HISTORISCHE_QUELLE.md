# Historische Attestorquelle – gezielte Suche vom 04.10.2026

**Ergebnis: kein exakter Treffer; die Provenienzlücke bleibt für 21 TensorRT-Full-Verweise offen.** Die Messkampagne und die wissenschaftliche Ableitung werden dadurch nicht erneut gestartet.

Gesucht ist der unveränderte Byteinhalt von `native_output_endpoint.py` mit SHA256 `aae20edc6a4bb19c40d00f82707e333d8c931a2ace23b641c426d099fb3a3d0e`. Ein semantisch ähnlicher Stand ist kein Ersatz. Die 21 Bindungen wurden aus dem vorhandenen Artefaktplan erneut gezählt: sieben Modelle × drei Setups. Originalcommands, Sollhashes und Ergebnisse wurden nicht geändert.

## Zeitliche Eingrenzung und Scope

Das Originalworkflowlog enthält am **28.09.2026, 22:17:12** den ersten dort aufgefundenen TensorRT-Full-Performanceaufruf für MobileNetV3-Large/H8, Wiederholung 1/3, 1.000 Frames nach 100 Warmup. Die Vendor-Full-Reihe beginnt dort um 22:16:39. Zeitstempel sind die logeigene Darstellung ohne zusätzliche Zeitzonenbehauptung. Der Suitepfad in den ursprünglichen Attestorbindungen ist eine generierte Legacy-Suite; damit bleibt eine von der gleichnamigen Releaseversion abweichende Arbeitskopie möglich. Das archivierte MobileNet-Suitepaket hat eine lokale mtime vom 25.09.2026 13:46:31; mtime ist kein Beweis des ausgeführten Byteinhalts.

Die bisherigen sieben `historical-attestor-*.json` wurden zuerst gelesen. Deren Angaben (315 lokale Module, 60 Kandidatenarchive/26 passende Mitglieder, sieben Haupt-Suites, zwei Gitstände) wurden nicht als erschöpfende Suche interpretiert. Das konkret ausgeschlossene v2.91.0_SOURCE.zip und die sieben ausdrücklich schon geprüften Hauptkampagnen-Suites wurden nicht erneut geöffnet. Die alten Zählprotokolle listen nicht alle 60 Archivpfade einzeln: Für die hier neu einzeln belegten Pakete ist daher nicht durchgehend beweisbar, ob ein früherer aggregierter Suchlauf sie bereits mitzählte. Dieser Nachweis wird nicht erfunden.

Die Suche beschränkte sich auf projektspezifische lokale Ablagen und konkrete Hinweise: Downloads-Namen, den vorhandenen lokalen Metadatenindex, Updatebackups, `~/.local/share/onnx-splitpoint-codex`, zwei benannte historische `/tmp`-Source-Snapshots sowie separat konservierte historische Suitepakete. Der AP08-Editiertext unter `/tmp` verwies konkret auf einen inzwischen nicht mehr vorhandenen AP06–AP08-Arbeitsbereich. Keine breite Netzlaufwerksuche, Installation oder Ausführung alten Codes; ZIPs wurden per Mitgliedsverzeichnis, TARs streamend nur bis zum relevanten Mitglied gelesen. Suchdauer etwa zwölf Minuten einschließlich konkreter Herkunftseingrenzung; Archivdiagnose lief parallel.

## Neu einzeln protokollierte Pakete

| Paket/Arbeitsstand | Archivmitglied | Ergebnis |
|---|---|---|
| `retry_main_release_20260925_b6cgpl9a/installed_source_before.tar.gz` | `onnx_splitpoint_tool/native_output_endpoint.py` | 56063 B; SHA256 `0667f3368b684ed5df2b801b8283a725d072722115a91f9cff2c3801a3396139`; kein Treffer |
| `thesis20_completion_2.91.1_v3O77ClC/ONNX-Splitpoint-Tool_v2.91.1_source.zip` | `ONNX-Splitpoint-Tool_v2.91.1/onnx_splitpoint_tool/native_output_endpoint.py` | 56063 B; SHA256 `0667f3368b684ed5df2b801b8283a725d072722115a91f9cff2c3801a3396139`; kein Treffer |
| `thesis20_resume_preflight_fix_2.91.1_f7yt3xf8/ONNX-Splitpoint-Tool_v2.91.1_resume_preflight_fix_source.zip` | `onnx_splitpoint_tool/native_output_endpoint.py` | 56063 B; SHA256 `0667f3368b684ed5df2b801b8283a725d072722115a91f9cff2c3801a3396139`; kein Treffer |
| `historical-suite-bundles/yolo26s/suite_bundle.tar.gz` | `splitpoint_runners/native_output_endpoint.py` | 56063 B; SHA256 `0667f3368b684ed5df2b801b8283a725d072722115a91f9cff2c3801a3396139`; kein Treffer |
| `historical-suite-bundles/yolov7_paper/suite_bundle.tar.gz` | `splitpoint_runners/native_output_endpoint.py` | 56063 B; SHA256 `0667f3368b684ed5df2b801b8283a725d072722115a91f9cff2c3801a3396139`; kein Treffer |
| `historical-suite-bundles/yolo11l/suite_bundle.tar.gz` | `splitpoint_runners/native_output_endpoint.py` | 56063 B; SHA256 `0667f3368b684ed5df2b801b8283a725d072722115a91f9cff2c3801a3396139`; kein Treffer |

Zusätzlich wurden zwei konkrete Source-Snapshots geprüft: R9L Source-Closure (Datei-mtime 20.09.2026) und Thesis-Baseline (25.09.2026). Beide liefern ebenfalls 56.063 Byte und SHA256 `0667f3368b684ed5df2b801b8283a725d072722115a91f9cff2c3801a3396139`. Der historische H8-v2.79.13-Helper wurde nicht mit dem Full-Attestor verwechselt.

## Verbleibende gezielte Anfrage an weitere Nutzerbackups

1. Originale Arbeits-/Installationsbackups oder Suitepakete aus **20.–28.09.2026**, insbesondere direkt vor den Full-Aufrufen am 28.09. ab 22:16 Uhr. Gesuchte Namen: `installed_source_before.tar.gz`, `source-before*.zip`, `suite_bundle.tar.gz`, `runner-bundle.tar.gz`; enthalten sein muss das exakte Modul.
2. Tatsächlich erhaltene `v2.90.1`-/`AP00`–`AP08`-Arbeitsstände, insbesondere der frühere AP06–AP08-Bereich vom 22.09.; die bereits lokal geprüften Releasequellen müssen nicht erneut angefordert werden.
3. Frühe `v2.91.1`-/`v2.91.2`-Sicherungen, sofern sie andere alte vendorte Suites enthalten; erst danach andersartige v2.83/R9-Pakete mit konkretem Ursprungshinweis.

Die Versionsnamen sind Suchhypothesen, keine bewiesene Releasezuordnung des gesuchten Hashs. Weitere Backups fehlen in den untersuchten lokalen Ablagen; das ist keine Aussage über sämtliche Nutzerbackups.

## Reviewbelege

- Private Einzelbelege: `private/historical-new-package-search.json` (exakte Pfade, Mitgliedsnamen, Größen und SHA256), `private/historical-first-full-command-excerpts.json`.
- Die 21 bestehenden Herkunftsverweise bleiben in `private/historical-21-reference-paths.json` und der kompakten Index-CSV nachvollziehbar; sie sind ausdrücklich keine vervollständigte Fund-Pfadkarte.
- Ohne Hashfund wurde keine alte Pythondatei additiv als vermeintliches Original gesichert und kein wissenschaftlicher Freigabewert angehoben.
