import React, { useState, useEffect } from 'react';
import './styles.css';

function AlertSystem() {
    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        fetch('/alerts')
            .then(response => response.json())
            .then(data => setAlerts(data.alerts))
            .catch(error => console.error(error));
    }, []);

    return (
        <div className="container">
            <h1>Alert System</h1>
            <ul>
                {alerts.map(alert => (
                    <li key={alert.id}>{alert.type} - {alert.timestamp}</li>
                ))}
            </ul>
        </div>
    );
}

export default AlertSystem;