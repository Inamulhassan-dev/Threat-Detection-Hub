# 🖥️ SETUP ON NEW MACHINE - COMPLETE GUIDE

**Version:** 2.0  
**Date:** April 12, 2026  
**Purpose:** Step-by-step guide to clone and setup Threat Detection Hub on any new laptop

---

## 🎯 BEFORE YOU START

### System Requirements
- **OS:** Windows 10+, Ubuntu 20.04+, macOS 10.14+
- **Python:** 3.9, 3.10, or 3.11
- **RAM:** 2GB minimum (4GB recommended)
- **Disk Space:** 1GB free
- **Network:** Internet connection for first setup

### What You'll Need
- Git installed (for cloning)
- Terminal/Command Prompt access
- Text editor or IDE (VSCode recommended)
- ~10-15 minutes of time

---

## 📥 STEP 1: CLONE THE PROJECT

### Windows (Command Prompt or PowerShell):
```batch
# Navigate to where you want the project
cd Desktop

# Clone the repository
git clone https://github.com/your-username/threat-detection-hub.git

# Enter the folder
cd threat-detection-hub
```

### Linux/Mac (Terminal):
```bash
# Navigate to where you want the project
cd ~/Desktop

# Clone the repository
git clone https://github.com/your-username/threat-detection-hub.git

# Enter the folder
cd threat-detection-hub
```

---

## ⚙️ STEP 2: VERIFY PYTHON INSTALLATION

### Check if Python is installed:

**Windows:**
```batch
python --version
```

**Linux/Mac:**
```bash
python3 --version
```

### If Python is NOT installed:

**Windows:**
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 (latest stable)
3. **IMPORTANT:** Check "Add Python to PATH" during installation
4. Click "Install Now"
5. Close installer and restart terminal
6. Verify: `python --version`

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

**Mac:**
```bash
# Using Homebrew (install from https://brew.sh if needed)
brew install python3
python3 --version
```

---

## 🚀 STEP 3: RUN AUTOMATED SETUP

This is the **easiest way** - just one command!

### Windows:
```batch
setup.bat
```

**What it does automatically:**
- ✓ Checks Python version
- ✓ Creates virtual environment (.venv)
- ✓ Installs all 34 dependencies
- ✓ Creates database with admin user
- ✓ Sets up folder structure
- ✓ Initializes logging system

**Expected output:**
```
✓ Python 3.11.0 found
✓ Virtual environment created
✓ Pip upgraded
✓ Dependencies installed
✓ Databases initialized
✓ Project ready!
```

### Linux/Mac:
```bash
chmod +x setup.sh
./setup.sh
```

---

## ⚠️ IF SETUP.BAT/SETUP.SH FAILS

### Manual Setup for Windows:

```batch
# Step 1: Create virtual environment
python -m venv .venv

# Step 2: Activate virtual environment
.venv\Scripts\activate.bat

# Step 3: Upgrade pip
python -m pip install --upgrade pip

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Create necessary folders
mkdir backend\logs
mkdir backend\models
mkdir backend\flask_session

# Step 6: Initialize databases (if missing)
python backend/src/database.py
```

### Manual Setup for Linux/Mac:

```bash
# Step 1: Create virtual environment
python3 -m venv .venv

# Step 2: Activate virtual environment
source .venv/bin/activate

# Step 3: Upgrade pip
python -m pip install --upgrade pip

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Create necessary folders
mkdir -p backend/logs backend/models backend/flask_session

# Step 6: Initialize databases (if missing)
python backend/src/database.py
```

---

## 🧠 STEP 4: INITIALIZE ML MODEL

The ML model needs to be trained once.

### Option A: Train locally (recommended)
```bash
# Activate virtual environment first
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Navigate to backend
cd backend

# Train the model
python -m src.train_pipeline
```

**What happens:**
- Takes ~2-3 minutes
- Creates: `models/best_terrorism_detector.pkl`
- Creates: `models/tfidf_vectorizer.pkl`
- Ready for analysis!

### Option B: Download pre-trained model
If training takes too long, ask the project maintainer for pre-trained models:
1. Download `.pkl` files
2. Place in: `backend/models/`
3. Skip to Step 5

