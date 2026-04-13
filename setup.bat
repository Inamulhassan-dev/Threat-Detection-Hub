@echo off
REM ============================================================
REM   THREAT DETECTION HUB - BULLETPROOF SETUP SCRIPT v4.0
REM   Developed by INAMULHASSAN
REM   Works on a BRAND NEW laptop with NOTHING installed.
REM   Automatically downloads Python, all packages, NLP data,
REM   trains the ML model, and initialises the database.
REM ============================================================

setlocal enabledelayedexpansion
color 0A
cls

echo.
echo ============================================================
echo    THREAT DETECTION HUB - AUTOMATIC SETUP v4.0
echo    Developed by INAMULHASSAN
echo    This will set up EVERYTHING from scratch.
echo ============================================================
echo.

set "PROJECT_DIR=%~dp0"
cd /d "!PROJECT_DIR!"
set "PYTHON_CMD=python"

REM ============================================================
REM STEP 1 - CHECK / INSTALL PYTHON
REM ============================================================
echo [STEP 1/9]  Checking Python 3.11+...
echo.

python -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)" >nul 2>&1
if errorlevel 1 (
    py -3.11 --version >nul 2>&1
    if not errorlevel 1 (
        set "PYTHON_CMD=py -3.11"
    ) else (
    echo   Python 3.11+ not found. Downloading Python 3.11.9 installer...
    echo   Please wait - this may take 1-2 minutes...
    echo.

    powershell -NoProfile -ExecutionPolicy Bypass -Command "$ProgressPreference='SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12; $url='https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe'; $out=Join-Path $env:TEMP 'python-installer.exe'; Invoke-WebRequest -Uri $url -OutFile $out; Write-Host 'Download complete.'"

    if not exist "%TEMP%\python-installer.exe" (
        echo.
        echo   ERROR: Could not download Python installer.
        echo   Please check your internet connection and try again.
        echo   Or download manually from: https://www.python.org/downloads/
        color 0C
        pause
        exit /b 1
    )

    echo   Installing Python 3.11.9 silently...
    "%TEMP%\python-installer.exe" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0 Include_launcher=1
    timeout /t 10 /nobreak >nul
    del "%TEMP%\python-installer.exe" >nul 2>&1

    REM Refresh PATH so python is found in this session
    for /f "usebackq tokens=2*" %%A in (`reg query "HKCU\Environment" /v PATH 2^>nul`) do set "USERPATH=%%B"
    set "PATH=!USERPATH!;%PATH%"

    py -3.11 --version >nul 2>&1
    if not errorlevel 1 (
        set "PYTHON_CMD=py -3.11"
    ) else (
    python -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)" >nul 2>&1
    if errorlevel 1 (
        echo.
        echo   ERROR: Python installation finished but Python 3.11+ is still not available.
        echo   Please CLOSE this window, reopen it, and run setup.bat again.
        color 0C
        pause
        exit /b 1
    )
    )
    )
)

for /f "tokens=2" %%V in ('!PYTHON_CMD! --version 2^>^&1') do set "PY_VER=%%V"
echo   Python !PY_VER! is ready.
echo.

REM ============================================================
REM STEP 2 - VERIFY PROJECT FILES
REM ============================================================
echo [STEP 2/9]  Verifying project files...
echo.

if not exist "backend\app.py" (
    echo   ERROR: backend\app.py not found.
    echo   Make sure you are running this from the project root folder.
    color 0C
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo   ERROR: requirements.txt not found.
    echo   Make sure you cloned the full repository.
    color 0C
    pause
    exit /b 1
)

echo   All project files verified.
echo.

REM ============================================================
REM STEP 3 - CREATE VIRTUAL ENVIRONMENT
REM ============================================================
echo [STEP 3/9]  Creating virtual environment...
echo.

if exist ".venv" (
    echo   Removing old virtual environment...
    rmdir /s /q ".venv" >nul 2>&1
    timeout /t 2 /nobreak >nul
)

!PYTHON_CMD! -m venv .venv
if errorlevel 1 (
    echo   ERROR: Could not create virtual environment.
    color 0C
    pause
    exit /b 1
)

echo   Virtual environment created.
echo.

