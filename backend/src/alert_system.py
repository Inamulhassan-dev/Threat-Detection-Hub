import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json
import logging
import os

class AlertSystem:
    def __init__(self, alert_threshold=0.7):
        """Initialize alert system"""
        if not os.path.exists('logs'):
            os.makedirs('logs')
        if not os.path.exists('data'):
            os.makedirs('data')
        
        logging.basicConfig(
            filename='logs/alerts.log',
            level=logging.WARNING,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        self.alert_threshold = alert_threshold
        self.email_config = {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'sender_email': 'your_email@gmail.com',
            'sender_password': 'your_app_password',
            'recipient_emails': ['security@agency.gov']
        }
    
    def should_alert(self, prediction_result):
        """Determine if alert should be triggered"""
        try:
            if prediction_result.get('prediction_code') == 2:  # Terrorist-related
                return True
            elif prediction_result.get('prediction_code') == 1 and \
                 prediction_result.get('confidence', 0) > self.alert_threshold:
                return True
            return False
        except Exception as e:
            logging.error(f"Error in should_alert: {str(e)}")
            return False
    
    def generate_alert(self, prediction_result, source_data):
        """Generate alert message"""
        try:
            alert = {
                'timestamp': datetime.now().isoformat(),
                'alert_level': 'HIGH' if prediction_result['prediction_code'] == 2 else 'MEDIUM',
                'prediction': prediction_result,
                'source': source_data,
                'action_required': 'Immediate review and investigation'
            }
            
            # Log alert
            logging.warning(f"ALERT GENERATED: {json.dumps(alert, indent=2)}")
            
            return alert
        except Exception as e:
            logging.error(f"Error generating alert: {str(e)}")
            return None
    
    def send_email_alert(self, alert):
        """Send email notification (configured for local use - requires setup)"""
        try:
            # This is a template. In production, configure with actual email credentials
            logging.info(f"Email alert would be sent for: {alert['timestamp']}")
            
            # Uncomment below for actual email sending when configured
            """
            msg = MIMEMultipart()
            msg['From'] = self.email_config['sender_email']
            msg['To'] = ', '.join(self.email_config['recipient_emails'])
            msg['Subject'] = f"[{alert['alert_level']}] Terrorist Content Detected"
            
            body = f'''
            SECURITY ALERT
            
            Alert Level: {alert['alert_level']}
            Timestamp: {alert['timestamp']}
            
            Prediction: {alert['prediction']['prediction']}
            Confidence: {alert['prediction']['confidence']:.2%}
            
            Source URL: {alert['source'].get('url', 'N/A')}
            
            Text Preview:
            {alert['prediction']['text_preview']}
            
            Action Required: {alert['action_required']}
            
            Full details in system logs.
            '''
            
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(
                self.email_config['smtp_server'],
                self.email_config['smtp_port']
            )
            server.starttls()
            server.login(
                self.email_config['sender_email'],
                self.email_config['sender_password']
            )
            
            server.send_message(msg)
            server.quit()
            
            logging.info(f"Email alert sent successfully for alert: {alert['timestamp']}")
            """
            
        except Exception as e:
            logging.error(f"Failed to send email alert: {str(e)}")
    
    def save_alert(self, alert):
        """Save alert to database"""
        try:
            alert_file = 'data/alerts.json'
            
            # Load existing alerts
            alerts = []
            if os.path.exists(alert_file):
                try:
                    with open(alert_file, 'r') as f:
                        for line in f:
                            try:
                                alerts.append(json.loads(line))
                            except:
                                pass
                except:
                    alerts = []
            
            # Append new alert
            alerts.append(alert)
            
            # Save all alerts
            with open(alert_file, 'w') as f:
                for a in alerts:
                    json.dump(a, f)
                    f.write('\n')
            
            logging.info(f"Alert saved to {alert_file}")
            
        except Exception as e:
            logging.error(f"Error saving alert: {str(e)}")
    
    def get_recent_alerts(self, limit=50):
        """Retrieve recent alerts"""
        try:
            alerts = []
            alert_file = 'data/alerts.json'
            
            if os.path.exists(alert_file):
                with open(alert_file, 'r') as f:
                    for line in f:
                        try:
                            alerts.append(json.loads(line))
                        except:
                            pass
            
            return alerts[-limit:]
        except Exception as e:
            logging.error(f"Error retrieving alerts: {str(e)}")
            return []


if __name__ == '__main__':
    alert_system = AlertSystem()
    print("AlertSystem initialized successfully")
