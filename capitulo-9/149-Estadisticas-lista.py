def estadisticas(numeros):
    if not numeros:
        return None
    return {
        "min": min(numeros),
        "max": max(numeros),
        "promedio": sum(numeros) / len(numeros),
        "rango": max(numeros) - min(numeros)
    }

datos = [85, 72, 90, 65, 88, 95, 78]
stats = estadisticas(datos)

for clave, valor in stats.items():
    print(f"{clave}: {valor}")