REM ============================================================
REM STEP 4 - UPGRADE PIP
REM ============================================================
echo [STEP 4/9]  Upgrading pip...
echo.

call ".venv\Scripts\activate.bat"
python -m pip install --upgrade pip setuptools wheel --quiet
echo   pip is up to date.
echo.

REM ============================================================
REM STEP 5 - INSTALL ALL PYTHON PACKAGES
REM ============================================================
echo [STEP 5/9]  Installing Python packages (may take 3-5 minutes)...
echo.

pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo   WARNING: Some packages may have had issues. Retrying...
    echo.
    pip install -r requirements.txt --no-cache-dir
    if errorlevel 1 (
        echo   ERROR: Package installation failed.
        echo   Check your internet connection and try again.
        color 0C
        pause
        exit /b 1
    )
)

echo.
echo   All packages installed successfully.
echo.

REM ============================================================
REM STEP 6 - DOWNLOAD NLP DATA
REM ============================================================
echo [STEP 6/9]  Downloading NLP language data...
echo.

python -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('punkt_tab', quiet=True); nltk.download('stopwords', quiet=True); nltk.download('wordnet', quiet=True); nltk.download('averaged_perceptron_tagger_eng', quiet=True); print('NLTK data ready.')"
python -c "import textblob; from textblob import download_corpora; download_corpora.main()" >nul 2>&1
echo   NLP data ready.
echo.

REM ============================================================
REM STEP 7 - CREATE REQUIRED FOLDERS
REM ============================================================
echo [STEP 7/9]  Creating required folders...
echo.

if not exist "backend\logs"          mkdir "backend\logs"
if not exist "backend\models"        mkdir "backend\models"
if not exist "backend\flask_session" mkdir "backend\flask_session"
if not exist "backend\data"          mkdir "backend\data"
if not exist "frontend\templates"    mkdir "frontend\templates"
if not exist "frontend\static\css"   mkdir "frontend\static\css"
if not exist "frontend\static\js"    mkdir "frontend\static\js"
if not exist "frontend\static\images" mkdir "frontend\static\images"
if not exist "logs"                  mkdir "logs"

echo   All folders ready.
echo.

REM ============================================================
REM STEP 8 - TRAIN ML MODEL
REM ============================================================
echo [STEP 8/9]  Training ML model (2-3 minutes)...
echo.

if exist "backend\models\best_terrorism_detector.pkl" (
    echo   ML model already exists. Skipping training.
) else (
    cd /d "!PROJECT_DIR!backend"
    python -m src.train_pipeline
    cd /d "!PROJECT_DIR!"

    if exist "backend\models\best_terrorism_detector.pkl" (
        echo   ML model trained and saved successfully.
    ) else (
        echo   WARNING: Model training may have failed.
        echo   The app will attempt to train on first run.
    )
)
echo.

REM ============================================================
REM STEP 9 - INITIALISE DATABASE
REM ============================================================
echo [STEP 9/9]  Initialising database...
echo.

if exist "backend\data\users.json" (
    echo   Database already exists.
) else (
    cd /d "!PROJECT_DIR!backend"
    python -c "from src.database import DatabaseManager; db = DatabaseManager('json'); db.create_user('admin', 'admin@threatdetection.io', 'admin123', 'Admin'); print('Admin user created.')"
    cd /d "!PROJECT_DIR!"
)
echo.

REM ============================================================
REM DONE
REM ============================================================
color 0A
cls

echo.
echo ============================================================
echo    SETUP COMPLETE!
echo    Threat Detection Hub is ready to use.
echo    Developed by INAMULHASSAN
echo ============================================================
echo.
echo    Python:          !PY_VER!
echo    Packages:        Installed
echo    NLP Data:        Downloaded
echo    ML Model:        Ready
echo    Database:        Initialised
echo.
echo ============================================================
echo    HOW TO START
echo ============================================================
echo.
echo    Double-click  start.bat   to launch the application.
echo    Then open:    http://localhost:5000
echo    Login:        admin  /  admin123
echo.
echo ============================================================
echo.

set /p LAUNCH="Start the application now? (Y/N): "
if /i "!LAUNCH!"=="Y" (
    call start.bat
) else (
    echo.
    echo    Run start.bat whenever you are ready.
    echo.
    pause
)

endlocal
