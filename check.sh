#!/bin/sh
# Public repos not yet linked from README.md. Empty output means the profile is current.
gh repo list abhaymettu --limit 200 --visibility public --no-archived --source \
  --json name,description,pushedAt --jq '.[] | "\(.pushedAt[:10])\t\(.name)\t\(.description // "")"' \
| grep -v -F -f <(grep -o 'github.com/abhaymettu/[^)]*' README.md | sed 's#.*/#\t#; s#$#\t#') \
| grep -v -E '^\S+\t(abhaymettu|artbutsports)\t'
