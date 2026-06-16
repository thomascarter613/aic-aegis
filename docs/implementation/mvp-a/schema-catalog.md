---
title: MVP-A Schema Catalog
project: AIC Aegis
status: Proposed
last_updated: 2026-06-16
---

# MVP-A Schema Catalog

> **Core law:** The model proposes; the platform disposes.

## 1. Schema Rules

Schemas must be explicit, versioned, and named using Aegis vocabulary.

Every boundary record should include:

- ID;
- schema version;
- Run ID where applicable;
- Actor attribution where applicable;
- timestamp;
- correlation ID where applicable.

## 2. Required Schemas

| Schema | Purpose | MVP-A Required |
|---|---|---|
| ActorRef | Identifies human/service/model/system actor | Yes |
| Run | Bounded unit of governed AI work | Yes |
| RunEvent | Event record for timeline/evidence | Yes |
| Proposal | Model-originated suggestion | Yes |
| ToolAction | Proposed or mocked tool action | Yes |
| PolicyCheck | Policy evaluation result | Yes |
| Disposition | Platform decision | Yes |
| ToolBrokerDecision | Tool Broker record | Yes |
| ApprovalRequest | Approval gate request | Yes |
| ApprovalDecision | Approval result | Yes |
| EvidencePackManifest | Evidence pack index | Yes |
| EvidenceArtifact | Evidence item reference | Yes |
| Timeline | Ordered Run reconstruction | Yes |

## 3. Canonical Enums

### Actor Type

```text
human
model_adapter
service
worker
system
```

### Proposal Type

```text
tool_action
```

### Disposition

```text
allow
mock
block
approval_required
```

### Risk Level

```text
low
medium
high
critical
```

### Approval Status

```text
requested
approved
rejected
expired
cancelled
```

### Tool Action Status

```text
proposed
policy_checked
mock_executed
blocked
pending_approval
approved
rejected
cancelled
```

## 4. Event Types

MVP-A event types:

- RunCreated;
- RunEventRecorded;
- ProposalSubmitted;
- ToolActionProposed;
- PolicyCheckCompleted;
- ToolActionDispositioned;
- ApprovalGateRequested;
- ApprovalDecisionRecorded;
- ToolActionMockExecuted;
- ToolActionBlocked;
- EvidencePackGenerated;
- TimelineGenerated.

## 5. Schema Versioning

Initial schema version:

```text
v0.1.0
```

Schema compatibility can remain manual during MVP-A, but every emitted record must include the schema version.
