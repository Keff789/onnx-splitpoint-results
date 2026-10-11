"""Explicit layout and semantic grouping; numerical files are never edited."""
from pathlib import PurePosixPath

VERSION = '1.0.0'
EXPECTED_ENERGY_TREE = 'a4ea6ff7c4659d80890028f021355b47fa4d66c6'
REVIEWED_COMMIT = '85eb488587a51659239c45d966f930f7c7b72a6e'
REPOSITORY = 'Keff789/onnx-splitpoint-results'
DEFAULT_BRANCH = 'energy/reorganize-20261009'
E = 'energy-measurement'
TIM = E + '/papers/tim-v0.3'
PARMA = E + '/papers/parma-v0.15.1'
MOVES = {
    E+'/2026-10-09-offline-robustness': E+'/evidence/reconstruction/sources/offline-robustness-2026-10-09',
    E+'/PSD_Analysis_journal_documentation_artifacts': E+'/evidence/spectra/sources/journal-psd',
    E+'/PSD_Analysis_multi_workload_documentation_artifacts': E+'/evidence/spectra/sources/multi-workload-psd',
    E+'/2026-09-30-offline-windows': E+'/evidence/measurement-comparison/sources/offline-windows-2026-09-30',
    E+'/publications/parma-v0.15.1': E+'/evidence/measurement-comparison/sources/parma-figure5-v0.15.1',
    E+'/2026-09-29-jetson-window-pause': E+'/evidence/protocol-controls/sources/window-pause-2026-09-29',
    E+'/2026-10-01-controlled-rate-test': E+'/evidence/protocol-controls/sources/controlled-rate-2026-10-01',
    E+'/Ergebnisse_Joris': E+'/archive/original-exports/Ergebnisse_Joris',
    E+'/Energy_Paper_TIM_KnowledgeBase_2026-09-30.md': E+'/knowledgebase/history/Energy_Paper_TIM_KnowledgeBase_2026-09-30.md',
    E+'/Energy_Paper_TIM_KnowledgeBase_CURRENT_2026-10-01.md': E+'/archive/navigation-before-20261009/Energy_Paper_TIM_KnowledgeBase_CURRENT_2026-10-01.md',
    E+'/README.md': E+'/archive/navigation-before-20261009/energy-README.md',
}
THEMES = {
    'reconstruction': ('Energie-Rekonstruktion', 'Native Scope-Rekonstruktion, Dauer/Ratenentscheidungen und FP16-Energie. Zwischenverarbeitung auf 1 MS/s ist eine Sensitivitätsprüfung, keine zweite Hauptauswertung.'),
    'spectra': ('Spektren und Messbandbreite', 'FP16, Jetson-/Hailo-Spektren und Messpfadvergleiche. Spektrale Varianz ist nicht Energie; mehrere Estimatoren und Kohorten bleiben getrennt.'),
    'measurement-comparison': ('Vergleich der Messverfahren', 'Gepaarte DC-, u.RECS-, Telemetrie- und skalierte AC-Beobachtungen. Mediane individueller Paarabweichungen; eigene Fenster und elektrische Grenzen bleiben erhalten.'),
    'protocol-controls': ('Dauer und Ausführungskontrollen', 'Direkte Sweeps, Benchmarkdauer, Fensterdefinition, Reihenfolge und Pausen. Physische Wiederholungen sind kein isolierter Samplingtest.'),
}
# Exact TIM figure names are verified against the supplied source package at runtime.
FIGURE_THEMES = {
    'hailo_ac_context': 'measurement-comparison', 'hailo_variable_intervals': 'measurement-comparison',
    'hailort_duration': 'measurement-comparison', 'jetson_rate_duration': 'reconstruction',
    'jetson_foundation_energy': 'reconstruction', 'fp16_energy': 'reconstruction',
    'fp16_energy_standalone': 'reconstruction',
    'fp16_coverage': 'spectra', 'fp16_variance_coverage': 'spectra',
    'native_spectral_comparison': 'spectra', 'native_cdf_difference': 'spectra',
    'hailo_spectra': 'spectra', 'hailo_spectral_tails': 'spectra',
    'device_pair_medians': 'measurement-comparison', 'measurement_boundaries': 'measurement-comparison',
    'jetson_meters': 'measurement-comparison', 'jetson_device_medians': 'measurement-comparison',
    'hailo_dc_telemetry': 'measurement-comparison', 'hailo_ac_boundary': 'measurement-comparison',
    'hailo_telemetry_duration': 'measurement-comparison', 'hailo_interval_contrast': 'measurement-comparison',
    'hailo_interval_comparison': 'measurement-comparison', 'hailo_duration': 'protocol-controls',
    'duration_dependence': 'protocol-controls', 'jetson_duration': 'protocol-controls',
    'pause_runtime': 'protocol-controls', 'scope_native_energy': 'reconstruction',
}
TABLE_THEMES = {
    'jetson_reference': 'reconstruction', 'jetson_foundation_energy': 'reconstruction',
    'native_reconstruction': 'reconstruction', 'fp16_energy': 'reconstruction', 'fp16_energy_plot': 'reconstruction',
    'fp16_coverage': 'spectra', 'fp16_coverage_plot': 'spectra', 'native_spectral_comparison': 'spectra', 'hailo_spectra': 'spectra',
    'paired_300s': 'measurement-comparison', 'jetson_paired_300s': 'measurement-comparison',
    'paired_summary': 'measurement-comparison', 'paired_all_durations': 'measurement-comparison',
    'hailo_variable_interval_comparison': 'measurement-comparison',
    'direct_repeatability': 'protocol-controls', 'hailo_repeatability': 'protocol-controls',
    'direct_rates': 'protocol-controls', 'controlled': 'protocol-controls', 'controlled_effects': 'protocol-controls',
    'duration': 'protocol-controls', 'jetson_duration': 'protocol-controls', 'pause_timing': 'protocol-controls',
}

