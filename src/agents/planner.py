from src.providers.openai import OpenAIProvider


class Planner:
    def __init__(self, provider):
        self.provider = provider

    def make_plan(self, task, context=""):
        prompt = f"""
You are the planning agent for a project called FORGE.

Your job is to take a software task and turn it into a simple
plan that another AI agent can use to build the software.

Task:
{task}

Extra context:
{context}

Give the answer in this format:

GOAL:
Explain what the program should do.

REQUIREMENTS:
- requirement 1
- requirement 2
- requirement 3

STEPS:
1. step 1
2. step 2
3. step 3

TESTS:
- test 1
- test 2

Keep the plan practical and don't write the actual code.
"""

        result = self.provider.generate(prompt)

        return result