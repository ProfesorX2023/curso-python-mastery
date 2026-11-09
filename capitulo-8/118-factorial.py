# Factorial de n es 1*2*3*...n = n!
# 4 es 4*3*2*1

factorial = int(input("Ingrese el número al cual desea calcular el factorial: "))

resultado = 1 # variable acumuladora, hay que saber como inicializar
for numero in range(1,factorial+1):
    resultado = resultado * numero

print(f"el factorial de {factorial} es: {resultado}")