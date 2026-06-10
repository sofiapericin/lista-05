linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"Elemento [{i}][{j}]: ")))
    matriz.append(linha)

maior = matriz[0][0]
menor = matriz[0][0]

for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print("Maior elemento:", maior)
print("Menor elemento:", menor)
