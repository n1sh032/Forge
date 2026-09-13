from src.providers.openai import OpenAIProvider
from src.orchestrator import Orchestrator


provider = OpenAIProvider()

forge = Orchestrator(provider)

task = """
Create a Python program called main.py that prints exactly:

Hello from FORGE
"""

forge.run(task)