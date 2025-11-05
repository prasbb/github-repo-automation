import os 
import requests
import sys

def create_repository(name: str, private: bool = False, description: str  = "default description") -> None: 
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Missing token in env.")
        sys.exit(1)
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    payload = {"name": name, "description": description, "private": private}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("Repository successfully created.")
    else:
         print(f"Failed to create repository with state code {response.status_code}: {response.text}")
