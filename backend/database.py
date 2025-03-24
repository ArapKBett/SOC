from pymongo import MongoClient

# Initialize MongoDB client and database
client = MongoClient('mongodb://localhost:27017/')  # Replace localhost if connecting to a remote database
db = client['cyber_threat_dashboard']  # Database name

# Collections for storing threat data and alerts
threats_collection = db['threats']
alerts_collection = db['alerts']

# Example function to insert data into MongoDB
def insert_threat(threat):
    threats_collection.insert_one(threat)

# Example function to fetch all threats
def fetch_threats():
    return list(threats_collection.find({}, {'_id': 0}))  # Exclude the MongoDB ObjectID field

# Example function to fetch all alerts
def fetch_alerts():
    return list(alerts_collection.find({}, {'_id': 0}))
