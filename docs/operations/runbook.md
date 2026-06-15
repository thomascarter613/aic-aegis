# Operations Runbook

## Local startup

```bash
cp .env.example .env
bash scripts/dev.sh
```

## Health checks

```bash
bash scripts/doctor.sh
bash scripts/check.sh
```

## Evidence review

Evidence packs should be reviewed before trusting agentic workflow outputs in production.
