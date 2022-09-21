print("="*20)
print(" REAJUSTE SALÁRIAL ")
print("="*20)

salario = float(input("Salário: "))

if salario > 1250:
    salario = salario+(salario*0.10)
elif salario <= 12500:
    salario = salario+(salario*0.15)

print("-"*20)
print(f"Salário atual: {salario}")
