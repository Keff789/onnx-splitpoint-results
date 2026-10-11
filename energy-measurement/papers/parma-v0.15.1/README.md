# PARMA manuscript and compact evidence – 0.15.1

`manuscript/paper.pdf` is the author working version. `manuscript/` is independently
compilable. Figure 5 replaces the former percentile table with 21 paired medians.
The 315 pair rows, complete spread summaries and the plot generator are included
here. To redraw this figure, run `python3 scripts/make_device_comparison.py` after
creating `figures/`. The complete result-export inputs and full regeneration
pipeline are supplied as the separate `PARMA_v0151_Quellenpaket.zip` release asset;
this compact directory alone does not reproduce every analysis.

The intended release tag is `parma-v0.15.1`. The source-results commit remains
`9b4208c97420b1621a14b7dc91f051985e65e6f5`. No DOI, acceptance, new measurement
campaign, sensor-interchangeability claim or universal hardware accuracy is implied.
See `release_assets.json` for the exact assets and checksums and the linked
[knowledgebase update](../../knowledgebase/2026-10-09-parma-v0151.md).
