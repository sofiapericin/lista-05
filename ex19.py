texto = input("Digite uma frase: ").lower()

vogais = 0
consoantes = 0

for letra in texto:
    if letra.isalpha():
        if letra in "aeiou":
            vogais += 1
        else:
            consoantes += 1

print("Quantidade de vogais:", vogais)
print("Quantidade de consoantes:", consoantes)
