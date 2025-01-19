#Password Generator Project
import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:

password = ""

for l in range(0, nr_letters):
    random_letter = random.choice(letters)
    password = password + random_letter

for s in range(0, nr_symbols):
    random_symbol = random.choice(letters)
    password = password + random_symbol

for n in range(0, nr_numbers):
    random_number = random.choice(letters)
    password = password + random_number

print(password)

#Hard Level - Order of characters randomised:

password_list = []

for l in range(0, nr_letters):
    password_list.append(random.choice(letters))

for s in range(0, nr_letters):
    password_list.append(random.choice(symbols))

for s in range(0, nr_letters):
    password_list.append(random.choice(numbers))

print("Before shuffling:", password_list)

random.shuffle(password_list)

print("After shuffling:", password_list)

my_password = ''.join(password_list)

print("Generated password:", my_password)
