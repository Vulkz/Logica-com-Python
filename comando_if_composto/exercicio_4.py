print("1 -->   Domingo")
print("2 -->   Segunda")
print("3 -->     Terça")
print("4 -->    Quarta")
print("5 -->    Quinta")
print("6 -->     Sexta")
print("7 -->    Sabado")
print("-"*15)

num_dia = int(input("Número: "))

if num_dia < 1 or num_dia > 7:
    print("Número inválido.")
else:
    if num_dia == 1:
        print("Hoje é DOMINGO!")
    elif num_dia == 2:
        print("Hoje é SEGUNDA!")
    elif num_dia == 3:
        print("Hoje é TERÇA!")
    elif num_dia == 4:
        print("Hoje é QUARTA!")
    elif num_dia == 5:
        print("Hoje é Quinta!")
    elif num_dia == 6:
        print("SEXTOUUUUU!")
    else:
        print("Hoje é Sabádo!")
