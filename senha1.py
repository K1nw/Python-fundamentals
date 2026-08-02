import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = '0123456789'
characteres = letters + numbers

password = ""

for i in range(6):
    char = random.choice(characteres)
    password = password + char
    
print(password)
