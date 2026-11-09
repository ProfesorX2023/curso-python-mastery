# 1,1,2,3,5,8,13,21,34,
# phi
lista = []
def fibonacci(n):

    global lista
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

# O(2^n)

lista = [fibonacci(n) for n in range(20)]
print(lista)