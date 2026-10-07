# Native/Generic Revision 3 — geprüfter Zwischenstand

Der aktuelle Auftrag ist noch in Ausführung. Der
[datierte Export](../results/evaluation/native_fairness_rev3_20261007/README.md)
führt 15 neue Native-Punkte mit drei tatsächlichen Prozessen, neun unveränderte
Klassifikations-Fulls mit belegter Performancewiederverwendung und neun neue
Generic-Paare. 222 Native- und 195 weitere Generic-Performancepunkte fehlen noch.
Die gemeinsame Dauersteuerung ist jetzt im Worktree integriert; die neun
Generic-Punkte benötigen vor finaler Energie eine neue Bestätigung. Eine alte Messung erhält keine erfundenen neuen Repeats.

Die Archivprüfung war ausschließlich lesend. Der vorhandene YOLOv7-Review-ZIP
bestand seinen Prüfer für 6.281 Payloadhashes sowie die 27 Splitrepeats,
18 Fullrepeats und drei Kontrollen. Manifeste, 246 Native-Commandbindungen und
benötigte tatsächliche Artefakte des historischen Gesamtarchivs wurden gezielt
geprüft; eine vollständige kryptografische Gesamtarchivprüfung wird nicht behauptet.
Keine Datenlöschung, Verschiebung, Retention oder Speicherbereinigung.

Die historische Generic-Nutzung wurde aus tatsächlichen 204 Completed-Fällen
und separaten Raw-Referenzen rekonstruiert. Allgemeines Streaming, Multi-Tensor,
`generic`, `native_fifo` und `NativeTRTSession` bleiben erforderlich. Entfernt
wurden ausschließlich drei unerreichbare DeepX-P2-Duplikate samt toten Helfern,
197 Zeilen mit erhaltenen Originalquellen und AST-/Diffbelegen. Raw-Messungen
behalten ihren begrenzten Endpunkt; sie werden nicht zu Completed Tasks umbenannt.

Geprüfte Korrekturen betreffen verlustfreien Queueabschluss und echte Counts,
eindeutige DeepX-Domänen ohne Boundary-Wertecache, das Ende standardmäßiger
label-/scoregesteuerter Mappingwahl, tatsächlich gleiche vorbereitete Timinginputs
und fachliche Completion im Timer mit strengem eigenem Postflight außerhalb.
NaN/Inf in verworfenen Kandidaten bleiben Fehler; Decoderformate behalten ihre
eigenen Verträge. Der Student-t-Fallback nutzt die vorhandene geprüfte Routine;
die 246 historischen Collectorintervalle benötigten keine Korrektur.

H10 Full konnte über bereits vorhandene sichere asynchrone Requests mit acht
Slots ausgeführt werden. Tatsächliche Parallelität, unabhängige Puffer,
Outputzuordnung und Drain sind belegt. Die vorab festgelegte Auswahlregel
übernimmt 33,230241 FPS; die Ein-Slot-Kontrolle mit 12,393079 FPS bleibt separat.
Für H8 hätte diese Erweiterung einen neuen Scheduler erfordert und bleibt
außerhalb des begrenzten Umbaus. Unterschiedliche zulässige Backendparallelität
wird nicht als kontrollierter isolierter Hardwareeffekt dargestellt.

Drei Full-Energiepunkte sind über die normalen Reportconsumer qualifiziert:
DeepX Vendor 0,689874383, H8 Vendor 0,549843563 und DeepX TRT 0,613181286 J/Task.
Je drei tatsächliche 60-s-Repeats liefern Mittelwerte und Student-t-Intervalle.
Rohe Systemenergie, bestehende TRT-Vergleichsnormalisierung und Qualityklasse
sind getrennte Felder. H8 behält `accuracy_loss`. Die Energie wird nur an exakt
gebundene aktuelle Performance-Reports angefügt. Frühere diagnostische
Erfassungen bleiben nichtclaimbar.

Der Reportfix verhindert die versehentliche Übernahme eines diagnostischen
A/B-Shadow-Flags in die Primärpolicy. 124 gezielte Tests gegen echte
Worktree-Module und die tatsächlichen positiven/negativen Aufnahmen bestehen.
Der neue normale Import dreier Single-Captures behält originale Rawindizes
und führt logische Repeatindizes lediglich als abgeleitete Felder.
Das ist eine Reportänderung ohne neue Hardwaremessung oder DUT-Deployment.

Der folgende H10-TRT-Versuch endete mit Silence-Timeout ohne bestätigten
Quellenabschluss. Die physische Quarantäne und alle Startketten bleiben erhalten;
ein H8-Folgeauftrag wurde vor Collectorstart abgewiesen. Für die konkrete
einmalige H10-Fortsetzung fordert die vorhandene Recovery-Schutzfunktion eine
Freigabe nach diesem STOP. Diese ist noch offen. Der isolierte Accountingfix
für den nachweislich ungestarteten H8-Auftrag ersetzt keine physische Freigabe.
Erfolgreiche Repeats werden bei der Fortsetzung nicht erneut gestartet.

Neue Gruppen sind im getrennten datierten Archiv einschließlich Fehlern,
Befehlen und Quellbindungen gespeichert und hashgeprüft. Die erforderlichen
weiteren Messungen und abschließenden Allmodell-Rankings bleiben offen. Die
private, ausdrücklich unvollständige Paperableitung ist gebaut und reproduziert;
das kompakte Rohbelegpaket wird als privater Offline-Checkpoint abgeschlossen. Fehlende Werte bleiben NA;
die unveränderte relative Fünf-Prozent-Qualityregel wird nicht als strengere
Nichtunterlegenheitsregel ausgegeben. 1.000 Wiederholungen desselben Bildes sind
keine 1.000 verschiedenen Bilder oder unabhängigen Sitzungen.

Die integrierte Generic-Dauererweiterung ist mit 182 Kandidatentests, zehn
unabhängigen Reviewproben und 36 Worktree-/Bundleprüfungen belegt. Diese
überlappenden Läufe werden nicht addiert und ersetzen keine Hardwaremessung.
Der aktuelle Review-Snapshot umfasst 80 geänderte Quell-/Testdateien; der
ursprüngliche 223-Dateien-DUT-Freeze bleibt für seine Kohorten verbindlich.
Die sechs alten DX/H10-Performancekohorten bleiben gültig. Sechs begrenzte
neue Bestätigungen sind ausschließlich für die normale Preflightzulassung
der reparierten Energie-Runtime vorbereitet; alte Reports werden nicht neuversiegelt.
