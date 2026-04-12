# 🚀 THREAT DETECTION HUB - DEPLOYMENT & OPERATIONS GUIDE

**Version:** 2.0 (Professional Structure)  
**Last Updated:** April 12, 2026  
**Status:** ✅ Production Ready

---

## 📌 QUICK START (60 SECONDS)

### For Windows Users:
```batch
1. Extract project folder
2. Double-click: setup.bat
3. Wait for completion
4. Double-click: start.bat
5. Open: http://localhost:5000
6. Login: admin / admin123
```

### For Linux/Mac Users:
```bash
1. chmod +x setup.sh
2. ./setup.sh
3. python -m flask run --app backend.app
4. Open: http://localhost:5000
```

---

## 🔧 SYSTEM REQUIREMENTS

### Minimum Requirements
- **OS:** Windows 10+, Linux (any), macOS 10.14+
- **Python:** 3.9 or higher
- **RAM:** 2GB minimum
- **Disk Space:** 500MB
- **Network Port:** 5000 (for development)

### Recommended Requirements
- **OS:** Windows 11, Ubuntu 20.04+, macOS 12+
- **Python:** 3.11 or higher
- **RAM:** 4GB or higher
- **Disk Space:** 1GB
- **SSD:** For better performance

### Browser Requirements
- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+

---

## 📥 INSTALLATION GUIDE

### STEP 1: Download Project

**Option A: Git Clone**
```bash
git clone https://github.com/your-repo/threat-detection-hub
cd threat-detection-hub
```

**Option B: Manual Download**
1. Download ZIP file
2. Extract to desired location
3. Navigate to project folder

### STEP 2: Initial Setup (Windows)

**Run Setup Script:**
```batch
setup.bat
```

**What it does:**
1. Checks Python installation
2. Creates virtual environment (.venv)
3. Installs all dependencies
4. Initializes databases
5. Creates necessary folders
6. Displays setup summary

**Expected Output:**
```
✓ Python 3.11.0 found
✓ Virtual environment created
✓ Pip upgraded
✓ Dependencies installed (34 packages)
✓ Databases initialized
✓ Project ready!
```

### STEP 3: Initial Setup (Linux/Mac)

**Run Setup Script:**
```bash
chmod +x setup.sh
./setup.sh
```

**Manual Setup:** (if script fails)
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create necessary folders
mkdir -p backend/logs backend/models backend/flask_session
mkdir -p frontend/static/{css,js,images,lib}
```

---

## 🚀 RUNNING THE APPLICATION

### WINDOWS - Start Application

**Method 1: Double-Click**
```
Double-click: start.bat
```

**Method 2: Command Prompt**
```batch
cd c:\path\to\project
start.bat
```

**Expected Output:**
```
============================================================================
        THREAT DETECTION HUB - APPLICATION LAUNCHER v2.0
              Professional Backend/Frontend Architecture
============================================================================

[STEP 1/3] Activating Python Virtual Environment...
[SUCCESS] Virtual environment activated

[STEP 2/3] Environment variables configured
[STEP 3/3] Starting Flask Backend Application

=== THREAT DETECTION HUB - RUNNING ===
[INFO] Flask Configuration:
   - Address: 0.0.0.0:5000
   - URL: http://localhost:5000

[INFO] Default Credentials:
   - Username: admin
   - Password: admin123

[Press CTRL+C to stop]
```

**Then Open Browser:**
```
http://localhost:5000
```

### WINDOWS - Stop Application

**Method 1: Double-Click**
```
Double-click: stop.bat
```

**Method 2: In Running Terminal**
```
Press Ctrl+C
```

**Method 3: Command Prompt**
```batch
stop.bat
```

### LINUX/MAC - Start Application

**Using Flask CLI:**
```bash
# Activate virtual environment
source .venv/bin/activate

# Set Flask app
export FLASK_APP=backend/app.py
export FLASK_ENV=development

