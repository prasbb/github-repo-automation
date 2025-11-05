# github-repo-automation

# AutoGit

A Python CLI tool to **automatically create GitHub repositories** from the command line, initialize them locally, and optionally set up a **Python CI/CD workflow** using GitHub Actions.

---

## Features

- Create a GitHub repository directly from the CLI  
- Initialize a local Git repository and push to GitHub  
- Automatically add a **README.md**  
- Optional CI/CD workflow for Python projects with GitHub Actions  

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/github-repo-automation.git
cd github-repo-automation

# Install dependencies
pip install -r requirements.txt

# Install as a CLI tool
pip install -e .

# Make sure to create a .env file in the project root with your GitHub personal access token:
GITHUB_TOKEN=your_personal_access_token_here

# Usage
# Create a new repository

autogit my-new-repo

Flags:
-d "description" → Add a repository description
--private → Create a private repository

autogit my-new-repo -d "My automated GitHub repo" --private

---
Much of this project is customized to my own preferences and workflow.  
The main goal was to **simplify creating GitHub repositories and setting up a CI/CD pipeline** for Python projects.  
It is designed as a learning exercise and a personal productivity tool, but it can be adapted for general use.
