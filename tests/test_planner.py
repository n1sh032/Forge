from src.providers.openai import OpenAIProvider
from src.agents.planner import Planner


provider = OpenAIProvider()

planner = Planner(provider)

plan = planner.make_plan(
    "Build a Python program that automatically organizes files in my Downloads folder.",
    "The program should eventually support machine learning."
)

print("\nGOAL:")
print(plan["goal"])

print("\nSTEPS:")
for step in plan["steps"]:
    print("-", step)