# Evidence nach Fragestellung

[Gesamtkatalog](../CATALOG.md) · [Projektstart](../README.md)

- [Energie-Rekonstruktion](reconstruction/README.md) — Native Scope-Rekonstruktion, Dauer/Ratenentscheidungen und FP16-Energie. Zwischenverarbeitung auf 1 MS/s ist eine Sensitivitätsprüfung, keine zweite Hauptauswertung.
- [Spektren und Messbandbreite](spectra/README.md) — FP16, Jetson-/Hailo-Spektren und Messpfadvergleiche. Spektrale Varianz ist nicht Energie; mehrere Estimatoren und Kohorten bleiben getrennt.
- [Vergleich der Messverfahren](measurement-comparison/README.md) — Gepaarte DC-, u.RECS-, Telemetrie- und skalierte AC-Beobachtungen. Mediane individueller Paarabweichungen; eigene Fenster und elektrische Grenzen bleiben erhalten.
- [Dauer und Ausführungskontrollen](protocol-controls/README.md) — Direkte Sweeps, Benchmarkdauer, Fensterdefinition, Reihenfolge und Pausen. Physische Wiederholungen sind kein isolierter Samplingtest.

Unter jedem Thema: `figures/` für Vorschauen/Formate, `tables/` für Tabellen und Plotinputs, `sources/` für zusammengehörige unveränderte Pakete. Keine zweite unkontrollierte Kopie der Ergebnisdateien.
