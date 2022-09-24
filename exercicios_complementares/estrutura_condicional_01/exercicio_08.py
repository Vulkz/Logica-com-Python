print("="*20)
print("    CALCULADORA   ")
print("="*20)

num1 = float(input("1° Número: "))
num2 = float(input("2° Número: "))

print("-"*20)
print(" + = Soma")
print(" - = Subtração")
print(" * = Multiplicação")
print(" / = Divisão")
print("-"*20)

sinal = input("Operador: ")
print("- "*10)

match sinal:
    case "+":
        print(f"R: {num1 + num2}")
    case "-":
        print(f"R: {num1 - num2}")
    case "*":
        print(f"R: {num1 * num2}")
    case "/":
        print(f"R: {num1 / num2}")
