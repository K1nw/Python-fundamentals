answer = ""


while answer != "azul" and answer != "vermelho" and answer != "verde":
        answer = input("Digite sua cor: ").lower()
        
        if answer != "azul" and answer != "vermelho" and answer != "verde":
            print("Opção inválida. Digite apenas azul, vermelho ou verde.")