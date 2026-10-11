#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
PYTHON=${PYTHON:-python3}
"$PYTHON" scripts/generate_results.py
"$PYTHON" scripts/make_figures.py
"$PYTHON" scripts/make_foundation_figures.py
"$PYTHON" scripts/verify_results.py
bash build.sh
printf '%s\n' 'PASS: numerical export reconstruction, independent audit and manuscript build.'
