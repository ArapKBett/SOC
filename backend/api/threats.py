import requests

def get_threat_data():
    api_key = "your_api_key"
    url = "https://api.virustotal.com/v3/intelligence"
    response = requests.get(url, headers={"x-apikey": api_key})
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch threat data"}