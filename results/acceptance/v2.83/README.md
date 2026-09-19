# v2.83: kuratierte Abnahmebelege bis R9G

Stand 19.09.2026. Dies ist eine ergänzende Auswahl, kein vollständiger Roharchivexport.
Der R9H-Drei-Splitlauf ist nicht als abgeschlossenes Ergebnis enthalten.

| Beleg | Inhalt / Grenze |
|---|---|
| [R8](R8_ABSCHLUSS.md) | Normale Config/Collector/GUI, kleiner H8-Smoke; spätere Korrekturen separat |
| [R9B Restabnahme](R9B_RESTABNAHME.md), [Coverage](R9B_GUI_COVERAGE.json) | H8-Ersatz b021 und beide DeepX-Pfade real; Messumfang/Latenzendpunkte erhalten |
| [R9C H10-Nachtest](R9C_H10_NACHTEST.md) | 3/3 Nativezeilen und 300 Top-k-Zeitpaare, normale Capture-/Consumerstrecke; Quality getrennt |
| [R9G GUI-Abschluss](R9G_GUI_RESULT.json) | Abschließender 7-Modelle-/1-Splitrun; 63 Native, 189 Energie, keine pauschale wissenschaftliche Freigabe |
| [R9G Host-JUnit](R9G_HOST_TESTS.xml) | 122 tatsächlich ausgeführte lokale Fälle, nicht die ganze Produktsuite |
| [JUnit-Nachzählung](TEST_EVIDENCE.csv) | Aus den angegebenen gelieferten JUnit-Dateien extrahiert; überlappende Reihen nicht addieren |

Die R3-/R6-Zahlen beziehen sich auf die angegebenen v2.83-Archive, nicht auf frühere
DeepX-R1/R2-Verzeichnisse anderer Versionen. Historische erfolglose Zwischenversuche sind nicht
zu PASS umgeschrieben. Insbesondere sind frühe einzelne R5-Energie-PASSs keine Dreierserienfreigabe.

Lokale Homes und private IP-Adressen sind in diesen öffentlichen Kopien redigiert.
[Quellenzuordnung](../../../inventory/V283_EVIDENCE_SOURCES.json) benennt Originalarchive,
interne Pfade und Originaldateihashes; die Originale bleiben unverändert außerhalb von Git.
Modelle, HEF/DXNN/TRT, Bilder, Roharrays, komplette ZIPs und private Profile sind nicht enthalten.
