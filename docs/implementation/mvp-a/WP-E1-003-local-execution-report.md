---
title: WP-E1-003 Local Execution Report
project: AIC Aegis
product: AIC AI Reliability Control Plane
status: Generated
work_packet: WP-E1-003
last_updated: 2026-06-16
---

# WP-E1-003 Local Execution Report

## Test Command

```bash
PYTHONPATH=services/runtime python -m unittest discover -s services/runtime/tests -p "test_*.py"
```

## Test Return Code

```text
0
```

## Test Output

```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/generated/interface/models.py", line 30820, in hydrate_crdt_from_proto
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/rpc/remote.py", line 749, in __call__
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
.......
----------------------------------------------------------------------
Ran 7 tests in 0.018s

OK
```

## Demo Command

```bash
PYTHONPATH=services/runtime python -m aegis_mvp_a safe --evidence-root .aic/runtime/evidence
```

## Demo Return Code

```text
0
```

## Demo Output

```json
{
  "approval_request_id": null,
  "approval_status": null,
  "approved": false,
  "evidence_artifacts": 11,
  "evidence_pack_id": "ep_353132b490264e6eb388cc401f0c5346",
  "run_id": "run_7789a1d19f844e9ba5b21bf12087e2e4",
  "run_status": "completed",
  "scenario": "safe",
  "timeline_items": 7,
  "tool_action_id": "tool_59014fd629f24cab8a6f08d45bb701a7",
  "tool_action_status": "mock_executed"
}
```
