l1 = float(input("1° Lado: "))
l2 = float(input("2° Lado: "))
l3 = float(input("3° Lado: "))

if (l1 > l2+l3) or (l2 > l1+l3) or (l3 > l1+l2):
    print(f"Os valores {l1}, {l2} e {l3} não formam um triângulo.")
else:
    if l1 == l2 and l1 == l3:
        print(f"Os valores {l1}, {l2} e {l3} formam um triângulo EQUILATERO.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print(f"Os valores {l1}, {l2} e {l3} formam um triângulo ISÓCELES.")
    else:
        print(f"Os valores {l1}, {l2} e {l3} formam um triângulo ESCALENO.")