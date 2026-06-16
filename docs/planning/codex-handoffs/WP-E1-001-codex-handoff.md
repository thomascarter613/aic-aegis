---
title: Codex Handoff — WP-E1-001 MVP-A Implementation Plan
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-001
last_updated: 2026-06-16
---

# Codex Handoff — WP-E1-001 MVP-A Implementation Plan

> **Core law:** The model proposes; the platform disposes.

## 1. Mission

Implement the MVP-A Proof Loop for AIC Aegis as a local-first, headless, API-first, mock-safe control-plane slice.

Do not build a broad platform. Do not build MVP-B. Do not use real customer data. Do not send real emails. Do not mutate real external systems.

## 2. First Instruction to Codex

```text
You are implementing AIC Aegis MVP-A Proof Loop.

Preserve the core law: The model proposes; the platform disposes.

First inspect the repository. Identify existing service, script, test, policy, and docs conventions. Do not overwrite existing work. Then implement the smallest local-first modular service that can demonstrate:

1. create Run;
2. record Run Events;
3. deterministic mock model proposes Tool Action;
4. Proposal is captured;
5. Tool Broker receives Proposal;
6. Policy Check evaluates Tool Action;
7. platform applies allow/mock/block/approval_required Disposition;
8. safe action is mock-executed or risky action is blocked/approval-gated;
9. Evidence Pack manifest is generated;
10. Run Timeline is visible.

Keep domain/application/adapters/interfaces boundaries. Domain must not depend on framework, database, model SDK, cloud SDK, queue, or tool SDK. Mock tool execution must only occur through the Tool Broker. Policy Check must occur before mock execution. MVP-A must not depend on memory, evals, feedback, or business outcomes.
```

## 3. Required Files to Read First

- `docs/product/product-charter.md`
- `docs/glossary/system-glossary.md`
- `docs/architecture/architecture-doctrine.md`
- `docs/architecture/aegis-laws.md`
- `docs/architecture/system-overview.md`
- `docs/architecture/architecture-fitness-functions.md`
- `docs/governance/control-catalog.md`
- `docs/governance/risk-register.md`
- `docs/product/mvp-strategy.md`
- `docs/planning/work-packets/WP-E0-004-mvp-system-boundaries.md`
- `docs/decisions/adr/README.md`
- `docs/planning/work-packets/WP-E1-001-mvp-a-implementation-plan.md`

## 4. Implementation Order

1. Inspect repo structure and scripts.
2. Choose or create MVP-A service location.
3. Add domain/application/adapters/interfaces modules.
4. Implement domain records.
5. Implement application ports and use cases.
6. Implement local adapters.
7. Implement API or CLI interface.
8. Implement deterministic golden workflow demo.
9. Implement tests.
10. Run existing check/test scripts.
11. Update docs only where necessary.

## 5. Hard Constraints

- No direct model-to-tool execution.
- No tool execution before Proposal capture.
- No mock execution before Policy Check.
- No high-risk execution before approval.
- No memory writes in MVP-A.
- No eval/result/outcome implementation in MVP-A.
- No real external side effects.
- No Kubernetes or cloud requirement.
- No generic agent-framework naming when Aegis vocabulary exists.

## 6. Definition of Done

Codex is done when:

- local demo runs;
- tests pass;
- Run is created;
- Proposal is captured;
- Policy Check is recorded;
- Tool Broker Decision is recorded;
- action is mocked, blocked, or approval-gated;
- Evidence Pack manifest is generated;
- Timeline reconstructs the Run;
- docs explain how to run the demo;
- no MVP-B functionality is required.
