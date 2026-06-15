# PDR-0001 — First Workflow is Governed Sales/Ops Follow-Up

Status: proposed  
Date: 2026-06-15  

## Context

Aegis needs a first workflow that proves the reliability loop without requiring regulated data, destructive actions, or complex integrations.

## Decision

The first canonical workflow is:

> Governed Sales/Ops Follow-Up

The workflow accepts a synthetic customer conversation and asks the AI to summarize the conversation, identify follow-up needs, draft a response, suggest CRM updates, and propose sending an email.

Aegis then creates a run, records events, policy-checks tool actions, allows safe draft behavior, blocks or approval-gates sending email, generates evidence, records eval and outcome data.

## Reasons

This workflow proves run identity, policy, tool governance, approval, evidence, evals, feedback, and outcomes.

It is commercially understandable because businesses already understand follow-up, CRM updates, and email risk.

## Consequences

Aegis should optimize the MVP demo around this workflow. Other workflows are deferred until this one is reliable.

