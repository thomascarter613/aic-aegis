# Evidence Schema

Evidence Pack structure.

---

## Purpose

Evidence Schema defines the structure of Evidence Packs.

---

## Evidence Pack Fields

Required:

* `evidence_pack_id`,
* `tenant_id`,
* `run_id`,
* `trace_id`,
* `evidence_level`,
* `summary`,
* `timeline`,
* `policy_decision_refs`,
* `tool_decision_refs`,
* `output_refs`,
* `generated_at`.

Recommended:

* memory refs,
* approval refs,
* eval refs,
* feedback refs,
* outcome refs,
* redaction notes,
* completeness score.

---

## North Star

Evidence Schema makes proof consistent and portable.
