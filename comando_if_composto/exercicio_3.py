num1 = int(input("1° Número: "))
num2 = int(input("2° Número: "))
num3 = int(input("3° Número: "))

gua = num1

if num1 > num2:
    num1 = num2
    num2 = gua

if num2 > num3:
    gua = num2
    num2 = num3
    num3 = gua
    gua = num2

if num1 > num2:
    num2 = num1
    num1 = gua

print("-"*20)
print(num1, num2, num3)
