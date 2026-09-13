import json

from src.providers.openai import OpenAIProvider


class Critic:
    def __init__(self, provider):
        self.provider = provider

    def review(self, task, plan, files):
        prompt = f"""
You are the critic agent for FORGE.

Review the code produced by the builder.

USER TASK:
{task}

PLAN:
{json.dumps(plan, indent=2)}

BUILDER FILES:
{json.dumps(files, indent=2)}

Check whether the implementation:
- follows the plan
- satisfies the requirements
- avoids unnecessary features
- contains obvious problems

Return ONLY valid JSON:

{{
    "approved": true,
    "issues": [
        "issue 1",
        "issue 2"
    ]
}}

If there are no important issues, return an empty issues list.

Do not rewrite the code.
Keep the review practical and concise.
"""

        result = self.provider.generate(prompt)

        try:
            return json.loads(result)
        except json.JSONDecodeError:
            print("The critic returned invalid JSON.")
            return None