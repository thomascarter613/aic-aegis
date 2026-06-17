#!/usr/bin/env bash
set -euo pipefail
HOST="${MVP_A_API_HOST:-127.0.0.1}"
PORT="${MVP_A_API_PORT:-8080}"
EVIDENCE_ROOT="${MVP_A_EVIDENCE_ROOT:-.aic/runtime/evidence}"
PYTHONPATH="${PYTHONPATH:-}:services/runtime" \
  python -m aegis_mvp_a.api_server --host "$HOST" --port "$PORT" --evidence-root "$EVIDENCE_ROOT"
