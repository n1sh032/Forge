from src.providers.openai import OpenAIProvider
from src.agents.repair import Repair


provider = OpenAIProvider()
repair = Repair(provider)

task = "Create a Python program that prints exactly: Hello from FORGE"

files = [
    {
        "path": "main.py",
        "content": 'print("Hello from FORGE"'
    }
]

test_result = {
    "success": False,
    "output": "",
    "error": "SyntaxError: '(' was never closed",
    "return_code": 1
}

result = repair.repair(
    task,
    files,
    test_result
)

print("\n--- REPAIR RESULT ---")

if result:
    for file in result["files"]:
        print("\nFILE:", file["path"])
        print(file["content"])