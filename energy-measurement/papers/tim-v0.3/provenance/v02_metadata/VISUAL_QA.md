# Visual inspection — TIM v0.2

The final 10-page PDF was rendered at 108 dpi and reviewed page by page, with
full-page checks of the first-page title/abstract, Related Work, boundary
figure, cohort/methods table, both deployed-meter figures, spectral figures,
Hailo duration plot, controls and references. No clipped plot labels, overlaps,
missing glyphs or overfull text boxes were found. Tiny reference-URL line breaks
produce underfull justification warnings, not missing citations.

Figures 2 and 3 each combine two separately generated charts. Their captions
state the separate axes and, where applicable, different horizontal scales.
The 300-s comparison shows medians; complete pair quantiles remain in CSV.
The spectral and duration ranges are empirical fifth–95th percentiles,
not confidence intervals. The control table's bounds are the different,
explicitly model-based 95% t intervals.

The final clean-source and full-package builds have identical extracted text
and identical page pixels at 108 dpi on all ten pages. This is a document
consistency test; it does not validate unprovided raw measurements.
