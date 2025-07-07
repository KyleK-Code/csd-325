# Author: Kyle Klausen 
# Date: 07/06/25
# Description: Demonstrates API interaction with The Star Wars API (SWAPI), showing raw and formatted responses.

import requests
import json

def interact_with_chosen_api():
    """
    Interacts with a chosen simple API (SWAPI - Star Wars API),
    tests connection, prints raw response, and then a formatted response.
    """
    # Using The Star Wars API (SWAPI) - Luke Skywalker's data
    api_url = "https://swapi.dev/api/people/1/"

    print(f"\n--- Interacting with The Star Wars API (SWAPI) ({api_url}) ---")

    try:
        # Test the connection to your API
        print("\n--- Testing Connection ---")
        # Added verify=False to bypass SSL certificate verification due to expired certificate.
        # WARNING: Disabling SSL verification is NOT recommended for production environments.
        response = requests.get(api_url, verify=False)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Connection to SWAPI successful!")
        else:
            print(f"Connection to SWAPI failed with status code {response.status_code}.")
            return # Exit if connection fails

        # Print out the response from the request, with no formatting.
        print("\n--- Raw Response (No Formatting) ---")
        print(response.text)

        # Print out the response with same formatting as the tutorial program.
        print("\n--- Formatted Response ---")
        data = response.json() # Parse the JSON response

        # Format the output based on SWAPI's people endpoint structure
        print(f"Name: {data.get('name', 'N/A')}")
        print(f"Height: {data.get('height', 'N/A')} cm")
        print(f"Mass: {data.get('mass', 'N/A')} kg")
        print(f"Hair Color: {data.get('hair_color', 'N/A')}")
        print(f"Skin Color: {data.get('skin_color', 'N/A')}")
        print(f"Eye Color: {data.get('eye_color', 'N/A')}")
        print(f"Birth Year: {data.get('birth_year', 'N/A')}")
        print(f"Gender: {data.get('gender', 'N/A')}")
        print("-" * 30) # Separator for readability

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
    interact_with_chosen_api()