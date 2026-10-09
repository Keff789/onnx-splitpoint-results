# Native/Generic Revision 3 — Current-Evidenz und Prüfgrenzen

Der aktuelle veröffentlichte Checkpoint steht im
[Publikationsmanifest](../results/evaluation/native_fairness_rev3_20261007/PUBLICATION_MANIFEST.json)
und den [Native-/Generic-Current-Zeilen](../results/evaluation/native_fairness_rev3_20261007/README.md).
Neue Performance, belegte historische Wiederverwendung, Datasetqualität,
Vergleichsclaims und zugelassene Energie sind getrennte Zählungen aus diesen
Zeilen. Der Ergebnisbericht und Resume beschreiben denselben Exportstichtag.
Lokale laufende oder vorbereitete Folgearbeiten sind damit noch nicht veröffentlicht.

Die geplante Sicht umfasst 246 Native-Fälle, darunter 204 Splits und 42 Fulls,
sowie 204 Generic-Fälle. Fehlende oder technisch ausgeschlossene Ergebnisse
bleiben NA. Wiederholungen eines einzelnen vorbereiteten Inputs werden nicht
als unabhängige Datasetbilder gezählt. Neue Performance verwendet drei reale
Prozesse mit jeweils 100 Warmup- und 1000 abgeschlossenen Tasks; gültige
historische Einzelbeobachtungen behalten ihren tatsächlichen ursprünglichen
Umfang, FPS und fehlende Wiederholungs-CI.

Der einzige finale Runtimefreeze ist
`8346d43d526221bd9d138943122206b658d56cbf` mit 241 Dateien. Der Controller-
Referenzreader wurde separat unter
`ec68097d0ca161a75380da158a257ad495296d90` korrigiert; seine beiden Dateien
gehören nicht zu diesen DUT-Runtime241. Tatsächliche Deploymentreceipts und
Quellbindungen stehen im Manifest. Weitere Controller-/Ops-Reportanpassungen
ändern keine eingefrorenen DUT-/Input-/Taskquellen und erfinden keine neue
Provenienz-, Registry-, Cache- oder Artefaktidentitätsschicht.

H8-Classification wurde anhand der konkreten sechs Split-/Full-HEFs, QuantInfo
und installierten SDK-Verträge geklärt: Float32-Splits verwenden einmal die
kanalweise ImageNet-Mean/Std-Normalisierung; UINT8-Vendor-Fulls den bestehenden
HEF-gebundenen SDK-Quantisierer derselben normalisierten Domäne. Detektoren
behalten ihren Vertrag. Die drei alten falsch normalisierten H8-Performance-
Beobachtungen bleiben als Historie erhalten, werden aber nicht aktuell
wiederverwendet. Regulär abgeschlossene korrigierte Vendor- und TRT-Fulls
haben normale aktuelle Qualitätsbindungen und zulässige gleiche Setup-
Vergleiche. H8-MobileNet behält ausdrücklich `accuracy_loss`.

Die enge Controllerkorrektur behandelt HEF-Quantcodes nicht als RGB-Pixel.
Sie verwendet vorhandene exakt gebundene kanonische RGB-Bytes für den normalen
CPU-Referenzfeed und lehnt fehlende oder widersprüchliche Metadaten ab.
Gespeicherte CPU-Referenzen, Logits/TopK und gültige ursprüngliche N5000-Ergebnisse
werden weiterverwendet; ein geänderter Dateihash allein löst keine Neumessung aus.
Softwaretests, tatsächliche Performance, normaler Datasetjoin und Vergleichsclaim
bleiben eigenständige Belege. Überlappende Testläufe werden nicht addiert.

