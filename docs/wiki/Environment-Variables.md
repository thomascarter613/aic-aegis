# Environment Variables

`.env` guide.

---

## Purpose

This page documents environment variables used by Aegis.

---

## Planned Variables

| Variable                      | Purpose                          |
| ----------------------------- | -------------------------------- |
| `DATABASE_URL`                | PostgreSQL connection            |
| `REDIS_URL`                   | Redis connection                 |
| `AEGIS_ENV`                   | local, test, staging, production |
| `POLICY_MODE`                 | mock, opa                        |
| `MODEL_PROVIDER`              | mock, local, external            |
| `LOG_LEVEL`                   | Logging level                    |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | Telemetry endpoint later         |

---

## Rules

1. Never commit secrets.
2. Provide `.env.example`.
3. Keep local defaults safe.
4. Use mock providers for MVP when possible.

---

## North Star

Environment variables should configure infrastructure without changing domain behavior.
