# Complete Setup & Deployment Guide

## Step-by-Step Installation

### Step 1: Install Python Dependencies

```bash
cd terrorism-detection-system
pip install -r requirements.txt
```

### Step 2: Download NLP Models

```bash
# Option 1: Using Python
python -c "import nltk; nltk.download('all')"
python -m spacy download en_core_web_sm

# Option 2: Manual download (if above fails)
python
>>> import nltk
>>> nltk.download('stopwords')
>>> nltk.download('punkt')
>>> nltk.download('wordnet')
>>> exit()
```

### Step 3: Train the Model

```bash
# This creates sample dataset and trains the model
python -m src.train_pipeline
```

Output should show:
```
Starting Training Pipeline...
============================================================
Loading training data...
Preprocessing texts...
Extracting TF-IDF features...
Splitting data...

Training models...
Training random_forest...
Training naive_bayes...
Training svm...

Evaluating models...
===================================
Evaluating random_forest:
===================================
...
Best Model: random_forest
Accuracy: 0.9583 (95.83%)
===================================
```

### Step 4: Start the Application

```bash
# Option 1: Development mode
python app.py

# Option 2: Production mode with gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Step 5: Access the Web Interface

Open browser and navigate to:
```
http://localhost:5000
```

## Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Build and start all services
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f web

# Stop services
docker-compose down
```

### Using Docker Alone

```bash
# Build image
docker build -t terrorism-detector:latest .

# Run container
docker run -p 5000:5000 -v $(pwd)/data:/app/data -v $(pwd)/logs:/app/logs terrorism-detector:latest

# Windows PowerShell
docker run -p 5000:5000 -v C:\path\to\project\data:/app/data terrorism-detector:latest
```

## Production Deployment

### Option 1: AWS Deployment

```bash
# 1. Create EC2 instance (Ubuntu 20.04)
# 2. SSH into instance
ssh -i key.pem ubuntu@instance-ip

# 3. Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 4. Clone repository
git clone <repository-url>
cd terrorism-detection-system

# 5. Deploy with Docker Compose
docker-compose up -d

# 6. Set up SSL with Let's Encrypt
sudo apt-get install certbot python3-certbot-nginx
```

### Option 2: Heroku Deployment

```bash
# 1. Install Heroku CLI
# 2. Login
heroku login

# 3. Create app
heroku create terrorism-detection-system

# 4. Push to Heroku
git push heroku main

# 5. View logs
heroku logs --tail
```

### Option 3: Kubernetes Deployment

Create `k8s-deployment.yaml`:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: terrorism-detection
spec:
  replicas: 3
  selector:
    matchLabels:
      app: terrorism-detection
  template:
    metadata:
      labels:
        app: terrorism-detection
    spec:
      containers:
      - name: app
        image: terrorism-detector:latest
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

Deploy:
```bash
kubectl apply -f k8s-deployment.yaml
```

## System Integration Examples

### 1. Integrate with External Web Services

```python
from src.data_collector import WebDataCollector
from src.classifier import ContentClassifier

collector = WebDataCollector()
classifier = ContentClassifier()

# Scrape and analyze
data = collector.scrape_website('https://example.com')
if data:
    result = classifier.predict(data['content'])
    print(result['prediction'])
```

### 2. Batch Processing

```python
from src.classifier import ContentClassifier

classifier = ContentClassifier()

texts = [
    "Text 1 to analyze",
    "Text 2 to analyze",
    "Text 3 to analyze"
]

for text in texts:
    result = classifier.predict(text)
    print(f"{text[:30]}... -> {result['prediction']}")
```

### 3. Custom Model Training with Your Data

```python
import pandas as pd
from src.feature_extractor import FeatureExtractor
from src.model_trainer import TerrorismDetectionModel
from sklearn.model_selection import train_test_split

# Load your dataset
df = pd.read_csv('your_data.csv')  # Columns: ['text', 'label']

# Extract features
extractor = FeatureExtractor()
processed = [text.lower() for text in df['text']]
X = extractor.extract_tfidf_features(processed)
y = df['label'].values

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

trainer = TerrorismDetectionModel()
models = trainer.train_models(X_train, y_train)

# Evaluate
for name, model in models.items():
    accuracy = trainer.evaluate_model(model, X_test, y_test)
    print(f"{name}: {accuracy:.2%}")
```

## Performance Optimization

### 1. Caching

```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def predict_cached(text):
    classifier = ContentClassifier()
    return classifier.predict(text)
```

### 2. Batch Processing

```python
import numpy as np

texts = [...]  # Large list of texts
batch_size = 32

for i in range(0, len(texts), batch_size):
    batch = texts[i:i+batch_size]
    results = process_batch(batch)
```

### 3. Database Indexing

For MongoDB:
```python
db.web_content.create_index([("timestamp", -1)])
db.web_content.create_index([("prediction", 1)])
```

## Monitoring & Maintenance

### 1. Health Check

```bash
curl http://localhost:5000/api/health
```

### 2. Monitor Logs

```bash
# Real-time log monitoring
tail -f logs/app.log
tail -f logs/alerts.log

# Search logs
grep "ALERT" logs/alerts.log
grep "ERROR" logs/app.log
```

### 3. Model Retraining

```bash
# Set up scheduled retraining
python -m src.train_pipeline  # Run weekly/monthly
```

### 4. Database Backup

```bash
# MongoDB backup
mongodump --db terrorism_detection --out backup/

# Restore
mongorestore --db terrorism_detection backup/terrorism_detection/
```

## Troubleshooting

### Issue: Port 5000 Already in Use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Issue: Model Load Error
```bash
# Retrain
python -m src.train_pipeline

# Verify model exists
ls -la models/
```

### Issue: NLP Model Missing
```bash
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('all')"
```

### Issue: Database Connection Error
```python
# Test connection
from src.database import DatabaseManager
db = DatabaseManager('json')
db.insert_content({'test': 'data'})
```

## Security Hardening

### 1. API Authentication

```python
from functools import wraps
from flask import request, jsonify

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('X-API-Token')
        if not token or token != os.getenv('API_TOKEN'):
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/api/analyze', methods=['POST'])
@token_required
def analyze_content():
    # ...
```

### 2. Rate Limiting

```bash
pip install flask-limiter

from flask_limiter import Limiter
limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/analyze', methods=['POST'])
@limiter.limit("10 per minute")
def analyze_content():
    # ...
```

### 3. HTTPS/SSL

```bash
pip install pyopenssl

# Generate self-signed certificate
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

# Run with SSL
python app.py --ssl_context=('cert.pem', 'key.pem')
```

## Performance Benchmarks

Typical performance metrics:
- Model training: 5-10 seconds (with sample data)
- Single prediction: 50-100ms
- Batch processing (100 items): 5-10 seconds
- Web API response time: 100-200ms

## FAQ

**Q: Can I use the system without Docker?**
A: Yes, just install dependencies and run `python app.py`

**Q: How often should I retrain the model?**
A: Monthly or when accuracy drops below acceptable threshold

**Q: Can I integrate with my existing system?**
A: Yes, use the API endpoints or import modules directly

**Q: What's the minimum hardware requirement?**
A: 2GB RAM, 2GB disk space, modern CPU

**Q: Is the system GDPR compliant?**
A: Ensure you handle personal data according to regulations

---

For more help, refer to README.md or check logs for error messages.
