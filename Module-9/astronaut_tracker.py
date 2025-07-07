# astronaut_tracker.py
# Author: Kyle Klausen
# Date: 07/06/25
# Description: Retrieves and displays a formatted list of astronauts currently in space.

import requests
import json # Used for pretty-printing JSON

def get_astronauts():
    """
    Fetches data about astronauts currently in space from the Open Notify API
    and prints it in a formatted way.
    """
    api_url = "http://api.open-notify.org/astros.json"
    print(f"\n--- Retrieving Astronauts from {api_url} ---")
    try:
        response = requests.get(api_url)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)

        data = response.json() # Parse the JSON response

        print(f"Status Code: {response.status_code}")
        print(f"Number of Astronauts in Space: {data['number']}")
        print("\n--- Current Astronauts ---")
        for person in data['people']:
            print(f"Name: {person['name']}")
            print(f"Craft: {person['craft']}")
            print("-" * 20) # Separator for readability

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred: {req_err}")
    except json.JSONDecodeError as json_err:
        print(f"Error decoding JSON response: {json_err}")
        print(f"Raw response content: {response.text}") # Print raw content for debugging

if __name__ == "__main__":
    get_astronauts()