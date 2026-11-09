class Empleado:

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def presentarse(self):
        print(f"Soy {self.nombre}")

    def calcular_sueldo(self):
        return self.salario * 1.20

class Programador(Empleado):

    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def codear(self):
        print(f"{self.nombre} está codeando en {self.lenguaje}")

class Gerente(Empleado):
    def __init__(self, nombre, salario, equipo):
        super().__init__(nombre, salario)
        self.equipo = equipo

    def asignar_tarea(self, persona, tarea):
        print(f"{self.nombre} asignó '{tarea}' a {persona}")

luis = Programador("Luis",9500,"Python")
luis.presentarse()
luis.codear()
print(luis.calcular_sueldo())

equipo = ["Pedro","Ana"]
maria = Gerente("Maria",15000,equipo)
maria.presentarse()
maria.asignar_tarea(equipo[0],"Setup del Servidor")