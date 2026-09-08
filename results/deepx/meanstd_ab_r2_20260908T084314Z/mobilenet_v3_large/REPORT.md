# R2 A/B – mobilenet_v3_large

- Samples: 16
- A Top-1: 11/16 = 0.688
- B Top-1: 12/16 = 0.750
- A Top-5: 15/16 = 0.938
- B Top-5: 15/16 = 0.938
- Top-1 delta B-A: +0.062
- Corrected by B: 2; regressed by B: 1
- Mean cosine A→scale_only: 0.8976414353201108
- Mean cosine A→mean/std: 0.767676197264897
- Mean cosine B→scale_only: 0.8338749761178226
- Mean cosine B→mean/std: 0.9115670230198796
- A R2 exact match to R1: 16/16
- Adapter ORT parity: pass
- Interpretation: supports_imagenet_mean_std_build_path

Diagnostic only; no model/quality/energy acceptance.
