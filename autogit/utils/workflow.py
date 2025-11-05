import base64
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

CD_YAML = """\
name: Python CI/CD
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
"""

def add_workflow(repo: str) -> None:
    directory = Path(repo)
    directory.mkdir(parents=True, exist_ok=True)
    workflow_dir = directory / ".github" / "workflows"
    workflow_dir.mkdir(parents=True, exist_ok=True)
    workflow_file = workflow_dir / "ci.yml"
    workflow_file.write_text(CD_YAML)
    url = f"https://api.github.com/repos/user/{repo}/contents/.github/workflows/ci.yml"
    content = base64.b64encode(CD_YAML.encode()).decode()
    data = {"message": "Add CI workflow", "content": content, "branch": "main"}
    response = requests.put(url, headers=HEADERS, json=data)
    return response.json()