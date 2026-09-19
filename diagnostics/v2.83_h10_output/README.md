# H10: negativer Outputvertrag und negativer Präzisionskandidat

[Native UINT8-Outputdiagnose](H10_OUTPUT_BEFUND.md) und
[einmaliger Compile-only-SDK-Befund](R9E_SDK_RESULT.json) sind verschiedene Verträge.
Die ursprünglichen HEFs sind gebaut, vernichten aber die betrachtete Scoreinformation.
Der alternative höherpräzise s/b364-Kandidat wurde aus einem quantisierten HAR geladen und
scheiterte bei der Compilerzuordnung (`auto_spatial_reshape_from_activation3_to_concat23`,
`Agent infeasible`). Das ist kein Timeout und kein Befund über alle H10-Graphen.

R9G hat die betroffenen späten Grenzen nicht numerisch repariert, sondern über allgemeine
Vertragsprüfung und normale Kandidatenreihenfolge einen anderen nutzbaren Split ausgewählt.
Siehe [R9G Backfill](../../results/evaluation/r9g_eval_20260918_171131/Backfill.csv).
Keine erneute unveränderte Kompilierung aus dieser Dokumentation ableiten.
