# Secrets Management

Rules for credentials and tool access.

---

## Purpose

Secrets Management protects credentials used by tools, providers, and infrastructure.

---

## Rules

1. Never commit secrets.
2. Use `.env.example` only for placeholders.
3. Provider credentials belong in adapters/config.
4. Tool credentials must not be exposed to models.
5. Evidence must not include secrets.
6. Logs must not include secrets.

---

## MVP Scope

MVP should use mock tools and avoid real secrets.

---

## North Star

Secrets must never become model context.
