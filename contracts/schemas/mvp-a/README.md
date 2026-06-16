# MVP-A Schema Contracts

> **Core law:** The model proposes; the platform disposes.

This directory contains the initial MVP-A JSON Schema contracts for AIC Aegis.

## Rules

- Use JSON Schema draft 2020-12.
- Use explicit `schema_version`.
- Use Aegis vocabulary.
- Keep MVP-B records out of MVP-A schemas.
- Prefer stable IDs and references.

## Schemas

- `actor.schema.json`
- `run.schema.json`
- `run-event.schema.json`
- `proposal.schema.json`
- `tool-action.schema.json`
- `policy-check.schema.json`
- `approval.schema.json`
- `evidence-pack.schema.json`
- `timeline.schema.json`
- `enums.schema.json`

## Notes

These schemas are implementation baseline contracts. They may be refined during coding, but changes that alter domain semantics should be captured in an ADR or follow-up work packet.
