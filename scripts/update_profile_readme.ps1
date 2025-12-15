# ==========================================
# Script: update_profile_readme.ps1
# Purpose: Update GitHub Profile README and push changes
# ==========================================

# Path to your GitHub profile repo
$repoPath = "C:\Users\buche\docs\Desktop\REPOS\charles-bucher"

# Path to your new README
$newReadme = "C:\Users\buche\docs\Desktop\REPOS\new_README.md"

# Check if new README exists
if (-Not (Test-Path $newReadme)) {
    Write-Host "❌ ERROR: New README not found at $newReadme"
    exit
}

# Check if repo exists
if (-Not (Test-Path $repoPath)) {
    Write-Host "❌ ERROR: Repo path not found at $repoPath"
    exit
}

# Navigate to repo
Set-Location $repoPath

# Ensure we are on main branch
git checkout main

# Copy the new README into the repo (overwrite)
Copy-Item -Path $newReadme -Destination "$repoPath\README.md" -Force

# Stage README
git add README.md

# Commit changes
$commitMessage = "Update README: scannable, SEO, ATS-friendly, portfolio & LinkedIn links"
git commit -m $commitMessage

# Push to GitHub
git push origin main

Write-Host "✅ Successfully updated README for $repoPath"
