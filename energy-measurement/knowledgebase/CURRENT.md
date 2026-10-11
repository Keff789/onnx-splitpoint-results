# Energy Paper — aktueller verbindlicher Projektstand

Stand: 09.10.2026. Dieser Einstieg konsolidiert die letzten Nutzerentscheidungen. Ältere datierte Texte sind Provenienz, keine konkurrierenden aktuellen Arbeitsaufträge.

## Paper und Stil

**PARMA v0.15.1** bleibt Jetson-only: Energie-Rekonstruktion, Fluktuationsabdeckung und praktische Messpfadvalidierung. Abbildung 5 zeigt 21 Paarmediane; vollständige Perzentile und 315 Paarvergleiche aus 105 Ausführungen bleiben im Artefakt.

**TIM v0.3** ist eine eigenständig vollständige technische Journalerweiterung. Das Jetson-Fundament bleibt mit Recap enthalten; die Lektüre von PARMA wird nicht vorausgesetzt. Hailo und die weiteren Mess-/Protokollvergleiche erweitern die Arbeit. Zusätzliche GPU-Messungen sind geplant, nicht bereits als finaler Datensatz bestätigt. Die frühere v0.2-Empfehlung, Jetson nur als knappen Referenzblock zu führen, ist aufgehoben.

Stil: verständliche Herleitung, Befund und Bedeutung; keine Entstehungs-/Reparaturchronik im Hauptpaper. Entscheidende Korrekturen und Aussagegrenzen bleiben dort; volle Koeffizienten, Rohpfade und Zusatzprüfungen im Artefakt.

## Verbindliche Auswertungsdefinitionen

- Native 5-MS/s-Scope-Rekonstruktion: sechs Workloads, 59 physische Ausführungen, 118 Spuren. Der 1-MS/s-Zweig bleibt Sensitivität.
- Feste 2 kS/s bestehen 1 % bei den getesteten 2/5/10 s; 10 s bestehen auch 0,5 %. Bei 2 s ist das persistente 1-%-Minimum trotzdem 16 kS/s. Kein Verwechseln von Einzelpunkt und persistentem Minimum.
- FP16: alle 15 Aufzeichnungen, 64 Offsets, 960 numerische Fälle je Energierate. 50 S/s besteht das Q95-Kriterium, nicht jeden Einzelfall; 85 S/s besteht alle getesteten Fälle.
- FP16-Spektren: all-15 / matched_4s_4s; getestete 125/160 kS/s erfüllen 95/99 % Abdeckung. Keine ungetestete Minimalrate behaupten.
- Gerätevergleich: Median individueller Paarabweichungen, nicht Quotient zweier Gruppenmediane. Sensorfenster, Skalierungen und elektrische Grenzen bleiben erhalten.
- Bei 300 s: 105 Jetson- und 45 Hailo-Ausführungen; 450 Komparatorpaare sind keine 450 unabhängigen Ausführungen.
- Direkte Sweeps: Gruppenmittel gegen gleich gewichtetes Mittel der Gruppenmittel; keine nachträgliche günstige Fensterauswahl oder Ratenkorrektur.

## Daten- und Artefaktstatus

Scope-Detailarchivierung ist seit `9b4208c` abgeschlossen. Der Umbau verändert keine Messdaten, startet keinen Collector und ersetzt kein Rohdatenbackup. Ein erfolgreicher Git-Push ist nicht gleichbedeutend mit bereitstehenden Release-Anhängen oder einer Zenodo-DOI.

[PARMA-Nachtrag](history/2026-10-09-parma-v0151.md) · [TIM-v0.3-Anschlussstand](../papers/tim-v0.3/KNOWLEDGEBASE_TIM_v03.md) · [Aktuelle Evidence](../evidence/README.md) · [Datierte Geschichte](history/README.md)

## Offen, nicht durch den Umbau erledigt

Finaler GPU-Export, Hailo-Ausführungsbindung und je nach finalem Anspruch Hailo-Same-Trace-Energieprüfung, Hostzerlegung, gematchte Bursts und dynamische Telemetrie. Neue technische Aussagen benötigen die passende Evidenz; nicht jede frühere Idee ist automatisch Pflicht. [Detaillierter TIM-Arbeitsstand](../papers/tim-v0.3/TIM_ARBEITSSTAND_UND_OFFENE_EVIDENZ.md).
