from flask import Flask
from api.threats import get_threat_data
from api.alerts import get_alerts

app = Flask(__name__)

@app.route('/threats', methods=['GET'])
def threats():
    return get_threat_data()

@app.route('/alerts', methods=['GET'])
def alerts():
    return get_alerts()

if __name__ == '__main__':
    app.run(debug=True)
