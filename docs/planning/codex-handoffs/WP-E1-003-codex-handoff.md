---
title: WP-E1-003 Codex Handoff
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-003
last_updated: 2026-06-16
---

# WP-E1-003 Codex Handoff

> **Core law:** The model proposes; the platform disposes.

## 1. Mission

Apply the MVP-A code skeleton and verify the local Proof Loop.

This packet intentionally uses Python stdlib only. Do not introduce external dependencies unless a later ADR/work packet accepts them.

## 2. Files to Add

Add:

```text
services/runtime/aegis_mvp_a/
services/runtime/tests/test_mvp_a_proof_loop.py
scripts/mvp-a-demo.sh
scripts/test-mvp-a.sh
docs/planning/work-packets/WP-E1-003-mvp-a-code-skeleton-and-local-proof-loop.md
```

## 3. Commands

Run:

```bash
bash scripts/test-mvp-a.sh
bash scripts/mvp-a-demo.sh safe
bash scripts/mvp-a-demo.sh risky --approve
bash scripts/mvp-a-demo.sh blocked
```

## 4. Required Behavior

The implementation must show:

- Run created before Proposal;
- Proposal captured before Tool Broker disposition;
- Policy Check created before mock execution or block;
- high-risk action requires approval;
- blocked action does not execute;
- Evidence Pack generated;
- Timeline reconstructable.

## 5. Prohibited Scope

Do not add:

- live LLM calls;
- real tool connectors;
- real email sending;
- CRM mutation;
- database dependency;
- web server dependency;
- MVP-B memory/eval/feedback/outcome implementation.

## 6. Expected Next Step

After this skeleton passes, proceed to:

**WP-E1-004 — MVP-A HTTP API and Contract Validation**
