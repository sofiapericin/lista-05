total_geral = 0

while True:
    print("\n100 - Cachorro Quente (R$1,20)")
    print("101 - Bauru Simples (R$1,30)")
    print("102 - Bauru com Ovo (R$1,50)")
    print("103 - Hambúrguer (R$1,20)")
    print("104 - Cheeseburguer (R$1,30)")
    print("105 - Refrigerante (R$1,00)")
    print("0 - Encerrar pedido")

    codigo = int(input("Código: "))

    if codigo == 0:
        break

    quantidade = int(input("Quantidade: "))

    if codigo == 100:
        preco = 1.20
    elif codigo == 101:
        preco = 1.30
    elif codigo == 102:
        preco = 1.50
    elif codigo == 103:
        preco = 1.20
    elif codigo == 104:
        preco = 1.30
    elif codigo == 105:
        preco = 1.00
    else:
        print("Código inválido!")
        continue

    total_item = preco * quantidade
    total_geral += total_item

    print(f"Valor do item: R$ {total_item:.2f}")

print(f"\nTotal geral: R$ {total_geral:.2f}")
