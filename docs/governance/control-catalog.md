# Aegis Control Catalog

Status: proposed  
Codename: Aegis  
Product: AIC AI Reliability Control Plane  
Last updated: 2026-06-15  

## Purpose

The Control Catalog defines governance controls Aegis should enforce or support. These controls can later map to policy tests, fitness functions, audit checks, evidence completeness checks, and enterprise reports.

## Runtime Controls

### CTRL-RUN-001 — Run Identity Required

Every governed AI workflow must have `run_id`, `tenant_id`, `agent_id`, and `trace_id`.

### CTRL-RUN-002 — Run Events Required

Important runtime activity must be recorded as run/domain events.

### CTRL-RUN-003 — No Silent Failure

Known failures must be recorded and surfaced.

## Tool Controls

### CTRL-TOOL-001 — Tool Broker Required

Models and agents must not execute tools directly.

### CTRL-TOOL-002 — Tool Manifest Required

Every tool must have a manifest with risk class, side-effect status, schemas, approval requirement, and evidence requirement.

### CTRL-TOOL-003 — Policy Decision Required for Tool Execution

Every executable tool call must have a policy decision.

### CTRL-TOOL-004 — High-Risk Actions Require Approval or Denial

High-risk tool actions are approval-gated or denied by default.

## Memory Controls

### CTRL-MEM-001 — Memory Admission Required

Durable AI-proposed memory must pass through Memory Admission Gate.

### CTRL-MEM-002 — Memory Provenance Required

Memory records must include source, scope, subject, confidence, sensitivity, and lifecycle metadata.

### CTRL-MEM-003 — Memory Sensitivity Required

Memory records must support public, internal, confidential, and restricted classifications.

### CTRL-MEM-004 — Memory Correction Path Required

Memory must be correctable, supersedable, and auditable.

## Policy Controls

### CTRL-POL-001 — Runtime Policy Checks Required

Sensitive operations must call policy at runtime.

### CTRL-POL-002 — Policy Decisions Require Reasons

Every policy decision must include a reason.

### CTRL-POL-003 — Policy Failure Mode Defined

High-risk actions fail closed when policy is unavailable.

## Evidence Controls

### CTRL-EVD-001 — Evidence Pack Required

Governed AI runs must produce evidence or record why evidence is incomplete.

### CTRL-EVD-002 — Evidence References Required

Evidence must link to relevant run, policy, tool, memory, eval, approval, and outcome records.

### CTRL-EVD-003 — Evidence Redaction Required

Evidence exports must obey audience, policy, and data classification rules.

## Eval Controls

### CTRL-EVAL-001 — Golden Workflow Eval Required

The golden workflow must have eval coverage.

### CTRL-EVAL-002 — Promotion Requires Evals

Workflow, prompt, policy, tool, and agent changes should require eval gates before promotion.

## Feedback Controls

### CTRL-FBK-001 — Feedback Capture Required

User feedback and corrections must be captured as structured records.

### CTRL-FBK-002 — Failure Taxonomy Required

Failures must be classified consistently.

## Outcome Controls

### CTRL-OUT-001 — Outcome Record Required for Value Claims

Business value claims require outcome records.

### CTRL-OUT-002 — Estimated vs Verified Distinction Required

Outcomes must distinguish estimated from verified.

## Security Controls

### CTRL-SEC-001 — Secrets Never Exposed to Models

Credentials must never be shown to models.

### CTRL-SEC-002 — Tenant Isolation Required

Tenant-owned data must be tenant-scoped.

### CTRL-SEC-003 — Synthetic Data Only for MVP Demo

MVP demos and fixtures use synthetic data.

## Architecture Controls

### CTRL-ARCH-001 — Domain Core Independence

Domain logic must not depend on infrastructure.

### CTRL-ARCH-002 — External Systems Are Adapters

Model providers, OPA, MCP, Postgres, telemetry, and storage are adapters.

## Control Coverage Metrics

Future dashboards should measure:

- percent of runs with evidence,
- percent of tool calls with policy decisions,
- percent of memory writes with admission decisions,
- percent of high-risk actions requiring approval,
- percent of workflows with eval coverage,
- percent of outputs with feedback,
- percent of runs with outcome records.

## Final Principle

Aegis is governance-grade only if controls are explicit, testable, evidenced, and reviewable.

