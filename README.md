<div align="center">

# 🛡️ Threat Detection Hub

### AI-Powered Content Analysis & Intelligence Platform

**Built with Machine Learning · Real-Time Detection · Enterprise-Grade Security**

---

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-lightgrey?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-3.9-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

<br/>

> **Developed by [INAMULHASSAN](https://github.com/INAMULHASSAN)**

</div>

---

## 📌 Overview

**Threat Detection Hub** is a full-stack AI security system that uses machine learning to classify text content into three threat levels in real time — **Normal**, **Suspicious**, and **Terrorist-Related** — with 94.5%+ accuracy.

It features a professional dark-mode web dashboard, role-based user authentication, batch processing, full analysis history, CSV export, and an automated alert system. Everything runs locally with zero cloud dependency.

---

## ⚡ Quick Start — Brand New Machine

> No Python? No problem. Just double-click and everything installs itself.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/INAMULHASSAN/threat-detection-hub.git
cd threat-detection-hub
```

### 2️⃣ Run Setup (One Time Only)
```
Double-click  ➜  setup.bat
```
Sit back. Everything downloads and installs automatically — takes about 5 minutes.

### 3️⃣ Start the Application
```
Double-click  ➜  start.bat
```

### 4️⃣ Open Your Browser
```
http://localhost:5000
```

### 5️⃣ Login
```
Username : admin
Password : admin123
```

**That's it. Nothing else. No manual steps.**

Need a full step-by-step guide (including USB transfer and troubleshooting)? See `backend/docs/SETUP_NEW_MACHINE.md`.

---

## 🤖 What `setup.bat` Does Automatically

| Step | Action |
|------|--------|
| 1 | Checks if Python is installed — **downloads & installs Python 3.11 if missing** |
| 2 | Verifies all project files are present |
| 3 | Creates an isolated virtual environment |
| 4 | Upgrades pip, setuptools, and wheel |
| 5 | **Installs all Python packages** (Flask, scikit-learn, pandas, numpy, nltk, textblob, etc.) |
| 6 | **Downloads all NLP language data** (punkt, stopwords, wordnet, etc.) |
| 7 | Creates all required folders |
| 8 | **Trains the ML model** and saves it to disk |
| 9 | **Creates the database** with the default admin account |

---

## ✨ Features

### 🧠 AI & Machine Learning
- Real-time text classification with **94.5%+ accuracy**
- 3-level threat classification: `Normal` · `Suspicious` · `Terrorist-Related`
- Confidence scores and probability breakdown for every prediction
- Sentiment analysis (polarity & subjectivity) on every submission
- TF-IDF vectorisation with 5,000 features and 1–3 gram range
- Trains 3 models (Random Forest, SVM, Naive Bayes) and auto-selects the best

### 📊 Dashboard
- Real-time statistics: total analysed, threats detected, alerts triggered, accuracy
- Single content analysis with instant results
- Probability bars showing confidence per threat class
- Keyword match scoring

### 📦 Batch Processing
- Analyse multiple texts simultaneously (one per line)
- Bulk results with prediction and confidence per item

### 🕵️ History & Search
- Full analysis history with timestamps and user tracking
- Advanced search with keyword filter, confidence range, and prediction type filter
- Pagination support

### 📤 Export
- One-click CSV export of all analysis records
- Compatible with Excel, Google Sheets, and any data tool

### 🔐 Authentication & Security
- Secure login and registration system
- PBKDF2-SHA256 password hashing with random salt
- Role-based access control: **Admin** · **Analyst** · **Viewer**
- Session management with 24-hour expiry
- Password strength indicator on registration

### 🚨 Alert System
- Automatic alert triggering on high-confidence threats
- Configurable alert threshold
- Alert history log
- Email notification support (configurable via `.env`)

---

## 🗂️ Project Structure

```
threat-detection-hub/
│
├── 📄 setup.bat                    ← Run FIRST on a new machine
├── 📄 start.bat                    ← Run to start the application
├── 📄 stop.bat                     ← Run to stop the application
├── 📄 requirements.txt             ← All Python dependencies (pinned)
├── 📄 .gitignore
├── 📄 README.md
│
├── 🗂️ backend/
│   ├── 📄 app.py                   ← Main Flask application (routes, auth, API)
│   │
│   ├── 🗂️ src/
│   │   ├── 📄 classifier.py        ← ML content classifier
│   │   ├── 📄 database.py          ← JSON / MongoDB / MySQL manager
│   │   ├── 📄 text_processor.py    ← NLP preprocessing (NLTK)
│   │   ├── 📄 feature_extractor.py ← TF-IDF & sentiment features
│   │   ├── 📄 model_trainer.py     ← ML model training (RF, SVM, NB)
│   │   ├── 📄 train_pipeline.py    ← Full end-to-end training pipeline
│   │   ├── 📄 alert_system.py      ← Alert generation & email notifications
│   │   ├── 📄 data_collector.py    ← Web scraping collector
│   │   └── 📄 monitor.py           ← Automated background monitoring
│   │
│   ├── 🗂️ config/
│   │   └── 📄 .env                 ← Environment configuration
│   │
│   ├── 🗂️ data/
│   │   └── 🗂️ data/
│   │       └── 📄 training_data.csv ← ML training dataset
│   │
│   ├── 🗂️ models/                  ← Trained model files (auto-generated)
│   ├── 🗂️ logs/                    ← Application logs (auto-generated)
│   ├── 🗂️ flask_session/           ← Session storage (auto-generated)
│   │
│   └── 🗂️ docker/
│       ├── 📄 Dockerfile
│       └── 📄 docker-compose.yml
│
└── 🗂️ frontend/
    ├── 🗂️ templates/
    │   ├── 📄 index.html            ← Main dashboard (7 tabs)
    │   └── 📄 login.html            ← Login & registration
    └── 🗂️ static/
        ├── 🗂️ css/
        ├── 🗂️ js/
        └── 🗂️ images/
```

---

## 🧠 ML Pipeline — How It Works

```
Raw Text
   │
   ▼
Text Preprocessing (NLTK)
   │  • Lowercase, remove URLs & special chars
   │  • Tokenisation
   │  • Stopword removal
   │  • Lemmatisation
   │
   ▼
Feature Extraction
   │  • TF-IDF (5,000 features, 1–3 grams)
   │  • Sentiment polarity & subjectivity
   │  • Terrorism keyword match score
   │  • Statistical features (word count, uppercase ratio, etc.)
   │
   ▼
Model Training (3 models in parallel)
   │  • Random Forest (100 estimators)
   │  • Support Vector Machine (RBF kernel)
   │  • Naive Bayes (Multinomial)
   │
   ▼
Best Model Selected by Accuracy
   │
   ▼
Saved to disk → best_terrorism_detector.pkl
                tfidf_vectorizer.pkl
```

**Classification Labels:**
| Code | Label | Meaning |
|------|-------|---------|
| 0 | ✅ Normal | Safe, non-threatening content |
| 1 | ⚠️ Suspicious | Potentially concerning, needs review |
| 2 | 🚨 Terrorist-Related | High-risk content, alert triggered |

To retrain the model manually:
```bash
cd backend
python -m src.train_pipeline
```

---

## 👤 User Roles

| Role | Permissions |
|------|-------------|
| 🔴 Admin | Full access — manage users, view all data, system settings |
| 🟡 Analyst | Analyse content, view history, export data |
| 🟢 Viewer | View dashboard and history only |

New registrations are assigned **Viewer** role by default. Admins can promote users.

---

## ⚙️ Configuration

Edit `backend/config/.env` to customise:

```env
# ── Database ──────────────────────────────────────
# Default is JSON files — no setup needed
MONGODB_URI=mongodb://localhost:27017/
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=terrorism_detection

# ── Email Alerts ──────────────────────────────────
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
ALERT_RECIPIENTS=admin@example.com

# ── System ────────────────────────────────────────
LOG_LEVEL=INFO
ALERT_THRESHOLD=0.7
MONITORING_INTERVAL=6
```

---

## 🐳 Docker Setup (Optional)

```bash
cd backend/docker
docker-compose up --build
```

Starts three services:
- `web` — Flask application on port 5000
- `mongo` — MongoDB on port 27017
- `monitor` — Background automated monitoring service

---

## 🛠️ Manual Setup (Advanced Users)

If you prefer not to use `setup.bat`:

```bash
# 1. Create virtual environment
python -m venv .venv

# 2. Activate
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Mac / Linux

# 3. Install packages
pip install -r requirements.txt

# 4. Download NLP data
python -c "import nltk; nltk.download('punkt_tab'); nltk.download('stopwords'); nltk.download('wordnet')"

# 5. Train the ML model
cd backend
python -m src.train_pipeline

# 6. Start the app
set PYTHONPATH=%cd%\backend     # Windows
python -m flask --app backend.app run --host=0.0.0.0 --port=5000
```

---

## 🔧 Troubleshooting

**Python not found after setup closes**
> Close the Command Prompt, reopen it, and run `setup.bat` again. PATH updates require a new session.

**Port 5000 already in use**
> Run `stop.bat` first, then `start.bat`.

**"Module not found" error**
> Make sure you are running from the project root folder. Re-run `setup.bat`.

**ML model not loading**
> Retrain manually:
> ```bash
> cd backend
> python -m src.train_pipeline
> ```

**Login always fails**
> Re-initialise the database:
> ```bash
> cd backend
> python -c "from src.database import DatabaseManager; db = DatabaseManager('json'); db.create_user('admin', 'admin@threatdetection.io', 'admin123', 'Admin')"
> ```

---

## 📦 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11, Flask 3.1 |
| ML | scikit-learn, joblib, scipy |
| NLP | NLTK, TextBlob |
| Data | pandas, numpy |
| Web Scraping | requests, BeautifulSoup4 |
| Auth | PBKDF2-SHA256, Flask-Session |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Database | JSON (default), MongoDB, MySQL |
| Deployment | Docker, docker-compose |

---

## 📄 License

This project is developed and owned by **INAMULHASSAN**.
All rights reserved. Unauthorised copying, distribution, or modification is prohibited.

---

<div align="center">

**Developed with ❤️ by [INAMULHASSAN](https://github.com/INAMULHASSAN)**

*Threat Detection Hub — AI Security System*

⭐ If you find this project useful, please give it a star!

</div>
