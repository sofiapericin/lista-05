faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0

while True:
    num = float(input("Digite um número positivo (negativo para sair): "))

    if num < 0:
        break

    if 0 <= num <= 25:
        faixa1 += 1
    elif 26 <= num <= 50:
        faixa2 += 1
    elif 51 <= num <= 75:
        faixa3 += 1
    elif 76 <= num <= 100:
        faixa4 += 1

print("\nResultado:")
print(f"[0 - 25]: {faixa1}")
print(f"[26 - 50]: {faixa2}")
print(f"[51 - 75]: {faixa3}")
print(f"[76 - 100]: {faixa4}")
