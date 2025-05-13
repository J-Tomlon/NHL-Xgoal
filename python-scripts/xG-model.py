import pandas as pd  
import numpy as np   
import matplotlib.pyplot as plt  
import requests

# CONSTANTS
NHL_API_URL = "https://statsapi.web.nhl.com/api/v1"

def get_nhl_data(endpoint, params=None):
    """
    Fetch data from the NHL API
    
    Parameters:
    endpoint (str): The API endpoint to request
    params (dict): Optional query parameters
    
    Returns:
    dict: JSON response from the API
    """

    url = f"{NHL_API_URL}/{endpoint}"
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None


teams_data = get_nhl_data("teams")
print(f"Number of teams: {len(teams_data['teams'])}")
print("First team:", teams_data['teams'][0]['name'])




def main():
    print("Hello, NHL!")

