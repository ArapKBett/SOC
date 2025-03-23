def get_alerts():
    alerts = [
        {"id": 1, "type": "Malicious IP detected", "timestamp": "2025-03-23T14:00:00"},
        {"id": 2, "type": "Phishing site reported", "timestamp": "2025-03-23T14:30:00"}
    ]
    return {"alerts": alerts}