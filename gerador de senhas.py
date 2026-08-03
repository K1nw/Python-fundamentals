import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&*"

characters = lowercase + uppercase + numbers + symbols

password = ""
size = int(input("Digite o tamanho da senha: "))
uppercase = input("Deseja incluir letras maiúsculas? (s/n): ").lower() == "s"
if uppercase:
    characters = lowercase + uppercase + numbers + symbols
else:
    print("Senha sem letras maiúsculas.")

numbers = input("Deseja incluir números? (s/n): ").lower() == "s"
if not numbers:
    characters = lowercase + uppercase + symbols
symbols = input("Deseja incluir símbolos? (s/n): ").lower() == "s"
if not symbols:
    characters = lowercase + uppercase + numbers

for i in range(size):
    char = random.choice(characters)
    password = password + char

print(f"Sua senha é: {password}")