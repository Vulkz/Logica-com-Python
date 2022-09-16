maior = 0
cont = 0

quant = int(input("Quantidade: "))

while quant > cont:

    valor = float(input(f"{cont+1}° Valor: "))

    if valor > maior:
        maior = valor

    cont += 1

print("-"*15)
print(f"O maior valor digitado foi: {maior}")
