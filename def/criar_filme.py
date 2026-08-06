def mostrar_filme(filme):
    print(f"Título: {filme['titulo']}")
    print(f"Nota: {filme['nota']}")
    print(f"Review: {filme['review']}")


# Teste
filme = {
    "titulo": "Superman",
    "nota": 9.5,
    "review": "filme muito bom"
}

mostrar_filme(filme)