pessoas = []
for i in range(3):
   if i == 0:
       pessoa = {}
       pessoa["nome"] = input("Digite o nome da pessoa: ")
       pessoa["idade"] = int(input("Digite a idade da pessoa: "))
       pessoa["cidade"] = input("Digite a cidade da pessoa: ")
       pessoas.append(pessoa)

for pessoa in pessoas:
    print(pessoa)   