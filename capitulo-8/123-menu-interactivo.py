while True:
    print("=== MENU ===")
    print("[1] ver productos")
    print("[2] Agregar producto")
    print("[0] Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        print("Mostrando productos ...")
    elif opcion == "2":
        print("Agregar producto ...")
    elif opcion == "0":
        print("Adios")
        break
    else:
        print("Opción inválida")