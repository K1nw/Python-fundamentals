notas = [10, 9, 7, 4]

def calcular_media (lista_de_notas):
    soma = sum(lista_de_notas)
    quantidade = len (lista_de_notas)
    return soma / quantidade

resultado = calcular_media(notas)
print(resultado)
