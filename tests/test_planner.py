from src.providers.openai import OpenAIProvider
from src.agents.planner import Planner


provider = OpenAIProvider()

planner = Planner(provider)

plan = planner.create_plan(
    task="Build a Python program that automatically organizes files in my Downloads folder.",
    context="The program should eventually support machine-learning based classification."
)

print(plan)