---
title: MVP-A Implementation Guide
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
phase: MVP-A Proof Loop
last_updated: 2026-06-16
---

# MVP-A Implementation Guide

> **Core law:** The model proposes; the platform disposes.

## 1. Purpose

This guide summarizes the implementation target for MVP-A.

MVP-A must prove that Aegis can govern a model-originated Tool Action Proposal and produce evidence.

## 2. MVP-A Promise

A successful MVP-A demo shows:

1. a Run is created;
2. an Actor is attributed;
3. Run Events are recorded;
4. a mock model proposes a Tool Action;
5. the Proposal is captured;
6. the Tool Broker receives the proposed action;
7. Policy Check determines Disposition;
8. safe work is mocked;
9. risky work is blocked or approval-gated;
10. Evidence Pack is generated;
11. Timeline reconstructs the Run.

## 3. MVP-A Must Not Do

MVP-A must not:

- send real emails;
- update real CRMs;
- process real customer data;
- write governed memory;
- run eval loops;
- record business outcomes;
- require Kubernetes;
- require cloud services;
- implement a connector ecosystem.

## 4. Documentation Map

- `module-boundaries.md` — Clean Architecture implementation boundaries.
- `api-contract.md` — MVP-A API endpoints and request/response shape.
- `schema-catalog.md` — MVP-A schema families and required fields.
- `persistence-model.md` — MVP-A records and relationships.
- `demo-scenario.md` — Golden workflow demo.
- `test-strategy.md` — Fitness and acceptance tests.
