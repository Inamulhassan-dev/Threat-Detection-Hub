@echo off
REM ============================================================================
REM THREAT DETECTION HUB - STOP SCRIPT
REM ============================================================================
REM This script stops all running Threat Detection Hub processes
REM Kills: Python (Flask), Node processes (if any)
REM ============================================================================

setlocal enabledelayedexpansion
color 0C
cls

echo.
echo ============================================================================
echo          THREAT DETECTION HUB - STOP APPLICATION
echo                    Stopping All Services
echo ============================================================================
echo.

REM Get the script directory
set "PROJECT_DIR=%~dp0"
cd /d "%PROJECT_DIR%"

echo [INFO] Project Directory: %PROJECT_DIR%
echo.

REM ============================================================================
REM Kill Python Processes (Flask)
REM ============================================================================
echo [STEP 1/3] Stopping Flask Backend...
tasklist | findstr /I "python.exe" >nul 2>&1
if %errorlevel% equ 0 (
    echo [INFO] Found Python processes running...
    taskkill /F /IM python.exe >nul 2>&1
    if %errorlevel% equ 0 (
        echo [SUCCESS] Python processes terminated
    ) else (
        echo [WARNING] Could not terminate some Python processes
    )
) else (
    echo [INFO] No Python processes found
)
echo.

REM ============================================================================
REM Kill Node Processes (if any)
REM ============================================================================
echo [STEP 2/3] Checking for Node.js processes...
tasklist | findstr /I "node.exe" >nul 2>&1
if %errorlevel% equ 0 (
    echo [INFO] Found Node.js processes running...
    taskkill /F /IM node.exe >nul 2>&1
    if %errorlevel% equ 0 (
        echo [SUCCESS] Node.js processes terminated
    ) else (
        echo [WARNING] Could not terminate some Node.js processes
    )
) else (
    echo [INFO] No Node.js processes found
)
echo.

REM ============================================================================
REM Kill Flask Development Server (by port)
REM ============================================================================
echo [STEP 3/3] Stopping Flask on port 5000...
netstat -ano | findstr /I ":5000" >nul 2>&1
if %errorlevel% equ 0 (
    echo [INFO] Process found on port 5000
    for /f "tokens=5" %%a in ('netstat -ano ^| findstr /I ":5000"') do (
        taskkill /F /PID %%a >nul 2>&1
    )
    if %errorlevel% equ 0 (
        echo [SUCCESS] Port 5000 released
    ) else (
        echo [WARNING] Could not release port 5000
    )
) else (
    echo [INFO] No process found on port 5000
)
echo.

REM ============================================================================
REM Summary
REM ============================================================================
cls
color 0A
echo.
echo ============================================================================
echo                    ALL SERVICES STOPPED SUCCESSFULLY
echo ============================================================================
echo.
echo [INFO] Summary:
echo   - Flask Backend: Stopped
echo   - All Python processes: Terminated
echo   - Port 5000: Released
echo.
echo [INFO] To restart the project:
echo   - Double-click start.bat
echo   - OR run: start.bat
echo.
echo ============================================================================
echo.
timeout /t 3 /nobreak
