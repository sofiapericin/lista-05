gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]

maior = 0
menor = 10
total_alunos = 0
soma_notas = 0

while True:
    acertos = 0

    print("\nResponda as questões:")

    for i in range(10):
        resposta = input(f"Questão {i+1}: ").upper()

        if resposta == gabarito[i]:
            acertos += 1

    print(f"Acertos: {acertos}")
    print(f"Nota: {acertos}")

    total_alunos += 1
    soma_notas += acertos

    if acertos > maior:
        maior = acertos

    if acertos < menor:
        menor = acertos

    continuar = input("Outro aluno? (S/N): ").upper()

    if continuar != "S":
        break

print("\nRelatório Final")
print(f"Maior Acerto: {maior}")
print(f"Menor Acerto: {menor}")
print(f"Total de Alunos: {total_alunos}")
print(f"Média da Turma: {soma_notas/total_alunos:.2f}")
