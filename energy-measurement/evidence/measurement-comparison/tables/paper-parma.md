# Tabellen und Tabellendaten: paper-parma

[Zurück](README.md)

**Einordnung:** PARMA v0.15.1.

[PARMA-Quellenzuordnung](../../../papers/parma-v0.15.1/SOURCE_MAPPING.md).

| Datei | Format | Einordnung | Verfügbare Spalten (Auszug) |
|---|---|---|---|
| [device pair medians](../../../papers/parma-v0.15.1/generated/device_pair_medians.csv) | CSV | PARMA-Paket; Umfang siehe Quellenzuordnung | slug, workload, sensor, sensor_name, n, paired_median_pct, row_order, sensor_order |
| [parma device pair spread](../../../papers/parma-v0.15.1/generated/parma_device_pair_spread.csv) | CSV | PARMA-Paket; Umfang siehe Quellenzuordnung | series, platform, slug, window, sensor, n, pico_median_W, ratio_of_medians_pct … |
| [parma device pair values](../../../papers/parma-v0.15.1/generated/parma_device_pair_values.csv) | CSV | PARMA-Paket; Umfang siehe Quellenzuordnung | series, platform, slug, window, sensor, record_id, pico_W, sensor_W … |

CSV-Dateien können vollständige Run-/Paarwerte oder Plotinputs enthalten; sie sind nicht automatisch zusätzliche Tabellen im Manuskript.
