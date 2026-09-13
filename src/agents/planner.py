import json

from src.providers.openai import OpenAIProvider


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
        "test 1",
        "test 2"
    ]
}}

Do not write any code.
Keep the plan practical and simple.
"""

        result = self.provider.generate(prompt)

        try:
            plan = json.loads(result)
            return plan
        except json.JSONDecodeError:
            print("The planner returned invalid JSON.")
            return None