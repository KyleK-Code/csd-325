# Author: Kyle Klausen
# Date: 05/31/25
"""
Description: This program is based off of the classic song and will 
display a loop feature to help keep the song going!
"""
def countdown_bottles(bottles):
    for i in range(bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer. Take one down and pass it around, {i-1} bottle(s) of beer on the wall.")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.")

def main():
    try:
        num_bottles = int(input("Enter number of bottles: "))
        if num_bottles < 1:
            print("Please enter a positive number greater than 0.")
            return
        countdown_bottles(num_bottles)
        print("Go buy more beer!")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
