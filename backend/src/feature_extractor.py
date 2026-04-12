from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from textblob import TextBlob
import numpy as np
import logging
import os

class FeatureExtractor:
    def __init__(self):
        """Initialize feature extractor"""
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        logging.basicConfig(
            filename='logs/feature_extractor.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        self.tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 3))
        self.count_vectorizer = CountVectorizer(max_features=1000)
        
        # Terrorism-related keywords (sample list)
        self.terrorist_keywords = [
            'attack', 'bomb', 'jihad', 'extremist', 'radical', 
            'terrorism', 'militant', 'weapon', 'threat', 'violence',
            'isis', 'al-qaeda', 'taliban', 'recruit', 'propaganda',
            'kill', 'destroy', 'war', 'explosive', 'target'
        ]
    
    def extract_tfidf_features(self, texts):
        """Extract TF-IDF features"""
        try:
            return self.tfidf.fit_transform(texts)
        except Exception as e:
            logging.error(f"Error extracting TF-IDF features: {str(e)}")
            return None
    
    def extract_sentiment(self, text):
        """Extract sentiment polarity and subjectivity"""
        try:
            blob = TextBlob(text)
            return {
                'polarity': float(blob.sentiment.polarity),
                'subjectivity': float(blob.sentiment.subjectivity)
            }
        except Exception as e:
            logging.error(f"Error extracting sentiment: {str(e)}")
            return {'polarity': 0.0, 'subjectivity': 0.0}
    
    def keyword_matching_score(self, text):
        """Calculate terrorism keyword matching score"""
        try:
            text_lower = text.lower()
            matches = sum(1 for keyword in self.terrorist_keywords if keyword in text_lower)
            return float(matches) / len(self.terrorist_keywords)
        except Exception as e:
            logging.error(f"Error calculating keyword score: {str(e)}")
            return 0.0
    
    def extract_statistical_features(self, text):
        """Extract statistical text features"""
        try:
            words = text.split()
            word_lengths = [len(word) for word in words] if words else [0]
            
            return {
                'word_count': len(words),
                'char_count': len(text),
                'avg_word_length': float(np.mean(word_lengths)),
                'uppercase_ratio': float(sum(1 for c in text if c.isupper()) / len(text)) if text else 0.0,
                'exclamation_count': text.count('!'),
                'question_count': text.count('?'),
                'digit_count': sum(1 for c in text if c.isdigit())
            }
        except Exception as e:
            logging.error(f"Error extracting statistical features: {str(e)}")
            return {
                'word_count': 0,
                'char_count': 0,
                'avg_word_length': 0.0,
                'uppercase_ratio': 0.0,
                'exclamation_count': 0,
                'question_count': 0,
                'digit_count': 0
            }
    
    def combine_features(self, text, preprocessed_text=None):
        """Combine all features"""
        try:
            features = {}
            
            # Sentiment features
            features.update(self.extract_sentiment(text))
            
            # Keyword matching
            features['keyword_score'] = self.keyword_matching_score(text)
            
            # Statistical features
            features.update(self.extract_statistical_features(text))
            
            return features
        except Exception as e:
            logging.error(f"Error combining features: {str(e)}")
            return {}


if __name__ == '__main__':
    extractor = FeatureExtractor()
    sample_text = "Attack bombs jihad extremist violent terrorism"
    features = extractor.combine_features(sample_text)
    print(f"Extracted features: {features}")
