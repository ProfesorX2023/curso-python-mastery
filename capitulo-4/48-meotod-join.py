palabras = ['Python', 'es', 'genial']
frase = " ".join(palabras)
print(frase)

partes = ["2026","01","15"]
fecha = "-".join(partes)
print(fecha)

emails = ["luis@mail.com","maria@mail.com","carlos@mail.com"]
lista_emails = ", ".join(emails)
print(lista_emails)

numeros = [1,2,3,4,5]
lista_numeros = ", ".join(str(n) for n in numeros)
print(lista_numeros)