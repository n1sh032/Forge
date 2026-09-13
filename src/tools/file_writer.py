from pathlib import Path


def write_files(files, project_dir):
    project_dir = Path(project_dir).resolve()

    for file in files:
        file_path = (project_dir / file["path"]).resolve()

        # Don't allow the builder to write outside the project.
        if project_dir not in file_path.parents and file_path != project_dir:
            raise ValueError(f"Unsafe file path: {file['path']}")

        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file["content"])

        print(f"Wrote: {file_path}")