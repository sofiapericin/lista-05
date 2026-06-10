divida = float(input("Digite o valor da dívida: R$ "))

print("\nValor da Dívida\tValor dos Juros\tParcelas\tValor da Parcela")

parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]

for i in range(len(parcelas)):
    valor_juros = divida * juros[i] / 100
    valor_total = divida + valor_juros
    valor_parcela = valor_total / parcelas[i]

    print(f"R$ {valor_total:.2f}\t\tR$ {valor_juros:.2f}\t\t{parcelas[i]}\t\tR$ {valor_parcela:.2f}")
