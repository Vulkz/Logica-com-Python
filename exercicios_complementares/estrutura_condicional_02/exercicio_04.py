print("="*20)
print("    Número Real   ")
print("="*20)

num = int(input("Digite um número: "))

if num > 0:
    print(f"A raiz de {num} é {num**(1/2)}")
else:
    print(f"{num} ao quadrado é {num**2}")
