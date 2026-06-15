# Approval Model

## Risk classes

| Risk | Example | Control |
|---|---|---|
| read_only | Read docs, search CRM | log and policy check |
| low_write | Create draft, add note | reversible action log |
| medium_write | Update CRM | approval or bounded autonomy |
| high_write | Send email, refund, delete | human approval |
| critical | legal, medical, financial, destructive infra | block or strong approval |

## Approval principle

Agents may propose. Humans or policy-approved capability grants authorize.
