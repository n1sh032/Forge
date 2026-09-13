import subprocess


def run_tests(project_dir, tests):
    results = []

    for test in tests:
        try:
            result = subprocess.run(
                ["python", "main.py"],
                cwd=project_dir,
                input=test["input"],
                capture_output=True,
                text=True,
                timeout=10
            )

            output = result.stdout.strip()
            expected = test["expected_output"].strip()

            success = (
                result.returncode == 0
                and output == expected
            )

            results.append({
                "success": success,
                "input": test["input"],
                "expected_output": expected,
                "output": output,
                "error": result.stderr,
                "return_code": result.returncode
            })

        except subprocess.TimeoutExpired:
            results.append({
                "success": False,
                "input": test["input"],
                "expected_output": test["expected_output"],
                "output": "",
                "error": "Program timed out after 10 seconds.",
                "return_code": -1
            })

    return {
        "success": all(test["success"] for test in results),
        "tests": results
    }