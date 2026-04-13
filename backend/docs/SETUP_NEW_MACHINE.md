# Threat Detection Hub - Full Start Guide (USB + New Laptop)

Last updated: 2026-04-14
Audience: Anyone running this project for the first time

## 1. What this guide does

This guide explains exactly how to:
- copy the project using a USB drive
- set it up on a new Windows laptop
- start it
- log in and use it
- stop it safely
- fix common setup problems

## 2. Minimum requirements

- Windows 10 or Windows 11
- Internet connection for first setup
- At least 3 GB free disk space
- Administrator permission if Windows asks during Python install

Notes:
- Python does not need to be pre-installed.
- setup.bat can install Python 3.11 automatically if missing.

## 3. Files you must have

Inside the project folder, confirm these files exist:
- setup.bat
- start.bat
- stop.bat
- requirements.txt
- backend/app.py

If any are missing, use a fresh project copy.

## 4. Share using USB

On the source laptop:
1. Close running app windows.
2. Copy the full project folder Threat-Detection-Hub to USB.

On the target laptop:
1. Paste Threat-Detection-Hub from USB to a local folder (Desktop recommended).
2. Open the pasted folder.

Important:
- Do not run directly from USB for first setup.
- Always run from local disk for better speed and fewer permission issues.

## 5. First-time setup on new laptop

1. Double-click setup.bat.
2. Wait until setup completes all steps.
3. If asked Start the application now? (Y/N), choose Y to launch immediately or N to start later.

What setup.bat does:
- checks for Python 3.11+
- downloads/install Python 3.11 if needed
- creates .venv virtual environment
- installs dependencies from requirements.txt
- downloads NLP data
- creates required folders
- trains ML model files in backend/models
- initializes database/admin user

First run time can be several minutes depending on internet speed.

## 6. Start application

Method A (recommended):
1. Double-click start.bat

Method B (terminal):
1. Open PowerShell in project root
2. Run:

```powershell
.\start.bat
```

When started, open:
- http://localhost:5000

Default login:
- Username: admin
- Password: admin123

## 7. Stop application

Use one of these:
- Press Ctrl+C in the terminal running the app
- Double-click stop.bat

stop.bat attempts to free port 5000 and stop related Python processes.

## 8. Quick smoke test (2 minutes)

After login:
1. Open Dashboard tab
2. Analyze a short text sample
3. Confirm you get prediction + confidence output
4. Open History and confirm saved record exists

If these work, installation is successful.

## 9. Common problems and fixes

### Problem: setup.bat closes quickly
Fix:
- Right-click setup.bat and Run as administrator.
- Run from a local folder path without special restrictions.

### Problem: dependency installation fails
Fix:
1. Check internet connection.
2. Run setup.bat again.
3. If corporate network blocks downloads, try home network or VPN.

### Problem: app does not open on localhost:5000
Fix:
1. Run stop.bat.
2. Run start.bat again.
3. Check firewall prompt and allow Python when asked.

### Problem: wrong username/password
Fix:
- Use exact default credentials:
  - admin
  - admin123

### Problem: very slow first startup
Fix:
- First run includes model and NLP setup.
- Wait until setup fully finishes; next runs are much faster.

## 10. For classroom or multiple laptops

Repeat this order on each laptop:
1. Copy folder locally from USB
2. Run setup.bat once
3. Run start.bat each time needed

Tip:
- Do first setup while internet is stable.
- Keep one USB copy as backup in case a laptop setup is interrupted.

## 11. Optional: start manually without batch files

From project root:

```powershell
.\.venv\Scripts\activate
python -m flask --app backend.app run --host=0.0.0.0 --port=5000
```

If that fails, run:

```powershell
cd backend
python app.py
```

## 12. Security notes

- Change default admin password after first login if this is not a demo machine.
- Do not expose this development server directly to the public internet.
- Use a proper production server if deploying beyond local/testing use.

## 13. Support checklist before asking for help

Share these details:
- Windows version
- exact step where setup fails
- screenshot or copy of error text
- whether setup.bat finished all 9 steps
- whether start.bat shows Running on http://127.0.0.1:5000

This helps fix issues much faster.
