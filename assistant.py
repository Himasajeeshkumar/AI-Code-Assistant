from retriever import search_code

def explain_code(result):

    explanation = f"""
Language: {result['language']}

What this code does:
{result['docstring']}

Code Example:
{result['code']}
"""

    return explanation


def ask_assistant(question):

    results = search_code(question)

    question_lower = question.lower()

    filtered_results = []

    for r in results:
        if r["language"] in question_lower:
            filtered_results.append(r)

    if len(filtered_results) == 0:
        filtered_results = results

    answers = []

    for r in filtered_results:
        answers.append(explain_code(r))

    return "\n\n----------------\n\n".join(answers)