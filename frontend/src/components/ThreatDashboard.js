import React, { useState, useEffect } from 'react';
import './styles.css';

function ThreatDashboard() {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('/threats')
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div className="container">
            <h1>Threat Dashboard</h1>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );
}

export default ThreatDashboard;