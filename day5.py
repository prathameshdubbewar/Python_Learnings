# using for looop with range

# for number in range(2, 101, 2):#for even number we can add size difference
    # print(number)

# Strong Password Generator 

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
a_letters= int(input("How many letters would you like in your password?\n")) 
a_numbers = int(input(f"How many numbers would you like?\n"))
a_symbols = int(input(f"How many symbols would you like?\n"))

#for sequential pattern

# password = ""

# for char in range(1, a_letters+1):
#     password = password+ random.choice(letters)

# for num in range (1, a_numbers+1):
#     password = password + random.choice(numbers)

# for sym in range (1, a_symbols+1):
#     password = password + random.choice(symbols)

# print(password)


#for random sequence

password = []

for char in range(1, a_letters+1):
    password += random.choice(letters)

for num in range (1, a_numbers+1):
    password += random.choice(numbers)

for sym in range (1, a_symbols+1):
    password += random.choice(symbols)

print(password)
random.shuffle(password)
final_password = ""

for a in password:
    final_password = final_password + a 
print(f"Your password can be {final_password}")