# Visual review — 14 October 2026

PASS. The seven numerical `04_tradeoff_<model>` PNGs were inspected, including
ResNet's four-point DeepX front and YOLO26m's four-point H8 front. RegNet,
ResNet and YOLO26m were also compiled at a seven-inch manuscript width and
viewed as rendered PDF pages. Trade-off labels and ticks are 7.7 pt at that
width, axis labels 8.4 pt and titles 9.1 pt. No selected observations are cut
off and the targeted labels do not overlap. Text offsets move labels only.

The final standalone asset previews were extracted and compiled twice using
pdfLaTeX. MLSys has nine pages; Dissertation has 23. Logs contain no overfull
boxes, undefined commands or unresolved references. The compiled RegNet page
(MLSys page 6), unchanged dataset-quality page (MLSys page 8), and YOLO26m
page (Dissertation page 11) were viewed. Final RegNet was checked again after
the vector colorbar cell-edge fix. Colorbar seams are absent.

RegNet correctly has one common-front point in each setup and no front line.
All seven figures show Native, Generic and both Full alternatives. Quality
uses the selected numeric metric on one scale per model, with distinct Top-1
and COCO mAP labels. Front outlines and straight connections describe observed
coordinates only; no smoothed curve or inferred intermediate deployment is
shown. The export and independent checker establish exact point identities,
coordinates, front flags, counts and F/E annotations.

Every new trade-off PDF was inspected for embedded image objects and every
SVG for image elements: none are present, including the colorbars. PNGs are
numerical Matplotlib previews. No generative image is used as data or output.
All 42 pre-existing non-trade-off PDF/SVG/PNG files, including the quality
figures, remain byte-identical to baseline `fc57876b0a6ba69e90723e3a9209b72b36cbaa51`.

[LaTeX evidence](LATEX_ASSET_CHECK.json) records archive hashes, pages and
review locations; [independent evidence](INDEPENDENT_CHECK.json) records all
21 fronts. Compiled preview PDFs and logs are retained in the local analysis
archive alongside the public package. No private manuscript was modified.
