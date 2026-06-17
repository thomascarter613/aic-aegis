#!/usr/bin/env python3
"""Stdlib contract checks for AIC Aegis MVP-A."""
from __future__ import annotations
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
OPENAPI_PATH = ROOT / 'contracts/openapi/mvp-a.openapi.json'
SCHEMA_DIR = ROOT / 'contracts/schemas/mvp-a'
EXPECTED_SCHEMA_FILES = [
    'actor.schema.json', 'run.schema.json', 'run-event.schema.json', 'proposal.schema.json',
    'tool-action.schema.json', 'policy-check.schema.json', 'approval.schema.json',
    'evidence-pack.schema.json', 'timeline.schema.json', 'enums.schema.json'
]
FORBIDDEN_MVP_B_PATH_PARTS = ['memory', 'feedback', 'eval', 'outcome']

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        raise AssertionError(f'Invalid JSON: {path}: {exc}') from exc

def main() -> int:
    errors: list[str] = []
    if not OPENAPI_PATH.exists():
        errors.append(f'Missing OpenAPI contract: {OPENAPI_PATH}')
    else:
        openapi = load_json(OPENAPI_PATH)
        if openapi.get('openapi') != '3.1.0':
            errors.append('OpenAPI version must be 3.1.0.')
        paths = openapi.get('paths', {})
        if not paths:
            errors.append('OpenAPI contract missing paths.')
        for route in paths:
            lowered = route.lower()
            for forbidden in FORBIDDEN_MVP_B_PATH_PARTS:
                if forbidden in lowered:
                    errors.append(f'MVP-B path exposed in MVP-A contract: {route}')
        schemas = openapi.get('components', {}).get('schemas', {})
        for component in ['Run', 'Proposal', 'ToolAction', 'PolicyCheck', 'Approval', 'EvidencePack', 'Timeline']:
            if component not in schemas:
                errors.append(f'Missing OpenAPI schema component: {component}')
    for name in EXPECTED_SCHEMA_FILES:
        path = SCHEMA_DIR / name
        if not path.exists():
            errors.append(f'Missing MVP-A schema file: {path}')
            continue
        schema = load_json(path)
        if schema.get('$schema') != 'https://json-schema.org/draft/2020-12/schema':
            errors.append(f'{name} must use JSON Schema draft 2020-12.')
        if '$id' not in schema:
            errors.append(f'{name} missing $id.')
    if errors:
        for error in errors:
            print(f'ERROR: {error}', file=sys.stderr)
        return 1
    print('MVP-A contract validation passed.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
