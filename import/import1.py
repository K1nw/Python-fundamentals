import random

numero1 = random.randint(1, 6)
user_input = int(input("Digite um número entre 1 e 6: "))
if user_input == numero1:
    print("Parabéns! Você acertou!")
else: print(f"Que pena! O número sorteado foi {numero1}. Tente novamente!")