# R9C: H10 YOLO26m b398 / YOLO26s b364

**Offline erneut eingegrenzt; kein belegter Produktadapterfix und kein Hardware-/Quality-PASS.** Untersucht wurde je das bereits in R2 aufgenommene Bild `000000000139.jpg`. R9C hat für diesen Befund **0 HEF-, 0 TRT-, 0 GUI-Aufrufe und 0 Builds** verbraucht. Vier lokale ORT-P2-Aufrufe wurden ausgeführt. Produktsource, Modellrezepte und Grenzen wurden nicht geändert.

## Erste beobachtbare Verluststelle

Schon B, der gespeicherte physische HEF-Hostoutput **vor** Namens-/Layoutabbildung, enthält in sämtlichen 80 Scorekanälen ausschließlich den jeweiligen UINT8-Nullpunkt. Das sind jeweils 672.000 Werte; die Boxkanäle besitzen dagegen unterschiedliche Codes. Der aktuelle Hostadapter, die gebundene P2-Bridge und der Decoder erzeugen den Scoreverlust nicht erst nach B.

| Beobachtung, neu aus den R2-Arrays nachgerechnet | YOLO26m b398 | YOLO26s b364 |
|---|---:|---:|
| B: Format / Shape | uint8 [1,8400,84] | uint8 [1,8400,84] |
| B: Boxcodes, Kanäle 0…3 | 33…228 | 33…242 |
| B: einzige Scorecodes, Kanäle 4…83 | 39 | 35 |
| Exakte HEF-/Bridge-Scale | 3,4920754432678223 | 3,1612741947174072 |
| Exakter Zero point | 39 | 35 |
| D: dequantisierte Boxwerte | −20,9524536…660,0022583 | −6,3225484…654,3837280 |
| D: Scorewerte | sämtlich 0 | sämtlich 0 |
| E: P2-Boxwerte | 0…45,40625 | 0…47,4375 |
| E: P2-Scorewerte | sämtlich 0 | sämtlich 0 |
| Float-P1-Referenz: Scoremaximum | 0,9599331617 | 0,9049965143 |
| Gleiche Floatreferenz nach vertragsgemäßer UINT8-Quantisierung: Scorecode | 39 | 35 |
| Aktueller BN6-Decoder, unverändertes Default-Conf 0,25: E / Floatreferenz | 0 / 5 | 0 / 8 |

Der vorhandene skalare UINT8-Vertrag verwendet dieselbe grobe Schrittweite für Pixelkoordinaten und Wahrscheinlichkeiten. Bei beiden Scales liegt sogar 1 unter einer halben Quantisierungsstufe. `rint(score / scale + zero_point)` bildet daher die vorhandenen Float-Scorewerte auf den Nullpunkt ab. Dies wurde erneut ohne Clipping, Sigmoid oder unquantisierte Floatwerte an einer UINT8-Engine geprüft; der gesamte quantisierte Referenztensor liegt im erlaubten Bereich 0…255. Die gleichen vier bestehenden Kontrollen wurden nicht nochmals auf Hardware gestartet.

Das grenzt die Ursache auf **spätestens den kompilierten UINT8-Ausgabevertrag / dessen Ausgabequantisierung** ein. Die Aufnahme ist keine interne HEF-Aktivierung vor Quantisierung; sie lokalisiert deshalb keinen bestimmten Compilerpass. Ein weiterer Verlust an einer nicht beobachteten früheren internen Stelle ist damit nicht ausgeschlossen. Unterschiedliche Boxcodes beweisen auch keine geometrische Referenztreue. Ein FLOAT32-VStream mit bloßer Dequantisierung derselben Codes könnte die verlorenen Scores nicht wiederherstellen.

## Aktuelle produktive Kette, offline geprüft

