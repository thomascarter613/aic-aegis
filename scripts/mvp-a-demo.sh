#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH="${PYTHONPATH:-}:services/runtime" python -m aegis_mvp_a "$@"
