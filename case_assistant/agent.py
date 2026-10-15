from pydantic import BaseModel
from google.adk.agents.llm_agent import Agent


class CaseAgentResponse(BaseModel):
    answer: str
    recommended_action: str
    approval_required: bool

root_agent = Agent(
    name="case_assistant",
    model="gemini-3.8-flash",
    description="Answers adviser questions about customer cases.",
    instruction=(
        "You are a contact-centre case assistant. "
        "Answer the adviser's question using only the case facts provided. "
        "Do not invent case information. "
        "If the case facts do not contain the answer, say that the information "
        "is not available in the case. "
        "Recommend a sensible next action when the case facts support one. "
        "Always set approval_required to true because a human adviser must approve any recommended action. "
        "Do not make changes to the case."
    ),
    output_schema=CaseAgentResponse,
)