#!/usr/bin/env bash
# ============================================================
#   THREAT DETECTION HUB - First-Time Setup (Linux/macOS)
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
BACKEND_DIR="$SCRIPT_DIR/backend"

echo "============================================================"
echo "       THREAT DETECTION HUB - Setup Script"
echo "============================================================"
echo ""

# ── Python check ──────────────────────────────────────────────
if ! command -v python3 &>/dev/null; then
    echo "[ERROR] Python 3 is not installed."
    echo "        Install it from https://www.python.org/downloads/"
    echo "        or via your system package manager:"
    echo "          Ubuntu/Debian : sudo apt install python3 python3-pip python3-venv"
    echo "          macOS         : brew install python"
    exit 1
fi

PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "[OK] Python $PYTHON_VERSION detected"

# ── Virtual environment ───────────────────────────────────────
if [ ! -d "$VENV_DIR" ]; then
    echo "[STEP 1/4] Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "[OK] Virtual environment created at .venv/"
else
    echo "[SKIP] Virtual environment already exists"
fi

# ── Activate venv ─────────────────────────────────────────────
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

# ── Install dependencies ──────────────────────────────────────
echo "[STEP 2/4] Installing Python dependencies..."
pip install --upgrade pip --quiet
pip install -r "$SCRIPT_DIR/requirements.txt" --quiet
echo "[OK] Dependencies installed"

# ── NLTK data ─────────────────────────────────────────────────
echo "[STEP 3/4] Downloading NLTK language data..."
python3 - <<'EOF'
import nltk
for pkg in ("stopwords", "punkt", "punkt_tab", "wordnet", "omw-1.4"):
    nltk.download(pkg, quiet=True)
EOF
echo "[OK] NLTK data ready"

# ── Environment file ──────────────────────────────────────────
echo "[STEP 4/4] Checking environment configuration..."
ENV_FILE="$BACKEND_DIR/config/.env"
ENV_EXAMPLE="$BACKEND_DIR/config/.env.example"
if [ ! -f "$ENV_FILE" ]; then
    if [ -f "$ENV_EXAMPLE" ]; then
        cp "$ENV_EXAMPLE" "$ENV_FILE"
        echo "[OK] Created backend/config/.env from .env.example"
        echo "     Edit it to set email/SMTP credentials if you want alerts."
    fi
else
    echo "[OK] backend/config/.env already exists"
fi

# ── Privileges note ───────────────────────────────────────────
echo ""
echo "============================================================"
echo " SETUP COMPLETE"
echo "============================================================"
echo ""
echo " Start the app : ./start.sh"
echo " Open browser  : http://localhost:5000"
echo " Default login : admin / admin123"
echo ""
echo " NOTE: No elevated privileges (root/sudo) are required."
echo "       The app only needs read/write access to the project"
echo "       folder (logs/, data/, flask_session/ under backend/)."
echo ""
echo "       To train a new ML model:"
echo "         cd backend && python -m src.train_pipeline"
echo "       Make sure backend/data/data/training_data.csv exists first."
echo ""
