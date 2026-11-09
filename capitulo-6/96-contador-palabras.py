texto = "el sol sale por el este y se pone por el oeste"
conteo = {}

for palabra in texto.split(): #iterador es palabra -> cambiante, texto.split() iterable
    conteo[palabra] =  conteo.get(palabra,0) + 1

print(conteo)

mas_frecuente = max(conteo, key=conteo.get)
print(f"✅ Más frecuente: '{mas_frecuente}' ({conteo[mas_frecuente]} veces)")