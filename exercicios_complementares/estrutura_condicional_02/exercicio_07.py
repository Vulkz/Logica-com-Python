print("="*19)
print("    VALOR FINAL    ")
print("="*19, "\n")

valor = input("Valor: R$")
estad = input("UF: ").upper()
print("-"*19)

if valor.isdigit() == False:
    print("Valor Inválido.")
else:
    valor = int(valor)

    match estad:
        case "MG":
            valor += valor * 0.07
        case "MS":
            valor += valor * 0.08
        case "SP":
            valor += valor * 0.12
        case "RJ":
            valor += valor * 0.15
        case _:
            print("UF Inválido.")

    print(f"VT: R${valor}")
