import subprocess
from pathlib import Path
import sys
from pathlib import Path
import os

def create_local_repository(name: str, remote_url: str) -> None: 
    directory = Path(name)
    directory.mkdir(parents=True, exist_ok=True)
    readme_path = os.path.join(directory, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {name}\n\nRepository created with autogit CLI.\n")
    commands = [["git", "init"],["git", "add", "."],["git", "commit", "-m", "Initial commit"],["git", "branch", "-M", "main"],["git", "remote", "add", "origin", remote_url],["git", "push", "-u", "origin", "main"]]
    for c in commands:
        subprocess.run(c, cwd=directory, check=True, capture_output=True, text=True)
