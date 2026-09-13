from pathlib import Path

from src.tools.file_writer import write_files


project_dir = Path("test_project")

files = [
    {
        "path": "src/main.py",
        "content": 'print("Hello from FORGE")\n'
    },
    {
        "path": "src/utils.py",
        "content": 'def hello():\n    return "Hello"\n'
    }
]

write_files(files, project_dir)