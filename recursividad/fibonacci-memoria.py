def fibonacci_memo(n, memoria=None):
    '''Versión con memoriaL guardar los resultados
    ya calculados para no repertirlos. De O(2^n) a O(n)'''

    if memoria is None:
        memoria = {}

    if n <= 1:
        return n

    if n in memoria:
        return memoria[n]

    memoria[n] = fibonacci_memo(n-1, memoria) + fibonacci_memo(n-2, memoria)

    return memoria[n]

print([fibonacci_memo(i) for i in range(100)])

# O(2^n)