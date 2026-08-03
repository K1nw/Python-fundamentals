número=[]

for i in range(5):
    num=int(input("Digite um número: "))
    número.append(num)
    if número[i] % 2 == 0:
        print(f"O número {número[i]} é par.")
    else:
        print(f"O número {número[i]} é ímpar.")
