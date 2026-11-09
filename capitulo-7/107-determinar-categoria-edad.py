# bebe 0-2, 3-12 niño, 13-17 adolescente, 18-64 adulto, 65+ adulto mayor


try:
    edad = int(input("Ingrese su edad: "))
    if edad < 0:
        print("No se puede agregar edades negativas")
    elif edad <= 2:
        print("Bebé")
    elif edad < 18:
        print("adolescente")
    elif edad <= 64:
        print("Adulto")
    elif edad > 64:
        print("Adulto mayor")
    else:
        print("Ingrese una edad válida")
except ValueError:
    print("Ingrese una edad valida")

