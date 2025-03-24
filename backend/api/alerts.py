from database import fetch_alerts

def get_alerts():
    try:
        # Fetch data from the MongoDB alerts collection
        alert_data = fetch_alerts()
        return {"alerts": alert_data}
    except Exception as e:
        return {"error": str(e)}
