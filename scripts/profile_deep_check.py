"""
Profile Deep Check
Purpose: [AWS automation script]
Author: Charles Bucher
"""

# Import required libraries
import os
import requests
from pathlib import Path


# -------------------------
# CONFIGURATION
# -------------------------
GITHUB_USERNAME = "charles-bucher"  # your GitHub username
PROFILE_REPO = "charles-bucher"     # your profile repo name
TOKEN = os.getenv("GITHUB_TOKEN")   # optional: GitHub personal access token for higher rate limits

HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

# -------------------------
# HELPER FUNCTIONS
# -------------------------
def get_repo_contents(repo, path=""):
    """
        Function to get_repo_contents.
    """

    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo}/contents/{path}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch {path}: {response.status_code}")
        return []
def analyze_readme(repo):
    """
        Function to analyze_readme.
    """

    contents = get_repo_contents(repo)
    readme = next((c for c in contents if c['name'].lower() == 'readme.md'), None)
    if readme:
        readme_url = readme['download_url']
        text = requests.get(readme_url).text
        lines = text.splitlines()
        word_count = sum(len(line.split()) for line in lines)
        sections = text.count("#")
        return {"exists": True, "lines": len(lines), "words": word_count, "sections": sections}
    return {"exists": False, "lines": 0, "words": 0, "sections": 0}
def count_scripts(repo, folder=""):
    """
        Function to count_scripts.
    """

    contents = get_repo_contents(repo, folder)
    scripts = {"python": 0, "bash": 0, "powershell": 0}
    for item in contents:
        if item['type'] == 'file':
            if item['name'].endswith(".py"): scripts["python"] += 1
            elif item['name'].endswith(".sh"): scripts["bash"] += 1
            elif item['name'].endswith(".ps1"): scripts["powershell"] += 1
        elif item['type'] == 'dir':
            sub_scripts = count_scripts(repo, item['path'])
            for k in scripts:
                scripts[k] += sub_scripts[k]
    return scripts
def deep_check_repo(repo):
    """
        Function to deep_check_repo.
    """

    print(f"\n🔎 Analyzing repo: {repo}")
    readme_info = analyze_readme(repo)
    scripts_info = count_scripts(repo)
    
    print(f"📄 README: {'Exists' if readme_info['exists'] else 'Missing'} | Sections: {readme_info['sections']} | Words: {readme_info['words']}")
    print(f"🛠️ Scripts: Python: {scripts_info['python']}, Bash: {scripts_info['bash']}, PowerShell: {scripts_info['powershell']}")
    
    cloud_keywords = ["aws", "ec2", "s3", "lambda", "vpc", "cloudwatch", "terraform", "cloudformation", "devops", "monitoring", "automation"]
    relevance = 0
    if readme_info["exists"]:
        readme_text = requests.get(get_repo_contents(repo)[0]['download_url']).text.lower()
        relevance = sum(1 for kw in cloud_keywords if kw in readme_text)
    print(f"☁️ Cloud relevance score (keywords matched): {relevance}/{len(cloud_keywords)}")

# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    repos_url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    repos = requests.get(repos_url, headers=HEADERS).json()
    
    for r in repos:
        deep_check_repo(r['name'])