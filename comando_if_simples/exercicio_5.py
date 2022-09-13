nome = input("Nome: ")
periodo = input("Periodo (M/V/N):").upper()

if periodo == "M":
    saudacao = "Bom dia"
elif periodo == "V":
    saudacao = "Boa tarde"
elif periodo == "N":
    saudacao = "Boa noite"
else:
    saudacao = "Valor inválido"

print(f"{saudacao}, {nome}.")
