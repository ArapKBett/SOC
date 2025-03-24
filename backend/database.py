from pymongo import MongoClient
from config import Config

# Initialize MongoDB client and database
client = MongoClient(Config.MONGODB_URI)
db = client[Config.DATABASE_NAME]

# Collections for threats and alerts
threats_collection = db['threats']
alerts_collection = db['alerts']

# Utility Functions
def insert_threat(threat):
    threats_collection.insert_one(threat)

def insert_alert(alert):
    alerts_collection.insert_one(alert)

def fetch_threats():
    return list(threats_collection.find({}, {'_id': 0}))

def fetch_alerts():
    return list(alerts_collection.find({}, {'_id': 0}))
