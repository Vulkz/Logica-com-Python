print("="*16)
print("    Produtos    ")
print("="*16)

categoria = int(input("Categoria: "))

match categoria:
    case 1:
        print("O valor é R$ 10.00")
    case 2:
        print("O valor é R$ 15.00")
    case 3:
        print("O valor é R$ 19.00")
    case 4:
        print("O valor é R$ 23.00")
    case 5:
        print("O valor é R$ 27.00")
