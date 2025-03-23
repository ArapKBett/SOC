# backend/api/visualization.py

import json

def format_data_for_visualization(data):
    """
    Process and format data for creating visualizations.
    Args:
        data (dict): Raw data from API responses or database.
    Returns:
        str: JSON string ready to be consumed by the frontend.
    """
    # Example processing
    formatted_data = {
        "labels": ["Malware", "Phishing", "Ransomware"],
        "values": [20, 30, 10]  # Example data distribution
    }
    return json.dumps(formatted_data)