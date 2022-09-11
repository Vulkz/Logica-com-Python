real = float(input("Valor em R$: "))
cota = float(input("Cotação atual em R$: "))

dolar = real*cota

print(f"R${real} é igual a US${dolar:.2f}.")
