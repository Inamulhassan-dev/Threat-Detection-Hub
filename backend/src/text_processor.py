import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import logging
import os

# Download required NLTK data automatically
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords', quiet=True)

try:
    from nltk.tokenize import word_tokenize
    word_tokenize("test")
except LookupError:
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)

try:
    from nltk.stem import WordNetLemmatizer
    WordNetLemmatizer().lemmatize("test")
except LookupError:
    nltk.download('wordnet', quiet=True)

# Try to load spaCy model
try:
    import spacy
    try:
        nlp = spacy.load('en_core_web_sm')
    except OSError:
        print("spaCy model not found. Install with: python -m spacy download en_core_web_sm")
        nlp = None
except ImportError:
    nlp = None

class TextPreprocessor:
    def __init__(self):
        """Initialize text preprocessor with NLTK and spaCy models"""
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        logging.basicConfig(
            filename='logs/preprocessor.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.nlp = nlp
    
    def clean_text(self, text):
        """Clean and normalize text"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def tokenize(self, text):
        """Tokenize text"""
        try:
            return word_tokenize(text)
        except Exception as e:
            logging.error(f"Error tokenizing text: {str(e)}")
            return text.split()
    
    def remove_stopwords(self, tokens):
        """Remove stopwords"""
        return [word for word in tokens if word not in self.stop_words]
    
    def lemmatize(self, tokens):
        """Lemmatize tokens"""
        try:
            return [self.lemmatizer.lemmatize(word) for word in tokens]
        except Exception as e:
            logging.error(f"Error lemmatizing: {str(e)}")
            return tokens
    
    def extract_features(self, text):
        """Extract NLP features using spaCy"""
        features = {
            'entities': [],
            'noun_phrases': [],
            'pos_tags': [],
            'keywords': []
        }
        
        if self.nlp is None:
            return features
        
        try:
            doc = self.nlp(text)
            
            features = {
                'entities': [(ent.text, ent.label_) for ent in doc.ents],
                'noun_phrases': [chunk.text for chunk in doc.noun_chunks],
                'pos_tags': [(token.text, token.pos_) for token in doc],
                'keywords': self.extract_keywords(doc)
            }
        except Exception as e:
            logging.error(f"Error extracting features: {str(e)}")
        
        return features
    
    def extract_keywords(self, doc, top_n=10):
        """Extract important keywords"""
        # Calculate word frequency
        word_freq = {}
        for token in doc:
            if not token.is_stop and not token.is_punct and token.pos_ in ['NOUN', 'VERB', 'ADJ']:
                word_freq[token.text] = word_freq.get(token.text, 0) + 1
        
        # Sort by frequency
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, freq in sorted_words[:top_n]]
    
    def preprocess_pipeline(self, text):
        """Complete preprocessing pipeline"""
        try:
            # Clean text
            cleaned = self.clean_text(text)
            
            # Tokenize
            tokens = self.tokenize(cleaned)
            
            # Remove stopwords
            tokens = self.remove_stopwords(tokens)
            
            # Lemmatize
            tokens = self.lemmatize(tokens)
            
            return ' '.join(tokens), tokens
        except Exception as e:
            logging.error(f"Error in preprocessing pipeline: {str(e)}")
            return text, text.split()


if __name__ == '__main__':
    preprocessor = TextPreprocessor()
    sample_text = "This is a sample text about terrorism and violent extremism attacks!"
    cleaned, tokens = preprocessor.preprocess_pipeline(sample_text)
    print(f"Original: {sample_text}")
    print(f"Cleaned: {cleaned}")
    print(f"Tokens: {tokens}")
