print("="*20)
print("     Car Year ")
print("="*20)

idade = int(input("Carro: "))

print("-"*20)

if idade > 0 and idade <= 3:
    print("Seu carro é NOVO!")
elif idade > 0 and idade > 3:
    print("Seu carro é VELHO!")
