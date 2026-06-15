#!/usr/bin/env bash
set -Eeuo pipefail

echo "[check] Running lightweight repository checks..."

bash scripts/doctor.sh

if command -v python3 >/dev/null 2>&1; then
  echo "[check] Validating JSON schemas are parseable..."
  python3 - <<'PY'
import json
from pathlib import Path

for path in sorted(Path("packages/schemas/json").glob("*.json")):
    with path.open("r", encoding="utf-8") as f:
        json.load(f)
    print(f"[check] json ok: {path}")
PY
else
  echo "[check] python3 not found; skipping JSON parse check"
fi

echo "[check] done"
