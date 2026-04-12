# 📁 PROJECT STRUCTURE GUIDE

**Version:** 3.0 - Professional Organization  
**Date:** April 12, 2026

---

## 🏢 MAIN DIRECTORY OVERVIEW

When you open the project folder, you'll see a **clean, professional structure** with only **4 main folders** and **essential setup files**:

```
threat-detection-hub/
│
├── ⚡ QUICK ACCESS SCRIPTS (Root Level)
│   ├── setup.bat              ← Setup Windows (first time)
│   ├── start.bat              ← Run Windows
│   ├── stop.bat               ← Stop Windows
│   ├── setup.sh               ← Setup Mac/Linux (first time)
│   ├── start.sh               ← Run Mac/Linux
│   ├── stop.sh                ← Stop Mac/Linux
│   ├── requirements.txt       ← Python packages
│   └── README.md              ← Project overview
│
├── 🎯 MAIN PROJECT FOLDERS (4 Total)
│   │
│   ├── backend/ ........................ Flask API & ML
│   │   ├── app.py              (Main application)
│   │   ├── src/                (Source code)
│   │   ├── logs/               (Application logs)
│   │   ├── models/             (AI models)
│   │   └── flask_session/      (Session storage)
│   │
│   ├── frontend/ ....................... Web Interface
│   │   ├── templates/          (HTML pages)
│   │   └── static/             (CSS, JS, images)
│   │
│   ├── data/ ........................... Databases
│   │   ├── users.json          (User accounts)
│   │   ├── alerts.json         (Alert history)
│   │   ├── web_content.json    (Samples)
│   │   └── training_data.csv   (Training data)
│   │
│   └── docs/ ........................... Documentation
│       ├── QUICK_INSTALL.md    (Quick setup)
│       ├── SETUP_NEW_MACHINE.md (Help & fixes)
│       ├── BULLETPROOF_SETUP_ANALYSIS.md (Tech details)
│       ├── DEPLOYMENT_GUIDE.md (Production)
│       ├── PROJECT_STRUCTURE.md (This file)
│       └── ... (more guides)
│
└── 📦 OPTIONAL CONFIGURATION
    └── config/ ....................... Settings
        └── (Environment configs)
```

---

## 📊 FOLDER DETAILS

### 1. **backend/** - Flask API & Machine Learning

**Purpose:** Core application logic, API endpoints, ML models

**What's Inside:**
```
backend/
├── app.py                      Main Flask app (entry point)
├── src/
│   ├── __init__.py             Package initialization
│   ├── alert_system.py         Alert management
│   ├── classifier.py           ML threat classifier
│   ├── data_collector.py       Web scraping (optional)
│   ├── database.py             Database operations
│   ├── feature_extractor.py    NLP feature extraction
│   ├── model_trainer.py        ML model training
│   ├── monitor.py              Automated monitoring
│   ├── text_processor.py       Text preprocessing
│   └── train_pipeline.py       Full training pipeline
├── logs/                       Application logs
│   ├── app.log                 Flask logs
│   ├── model_trainer.log       Training logs
│   ├── alerts.log              Alert logs
│   └── scraper.log             Scraping logs
├── models/                     AI Model files
│   ├── best_terrorism_detector.pkl    Main ML model
│   ├── tfidf_vectorizer.pkl           Feature vectorizer
│   └── ... (backup models)
├── data/                       Temporary data
│   ├── alerts.json             Alert records
│   ├── users.json              User database
│   └── web_content.json        Web samples
└── flask_session/              User sessions
    └── (Session storage files)
```

**Key File: `backend/app.py`**
- Starts Flask web server
- Defines API endpoints
- Handles web requests
- Manages user sessions

---

### 2. **frontend/** - Web User Interface

**Purpose:** Everything users see in their browser

**What's Inside:**
```
frontend/
├── templates/                  HTML pages
│   ├── index.html              Main dashboard (dark mode UI)
│   ├── login.html              Login page
│   └── ... (other pages)
└── static/                     CSS, JavaScript, Images
    ├── css/
    │   ├── style.css           Main styling
    │   └── ... (other styles)
    ├── js/
    │   ├── app.js              Main JavaScript
    │   └── ... (other scripts)
    └── images/
        └── (Icons, logos, images)
```

**Key File: `frontend/templates/index.html`**
- Dark mode professional dashboard
- 7 tabs: Dashboard, Batch, Samples, History, Search, Analytics, Export
- Real-time threat analysis interface
- Charts and statistics display

---

### 3. **data/** - Application Databases & Data

**Purpose:** Store all application data

**What's Inside:**
```
data/
├── users.json                  User accounts & credentials
├── alerts.json                 Analysis history & alerts
├── web_content.json            Sample texts for testing
└── training_data.csv           ML training dataset
```

**Important Files:**
- `users.json` - Created on setup with default admin account
- `alerts.json` - Stores all analyses with results
- `training_data.csv` - Used to train ML models
- `web_content.json` - Sample texts for sample tab

---

### 4. **docs/** - Documentation & Guides

**Purpose:** Help documentation for users

