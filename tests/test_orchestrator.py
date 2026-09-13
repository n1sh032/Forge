from src.providers.openai import OpenAIProvider
from src.orchestrator import Orchestrator


provider = OpenAIProvider()

forge = Orchestrator(provider)

task = """
Create a Python program called main.py that prints exactly:

Hello from FORGE

The first version of the program should contain a syntax error.
FORGE should detect the failure and repair it automatically.
"""

forge.run(task)