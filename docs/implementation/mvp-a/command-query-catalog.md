---
title: MVP-A Command and Query Catalog
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-002
last_updated: 2026-06-16
---

# MVP-A Command and Query Catalog

> **Core law:** The model proposes; the platform disposes.

## 1. Purpose

This document defines the minimum MVP-A command and query catalog.

Commands change state. Queries read state.

## 2. MVP-A Commands

| Command | Purpose | Required Output |
|---|---|---|
| CreateRun | Create a governed Run. | Run |
| RecordRunEvent | Append a Run Event. | Run Event |
| SubmitProposal | Capture model/mock-model Proposal. | Proposal |
| BrokerToolAction | Route Tool Action Proposal through policy, disposition, approval, and mock execution. | Tool Action / Disposition |
| EvaluatePolicy | Evaluate Proposal or Tool Action against controls. | Policy Check |
| RequestApproval | Create Approval Request. | Approval Request |
| RecordApprovalDecision | Record Approval Decision. | Approval Decision |
| GenerateEvidencePack | Generate Evidence Pack manifest and artifacts. | Evidence Pack |

## 3. MVP-A Queries

| Query | Purpose | Required Output |
|---|---|---|
| GetRun | Retrieve Run. | Run |
| ListRuns | List Runs. | Run summaries |
| ListRunEvents | List events for Run. | Run Events |
| GetProposal | Retrieve Proposal. | Proposal |
| GetToolAction | Retrieve Tool Action. | Tool Action |
| GetPolicyCheck | Retrieve Policy Check. | Policy Check |
| GetApprovalRequest | Retrieve Approval Request. | Approval Request |
| GetEvidencePack | Retrieve Evidence Pack metadata. | Evidence Pack |
| GetRunTimeline | Reconstruct Run Timeline. | Timeline |

## 4. Command Rules

Commands must:

- validate schema;
- require Actor attribution where applicable;
- call application use cases;
- record domain events;
- not bypass policy/tool/evidence boundaries.

## 5. Query Rules

Queries must:

- not mutate state;
- reconstruct from persisted records;
- use Aegis domain vocabulary;
- expose Timeline and Evidence Pack data without relying on hidden logs.

## 6. MVP-B Deferred Commands

Do not require these in MVP-A:

- RetrieveGovernedMemory
- ProposeMemoryCandidate
- EvaluateMemoryAdmission
- CaptureFeedback
- RecordEvalResult
- RecordBusinessOutcome
