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
- satisfies the user's actual requirements
- follows the plan
- has obvious bugs
- has unnecessary features or complexity
- has error handling that could cause problems

Return ONLY valid JSON:

{{
    "approved": true,
    "issues": []
}}

IMPORTANT:
- Set approved to false if there is any important issue.
- Set approved to true ONLY when there are no important issues.
- If approved is false, include every important issue in the issues list.
- Do not reject code for harmless style preferences.
- Do not invent requirements that the user did not ask for.
- Do not rewrite the code.

This is a small student portfolio project.
Prefer simple Python solutions that a student can understand.
"""

        result = self.provider.generate(prompt)

        try:
            critique = json.loads(result)

            if critique["issues"]:
                critique["approved"] = False
            else:
                critique["approved"] = True

            return critique

        except (json.JSONDecodeError, KeyError, TypeError):
            print("The critic returned invalid JSON.")
            return None