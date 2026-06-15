# Architecture Fitness Functions

Status: proposed  
Codename: Aegis  
Product: AIC AI Reliability Control Plane  
Last updated: 2026-06-15  

## Purpose

Architecture fitness functions are executable or reviewable checks that protect Aegis from architectural drift. They should become tests, CI checks, schema checks, policy tests, static analysis, or review checklists.

## Identity Fitness

### AF-IDENT-001 — Every run has identity

Every `Run` must have `run_id`, `tenant_id`, `agent_id`, and `trace_id`.

### AF-IDENT-002 — Run-scoped objects link to runs

Run-scoped model calls, tool calls, policy decisions, evidence packs, eval results, feedback records, and outcomes should reference `run_id`.

## Boundary Fitness

### AF-BOUNDARY-001 — Domain does not import infrastructure

Domain code must not import database clients, model provider SDKs, OPA clients, Redis clients, MCP SDK types, OpenTelemetry SDKs, or web framework types.

### AF-BOUNDARY-002 — External provider types are translated at adapter boundary

Provider responses, MCP tools, OPA results, and SQL rows must be mapped into Aegis domain objects.

## Event Fitness

### AF-EVENT-001 — Important actions emit events

Run creation, policy checks, memory retrieval, tool proposals, tool decisions, approvals, evidence generation, eval completion, feedback receipt, and outcome recording must emit events.

### AF-EVENT-002 — Events are versioned

Every event must include `event_type`, `event_version`, `occurred_at`, and run/tenant identifiers when applicable.

### AF-EVENT-003 — No silent failure

Known failures must emit failure events.

## Tool Governance Fitness

### AF-TOOL-001 — No direct tool execution by model

All tool execution must pass through Tool Broker.

### AF-TOOL-002 — Every tool has a manifest

Every registered tool must have ID, name, risk level, side-effect flag, input schema, output schema, and approval requirement.

### AF-TOOL-003 — Every tool call has a policy decision

A `ToolCall` cannot execute without a `PolicyDecision`.

### AF-TOOL-004 — High-risk tools require approval or denial

Tools classified as `high_write` or `critical` must not execute without approval or explicit deny path.

## Memory Governance Fitness

### AF-MEM-001 — No durable memory without admission

A `MemoryRecord` cannot be created from AI output without a `MemoryAdmissionDecision`.

### AF-MEM-002 — Every memory has provenance

Every `MemoryRecord` must have source type, source reference, subject, scope, confidence, sensitivity, and timestamp.

### AF-MEM-003 — Restricted memory is blocked by default

Restricted memory candidates are denied by default in MVP.

## Policy Fitness

### AF-POL-001 — Policy decisions include reasons

Every `PolicyDecision` must include a human-readable reason.

### AF-POL-002 — Sensitive checkpoints call policy

Sensitive operations must call policy before proceeding.

### AF-POL-003 — Risky actions fail closed when policy unavailable

If the policy service is unavailable, high-risk actions must not execute.

## Evidence Fitness

### AF-EVD-001 — Evidence pack references run

Every `EvidencePack` must include `run_id`.

### AF-EVD-002 — Evidence pack contains required references

Evidence packs should include relevant input, memory, policy, model call, tool call, approval, output, eval, and outcome refs.

### AF-EVD-003 — Evidence generation failure is recorded

If evidence generation fails or is incomplete, an event must record the failure.

## Eval Fitness

### AF-EVAL-001 — Golden workflow has eval coverage

The governed Sales/Ops Follow-Up workflow must always have at least one passing eval.

### AF-EVAL-002 — Eval results link to runs

Eval results created from run output must reference the run.

## Tenant Isolation Fitness

### AF-TENANT-001 — Tenant-owned records have tenant_id

All tenant-owned tables must include `tenant_id`.

### AF-TENANT-002 — Repository queries are tenant-scoped

Repository methods must require tenant context for tenant-owned records.

### AF-TENANT-003 — No cross-tenant memory retrieval

Memory retrieval must not return records from another tenant.

## Security Fitness

### AF-SEC-001 — No secrets exposed to model

Model prompts must not include raw secrets.

### AF-SEC-002 — Tool credentials are brokered

Tools use platform-managed scoped credentials, not model-owned credentials.

### AF-SEC-003 — Synthetic data only in MVP demo

MVP fixtures and demos must not require real customer data.

## Outcome Fitness

### AF-OUT-001 — Outcome claims require outcome records

Business value claims must be backed by `BusinessOutcome` records.

### AF-OUT-002 — Outcomes mark estimated vs verified

Every outcome must indicate whether it is estimated or verified.

## API and Contract Fitness

### AF-API-001 — API schemas are versioned

Public APIs and schema contracts must be versioned.

### AF-API-002 — Write endpoints support idempotency where side effects are possible

Commands that create or mutate state should support idempotency keys.

## Initial CI Targets

The first executable checks should validate that JSON schemas parse, required docs exist, tool manifests validate, policy packs have fixtures, evidence schema validates, no obvious secrets are committed, golden workflow fixtures exist, and tenant-owned schema tables include `tenant_id`.

## Final Rule

If the architecture cannot be tested, it will drift.

