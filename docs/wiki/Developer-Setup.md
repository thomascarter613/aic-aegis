# Developer Setup

How to clone and run locally.

---

## Purpose

Developer Setup explains how to get Aegis running locally.

---

## Current Status

Developer setup is not yet finalized.

This page should eventually include:

* prerequisites,
* clone instructions,
* environment setup,
* service startup,
* database migration,
* demo command,
* test command.

---

## Target Flow

```bash
git clone https://github.com/thomascarter613/aic-aegis.git
cd aic-aegis
cp .env.example .env
bash scripts/doctor.sh
bash scripts/dev.sh
```

---

## MVP Goal

A contributor should be able to run the Golden Workflow locally with synthetic data.

---

## North Star

Developer setup should make Aegis easy to run, test, and understand.
