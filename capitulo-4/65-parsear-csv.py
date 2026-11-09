#"Luis,30,Guatemala"

linea = "Luis,30,Guatemala"

nombre, edad, pais = linea.split(",") #["Luis", "30", "Guatemala"]

print(f"{nombre} tienes {edad} años y vives en {pais}")