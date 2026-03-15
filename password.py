import random
import string

print("=== Random Password Generator ===")

length = int(input("Enter password length: "))
letters = input("Include letters? (yes/no): ").lower()
numbers = input("Include numbers? (yes/no): ").lower()
symbols = input("Include symbols? (yes/no): ").lower()

characters = ""

if letters == "yes":
    characters += string.ascii_letters
if numbers == "yes":
    characters += string.digits
if symbols == "yes":
    characters += string.punctuation

if characters == "":
    print("You must select at least one option!")
else:
    password = "".join(random.choice(characters) for i in range(length))
    print("Generated Password:", password)
