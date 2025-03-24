from database import fetch_threats

def get_threat_data():
    try:
        # Fetch data from the MongoDB threats collection
        threat_data = fetch_threats()
        return {"threats": threat_data}
    except Exception as e:
        return {"error": str(e)}
