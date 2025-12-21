import os
import shutil
from pathlib import Path
import re

# =============================
# CONFIGURATION
# =============================
README_TEMPLATE = """# {repo_name}

![Build Status](https://img.shields.io/badge/build-pending-lightgrey)
![Python Version](https://img.shields.io/badge/python-3.x-blue)
![GitHub Repo](https://img.shields.io/badge/github-repo-yes-green)

## Project Overview
Describe your project purpose and tech stack here.

## Installation
Step-by-step instructions to install and run your project.

## Features
Highlight key functionality of your project.

## Usage
Provide usage examples, screenshots, or GIFs:
![Example](docs/screenshots/example.png)

## License
Specify your license (e.g., MIT, GPL, Apache).
"""

# =============================
# STEP 0: PATH SETUP
# =============================
repo_path_input = input("Enter path to your GitHub repository (or press Enter for current directory): ").strip()
repo_path = Path(repo_path_input) if repo_path_input else Path(os.getcwd())

# =============================
# STEP 1: README.md
# =============================
readme_path = repo_path / "README.md"
if not readme_path.exists():
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(README_TEMPLATE.format(repo_name=repo_path.name))
    print("✅ README.md created with boilerplate sections.")
else:
    print("ℹ README.md already exists, skipping creation (you can merge content manually).")

# =============================
# STEP 2: PROJECT STRUCTURE
# =============================
folders = ["src", "docs", "docs/screenshots", "scripts"]
for folder in folders:
    folder_path = repo_path / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    print(f"✅ Folder created: {folder_path}")

# Move .py scripts to src/ or scripts/ if they are in root
for py_file in repo_path.glob("*.py"):
    if py_file.name != "Portfolio validator.py":  # don't move validator itself
        dest = repo_path / "src" / py_file.name
        shutil.move(str(py_file), str(dest))
        print(f"📦 Moved {py_file.name} → src/")

# =============================
# STEP 3: PYTHON SCRIPTS CLEANUP
# =============================
def add_docstring_placeholder(content):
    #
"""TODO: Add description""" Add docstring to function or class if missing
    def replacer(match):
        line = match.group(0)
        indent = " " * (len(line) - len(line.lstrip()))
        return f"{line}\n{indent}\"\"\"TODO: Add description\"\"\""
    content = re.sub(r"^(def .+?:|class .+?:)(\n( {4,}.+?)*)?", replacer, content, flags=re.MULTILINE)
    return content

for py_file in (repo_path / "src").glob("*.py"):
    try:
        content = py_file.read_text(encoding="utf-8")
        # Remove TODO/FIXME comments
        content = re.sub(r"#\s*TODO.*", "", content)
        content = re.sub(r"#\s*FIXME.*", "", content)
        # Add docstring placeholders
        content = add_docstring_placeholder(content)
        py_file.write_text(content, encoding="utf-8")
        print(f"🛠 Cleaned and updated {py_file.name}")
    except Exception as e:
        print(f"❌ Failed to process {py_file.name}: {e}")

# =============================
# STEP 4: SCREENSHOTS FOLDER
# =============================
screenshots_folder = repo_path / "docs" / "screenshots"
screenshots_folder.mkdir(exist_ok=True)
print(f"📸 Screenshots folder ready: {screenshots_folder}")

# =============================
# STEP 5: NEXT STEP
# =============================
print("\n🎯 Repo structure and README boilerplate ready. Next: Add screenshots and actual content, then rerun validator.")
