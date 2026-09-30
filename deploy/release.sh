#!/usr/bin/env bash
# Run from your laptop:  bash deploy/release.sh
# Pushes code to git, syncs the private media (images/videos, not in git) to the server, deploys.
set -euo pipefail
HOST="${DEPLOY_HOST:-trendcraftersaws}"
cd "$(dirname "$0")/.."

git push origin main
ssh "$HOST" 'cd ~/trendcrafters && git pull -q origin main'
rsync -az --delete --info=stats1 main/static/main/images/ "$HOST":trendcrafters/main/static/main/images/
rsync -az --delete main/static/main/videos/ "$HOST":trendcrafters/main/static/main/videos/
ssh "$HOST" 'cd ~/trendcrafters && bash deploy.sh'
