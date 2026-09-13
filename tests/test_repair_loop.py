from pathlib import Path

from src.providers.openai import OpenAIProvider
from src.agents.repair import Repair
from src.tools.file_writer import write_files
from src.tools.test_runner import run_tests


provider = OpenAIProvider()
repair = Repair(provider)

project_dir = Path("repair_test_project")

task = "Create a Python program that prints exactly: Hello from FORGE"

files = [
    {
        "path": "main.py",
        "content": 'print("Hello from FORGE"'
    }
]

write_files(files, project_dir)

print("\n--- FIRST TEST ---")

test_result = run_tests(project_dir)

print("Success:", test_result["success"])
print("Error:", test_result["error"])

if not test_result["success"]:
    print("\n--- REPAIRING ---")

    repaired = repair.repair(
        task,
        files,
        test_result
    )

    if repaired:
        write_files(
            repaired["files"],
            project_dir
        )

        print("\n--- SECOND TEST ---")

        test_result = run_tests(project_dir)

        print("Success:", test_result["success"])
        print("Output:", test_result["output"])
        print("Error:", test_result["error"])