import joblib
from src.text_processor import TextPreprocessor
from src.feature_extractor import FeatureExtractor
import logging
import os

# Always resolve paths relative to this file's location (backend/)
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_MODELS_DIR = os.path.join(os.path.dirname(_BASE_DIR), 'models')

class ContentClassifier:
    def __init__(self,
                 model_path=None,
                 tfidf_path=None):
        """Initialize content classifier"""
        if model_path is None:
            model_path = os.path.join(_MODELS_DIR, 'best_terrorism_detector.pkl')
        if tfidf_path is None:
            tfidf_path = os.path.join(_MODELS_DIR, 'tfidf_vectorizer.pkl')

        logs_dir = os.path.join(os.path.dirname(_BASE_DIR), 'logs')
        os.makedirs(logs_dir, exist_ok=True)
        
        logging.getLogger(__name__).setLevel(logging.INFO)
        
        try:
            self.model = joblib.load(model_path)
            logging.info(f"Model loaded from {model_path}")
        except Exception as e:
            logging.error(f"Error loading model from {model_path}: {str(e)}")
            self.model = None
        
        try:
            self.tfidf = joblib.load(tfidf_path)
            logging.info(f"TF-IDF vectorizer loaded from {tfidf_path}")
        except Exception as e:
            logging.error(f"Error loading TF-IDF vectorizer from {tfidf_path}: {str(e)}")
            self.tfidf = None
        
        self.preprocessor = TextPreprocessor()
        self.feature_extractor = FeatureExtractor()
        
        self.labels = {
            0: 'Normal',
            1: 'Suspicious',
            2: 'Terrorist-Related'
        }
    
    def predict(self, text):
        """Predict if content is terrorist-related"""
        try:
            if self.model is None or self.tfidf is None:
                return {
                    'prediction': 'Error - Model not loaded',
                    'prediction_code': -1,
                    'confidence': 0.0,
                    'probabilities': {
                        'normal': 0.0,
                        'suspicious': 0.0,
                        'terrorist': 0.0
                    },
                    'sentiment': {'polarity': 0.0, 'subjectivity': 0.0},
                    'keyword_score': 0.0,
                    'text_preview': text[:200],
                    'error': 'Model not initialized'
                }
            
            # Preprocess
            processed_text, tokens = self.preprocessor.preprocess_pipeline(text)
            
            # Extract features
            features = self.tfidf.transform([processed_text])
            
            # Predict
            prediction = self.model.predict(features)[0]
            
            # Get probabilities
            try:
                probability = self.model.predict_proba(features)[0]
            except:
                # Some models don't have predict_proba
                probability = [0.0, 0.0, 0.0]
                probability[int(prediction)] = 1.0
            
            # Extract additional features
            sentiment = self.feature_extractor.extract_sentiment(text)
            keyword_score = self.feature_extractor.keyword_matching_score(text)
            
            result = {
                'prediction': self.labels.get(int(prediction), 'Unknown'),
                'prediction_code': int(prediction),
                'confidence': float(max(probability)),
                'probabilities': {
                    'normal': float(probability[0]) if len(probability) > 0 else 0.0,
                    'suspicious': float(probability[1]) if len(probability) > 1 else 0.0,
                    'terrorist': float(probability[2]) if len(probability) > 2 else 0.0
                },
                'sentiment': sentiment,
                'keyword_score': float(keyword_score),
                'text_preview': text[:200]
            }
            
            logging.info(f"Prediction: {result['prediction']}, Confidence: {result['confidence']:.4f}")
            return result
            
        except Exception as e:
            logging.error(f"Error in prediction: {str(e)}")
            return {
                'prediction': 'Error',
                'prediction_code': -1,
                'confidence': 0.0,
                'probabilities': {
                    'normal': 0.0,
                    'suspicious': 0.0,
                    'terrorist': 0.0
                },
                'sentiment': {'polarity': 0.0, 'subjectivity': 0.0},
                'keyword_score': 0.0,
                'text_preview': text[:200],
                'error': str(e)
            }


if __name__ == '__main__':
    classifier = ContentClassifier()
    sample_texts = [
        "This is a normal tweet about the weather",
        "Join our violent extremist group for jihad",
        "Having a great day at the park"
    ]
    
    for text in sample_texts:
        result = classifier.predict(text)
        print(f"Text: {text[:50]}...")
        print(f"Prediction: {result['prediction']}")
        print(f"Confidence: {result['confidence']:.4f}\n")
