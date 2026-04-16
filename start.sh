#!/usr/bin/env bash
# ============================================================
#   THREAT DETECTION HUB - Start Application (Linux/macOS)
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
BACKEND_DIR="$SCRIPT_DIR/backend"

echo "============================================================"
echo "       THREAT DETECTION HUB - Starting Application"
echo "============================================================"
echo ""

# ── Check setup has been run ──────────────────────────────────
if [ ! -d "$VENV_DIR" ]; then
    echo "[ERROR] Virtual environment not found."
    echo "        Run setup first:  ./setup.sh"
    exit 1
fi

# ── Activate venv ─────────────────────────────────────────────
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

# ── Write permissions check ───────────────────────────────────
for dir in "$BACKEND_DIR/logs" "$BACKEND_DIR/data" "$BACKEND_DIR/flask_session"; do
    mkdir -p "$dir"
    if ! touch "$dir/.write_test" 2>/dev/null; then
        echo "[ERROR] Cannot write to $dir"
        echo "        Fix permissions:  chmod -R u+w $dir"
        exit 1
    fi
    rm -f "$dir/.write_test"
done

echo "[OK] Write permissions verified"
echo ""
echo " Application URL : http://localhost:5000"
echo " Default login   : admin / admin123"
echo " Press CTRL+C to stop"
echo ""

cd "$BACKEND_DIR"
python app.py
