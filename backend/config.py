from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

class Config:
    # MongoDB Configuration
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'cyber_threat_dashboard')

    # External API Keys
    VIRUSTOTAL_API_KEY = os.getenv('VIRUSTOTAL_API_KEY', 'your_virustotal_api_key_here')
    SHODAN_API_KEY = os.getenv('SHODAN_API_KEY', 'your_shodan_api_key_here')

    # Other Configurations
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
