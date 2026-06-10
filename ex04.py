cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulos = 0
brancos = 0

while True:
    print("\n1 - José")
    print("2 - João")
    print("3 - Maria")
    print("4 - Ana")
    print("5 - Nulo")
    print("6 - Branco")
    print("0 - Encerrar")

    voto = int(input("Voto: "))

    if voto == 0:
        break
    elif voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 4:
        cand4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1

total = cand1 + cand2 + cand3 + cand4 + nulos + brancos

print("\nResultado da eleição")
print(f"José: {cand1}")
print(f"João: {cand2}")
print(f"Maria: {cand3}")
print(f"Ana: {cand4}")
print(f"Nulos: {nulos}")
print(f"Brancos: {brancos}")

if total > 0:
    print(f"% Nulos: {(nulos/total)*100:.2f}%")
    print(f"% Brancos: {(brancos/total)*100:.2f}%")
