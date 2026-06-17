---
title: WP-E1-004 — MVP-A HTTP API and Contract Validation
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-004
phase: E1
depends_on:
  - WP-E1-003
next_work_packet: WP-E1-005
last_updated: 2026-06-16
---

# WP-E1-004 — MVP-A HTTP API and Contract Validation

> **Core law:** The model proposes; the platform disposes.

> **Core doctrine:** Aegis is a Clean Architecture, domain-driven, event-rich, selectively CQRS, policy-enforced, evidence-first, headless, API-first, local-first, cloud-native-capable, enterprise-governance-grade AI Reliability Control Plane for provable AI work.

## 1. Work Packet Summary

WP-E1-004 adds a thin HTTP API and contract-validation baseline for the MVP-A Proof Loop.

This packet does not turn Aegis into a web application. It exposes the existing MVP-A application use cases through a local, stdlib-only HTTP boundary so the control plane can be exercised through machine-usable API calls.

The API must not bypass the governed path implemented in WP-E1-003:

```text
Run → Proposal → Tool Broker → Policy Check → Disposition → Approval Gate / Mock Execution / Block → Evidence Pack → Timeline
```

## 2. Objective

Create the first MVP-A API boundary and contract validation baseline.

The implementation must provide:

- local HTTP API server;
- OpenAPI contract;
- API tests;
- contract validation script;
- demo and test scripts;
- documentation and Codex handoff.

## 3. In Scope

- `services/runtime/aegis_mvp_a/http_api.py`
- `services/runtime/aegis_mvp_a/api_server.py`
- `services/runtime/tests/test_mvp_a_http_api.py`
- `contracts/openapi/mvp-a.openapi.json`
- `scripts/mvp-a-api.sh`
- `scripts/test-mvp-a-api.sh`
- `scripts/validate-mvp-a-contracts.py`

## 4. Out of Scope

- production API framework;
- FastAPI/Flask/Django;
- authentication/authorization;
- database persistence;
- queue/worker infrastructure;
- real external tool execution;
- real LLM calls;
- production email sending;
- real CRM mutation;
- UI;
- Kubernetes;
- memory/eval/feedback/outcome endpoints.

## 5. Initial Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Return API health and product identity. |
| POST | `/v1/runs` | Create a Run. |
| GET | `/v1/runs/{run_id}` | Retrieve a Run. |
| POST | `/v1/runs/{run_id}/mock-proposals` | Generate and record a mock Tool Action Proposal. |
| POST | `/v1/tool-actions/{tool_action_id}/broker` | Broker Tool Action through Policy Check and Disposition. |
| POST | `/v1/approvals/{approval_request_id}/approve` | Approve and resume approval-gated mock execution. |
| POST | `/v1/runs/{run_id}/evidence-packs` | Generate Evidence Pack. |
| GET | `/v1/runs/{run_id}/timeline` | Retrieve Timeline. |
| POST | `/v1/demo` | Execute a full local demo scenario. |

## 6. Contract Validation Boundary

Contract validation for this packet means:

1. OpenAPI contract parses as JSON.
2. MVP-A JSON Schema files parse as JSON.
3. Expected schema files exist.
4. OpenAPI components include MVP-A records.
5. MVP-B endpoints are absent.
6. API tests verify response shapes for the local proof loop.

This packet intentionally avoids adding a third-party JSON Schema validator. Full schema validation can be introduced later by ADR if needed.

## 7. Acceptance Criteria

WP-E1-004 is accepted when:

- the HTTP API starts locally;
- API calls create a Run;
- API calls generate a mock Proposal;
- API calls broker Tool Action through Policy Check;
- safe actions are mock-executed only after Policy Check;
- risky actions create Approval Requests;
- approved risky actions resume mock execution;
- blocked actions do not execute;
- Evidence Pack generation works through API;
- Timeline retrieval works through API;
- OpenAPI contract exists and parses;
- contract validation script passes;
- API tests pass;
- no MVP-B endpoints are introduced.

## 8. Handoff to WP-E1-005

Recommended next packet:

**WP-E1-005 — MVP-A Persistence and Evidence Hardening**
