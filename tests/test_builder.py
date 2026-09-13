from src.providers.openai import OpenAIProvider
from src.agents.planner import Planner
from src.agents.builder import Builder


provider = OpenAIProvider()

planner = Planner(provider)
builder = Builder(provider)

task = "Build a simple Python program that organizes files in my Downloads folder."

plan = planner.make_plan(
    task,
    "Keep it simple. Use rule-based classification by file extension."
)

print("\n--- PLAN ---")
print(plan)

result = builder.build(task, plan)

print("\n--- FILES ---")

if result:
    for file in result["files"]:
        print("\nFILE:", file["path"])
        print(file["content"])