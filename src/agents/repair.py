import json

from src.providers.openai import OpenAIProvider


class Repair:
    def __init__(self, provider):
        self.provider = provider

    def repair(self, task, files, critic_feedback=None, test_result=None):
        prompt = f"""
You are the repair agent for FORGE.

A builder created code for a software task, but the code has a problem.

Your job is to fix the code based on the feedback you receive.

USER TASK:
{task}

CURRENT FILES:
{json.dumps(files, indent=2)}

CRITIC FEEDBACK:
{json.dumps(critic_feedback, indent=2)}

TEST RESULT:
{json.dumps(test_result, indent=2)}

Return ONLY valid JSON using this format:

{{
    "files": [
        {{
            "path": "main.py",
            "content": "full corrected file content"
        }}
    ]
}}

Rules:
- Fix the actual problems identified by the feedback.
- If tests failed, fix the cause of the test failure.
- If the critic identified unnecessary complexity, simplify the code.
- Keep the existing implementation where possible.
- Do not add unnecessary features.
- Do not change requirements that were not requested.
- Return complete file contents.
- Do not use markdown code blocks.

This is a small student portfolio project.
Prefer simple Python solutions that a student can understand.
"""

        result = self.provider.generate(prompt)

        try:
            return json.loads(result)
        except json.JSONDecodeError:
            print("The repair agent returned invalid JSON.")
            return None