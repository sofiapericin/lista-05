linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(i * j)
    matriz.append(linha)

print("\nMatriz:")

for linha in matriz:
    print(linha)
