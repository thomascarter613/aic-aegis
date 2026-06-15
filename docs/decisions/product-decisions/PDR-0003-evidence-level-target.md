# PDR-0003 — MVP Targets Evidence Level 2

Status: proposed  
Date: 2026-06-15  

## Context

Aegis is evidence-first, but evidence can have different maturity levels. Building audit-grade evidence in MVP would slow delivery.

## Decision

MVP targets **Evidence Level 2 — Operational Evidence**.

| Level | Name | Description |
|---|---|---|
| 0 | None | No evidence |
| 1 | Basic | run ID, input ref, output ref, timestamps |
| 2 | Operational | events, model calls, tool calls, policy decisions |
| 3 | Governance | approvals, memory refs, evals, redaction, outcomes |
| 4 | Audit-grade | hashes, signed exports, immutable retention |
| 5 | Regulated-grade | strict retention, WORM, legal hold, attestations |

## Reasons

Evidence Level 2 is sufficient to prove what happened, what tool was proposed, what policy decided, what was blocked, and what output was produced.

## Consequences

MVP evidence should be useful and readable but not overbuilt. v1 should target Evidence Level 3.

