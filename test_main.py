from agent import answer_case_question
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_existing_customer():
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

def test_answer_case_question():
    case = {
        "case_id": "CLM-202",
        "status": "Awaiting documents",
        "missing_document": "Repair estimate"
    }

    result = answer_case_question(
        "What is holding up the claim?",
        case
    )

    assert result == {
        "answer": (
            "Case CLM-202 is currently awaiting documents "
            "because the repair estimate is missing."
        ),
        "recommended_action": (
            "Ask the customer to provide the repair estimate."
        ),
        "approval_required": True
    }