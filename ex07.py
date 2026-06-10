while True:
    nome = input("\nNome do atleta: ")

    if nome == "":
        break

    notas = []

    for i in range(7):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)

    melhor = max(notas)
    pior = min(notas)

    notas.remove(melhor)
    notas.remove(pior)

    media = sum(notas) / len(notas)

    print("\nResultado Final")
    print(f"Atleta: {nome}")
    print(f"Melhor nota: {melhor}")
    print(f"Pior nota: {pior}")
    print(f"Média: {media:.2f}")
