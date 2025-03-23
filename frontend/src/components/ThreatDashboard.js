import React, { useState, useEffect } from 'react';

function ThreatDashboard() {
    const [data, setData] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/threats') // Fetch data from the backend API
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                setData(data); // Set the state with fetched data
            })
            .catch(err => {
                setError(err.message); // Handle errors gracefully
            });
    }, []);

    return (
        <div className="container">
            <h1>Threat Dashboard</h1>
            {error ? (
                <p>Error: {error}</p> // Display error message if an error occurs
            ) : (
                <pre>{JSON.stringify(data, null, 2)}</pre> // Display fetched data
            )}
        </div>
    );
}

export default ThreatDashboard;