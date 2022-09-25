print("="*19)
print(" Números Positivos  ")
print("="*19)

num = int(input("Número: "))

if num > 0:
    print(f"Raiz: {num**(1/2)}")
    print(f"Quadrado: {num**2}")
else:
    print("Número Inválido.")
