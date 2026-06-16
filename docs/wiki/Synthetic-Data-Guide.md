# Synthetic-Data-Guide

Safe fake data for demos and tests.

---

## Purpose

Synthetic Data Guide defines how Aegis uses fake data safely.

---

## Rules

1. No real customer data in MVP demos.
2. No real secrets.
3. No real emails sent.
4. Data should be realistic enough to test workflows.
5. Synthetic records should be clearly labeled.

---

## Example Entity

```json
{
  "company": "Acme HVAC",
  "contact": "Jordan Smith",
  "need": "Appointment follow-up automation",
  "preference": "Do not send emails without approval"
}
```

---

## North Star

Synthetic data lets Aegis prove governance without creating real risk.

---