num = int(input("Digite um número: "))

print("Números primos: ", end='')

for c in range(num, 1, -1):
    cont = 0

    for i in range(c, 1, -1):
        if c % i == 0:
            cont += 1

    if cont < 2:
        print(c, end=' ')
