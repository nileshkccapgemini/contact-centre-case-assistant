from google.adk.runners import InMemoryRunner
from case_assistant.agent import root_agent

runner = InMemoryRunner(agent=root_agent)

import asyncio

events = asyncio.run(
    runner.run_debug(
        """
        Case facts:
        case_id: CLM-202
        status: Awaiting documents
        missing_document: Repair estimate

        Question: What is holding up the claim?
        """
    )
)