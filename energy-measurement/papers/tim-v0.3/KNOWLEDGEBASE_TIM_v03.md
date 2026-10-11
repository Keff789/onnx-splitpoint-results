# TIM — verbindlicher Anschlussstand v0.3, 09.10.2026

## Publikations- und Schreibprinzip

Die TIM-Arbeit ist eine technisch erweiterte und eigenständig vollständige
Journalfassung. Sie setzt weder die Lektüre des PARMA-Manuskripts noch die des
Artefakts voraus, um den wissenschaftlichen Gedankengang zu verstehen.

Die bisherige Vorgabe, Jetson im Journal nur als knappen Referenzblock zu führen,
ist durch die Nutzerentscheidung aufgehoben. Es gibt keinen Zwang, auf zehn
IEEE-Seiten zu verkürzen. Der Recap gehört ins Journal und wird klar als
übernommene Grundlage zugeordnet, nicht als neuer technischer Beitrag verkauft.

Der Stil bleibt: Befund, Bedeutung, notwendige Einschränkung. Methoden verständlich
erklären; volle Koeffizienten, Quellpfade und Zusatzprüfungen ins Artefakt. Keine
historische Entstehungs-/Reparaturgeschichte im Hauptpaper. Keine überfüllten
Perzentilklammer-Tabellen für die Messpfadvergleiche.

## Aktuelle Struktur

Messdesign und vollständige Methoden führen zu vier Forschungsfragen:

1. RQ1: Abtastrate und Integrationsdauer für Energie; vollständiges Jetson-Fundament.
2. RQ2: Energie versus Fluktuationen; FP16, Messpfadbandbreite und Hailo-Spektren.
3. RQ3: Eingesetzte Messverfahren auf Jetson und Hailo; DC, Telemetrie, skalierte AC-
   Beobachtung; Energie, Leistung und tatsächliche Intervallspanne gemeinsam.
4. RQ4: Ausführungsdauer, direkte Sweeps, Reihenfolge und Anfangszustand.

Hailo bleibt aus PARMA heraus und ist Bestandteil der Journalerweiterung.
Die geplanten zusätzlichen GPU-Messungen erweitern dieses Fundament weiter.
Sie werden nicht als fertig behauptet und nicht durch erfundene Werte ersetzt.

## Ergebnisentscheidungen unverändert

- Native 5-MS/s-Scope-Rekonstruktion: sechs Workloads, 59 Ausführungen / 118 Spuren.
- Feste 2 kS/s bestehen 1 % bei den getesteten 2/5/10 s; 10 s bestehen auch 0,5 %.
  Bei 2 s beträgt das persistente 1-%-Minimum dennoch 16 kS/s.
- Alle 15 FP16-Aufzeichnungen; 64 Offsets und 960 numerische Fälle je Energierate.
- FP16-Spektren: all-15, matched_4s_4s; 125/160 kS/s erfüllen 95/99 % Abdeckung,
  ohne Behauptung einer ungetesteten Minimalrate.
- Mediane individueller Paarabweichungen; keine Quotienten von Gruppenmedianen.
- Bei 300 s: 105 Jetson- und 45 Hailo-Ausführungen, insgesamt 450 Komparatorpaare.
- Keine nachträgliche günstige Fensterauswahl oder Neuanpassung der Skalierungen.
- AC/Karten-Differenz ist keine isolierte Gerätegenauigkeit oder gemessene Hostquote.

## Zugeordnete Vorarbeit und technische Erweiterung

Die Intro nennt die PARMA-Autorenfassung und Wachsmuths Masterarbeit als Quellen.
Eine knappe Erklärung des Zusammenhangs genügt; keine wiederholte Anleitung,
zum Verständnis erst das andere Paper zu lesen. Die separate Erweiterungsliste
unterscheidet vorhandene zusätzliche Befunde und noch geplante Untersuchungen.
PARMA wird bis zur tatsächlichen Publikation nicht als Proceedings-Beitrag mit
erfundener DOI ausgegeben. Für die spätere Einreichung werden der dann finale
Konferenzbeitrag, Zitation, Rechte und technische Erweiterungen abgeglichen.

## Liefer- und Arbeitsstand

Geprüfte lokale Fassung: 13 IEEE-Seiten inklusive Literatur, zehn Abbildungen,
vier Tabellen; unveränderte Schrift und Geometrie. Datenverzeichnis unverändert
gegenüber v0.2. Der komplette Ergebnisexport-Neuaufbau und der schlanke Build sind
getrennt geprüft. Keine neue Rohdatenrechnung und kein neuer Hardwarelauf.

Die offenen GPU-, Hailo-Ausführungs-, Same-Trace-, Host-/Burst-/Telemetriefragen
stehen in `TIM_ARBEITSSTAND_UND_OFFENE_EVIDENZ.md`. Nicht alle früheren Ideen sind
stillschweigend Pflicht: neue Claims benötigen entsprechende Evidenz.
Der bestehende PARMA-Freeze bleibt unangetastet. Diese Lieferung aktualisiert
lokale Knowledgebase- und Manuskriptdateien; kein TIM-Online-Commit, Release,
Zenodo-Deposit oder Submission wurde vorgenommen.
