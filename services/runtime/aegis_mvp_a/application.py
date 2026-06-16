"""Application use cases and local adapters for AIC Aegis MVP-A."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .domain import (
    Actor,
    ActorType,
    ApprovalDecision,
    ApprovalDecisionRecord,
    ApprovalRequest,
    ApprovalStatus,
    Disposition,
    EventType,
    EvidenceArtifact,
    EvidencePack,
    InvariantViolation,
    PolicyCheck,
    Proposal,
    ProposalStatus,
    ProposalType,
    RiskLevel,
    Run,
    RunEvent,
    RunStatus,
    Timeline,
    TimelineItem,
    ToolAction,
    ToolActionStatus,
    new_id,
    utc_now,
)
from .serialization import write_json


@dataclass
class InMemoryStore:
    """Simple local repository adapter for MVP-A."""

    actors: dict[str, Actor] = field(default_factory=dict)
    runs: dict[str, Run] = field(default_factory=dict)
    events: list[RunEvent] = field(default_factory=list)
    proposals: dict[str, Proposal] = field(default_factory=dict)
    tool_actions: dict[str, ToolAction] = field(default_factory=dict)
    policy_checks: dict[str, PolicyCheck] = field(default_factory=dict)
    approval_requests: dict[str, ApprovalRequest] = field(default_factory=dict)
    approval_decisions: dict[str, ApprovalDecisionRecord] = field(default_factory=dict)
    evidence_packs: dict[str, EvidencePack] = field(default_factory=dict)

    def events_for_run(self, run_id: str) -> list[RunEvent]:
        return [event for event in self.events if event.run_id == run_id]

    def policy_for_tool_action(self, tool_action_id: str) -> PolicyCheck | None:
        for check in self.policy_checks.values():
            if check.tool_action_id == tool_action_id:
                return check
        return None

    def approval_for_tool_action(self, tool_action_id: str) -> ApprovalRequest | None:
        for request in self.approval_requests.values():
            if request.tool_action_id == tool_action_id:
                return request
        return None


class MockModelAdapter:
    """Deterministic mock model adapter.

    The mock model proposes Tool Actions. It never executes tools.
    """

    def propose_tool_action(self, run: Run, actor: Actor, scenario: str) -> tuple[Proposal, ToolAction]:
        now = utc_now()
        proposal_id = new_id("prop")
        tool_action_id = new_id("tool")

        if scenario == "safe":
            summary = "Create an internal follow-up task."
            tool_name = "mock_tasks"
            operation = "create_task"
            target = "internal_sales_ops_queue"
            arguments = {
                "title": "Follow up with prospect",
                "body": "Prepare a safe internal follow-up task.",
            }
        elif scenario == "risky":
            summary = "Send a customer-facing follow-up email."
            tool_name = "mock_email"
            operation = "send_follow_up_email"
            target = "prospect@example.invalid"
            arguments = {
                "subject": "Following up",
                "body": "Draft customer-facing follow-up.",
            }
        elif scenario == "blocked":
            summary = "Send sensitive data to an external recipient."
            tool_name = "mock_email"
            operation = "send_sensitive_data"
            target = "external@example.invalid"
            arguments = {
                "subject": "Sensitive account data",
                "body": "This action is intentionally blocked in MVP-A.",
            }
        else:
            raise ValueError(f"Unknown MVP-A scenario: {scenario!r}")

        proposal = Proposal(
            proposal_id=proposal_id,
            run_id=run.run_id,
            proposed_by_actor_id=actor.actor_id,
            proposal_type=ProposalType.TOOL_ACTION,
            status=ProposalStatus.SUBMITTED,
            created_at=now,
            summary=summary,
            payload={"tool_action_id": tool_action_id, "scenario": scenario},
            source={"source_type": "mock_model", "source_ref": actor.actor_id},
        )

        tool_action = ToolAction(
            tool_action_id=tool_action_id,
            run_id=run.run_id,
            proposal_id=proposal_id,
            tool_name=tool_name,
            operation=operation,
            target=target,
            arguments=arguments,
            status=ToolActionStatus.PROPOSED,
            created_at=now,
            updated_at=now,
        )

        return proposal, tool_action


class LocalPolicyEvaluator:
    """Local policy adapter for MVP-A."""

    def evaluate(self, run: Run, proposal: Proposal, tool_action: ToolAction) -> PolicyCheck:
        if tool_action.operation == "send_sensitive_data":
            risk = RiskLevel.CRITICAL
            disposition = Disposition.BLOCK
            controls = ["CTRL-002", "CTRL-003", "CTRL-004", "CTRL-010"]
            rationale = "Sensitive data exfiltration is blocked in MVP-A."
        elif tool_action.operation == "send_follow_up_email":
            risk = RiskLevel.HIGH
            disposition = Disposition.APPROVAL_REQUIRED
            controls = ["CTRL-003", "CTRL-004", "CTRL-005", "CTRL-010"]
            rationale = "Customer-facing communication requires approval in MVP-A."
        else:
            risk = RiskLevel.LOW
            disposition = Disposition.MOCK
            controls = ["CTRL-003", "CTRL-004", "CTRL-010"]
            rationale = "Internal mock-safe action may be executed by mock adapter."

        return PolicyCheck(
            policy_check_id=new_id("pol"),
            run_id=run.run_id,
            proposal_id=proposal.proposal_id,
            tool_action_id=tool_action.tool_action_id,
            checked_at=utc_now(),
            policy_engine="local-mvp-a-policy",
            input_ref=f"tool_action:{tool_action.tool_action_id}",
            risk_level=risk,
            matched_controls=controls,
            disposition=disposition,
            rationale=rationale,
        )


class MockToolExecutor:
    """Mock-safe tool executor.

    This adapter never sends email, mutates a CRM, or calls external APIs.
    """

    def execute(self, tool_action: ToolAction) -> dict[str, Any]:
        return {
            "mock": True,
            "tool_name": tool_action.tool_name,
            "operation": tool_action.operation,
            "target": tool_action.target,
            "result": "mock_executed",
            "executed_at": utc_now(),
        }


class TimelineQuery:
    """Timeline read model."""

    TITLES = {
        EventType.RUN_CREATED: "Run created",
        EventType.PROPOSAL_SUBMITTED: "Proposal submitted",
        EventType.TOOL_ACTION_PROPOSED: "Tool action proposed",
        EventType.POLICY_CHECK_COMPLETED: "Policy check completed",
        EventType.TOOL_ACTION_DISPOSITIONED: "Tool action dispositioned",
        EventType.APPROVAL_GATE_REQUESTED: "Approval requested",
        EventType.APPROVAL_DECISION_RECORDED: "Approval decision recorded",
        EventType.TOOL_ACTION_MOCK_EXECUTED: "Mock tool action executed",
        EventType.TOOL_ACTION_BLOCKED: "Tool action blocked",
        EventType.EVIDENCE_PACK_GENERATED: "Evidence pack generated",
        EventType.TIMELINE_GENERATED: "Timeline generated",
        EventType.RUN_EVENT_RECORDED: "Run event recorded",
    }

    def __init__(self, store: InMemoryStore):
        self.store = store

    def get_timeline(self, run_id: str) -> Timeline:
        if run_id not in self.store.runs:
            raise InvariantViolation(f"Run does not exist: {run_id}")

        items: list[TimelineItem] = []
        for event in sorted(self.store.events_for_run(run_id), key=lambda e: e.occurred_at):
            refs = event.payload.get("record_refs", [])
            if not isinstance(refs, list):
                refs = []
            items.append(
                TimelineItem(
                    timeline_item_id=new_id("tl"),
                    occurred_at=event.occurred_at,
                    event_type=event.event_type,
                    title=self.TITLES.get(event.event_type, event.event_type.value),
                    description=str(event.payload.get("description", "")),
                    record_refs=refs,
                )
            )

        return Timeline(run_id=run_id, generated_at=utc_now(), items=items)


class EvidenceWriter:
    """File-backed evidence writer adapter."""

    def __init__(self, store: InMemoryStore, output_root: Path | None = None):
        self.store = store
        self.output_root = output_root or Path(".aic/runtime/evidence")

    def generate(self, run_id: str, actor_id: str) -> EvidencePack:
        if run_id not in self.store.runs:
            raise InvariantViolation(f"Cannot generate evidence for missing Run: {run_id}")

        # Ensure a timeline can be reconstructed before evidence is emitted.
        timeline = TimelineQuery(self.store).get_timeline(run_id)

        evidence_pack_id = new_id("ep")
        pack_root = self.output_root / run_id / evidence_pack_id
        artifacts: list[EvidenceArtifact] = []

        def emit(artifact_type: str, record_ref: str, filename: str, value: Any) -> None:
            path = pack_root / filename
            digest = write_json(path, value)
            artifacts.append(
                EvidenceArtifact(
                    artifact_id=new_id("art"),
                    artifact_type=artifact_type,
                    record_ref=record_ref,
                    uri=str(path),
                    sha256=digest,
                )
            )

        run = self.store.runs[run_id]
        emit("run", f"run:{run_id}", "run.json", run)

        for event in self.store.events_for_run(run_id):
            emit("event", f"event:{event.event_id}", f"events/{event.event_id}.json", event)

        for proposal in self.store.proposals.values():
            if proposal.run_id == run_id:
                emit("proposal", f"proposal:{proposal.proposal_id}", f"proposals/{proposal.proposal_id}.json", proposal)

        for tool_action in self.store.tool_actions.values():
            if tool_action.run_id == run_id:
                emit("tool_action", f"tool_action:{tool_action.tool_action_id}", f"tool_actions/{tool_action.tool_action_id}.json", tool_action)

        for policy_check in self.store.policy_checks.values():
            if policy_check.run_id == run_id:
                emit("policy_check", f"policy_check:{policy_check.policy_check_id}", f"policy_checks/{policy_check.policy_check_id}.json", policy_check)

        for approval in self.store.approval_requests.values():
            if approval.run_id == run_id:
                emit("approval", f"approval_request:{approval.approval_request_id}", f"approvals/{approval.approval_request_id}.json", approval)

        emit("timeline", f"timeline:{run_id}", "timeline.json", timeline)

        pack = EvidencePack(
            evidence_pack_id=evidence_pack_id,
            run_id=run_id,
            generated_at=utc_now(),
            generated_by_actor_id=actor_id,
            manifest_version="mvp-a.evidence.v1",
            artifacts=artifacts,
            summary="MVP-A evidence pack generated from local proof-loop records.",
        )
        self.store.evidence_packs[evidence_pack_id] = pack
        write_json(pack_root / "manifest.json", pack)
        return pack


class AegisMvpA:
    """Application facade for the local MVP-A proof loop."""

    def __init__(
        self,
        store: InMemoryStore | None = None,
        model: MockModelAdapter | None = None,
        policy: LocalPolicyEvaluator | None = None,
        tool_executor: MockToolExecutor | None = None,
        evidence_writer: EvidenceWriter | None = None,
    ):
        self.store = store or InMemoryStore()
        self.model = model or MockModelAdapter()
        self.policy = policy or LocalPolicyEvaluator()
        self.tool_executor = tool_executor or MockToolExecutor()
        self.evidence_writer = evidence_writer or EvidenceWriter(self.store)

    def create_actor(self, actor_type: ActorType, display_name: str, external_ref: str | None = None) -> Actor:
        actor = Actor(
            actor_id=new_id("actor"),
            actor_type=actor_type,
            display_name=display_name,
            external_ref=external_ref,
        )
        self.store.actors[actor.actor_id] = actor
        return actor

    def create_run(self, workflow: str, purpose: str, initiating_actor_id: str) -> Run:
        if initiating_actor_id not in self.store.actors:
            raise InvariantViolation(f"Initiating Actor does not exist: {initiating_actor_id}")

        now = utc_now()
        run = Run(
            run_id=new_id("run"),
            workflow=workflow,
            purpose=purpose,
            status=RunStatus.CREATED,
            initiating_actor_id=initiating_actor_id,
            created_at=now,
            updated_at=now,
        )
        self.store.runs[run.run_id] = run
        self._record_event(
            run.run_id,
            EventType.RUN_CREATED,
            initiating_actor_id,
            {
                "description": "Run created.",
                "record_refs": [{"record_type": "run", "record_id": run.run_id}],
            },
        )
        return run

    def propose_tool_action(self, run_id: str, proposed_by_actor_id: str, scenario: str) -> tuple[Proposal, ToolAction]:
        run = self._require_run(run_id)
        actor = self._require_actor(proposed_by_actor_id)

        if actor.actor_type != ActorType.MOCK_MODEL:
            raise InvariantViolation("MVP-A tool proposals must come from mock model actor.")

        proposal, tool_action = self.model.propose_tool_action(run, actor, scenario)
        self.store.proposals[proposal.proposal_id] = proposal
        self.store.tool_actions[tool_action.tool_action_id] = tool_action

        self._record_event(
            run_id,
            EventType.PROPOSAL_SUBMITTED,
            proposed_by_actor_id,
            {
                "description": proposal.summary,
                "record_refs": [{"record_type": "proposal", "record_id": proposal.proposal_id}],
            },
        )
        self._record_event(
            run_id,
            EventType.TOOL_ACTION_PROPOSED,
            proposed_by_actor_id,
            {
                "description": f"{tool_action.tool_name}.{tool_action.operation} proposed.",
                "record_refs": [
                    {"record_type": "proposal", "record_id": proposal.proposal_id},
                    {"record_type": "tool_action", "record_id": tool_action.tool_action_id},
                ],
            },
        )
        return proposal, tool_action

    def broker_tool_action(self, tool_action_id: str, actor_id: str) -> ToolAction:
        actor = self._require_actor(actor_id)
        tool_action = self._require_tool_action(tool_action_id)
        run = self._require_run(tool_action.run_id)

        if tool_action.proposal_id not in self.store.proposals:
            raise InvariantViolation("Cannot broker Tool Action without Proposal record.")

        proposal = self.store.proposals[tool_action.proposal_id]
        proposal.status = ProposalStatus.UNDER_POLICY_REVIEW

        policy_check = self.policy.evaluate(run, proposal, tool_action)
        self.store.policy_checks[policy_check.policy_check_id] = policy_check
        tool_action.status = ToolActionStatus.POLICY_CHECKED
        tool_action.updated_at = utc_now()

        self._record_event(
            run.run_id,
            EventType.POLICY_CHECK_COMPLETED,
            actor.actor_id,
            {
                "description": policy_check.rationale,
                "record_refs": [
                    {"record_type": "policy_check", "record_id": policy_check.policy_check_id},
                    {"record_type": "proposal", "record_id": proposal.proposal_id},
                    {"record_type": "tool_action", "record_id": tool_action.tool_action_id},
                ],
            },
        )

        if policy_check.disposition == Disposition.MOCK:
            return self._mock_execute(tool_action, policy_check, actor.actor_id)

        if policy_check.disposition == Disposition.BLOCK:
            tool_action.status = ToolActionStatus.BLOCKED
            tool_action.updated_at = utc_now()
            proposal.status = ProposalStatus.BLOCKED
            run.status = RunStatus.BLOCKED
            run.updated_at = utc_now()
            self._record_event(
                run.run_id,
                EventType.TOOL_ACTION_BLOCKED,
                actor.actor_id,
                {
                    "description": "Tool Action blocked by policy.",
                    "record_refs": [
                        {"record_type": "tool_action", "record_id": tool_action.tool_action_id},
                        {"record_type": "policy_check", "record_id": policy_check.policy_check_id},
                    ],
                },
            )
            return tool_action

        if policy_check.disposition == Disposition.APPROVAL_REQUIRED:
            return self._request_approval(tool_action, policy_check, actor.actor_id)

        raise InvariantViolation(f"Unsupported MVP-A disposition: {policy_check.disposition.value}")

    def approve_and_resume(self, approval_request_id: str, decided_by_actor_id: str, rationale: str) -> ToolAction:
        actor = self._require_actor(decided_by_actor_id)
        if approval_request_id not in self.store.approval_requests:
            raise InvariantViolation(f"Approval Request does not exist: {approval_request_id}")

        request = self.store.approval_requests[approval_request_id]
        tool_action = self._require_tool_action(request.tool_action_id)
        policy_check = self.store.policy_for_tool_action(tool_action.tool_action_id)
        if policy_check is None:
            raise InvariantViolation("Cannot approve Tool Action without Policy Check.")

        decision = ApprovalDecisionRecord(
            approval_decision_id=new_id("appr_dec"),
            approval_request_id=approval_request_id,
            decided_by_actor_id=actor.actor_id,
            decision=ApprovalDecision.APPROVED,
            rationale=rationale,
            decided_at=utc_now(),
        )
        self.store.approval_decisions[decision.approval_decision_id] = decision
        request.status = ApprovalStatus.APPROVED
        tool_action.status = ToolActionStatus.APPROVED
        tool_action.updated_at = utc_now()

        self._record_event(
            request.run_id,
            EventType.APPROVAL_DECISION_RECORDED,
            actor.actor_id,
            {
                "description": "Approval decision recorded.",
                "record_refs": [
                    {"record_type": "approval_request", "record_id": request.approval_request_id},
                    {"record_type": "approval_decision", "record_id": decision.approval_decision_id},
                ],
            },
        )

        return self._mock_execute(tool_action, policy_check, actor.actor_id)

    def generate_evidence_pack(self, run_id: str, actor_id: str) -> EvidencePack:
        self._require_actor(actor_id)
        pack = self.evidence_writer.generate(run_id, actor_id)
        self._record_event(
            run_id,
            EventType.EVIDENCE_PACK_GENERATED,
            actor_id,
            {
                "description": "Evidence Pack generated.",
                "record_refs": [{"record_type": "evidence_pack", "record_id": pack.evidence_pack_id}],
            },
        )
        return pack

    def get_timeline(self, run_id: str) -> Timeline:
        timeline = TimelineQuery(self.store).get_timeline(run_id)
        return timeline

    def run_demo(self, scenario: str, approve: bool = False) -> dict[str, Any]:
        human = self.create_actor(ActorType.HUMAN, "Local Operator")
        mock_model = self.create_actor(ActorType.MOCK_MODEL, "Deterministic Mock Model")
        run = self.create_run("Governed Sales/Ops Follow-Up", f"MVP-A demo scenario: {scenario}", human.actor_id)
        _, tool_action = self.propose_tool_action(run.run_id, mock_model.actor_id, scenario)
        final_tool_action = self.broker_tool_action(tool_action.tool_action_id, human.actor_id)

        approval_request = self.store.approval_for_tool_action(tool_action.tool_action_id)
        if approve and approval_request is not None:
            final_tool_action = self.approve_and_resume(
                approval_request.approval_request_id,
                human.actor_id,
                "Approved for local mock-safe execution.",
            )

        evidence_pack = self.generate_evidence_pack(run.run_id, human.actor_id)
        timeline = self.get_timeline(run.run_id)

        return {
            "run": run,
            "tool_action": final_tool_action,
            "approval_request": approval_request,
            "evidence_pack": evidence_pack,
            "timeline": timeline,
        }

    def _mock_execute(self, tool_action: ToolAction, policy_check: PolicyCheck, actor_id: str) -> ToolAction:
        if policy_check.policy_check_id not in self.store.policy_checks:
            raise InvariantViolation("Cannot mock execute without recorded Policy Check.")

        if policy_check.risk_level in {RiskLevel.HIGH, RiskLevel.CRITICAL}:
            approval = self.store.approval_for_tool_action(tool_action.tool_action_id)
            if approval is None or approval.status != ApprovalStatus.APPROVED:
                raise InvariantViolation("High-risk Tool Action cannot execute without approval.")

        result = self.tool_executor.execute(tool_action)
        tool_action.mock_result = result
        tool_action.status = ToolActionStatus.MOCK_EXECUTED
        tool_action.updated_at = utc_now()

        proposal = self.store.proposals[tool_action.proposal_id]
        proposal.status = ProposalStatus.MOCK_EXECUTED

        run = self.store.runs[tool_action.run_id]
        run.status = RunStatus.COMPLETED
        run.updated_at = utc_now()

        self._record_event(
            tool_action.run_id,
            EventType.TOOL_ACTION_DISPOSITIONED,
            actor_id,
            {
                "description": f"Disposition applied: {policy_check.disposition.value}.",
                "record_refs": [
                    {"record_type": "tool_action", "record_id": tool_action.tool_action_id},
                    {"record_type": "policy_check", "record_id": policy_check.policy_check_id},
                ],
            },
        )
        self._record_event(
            tool_action.run_id,
            EventType.TOOL_ACTION_MOCK_EXECUTED,
            actor_id,
            {
                "description": "Mock-safe Tool Action executed.",
                "record_refs": [{"record_type": "tool_action", "record_id": tool_action.tool_action_id}],
            },
        )
        return tool_action

    def _request_approval(self, tool_action: ToolAction, policy_check: PolicyCheck, actor_id: str) -> ToolAction:
        approval = ApprovalRequest(
            approval_request_id=new_id("appr"),
            run_id=tool_action.run_id,
            proposal_id=tool_action.proposal_id,
            tool_action_id=tool_action.tool_action_id,
            requested_by_actor_id=actor_id,
            status=ApprovalStatus.REQUESTED,
            rationale=policy_check.rationale,
            created_at=utc_now(),
        )
        self.store.approval_requests[approval.approval_request_id] = approval

        tool_action.status = ToolActionStatus.APPROVAL_REQUIRED
        tool_action.updated_at = utc_now()
        self.store.proposals[tool_action.proposal_id].status = ProposalStatus.APPROVAL_REQUIRED

        run = self.store.runs[tool_action.run_id]
        run.status = RunStatus.AWAITING_APPROVAL
        run.updated_at = utc_now()

        self._record_event(
            tool_action.run_id,
            EventType.TOOL_ACTION_DISPOSITIONED,
            actor_id,
            {
                "description": "Disposition applied: approval_required.",
                "record_refs": [
                    {"record_type": "tool_action", "record_id": tool_action.tool_action_id},
                    {"record_type": "policy_check", "record_id": policy_check.policy_check_id},
                ],
            },
        )
        self._record_event(
            tool_action.run_id,
            EventType.APPROVAL_GATE_REQUESTED,
            actor_id,
            {
                "description": "Approval Gate requested.",
                "record_refs": [{"record_type": "approval_request", "record_id": approval.approval_request_id}],
            },
        )
        return tool_action

    def _record_event(
        self,
        run_id: str,
        event_type: EventType,
        actor_id: str | None,
        payload: dict[str, Any],
    ) -> RunEvent:
        if run_id not in self.store.runs:
            raise InvariantViolation(f"Cannot record event for missing Run: {run_id}")
        if actor_id is not None and actor_id not in self.store.actors:
            raise InvariantViolation(f"Cannot record event for missing Actor: {actor_id}")

        event = RunEvent(
            event_id=new_id("evt"),
            run_id=run_id,
            event_type=event_type,
            event_version=1,
            occurred_at=utc_now(),
            actor_id=actor_id,
            payload=payload,
        )
        self.store.events.append(event)
        return event

    def _require_actor(self, actor_id: str) -> Actor:
        if actor_id not in self.store.actors:
            raise InvariantViolation(f"Actor does not exist: {actor_id}")
        return self.store.actors[actor_id]

    def _require_run(self, run_id: str) -> Run:
        if run_id not in self.store.runs:
            raise InvariantViolation(f"Run does not exist: {run_id}")
        return self.store.runs[run_id]

    def _require_tool_action(self, tool_action_id: str) -> ToolAction:
        if tool_action_id not in self.store.tool_actions:
            raise InvariantViolation(f"Tool Action does not exist: {tool_action_id}")
        return self.store.tool_actions[tool_action_id]
