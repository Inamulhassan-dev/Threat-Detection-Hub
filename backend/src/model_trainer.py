from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import pandas as pd
import numpy as np
import logging
import os

# Always resolve to backend/ directory
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_BACKEND_DIR = os.path.dirname(_BASE_DIR)

class TerrorismDetectionModel:
    def __init__(self):
        """Initialize model trainer"""
        os.makedirs(os.path.join(_BACKEND_DIR, 'logs'), exist_ok=True)
        os.makedirs(os.path.join(_BACKEND_DIR, 'models'), exist_ok=True)
        
        logging.basicConfig(
            filename='logs/model_trainer.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        self.models = {
            'random_forest': RandomForestClassifier(
                n_estimators=100,
                random_state=42,
                n_jobs=-1
            ),
            'naive_bayes': MultinomialNB(),
            'svm': SVC(kernel='rbf', probability=True, random_state=42)
        }
        self.best_model = None
        self.best_model_name = None
    
    def prepare_dataset(self, data_path):
        """Load and prepare dataset"""
        try:
            # Sample dataset structure
            # columns: ['text', 'label'] where label: 0=normal, 1=suspicious, 2=terrorist
            df = pd.read_csv(data_path)
            logging.info(f"Dataset loaded: {len(df)} records")
            return df['text'].values, df['label'].values
        except Exception as e:
            logging.error(f"Error preparing dataset: {str(e)}")
            return None, None
    
    def train_models(self, X_train, y_train):
        """Train multiple models"""
        results = {}
        
        try:
            for name, model in self.models.items():
                print(f"Training {name}...")
                logging.info(f"Training {name}...")
                model.fit(X_train, y_train)
                results[name] = model
                logging.info(f"Successfully trained {name}")
            
            return results
        except Exception as e:
            logging.error(f"Error training models: {str(e)}")
            return results
    
    def evaluate_model(self, model, X_test, y_test):
        """Evaluate model performance"""
        try:
            y_pred = model.predict(X_test)
            
            print("\nClassification Report:")
            print(classification_report(y_test, y_pred))
            
            print("\nConfusion Matrix:")
            print(confusion_matrix(y_test, y_pred))
            
            accuracy = accuracy_score(y_test, y_pred)
            print(f"\nAccuracy: {accuracy:.4f}")
            
            logging.info(f"Accuracy: {accuracy:.4f}")
            logging.info(f"Classification Report:\n{classification_report(y_test, y_pred)}")
            
            return accuracy
        except Exception as e:
            logging.error(f"Error evaluating model: {str(e)}")
            return 0.0
    
    def save_model(self, model, filename):
        """Save trained model"""
        try:
            model_path = os.path.join(_BACKEND_DIR, 'models', f'{filename}.pkl')
            joblib.dump(model, model_path)
            logging.info(f"Model saved: {model_path}")
            print(f"Model saved: {model_path}")
        except Exception as e:
            logging.error(f"Error saving model: {str(e)}")
    
    def load_model(self, filename):
        """Load trained model"""
        try:
            model_path = os.path.join(_BACKEND_DIR, 'models', f'{filename}.pkl')
            model = joblib.load(model_path)
            logging.info(f"Model loaded: {model_path}")
            return model
        except Exception as e:
            logging.error(f"Error loading model: {str(e)}")
            return None


if __name__ == '__main__':
    trainer = TerrorismDetectionModel()
    print("TerrorismDetectionModel initialized successfully")
