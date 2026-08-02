answer = ""

while answer != "s" and answer != "n":
    answer = input("Deseja incluir letras maiúsculas? (s/n): ").lower()
    
    if answer != "s" and answer != "n":
        print("Opção inválida. Digite apenas s ou n.")