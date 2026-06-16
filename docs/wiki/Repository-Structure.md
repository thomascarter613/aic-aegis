# Repository Structure

Explanation of folders and ownership.

---

## Purpose

Repository Structure explains where code, docs, schemas, policies, and tests belong.

---

## Recommended Structure

```text
apps/
services/
packages/
docs/
db/
infra/
scripts/
tests/
```

---

## Ownership

| Folder      | Purpose                             |
| ----------- | ----------------------------------- |
| `apps/`     | UI/demo apps                        |
| `services/` | API and workers                     |
| `packages/` | Shared domain, schemas, adapters    |
| `docs/`     | Product and architecture docs       |
| `db/`       | Migrations                          |
| `infra/`    | Local and deployment infrastructure |
| `scripts/`  | Developer scripts                   |
| `tests/`    | Test suites                         |

---

## North Star

Repo structure should make boundaries obvious.
