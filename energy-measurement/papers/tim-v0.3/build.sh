#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
command -v pdflatex >/dev/null || { echo 'STOP: pdflatex is required.' >&2; exit 1; }
export SOURCE_DATE_EPOCH=1791504000
export FORCE_SOURCE_DATE=1
LOG=build.log
pdflatex -interaction=nonstopmode -halt-on-error main.tex >"$LOG" 2>&1 || { tail -60 "$LOG"; exit 1; }
if command -v bibtex.original >/dev/null 2>&1; then
  bibtex.original main >>"$LOG" 2>&1
elif command -v bibtex >/dev/null 2>&1; then
  bibtex main >>"$LOG" 2>&1
elif [ -s main.bbl ]; then
  sha256sum -c metadata/BIBLIOGRAPHY.sha256 >>"$LOG" 2>&1
else
  echo 'STOP: BibTeX or the bundled bibliography is required.' >&2; exit 1
fi
for pass in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error main.tex >>"$LOG" 2>&1 || { tail -60 "$LOG"; exit 1; }
done
if grep -Eq 'undefined references|Citation .* undefined|Reference .* undefined' main.log; then
  echo 'STOP: unresolved references.' >&2; exit 1
fi
echo 'OK: main.pdf'
