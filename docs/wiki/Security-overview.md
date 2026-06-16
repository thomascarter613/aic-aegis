# Security Overview

Security posture and assumptions.

---

## Purpose

Security Overview defines the initial security posture for Aegis.

---

## Core Security Concerns

Aegis must protect:

* tenant data,
* memory,
* tool credentials,
* policy decisions,
* evidence,
* approvals,
* outputs,
* business systems.

---

## MVP Assumptions

MVP uses synthetic data.

MVP is not production HIPAA, PCI, or regulated-grade.

MVP should still preserve secure architecture direction.

---

## Security Rules

1. No secrets in repo.
2. No cross-tenant leakage.
3. High-risk tools fail closed.
4. Evidence must be redacted when needed.
5. Provider SDKs stay in adapters.
6. Sensitive actions require policy.

---

## North Star

Security should be built into Aegis governance, not added later.
