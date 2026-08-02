import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

password = ""

for i in range(10):
        char = random.choice(letters + numbers)
        password = password + char
print(password)