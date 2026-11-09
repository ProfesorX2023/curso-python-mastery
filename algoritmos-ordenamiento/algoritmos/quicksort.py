from algoritmos.base import Ordenamiento

class QuickSort(Ordenamiento):
    def __init__(self):
        super().__init__("Quick sort")

    def _ordenar(self,a):
        if len(a) <= 1:
            return a[:]

        pivote = a[-1]
        menores, iguales, mayores = [],[],[]
        for x in a:
            if self.es_mayor(pivote,x):
                menores.append(x)
            elif x == pivote:
                iguales.append(x)
            else:
                mayores.append(x)

        return self._ordenar(menores) + iguales + self._ordenar(mayores)
