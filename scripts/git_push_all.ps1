$repos = Get-ChildItem "C:\Users\buche\docs\Desktop\REPOS\" -Directory
foreach ($repo in $repos) {
    Set-Location $repo.FullName
    git add .
    git commit -m "Routine update: $(Get-Date -Format yyyy-MM-dd_HH:mm)"
    git push origin main
    Write-Host "✅ Pushed updates for $($repo.Name)"
}
