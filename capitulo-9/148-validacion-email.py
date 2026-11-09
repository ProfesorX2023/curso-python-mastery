'''
emails =[
    "luis@fibonacci.com.gt", -> True
    "no-arroba"
    "doble@@arroba.com",
    "sin@dominio",
    "@dominio.com"
    "usuario@sinpunto"
]

crear una función que se llame es_valido(texto)
retornara Verdadero si es valido

for para que tome a todos los emails y diga cuales son validos
Hacer varios if con early return
'''

emails =[
    "luis@fibonacci.com.gt",
    "no-arroba",
    "doble@@arroba.com",
    "sin@dominio",
    "@dominio.com",
    "usuario@sinpunto"
]

def es_valido(texto):

    #antes de esto debe tener verificaciones
    #estas son if con early return
    if texto.count("@") != 1:
        return "No es un correo valido"
    nombre, dominio = texto.split("@")
    if not nombre or not dominio:
        return "No es un correo valido"
    if "." not in dominio:
        return "No es un correo valido"

    return "Es un correo valido"

for email in emails:
    print(email, es_valido(email))