nombres = ["Luis","María","Pedro"]
buscando = "Juan"

for nombre in nombres:
    if nombre == buscando:
        print("Encontrado!")
        break
else:
    print(f"{buscando} no está en la lista!")