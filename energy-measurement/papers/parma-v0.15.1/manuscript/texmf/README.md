# Bundled LaTeX dependencies

The supplied OASIcs class and artwork are unchanged. This local tree supplies two dependencies absent from the build environment:

- `tex/generic/soul/{soul,soul-ori,soulutf8}.sty`: unmodified SOUL package files from Debian `texlive-plain-generic` 2023.20240207-1. The package README and copyright/licence notices in the files are included.
- `bibtex/bst/urlbst/plainurl.bst`: unmodified URL-aware bibliography style from Debian `texlive-bibtex-extra` 2023.20240207-1. Its README and LPPL/GPL licence texts are included alongside it.

`build.sh` adds this tree to `TEXINPUTS` and `BSTINPUTS`, retaining the TeX distribution search paths. The manuscript uses the supplied `orcid.pdf` directly, so the optional Font Awesome icons do not affect the build.
