primos = ""

num = int(input("Digite um número: "))

while num > 0:

    sub_num = num
    cont = 0

    while sub_num > 0:

        if num % sub_num == 0:
            cont += 1

        sub_num -= 1

    if cont == 2:
        primos = primos + " " + str(num)

    num -= 1

print(f"Primos: {primos}")
