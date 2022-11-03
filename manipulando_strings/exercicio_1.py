palavra = input("Digite uma palavra: ")
num_vogais = 0

if palavra[0].upper() == 'A':
    print(f"{palavra} começa com a letra 'A'.")
else:
    print(f"{palavra} não começa com a letra 'A'.")

for c in palavra:

    if c.lower() in 'aeiou':
        num_vogais += 1

print(f"{palavra} tem {num_vogais} vogais.")
print(f"{palavra} tem {len(palavra)} caracteres.")
print(f"{palavra.upper()}.")
