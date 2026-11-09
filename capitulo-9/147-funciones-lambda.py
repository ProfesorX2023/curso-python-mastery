cuadrado = lambda x: x ** 2
print(cuadrado(5))
print(cuadrado(7))

suma = lambda a, b: a + b
print(suma(5, 7))

nombres = ["María","Luis","Ana","Pedro"]
ordenados = sorted(nombres, key=lambda x: len(x))
print(ordenados)

precios = [100,250,480,320]
con_iva = list(map(lambda p: round(p * 1.12,2), precios))

print(con_iva)

caros = list(filter(lambda p: p > 200, precios))
print(caros)
