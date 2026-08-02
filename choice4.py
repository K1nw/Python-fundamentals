import random

letters = "python"

random_letter = random.choice(letters)

user_input = input("Digite uma letra: ")
if user_input == random_letter:
    print("Parabéns! Você acertou!")
else:
    print(f"Que pena! A letra sorteada foi {random_letter}. Tente novamente!")