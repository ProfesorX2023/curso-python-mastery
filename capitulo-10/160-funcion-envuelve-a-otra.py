import time

def cronometrar(func, *args, **kwargs):
    '''
        Ejecutar funcion con sus argumentos, y mide
        cuanto tiempo tarda
    '''
    inicio = time.time() # captura la hora 3:48:24:12
    resultado = func(*args, **kwargs)
    duracion = time.time() - inicio
    print(f"{func.__name__} tardó {duracion:.4f} segundos")
    return resultado

def sumar_hasta(n):
    total = 0
    for i in range(n):
        total += i

    return total

resultado = cronometrar(sumar_hasta,1_000_000_000)
print(resultado)