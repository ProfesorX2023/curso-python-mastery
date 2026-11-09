#3725 -> 1h 02m 05s
try:
    total =  int(input("Escribe la cantidad de segundos: "))

    horas = total // 3600
    resto = total % 3600
    minutos = resto // 60
    segundos = resto % 60
    print(f"{total} segundos = {horas}h {minutos:02d}m {segundos:02d}s")
except ValueError:
    print("❌Cantidad invalidad, pruebe de nuevo")