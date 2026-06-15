# ADR-0003 — Policy-as-Code is Required for Runtime Decisions

Status: proposed

## Context

Prompt-only safety is insufficient for production AI workflows.

## Decision

Use policy-as-code for runtime decisions involving memory, tools, context, outputs, approvals, and model selection.

## Consequences

Sensitive actions become inspectable, testable, versioned, and auditable.
