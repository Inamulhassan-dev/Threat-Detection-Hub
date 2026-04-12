# Threat Detection Hub - Windows Batch Scripts Guide

## Overview
Three automated batch scripts have been created to manage your Threat Detection Hub project on Windows. They handle setup, starting, and stopping the application.

---

## 📋 Files Created

### 1. **setup.bat** - Project Initialization
**Purpose:** Automated setup for fresh Windows installation
**Location:** `C:\Users\musha\OneDrive\Desktop\afrren\setup.bat`

#### What it does:
- ✅ Checks if Python 3.11+ is installed
- ✅ Validates pip installation
- ✅ Creates Python virtual environment (.venv)
- ✅ Installs all dependencies from requirements.txt
- ✅ Creates required project directories:
  - `data/` - Database files
  - `logs/` - Application logs
  - `models/` - ML models
  - `flask_session/` - Session storage
  - `static/` - Static files
  - `templates/` - HTML templates
- ✅ Initializes JSON databases:
  - `data/users.json` - User accounts
  - `data/web_content.json` - Analyzed content
  - `data/alerts.json` - Threat alerts

#### How to use:
```
1. Double-click setup.bat
   OR
2. Right-click → Run as Administrator
   OR
3. Open Command Prompt in project folder and type: setup.bat
```

#### Output:
- [SUCCESS] messages = Everything installed correctly
- [ERROR] messages = Something needs attention

#### Requirements:
- Windows 7 or newer
- Admin privileges recommended
- Internet connection for package downloads
- 500MB free disk space

---

### 2. **start.bat** - Start Application
**Purpose:** Launch the entire Threat Detection Hub application
**Location:** `C:\Users\musha\OneDrive\Desktop\afrren\start.bat`

#### What it does:
- ✅ Activates Python virtual environment
- ✅ Validates setup completion
- ✅ Starts Flask backend on port 5000
- ✅ Displays startup information
- ✅ Shows login credentials
- ✅ Waits for user input (CTRL+C to stop)

#### How to use:
```
1. Double-click start.bat
   OR
2. Open Command Prompt and type: start.bat
```

#### What happens:
- Console displays: `* Running on http://127.0.0.1:5000`
- Application accessible at: `http://localhost:5000`
- Login page automatically shown
- Backend processes requests

#### Access Information:
```
URL: http://localhost:5000/login
Username: admin
Password: admin123
```

#### Output:
```
[STEP 1/2] Activating Python Virtual Environment...
[SUCCESS] Virtual environment activated

[STEP 2/2] Starting Flask Backend Server...
[INFO] Flask Server Configuration:
   - Host: 0.0.0.0
   - Port: 5000
   - URL: http://localhost:5000
```

#### To Stop:
- Press `CTRL+C` in the console
- OR use stop.bat in another window

---

### 3. **stop.bat** - Stop Application
**Purpose:** Gracefully stop all running services
**Location:** `C:\Users\musha\OneDrive\Desktop\afrren\stop.bat`

#### What it does:
- ✅ Finds and terminates Python processes
- ✅ Finds and terminates Node.js processes (if any)
- ✅ Releases port 5000
- ✅ Cleans up all running services
- ✅ Displays confirmation message

#### How to use:
```
1. Double-click stop.bat (from start.bat console)
   OR
2. Open new Command Prompt and type: stop.bat
   OR
3. Press CTRL+C in start.bat console
```

#### Output:
```
[STEP 1/3] Stopping Flask Backend...
[SUCCESS] Python processes terminated

[STEP 2/3] Checking for Node.js processes...
[INFO] No Node.js processes found

[STEP 3/3] Stopping Flask on port 5000...
[SUCCESS] Port 5000 released

[INFO] Summary:
   - Flask Backend: Stopped
   - All Python processes: Terminated
   - Port 5000: Released
```

---

## 🚀 Quick Start Guide

### First Time Setup:
```
1. Open Command Prompt
2. Navigate to: C:\Users\musha\OneDrive\Desktop\afrren
3. Run: setup.bat
4. Wait for "SETUP COMPLETED SUCCESSFULLY"
5. Review displayed instructions
```

### Start Application:
```
1. Open Command Prompt
2. Navigate to: C:\Users\musha\OneDrive\Desktop\afrren
3. Run: start.bat
4. Open browser to: http://localhost:5000/login
5. Enter credentials: admin / admin123
```

