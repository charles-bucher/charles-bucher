# Update README in all repos
$repos = @(
    "C:\Users\buche\docs\Desktop\REPOS\charles-bucher",
    "C:\Users\buche\docs\Desktop\REPOS\AWS_Cloudops_Suite",
    "C:\Users\buche\docs\Desktop\REPOS\AWS_Cloud_Support_Sim",
    "C:\Users\buche\docs\Desktop\REPOS\AWS_Incident_Postmortems"
)

$newReadme = "C:\Users\buche\docs\Desktop\REPOS\new_README.md"

foreach ($repo in $repos) {
    if (Test-Path $repo) {
        Write-Host "Processing repo: $repo"
        Set-Location $repo
        git checkout main
        Copy-Item -Path $newReadme -Destination "$repo\README.md" -Force
        git add README.md
        git commit -m "Update README: scannable, badges, portfolio links, ATS-friendly"
        git push origin main
        Write-Host "✅ Successfully updated: $repo"
    } else {
        Write-Host "❌ Repo not found: $repo"
    }
}
