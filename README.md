# Contact Centre Case Assistant

## Problem

Contact-centre advisers need to understand a customer case quickly and identify the correct next action.

## First Use Case

An adviser submits a customer ID and a question.

The agent retrieves mock customer and case data, summarises the current case status, and recommends the next action.

The agent must not make any case update without adviser approval.

## Initial API

### Endpoint

`POST /agent/query`

### Request

```json
{
  "customer_id": "CUST-101",
  "question": "What is holding up the claim?"
}
```

### Response

```json
{
  "case_id": "CLM-202",
  "summary": "The claim is awaiting a repair estimate.",
  "recommended_action": "Ask the customer to upload the repair estimate.",
  "approval_required": true
}
```

## First Success Criteria

- A REST API exposes the agent capability.
- The correct mock case is retrieved.
- The response is grounded in the case data.
- No case update occurs without human approval.
- Invalid requests return a controlled error.
- The behaviour is covered by automated tests.