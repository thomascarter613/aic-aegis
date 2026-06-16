---
title: WP-E1-002 Codex Handoff
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-002
last_updated: 2026-06-16
---

# WP-E1-002 Codex Handoff

> **Core law:** The model proposes; the platform disposes.

## 1. Mission

Use this packet to implement the MVP-A domain model and schema baseline.

Do not build the full application yet. Establish the domain and contract foundation for the MVP-A Proof Loop.

## 2. Required Inputs

Read:

- `docs/planning/work-packets/WP-E1-002-mvp-a-domain-model-and-schema-baseline.md`
- `docs/implementation/mvp-a/domain-model.md`
- `docs/implementation/mvp-a/domain-invariants.md`
- `docs/implementation/mvp-a/event-catalog.md`
- `docs/implementation/mvp-a/command-query-catalog.md`
- `contracts/schemas/mvp-a/*.schema.json`

## 3. Implementation Instructions

1. Preserve Clean Architecture boundaries.
2. Implement or scaffold only MVP-A objects.
3. Do not implement Memory, Feedback, Eval, or Business Outcome.
4. Do not implement real external tools.
5. Use mock-safe tool execution only.
6. Ensure Proposal exists before Tool Action disposition.
7. Ensure Policy Check exists before mock execution or block/approval disposition.
8. Ensure Evidence Pack and Timeline records can reference all relevant artifacts.

## 4. Suggested Tasks

- Add schema validation tooling if missing.
- Add a schema validation test for every schema in `contracts/schemas/mvp-a`.
- Add domain type skeletons for Actor, Run, RunEvent, Proposal, ToolAction, PolicyCheck, Approval, EvidencePack, Timeline.
- Add enum definitions matching `enums.schema.json`.
- Add invariant tests for proposal-before-disposition and policy-before-effect.
- Add README notes describing MVP-B exclusions.

## 5. Acceptance Tests

Minimum tests:

1. All JSON schemas parse successfully.
2. A valid sample Run passes schema validation.
3. A valid sample Proposal passes schema validation.
4. A valid sample Tool Action references a Proposal ID.
5. A valid sample Policy Check references Proposal and Tool Action IDs.
6. A high-risk policy output uses `approval_required` or `block`.
7. Timeline schema supports ordered items.
8. Evidence Pack schema supports artifact references.

## 6. Prohibited Changes

Do not:

- add production connector code;
- add real email sending;
- add real CRM mutation;
- add Kubernetes manifests for MVP-A;
- add enterprise SSO;
- add billing;
- add memory/eval/outcome dependencies to MVP-A;
- rename Aegis domain terms to generic agent terms.

## 7. Expected Result

After this handoff is implemented, the repository should have a validated domain/schema baseline ready for:

**WP-E1-003 — MVP-A Code Skeleton and Local Proof Loop**
