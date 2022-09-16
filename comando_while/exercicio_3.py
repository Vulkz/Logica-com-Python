valores = ""

print("0 - Para sair")
print("="*20)

while True:
    num = int(input("Numero: "))

    if num == 0:
        break
    elif num % 2 != 0:
        valores = valores + str(num) + "\n"

print(valores)
