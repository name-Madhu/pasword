This project is a simple password generator built using Python. It generates a strong and random password using letters, numbers, and special characters.

Features
Generates random secure passwords
User can choose password length
Uses letters, digits, and symbols
Simple command-line program
Technologies Used
Python
random module
string module                                                                                                                                                                                                          Code
import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)
How to Run the Program
Install Python on your computer.
Save the file as:
password_generator.py
Run the program using the terminal:
python password_generator.py
Example Output
Enter password length: 10
Generated Password: A7@kP!9qW2
Project Purpose
This project demonstrates how Python can be used to generate secure random passwords. It helps beginners understand how to use Python libraries like random and string.

Author
Madhu Chirghute