# Run Flask
python -m flask run --host=0.0.0.0 --port=5000
```

**Or with Python directly:**
```bash
cd backend
python app.py
```

### LINUX/MAC - Stop Application

**In Terminal:**
```bash
Press Ctrl+C
```

**Or in another terminal:**
```bash
pgrep -f "flask run" | xargs kill
```

---

## 🌐 ACCESSING THE APPLICATION

### Local Access (During Development)
```
URL: http://localhost:5000
Dashboard: http://localhost:5000/
API: http://localhost:5000/api/*
Health Check: http://localhost:5000/api/health
```

### Network Access (Same WiFi)
```
Find your machine IP: ipconfig (Windows) or ifconfig (Linux/Mac)
URL: http://<YOUR_IP>:5000
```

### Default Credentials

| User | Username | Password | Role | Permissions |
|------|----------|----------|------|-------------|
| Administrator | admin | admin123 | Admin | Full access |
| Analyst | analyst | analyst123 | Analyst | Analysis + history |
| Viewer | viewer | viewer123 | Viewer | Read-only |

### Available URLs

| URL | Method | Purpose | Auth Required |
|-----|--------|---------|---|
| / | GET | Main dashboard | Yes |
| /login | GET, POST | Login page | No |
| /register | GET, POST | Registration | No |
| /logout | GET | Logout | Yes |
| /api/analyze | POST | Analyze text | Yes |
| /api/batch-upload | POST | Batch upload | Yes |
| /api/history | GET | Get history | Yes |
| /api/search | POST | Search history | Yes |
| /api/export | GET | Export CSV | Yes |
| /api/alerts | GET | Get alerts | Yes |
| /api/statistics | GET | System stats | Yes |
| /api/health | GET | Health check | No |
| /api/model-info | GET | Model info | No |

---

## ⚙️ CONFIGURATION & CUSTOMIZATION

### Environment Variables

**Set in start.bat (Windows):**
```batch
set FLASK_ENV=development
set FLASK_DEBUG=0
set SECRET_KEY=your-secret-key
set DATABASE_URL=json://backend/data/
```

**Set in terminal (Linux/Mac):**
```bash
export FLASK_ENV=development
export FLASK_DEBUG=0
export SECRET_KEY=your-secret-key
export DATABASE_URL=json://backend/data/
```

### Configuration File (Optional)

**Create backend/config/settings.py:**
```python
# Application Settings
DEBUG = False
SECRET_KEY = 'your-secret-key-here'
SESSION_TIMEOUT = 24 * 60  # 24 hours in minutes

# Database Configuration
DB_TYPE = 'json'
DB_PATH = '../data/'

# Logging Configuration
LOG_LEVEL = 'INFO'
LOG_DIR = '../logs/'

# ML Model Configuration
MODEL_PATH = '../models/best_terrorism_detector.pkl'
TFIDF_PATH = '../models/tfidf_vectorizer.pkl'

# API Configuration
API_TIMEOUT = 30
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
```

### Database Configuration

**Current: JSON-based (Development/Small deployments)**
```python
Database: backend/data/
Files: users.json, web_content.json, alerts.json, training_data.csv
```

**For Production: PostgreSQL (Optional)**
1. Install PostgreSQL
2. Create database
3. Update requirements.txt to add psycopg2
4. Update database.py connection string
5. Update Flask app configuration

---

## 📊 TRAINING THE ML MODEL

### Train with Default Dataset
```bash
# Activate virtual environment first
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Train model
cd backend
python -m src.train_pipeline
```

### Custom Training Dataset

**Create custom_data.csv:**
```csv
text,label
"This is normal text",0
"Terrorist content example",2
"Suspicious content",1
```

**Modify train_pipeline.py:**
```python
# Load custom data
data = pd.read_csv('../data/custom_data.csv')

