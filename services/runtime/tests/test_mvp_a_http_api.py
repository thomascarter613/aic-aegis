import json
import tempfile
import threading
import unittest
from urllib import request

from aegis_mvp_a.http_api import create_server


class MvpAHttpApiTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.server = create_server('127.0.0.1', 0)
        self.port = self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base_url = f'http://127.0.0.1:{self.port}'

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=5)
        self.tmp.cleanup()

    def get_json(self, path):
        with request.urlopen(self.base_url + path, timeout=5) as response:
            return response.status, json.loads(response.read().decode('utf-8'))

    def post_json(self, path, payload):
        data = json.dumps(payload).encode('utf-8')
        req = request.Request(self.base_url + path, data=data, headers={'content-type': 'application/json'}, method='POST')
        with request.urlopen(req, timeout=5) as response:
            return response.status, json.loads(response.read().decode('utf-8'))

    def test_health(self):
        status, payload = self.get_json('/health')
        self.assertEqual(status, 200)
        self.assertEqual(payload['status'], 'ok')
        self.assertIn('platform disposes', payload['core_law'])

    def test_demo_safe_mock_executes(self):
        status, payload = self.post_json('/v1/demo', {'scenario': 'safe'})
        self.assertEqual(status, 200)
        self.assertEqual(payload['tool_action']['status'], 'mock_executed')
        self.assertGreater(len(payload['evidence_pack']['artifacts']), 0)
        self.assertGreater(len(payload['timeline']['items']), 0)

    def test_demo_risky_requires_approval_without_approve_flag(self):
        status, payload = self.post_json('/v1/demo', {'scenario': 'risky'})
        self.assertEqual(status, 200)
        self.assertEqual(payload['tool_action']['status'], 'approval_required')
        self.assertEqual(payload['approval_request']['status'], 'requested')
        self.assertIsNone(payload['tool_action']['mock_result'])

    def test_demo_risky_approve_resumes_mock_execution(self):
        status, payload = self.post_json('/v1/demo', {'scenario': 'risky', 'approve': True})
        self.assertEqual(status, 200)
        self.assertEqual(payload['tool_action']['status'], 'mock_executed')
        self.assertEqual(payload['approval_request']['status'], 'approved')

    def test_demo_blocked_never_executes(self):
        status, payload = self.post_json('/v1/demo', {'scenario': 'blocked'})
        self.assertEqual(status, 200)
        self.assertEqual(payload['tool_action']['status'], 'blocked')
        self.assertIsNone(payload['tool_action']['mock_result'])

    def test_step_by_step_safe_proof_loop(self):
        status, run_payload = self.post_json('/v1/runs', {'workflow': 'Governed Sales/Ops Follow-Up', 'purpose': 'Step-by-step API test'})
        self.assertEqual(status, 201)
        run_id = run_payload['run']['run_id']
        status, proposal_payload = self.post_json(f'/v1/runs/{run_id}/mock-proposals', {'scenario': 'safe'})
        self.assertEqual(status, 201)
        tool_action_id = proposal_payload['tool_action']['tool_action_id']
        status, broker_payload = self.post_json(f'/v1/tool-actions/{tool_action_id}/broker', {})
        self.assertEqual(status, 200)
        self.assertEqual(broker_payload['tool_action']['status'], 'mock_executed')
        self.assertEqual(broker_payload['policy_check']['disposition'], 'mock')
        status, evidence_payload = self.post_json(f'/v1/runs/{run_id}/evidence-packs', {})
        self.assertEqual(status, 201)
        self.assertGreater(len(evidence_payload['evidence_pack']['artifacts']), 0)
        status, timeline_payload = self.get_json(f'/v1/runs/{run_id}/timeline')
        self.assertEqual(status, 200)
        event_types = [item['event_type'] for item in timeline_payload['timeline']['items']]
        self.assertIn('ProposalSubmitted', event_types)
        self.assertIn('PolicyCheckCompleted', event_types)
        self.assertIn('ToolActionMockExecuted', event_types)


if __name__ == '__main__':
    unittest.main()
