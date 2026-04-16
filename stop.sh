#!/usr/bin/env bash
# ============================================================
#   THREAT DETECTION HUB - Stop Application (Linux/macOS)
# ============================================================

echo "Stopping Threat Detection Hub..."

# Find and kill any Flask process listening on port 5000
PORT=5000
PIDS=$(lsof -ti tcp:"$PORT" 2>/dev/null || true)

if [ -z "$PIDS" ]; then
    echo "No process found on port $PORT."
else
    for PID in $PIDS; do
        echo "Stopping process $PID on port $PORT..."
        kill "$PID" 2>/dev/null || true
    done
    echo "Done."
fi
