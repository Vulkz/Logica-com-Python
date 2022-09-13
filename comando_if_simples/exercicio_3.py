valor = float(input("Valor da compra: R$"))
parcelas = int(input("Quantidade de parcelas: "))

valor_parcelas = valor/parcelas

if (valor/parcelas >= 20):
    print(f"{parcelas} parcelas R${valor_parcelas:.2f} cada uma.")
else:
    print(f"Não é possivel parcelar esse valor em {parcelas}.")
