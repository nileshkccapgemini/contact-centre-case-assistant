from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from mock_cases import MOCK_CASES

app = FastAPI(title="Contact Centre Case Assistant")


class AgentRequest(BaseModel):
    customer_id: str = Field(min_length=1)
    question: str = Field(min_length=1)

class CaseResponse(BaseModel):
    customer_id: str
    case_id: str
    status: str
    missing_document: str

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/agent/query", response_model=CaseResponse)
def query_agent(request: AgentRequest):
    case = MOCK_CASES.get(request.customer_id)

    if case is None:
        raise HTTPException(
            status_code=404,
            detail="No case found for this customer"
        )

    return {
        "customer_id": request.customer_id,
        "case_id": case["case_id"],
        "status": case["status"],
        "missing_document": case["missing_document"]
    }