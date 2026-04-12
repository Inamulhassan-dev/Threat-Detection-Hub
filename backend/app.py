"""
=====================================================================
THREAT DETECTION HUB - BACKEND APPLICATION
=====================================================================
Main Flask application with authentication, analysis, and API endpoints
Modern, professional backend serving REST API and web interface
=====================================================================
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_cors import CORS
from flask_session import Session
from src.classifier import ContentClassifier
from src.alert_system import AlertSystem
from src.database import DatabaseManager
from datetime import datetime, timedelta
import json
import os
import logging
import functools
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Base directory — always the backend/ folder, regardless of where Python is launched from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ================================================================================
# FLASK APPLICATION CONFIGURATION
# ================================================================================

app = Flask(
    __name__,
    template_folder='../frontend/templates',
    static_folder='../frontend/static'
)

# Security and Session Configuration
app.config['SECRET_KEY'] = 'threat-detection-secret-key-2024-secure'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
app.config['SESSION_FILE_DIR'] = os.path.join(BASE_DIR, 'flask_session')

Session(app)
CORS(app)

# ================================================================================
# LOGGING CONFIGURATION
# ================================================================================

if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(BASE_DIR, 'logs', 'app.log')),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("=" * 70)
logger.info("THREAT DETECTION HUB - BACKEND LOGGER INITIALIZED")
logger.info("=" * 70)

# ================================================================================
# COMPONENT INITIALIZATION
# ================================================================================

try:
    classifier = ContentClassifier()
    logger.info("✓ ContentClassifier loaded successfully")
except Exception as e:
    logger.error(f"✗ Error loading ContentClassifier: {str(e)}")
    classifier = None

alert_system = AlertSystem()
logger.info("✓ AlertSystem initialized")

db = DatabaseManager('json')
logger.info("✓ DatabaseManager initialized")

# ================================================================================
# STATISTICS TRACKER
# ================================================================================

stats = {
    'total_analyzed': 0,
    'threats_detected': 0,
    'alerts_sent': 0,
    'accuracy': 94.5,
    'system_status': 'operational'
}

logger.info("✓ Statistics tracker initialized")

# ================================================================================
# AUTHENTICATION DECORATORS
# ================================================================================

def login_required(f):
    """Decorator: Check if user is logged in"""
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            if request.path.startswith('/api/'):
                return jsonify({'success': False, 'message': 'Authentication required'}), 401
            logger.warning(f"Unauthorized access attempt to {request.path}")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def role_required(*roles):
    """Decorator: Check if user has required role"""
    def decorator(f):
        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            if 'username' not in session:
                if request.path.startswith('/api/'):
                    return jsonify({'success': False, 'message': 'Authentication required'}), 401
                return redirect(url_for('login'))
            
            user = db.get_user(session['username'])
            if not user or user['role'] not in roles:
                if request.path.startswith('/api/'):
                    logger.warning(f"User {session.get('username')} denied access to {request.path}")
                    return jsonify({'success': False, 'message': 'Insufficient permissions'}), 403
                return jsonify({'error': 'Insufficient permissions'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# ================================================================================
# AUTHENTICATION ROUTES
# ================================================================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page and authentication endpoint"""
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        if not username or not password:
            msg = 'Username and password required'
            if request.is_json:
                return jsonify({'success': False, 'message': msg}), 400
            logger.warning(f"Login attempt with missing credentials")
            return render_template('login.html', error=msg)
        
        result = db.authenticate_user(username, password)
        
        if result['success']:
            session['username'] = username
            session['email'] = result['user']['email']
            session['role'] = result['user']['role']
            session.permanent = True
            
            logger.info(f"✓ User '{username}' logged in successfully")
            
            if request.is_json:
                return jsonify(result)
            return redirect(url_for('dashboard'))
        else:
            logger.warning(f"✗ Failed login attempt for user '{username}'")
            if request.is_json:
                return jsonify(result), 401
            return render_template('login.html', error=result['message'])
    
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration endpoint"""
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()
        confirm_password = data.get('confirm_password', '').strip()
        
        # Validation
        if not username or not email or not password:
            msg = 'All fields required'
            if request.is_json:
                return jsonify({'success': False, 'message': msg}), 400
            return render_template('login.html', error=msg, tab='register')
        
        if len(password) < 6:
            msg = 'Password must be at least 6 characters'
            if request.is_json:
                return jsonify({'success': False, 'message': msg}), 400
            return render_template('login.html', error=msg, tab='register')
        
        if password != confirm_password:
            msg = 'Passwords do not match'
            if request.is_json:
                return jsonify({'success': False, 'message': msg}), 400
            return render_template('login.html', error=msg, tab='register')
        
        result = db.create_user(username, email, password, 'Viewer')
        
        if result['success']:
            logger.info(f"✓ New user registered: '{username}'")
            if request.is_json:
                return jsonify({'success': True, 'message': 'Registration successful. Please login.'}), 201
            return render_template('login.html', success='Registration successful. Please login.')
        else:
            logger.warning(f"✗ Registration failed for '{username}': {result['message']}")
            if request.is_json:
                return jsonify(result), 400
            return render_template('login.html', error=result['message'], tab='register')
    
    return render_template('login.html', tab='register')


@app.route('/logout')
def logout():
    """Logout user and clear session"""
    username = session.get('username', 'Unknown')
    session.clear()
    logger.info(f"✓ User '{username}' logged out")
    return redirect(url_for('login'))

# ================================================================================
# USER PROFILE & AUTH API ROUTES
# ================================================================================

@app.route('/api/auth/user')
@login_required
def get_current_user():
    """Get current logged-in user information"""
    user = db.get_user(session['username'])
    if user:
        user.pop('password_hash', None)
        user.pop('password_salt', None)
        return jsonify({'success': True, 'user': user})
    return jsonify({'success': False, 'message': 'User not found'}), 404


@app.route('/api/auth/change-password', methods=['POST'])
@login_required
def change_password():
    """Change user password"""
    data = request.get_json()
    old_password = data.get('old_password', '').strip()
    new_password = data.get('new_password', '').strip()
    confirm_password = data.get('confirm_password', '').strip()
    
    if not old_password or not new_password:
        return jsonify({'success': False, 'message': 'All fields required'}), 400
    
    if len(new_password) < 6:
        return jsonify({'success': False, 'message': 'Password must be at least 6 characters'}), 400
    
    if new_password != confirm_password:
        return jsonify({'success': False, 'message': 'Passwords do not match'}), 400
    
    result = db.update_password(session['username'], old_password, new_password)
    
    if result['success']:
        logger.info(f"✓ User '{session['username']}' changed password")
        return jsonify(result)
    return jsonify(result), 400


@app.route('/api/admin/users')
@role_required('Admin')
def list_users():
    """Get list of all users (Admin only)"""
    users = db.list_users()
    # Remove sensitive data
    for user in users:
        user.pop('password_hash', None)
        user.pop('password_salt', None)
    return jsonify({'success': True, 'users': users})

# ================================================================================
# MAIN DASHBOARD ROUTE
# ================================================================================

@app.route('/')
@login_required
def dashboard():
    """Main dashboard page"""
    logger.info(f"Dashboard accessed by {session['username']}")
    return render_template('index.html')

# ================================================================================
# CONTENT ANALYSIS API ROUTES
# ================================================================================

@app.route('/api/analyze', methods=['POST'])
@login_required
def analyze_content():
    """Analyze single text content for terrorism-related material"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        source = data.get('source', 'web_interface')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        if classifier is None:
            logger.error("Classifier not initialized")
            return jsonify({'error': 'Classifier not initialized. Please train the model first.'}), 500
        
        # Classify content
        result = classifier.predict(text)
        
        # Update statistics
        stats['total_analyzed'] += 1
        if result['prediction_code'] in [1, 2]:
            stats['threats_detected'] += 1
        
        # Store in database
        record = {
            'text': text,
            'source': source,
            'prediction': result,
            'timestamp': datetime.now().isoformat(),
            'user': session['username']
        }
        db.insert_content(record)
        
        # Check if alert needed
        alert_triggered = alert_system.should_alert(result)
        if alert_triggered:
            alert = alert_system.generate_alert(result, {'source': source, 'user': session['username']})
            alert_system.send_email_alert(alert)
            alert_system.save_alert(alert)
            stats['alerts_sent'] += 1
            result['alert_triggered'] = True
        else:
            result['alert_triggered'] = False
        
        logger.info(f"Analysis by {session['username']}: {result['prediction']} (Confidence: {result['confidence']:.4f})")
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Error in analyze_content: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/batch-upload', methods=['POST'])
@login_required
def batch_upload():
    """Handle batch text upload and analysis"""
    try:
        data = request.get_json()
        texts = data.get('texts', [])
        
        if not texts or not isinstance(texts, list):
            return jsonify({'error': 'Please provide a list of texts'}), 400
        
        if classifier is None:
            return jsonify({'error': 'Classifier not initialized'}), 500
        
        results = []
        for text in texts:
            if isinstance(text, str) and text.strip():
                result = classifier.predict(text.strip())
                results.append({
                    'text': text.strip()[:200],
                    'prediction': result['prediction'],
                    'confidence': result['confidence'],
                    'alert_triggered': result.get('alert_triggered', False)
                })
                
                # Update statistics
                stats['total_analyzed'] += 1
                if result.get('prediction_code') in [1, 2]:
                    stats['threats_detected'] += 1
        
        logger.info(f"Batch analysis by {session['username']}: {len(results)} texts analyzed")
        return jsonify({'results': results, 'count': len(results)})
    except Exception as e:
        logger.error(f"Error in batch upload: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/batch-analyze', methods=['POST'])
@login_required
def batch_analyze():
    """Analyze multiple texts with metadata"""
    try:
        data = request.get_json()
        items = data.get('items', [])
        
        if not items:
            return jsonify({'error': 'No items provided'}), 400
        
        if classifier is None:
            return jsonify({'error': 'Classifier not initialized'}), 500
        
        results = []
        for item in items:
            text = item.get('text', '').strip()
            if text:
                result = classifier.predict(text)
                result['source'] = item.get('source', 'unknown')
                results.append(result)
                
                stats['total_analyzed'] += 1
                if result['prediction_code'] in [1, 2]:
                    stats['threats_detected'] += 1
        
        logger.info(f"Batch analyzed {len(results)} items by {session['username']}")
        return jsonify({'results': results})
        
    except Exception as e:
        logger.error(f"Error in batch_analyze: {str(e)}")
        return jsonify({'error': str(e)}), 500

# ================================================================================
# DATA RETRIEVAL & HISTORY ROUTES
# ================================================================================

@app.route('/api/history', methods=['GET'])
@login_required
def get_history():
    """Get analysis history with pagination"""
    try:
        limit = request.args.get('limit', 50, type=int)
        offset = request.args.get('offset', 0, type=int)
        
        all_contents = db.get_all_contents()
        total = len(all_contents)
        
        # Paginate results
        history = all_contents[offset:offset + limit]
        
        logger.info(f"History retrieved by {session['username']}: {len(history)} records")
        return jsonify({
            'history': history,
            'total': total,
            'limit': limit,
            'offset': offset,
            'count': len(history)
        })
    except Exception as e:
        logger.error(f"Error retrieving history: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/search', methods=['POST'])
@login_required
def search_history():
    """Search and filter analysis history"""
    try:
        data = request.get_json()
        search_term = data.get('search_term', '').lower()
        min_confidence = data.get('min_confidence', 0)
        max_confidence = data.get('max_confidence', 1)
        prediction_filter = data.get('prediction', None)
        
        all_contents = db.get_all_contents()
        results = []
        
        for record in all_contents:
            pred = record.get('prediction', {})
            text = record.get('text', '').lower()
            confidence = pred.get('confidence', 0)
            prediction = pred.get('prediction', '')
            
            # Apply filters
            if search_term and search_term not in text:
                continue
            if not (min_confidence <= confidence <= max_confidence):
                continue
            if prediction_filter and prediction != prediction_filter:
                continue
            
            results.append(record)
        
        logger.info(f"Search by {session['username']} returned {len(results)} results")
        return jsonify({'results': results, 'count': len(results)})
    except Exception as e:
        logger.error(f"Error searching history: {str(e)}")
        return jsonify({'error': str(e)}), 500

# ================================================================================
# EXPORT & ANALYTICS ROUTES
# ================================================================================

@app.route('/api/export', methods=['GET'])
@login_required
def export_results():
    """Export analysis results as CSV"""
    try:
        import csv
        from io import StringIO
        
        all_contents = db.get_all_contents()
        
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(['Timestamp', 'User', 'Text Preview', 'Prediction', 'Confidence', 'Keyword Score', 'Alert'])
        
        for record in all_contents:
            pred = record.get('prediction', {})
            text_preview = record.get('text', '')[:100]
            writer.writerow([
                record.get('timestamp', 'N/A'),
                record.get('user', 'Unknown'),
                text_preview,
                pred.get('prediction', 'N/A'),
                f"{pred.get('confidence', 0):.4f}",
                f"{pred.get('keyword_score', 0):.4f}",
                pred.get('alert_triggered', False)
            ])
        
        logger.info(f"Export by {session['username']}: {len(all_contents)} records")
        return output.getvalue(), 200, {
            'Content-Disposition': 'attachment; filename="threat_analysis_export.csv"',
            'Content-Type': 'text/csv'
        }
    except Exception as e:
        logger.error(f"Error exporting results: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/alerts', methods=['GET'])
@login_required
def get_alerts():
    """Retrieve recent alerts"""
    try:
        alerts = alert_system.get_recent_alerts(limit=50)
        logger.info(f"Alerts retrieved by {session['username']}: {len(alerts)} alerts")
        return jsonify({'alerts': alerts, 'count': len(alerts)})
    except Exception as e:
        logger.error(f"Error retrieving alerts: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/statistics', methods=['GET'])
@login_required
def get_statistics():
    """Get system statistics"""
    try:
        return jsonify(stats)
    except Exception as e:
        logger.error(f"Error getting statistics: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/model-info', methods=['GET'])
def get_model_info():
    """Get information about the trained model"""
    try:
        model_path = 'models/best_terrorism_detector.pkl'
        model_exists = os.path.exists(model_path)
        
        if model_exists:
            model_size = os.path.getsize(model_path) / 1024
        else:
            model_size = 0
        
        model_info = {
            'model_loaded': classifier is not None and classifier.model is not None,
            'model_type': 'Random Forest Classifier' if classifier and classifier.model else 'None',
            'model_path': model_path,
            'model_exists': model_exists,
            'model_size_kb': round(model_size, 2),
            'vectorizer_loaded': classifier is not None and classifier.tfidf is not None,
            'total_features': 150,
            'classes': ['Normal', 'Suspicious', 'Terrorist-Related'],
            'accuracy': stats.get('accuracy', 0),
            'total_samples_analyzed': stats.get('total_analyzed', 0),
            'threats_detected': stats.get('threats_detected', 0)
        }
        
        return jsonify(model_info)
    except Exception as e:
        logger.error(f"Error retrieving model info: {str(e)}")
        return jsonify({'error': str(e)}), 500

# ================================================================================
# SAMPLE & UTILITY ROUTES
# ================================================================================

@app.route('/api/samples', methods=['GET'])
@login_required
def get_samples():
    """Get sample texts for quick testing"""
    try:
        samples = [
            {
                'id': 1,
                'title': 'Technology News',
                'text': 'Latest advances in artificial intelligence and machine learning are transforming industries. New deep learning models show promise in medical diagnostics and autonomous systems.'
            },
            {
                'id': 2,
                'title': 'Sports Report',
                'text': 'The championship game was exciting with amazing performances from both teams. The final score was 3-2 after an intense match with spectacular goals.'
            },
            {
                'id': 3,
                'title': 'Weather Update',
                'text': 'Today will be sunny with mild temperatures around 22 degrees. Perfect weather for outdoor activities and recreation in the park.'
            },
            {
                'id': 4,
                'title': 'Business Article',
                'text': 'Stock markets reached new highs today as investors showed confidence in economic growth. Major indices gained over 2% in trading activity.'
            },
            {
                'id': 5,
                'title': 'Travel Blog',
                'text': 'Exploring exotic destinations offers unique cultural experiences. The local cuisine and friendly residents made the experience memorable and enriching.'
            },
            {
                'id': 6,
                'title': 'Education Update',
                'text': 'Educational institutions are adopting new teaching methods to improve student engagement. Technology integration is showing positive results in learning outcomes.'
            }
        ]
        
        logger.info(f"Sample texts retrieved by {session['username']}")
        return jsonify({'samples': samples})
    except Exception as e:
        logger.error(f"Error retrieving samples: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """System health check"""
    return jsonify({
        'status': 'healthy' if classifier is not None else 'classifier_not_loaded',
        'timestamp': datetime.now().isoformat(),
        'classifier_loaded': classifier is not None,
        'database_connected': True,
        'version': '1.0.0'
    })

# ================================================================================
# ERROR HANDLERS
# ================================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found', 'status': 404}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    logger.error(f"Server error: {str(error)}")
    return jsonify({'error': 'Internal server error', 'status': 500}), 500


@app.errorhandler(403)
def forbidden(error):
    """Handle 403 errors"""
    return jsonify({'error': 'Forbidden', 'status': 403}), 403


@app.errorhandler(401)
def unauthorized(error):
    """Handle 401 errors"""
    return jsonify({'error': 'Unauthorized', 'status': 401}), 401

# ================================================================================
# APPLICATION STARTUP
# ================================================================================

if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("THREAT DETECTION HUB - BACKEND APPLICATION")
    print("=" * 70)
    print(f"Status: Starting...")
    print(f"Classifier Loaded: {'✓ Yes' if classifier is not None else '✗ No'}")
    print(f"Database Connected: ✓ Yes")
    print(f"Authentication: ✓ Enabled")
    print(f"Flask Environment: Development")
    print(f"Debug Mode: Disabled")
    print("\nTo train the model, run: python -m src.train_pipeline")
    print("To access the application, navigate to: http://localhost:5000")
    print(f"Login with: admin / admin123")
    print("=" * 70 + "\n")
    
    try:
        app.run(debug=False, host='0.0.0.0', port=5000, threaded=True)
    except Exception as e:
        logger.error(f"Fatal error starting application: {str(e)}")
        print(f"ERROR: {str(e)}")
