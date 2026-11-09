class Empleado:


    empresa = "Academia Fibonacci"
    contador = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.contador += 1
        self.id_empleado = str(Empleado.contador)+" " + str(self.salario) + " 0101"


empleado1 = Empleado("Luis", 15_000)
empleado2 = Empleado("María", 24_000)

print(empleado1.nombre, empleado1.empresa,empleado1.id_empleado)
print(empleado2.nombre, empleado2.empresa,empleado2.id_empleado)