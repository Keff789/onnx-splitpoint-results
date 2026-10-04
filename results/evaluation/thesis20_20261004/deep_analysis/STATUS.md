# Getrennter Abschlussstatus

Snapshot 2026-10-04T21:50:50.002714+02:00; spätere Archivfortschritte sind separate Laufzeitbelege.

| Arbeitsachse | Tatsächlicher Zustand |
|---|---|
| Wissenschaftliche Ableitung | A–F ausgeführt; konkrete Tabellen/Claims; sechs Haupt- und drei Supplementfiguren PDF/SVG/PNG; 31 Tests PASS; 71/71 abgeleitete Dateien bytegleich |
| Historische Quelle | Kein exakter SHA-Treffer in sechs einzeln protokollierten zusätzlichen Paketen und zwei Snapshots; 21 alte TRT-Full-Verweise behalten die deklarierte Provenienzlücke |
| Bestehende große Archivierung | Fehlerursache behoben und bestehende Warteschlange gezielt fortgesetzt; completion192 Copy 0 / Verify 0; YOLO-Nachlieferung läuft; ursprüngliche Finalisierung wartet |
| Gesamtarchivabnahme | **OFFEN**. Kein Gesamt-PASS und kein Abschluss-Endcode behauptet. Noch kein Vollinhaltsnachweis |
| Zusatzarchivierung dieser Analyse | Separater kleiner Folgeweg vorbereitet; darf erst nach Freeze, echtem Abschlussstatus+Exitcode 0 der ursprünglichen Finalisierung und Ende aller Archivwriter schreiben |
| Tool und Originalmessungen | Toolcommit d164aad6d7c7ef68c1b371c49a1fdea0a3b27dd7/v2.92.0 unverändert; Originalergebnisse erhalten; 0 neue Hardware-/Mess-/Compileläufe |

## Archivübernahme

Bei Übernahme waren die vorhandenen Sitzungen bereits mit rsync 23 und Folgeexit 1 beendet. 152 Fehler betrafen ausschließlich Symlinkzeitstempel; Linktexte waren erhalten. Die vorhandenen Skripte erhielten minimal `--omit-link-times`. 15 kleine Dateien mit Quell-mtime 0 benötigen eine eng begrenzte Ausnahme, die reine mtime-Differenz und exakte Bytegleichheit verlangt. Alte Skripte/Logs/Endcodes bleiben privat gesichert. Kein BASE-Neustart, kein zweiter Writer, keine Bereinigung oder Cachelöschung.

Die bereits vorhandenen Sitzungsnamen `thesis20-archive-20261004` und `thesis20-archive-finalize-20261004` wurden für genau diesen Fortsetzungsweg wiederverwendet. Fortschritt ist durch wachsende übertragenen Bytes/Dateien belegt. Ein rsync-Prozentwert bei inkrementeller Dateilistenaufzählung ist kein verlässlicher Gesamtprozentsatz. Die sehr große YOLO-Nachlieferung bleibt dauerhaft aktiv und darf weiterlaufen. Der tatsächliche schreibbare SSHFS-Mount wurde geprüft; dessen lokaler Alias ist kein Beleg einer separaten Zielmaschine.

Die neue Analyse bleibt bis zum Ende der bisherigen Writer ausschließlich lokal bzw. auf ihrem freigegebenen Git-Reviewbranch. Ihr kleiner Folgekopieprozess prüft den ursprünglichen Finalstatus `copies_complete_with_declared_historical_source_gap`, den echten Endcode 0 und Writerfreiheit; ein wartender Prozess ist kein erfolgreicher Transfer.

## Wissenschaftliche Grenzen und nächster Schritt

Post-hoc/development, drei Wiederholungen, geteilte Fullbaselines, systematische Single-Input-Untermenge, nicht kontrollierte Runtimebedingungen, 16 Energie-Semantikgrenzen und 21 historische Quellenlücken bleiben explizit. Die gemischte Legacy-Full-Energiespalte wurde ausschließlich in der neuen Ableitung eindeutig benannt und aus E/N berichtigt; die ursprünglichen Ratioergebnisse waren bereits korrekt.

Nächster fachlicher Schritt: Claims und sechs Hauptfiguren reviewen, dann gegebenenfalls gezielt ins Paper übernehmen. Nächster Archivschritt: vorhandene YOLO-/Restfolge und Finalisierung ihren Endcode erreichen lassen; danach der getrennte kleine Analysezusatz. Keine neue Messung ist daraus abgeleitet.
