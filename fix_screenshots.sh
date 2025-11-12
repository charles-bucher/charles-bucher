#!/bin/bash
set +H   # disable ! history expansion

# GitHub info
GITHUB_USER="charles-bucher"
REPO_NAME="charles-bucher"
BRANCH="main"

# Screenshots folder
SCREENSHOT_DIR="screenshots"

# Loop through all png/jpg/jpeg files
for file in $SCREENSHOT_DIR/*.{png,jpg,jpeg}; do
    [ -e "$file" ] || continue  # skip if no files found

    filename=$(basename "$file")
    raw_url="https://raw.githubusercontent.com/$GITHUB_USER/$REPO_NAME/$BRANCH/$SCREENSHOT_DIR/$filename"

    # Replace local markdown link with raw URL
    sed -i 's|!\[\(.*\)\]('"$SCREENSHOT_DIR"'/'"$filename"')|![\1]('"$raw_url"')|g' README.md

    echo "Updated $filename"
done

echo "All screenshot links updated!"
