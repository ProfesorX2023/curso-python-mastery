'''

    habiendo recorrido con un for hacemos esto:
    if numeros[i] == 0 and numeros[i + 1] == 0 podemos retornar True

'''

def consecutivos(*args):

    for i in range(len(args)):
        if args[i] == 0 and args[i+1] == 0:
            return True


    return False


print(consecutivos(5,6,1,0,0,0,3,5))