Für 56 DX-Classifier-Splits ist der Datasettransfer konkret gesperrt: der Original-
N5000-Runner rekonstruiert nach ImageNet-Float32 uint8 mittels Trunkierung;
die aktuelle Runtime nimmt direkte RGB-Bytes. Ein bereits ausgeführter endlicher
Gegenbeweis unterscheidet 137 von 768 Kanalwerten um 1 LSB. Gleiche Artefakte oder
Normalisierungsnamen und drei Timingkontrollen beweisen hier keine universelle
Gleichheit. Der isolierte positive Vorabtransfer wurde nie integriert und bleibt
als ungültige Diagnose erhalten. Der enge Reporter lehnt die vorhandene
Übertragung ab; gültige aktuelle Performance und originale N5000-Daten bleiben
unverändert. [Sourcebefund](../results/evaluation/native_fairness_rev3_20261007/quality_transfer/classifier_split_preparation_20261008/DX56_N5000_INPUT_SOURCE_REVIEW.json),
[gebundene Holds](../results/evaluation/native_fairness_rev3_20261007/current_results/QUALITY_JOIN_REVIEW_HOLDS.json)
und Resume nennen den jeweils konkreten Input-/Frozen-API-Blocker und die
gezielte Readiness. Fehlende neue API-Zulassung wird nicht durch Qualityflags ersetzt.

Originale Vendor-DX/H10-Classifier-Full-Qualität kann an ihren tatsächlich
unveränderten einzelnen Performancebeobachtungen gültig bleiben. Dieser
Datasetnachweis erzeugt keine neuen drei Repeats, CI oder Performanceclaims.
Der normale gemeinsame DX-Full-Consumer unterscheidet diese Begrenzung von
aktuellen TRT-Kohorten. Für den historischen H10-Full-Kontext meldet derselbe
Consumer einen echten Konflikt zwischen expliziter physischer Raw-Attestation
und Original-V10-Marker sowie fehlendem Prepared-Tensor-Topalias. Diese Angaben
wurden nicht angeglichen. Seine Originaldatasetqualität bleibt separat gültig;
der widersprüchliche physische Kontext bleibt aus der normalen Full-Komposition.

Die aktuelle normale Qualitygeneration folgt
[CURRENT_FINALIZED.json](../results/evaluation/native_fairness_rev3_20261007/quality_transfer/CURRENT_FINALIZED.json).
Die vorhandenen Kompositions-/Reviewbelege werden für genau dessen Generation
exportiert. Sie bewahren ältere wissenschaftliche Werte, Source-/Prozess-/Input-
Bindungen und echte negative Vergleichsgates. Vollständige Qualitätsreports,
kanonische CPU-Daten und private Originale werden hier nicht dupliziert.

Energie wird ausschließlich nach der normalen Aufnahme-/Reportzulassung an
exakte aktuelle Konfigurationen angefügt. Angezeigt werden mJ/Task mittels
J/Task×1000 und separat Tasks/J als Mittel der tatsächlichen N/E-Repeats;
der Kehrwert des mittleren E/N ist eine andere Größe. Rohe Systemenergie und
bestehende Vergleichsnormalisierung bleiben getrennte Felder. Technisch zulässige
diagnostische Aufnahmen oder Offline-Reintegration sind keine neuen qualifizierten
Hardwaremessungen. Generic-Energieanschluss und Matrixprojektion sind softwareseitig
geprüft; diese Prüfung behauptet keine tatsächlich neue Generic-Sensoraufnahme.

H10s einmal konkret autorisierte Fortsetzung bestätigte Quellenabschluss und
Cleanup, wurde aber wegen 7936 fehlender Samples beziehungsweise 124 Paketen
in einem Gap innerhalb des Commandfensters abgewiesen. Diese Freigabe ist
verbraucht; kein automatischer Retry oder neuer Capture folgt daraus. Der ältere
unbestätigte Quellenabschluss bleibt unverändert negative Historie. H8-Zero-Start,
accepted-repeat-Blocker, physischer/source STOP und verbleibende Budgets stehen
im aktuellen [Resume](../results/evaluation/native_fairness_rev3_20261007/RESUME_STATE.json).
Freie Leases sind keine Aufnahmefreigabe. Normale DUT-Performance benötigt die
aktuelle Ressourcenownership und normale Plan-/Sourcezulassung.

