import json
from google.adk.runners import InMemoryRunner
from case_assistant.agent import root_agent

runner = InMemoryRunner(agent=root_agent)


async def ask_case_agent(question: str, case: dict):
    case_facts = json.dumps(case, indent=2)
    prompt = f"""
    Case facts:
    {case_facts}

    Question: {question}
    """

    events = await runner.run_debug(prompt, quiet=True) 
    response_text = events[-1].content.parts[0].text
    return json.loads(response_text)