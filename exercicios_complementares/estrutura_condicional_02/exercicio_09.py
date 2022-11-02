from math import ceil

print("="*20)
print("   ESTACIONAMENTO   ")
print("="*20)

chegada = input("Chegada: ")
saida = input("Saida: ")

chegada = chegada.replace(':', '', 1)
saida = saida.replace(':', '', 1)

if chegada.isdigit() and saida.isdigit():
    if int(chegada) > int(saida):
        tot_horas = ceil(24-((int(chegada) - int(saida)) / 60))
    else:
        tot_horas = ceil((int(saida) - int(chegada)) / 60)
else:
    print("Erro!")
    exit()

if tot_horas <= 2:
    val_tot = tot_horas
elif tot_horas <= 4:
    val_tot = tot_horas * 1.40
elif tot_horas >= 5:
    val_tot = tot_horas * 2


print(f"Valor total a ser pago: R${val_tot}")
