# Sales/Ops Assistant Example

This is the canonical MVP workflow.

## Flow

1. User submits a customer conversation.
2. Aegis creates a run envelope.
3. Memory service retrieves allowed customer memory.
4. Runtime prompts the model.
5. Model proposes CRM and email actions.
6. Tool Broker allows draft creation but requires approval for send.
7. Evidence service generates an evidence pack.
8. Eval service scores the workflow.
9. Feedback is captured.
10. Memory Admission Gate accepts, rejects, or queues memory candidates.
