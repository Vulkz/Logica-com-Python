print("="*20)
print(" " * 7 + "RADAR" + " " * 7)
print("="*20)
vel = float(input("Velocidade (KM): "))
print("-"*20)

if vel > 80:
    multa = (vel-80) * 5

    print("Acima da velocidade.")
    print(f"MULTA: R${multa}.")
else:
    print("Está na velocidade permitida.")
