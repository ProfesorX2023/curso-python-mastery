nombres = ["Luis","María","Pedro","Ana","Juan"]
buscado = "Pedro"

for nombre in nombres:
    if buscado == nombre:
        print(f"Encontrado {nombre}")
        break
    print(f"buscando {nombre}")