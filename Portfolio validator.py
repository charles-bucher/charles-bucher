import os
import json
from pathlib import Path
import re
import subprocess

class DeepPortfolioValidator:
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.readme_path = self.repo_path / "README.md"
        self.scores = {
            "readme": 0,
            "project_structure": 0,
            "python_scripts": 0,
            "screenshots": 0,
            "git_history": 0
        }
        self.fix_list = []

    # ============================
    # README Validation
    # ============================
    def validate_readme(self):
        if not self.readme_path.exists():
            self.fix_list.append("Add a README.md to your repository.")
            print("❌ README.md not found!")
            return

        try:
            content = self.readme_path.read_text(encoding="utf-8")
        except Exception as e:
            self.fix_list.append("Fix README.md encoding issues.")
            print(f"❌ Failed to read README.md: {e}")
            return

        # Check for essential sections
        sections = ["project overview", "installation", "usage", "features", "license"]
        missing_sections = [sec for sec in sections if sec.lower() not in content.lower()]
        if missing_sections:
            self.fix_list.append(f"README missing sections: {', '.join(missing_sections)}")
        else:
            self.scores["readme"] += 1
            print("✅ README sections complete.")

        # Check for badges
        if re.search(r"\[!\[.*\]\(.*\)\]", content):
            self.scores["readme"] += 0.5
        else:
            self.fix_list.append("Add badges to README (build, Python version, GitHub stars).")

        # Check formatting: headers and code blocks
        if re.search(r"# .+", content) and re.search(r"```.*```", content, re.DOTALL):
            self.scores["readme"] += 0.5
        else:
            self.fix_list.append("Improve README formatting: headers and code blocks.")

    # ============================
    # Project Structure
    # ============================
    def validate_project_structure(self):
        essential_folders = ["scripts", "src", "docs", "screenshots"]
        missing_folders = [f for f in essential_folders if not (self.repo_path / f).exists()]
        if missing_folders:
            self.fix_list.append(f"Missing essential folders: {', '.join(missing_folders)}")
        else:
            self.scores["project_structure"] = 1
            print("✅ Project structure looks solid.")

        # Check for orphaned Python files
        python_files = list(self.repo_path.glob("*.py"))
        if python_files:
            self.scores["project_structure"] += 0.5
        else:
            self.fix_list.append("Consider organizing Python scripts under 'src/' or 'scripts/'.")

    # ============================
    # Python Scripts Quality
    # ============================
    def validate_python_scripts(self):
        scripts = list(self.repo_path.glob("*.py")) + list((self.repo_path / "scripts").glob("*.py"))
        if not scripts:
            self.fix_list.append("Add Python scripts to demonstrate your skills.")
            return

        score = 0
        for script in scripts:
            try:
                content = script.read_text(encoding="utf-8")
                if "def " in content or "class " in content:
                    score += 0.5
                if re.search(r'"""', content):
                    score += 0.5
                if "TODO" in content or "FIXME" in content:
                    self.fix_list.append(f"Remove TODO/FIXME comments in {script.name}")
                    score -= 0.5
            except Exception as e:
                self.fix_list.append(f"Cannot read {script.name}: {e}")

        self.scores["python_scripts"] = max(0, min(score / len(scripts), 1))
        print(f"✅ Python script quality scored: {self.scores['python_scripts']*100:.0f}%")

    # ============================
    # Screenshots / Media
    # ============================
    def validate_screenshots(self):
        folder = self.repo_path / "screenshots"
        if folder.exists() and any(folder.iterdir()):
            images = [f for f in folder.iterdir() if f.suffix.lower() in [".png", ".jpg", ".gif"]]
            if images:
                self.scores["screenshots"] = 1
                print(f"✅ Found {len(images)} screenshot(s).")
            else:
                self.fix_list.append("Add proper image files (.png/.jpg/.gif) in 'screenshots' folder.")
        else:
            self.fix_list.append("Add a 'screenshots' folder with images of your projects.")

    # ============================
    # Git History
    # ============================
    def validate_git_history(self):
        try:
            commits = subprocess.check_output(
                ["git", "-C", str(self.repo_path), "rev-list", "--count", "HEAD"],
                stderr=subprocess.DEVNULL
            ).decode().strip()
            if int(commits) > 0:
                self.scores["git_history"] = 1
                print(f"✅ Git commit count: {commits}")
            else:
                self.fix_list.append("Add commits to your Git repository.")
        except Exception:
            self.fix_list.append("Git repository not initialized or cannot access git history.")

    # ============================
    # Compute Overall Score
    # ============================
    def compute_overall_score(self):
        weighted = (
            self.scores["readme"] * 0.35 +
            self.scores["project_structure"] * 0.2 +
            self.scores["python_scripts"] * 0.25 +
            self.scores["screenshots"] * 0.1 +
            self.scores["git_history"] * 0.1
        )
        return int(weighted * 100)

    def hiring_recommendation(self, score):
        if score >= 90:
            return "Highly recommended for interview."
        elif score >= 70:
            return "Recommended, but portfolio needs improvement."
        elif score >= 50:
            return "Low recommendation; fix critical issues."
        else:
            return "Not recommended until improvements are made."

    def print_summary(self):
        score = self.compute_overall_score()
        print("\n📊 Portfolio Summary")
        print(f"Overall Score: {score}%")
        print(f"Hiring Recommendation: {self.hiring_recommendation(score)}")
        if self.fix_list:
            print("\n🛠 Prioritized Fix List:")
            for fix in self.fix_list:
                print(f"- {fix}")
        else:
            print("\n🎉 Portfolio looks solid! No critical issues found.")

    def save_json_report(self):
        report = {
            "score": self.compute_overall_score(),
            "recommendation": self.hiring_recommendation(self.compute_overall_score()),
            "fix_list": self.fix_list,
            "scores": self.scores
        }
        json_path = self.repo_path / "portfolio_deep_report.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        print(f"\n💾 Deep JSON report saved to {json_path}")

    # ============================
    # Run All Checks
    # ============================
    def validate_all(self):
        self.validate_readme()
        self.validate_project_structure()
        self.validate_python_scripts()
        self.validate_screenshots()
        self.validate_git_history()
        self.print_summary()
        self.save_json_report()

def main():
    print("╔══════════════════════════════════════════════════╗")
    print("║      DEEP- DIVE PORTFOLIO VALIDATOR             ║")
    print("╚══════════════════════════════════════════════════╝\n")

    repo_path = input("Enter path to your GitHub repository (or press Enter for current directory): ").strip()
    if not repo_path:
        repo_path = os.getcwd()

    validator = DeepPortfolioValidator(repo_path)
    validator.validate_all()

if __name__ == "__main__":
    main()
