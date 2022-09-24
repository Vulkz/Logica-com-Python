print("="*20)
print("   CONTA DE LUZ   ")
print("="*20)
print()

kwh = float(input("Kwh Gastos: "))

print("-"*20)
print(" R = Residencial")
print(" C = Comercial")
print(" I = Industrial")
print("-"*20)

tipo = input("Instalação: ").upper()

print("- "*10)

match tipo:
    case "R":
        if kwh <= 500:
            print(f"VALOR: {kwh * 0.40}")
        else:
            print(f"VALOR: {kwh * 0.65}")
    case "C":
        if kwh <= 1000:
            print(f"VALOR: {kwh * 0.55}")
        else:
            print(f"VALOR: {kwh * 0.60}")
    case "I":
        if kwh <= 5000:
            print(f"VALOR: {kwh * 0.55}")
        else:
            print(f"VALOR: {kwh * 0.60}")
