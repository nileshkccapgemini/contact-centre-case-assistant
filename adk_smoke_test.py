import asyncio

from adk_runner import ask_case_agent


case = {
    "case_id": "CLM-202",
    "status": "Awaiting documents",
    "missing_document": "Repair estimate",
}

events = asyncio.run(
    ask_case_agent(
        "What is holding up the claim?",
        case,
    )
)

print(events)