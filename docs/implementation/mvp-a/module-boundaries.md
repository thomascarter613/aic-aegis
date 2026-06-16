---
title: MVP-A Module Boundaries
project: AIC Aegis
status: Proposed
last_updated: 2026-06-16
---

# MVP-A Module Boundaries

> **Core law:** The model proposes; the platform disposes.

## 1. Required Logical Layout

```text
services/aegis-control-plane/
  src/
    domain/
    application/
    adapters/
    interfaces/
```

If another service path already exists, keep the logical boundaries even if the physical path differs.

## 2. Domain Boundary

Domain contains pure Aegis concepts:

- ActorRef;
- Run;
- RunStatus;
- RunEvent;
- Proposal;
- ProposalType;
- ToolAction;
- ToolActionStatus;
- PolicyCheck;
- RiskLevel;
- Disposition;
- ApprovalRequest;
- ApprovalDecision;
- EvidencePack;
- EvidenceArtifact;
- TimelineEntry.

Domain must not import framework, database, model SDK, queue, HTTP, cloud, or filesystem libraries.

## 3. Application Boundary

Application contains:

- commands;
- queries;
- use cases;
- ports;
- orchestration.

Application may depend on domain. Application must not depend on concrete adapters.

## 4. Adapter Boundary

Adapters implement ports:

- local persistence;
- local event store;
- policy evaluator;
- mock model;
- mock tool executor;
- file-backed evidence writer;
- timeline reader.

Adapters translate infrastructure details into Aegis records.

## 5. Interface Boundary

Interfaces expose the system:

- HTTP routes;
- CLI commands;
- local demo runner;
- optional worker entry point.

Interfaces call application use cases. They do not directly execute tools, evaluate policy, or write evidence.

## 6. Boundary Tests

Minimum boundary checks:

- domain has no adapter/framework imports;
- mock tool executor is only invoked by Tool Broker use case;
- policy evaluator is called before mock tool execution;
- evidence writer is called by GenerateEvidencePack use case;
- API/CLI handlers call commands and queries rather than mutating persistence directly.
