#numero = 8
#if numero > 0:
#    print("positivo")
#elif numero < 0:
#    print("negativo")
#else:
#    print("CERO")

# 8 > 0 🤔✅
#"positivo"

opcion = input("Ingrese la opción(1,2,3,4): ")

match opcion:
    case "1":
        print("Listar productos")
    case "2":
        print("crear producto")
    case "3":
        print("Editar producto")
    case "4":
        print("salir")
    case _:
        print("Opcion invalida")