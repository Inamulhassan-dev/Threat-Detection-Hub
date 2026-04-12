from src.text_processor import TextPreprocessor
from src.feature_extractor import FeatureExtractor
from src.model_trainer import TerrorismDetectionModel
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import joblib
import os
import logging

# Always resolve to backend/ directory
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_BACKEND_DIR = os.path.dirname(_BASE_DIR)
_DATA_DIR = os.path.join(_BACKEND_DIR, 'data')
_MODELS_DIR = os.path.join(_BACKEND_DIR, 'models')

class TrainingPipeline:
    def __init__(self):
        """Initialize training pipeline"""
        self.preprocessor = TextPreprocessor()
        self.feature_extractor = FeatureExtractor()
        self.model_trainer = TerrorismDetectionModel()
        
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        logging.basicConfig(
            filename='logs/training_pipeline.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def create_sample_dataset(self):
        """Create sample training dataset"""
        data = {
            'text': [
                'This is normal social media post about daily life',
                'Join our peaceful community event tomorrow',
                'Beautiful sunset at the beach today',
                'Had a great time with friends at the park',
                'Weather is nice this week',
                'New restaurant opening in downtown',
                'Discussion about controversial political views',
                'Debate about government policies and reforms',
                'Online argument about religion and beliefs',
                'Strong political opinions about national issues',
                'Threatening violence and extremist propaganda',
                'Radical ideology and call for attacks',
                'Terrorist recruitment message with violent content',
                'Plans for bombing and violent extremism',
                'Join our militant group for jihad',
                'ISIS recruitment and violent propaganda'
            ],
            'label': [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
        }
        
        df = pd.DataFrame(data)
        os.makedirs(_DATA_DIR, exist_ok=True)
        csv_path = os.path.join(_DATA_DIR, 'training_data.csv')
        df.to_csv(csv_path, index=False)
        logging.info(f"Sample dataset created with {len(df)} records")
        print(f"Sample dataset created with {len(df)} records")
        return df
    
    def run_training(self):
        """Execute complete training pipeline"""
        try:
            csv_path = os.path.join(_DATA_DIR, 'training_data.csv')

            if not os.path.exists(csv_path):
                print("Creating sample dataset...")
                self.create_sample_dataset()
            
            print("Loading training data...")
            df = pd.read_csv(csv_path)
            logging.info(f"Loaded {len(df)} records from training data")
            
            # Preprocess texts
            print("Preprocessing texts...")
            processed_texts = []
            for idx, text in enumerate(df['text']):
                processed, _ = self.preprocessor.preprocess_pipeline(text)
                processed_texts.append(processed)
                if (idx + 1) % 5 == 0:
                    print(f"  Processed {idx + 1}/{len(df['text'])} texts")
            
            # Extract features
            print("Extracting TF-IDF features...")
            X = self.feature_extractor.extract_tfidf_features(processed_texts)
            y = df['label'].values
            
            # Save TF-IDF vectorizer for later use
            tfidf_path = os.path.join(_MODELS_DIR, 'tfidf_vectorizer.pkl')
            os.makedirs(_MODELS_DIR, exist_ok=True)
            joblib.dump(self.feature_extractor.tfidf, tfidf_path)
            logging.info(f"TF-IDF vectorizer saved: {tfidf_path}")
            print(f"TF-IDF vectorizer saved: {tfidf_path}")
            
            # Split data
            print("Splitting data...")
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
            logging.info(f"Train set: {X_train.shape}, Test set: {X_test.shape}")
            print(f"Train set: {X_train.shape}, Test set: {X_test.shape}")
            
            # Train models
            print("\nTraining models...")
            trained_models = self.model_trainer.train_models(X_train, y_train)
            
            # Evaluate and save best model
            best_accuracy = 0
            best_model_name = None
            
            print("\nEvaluating models...")
            for name, model in trained_models.items():
                print(f"\n{'='*50}")
                print(f"Evaluating {name}:")
                print(f"{'='*50}")
                accuracy = self.model_trainer.evaluate_model(model, X_test, y_test)
                
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    best_model_name = name
            
            # Save best model
            best_model = trained_models[best_model_name]
            self.model_trainer.save_model(best_model, 'best_terrorism_detector')
            
            print(f"\n{'='*50}")
            print(f"Best Model: {best_model_name}")
            print(f"Accuracy: {best_accuracy:.4f} ({best_accuracy*100:.2f}%)")
            print(f"{'='*50}")
            
            logging.info(f"Best Model: {best_model_name} with accuracy: {best_accuracy:.4f}")
            
            return best_model, best_accuracy
            
        except Exception as e:
            logging.error(f"Error in training pipeline: {str(e)}")
            print(f"Error: {str(e)}")
            return None, 0.0


if __name__ == '__main__':
    print("Starting Training Pipeline...")
    print("="*60)
    
    pipeline = TrainingPipeline()
    best_model, accuracy = pipeline.run_training()
    
    print("\nTraining Pipeline Completed!")
