# Tenant Isolation

No cross-tenant leakage.

---

## Purpose

Tenant Isolation protects customer and organization boundaries.

---

## Core Rule

Aegis Law:

> **No cross-tenant leakage.**

---

## Tenant-Scoped Records

Tenant-owned records include:

* runs,
* memory,
* tool calls,
* policy decisions,
* evidence,
* evals,
* feedback,
* outcomes.

---

## MVP Rule

All tenant-owned tables should include `tenant_id`.

All queries should filter by tenant.

---

## North Star

Tenant Isolation is required for trust.
