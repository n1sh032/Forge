import json


class Builder:
    def __init__(self, provider):
        self.provider = provider

    def build(self, task, plan):
        prompt = f"""
You are the builder agent for FORGE.

Build the software described below.

USER TASK:
{task}

PLAN:
{json.dumps(plan, indent=2)}

Return ONLY valid JSON using this format:

{{
    "files": [
        {{
            "path": "src/main.py",
            "content": "full file content here"
        }}
    ]
}}

Rules:
- Keep the implementation simple.
- This is a student portfolio project.
- Only create files that are needed.
- Don't add unnecessary frameworks.
- Include basic error handling where needed.
- Return the complete contents of every file.
- Do not use markdown code blocks.
- The generated project must have main.py at the project root.
- Do not place the generated main.py inside src/.
"""

        result = self.provider.generate(prompt)

        try:
            return json.loads(result)
        except json.JSONDecodeError:
            print("The builder returned invalid JSON.")
            return None