# DeepX Pre-/Postprocessing-Smoke: mobilenet_v3_large

**Diagnose, keine Modell-/Performance-/Energieabnahme.**

## CPU-Kontrollarme auf demselben unveränderten ONNX

| Arm | Bilder | Top-1 | Top-5 |
|---|---:|---:|---:|
| scale_only | 32 | 65.62 % | 84.38 % |
| imagenet_mean_std | 32 | 81.25 % | 93.75 % |
| canonical_reference | 32 | 81.25 % | 93.75 % |
| harness_crop256 | 32 | 81.25 % | 96.88 % |
| export_metadata_geometry | 32 | 75.00 % | 96.88 % |

## DeepX Full

Native/sealed: 16 Bilder, Top-1 68.75 %.
Produktiver Quality-Pfad: 16 Bilder, Top-1 68.75 %.

CPU- und Hardwarequoten haben ggf. unterschiedliche Nenner. Für die Ursachenprüfung die bildweise gepaarten Zeilen in `analysis.json` verwenden.

## Grenzen

Die erste Auswahl folgt ausschließlich den ersten IDs des ursprünglichen B500-Auftrags, nicht den Erfolgen eines Kontrollarms. Kein neuer Referenzvertrag wird erzeugt.
Der Crop-Arm und gegebenenfalls der Metadaten-Arm sind ausdrücklich alternative Eingabekontrollen. Die Kampagnenreferenz wird nicht überschrieben.
Der Kalibrierungsreplay ist ein gekennzeichneter Nachbau der gespeicherten Konfigurationsfolge, kein direkt ausgeführter DX-COM-Loader.
Ein optionaler Splitvergleich nutzt den vorhandenen Float-ONNX-Tail auf der CPU, nicht die TensorRT-Pipeline.
Abweichungen sind Evidence, nicht automatisch ein Fehlerbeweis. Die zentrale B500-Statistik und Detectionmodelle werden hier nicht ausgeführt.

Rohwerte liegen in NPZ-Dateien. Paketstatus `evidence_collected` bestätigt nur das Einsammeln, nicht eine bestandene Qualität.
