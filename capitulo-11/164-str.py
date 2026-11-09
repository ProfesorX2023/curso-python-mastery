class Producto:
    def __init__(self, nombre, precio, stock): #constructor de clase, para cerar objetos, para instanciar
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self): #metodo para imprimir el objeto - llamados dunders
        return f"{self.nombre} - (Q{self.precio:.2f}) - stock: {self.stock}"

producto1 = Producto("Laptop HP", 8500, 12)

print(producto1)