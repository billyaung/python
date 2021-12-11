import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#or use random.choice
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random_letter = ""
random_number = ""
random_symbol = ""

for letter in range(0,nr_letters) :
    random_letter += letters[random.randint(0,50)]
for number in range(0, nr_numbers) :
    random_number += numbers[random.randint(0,10)]
for symbol in range(0,nr_symbols) :
    random_symbol += symbols[random.randint(0,8)]

random_password = random_letter + random_number + random_symbol
print(f"password in order - {random_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
unordered_password = ""

for password in range(0,len(random_password)):
    unordered_password += random_password[random.randint(0,len(random_password)-1)]
    
print(f"Password in random order - {unordered_password}")