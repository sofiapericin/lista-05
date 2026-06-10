linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"Elemento [{i}][{j}]: ")))
    matriz.append(linha)

nova_matriz = matriz[::-1]

print("\nNova matriz:")

for linha in nova_matriz:
    print(linha)
