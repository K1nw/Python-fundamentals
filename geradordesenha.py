import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers_chars = "0123456789"
symbols_chars = "!@#$%&*"

size = int(input("Digite o tamanho da senha: "))

use_uppercase = input("Deseja incluir letras maiúsculas? (s/n): ").lower() == "s"
use_numbers = input("Deseja incluir números? (s/n): ").lower() == "s"
use_symbols = input("Deseja incluir símbolos? (s/n): ").lower() == "s"

characters = lowercase

if use_uppercase:
    characters += uppercase_letters

if use_numbers:
    characters += numbers_chars

if use_symbols:
    characters += symbols_chars

password = ""

for i in range(size):
    char = random.choice(characters)
    password += char

print(f"Sua senha é: {password}")