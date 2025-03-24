from database import fetch_threats
from config import Config
import requests

def get_threat_data():
    try:
        # Fetch data from MongoDB
        threats = fetch_threats()

        # Optionally, fetch and merge external threat data from VirusTotal
        headers = {"x-apikey": Config.VIRUSTOTAL_API_KEY}
        response = requests.get("https://api.virustotal.com/v3/intelligence", headers=headers)
        if response.status_code == 200:
            external_data = response.json()
            threats.extend(external_data.get('data', []))
        
        return {"threats": threats}
    except Exception as e:
        return {"error": str(e)}
