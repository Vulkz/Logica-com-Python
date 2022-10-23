for c in range(0, 5):
    num = int(input(f"Digite o {c+1}° número: "))

    if c == 0:
        maior = num
        menor = num
        continue

    if num > maior:
        maior = num
    if num < menor:
        menor = num
    
print("- "*10)

print(f"O menor número digitado foi: {menor}")
print(f"O maior número digitado foi: {maior}")