# git_status_all.ps1 - Auto-updated documentation
# Author: Charles Bucher
# Description: Add description here

$repos = Get-ChildItem "C:\Users\buche\docs\Desktop\REPOS\" -Directory
foreach ($repo in $repos) {
    Set-Location $repo.FullName
    Write-Host "----------------------------------------"
    Write-Host "Repo: $($repo.Name)"
    git status
}