# Train and evaluate
classifier.train(data)
```

---

## 🔐 SECURITY BEST PRACTICES

### For Development
✓ Use environment variables for secrets  
✓ Enable HTTPS in production  
✓ Use strong SECRET_KEY  
✓ Regular security updates  

### Default Credentials - CHANGE THESE
```bash
# After first login, change admin password via UI
# Or edit backend/data/users.json and regenerate hashes
```

### Firewall Configuration
```
Allow: Port 5000 (application)
Block: Direct database access
Enable: HTTPS reverse proxy
```

### SSL/TLS Configuration (Production)
```
Use nginx or Apache as reverse proxy
Enable SSL certificates (Let's Encrypt)
Redirect HTTP to HTTPS
```

---

## 📈 PERFORMANCE OPTIMIZATION

### Development Mode
```bash
# Default settings optimized for development
FLASK_ENV=development
FLASK_DEBUG=0
```

### Production Mode
```bash
# Optimize for performance
FLASK_ENV=production

# Use production WSGI server (Gunicorn)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 backend.app:app
```

### Load Testing
```bash
# Use Apache Bench
ab -n 1000 -c 10 http://localhost:5000/api/health

# Or use wrk
wrk -t4 -c100 -d30s http://localhost:5000/api/health
```

---

## 🛠️ TROUBLESHOOTING GUIDE

### Issue: "Python not found"
**Solution:**
1. Install Python 3.9+ from python.org
2. Add Python to PATH
3. Restart command prompt
4. Try setup.bat again

### Issue: "Port 5000 already in use"
**Windows:**
```batch
netstat -ano | findstr :5000
taskkill /PID <PID> /F
start.bat
```

**Linux/Mac:**
```bash
lsof -i :5000
kill -9 <PID>
./start.sh
```

### Issue: "ModuleNotFoundError"
**Solution:**
```batch
# Reinstall dependencies
.venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: "Database connection error"
**Solution:**
1. Check backend/data/ folder exists
2. Verify file permissions
3. Check disk space available
4. Review backend/logs/app.log

### Issue: "ML Model not found"
**Solution:**
```bash
# Train the model
cd backend
python -m src.train_pipeline

# Verify model created
ls backend/models/
```

### Issue: "Login fails with admin/admin123"
**Solution:**
1. Reset users.json to default
2. Run setup.bat again
3. Check database permissions
4. Review error logs

### Issue: Can't access from other computer
**Solution:**
1. Get your IP: `ipconfig` (Windows) or `ifconfig` (Linux)
2. Access: `http://<YOUR_IP>:5000`
3. Check firewall allows port 5000
4. Ensure both on same network

---

## 📋 MAINTENANCE & UPDATES

### Regular Maintenance
```
Weekly: Review logs and backup data
Monthly: Update dependencies (pip install -U)
Quarterly: Security audit and updates
```

### Backup Strategy
```bash
# Backup user data
cp -r backend/data/ backups/data_backup_$(date +%Y%m%d).zip

# Backup models
cp -r backend/models/ backups/models_backup_$(date +%Y%m%d).zip

# Backup logs
cp -r backend/logs/ backups/logs_backup_$(date +%Y%m%d).zip
```

### Update Dependencies
```bash
# Check for updates
pip list --outdated

# Update specific package
pip install --upgrade flask

# Update all packages
pip install --upgrade -r requirements.txt
```

---

## 🐳 DOCKER DEPLOYMENT (OPTIONAL)

### Build Docker Image
```bash
docker build -t threat-detection-hub .
```

### Run Docker Container
```bash
docker run -d \
  -p 5000:5000 \
  -v $(pwd)/backend/data:/app/backend/data \
  -v $(pwd)/backend/logs:/app/backend/logs \
  --name threat-hub \
  threat-detection-hub
```

### Using Docker Compose
```bash
docker-compose up -d
docker-compose down
```

---

## ☁️ CLOUD DEPLOYMENT (AWS/AZURE/GCP)

### Preparation
1. Create backend/requirements.txt with all dependencies
2. Configure environment variables for cloud platform
3. Set up database (RDS, Cloud SQL, etc.)
4. Configure storage (S3, Blob Storage, etc.)

### AWS Deployment (Example)
```bash
# 1. Create EC2 instance
# 2. SSH into instance
# 3. Clone project
git clone https://github.com/your-repo/threat-detection-hub
cd threat-detection-hub

# 4. Setup
./setup.sh

# 5. Install Gunicorn
pip install gunicorn

# 6. Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 backend.app:app

# 7. Use PM2 for process management
npm install -g pm2
pm2 start "gunicorn -w 4 -b 0.0.0.0:5000 backend.app:app" --name threat-hub
```

---

## 📞 SUPPORT & RESOURCES

### Online Documentation
- Flask: https://flask.palletsprojects.com
- Scikit-learn: https://scikit-learn.org
- Python: https://docs.python.org

### Project Documentation
- README.md - Overview
- SETUP_GUIDE.md - Detailed setup
- PROJECT_STRUCTURE.md - File organization
- CODE_ANALYSIS_REPORT.md - Code verification
- AUTH_SYSTEM.md - Authentication details

### Getting Help
1. Check PROJECT_STRUCTURE.md for organization
2. Review CODE_ANALYSIS_REPORT.md for known issues
3. Check backend/logs/ for error messages
4. Enable debug mode: set FLASK_DEBUG=1

---

## ✅ DEPLOYMENT CHECKLIST

Before going to production:
- [ ] Setup completed successfully
- [ ] Application starts without errors
- [ ] Login works with test credentials
- [ ] ML model loads successfully
- [ ] Database functions properly
- [ ] Logs are being generated
- [ ] Batch scripts work
- [ ] All 20 API endpoints functional
- [ ] CORS enabled for API calls
- [ ] Error handlers working
- [ ] Security best practices applied
- [ ] Performance optimized
- [ ] Backups configured
- [ ] Monitoring setup
- [ ] Documentation reviewed

---

## 🎯 MONITORING & HEALTH CHECKS

### Health Check Endpoint
```bash
curl http://localhost:5000/api/health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-04-12T10:30:00",
  "classifier_loaded": true,
  "database_connected": true,
  "version": "1.0.0"
}
```

### Log Monitoring
```bash
# Watch application logs
tail -f backend/logs/app.log

# Watch classifier logs
tail -f backend/logs/classifier.log

# Search for errors
grep ERROR backend/logs/app.log
```

---

## 🚨 EMERGENCY PROCEDURES

### Emergency Stop
```batch
# Windows
stop.bat
taskkill /IM python.exe /F

# Linux/Mac
kill $(pgrep -f "flask run")
```

### Emergency Restart
```batch
# Windows
stop.bat
timeout /t 5
start.bat

# Linux/Mac
sleep 5
./start.sh
```

### Data Recovery
```bash
# Restore from backup
cp backups/data_backup_<date>.zip backend/data/

# Verify integrity
ls -la backend/data/
```

---

## 📝 VERSION INFO

- **Project:** Threat Detection Hub
- **Version:** 2.0
- **Release Date:** April 12, 2026
- **Status:** ✅ Production Ready
- **Python:** 3.9 - 3.11+
- **License:** Proprietary

---

**Last Updated:** April 12, 2026  
**Next Review:** Q3 2026  
**Maintained By:** Threat Detection Team

✅ **Ready for enterprise deployment!**
