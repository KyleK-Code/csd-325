# Author - Kyle Klausen
# Assignment4_2
# Date - 06/12/25
# Description: Below is a program designed to help people gain
# insight / data from some provided charts. This is provided through user input.

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Load data from the CSV file
filename = 'C:/Users/Kyle/Documents/CSD-325 Python Projects/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Start interactive loop
while True:
    print("\n--- Sitka Weather Data Viewer ---")
    print("1: View High Temperatures")
    print("2: View Low Temperatures")
    print("3: Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        # Plot high temperatures
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == '2':
        # Plot low temperatures
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == '3':
        print("\nThank you for using the Sitka Weather Data Viewer. Goodbye!")
        sys.exit()

    else:
        print("Invalid input. Please choose 1, 2, or 3.")