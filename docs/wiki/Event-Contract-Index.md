# Event Contract Index

Event names, payloads, and versions.

---

## Purpose

The Event Contract Index lists canonical event types.

---

## Event Families

* `run.*`,
* `model.*`,
* `memory.*`,
* `tool.*`,
* `policy.*`,
* `approval.*`,
* `evidence.*`,
* `eval.*`,
* `feedback.*`,
* `outcome.*`.

---

## Required Event Metadata

Every event should include:

* event ID,
* event type,
* event version,
* tenant ID,
* run ID when applicable,
* trace ID when applicable,
* actor,
* timestamp,
* payload.

---

## Versioning Rule

Event payloads should be versioned.

Breaking event changes require version updates.

---

## North Star

Event contracts make Aegis behavior reconstructable.
