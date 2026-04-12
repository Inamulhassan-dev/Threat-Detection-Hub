import json
from datetime import datetime
import os
import logging
import hashlib
import secrets

# Always resolve paths relative to backend/ regardless of where Python is launched from
_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
_BACKEND_DIR = os.path.dirname(_SRC_DIR)
_DATA_DIR = os.path.join(_BACKEND_DIR, 'data')
_LOGS_DIR = os.path.join(_BACKEND_DIR, 'logs')


class DatabaseManager:
    def __init__(self, db_type='json'):
        """
        Initialize database manager.
        db_type: 'json' (default), 'mongodb', or 'mysql'
        """
        self.db_type = db_type

        os.makedirs(_DATA_DIR, exist_ok=True)
        os.makedirs(_LOGS_DIR, exist_ok=True)

        # Use module-level logger — don't call basicConfig here (app.py owns it)
        self.logger = logging.getLogger(__name__)

        if db_type == 'json':
            self.data_file = os.path.join(_DATA_DIR, 'web_content.json')
            if not os.path.exists(self.data_file):
                with open(self.data_file, 'w') as f:
                    json.dump([], f)

        elif db_type == 'mongodb':
            try:
                import pymongo
                self.client = pymongo.MongoClient('mongodb://localhost:27017/')
                self.db_conn = self.client['terrorism_detection']
                self.collection = self.db_conn['web_content']
            except Exception as e:
                self.logger.error(f"MongoDB connection failed: {str(e)}")

        elif db_type == 'mysql':
            try:
                import mysql.connector
                self.conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='your_password',
                    database='terrorism_detection'
                )
                self.cursor = self.conn.cursor()
            except Exception as e:
                self.logger.error(f"MySQL connection failed: {str(e)}")

    # ------------------------------------------------------------------ #
    # Content Methods
    # ------------------------------------------------------------------ #

    def insert_content(self, data):
        """Insert analysed content record into database"""
        try:
            if self.db_type == 'json':
                with open(self.data_file, 'r') as f:
                    records = json.load(f)
                records.append(data)
                with open(self.data_file, 'w') as f:
                    json.dump(records, f, indent=2)
            elif self.db_type == 'mongodb':
                self.collection.insert_one(data)
        except Exception as e:
            self.logger.error(f"Error inserting content: {str(e)}")

    def get_all_content(self):
        """Retrieve all content records"""
        try:
            if self.db_type == 'json':
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            elif self.db_type == 'mongodb':
                return list(self.collection.find())
        except Exception as e:
            self.logger.error(f"Error retrieving content: {str(e)}")
            return []

    def get_all_contents(self):
        """Alias for get_all_content"""
        return self.get_all_content()

    def get_unprocessed_content(self):
        """Retrieve content not yet analysed"""
        try:
            if self.db_type == 'json':
                with open(self.data_file, 'r') as f:
                    records = json.load(f)
                return [r for r in records if not r.get('analyzed', False)]
            elif self.db_type == 'mongodb':
                return list(self.collection.find({'analyzed': {'$ne': True}}))
        except Exception as e:
            self.logger.error(f"Error retrieving unprocessed content: {str(e)}")
            return []

    # ------------------------------------------------------------------ #
    # User Authentication Methods
    # ------------------------------------------------------------------ #

    def _users_file(self):
        """Return absolute path to users.json, creating it with default admin if missing"""
        path = os.path.join(_DATA_DIR, 'users.json')
        if not os.path.exists(path):
            default_admin = {
                'username': 'admin',
                'email': 'admin@threatdetection.local',
                'password_hash': self._hash_password('admin123'),
                'role': 'Admin',
                'created_at': datetime.now().isoformat(),
                'last_login': None,
                'is_active': True
            }
            with open(path, 'w') as f:
                json.dump([default_admin], f, indent=2)
            self.logger.info("Created default admin user")
        return path

    def _hash_password(self, password):
        """Hash password with PBKDF2-SHA256 and a random salt"""
        salt = secrets.token_hex(16)
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
        return f"{salt}${pwd_hash.hex()}"

    def _verify_password(self, password, password_hash):
        """Verify a plaintext password against a stored hash"""
        try:
            salt, stored_hash = password_hash.split('$', 1)
            new_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
            return new_hash.hex() == stored_hash
        except Exception as e:
            self.logger.error(f"Password verification error: {str(e)}")
            return False

    def create_user(self, username, email, password, role='Viewer'):
        """Create a new user account"""
        try:
            users_file = self._users_file()
            with open(users_file, 'r') as f:
                users = json.load(f)

            if any(u['username'] == username for u in users):
                return {'success': False, 'message': 'Username already exists'}
            if any(u['email'] == email for u in users):
                return {'success': False, 'message': 'Email already registered'}
            if role not in ['Admin', 'Analyst', 'Viewer']:
                role = 'Viewer'

            new_user = {
                'username': username,
                'email': email,
                'password_hash': self._hash_password(password),
                'role': role,
                'created_at': datetime.now().isoformat(),
                'last_login': None,
                'is_active': True
            }
            users.append(new_user)
            with open(users_file, 'w') as f:
                json.dump(users, f, indent=2)

            self.logger.info(f"Created user: {username} ({role})")
            return {'success': True, 'message': 'User created successfully', 'user': username}

        except Exception as e:
            self.logger.error(f"Error creating user: {str(e)}")
            return {'success': False, 'message': f'Error: {str(e)}'}

    def authenticate_user(self, username, password):
        """Authenticate user credentials"""
        try:
            users_file = self._users_file()
            with open(users_file, 'r') as f:
                users = json.load(f)

            user = next((u for u in users if u['username'] == username), None)
            if not user:
                return {'success': False, 'message': 'User not found'}
            if not user.get('is_active', True):
                return {'success': False, 'message': 'Account is inactive'}
            if not self._verify_password(password, user['password_hash']):
                return {'success': False, 'message': 'Invalid password'}

            user['last_login'] = datetime.now().isoformat()
            with open(users_file, 'w') as f:
                json.dump(users, f, indent=2)

            self.logger.info(f"User authenticated: {username}")
            return {
                'success': True,
                'message': 'Authentication successful',
                'user': {
                    'username': user['username'],
                    'email': user['email'],
                    'role': user['role'],
                    'created_at': user['created_at']
                }
            }
        except Exception as e:
            self.logger.error(f"Authentication error: {str(e)}")
            return {'success': False, 'message': f'Error: {str(e)}'}

    def get_user(self, username):
        """Get user info by username"""
        try:
            users_file = self._users_file()
            with open(users_file, 'r') as f:
                users = json.load(f)
            user = next((u for u in users if u['username'] == username), None)
            if user:
                return {
                    'username': user['username'],
                    'email': user['email'],
                    'role': user['role'],
                    'created_at': user['created_at'],
                    'last_login': user.get('last_login'),
                    'is_active': user.get('is_active', True)
                }
            return None
        except Exception as e:
            self.logger.error(f"Error getting user: {str(e)}")
            return None

    def update_password(self, username, old_password, new_password):
        """Update a user's password"""
        try:
            users_file = self._users_file()
            with open(users_file, 'r') as f:
                users = json.load(f)
            user = next((u for u in users if u['username'] == username), None)
            if not user:
                return {'success': False, 'message': 'User not found'}
            if not self._verify_password(old_password, user['password_hash']):
                return {'success': False, 'message': 'Current password is incorrect'}
            user['password_hash'] = self._hash_password(new_password)
            with open(users_file, 'w') as f:
                json.dump(users, f, indent=2)
            self.logger.info(f"Password updated for: {username}")
            return {'success': True, 'message': 'Password updated successfully'}
        except Exception as e:
            self.logger.error(f"Error updating password: {str(e)}")
            return {'success': False, 'message': f'Error: {str(e)}'}

    def list_users(self):
        """List all users (Admin only)"""
        try:
            users_file = self._users_file()
            with open(users_file, 'r') as f:
                users = json.load(f)
            return [{
                'username': u['username'],
                'email': u['email'],
                'role': u['role'],
                'created_at': u['created_at'],
                'is_active': u.get('is_active', True)
            } for u in users]
        except Exception as e:
            self.logger.error(f"Error listing users: {str(e)}")
            return []


if __name__ == '__main__':
    db = DatabaseManager('json')
    print("DatabaseManager initialized successfully")
