# Versioning Policy

Schema, API, workflow, policy, prompt, and tool versions.

---

## Purpose

Versioning Policy defines what Aegis must version.

---

## Versioned Artifacts

Aegis should version:

* schemas,
* APIs,
* events,
* workflows,
* prompts,
* policies,
* tool manifests,
* eval packs,
* memory rules,
* evidence formats.

---

## Rules

1. Breaking changes require version bumps.
2. Evidence should record relevant versions.
3. Eval results should record artifact versions.
4. Workflow runs should record workflow version.
5. Policy decisions should record policy version.
6. Tool calls should record tool manifest version.

---

## North Star

Versioning keeps Aegis behavior explainable over time.