Die historische Generic-Nutzung wurde gezielt aus vorhandenen Katalogen und
Originalreports geprüft. Raw, allgemeines Streaming, Multi-Tensor, `generic`,
`native_fifo` und `NativeTRTSession` bleiben erhalten. Ausschließlich nachweislich
tote isolierte DeepX-P2-Duplikate und Helfer wurden entfernt: 197 Zeilen mit
Originalsource-/Diffbeleg. Verlustfreier Drain, tatsächliche Counts, eindeutige
Eingabedomänen, fachliche Completion im Timer und Postflight außerhalb sind
getrennt getestet. Raw-Endpunkte werden nicht zu Completed Tasks umbenannt.

Historisches Archiv und gültige Originalergebnisse bleiben erhalten. Es gab
keine Datenlöschung, Verschiebung oder Speicherbereinigung. Gezielte Payload-,
Manifest- und benötigte Artefaktprüfungen sind keine pauschale vollständige
Inhaltsprüfung des Gesamtarchivs. Neue Messungen, negative Versuche und
Quellenkopien werden über die vorhandenen datierten Archivmechanismen gesichert.
Die private Paperableitung verwendet die aktuelle normale Sicht, zeigt fehlende
Zeilen und bleibt einschließlich sämtlicher LaTeX-Quellen außerhalb dieses Gitpayloads.
Ein abschließendes Allmodell-Ranking wird nur für die tatsächlich zugelassene
und vollständig bezeichnete Schnittmenge behauptet.


Stand 2026-10-09: Der normale Current enthält232 neue Native-Kohorten, sechs historische Singles und acht technische Full-Ausschlüsse;180 Native-Qualitybindungen,169 Claims und fünf Energiepunkte. Generic204/612 Prozesse ist vollständig exportiert:204 technische Paare,148 Quality-/Claimpaare, keine Exportfehler und keine Generic-Energie. Zwölf vorhandene H8/H10-YOLO26-Vergleiche sind über den gebundenen normalen Native-Report geschlossen. Alle192 alten Paare und sämtliche ursprünglichen numerischen Kohorten-/Prozess-/Quellenwerte bleiben unverändert. Die56 DX-Classifier-Quality-Holds bleiben ausgeschlossen.

Der bestehende Plan-Updater trennt `native` und `generic_completed`:14 falsche Fertigmeldungen sowie204 falsch übernommene Generic-Quellbindungen wurden korrigiert. Native-b044/b066 besitzt Energie; die gleichnamigen Genericfälle besitzen keine. Lokaler Cohort-Readercommit: `b7c2094e329351dcbdbeef4d3fcac48eec9458f3`; gemessener Runtimefreeze/DUTs unverändert.26 fokussierte Tests und eine überlappende Generic-STOP-Planprobe bestanden; unabhängiger Review abgeschlossen.

Energie bleibt offen:445 Matrixlücken, davon442 Delta-Fälle und drei historische H10-Screeningfälle außerhalb des Deltas.141 DX-Fälle besitzen vorbereitete Metadaten;145 Parents sind unvorbereitet,146 Fälle durch STOP, acht durch technische Bindung und zwei durch Repeat-Scope blockiert. Die nächsten14 DX-Kandidaten sind nur Metadaten-PASS; kein Parent/Capture gestartet.42 Minuten sind reine Lastzeit, keine ETA oder Freigabe. H10 benötigt neue konkrete Einzelfreigabe; alter Grant verbraucht und ursprünglicher Quellenabschluss unbekannt.

Der bestehende private Paperworkflow wurde aus Current aktualisiert;18 Tests und Haupt-/Supplement-PDF bestehen. Die Kampagne bleibt wegen Energie-/Quality-/Full-Lücken in_progress. Kleine Current-/Source-/Receiptmetadaten und der normale Archivindex sind verifiziert; vorhandene Payloads werden wiederverwendet. Kein neuer Mess-, Build-, Runtimefreeze- oder Deploymentlauf. Das begrenzte Reviewpaket ist ein Metadatenpaket und kein vollständiger Rohdatennachweis. Private LaTeX-Quellen werden nicht veröffentlicht.
