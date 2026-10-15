from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@patch("main.ask_case_agent", new_callable=AsyncMock)

def test_existing_customer(mock_ask_case_agent):
    mock_ask_case_agent.return_value = {
        "answer": (
            "Case CLM-202 is currently awaiting documents "
            "because the repair estimate is missing."
        ),
        "recommended_action": (
            "Ask the customer to provide the repair estimate."
        ),
        "approval_required": True,
    }
    
    response = client.post(
        "/agent/query",
        json={
            "customer_id": "CUST-101",
            "question": "What is holding up the claim?"
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "customer_id": "CUST-101",
        "case_id": "CLM-202",
        "answer": (
            "Case CLM-202 is currently awaiting documents "
            "because the repair estimate is missing."
        ),
        "recommended_action": (
            "Ask the customer to provide the repair estimate."
        ),
        "approval_required": True
    }


def test_unknown_customer():
    response = client.post(
        "/agent/query",
        json={
            "customer_id": "CUST-999",
            "question": "What is holding up the claim?"
        }
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "No case found for this customer"
    }

def test_empty_customer_id():
    response = client.post(
        "/agent/query",
        json={
            "customer_id": "",
            "question": "What is holding up the claim?"
        }
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == [
        "body", "customer_id"
    ]
