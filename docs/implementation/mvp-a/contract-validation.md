---
title: MVP-A Contract Validation
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-004
last_updated: 2026-06-16
---

# MVP-A Contract Validation

> **Core law:** The model proposes; the platform disposes.

## Purpose

Contract validation prevents API/schema drift as the MVP-A Proof Loop becomes executable.

## Command

```bash
python scripts/validate-mvp-a-contracts.py
```

## Current Constraint

This packet does not add a third-party JSON Schema validator. The script is intentionally stdlib-only so it can run locally without dependency installation.
