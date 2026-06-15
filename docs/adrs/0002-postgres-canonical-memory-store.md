# ADR-0002 — PostgreSQL is the Canonical Memory Store

Status: proposed

## Context

Reliable AI memory requires provenance, ownership, versioning, confidence, lifecycle, sensitivity, and correction.

## Decision

Use PostgreSQL as the canonical memory source of truth. Use pgvector for semantic retrieval. Allow Qdrant later as an optional accelerator.

## Consequences

Memory is auditable and relationally governed. Vector search remains an access pattern, not the source of truth.
