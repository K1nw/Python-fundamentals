number = 0 

while number < 1 or number > 120:
    number = int(input("Digite um número entre 1 e 120: "))
    if number < 1 or number > 120:
        print("Número inválido. Digite um número entre 1 e 120.")