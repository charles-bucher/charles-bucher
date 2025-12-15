$repos = Get-ChildItem "C:\Users\buche\docs\Desktop\REPOS\" -Directory
foreach ($repo in $repos) {
    Set-Location $repo.FullName
    Write-Host "----------------------------------------"
    Write-Host "Repo: $($repo.Name)"
    git status
}
