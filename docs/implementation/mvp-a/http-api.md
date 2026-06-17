---
title: MVP-A HTTP API
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Proposed
work_packet: WP-E1-004
last_updated: 2026-06-16
---

# MVP-A HTTP API

> **Core law:** The model proposes; the platform disposes.

## Purpose

The MVP-A HTTP API exposes the local Proof Loop through a machine-usable interface.

The API is not the domain. It is an interface adapter over application use cases.

## Running Locally

```bash
bash scripts/mvp-a-api.sh
```

Default URL:

```text
http://127.0.0.1:8080
```

## Example Demo Request

```bash
curl -s -X POST http://127.0.0.1:8080/v1/demo \
  -H 'content-type: application/json' \
  -d '{"scenario":"safe"}' | python -m json.tool
```

## Boundary Rules

Route handlers must call application use cases.

They must not:

- execute tools directly;
- evaluate policy directly;
- generate evidence directly outside the Evidence use case;
- write memory;
- capture feedback;
- record evals;
- infer business outcomes.
