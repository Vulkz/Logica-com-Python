num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
resultado = num1

for c in range(num2-1):
    acumulador = 0

    for c in range(num1):
        acumulador += resultado

    resultado = acumulador


print(f"{num1} elevado à {num2}: {resultado}")
