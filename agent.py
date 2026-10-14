def answer_case_question(question: str, case: dict) -> dict:
    return {
        "answer": (
            f"Case {case['case_id']} is currently "
            f"{case['status'].lower()} because the "
            f"{case['missing_document'].lower()} is missing."
        ),
        "recommended_action": (
            f"Ask the customer to provide the "
            f"{case['missing_document'].lower()}."
        ),
        "approval_required": True
    }