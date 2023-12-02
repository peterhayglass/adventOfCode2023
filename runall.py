import os
import subprocess
from pathlib import Path


def get_subdirs(path: Path) -> list[Path]:
    return sorted([d for d in path.iterdir() if d.is_dir()])


def run_main_files(subdirectories: list[Path]) -> None:
    for subdir in subdirectories:
        main_file = subdir / "main.py"
        if main_file.is_file():
            print(f"\nRunning {subdir.relative_to(Path(__file__).resolve().parent)}:")
            subprocess.run(["python", str(main_file)])


if __name__ == "__main__":
    current_directory = Path(__file__).resolve().parent
    subdirs = get_subdirs(current_directory)
    run_main_files(subdirs)