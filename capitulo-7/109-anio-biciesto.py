# Dado un año, decir si es biciesto
# Biciesto si es divisible por 4
# Excepto si es divisible por 100
# A menos que tambien sea divisible por 400
# // division al piso da el cociente
# % modulo y da el residuo

anio = int(input("Ingrese su anio: "))

if anio % 400 == 0:
    print(f"{anio} es biciesto")
elif anio % 100 == 0:
    print(f"{anio} no es biciesto")
elif anio % 4 == 0:
    print(f"{anio} es biciesto")
else:
    print(f"{anio} no es biciesto")

es_biciesto = (anio % 4 == 0 and  anio % 100 != 0) or (anio % 400 == 0)
print(f"{anio} es {es_biciesto}")
