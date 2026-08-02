notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for nota in notas:
        if nota >= 7:
            print(f"Nota {nota}: Aprovado")
        elif nota >= 5:
            print(f"Nota {nota}: Recuperação")
        else:
            print(f"Nota {nota}: Reprovado")
