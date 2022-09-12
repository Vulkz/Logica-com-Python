sexo = input("Sexo (M/F): ").upper()

if sexo == "F" or "M":
    if sexo == "F":
        print("F - Feminino.")
    else:
        print("M - Masculino.")
else:
    print("Sexo inválido.")
