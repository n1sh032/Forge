import subprocess


def run_tests(project_dir):
    result = subprocess.run(
        ["python", "main.py"],
        cwd=project_dir,
        capture_output=True,
        text=True
    )

    return {
        "success": result.returncode == 0,
        "output": result.stdout,
        "error": result.stderr,
        "return_code": result.returncode
    }