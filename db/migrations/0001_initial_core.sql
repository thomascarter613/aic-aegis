-- AIC Aegis initial core schema
-- PostgreSQL source of truth. pgvector is expected for semantic retrieval.

create extension if not exists vector;
create extension if not exists pgcrypto;

create table if not exists tenants (
  id text primary key,
  name text not null,
  created_at timestamptz not null default now()
);

create table if not exists agents (
  id text primary key,
  tenant_id text not null references tenants(id),
  name text not null,
  purpose text,
  status text not null default 'active',
  created_at timestamptz not null default now()
);

create table if not exists runs (
  id text primary key,
  tenant_id text not null references tenants(id),
  user_id text,
  agent_id text not null references agents(id),
  task_type text not null,
  status text not null,
  trace_id text,
  evidence_pack_id text,
  input_refs jsonb not null default '[]'::jsonb,
  policy_context jsonb not null default '{}'::jsonb,
  memory_context jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists run_events (
  id uuid primary key default gen_random_uuid(),
  run_id text not null references runs(id),
  event_type text not null,
  payload jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table if not exists memories (
  id text primary key,
  tenant_id text not null references tenants(id),
  subject_type text not null,
  subject_id text,
  memory_type text not null,
  content text not null,
  normalized_content text,
  embedding vector(1536),
  source_type text not null,
  source_ref text not null,
  confidence numeric(4,3) not null default 0.500,
  sensitivity text not null default 'internal',
  status text not null default 'active',
  valid_from timestamptz not null default now(),
  valid_until timestamptz,
  supersedes_memory_id text references memories(id),
  created_by text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists memory_events (
  id uuid primary key default gen_random_uuid(),
  memory_id text not null references memories(id),
  run_id text references runs(id),
  event_type text not null,
  old_value jsonb,
  new_value jsonb,
  reason text,
  actor_type text,
  actor_id text,
  created_at timestamptz not null default now()
);

create table if not exists tool_definitions (
  id text primary key,
  name text not null,
  manifest jsonb not null,
  risk_level text not null,
  side_effect boolean not null default false,
  created_at timestamptz not null default now()
);

create table if not exists tool_calls (
  id text primary key,
  run_id text not null references runs(id),
  tool_id text not null references tool_definitions(id),
  status text not null,
  input jsonb not null,
  output jsonb,
  policy_decision_id text,
  created_at timestamptz not null default now(),
  completed_at timestamptz
);

create table if not exists policy_decisions (
  id text primary key,
  run_id text references runs(id),
  trace_id text,
  decision text not null,
  reason text not null,
  policy_id text not null,
  policy_version text,
  input_hash text,
  created_at timestamptz not null default now()
);

create table if not exists evidence_packs (
  id text primary key,
  run_id text not null references runs(id),
  tenant_id text not null references tenants(id),
  agent_id text not null references agents(id),
  payload jsonb not null,
  created_at timestamptz not null default now()
);

create table if not exists eval_results (
  id text primary key,
  run_id text references runs(id),
  eval_name text not null,
  score numeric(5,4),
  passed boolean,
  details jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create table if not exists business_outcomes (
  id text primary key,
  run_id text references runs(id),
  tenant_id text not null references tenants(id),
  metric_name text not null,
  metric_value numeric not null,
  unit text,
  baseline_value numeric,
  estimated boolean not null default true,
  notes text,
  created_at timestamptz not null default now()
);
