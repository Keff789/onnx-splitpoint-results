# Post-hoc-Analyseplan B, C und ausgewählte Gegenfälle F

Festgehalten am 04.10.2026 vor neuen Detailrechnungen. Dies ist explorative Planung nach Kenntnis der publizierten Zusammenfassung, keine Präregistrierung oder Hold-out-Auswahl.

Die unveränderten kompakten Eingaben des gemeinsamen Abschlusses sind die Datenbasis. B verwendet exakt Modell, Setup, Richtung, Precision, Vergleichsbackend, Completed-Endpunkt und Messgrenze als Stratum. Basis und augmentierte Vereinigung bleiben getrennt. Technical verlangt das bestehende technische Gate; qualitytransfer zusätzlich das bestehende Qualitytransfer-Gate; reference_close zusätzlich beide vorhandenen reference_close-Entscheidungen. Alle Gruppen einschließlich unzureichender n bleiben sichtbar.

Primär werden Spearman, Kendall tau-b, Paar-Konkordanz, Top1, Durchsatzverlust L_R=1-R_selected/R_best und Kapazitätsregret L_C=R_best/R_selected-1 aus den drei-Wiederholungsmedianen berechnet. Vorhandene reine Rangfunktionen, exakte Gleichheit für Ties und die vorhandene stabile Eingabereihenfolge werden beibehalten. Gleich gute Native-Maxima gelten zusätzlich in einer expliziten tie-aware Ansicht als Treffer. Für n>=4 werden k=2 und k=3 gegen die exakte Erwartung gleichwahrscheinlicher k-Teilmengen ohne Zurücklegen verglichen (Treffer und erwarteter bester L_R/L_C). Kein Monte-Carlo-Lauf.

Sensitivität: alle neun Kombinationen bestehender Generic-/Native-Wiederholungen; diese sind abhängige Rekombinationen, keine neun Studien oder Konfidenzintervalle. Alle exakten Generic-Top-Ties werden hinsichtlich möglichem L_R/L_C ausgewiesen. Deskriptive Gruppensummen werden zusätzlich ohne die bereits berichteten RegNet/H10-, ResNet/H10- und YOLOv7/H8-Gegenfälle gerechnet, ohne Fälle aus der Hauptansicht zu löschen. Keine gepoolte Korrelation.

C vergleicht historische Raw-Output- und neue Completion-Proxies nur auf identischen Basisfallidentitäten; zwölf kurze Vorläufe bleiben ausgeschlossen. Endpunktunterschied und nicht kontrollierte Zeit-/Thread-/Thermikbedingungen verhindern eine rein kausale Zuschreibung an Postprocessing. Vorhandene Rohproxywerte werden gegen generic_raw.csv exakt gejoint und geprüft.

F dokumentiert für die drei genannten Gegenfälle und positive/null Gegenbeispiele Counts, Makespans, drei FPS-Werte und gespeicherten Native-Runnerpfad aus kompakten Belegen. Input-, Queue-/Inflight-, Thread-/Thermikdetails bleiben unbekannt, soweit sie nicht gezielt aus vorhandenen Originalbelegen nachgewiesen werden. Keine neue Messung oder Ausführung historischer Pakete. Die historische Full-Attestorquellenlücke betrifft keine Split-vs-Split-Rangmetrik; es werden keine Fullreferenzen eingesetzt.

Gezielte neue Tests prüfen Regretnenner, deterministische Ties, analytische Random-Shortlist-Erwartung einschließlich Native-Ties, exakte Joinidentitäten und bestehende negative Gates. Deterministische Offline-Reproduktion wird separat geprüft.
