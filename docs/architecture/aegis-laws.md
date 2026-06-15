# Aegis Laws

Status: proposed  
Codename: Aegis  
Product: AIC AI Reliability Control Plane  
Last updated: 2026-06-15  

## Purpose

The Aegis Laws are the constitutional rules of the system. Future work packets, implementations, prompts, policies, schemas, tests, and demos should preserve them.

## The Laws

### Law 1 — The model proposes; the platform disposes.

The model may classify, summarize, recommend, draft, and propose. The platform decides, authorizes, records, executes, blocks, escalates, and proves.

### Law 2 — No AI action without identity.

Every governed run must have `tenant_id`, `agent_id`, `run_id`, and `trace_id`.

### Law 3 — No tool execution without brokered authorization.

Agents do not call tools directly. Tool execution must pass through the Tool Broker.

### Law 4 — No durable memory without admission.

The model may propose memory. Only the Memory Admission Gate can admit durable memory.

### Law 5 — No sensitive action without policy.

Sensitive actions require runtime policy checks. Policy in documentation or prompts is not enough.

### Law 6 — No high-risk action without approval or denial.

High-risk tool calls must be approval-gated or denied by default. Critical actions are blocked by default until explicit governance exists.

### Law 7 — No evidence-free governed run.

A governed run must produce evidence or record why evidence is incomplete.

### Law 8 — No unattributed output.

Every output should be attributable to run, agent, model call, prompt/config version when available, memory/context refs, tool result refs, policy decision refs, and timestamp.

### Law 9 — No silent failure.

Failures must be recorded as events.

### Law 10 — No business-value claim without an outcome record.

Aegis must not claim business value without an outcome record. Outcomes may be estimated or verified, but they must be labeled accurately.

### Law 11 — No infrastructure dependency inside the domain core.

The domain core must not depend on model provider SDKs, OPA internals, Postgres row types, Redis clients, MCP SDK types, OpenTelemetry SDKs, UI frameworks, or cloud SDKs.

### Law 12 — No cross-tenant leakage.

Every tenant-owned object must be tenant-scoped.

### Law 13 — No unmanaged autonomy.

Aegis should increase autonomy only when evidence, policy, evals, approvals, and outcomes justify it.

### Law 14 — No promotion without proof.

Workflow, prompt, policy, tool, eval, memory-rule, or agent-version changes should not be promoted without relevant gates.

### Law 15 — No architecture without doctrine.

Major implementation decisions must remain consistent with Architecture Doctrine, Aegis Laws, Control Catalog, Risk Register, Product Decision Records, and ADRs.

## Summary

If any law is violated, the system may still be software, but it is no longer Aegis.

