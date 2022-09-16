nome = ""
sexo = ""
idade = 0
salario = 0

print("="*20)
print("Formulário")
print("="*20)

while True:

    if nome == "":
        nome = input("Nome: ")
        continue
    elif idade < 14 or idade > 80:
        idade = int(input("Idade: "))
        continue
    elif salario <= 0:
        salario = float(input("Salário: "))
        continue
    elif sexo != 'F' or 'M':
        sexo = input("Sexo: ").upper()
        continue
    else:
        break

print("-"*20)
print(f"Nome:    {nome}")
print(f"Idade:   {idade}")
print(f"Salário: {salario}")
print(f"Sexo:    {sexo}")
