while True:
    try:
        numero = int(input("Ingresa un número entero: "))
        print(f"El doble es {numero * 2 }")
        print(f"El cuadrado es {numero ** 2}")
        print(f"Es par? {numero % 2 == 0}")
    except ValueError:
        print("Eso no parece un número entero válido")
        print("Volver a correr el programa")