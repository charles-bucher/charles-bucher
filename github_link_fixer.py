# Complete Repository Cleanup and Push
# This script fixes README links AND commits all file changes (deleted/renamed screenshots)

$reposPath = "C:\Users\buche\repos\Cloud_Work\repos"

# Define repos and their correct GitHub URLs
$repos = @{
    "aws_monitoring_observability" = "https://github.com/charles-bucher/aws_monitoring_observability.git"
    "aws_mult_itier_vpc_cloud_ops" = "https://github.com/charles-bucher/aws_mult_itier_vpc_cloud_ops.git"
    "charles-bucher.github.io" = "https://github.com/charles-bucher/charles-bucher.github.io.git"
    "cloudOps-guardDuty-automation" = "https://github.com/charles-bucher/cloudOps-guardDuty-automation.git"
    "NOC-Toolkit-Automation" = "https://github.com/charles-bucher/NOC-Toolkit-Automation.git"
}

Write-Host "`n================================" -ForegroundColor Cyan
Write-Host "Repository Cleanup & Push Script" -ForegroundColor Cyan
Write-Host "================================`n" -ForegroundColor Cyan

foreach ($repo in $repos.Keys) {
    $repoPath = Join-Path $reposPath $repo
    $correctUrl = $repos[$repo]
    
    if (Test-Path $repoPath) {
        Write-Host "Processing: $repo" -ForegroundColor Yellow
        Set-Location $repoPath
        
        # Check current remote URL
        $currentRemote = git remote get-url origin 2>$null
        if ($currentRemote -ne $correctUrl) {
            Write-Host "  [FIX] Updating remote URL..." -ForegroundColor Magenta
            git remote set-url origin $correctUrl
            Write-Host "  [OK] Remote URL updated to: $correctUrl" -ForegroundColor Green
        }
        
        # Check if there are ANY changes (including deleted files)
        $status = git status --porcelain
        
        if ($status) {
            Write-Host "  [INFO] Changes detected:" -ForegroundColor Cyan
            
            # Show what will be committed
            $deletedFiles = ($status | Select-String "^ D" | Measure-Object).Count
            $modifiedFiles = ($status | Select-String "^ M" | Measure-Object).Count
            $untrackedFiles = ($status | Select-String "^\?\?" | Measure-Object).Count
            
            if ($deletedFiles -gt 0) { Write-Host "    - Deleted files: $deletedFiles" -ForegroundColor Gray }
            if ($modifiedFiles -gt 0) { Write-Host "    - Modified files: $modifiedFiles" -ForegroundColor Gray }
            if ($untrackedFiles -gt 0) { Write-Host "    - New files: $untrackedFiles" -ForegroundColor Gray }
            
            # Stage ALL changes (including deletions and new files)
            Write-Host "  [ACTION] Staging all changes..." -ForegroundColor Cyan
            git add -A
            
            # Commit with descriptive message
            $commitMsg = "Fix README links and reorganize screenshots"
            Write-Host "  [ACTION] Committing changes..." -ForegroundColor Cyan
            git commit -m $commitMsg
            
            # Push to main branch
            Write-Host "  [ACTION] Pushing to GitHub..." -ForegroundColor Cyan
            $pushResult = git push origin main 2>&1
            
            if ($LASTEXITCODE -eq 0) {
                Write-Host "  [SUCCESS] Pushed successfully!`n" -ForegroundColor Green
            } else {
                Write-Host "  [ERROR] Push failed: $pushResult" -ForegroundColor Red
                Write-Host "  [TIP] You may need to pull first: git pull origin main`n" -ForegroundColor Yellow
            }
        }
        else {
            Write-Host "  [OK] No changes to commit`n" -ForegroundColor Gray
        }
    }
    else {
        Write-Host "[ERROR] Repository not found: $repoPath`n" -ForegroundColor Red
    }
}

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

# Show final status of all repos
foreach ($repo in $repos.Keys) {
    $repoPath = Join-Path $reposPath $repo
    if (Test-Path $repoPath) {
        Set-Location $repoPath
        $statusClean = -not (git status --porcelain)
        $branch = git branch --show-current
        $ahead = git rev-list --count origin/$branch..$branch 2>$null
        
        if ($statusClean -and $ahead -eq 0) {
            Write-Host "[OK] $repo - Clean and synced" -ForegroundColor Green
        } elseif ($ahead -gt 0) {
            Write-Host "[WARN] $repo - $ahead commits ahead of remote" -ForegroundColor Yellow
        } else {
            Write-Host "[WARN] $repo - Has uncommitted changes" -ForegroundColor Yellow
        }
    }
}

Write-Host "`n================================" -ForegroundColor Cyan
Write-Host "Done!" -ForegroundColor Cyan
Write-Host "================================`n" -ForegroundColor Cyan

# Return to repos folder
Set-Location $reposPath