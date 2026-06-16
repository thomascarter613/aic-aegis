# Tool Schema

Tool manifests, proposals, calls, and results.

---

## Purpose

Tool Schema defines how Aegis represents governed tool use.

---

## Tool Manifest

Includes:

* `tool_id`,
* name,
* description,
* version,
* risk class,
* input schema,
* output schema,
* permissions,
* policy requirements,
* approval requirement,
* owner,
* status.

---

## Tool Proposal

Includes:

* proposal ID,
* tenant ID,
* run ID,
* trace ID,
* agent ID,
* tool ID,
* proposed input,
* reason,
* model call ID.

---

## Tool Call

Includes:

* tool call ID,
* proposal ID,
* policy decision ID,
* approval request ID,
* execution status,
* result reference.

---

## North Star

Tool Schema ensures tool use is structured, governed, and auditable.
