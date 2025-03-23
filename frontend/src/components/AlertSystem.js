import React, { useState, useEffect } from 'react';

function AlertSystem() {
    const [alerts, setAlerts] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/alerts') // Fetch data from the backend API
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                setAlerts(data.alerts); // Set the state with fetched alerts
            })
            .catch(err => {
                setError(err.message); // Handle errors gracefully
            });
    }, []);

    return (
        <div className="container">
            <h1>Alert System</h1>
            {error ? (
                <p>Error: {error}</p> // Display error message if an error occurs
            ) : (
                <ul>
                    {alerts.map(alert => (
                        <li key={alert.id}>
                            {alert.type} - {alert.timestamp}
                        </li>
                    ))}
                </ul> // Render a list of fetched alerts
            )}
        </div>
    );
}

export default AlertSystem;