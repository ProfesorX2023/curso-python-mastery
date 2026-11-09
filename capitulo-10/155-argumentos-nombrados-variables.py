def crear_perfil(**datos):
    print("=== Perfil ===")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

crear_perfil(nombre="Luis",edad=30,ciudad="Guatemala")
crear_perfil(nombre="María",profesion="Programadora")