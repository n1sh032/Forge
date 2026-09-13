from pathlib import Path

from src.providers.openai import OpenAIProvider
from src.agents.planner import Planner
from src.agents.builder import Builder
from src.tools.file_writer import write_files


provider = OpenAIProvider()

planner = Planner(provider)
builder = Builder(provider)

task = """
Build a simple Python program that creates a greeting message.

The program should have a main.py file and print:
Hello from FORGE
"""

plan = planner.make_plan(task)

print("\n--- PLAN ---")
print(plan)

result = builder.build(task, plan)

print("\n--- BUILDER FILES ---")

if result:
    for file in result["files"]:
        print(file["path"])

    project_dir = Path("generated_project")

    write_files(
        result["files"],
        project_dir
    )

    print("\nProject created successfully.")