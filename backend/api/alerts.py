from database import fetch_alerts

def get_alerts():
    try:
        # Fetch data from MongoDB
        alerts = fetch_alerts()
        return {"alerts": alerts}
    except Exception as e:
        return {"error": str(e)}