---

## 📊 STEP 5: VERIFY DATABASE

Check if admin user is created:

```bash
# View users database
cat backend/data/users.json  # Linux/Mac
type backend\data\users.json  # Windows
```

**Expected output:**
```json
{
  "users": [
    {
      "username": "admin",
      "email": "admin@threatdetection.io",
      "role": "Admin",
      ...
    }
  ]
}
```

**If file doesn't exist or is empty:**
```bash
# Run setup again
setup.bat  # Windows
./setup.sh  # Linux/Mac
```

---

## ✅ STEP 6: START THE APPLICATION

### Windows - Easy way (Double-click):
```
Double-click: start.bat
```

### Windows - Command Prompt:
```batch
start.bat
```

### Linux/Mac:
```bash
# Activate virtual environment first
source .venv/bin/activate

# Set Flask app
export FLASK_APP=backend/app.py

# Start Flask
python -m flask run --host=0.0.0.0 --port=5000
```

**You should see:**
```
 * Serving Flask app 'backend.app'
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
```

---

## 🌐 STEP 7: ACCESS THE APPLICATION

**Open your browser and go to:**
```
http://localhost:5000
```

**Login with:**
- Username: `admin`
- Password: `admin123`

**You should see:**
- ✓ Dashboard with 7 tabs
- ✓ Statistics cards showing 0 analyzed
- ✓ Text input area
- ✓ Dark mode interface

---

## 🧪 STEP 8: TEST THE APPLICATION

### Test 1: Single Text Analysis
1. Go to **DASHBOARD** tab
2. Paste sample text in text area
3. Click **ANALYZE NOW**
4. Should see prediction result with confidence score

### Test 2: Batch Processing
1. Go to **BATCH PROCESSING** tab
2. Enter multiple texts (one per line)
3. Click **PROCESS BATCH**
4. Should see results for all texts

### Test 3: View History
1. Go to **HISTORY** tab
2. Click **REFRESH RECORDS**
3. Should see your previous analyses

---

## ⚠️ COMMON PROBLEMS & SOLUTIONS

### ❌ "python: command not found"
**Solution:**
- Install Python from python.org
- Mac: use `python3` instead of `python`
- Windows: Add Python to PATH during installation

### ❌ "Port 5000 already in use"
**Solution:**

Windows:
```batch
netstat -ano | findstr :5000
taskkill /PID <PID> /F
start.bat
```

Linux/Mac:
```bash
lsof -i :5000
kill -9 <PID>
source .venv/bin/activate
flask run
```

### ❌ "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
# Make sure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Reinstall dependencies
pip install -r requirements.txt
```

### ❌ "Classifier not initialized"
**Solution:**
```bash
# Train the model
cd backend
python -m src.train_pipeline
cd ..
# Restart Flask
start.bat  # Windows
```

### ❌ "Login fails with admin/admin123"
**Solution:**
```bash
# Delete database to reset
rm backend/data/users.json  # Linux/Mac
del backend\data\users.json  # Windows

# Run setup again
setup.bat  # Windows
./setup.sh  # Linux/Mac
```

### ❌ "Cannot find module 'backend.app'"
**Solution:**
- Ensure you're in the project root directory
- Check `backend/app.py` exists
- Verify FLASK_APP environment variable is set correctly

### ❌ "Templates not found" (404 error)
**Solution:**
```bash
# Check templates exist
ls frontend/templates/  # Linux/Mac
dir frontend\templates  # Windows

# Ensure app.py has correct paths
# Should contain:
# template_folder='../frontend/templates'
# static_folder='../frontend/static'
```

### ❌ "Permission denied" on Linux/Mac
**Solution:**
```bash
chmod +x setup.sh
chmod +x start.sh
chmod 755 backend/logs
chmod 755 backend/flask_session
```

### ❌ "Large file size / slow clone"
**Solution:**
- ML models are large (100MB+)
- First clone might take time
- Use Git LFS if available: `git lfs install`

---

## 🔧 OPTIONAL: ADVANCED CONFIGURATION

### Change Port Number

**Windows (start.bat):**
```batch
python -m flask run --host=0.0.0.0 --port=5001
```

**Linux/Mac:**
```bash
flask run --host=0.0.0.0 --port=5001
```

Then access: `http://localhost:5001`

