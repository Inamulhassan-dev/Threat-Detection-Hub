@echo off
REM ============================================================
REM   THREAT DETECTION HUB - START SCRIPT v4.0
REM   Developed by INAMULHASSAN
REM ============================================================

setlocal enabledelayedexpansion
color 0A
cls

echo.
echo ============================================================
echo    THREAT DETECTION HUB - STARTING APPLICATION
echo    Developed by INAMULHASSAN
echo ============================================================
echo.

set "PROJECT_DIR=%~dp0"
cd /d "!PROJECT_DIR!"

REM --- Check setup has been run ---
if not exist ".venv" (
    echo   Virtual environment not found. Running setup first...
    echo.
    call setup.bat
    if errorlevel 1 exit /b 1
)

if not exist "backend\app.py" (
    echo   ERROR: backend\app.py not found.
    color 0C
    pause
    exit /b 1
)

REM --- Free port 5000 if occupied ---
echo   Checking port 5000...
for /f "tokens=5" %%P in ('netstat -ano 2^>nul ^| findstr ":5000 "') do (
    taskkill /PID %%P /F >nul 2>&1
)
timeout /t 1 /nobreak >nul

REM --- Activate virtual environment ---
call ".venv\Scripts\activate.bat"

REM --- Set environment ---
set "FLASK_APP=backend.app"
set "FLASK_ENV=development"
set "FLASK_DEBUG=0"
set "PYTHONPATH=!PROJECT_DIR!backend"

echo.
echo   Application : http://localhost:5000
echo   Login       : admin / admin123
echo   Stop        : Press CTRL+C
echo.
echo ============================================================
echo.

REM --- Launch Flask ---
python -m flask --app backend.app run --host=0.0.0.0 --port=5000

if errorlevel 1 (
    echo.
    echo   Flask failed. Trying direct Python launch...
    cd /d "!PROJECT_DIR!backend"
    python app.py
    cd /d "!PROJECT_DIR!"
)

echo.
echo ============================================================
echo    APPLICATION STOPPED
echo ============================================================
echo.
pause
endlocal
