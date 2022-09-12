numero = list()

for c in range(3):
    num = int(input(f"Digite o {c+1}° número: "))
    numero.append(num)

print(f"Maior: {max(numero)}")