- Hailoformatwahl: `onnx_splitpoint_tool/runners/backends/hailo_backend.py:628` (`_hailo_native_vstream_format_type_name`) und `:1336` (`_set_output_formats`) trennen den nativen HEF-Streamtyp von der Hostformatwahl. Die vorhandenen Capturemetadaten deklarieren UINT8, exakte QuantInfo und `outputs_dequantized=false`.
- Native Hostweg: `scripts/native_hailo10_trt_e2e_from_benchmarkset.py`, `_extract_slot_outputs` → `_pick_hailo_output` → `NativeTRT.prepare_inputs`, wurde mit den physischen B-Arrays und den originalen Shape-/Dtype-/Namensverträgen ausgeführt, mit simuliertem Bufferhandle und ohne Runtimeinstanziierung. Der resultierende Hostinput ist byteidentisch zu gespeichertem C und B. Die scheinbare NCW-Inputshape von C ist absichtlich nur die TRT-Bindingshape; die Bridge erwartet darin die ursprüngliche NWC-Speicherreihenfolge.
- Generic Hostweg: aktuelles `_adapt_tensor` und `onnx_splitpoint_tool/runners/native_split_quality_runtime.py:191` (`prepare_quality_first_boundary_input`) mit der originalen Bridge-Layoutdeklaration liefern ebenfalls exakt C. Der Aufrufer in `resources/templates/run_split_onnxruntime.py.txt:3250` protokolliert diesen bereits vorhandenen Weg als `quality_first_internal_bridge_memory_order_preserved`.
- Gebundene `bound_bridge.onnx`: genau `Cast → Sub(zero_point) → Mul(scale) → Reshape([1,8400,84]) → Transpose([0,2,1])`, anschließend unveränderte P2. Die Initializer entsprechen exakt der erfassten HEF-QuantInfo. Aktuelles `dequant_reference` dequantisiert einmal; sein transponiertes Resultat ist exakt gespeichertes D. Zwei ORT-Aufrufe je Modell verarbeiten C und die passend gepackte quantisierte Floatreferenz. Die neu berechnete Ausgabe für C ist exakt die gespeicherte ORT-Ausgabe `P2_same_C_000`; sämtliche Scores bleiben null.
- Aktueller `onnx_splitpoint_tool/runners/harness/yolo.py:222` (`_decode_bn6`) findet bei unveränderter Konfiguration keine Detektion in E. Der Scoreverlust liegt bereits vor diesem Filter. `native_output_endpoint.py:660` / `runtime_output_contract` verweigert mit der unveränderten R2-Deklaration weiterhin `decoded_values_do_not_prove_nms;explicit_nms_declaration_required`. Das ist ein separater Deklarationsbefund, keine Ursache der Nullscores und kein Anlass, eine NMS-Deklaration zu erfinden.

Alle Assertions der beiden lokalen Replaykommandos (`.venv/bin/python -B`, In-Memory-Array-/ORT-Prüfung) bestanden, Exit 0. Die gespeicherten echten Generic-/Native-TRT-Ausgaben für dasselbe C sind byteidentisch. Neu nachgerechnete maximale TRT-vs.-ORT-Abweichungen: m `0,00926971435546875`, s `0,0183868408203125`; für die quantisierte Referenz m `0,008821487426757812`, s `0,012258529663085938`. Diese Zahlen sind **kein pauschaler numerischer PASS**.

## Primärbelege und Grenzen

R2-Basis nach dokumentiertem Pfadumzug:

`${CONTROLLER_HOME}/.local/share/onnx-splitpoint-codex/v283_r3_lokal_20260914_192352_8vql14m7/archivierte_codex_runs/v283-nightfix-20260914_161840-ZUNmFW/fortsetzung_r2_20260914_173733_k7C9wO`

Die tatsächlich erneut gelesenen Rohpakete liegen relativ dazu unter `h10_diagnosis_resolver_fix/hailo10_yolo26_v27931_20260914T154539Z_33bb75ye/results/{yolo26m,yolo26s}/`: `raw_tensors.npz`, `diagnostic.json`, `request.json`, `bound_bridge.onnx`. Der vorhandene `load_packet` prüfte die bereits gespeicherte Paketbindung und Shapes/Dtypes; neue Bild-/Modellhashes wurden nicht angelegt. Weitere gelesene Belege: `h10_control_results.json`, `h10_p2_remote/results/controls_summary.json` und je Modell `native_same_C.npz`, `reference_P1_quantized_TRT.npz`. Diese Roharrays/Modelle gehören nicht ins Ergebnis-ZIP.

Es fehlt kein Rohoutput für diese begrenzte Fragestellung. Deshalb keine neue Rohaufnahme und mangels belegtem Produktfix kein Output-GUI-Nachtest. Keine neue pytest-Auswahl durch den lesenden Teilagenten; die vorhandenen Generic-/Bridge-Regressionsanker wurden gelesen, die gemeinsame finale Softwareabnahme liegt beim Hauptagenten. Die Aussage gilt für dieses eine Bild je Modell; keine neue 32-/500-/5000-Bilder-Qualitätsaussage, keine Energie-/Latenzmessung.

Ein eigener Folgeauftrag müsste einen **nachweislich scoreerhaltenden kompilierten Ausgabevertrag an denselben Grenzen b398/b364** belegen; die vorhandene gemeinsame skalare UINT8-Quantisierung reicht dafür nicht. Score- und Koordinatenrepräsentation müssten dabei unterscheidbar beziehungsweise ausreichend auflösbar sein. Ob das vorhandene Compilerwerkzeug dies an exakt diesen Grenzen unterstützt, ist hier nicht nachgewiesen. Falls der Vertragswechsel unterstützt wird, wäre der kleinste gezielte Buildumfang ein neues P1-HEF plus passend gebundene P2-Bridge/TRT-Engine je betroffenem Modell, danach dieselbe feste Bildgegenprobe und erst anschließend eine begrenzte GUI-Abnahme. **Kein solcher Build ist durchgeführt oder als bereits sicherer Fix freigegeben; kein Boundarywechsel nach günstiger AP.**