def mapped(path, moves):
    for old, new in sorted(moves.items(), key=lambda item: -len(item[0])):
        if path == old or path.startswith(old+'/'):
            return new + path[len(old):]
    return path

def topic_for(path, fallback='protocol-controls'):
    p = PurePosixPath(path); stem = p.stem.lower()
    explicit = FIGURE_THEMES.get(stem) or TABLE_THEMES.get(stem)
    if explicit:
        return explicit
    if any(x in path.lower() for x in ('/common_reference/', '/energy_reconstruction/', '/f_min_', '/highlighted_rate_thresholds.')):
        return 'reconstruction'
    if any(x in path.lower() for x in ('/direct_rate_validation/', '/controlled', '/window_sensitivity')):
        return 'protocol-controls'
    for topic in THEMES:
        if '/evidence/'+topic+'/' in path:
            return topic
    if any(x in stem for x in ('paired','device','meter','telemetry','boundary','interval_contrast')):
        return 'measurement-comparison'
    if any(x in stem for x in ('spectr','coverage','variance','cdf','psd','band')):
        return 'spectra'
    if any(x in stem for x in ('reconstruct','fp16_energy','foundation_energy','scope','fmin','f_min','two_k')):
        return 'reconstruction'
    return fallback

TIM_LABELS = {
 'measurement_boundaries': 'Abb. 1 — Elektrische Messgrenzen',
 'jetson_rate_duration': 'Abb. 2 — Jetson: Energiefehler und Integrationsdauer',
 'fp16_energy_objective': 'Abb. 3a — FP16: Energieintegration',
 'fp16_fluctuation_coverage': 'Abb. 3b — FP16: Fluktuationsabdeckung',
 'native_cdf': 'Abb. 4 — Spektraler Vergleich der Messpfade',
 'hailo_spectral_tail': 'Abb. 5 — Hailo: spektrale Verteilung',
 'jetson_deployed_meters': 'Abb. 6 — Jetson: reale Messverfahren',
 'hailo_dc_telemetry': 'Abb. 7a — Hailo: DC und Telemetrie',
 'hailo_ac_context': 'Abb. 7b — Hailo: AC-Beobachtung',
 'hailort_duration': 'Abb. 8a — HailoRT über der angeforderten Dauer',
 'hailo_variable_intervals': 'Abb. 8b — Variable YOLO: Energie, Leistung und Spanne',
 'jetson_duration': 'Abb. 9a — Jetson: Benchmarkdauer',
 'hailo_duration': 'Abb. 9b — Hailo: Benchmarkdauer',
 'pause_runtime': 'Abb. 10 — Pausen und Ausführungszeit',
 'jetson_reference': 'Tab. II — Jetson: neun Energieintervalle',
 'direct_repeatability': 'Tab. III — Direkte Ratensweeps beider Plattformen',
 'controlled': 'Tab. IV — Kontrollierter Festarbeitsvergleich',
}
