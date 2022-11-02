print("="*24)
print(" Seu carro é econômico? ")
print("="*24)

l = float(input("Litros: "))
km = float(input("Km: "))

kml = l / km

if kml < 8:
    print("Venda o carro !")
elif kml > 8 and kml < 12:
    print("Econômico !")
else:
    print("Super econômico !")
