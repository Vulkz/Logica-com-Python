print("="*10)
print("   UBER   ")
print("="*10)

km = float(input("KMs: "))

if km <= 200:
    km *= 0.5
else:
    km *= 0.45

print(f"Valor: {km}")
