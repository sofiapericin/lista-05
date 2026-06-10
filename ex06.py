while True:
    nome = input("\nNome do atleta: ")

    if nome == "":
        break

    saltos = []

    for i in range(5):
        salto = float(input(f"{i+1}º salto: "))
        saltos.append(salto)

    melhor = max(saltos)
    pior = min(saltos)

    saltos.remove(melhor)
    saltos.remove(pior)

    media = sum(saltos) / 3

    print(f"\nAtleta: {nome}")
    print(f"Melhor salto: {melhor} m")
    print(f"Pior salto: {pior} m")
    print(f"Média dos demais saltos: {media:.2f} m")
