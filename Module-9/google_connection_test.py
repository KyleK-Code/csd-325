# google_connection_test.py
# Author: Kyle Klausen
# Date: 07/06/25
# Description: Tests a basic HTTP connection to Google.com.

import requests

def test_google_connection():
    """
    Tests a basic HTTP GET request to http://www.google.com
    and prints the HTTP status code.
    """
    print("--- Testing Connection to http://www.google.com ---")
    try:
        response = requests.get('http://www.google.com')
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Connection to Google.com successful!")
        else:
            print(f"Connection to Google.com failed with status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during connection: {e}")

if __name__ == "__main__":
    test_google_connection()