### Enable Debug Mode

**For development only (NOT for production!):**

Windows:
```batch
set FLASK_DEBUG=1
set FLASK_ENV=development
start.bat
```

Linux/Mac:
```bash
export FLASK_DEBUG=1
export FLASK_ENV=development
source .venv/bin/activate
flask run
```

### Create New User

1. Go to application
2. Click **Register**
3. Create account with email
4. Login with new credentials

Or programmatically:
```python
from backend.src.database import DatabaseManager
db = DatabaseManager('json')
db.create_user('newuser', 'email@example.com', 'password123', 'Analyst')
```

---

## 📚 PROJECT STRUCTURE REMINDER

```
threat-detection-hub/
├── backend/                    ← All server code
│   ├── app.py                 ← Main Flask app
│   ├── src/                   ← Core modules
│   ├── data/                  ← Databases (JSON)
│   ├── models/                ← ML models
│   ├── logs/                  ← Application logs
│   └── flask_session/         ← Session storage
│
├── frontend/                   ← All client code
│   ├── templates/             ← HTML pages
│   └── static/                ← CSS, JS, images
│
├── setup.bat                  ← Windows setup
├── start.bat                  ← Windows start
├── setup.sh                   ← Linux/Mac setup
├── requirements.txt           ← Python dependencies
└── README.md                  ← Project info
```

---

## ✅ VERIFICATION CHECKLIST

After setup, verify everything works:

- [ ] Python 3.9+ installed
- [ ] Virtual environment created (.venv folder exists)
- [ ] Dependencies installed (no errors on `pip list`)
- [ ] Backend folder structure intact
- [ ] Frontend folder structure intact
- [ ] `backend/models/*.pkl` files exist
- [ ] `backend/data/users.json` exists
- [ ] `backend/logs/` folder is writable
- [ ] Flask starts without errors
- [ ] Dashboard loads at http://localhost:5000
- [ ] Can login with admin/admin123
- [ ] Can analyze text and get results
- [ ] History tab shows previous analyses

---

## 🆘 IF PROBLEMS PERSIST

1. **Check the logs:**
```bash
tail -f backend/logs/app.log  # Linux/Mac
type backend\logs\app.log     # Windows
```

2. **Verify Python path:**
```bash
which python  # Linux/Mac
where python  # Windows
```

3. **Check virtual environment is activated:**
```bash
# You should see (.venv) before your prompt
# If not, run:
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

4. **Review DEPLOYMENT_GUIDE.md:**
- More detailed troubleshooting
- Platform-specific issues
- Advanced configuration

5. **Check PROJECT_STRUCTURE.md:**
- Understand folder organization
- Verify all files are present

---

## 📞 QUICK REFERENCE

### Essential Commands

**Windows:**
```batch
setup.bat              # One-time setup
start.bat             # Start application
stop.bat              # Stop application
```

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh            # One-time setup
source .venv/bin/activate  # Activate environment
flask run             # Start application
Ctrl+C                # Stop application
```

---

## ⏱️ ESTIMATED TIME

- **Fresh laptop with Python:** 5-10 minutes
- **Fresh laptop without Python:** 15-20 minutes (includes Python install)
- **With model training:** Add 3-5 minutes

---

## 🎉 YOU'RE DONE!

Once you see the dashboard, you're ready to use the Threat Detection Hub!

**Next steps:**
- Explore the 7 tabs (Dashboard, Batch, Samples, History, Search, Analytics, Export)
- Test with sample texts
- Check analysis history
- Export results as CSV
- Customize user accounts

---

**Questions?** See the other documentation files:
- `QUICK_START.md` - Fast overview
- `DEPLOYMENT_GUIDE.md` - Full operations manual
- `PROJECT_STRUCTURE.md` - File organization
- `CODE_ANALYSIS_REPORT.md` - Technical details

**Happy threat detecting!** 🛡️
