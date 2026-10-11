#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
export TEXINPUTS="$PWD/texmf//:${TEXINPUTS:-}"
export BSTINPUTS="$PWD/texmf//:${BSTINPUTS:-}"
command -v pdflatex >/dev/null || { echo 'STOP: pdflatex fehlt.' >&2; exit 1; }
LOG="build_pdf.log"
printf 'Compiling paper.tex; log: %s\n' "$LOG"
pdflatex -interaction=nonstopmode -halt-on-error paper.tex >"$LOG" 2>&1 || { tail -60 "$LOG"; exit 1; }
if command -v bibtex >/dev/null 2>&1; then
  bibtex paper >>"$LOG" 2>&1
elif command -v bibtex.original >/dev/null 2>&1; then
  bibtex.original paper >>"$LOG" 2>&1
elif [ -s paper.bbl ]; then
  command -v sha256sum >/dev/null || { echo 'STOP: BibTeX oder sha256sum erforderlich.'; exit 1; }
  sha256sum -c metadata/BUNDLED_BIBLIOGRAPHY.sha256 >>"$LOG" 2>&1 || {
    echo 'STOP: Referenzen geändert; BibTeX für neue Bibliografie nötig.'; exit 1;
  }
  printf 'Using bundled checked paper.bbl.\n' >>"$LOG"
else
  echo 'STOP: BibTeX und mitgelieferte paper.bbl fehlen.' >&2; exit 1
fi
for pass in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error paper.tex >>"$LOG" 2>&1 || { tail -60 "$LOG"; exit 1; }
done
if grep -Eq 'undefined references|Citation .* undefined|Reference .* undefined' paper.log; then
  echo 'STOP: Ungelöste Literatur-/Querverweise, siehe paper.log.' >&2; exit 1
fi
printf 'OK: paper.pdf\n'
