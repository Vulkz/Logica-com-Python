num1 = int(input("1° Número: "))
num2 = int(input("2° Número: "))
num3 = int(input("3° Número: "))

guard = 0

if num1 > num2:
    guard = num2
    num2 = num1
    num1 = guard

if num1 > num3:
    guard = num3
    num3 = num1
    num1 = guard

if num2 > num3:
    guard = num3
    num3 = num2
    num2 = guard

print("-"*15)
print(f"Maior: {num1}")
print(f"Menor: {num3}")
