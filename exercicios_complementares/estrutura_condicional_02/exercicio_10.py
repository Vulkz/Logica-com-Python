data = input("Digite uma data (dd/mm/aaaa): ")
data_verifi = data.split('/')

erros = 0

if int(data_verifi[0]) > 30 or int(data_verifi[0]) < 1:
    erros += 1
elif int(data_verifi[1]) > 12 or int(data_verifi[1]) < 1:
    erros += 1
elif int(data_verifi[2]) < 0:
    erros += 1

if int(data_verifi[2]) % 4 == 0 or int(data_verifi[2]) % 400 == 0:
    if int(data_verifi[1]) == 2 and int(data_verifi[0]) > 29:
        erros += 1
else:
    if int(data_verifi[1]) == 2 and int(data_verifi[0]) > 28:
        erros += 1

if erros > 0:
    print("Data inválida.")
else:
    print("Data correta !")
