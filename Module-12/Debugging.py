"""
Author: Kyle Klausen
Date: 05/17/25
Description:
Create a program that collects user data from a charity event, and the program will save this data to a CSV file for compatability with spreadsheet software.
"""

import csv
import os

# Define the CSV file name
FILE_NAME = "charity_event_attendees.csv"

# Create the file with headers if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone", "Donation"])

def get_user_data():
    print("Enter attendee information:")
    name = input("Full Name: ").strip()
    import pdb; pdb.set_trace() # <- Breakpoint
    email = input("Email Address: ").strip()
    phone = input("Phone Number: ").strip()
    donation = input("Donation Amount (USD): ").strip()

    return [name, email, phone, donation]

def save_user_data(user_data):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(user_data)

def main():
    print("Welcome to the Charity Event Registration System")
    while True:
        user_data = get_user_data()
        save_user_data(user_data)
        print("Attendee data saved successfully.\n")

        more = input("Would you like to enter another attendee? (y/n): ").strip().lower()
        if more != 'y':
            break

    print("Thank you for using the registration system.")

if __name__ == "__main__":
    main()
    