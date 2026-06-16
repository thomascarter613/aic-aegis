# Dependency Policy

How dependencies are added or upgraded.

---

## Purpose

Dependency Policy protects Aegis from unnecessary risk and bloat.

---

## Rules

1. Add dependencies intentionally.
2. Prefer stable, maintained packages.
3. Avoid vendor lock-in in domain core.
4. Security-sensitive dependencies require review.
5. Provider SDKs belong in adapters.
6. Upgrade with tests.
7. Remove unused dependencies.

---

## North Star

Dependencies should support the architecture, not define it.
