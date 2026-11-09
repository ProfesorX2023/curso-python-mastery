class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return self.base * self.altura

    @property
    def perimetro(self):
        return 2 * (self.altura + self.base)

rectanulo1 = Rectangulo(5, 3)
print(rectanulo1.area)
print(rectanulo1.perimetro)
