import schedule
import time
from src.data_collector import WebDataCollector
from src.classifier import ContentClassifier
from src.alert_system import AlertSystem
from src.database import DatabaseManager
import logging
import os

class AutomatedMonitor:
    def __init__(self):
        """Initialize automated monitoring system"""
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        logging.basicConfig(
            filename='logs/monitor.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        self.collector = WebDataCollector()
        self.classifier = ContentClassifier()
        self.alert_system = AlertSystem()
        self.db = DatabaseManager('json')
        
        # List of URLs to monitor
        self.monitored_urls = [
            # Example URLs - add your actual URLs here
            # 'https://example-news-site.com',
            # 'https://example-forum.com',
        ]
        
        logging.info("AutomatedMonitor initialized")
    
    def monitor_websites(self):
        """Monitor configured websites"""
        logging.info("Starting website monitoring cycle")
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting website monitoring cycle")
        
        if not self.monitored_urls:
            logging.warning("No URLs configured for monitoring")
            print("No URLs configured for monitoring")
            return
        
        for url in self.monitored_urls:
            try:
                print(f"  Monitoring: {url}")
                logging.info(f"Monitoring URL: {url}")
                
                # Collect data
                data = self.collector.scrape_website(url)
                
                if data:
                    # Classify content
                    result = self.classifier.predict(data['content'])
                    
                    # Store in database
                    data['analysis'] = result
                    self.db.insert_content(data)
                    
                    # Check for alerts
                    if self.alert_system.should_alert(result):
                        alert = self.alert_system.generate_alert(result, data)
                        self.alert_system.send_email_alert(alert)
                        self.alert_system.save_alert(alert)
                        logging.warning(f"ALERT: {url} - {result['prediction']}")
                    
                    logging.info(f"Processed {url}: {result['prediction']}")
                    print(f"    Result: {result['prediction']} ({result['confidence']:.2%} confidence)")
                
                # Rate limiting
                time.sleep(2)
                
            except Exception as e:
                logging.error(f"Error monitoring {url}: {str(e)}")
                print(f"  Error monitoring {url}: {str(e)}")
        
        logging.info("Website monitoring cycle completed")
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Website monitoring cycle completed\n")
    
    def add_url(self, url):
        """Add URL to monitoring list"""
        if url not in self.monitored_urls:
            self.monitored_urls.append(url)
            logging.info(f"Added URL to monitoring: {url}")
            print(f"Added URL to monitoring: {url}")
    
    def remove_url(self, url):
        """Remove URL from monitoring list"""
        if url in self.monitored_urls:
            self.monitored_urls.remove(url)
            logging.info(f"Removed URL from monitoring: {url}")
            print(f"Removed URL from monitoring: {url}")
    
    def run(self):
        """Start scheduled monitoring"""
        # Schedule monitoring every 6 hours
        schedule.every(6).hours.do(self.monitor_websites)
        
        # Alternative: run every 30 minutes for testing
        # schedule.every(30).minutes.do(self.monitor_websites)
        
        # Run immediately on start
        self.monitor_websites()
        
        logging.info("Automated monitoring started")
        print("Automated monitoring started. Press Ctrl+C to stop.")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            logging.info("Automated monitoring stopped")
            print("\nAutomated monitoring stopped.")


if __name__ == '__main__':
    print("Starting Automated Website Monitor...")
    print("="*60)
    
    monitor = AutomatedMonitor()
    
    # Example: Add URLs to monitor
    # monitor.add_url('https://example.com')
    
    monitor.run()
