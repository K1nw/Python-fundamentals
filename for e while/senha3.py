import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&*"

characters = lowercase + uppercase + numbers + symbols

password = ""
size = int(input("Digite o tamanho da senha: "))

for i in range(size):
    char = random.choice(characters)
    password = password + char

print(f"Sua senha é: {password}")