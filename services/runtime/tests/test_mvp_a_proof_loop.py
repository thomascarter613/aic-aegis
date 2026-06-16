import tempfile
import unittest
from pathlib import Path

from aegis_mvp_a.application import AegisMvpA, EvidenceWriter, InMemoryStore
from aegis_mvp_a.domain import (
    ActorType,
    ApprovalStatus,
    Disposition,
    EventType,
    InvariantViolation,
    ProposalStatus,
    ToolActionStatus,
)


class MvpAProofLoopTests(unittest.TestCase):
    def make_app(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        store = InMemoryStore()
        app = AegisMvpA(store=store)
        app.evidence_writer = EvidenceWriter(store, Path(tmp.name))
        return app

    def test_safe_scenario_mock_executes_and_generates_evidence(self):
        app = self.make_app()
        result = app.run_demo("safe")

        self.assertEqual(result["tool_action"].status, ToolActionStatus.MOCK_EXECUTED)
        self.assertIsNotNone(result["tool_action"].mock_result)
        self.assertGreater(len(result["evidence_pack"].artifacts), 0)

        event_types = [item.event_type for item in result["timeline"].items]
        self.assertIn(EventType.PROPOSAL_SUBMITTED, event_types)
        self.assertIn(EventType.POLICY_CHECK_COMPLETED, event_types)
        self.assertIn(EventType.TOOL_ACTION_MOCK_EXECUTED, event_types)

    def test_risky_scenario_requires_approval_and_does_not_execute_before_approval(self):
        app = self.make_app()
        human = app.create_actor(ActorType.HUMAN, "Operator")
        model = app.create_actor(ActorType.MOCK_MODEL, "Mock Model")
        run = app.create_run("Governed Sales/Ops Follow-Up", "Risky test", human.actor_id)
        _, tool_action = app.propose_tool_action(run.run_id, model.actor_id, "risky")

        result = app.broker_tool_action(tool_action.tool_action_id, human.actor_id)

        self.assertEqual(result.status, ToolActionStatus.APPROVAL_REQUIRED)
        self.assertIsNone(result.mock_result)
        approval = app.store.approval_for_tool_action(tool_action.tool_action_id)
        self.assertIsNotNone(approval)
        self.assertEqual(approval.status, ApprovalStatus.REQUESTED)

    def test_risky_scenario_can_resume_after_approval(self):
        app = self.make_app()
        result = app.run_demo("risky", approve=True)

        self.assertEqual(result["approval_request"].status, ApprovalStatus.APPROVED)
        self.assertEqual(result["tool_action"].status, ToolActionStatus.MOCK_EXECUTED)
        self.assertIsNotNone(result["tool_action"].mock_result)

    def test_blocked_scenario_never_executes(self):
        app = self.make_app()
        result = app.run_demo("blocked")

        self.assertEqual(result["tool_action"].status, ToolActionStatus.BLOCKED)
        self.assertIsNone(result["tool_action"].mock_result)

    def test_cannot_broker_tool_action_without_proposal(self):
        app = self.make_app()
        human = app.create_actor(ActorType.HUMAN, "Operator")
        model = app.create_actor(ActorType.MOCK_MODEL, "Mock Model")
        run = app.create_run("Governed Sales/Ops Follow-Up", "Invariant test", human.actor_id)
        proposal, tool_action = app.propose_tool_action(run.run_id, model.actor_id, "safe")
        del app.store.proposals[proposal.proposal_id]

        with self.assertRaises(InvariantViolation):
            app.broker_tool_action(tool_action.tool_action_id, human.actor_id)

    def test_policy_check_exists_before_mock_execution(self):
        app = self.make_app()
        human = app.create_actor(ActorType.HUMAN, "Operator")
        model = app.create_actor(ActorType.MOCK_MODEL, "Mock Model")
        run = app.create_run("Governed Sales/Ops Follow-Up", "Policy ordering test", human.actor_id)
        proposal, tool_action = app.propose_tool_action(run.run_id, model.actor_id, "safe")

        app.broker_tool_action(tool_action.tool_action_id, human.actor_id)

        policy = app.store.policy_for_tool_action(tool_action.tool_action_id)
        self.assertIsNotNone(policy)
        self.assertEqual(policy.disposition, Disposition.MOCK)
        self.assertEqual(app.store.proposals[proposal.proposal_id].status, ProposalStatus.MOCK_EXECUTED)

    def test_evidence_pack_contains_proposal_policy_tool_and_timeline_artifacts(self):
        app = self.make_app()
        result = app.run_demo("safe")
        artifact_types = {artifact.artifact_type for artifact in result["evidence_pack"].artifacts}

        self.assertIn("proposal", artifact_types)
        self.assertIn("policy_check", artifact_types)
        self.assertIn("tool_action", artifact_types)
        self.assertIn("timeline", artifact_types)


if __name__ == "__main__":
    unittest.main()
