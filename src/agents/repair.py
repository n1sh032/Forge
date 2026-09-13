import json

from src.providers.openai import OpenAIProvider


class Repair:
    def __init__(self, provider):
        self.provider = provider

    def repair(self, task, files, test_result):
        prompt = f"""
You are the repair agent for FORGE.

A builder created code for a software task, but the tests failed.

Your job is to fix the code based on the test failure.

USER TASK:
{task}

CURRENT FILES:
{json.dumps(files, indent=2)}

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
- Fix the actual problem shown by the test result.
- Keep the existing implementation where possible.
- Do not add unnecessary features.
- Return complete file contents.
- Do not use markdown code blocks.
"""

        result = self.provider.generate(prompt)

        try:
            return json.loads(result)
        except json.JSONDecodeError:
            print("The repair agent returned invalid JSON.")
            return None