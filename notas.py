notas = [8, 7, 5, 9, 6]
for nota in notas:
    if nota >= 7:
        print(f"Nota {nota}: Aprovado")
    elif nota >= 5:
        print(f"Nota {nota}: Recuperação")
    else:
        print(f"Nota {nota}: Reprovado")