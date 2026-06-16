#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH="${PYTHONPATH:-}:services/runtime" python -m unittest discover -s services/runtime/tests -p "test_*.py"
