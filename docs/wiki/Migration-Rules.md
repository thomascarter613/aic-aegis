# Migration Rules

How database changes should be introduced.

---

## Purpose

Migration Rules protect data integrity as schemas evolve.

---

## Rules

1. All schema changes require migrations.
2. Migrations must be versioned.
3. Destructive migrations require explicit review.
4. Migrations should be reversible where practical.
5. Schema docs must be updated.
6. Tests should cover important migrations.
7. Seed data must be synthetic in MVP.
8. Tenant-scoped tables must preserve `tenant_id`.

---

## Destructive Changes

Destructive changes include:

* dropping columns,
* deleting data,
* changing meaning of fields,
* changing tenant scope,
* changing event payload semantics.

These require special review.

---

## North Star

Migration Rules let Aegis evolve without corrupting evidence, memory, or audit history.
