pessoa1 = {}
pessoa2 = {}
pessoa3 = {}
pessoas = [pessoa1, pessoa2, pessoa3]

pessoa1["nome"] = input("Digite o nome da pessoa: ")
pessoa1["idade"] = int(input("Digite a idade da pessoa: "))
pessoa1["cidade"] = input("Digite a cidade da pessoa: ")

pessoa2["nome"] = input("Digite o nome da pessoa: ")
pessoa2["idade"] = int(input("Digite a idade da pessoa: "))
pessoa2["cidade"] = input("Digite a cidade da pessoa: ")

pessoa3["nome"] = input("Digite o nome da pessoa: ")
pessoa3["idade"] = int(input("Digite a idade da pessoa: "))
pessoa3["cidade"] = input("Digite a cidade da pessoa: ")

print(pessoas[0])
print(pessoas[1])
print(pessoas[2])