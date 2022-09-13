p1 = float(input("1° Produto: "))
p2 = float(input("2° Produto: "))
p3 = float(input("3° Produto: "))

menor = p1

if menor > p2:
    menor = p2
if menor > p3:
    menor = p3

print(f"O produto mais barato custa: {menor}")
