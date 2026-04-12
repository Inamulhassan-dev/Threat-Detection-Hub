import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
import logging
import os

class WebDataCollector:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
        logging.basicConfig(filename='logs/scraper.log', level=logging.INFO)
    
    def scrape_website(self, url):
        """Scrape text content from a website"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract text
            text = soup.get_text(separator=' ', strip=True)
            
            # Extract metadata
            data = {
                'url': url,
                'title': soup.title.string if soup.title else '',
                'content': text,
                'timestamp': datetime.now().isoformat(),
                'links': [a.get('href') for a in soup.find_all('a', href=True)]
            }
            
            logging.info(f"Successfully scraped: {url}")
            return data
        
        except Exception as e:
            logging.error(f"Error scraping {url}: {str(e)}")
            return None
    
    def scrape_twitter_simulation(self, keywords):
        """Simulated Twitter data collection (use Twitter API in production)"""
        # In production, use tweepy library with Twitter API
        sample_tweets = [
            {
                'text': 'Sample tweet for testing purposes',
                'user': 'user123',
                'timestamp': datetime.now().isoformat(),
                'hashtags': ['#test'],
                'retweets': 10,
                'likes': 25
            }
        ]
        return sample_tweets
    
    def save_data(self, data, filename):
        """Save collected data to JSON"""
        if not os.path.exists('data'):
            os.makedirs('data')
        with open(f'data/{filename}', 'a') as f:
            json.dump(data, f)
            f.write('\n')


if __name__ == '__main__':
    collector = WebDataCollector()
    print("WebDataCollector initialized successfully")
