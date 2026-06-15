# ADR-0004 — Tools Execute Through a Broker

Status: proposed

## Context

Tool use is where AI becomes operationally useful and operationally dangerous.

## Decision

Agents may propose tool calls, but all tool execution flows through a Tool Broker.

## Consequences

The broker can enforce schema validation, policy checks, approval gates, rate limits, scoped credentials, audit logs, and evidence collection.
