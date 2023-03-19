import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")

#Ask how long they would like the password to be
pw_length = int(input("How many letters would you like in your password?\n"))

#Ask how many numbers thet would like in the password
pw_numbers = int(input("How many numbers would you like in your password?\n"))

#Ask how many symbols they would like in the password
pw_symbol = int(input("How many symbols would you like in your password?\n"))

#print generated password
pw_list = []

for char in range(1, pw_length +1):
    pw_list.append(random.choice(letters))

for char in range(1, pw_numbers +1):
    pw_list.append(random.choice(numbers))

for char in range(1, pw_symbol +1):
    pw_list.append(random.choice(symbols))

random.shuffle(pw_list)

password = ""
for x in pw_list:
    password += x

print("Your password is " + password)