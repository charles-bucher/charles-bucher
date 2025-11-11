#!/bin/bash
# Cleanup script for Charles Bucher GitHub repo
# Deletes old screenshot folders and pushes changes to GitHub

echo "🧹 Starting cleanup..."

cd "$(dirname "$0")" || exit

# Remove the folders
rm -rf NOC_Toolkit_screenshots
rm -rf aws_monitoring_observability_screenshots
rm -rf cloudOps-guardDuty-automation-screenshots

# Stage, commit, and push
git add -A
git commit -m "Delete screenshot folders: NOC_Toolkit, AWS monitoring, GuardDuty"
git push origin main

echo "✅ Cleanup complete and changes pushed!"
