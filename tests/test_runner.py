from pathlib import Path

from src.tools.test_runner import run_tests


project_dir = Path("generated_project")

result = run_tests(project_dir)

print("\n--- TEST RESULT ---")
print("Success:", result["success"])
print("Output:", result["output"])
print("Error:", result["error"])
print("Return code:", result["return_code"])