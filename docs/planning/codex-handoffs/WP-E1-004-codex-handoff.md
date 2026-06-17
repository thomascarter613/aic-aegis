---
title: WP-E1-004 Codex Handoff
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-004
last_updated: 2026-06-16
---

# WP-E1-004 Codex Handoff

> **Core law:** The model proposes; the platform disposes.

## Mission

Add the MVP-A HTTP API and contract validation baseline.

Do not replace the WP-E1-003 application layer. The API must call the existing `AegisMvpA` application facade.

## Commands

```bash
python scripts/validate-mvp-a-contracts.py
bash scripts/test-mvp-a-api.sh
bash scripts/mvp-a-api.sh
```

## Prohibited Changes

Do not add live LLM calls, real external tools, production email, CRM mutation, database dependency, FastAPI/Flask/Django, auth, UI, or MVP-B memory/eval/feedback/outcome endpoints.
