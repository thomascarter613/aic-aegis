#!/usr/bin/env bash
set -Eeuo pipefail

echo "[dev] Starting local dependencies with docker compose..."
if command -v docker >/dev/null 2>&1; then
  docker compose up -d postgres redis opa otel-collector
  echo "[dev] local dependencies requested"
else
  echo "[dev] docker not found; install Docker or run services manually" >&2
  exit 1
fi
