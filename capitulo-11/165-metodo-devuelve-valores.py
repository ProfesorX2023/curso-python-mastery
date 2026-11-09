class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def es_cuadrado(self):
        return self.base == self.altura

    def __str__(self):
        return f"Area: {self.area()}\nPerimetro: {self.perimetro()}\nEs cuadrado: {self.es_cuadrado()}"

rectangulo1 = Rectangulo(5,2)
rectangulo2 = Rectangulo(5,5)

print(rectangulo1)
print(rectangulo2)