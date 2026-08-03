import random

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers_letters = "0123456789"
symbols_letters = "!@#$%&*"

password = ""
user_uppercase = ""
user_numbers = ""
user_symbols = ""
user_lowercase = ""

size = int(input("Digite o tamanho da senha: "))

while user_uppercase != "s" and user_uppercase != "n":
    user_uppercase = input("Deseja incluir letras maiúsculas? (s/n): ").lower()
    if user_uppercase != "s" and user_uppercase != "n":
        print("Opção inválida. Digite apenas s ou n.")

while user_numbers != "s" and user_numbers != "n":
    user_numbers = input("Deseja incluir números? (s/n): ").lower()
    if user_numbers != "s" and user_numbers != "n":
        print("Opção inválida. Digite apenas s ou n.")

while user_symbols != "s" and user_symbols != "n":
    user_symbols = input("Deseja incluir símbolos? (s/n): ").lower()
    if user_symbols != "s" and user_symbols != "n":
        print("Opção inválida. Digite apenas s ou n.")

characters = lowercase_letters

if user_uppercase == "s":
    characters += uppercase_letters

if user_numbers == "s":
    characters += numbers_letters

if user_symbols == "s":
    characters += symbols_letters

for i in range(size):
    char = random.choice(characters)
    password = password + char

print(f"Sua senha é: {password}")