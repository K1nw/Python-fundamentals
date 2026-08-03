size = 0 
answer = ""


while size < 6 or size > 30:
    size = int(input("Qual o tamanho da sua senha? "))
    if size < 6 or size > 30:
        print("Tamanho inválido. Digite um tamanho entre 6 e 30.")

while answer != "s" and answer != "n":
    answer = input("deseja incluir símbolos? (s/n)").lower()
    if answer != "s" and answer != "n":
        print("Opção inválida. Digite apenas s ou n.")

if answer == "s":
        answer = "Sim"
else:
        answer = "Não"

print("Tamanho da senha escolhida:", size)
print("Incluir símbolos:", answer)
