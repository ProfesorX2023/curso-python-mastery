def calcular_imc(peso_kg, altura_m):
    '''
    Calcular el Indice de masa Corporal (IMC)

    Argumentos:
        peso_kg: Peso del paciente float
        altura_m: Altura del paciente en float

    Retorna:
        float: el IMC redondeado a 2 decimales
    '''
    return round(peso_kg / (altura_m ** 2), 2)


print(calcular_imc(70,1.60))
help(calcular_imc)
print(calcular_imc.__doc__)