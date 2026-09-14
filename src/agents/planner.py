import json



class Planner:
    def __init__(self, provider):
        self.provider = provider

    def make_plan(self, task, context=""):
        prompt = f"""
You are the planning agent for FORGE.

Turn the user's software task into a simple implementation plan.

Task:
{task}

Extra context:
{context}

Return ONLY valid JSON in this format:

{{
    "goal": "what the software should do",
    "requirements": [
        "requirement 1",
        "requirement 2"
    ],
    "steps": [
        "step 1",
        "step 2"
    ],
    "tests": [
        {{
            "input": "input to give the program",
            "expected_output": "expected output"
        }}
    ]
}}

Rules:

- Only include requirements directly implied by the user's task.
- Do not invent unnecessary features.
- Do not invent arbitrary output formatting.
- Tests must verify the user's actual requirements.
- If the program requires user input, provide realistic test input.
- If the program does not require input, use an empty input string.
- Keep tests simple and deterministic.
- Do not write any code.

This is a small student portfolio project.
Prefer simple Python solutions that a student can understand.
"""

        result = self.provider.generate(prompt)

        try:
            plan = json.loads(result)
            return plan
        except json.JSONDecodeError:
            print("The planner returned invalid JSON.")
            return None