#!/bin/bash
set +H   # disable ! history expansion

# -----------------------------
# CONFIGURATION
# -----------------------------
GITHUB_USER="charles-bucher"
REPO_NAME="charles-bucher"
BRANCH="main"
SCREENSHOT_DIR="Screenshots"
README_FILE="README.md"
AUTO_PUSH=true   # set to false if you don't want auto push

# -----------------------------
# FUNCTION: Convert local path to GitHub raw URL
# -----------------------------
function raw_url() {
    local file_path="$1"
    # convert backslashes to forward slashes
    local path_unix=$(echo "$file_path" | sed 's|\\|/|g')
    echo "https://raw.githubusercontent.com/$GITHUB_USER/$REPO_NAME/$BRANCH/$path_unix"
}

# -----------------------------
# SCAN & UPDATE README
# -----------------------------
echo "Updating README with GitHub raw URLs..."

# Find all images recursively
find "$SCREENSHOT_DIR" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.gif" \) | while read file; do
    filename=$(basename "$file")
    alt_text=$(basename "$file" | sed 's/\.[^.]*$//')   # remove extension for alt text
    url=$(raw_url "$file")

    # Escape ! in sed pattern
    escaped_file=$(echo "$file" | sed 's/[]\/$*.^[]/\\&/g')
    
    # Update README
    sed -i "" "s|!\[.*\]($escaped_file)|![${alt_text}]($url)|g" "$README_FILE"
    echo "Updated $file → $url"
done

echo "README update complete."

# -----------------------------
# OPTIONAL: Commit & Push
# -----------------------------
if [ "$AUTO_PUSH" = true ]; then
    git add "$README_FILE"
    git commit -m "Auto-update screenshot links in README"
    git push origin "$BRANCH"
    echo "Changes committed and pushed to GitHub."
fi
