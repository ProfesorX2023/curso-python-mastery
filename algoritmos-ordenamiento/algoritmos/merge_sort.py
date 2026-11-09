from algoritmos.base import Ordenamiento

class MergeSort(Ordenamiento):
    def __init__(self):
        super().__init__("Merge sort")

    def _ordenar(self,a):
        if len(a) <=1:
            return a[:]

        medio = len(a) // 2
        izq_ordenada = self._ordenar(a[:medio])
        der_ordenada = self._ordenar(a[medio:])
        return self.mezclar(izq_ordenada, der_ordenada)

    def mezclar(self, izquierda, derecha):
        resultado = []
        i = j = 0
        while i < len(izquierda) and j < len(derecha):
            if self.es_mayor(izquierda[i],derecha[j]):
                resultado.append(derecha[j])
                j += 1
            else:
                resultado.append(izquierda[i])
                i += 1
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado