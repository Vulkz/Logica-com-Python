num1 = float(input("1° Número: "))
num2 = float(input("2° Número: "))
num3 = float(input("3° Número: "))

maior = num1

if maior < num2:
    maior = num2
if maior < num3:
    maior = num3

print(f"Maior: {maior}")
