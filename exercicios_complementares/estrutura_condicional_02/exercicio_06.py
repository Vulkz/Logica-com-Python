num = input("Digite um valor com 3 digitos: ")
soma = 0

if num.isdigit():

    for c in num:
        soma += int(c)
else:
    print("Número inválido.")
