# Author: Kyle Klausen
# Date: 06/29/25
# Assignment: 8.2
# Description: Loads, displays, updates, and saves a student list from a JSON file using py.

import json

def load_students(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def print_students(students, header):
    print(header)
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")
    print()  # Blank line for readability

def save_students(filename, students):
    with open(filename, 'w') as f:
        json.dump(students, f, indent=4)

def main():
    filename = r"C:/csd/csd-325/Module-8/student.json"

    # Load original students list
    students = load_students(filename)

    # Print original list
    print_students(students, "Original Student List:")

    # Append your own student info (replace with your details)
    new_student = {
        "F_Name": "YourFirstName",
        "L_Name": "YourLastName",
        "Student_ID": 123456,
        "Email": "youremail@example.com"
    }
    students.append(new_student)

    # Print updated list
    print_students(students, "Updated Student List:")

    # Save updated list back to JSON file
    save_students(filename, students)
    print(f"{filename} has been updated.")

if __name__ == "__main__":
    main()