# event-type-reference

`run.*`, `tool.*`, `policy.*`, `memory.*`, `evidence.*`, etc.

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

## Required Metadata

Every event should include:

* event ID,
* event type,
* version,
* tenant ID,
* run ID when applicable,
* trace ID,
* actor,
* timestamp,
* payload.

---

## North Star

Event types make Aegis behavior reconstructable.

---