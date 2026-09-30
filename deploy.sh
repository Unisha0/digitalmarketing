#!/usr/bin/env bash
set -euo pipefail

# Simple deploy helper for TrendCrafters
# Edit paths, service names, and user as needed before running on production.

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$PROJECT_DIR/.venv"
GUNICORN_SERVICE="gunicorn-trendcrafters"

echo "Deploying TrendCrafters from ${PROJECT_DIR}"

cd "$PROJECT_DIR"

if [ -f "$VENV/bin/activate" ]; then
  # Activate virtualenv
  # shellcheck disable=SC1091
  source "$VENV/bin/activate"
else
  echo "Warning: virtualenv not found at $VENV. Continuing without activation."
fi

echo "Pulling latest code..."
git pull origin main

echo "Installing Python dependencies (if requirements.txt changed)..."
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Running deployment checks..."
python manage.py check --deploy || true

echo "Collecting static files..."
python manage.py collectstatic --noinput


echo "Restarting application services (update service names if necessary)..."
if systemctl cat "$GUNICORN_SERVICE" >/dev/null 2>&1; then
  sudo systemctl reload "$GUNICORN_SERVICE" || sudo systemctl restart "$GUNICORN_SERVICE"
else
  echo "Service $GUNICORN_SERVICE not found. Please restart your WSGI process manually." 
fi

if systemctl cat nginx >/dev/null 2>&1; then
  sudo systemctl reload nginx || true
fi

echo "Smoke test..."
sleep 2
curl -fsS -H "X-Forwarded-Proto: https" -H "Host: trendcrafters.global" http://127.0.0.1/health/ >/dev/null && echo "health OK" || echo "WARNING: health check failed"

echo "Deployment completed."
