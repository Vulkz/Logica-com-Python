ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 4 != 0) or (ano % 400):
    print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é bissexto.")
