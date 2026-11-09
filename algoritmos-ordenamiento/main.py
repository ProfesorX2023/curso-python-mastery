from algoritmos import ALGORITMOS
import os

def mostrar_menu():
    print("\n===== ALGORITMOS DE ORDENAIENTO =====")
    for i, clase in enumerate(ALGORITMOS, start=1):
        print(f"{i}. {clase().nombre}")
    print(f"{len(ALGORITMOS) + 1}. Comparar todos")
    print("0. Salir")


def leer_lista():
    texto = input("Números separados por comas (ENTER = 6,5,3,1,8,7,2,4)")
    if texto.strip() == "":
        return [6,5,3,1,8,7,2,4]
    return [int(x) for x in texto.split(",")]

def main():
    os.system("color 51")
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "0":
            print("¡Hasta luego!")
            break

        if not opcion.isdigit() or int(opcion) > len(ALGORITMOS) + 1:
            print("Opción no válida")
            continue

        lista = leer_lista()
        opcion = int(opcion)

        if opcion == len(ALGORITMOS) + 1:
            for clase in ALGORITMOS:
                algoritmo = clase()
                resultado = algoritmo.ordenar(lista)
                print(f"{algoritmo.nombre:<12}: {resultado} comparaciones: {algoritmo.comparaciones} \n")
        else:
            algoritmo = ALGORITMOS[opcion - 1]()
            resultado = algoritmo.ordenar(lista)
            print(f"\n{algoritmo.nombre:<12}: {resultado}")
            print(f"{'Comparaciones':<12} {algoritmo.comparaciones}")


if __name__ == '__main__':
    main()