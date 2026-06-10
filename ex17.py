linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))

matriz = []

for i in range(linhas):
    linha = list(map(int, input(f"Linha {i+1}: ").split()))
    matriz.append(linha)

valida = True

for linha in matriz:
    if len(linha) != colunas:
        valida = False

quadrada = valida and (linhas == colunas)

print(quadrada)
