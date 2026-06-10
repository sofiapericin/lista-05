n = int(input("Digite a ordem da matriz quadrada: "))

matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input(f"Elemento [{i}][{j}]: ")))
    matriz.append(linha)

soma_principal = 0
soma_secundaria = 0

for i in range(n):
    soma_principal += matriz[i][i]
    soma_secundaria += matriz[i][n - 1 - i]

print("Soma da diagonal principal:", soma_principal)
print("Soma da diagonal secundária:", soma_secundaria)