### Stop Application:
```
1. Option A: Press CTRL+C in start.bat window
2. Option B: Open new Command Prompt and run: stop.bat
3. Wait for confirmation message
```

---

## 🔧 Troubleshooting

### Problem: "Python not found"
**Solution:**
- Download from: https://www.python.org/downloads/
- During installation: ✓ Check "Add Python to PATH"
- Re-run setup.bat

### Problem: "Virtual environment not found"
**Solution:**
- Run setup.bat again
- Or manually run: `python -m venv .venv`

### Problem: "Port 5000 already in use"
**Solution:**
- Run stop.bat to release port
- Or use: `netstat -ano | findstr :5000`

### Problem: "Permission denied"
**Solution:**
- Right-click batch file → Run as Administrator
- Or open Command Prompt as Administrator first

### Problem: "requirements.txt not found"
**Solution:**
- Ensure you're in project root directory
- File should be: `c:\Users\musha\OneDrive\Desktop\afrren\requirements.txt`

---

## 📊 Environment Details

### Python Virtual Environment
- **Location:** `.venv/` (in project folder)
- **Python Version:** 3.11+
- **Packages:** Installed from requirements.txt
- **Size:** ~500MB

### Project Structure After Setup:
```
afrren/
├── .venv/                      # Virtual environment
├── app.py                      # Flask application
├── requirements.txt            # Python packages
├── setup.bat                   # Setup script
├── start.bat                   # Start script
├── stop.bat                    # Stop script
├── src/                        # Source code
├── templates/                  # HTML templates
├── static/                     # CSS, JS files
├── data/                       # Data files
│   ├── users.json             # User database
│   ├── web_content.json       # Analysis records
│   └── alerts.json            # Alerts database
├── logs/                       # Application logs
├── models/                     # ML models
└── flask_session/             # Session files
```

---

## 🔐 Security Notes

### Default Login:
```
Username: admin
Password: admin123
```

**IMPORTANT:** Change this password after first login via dashboard.

### Virtual Environment:
- Isolates project dependencies
- Prevents system-wide package conflicts
- Can be safely deleted (setup recreates it)

### Port 5000:
- Used exclusively by Flask
- Released when application stops
- Can be changed in start.bat if needed

---

## ✅ Verification Checklist

After running each script, verify:

**After setup.bat:**
- [ ] No error messages displayed
- [ ] ".venv" folder created
- [ ] "Setup Complete" message shown
- [ ] All directories created

**After start.bat:**
- [ ] Flask server shows "Running on..."
- [ ] Port 5000 is accessible
- [ ] No errors in console
- [ ] Can access http://localhost:5000

**After stop.bat:**
- [ ] All processes terminated
- [ ] Port 5000 released
- [ ] No python.exe in Task Manager
- [ ] Confirmation message displayed

---

## 📝 Command Reference

| Command | Windows | Purpose |
|---------|---------|---------|
| `setup.bat` | Double-click or via CMD | Initial project setup |
| `start.bat` | Double-click or via CMD | Launch application |
| `stop.bat` | Double-click or via CMD | Stop all services |
| `CTRL+C` | In start.bat console | Emergency stop |

---

## 🎯 Common Workflows

### Fresh Installation:
```
1. setup.bat     → Setup project (once)
2. start.bat     → Start application
3. (use app)
4. stop.bat      → Stop application
```

### Daily Usage:
```
1. start.bat     → Run application
2. (use app)
3. stop.bat      → Stop when done
```

### Troubleshooting:
```
1. stop.bat      → Stop all services
2. setup.bat     → Reinitialize
3. start.bat     → Start fresh
```

---

## 📞 Support

### Logs Location:
- `logs/app.log` - Application logs
- `logs/database.log` - Database operations

### Database Files:
- `data/users.json` - User accounts
- `data/web_content.json` - Analysis records
- `data/alerts.json` - Alert records

### Configuration:
- `app.py` - Main Flask application
- `requirements.txt` - All dependencies
- `.venv/` - Virtual environment

---

## 🎉 You're All Set!

Your Threat Detection Hub is now set up and ready to use on any Windows machine.

**Next Steps:**
1. Run `setup.bat` - One-time setup
2. Run `start.bat` - Each time you want to use it
3. Run `stop.bat` - When you're done

**Enjoy!** 🚀

---

**Last Updated:** 2024-04-12
**Version:** 1.0
**Platform:** Windows 7+
