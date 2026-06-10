linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"Elemento [{i}][{j}]: ")))
    matriz.append(linha)

elemento = int(input("Elemento a procurar: "))

contador = 0

for linha in matriz:
    contador += linha.count(elemento)

print(f"O elemento aparece {contador} vez(es).")
