#!/usr/bin/env bash
set -Eeuo pipefail

echo "[doctor] Checking AIC Aegis scaffold..."

required_paths=(
  "README.md"
  ".aic/metadata/project.yaml"
  "PROJECT_INDEX_ENTRY.yaml"
  "docs/product/WP-E0-001-product-charter.md"
  "docs/adrs/README.md"
  "docs/planning/epics/README.md"
  "docs/planning/work-packets/README.md"
  "packages/schemas/json/run-envelope.schema.json"
  "packages/schemas/json/evidence-pack.schema.json"
  "packages/policy-packs/base/tool_policy.rego"
  "packages/tool-packs/email.send.yaml"
  "db/migrations/0001_initial_core.sql"
  "docker-compose.yml"
)

missing=0
for path in "${required_paths[@]}"; do
  if [[ ! -e "$path" ]]; then
    echo "[doctor] missing: $path" >&2
    missing=1
  else
    echo "[doctor] ok: $path"
  fi
done

if [[ "$missing" -ne 0 ]]; then
  echo "[doctor] failed"
  exit 1
fi

echo "[doctor] scaffold looks good"
