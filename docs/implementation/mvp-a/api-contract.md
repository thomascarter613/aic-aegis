---
title: MVP-A API Contract
project: AIC Aegis
status: Proposed
last_updated: 2026-06-16
---

# MVP-A API Contract

> **Core law:** The model proposes; the platform disposes.

## 1. API Rule

The API is a governed interface into Aegis. It must not bypass application use cases.

## 2. Endpoints

### Create Run

```http
POST /runs
```

Request:

```json
{
  "actor": { "actor_id": "human.demo.operator", "actor_type": "human" },
  "workflow": "governed-sales-ops-follow-up",
  "purpose": "Demonstrate MVP-A proof loop"
}
```

Response:

```json
{
  "run_id": "run_...",
  "status": "created",
  "created_at": "2026-06-16T00:00:00Z"
}
```

### Submit Tool Action Proposal

```http
POST /runs/{run_id}/proposals/tool-action
```

Request:

```json
{
  "actor": { "actor_id": "mock-model.sales-follow-up", "actor_type": "model_adapter" },
  "proposal_type": "tool_action",
  "tool_action": {
    "tool_name": "mock.sales_follow_up",
    "operation": "send_follow_up_email",
    "target": { "kind": "mock_contact", "id": "contact_demo_001" },
    "payload": { "message": "Following up on our previous conversation." }
  }
}
```

Response:

```json
{
  "proposal_id": "prop_...",
  "tool_action_id": "tool_...",
  "status": "submitted"
}
```

### Broker Tool Action

```http
POST /runs/{run_id}/tool-actions/{tool_action_id}/broker
```

Response:

```json
{
  "tool_broker_decision_id": "tbd_...",
  "policy_check_id": "pol_...",
  "disposition": "approval_required",
  "risk_level": "high",
  "tool_action_status": "pending_approval"
}
```

### Record Approval Decision

```http
POST /runs/{run_id}/approvals/{approval_request_id}/decisions
```

Request:

```json
{
  "actor": { "actor_id": "human.demo.approver", "actor_type": "human" },
  "decision": "approved",
  "rationale": "Demo approval for mock execution only."
}
```

### Generate Evidence Pack

```http
POST /runs/{run_id}/evidence-packs
```

Response:

```json
{
  "evidence_pack_id": "evp_...",
  "run_id": "run_...",
  "manifest_path": ".aic/runtime/evidence/run_.../evp_.../manifest.json"
}
```

### Get Timeline

```http
GET /runs/{run_id}/timeline
```

Response:

```json
{
  "run_id": "run_...",
  "entries": [
    { "sequence": 1, "event_type": "RunCreated", "summary": "Run created" },
    { "sequence": 2, "event_type": "ProposalSubmitted", "summary": "Tool Action Proposal captured" }
  ]
}
```

### Run Golden Workflow Demo

```http
POST /demo/golden-workflow
```

Response:

```json
{
  "run_id": "run_...",
  "disposition": "approval_required",
  "evidence_pack_id": "evp_...",
  "timeline_url": "/runs/run_.../timeline"
}
```

## 3. Error Shape

All errors should use a stable shape:

```json
{
  "error": {
    "code": "POLICY_REQUIRED",
    "message": "Policy Check is required before tool execution.",
    "run_id": "run_...",
    "correlation_id": "corr_..."
  }
}
```
