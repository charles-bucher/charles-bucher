$repos = Get-ChildItem "C:\Users\buche\docs\Desktop\REPOS\" -Directory
foreach ($repo in $repos) {
    Set-Location $repo.FullName
    git checkout main
    git pull origin main
    Write-Host "✅ Pulled latest for $($repo.Name)"
}
