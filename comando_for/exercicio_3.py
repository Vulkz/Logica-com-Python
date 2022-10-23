media_m = 0
homem = 0

media_f = 0
mulher = 0

media_g = 0
maior = 0

for c in range(0, 10):

    sexo = input("Sexo (M/F) : ")
    idade = int(input("Idade: "))

    media_g += idade

    if sexo.upper() == "M":
        media_m += idade
        homem += 1
    elif sexo.upper() == "F":
        media_f += idade
        mulher += 1

    if idade > maior:
        maior = idade

media_m /= homem
media_f /= mulher
media_g /= 10

print(f"Idade média das mulheres: {media_f}")
print(f"Idade média dos homens: {media_m}")
print(f"Idade média do grupo: {media_g}")
print('-'*20)

print(f"A maior idade digitada foi: {maior}")
