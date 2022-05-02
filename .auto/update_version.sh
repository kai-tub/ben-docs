#!/bin/bash
# Script is triggered by `auto` beforeCommitChangelog
# should include any changes that are
# Assumes current dir is the project root

set -e

# Print on stderr to not pollute function return echo
function error {
    echo "::error::$1" >& 2
    exit 1
}

# https://stackoverflow.com/questions/59895/how-to-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
# scriptFolder="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "$ARG_0"
bumpType=$(echo "$ARG_0" | jq -r '.bump')
echo "bump type: $bumpType"


if [[ -z "$(command -v poetry)" ]]; then
    error "requires poetry to bump version!"
fi

# bump version
poetry version "$bumpType"


# Files will be commited via `auto` tool
git add .
