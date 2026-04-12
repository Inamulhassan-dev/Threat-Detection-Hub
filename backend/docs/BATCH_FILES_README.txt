╔══════════════════════════════════════════════════════════════════════════════╗
║                    THREAT DETECTION HUB - BATCH FILES READY                   ║
║                         Windows Automation Scripts                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

📁 PROJECT FOLDER: C:\Users\musha\OneDrive\Desktop\afrren

✅ THREE BATCH FILES CREATED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣  SETUP.BAT - INITIAL PROJECT SETUP
   ┌─────────────────────────────────────────────────────────────────────────┐
   │ Purpose: Automated Windows laptop setup (run ONCE)                      │
   │                                                                          │
   │ What it does:                                                           │
   │ ✓ Validates Python 3.11+ installation                                   │
   │ ✓ Validates pip package manager                                         │
   │ ✓ Creates Python virtual environment (.venv)                            │
   │ ✓ Installs all dependencies from requirements.txt                       │
   │ ✓ Creates project directories (data, logs, models, etc.)                │
   │ ✓ Initializes JSON databases                                            │
   │                                                                          │
   │ Usage: Double-click setup.bat (or: setup.bat in Command Prompt)         │
   │ Time: ~2-5 minutes (depending on internet speed)                        │
   │ Frequency: Run ONCE per machine                                         │
   └─────────────────────────────────────────────────────────────────────────┘

2️⃣  START.BAT - RUN THE APPLICATION
   ┌─────────────────────────────────────────────────────────────────────────┐
   │ Purpose: Start Flask backend and web application                        │
   │                                                                          │
   │ What it does:                                                           │
   │ ✓ Activates Python virtual environment                                  │
   │ ✓ Verifies setup completion                                             │
   │ ✓ Starts Flask on port 5000                                             │
   │ ✓ Displays login credentials                                            │
   │ ✓ Keeps server running (shows real-time output)                         │
   │                                                                          │
   │ Usage: Double-click start.bat (or: start.bat in Command Prompt)         │
   │ Access: http://localhost:5000/login                                     │
   │ Login: admin / admin123                                                 │
   │ Stop: Press CTRL+C in console                                           │
   └─────────────────────────────────────────────────────────────────────────┘

3️⃣  STOP.BAT - STOP ALL SERVICES
   ┌─────────────────────────────────────────────────────────────────────────┐
   │ Purpose: Gracefully terminate all running processes                     │
   │                                                                          │
   │ What it does:                                                           │
   │ ✓ Terminates Python processes (Flask)                                   │
   │ ✓ Terminates Node.js processes (if any)                                 │
   │ ✓ Releases port 5000                                                    │
   │ ✓ Displays confirmation of stopping                                     │
   │                                                                          │
   │ Usage: Double-click stop.bat (or: stop.bat in new Command Prompt)       │
   │ Alternative: Press CTRL+C in start.bat console                          │
   │ Time: ~1-2 seconds                                                      │
   └─────────────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 QUICK START - COMPLETE WORKFLOW:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1 - FIRST TIME ONLY:
├─ Open Command Prompt
├─ Navigate to: C:\Users\musha\OneDrive\Desktop\afrren
├─ Run: setup.bat
├─ Wait for completion message
└─ Review setup information

STEP 2 - EVERY TIME YOU WANT TO USE IT:
├─ Double-click: start.bat
├─ Wait for: "Running on http://127.0.0.1:5000"
├─ Open browser: http://localhost:5000/login
├─ Login: admin / admin123
└─ Use the application

STEP 3 - WHEN YOU'RE DONE:
├─ Option A: Press CTRL+C in start.bat window
├─ Option B: Double-click: stop.bat
└─ All services stopped

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 FILE LOCATIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Project Root:
   C:\Users\musha\OneDrive\Desktop\afrren\

📄 Batch Files:
   • setup.bat          → Initial setup and configuration
   • start.bat          → Start the application
   • stop.bat           → Stop all running services

📂 Created After Setup:
   • .venv/             → Python virtual environment (auto-created)
   • data/              → Database files
   • logs/              → Application logs
   • models/            → ML model files
   • flask_session/     → Session storage

📊 Data Files:
   • data/users.json        → User database
   • data/web_content.json  → Analysis records
   • data/alerts.json       → Alert records

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ FEATURES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Fully Automated Setup
  • Detects existing Python and skips if present
  • Validates all dependencies
  • Creates only missing directories
  • Handles errors gracefully

✓ Easy Start/Stop
  • Single click to start
  • Single click to stop
  • Real-time console output
  • Clear status messages

✓ Intelligent Error Handling
  • Checks prerequisites before running
  • Provides helpful error messages
  • Suggests solutions
  • Validates setup completion

✓ For Fresh Windows Machines
  • Works on clean Windows installations
  • Downloads all required packages
  • No manual setup needed
  • Fully portable

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 REQUIREMENTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Windows 7 or newer
✓ Python 3.11+ (auto-installed if needed)
✓ 500MB free disk space
✓ Internet connection for package downloads
✓ Admin privileges (recommended for setup)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔐 LOGIN CREDENTIALS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

URL:      http://localhost:5000/login
Username: admin
Password: admin123

🚨 IMPORTANT: Change the default password after first login!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📞 TROUBLESHOOTING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Issue: "Python not found"
→ Download from https://www.python.org/downloads/
→ During install: CHECK "Add Python to PATH"
→ Re-run setup.bat

Issue: "Port 5000 already in use"
→ Run: stop.bat
→ Wait a few seconds
→ Run: start.bat again

Issue: "Virtual environment not found"
→ Run: setup.bat again
→ It will recreate the environment

Issue: "Permission denied"
→ Right-click batch file → Run as Administrator
→ Or open Command Prompt as Administrator first

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📖 ADDITIONAL DOCUMENTATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For detailed documentation, see:
→ BATCH_SCRIPTS_GUIDE.md  (Complete guide with examples)
→ README.md               (Project overview)
→ QUICK_START.md          (Getting started guide)
→ SETUP_GUIDE.md          (Detailed setup instructions)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎉 YOU'RE ALL SET!

Your Threat Detection Hub is now ready to deploy on any Windows machine.

                    START YOUR FIRST RUN:
                    ➜ Double-click: start.bat
                    ➜ Access: http://localhost:5000
                    ➜ Login: admin / admin123
                    ➜ Enjoy! 🚀

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Version: 1.0
Created: 2024-04-12
Platform: Windows 7+

╔══════════════════════════════════════════════════════════════════════════════╗
║            All batch files are ready to use! Happy coding! 🎯               ║
╚══════════════════════════════════════════════════════════════════════════════╝
