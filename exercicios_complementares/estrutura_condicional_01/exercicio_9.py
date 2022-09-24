print("="*20)
print("    FINANCIAMENTO    ")
print("="*20)

valor_casa = float(input("Valor: "))
anos = int(input("Anos: "))
mensalidade = valor_casa / (anos * 12)

print("-"*20)

salario = float(input("Salário: R$"))

print("- "*10)

if (mensalidade / salario) <= 0.3:
    print("APROVADO!")
else:
    print("REPROVADO!")
