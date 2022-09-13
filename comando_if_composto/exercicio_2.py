nome = input("Nome: ")
salario_atual = float(input("Salário Atual: "))

if salario_atual <= 1500:
    aumento = salario_atual + (salario_atual * 0.2)
elif salario_atual > 1500 or salario_atual <= 2800:
    aumento = salario_atual + (salario_atual * 0.15)
else:
    aumento = salario_atual + (salario_atual * 0.1)

print("-"*20)

print(f"Nome: {nome}")
print(f"Salário: {aumento}")