**What's Inside:**
```
docs/
├── QUICK_INSTALL.md           ⭐ START HERE (60-second setup)
├── SETUP_NEW_MACHINE.md       Complete troubleshooting (26 solutions)
├── BULLETPROOF_SETUP_ANALYSIS.md  Technical analysis
├── DEPLOYMENT_GUIDE.md        Production deployment
├── PROJECT_STRUCTURE.md       This file
├── BATCH_SCRIPTS_GUIDE.md    Script documentation
├── AUTH_SYSTEM.md             Authentication details
├── QUICK_START.md             Feature walkthrough
└── ... (more guides)
```

**Which Guide To Use:**
- **New user?** → `QUICK_INSTALL.md`
- **Having problems?** → `SETUP_NEW_MACHINE.md`
- **Technical questions?** → `BULLETPROOF_SETUP_ANALYSIS.md`
- **Production deployment?** → `DEPLOYMENT_GUIDE.md`
- **Want to understand code?** → `PROJECT_STRUCTURE.md`

---

## 🔧 CONFIG/ FOLDER (Optional)

**Purpose:** Configuration and environment settings

```
config/
├── settings.json              Application settings
├── environment.json           Environment variables
└── ... (other configs)
```

---

## 📍 ROOT LEVEL FILES

These are quick-access files in the main directory:

| File | Purpose | Windows | Mac/Linux |
|------|---------|---------|----------|
| `setup.bat` | First-time setup | ✅ | ❌ |
| `start.bat` | Start application | ✅ | ❌ |
| `stop.bat` | Stop application | ✅ | ❌ |
| `setup.sh` | First-time setup | ❌ | ✅ |
| `start.sh` | Start application | ❌ | ✅ |
| `stop.sh` | Stop application | ❌ | ✅ |
| `requirements.txt` | Python dependencies | ✅ | ✅ |
| `README.md` | Project overview | ✅ | ✅ |

---

## 🎯 WORKFLOW EXAMPLE

### User Flow

```
1. Downloads project
   ↓
2. Finds setup.bat (Windows) or setup.sh (Mac/Linux) in root
   ↓
3. Runs setup → Auto-configures everything
   ↓
4. Finds start.bat or start.sh in root
   ↓
5. Runs start → Application opens in browser
   ↓
6. Accesses http://localhost:5000
   ↓
7. Logs in with admin/admin123
   ↓
8. Uses interface to analyze threats
```

### File Access During Use

- **Static assets** ← Loaded from `frontend/static/`
- **HTML pages** ← Loaded from `frontend/templates/`
- **User database** ← Read/written to `data/users.json`
- **Analysis results** ← Saved to `data/alerts.json`
- **ML model** ← Loaded from `backend/models/best_terrorism_detector.pkl`
- **Application logs** ← Written to `backend/logs/app.log`

---

## 🎯 FILE ORGANIZATION PRINCIPLES

### ✅ What We DO
- Keep main folder clean (only 4 main folders + setup scripts)
- Organize by function (backend, frontend, data, docs)
- Put scripts at root for easy access
- Group related files together
- Use descriptive folder names

### ❌ What We DON'T Do
- Scatter files everywhere
- Mix frontend and backend at root
- Confuse users with 10+ top-level folders
- Hide important files in deep subfolders

---

## 🚀 RECOMMENDED USAGE

### First Time Users
1. Look at `README.md` (root level)
2. Read `docs/QUICK_INSTALL.md`
3. Run `setup.bat` or `./setup.sh`
4. Run `start.bat` or `./start.sh`
5. Open `http://localhost:5000`

### Troubleshooting
1. Check `docs/SETUP_NEW_MACHINE.md`
2. Look at `backend/logs/app.log`
3. Run setup again
4. Contact support with log files

### Developers
1. Modify code in `backend/src/`
2. Edit UI in `frontend/templates/` and `frontend/static/`
3. Tests in `backend/tests/`
4. Deploy per `docs/DEPLOYMENT_GUIDE.md`

---

## 📊 SIZE REFERENCE

```
Total Project Size: ~150-200 MB
├── backend/      ~30 MB  (Code + ML models)
├── frontend/     ~5 MB   (HTML, CSS, JS)
├── data/         ~80 MB  (Databases + training data)
├── docs/         ~2 MB   (Documentation)
└── Other         ~50 MB  (.venv virtual environment)

After setup (.venv created): ~250-300 MB total
After first ML training: ~350-400 MB total
```

---

## ✨ CLEAN STRUCTURE BENEFITS

✅ **Professional** - Organized like enterprise applications  
✅ **Easy to Navigate** - Users find what they need quickly  
✅ **Maintainable** - Developers understand code layout  
✅ **Scalable** - Can grow without becoming messy  
✅ **Professional Image** - Looks polished and complete  

---

## 📚 RELATED DOCUMENTS

For more information, see:
- `README.md` - Main project overview
- `docs/QUICK_INSTALL.md` - Setup instructions
- `docs/SETUP_NEW_MACHINE.md` - Troubleshooting guide
- `docs/DEPLOYMENT_GUIDE.md` - Production setup

---

**Last Updated:** April 12, 2026  
**Version:** 3.0 Bulletproof Edition
