import subprocess
from pathlib import Path

def create_local_repository(name: str, remote_url: str) -> None: 
    directory = Path(name)
    directory.mkdir(exist_ok=True)
    commands = [["git", "init"],["git", "add", "."],["git", "commit", "-m", "Initial commit"],["git", "branch", "-M", "main"],["git", "remote", "add", "origin", remote_url],["git", "push", "-u", "origin", "main"]]
    for c in commands:
        subprocess.run(c, cwd=directory, check=True)
