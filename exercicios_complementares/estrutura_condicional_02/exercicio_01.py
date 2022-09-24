print("="*20)
print("   DVISIVEL 3 OU 5   ")
print("="*20)

num = int(input("Digite um número: "))
print("- "*10)

if (num % 3 == 0) and (num % 5 != 0):
    print("DIVISIVEL POR 3.")
elif (num % 5 == 0) and (num % 3 != 0):
    print("DIVISIVEL POR 5.")
elif (num % 5 == 0) and (num % 3 == 0):
    print("DIVISIVEL POR 3 E 5.")
else:
    print("NÃO É DIVISIVEL.")
