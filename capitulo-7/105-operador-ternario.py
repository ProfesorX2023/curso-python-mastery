edad = 29

#if edad >= 18:
#    estado = "mayor"
#else:
#    estado = "menor"

estado = "mayor" if edad >= 18 else "menor"

print(estado)

hora = 15

saludo = "Buen día" if hora < 12 else "buena tarde" if hora < 18 else "Buena noche"

puntaje = 89

nota_letra = "A" if puntaje >= 90 else "B" if puntaje >= 80 else "C" if puntaje >= 70 else "D"

print(saludo)
print(nota_letra)
