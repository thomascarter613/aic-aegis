---
title: MVP-A Local Proof Loop
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-003
last_updated: 2026-06-16
---

# MVP-A Local Proof Loop

> **Core law:** The model proposes; the platform disposes.

## Purpose

This document describes the local proof-loop skeleton emitted by WP-E1-003.

## Demo Paths

```bash
bash scripts/mvp-a-demo.sh safe
bash scripts/mvp-a-demo.sh risky
bash scripts/mvp-a-demo.sh risky --approve
bash scripts/mvp-a-demo.sh blocked
```

## Expected Results

- `safe`: internal mock-safe action receives `mock` disposition and executes through the mock tool adapter.
- `risky`: customer-facing action receives `approval_required` disposition and does not execute until approved.
- `risky --approve`: customer-facing action is approval-gated, approved, then mock-executed.
- `blocked`: sensitive-data action receives `block` disposition and never executes.

## Evidence Output

Evidence is written under:

```text
.aic/runtime/evidence/
```

Evidence includes Run, Event, Proposal, Tool Action, Policy Check, Approval where applicable, Timeline, and manifest records.

## Boundary Guarantee

The local proof loop does not use a live model, real external tool, production connector, database, queue, UI, memory store, eval engine, feedback system, or business outcome system.
