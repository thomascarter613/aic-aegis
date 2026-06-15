# ADR-0001 — Build an AI Reliability Control Plane

Status: proposed

## Context

AIC needs a platform layer for making AI systems reliable, governable, auditable, and outcome-driven.

## Decision

Build Aegis as an AI Reliability Control Plane, not as a chatbot app or narrow agent framework.

## Consequences

Aegis will own run envelopes, memory governance, tool brokering, policy decisions, evals, evidence packs, and business outcomes.

## Alternatives considered

- Build a chatbot app.
- Build only an agent framework.
- Build only an eval platform.
- Build only a memory service.
