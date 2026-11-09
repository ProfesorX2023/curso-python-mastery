import random

PALABRAS =[
    "python","fibonacci","guatemala","programacion",
    "computadora","diccionario","variable","funcion",
    "academia","algoritmo","internet","telescopio"
]

DIBUJOS = [
    r'''
  +---+
  |   |
      |
      |
      |
      |
========= ''',
    r'''
  +---+
  |   |
  O   |
      |
      |
      |
========= ''',
    r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
========= ''',
    r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========= ''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= ''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= ''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= '''
]

print("="*45)
print("\t\t\tEL JUEGO DEL AHORCADO")
print("\t\t\tAcademia Fibonacci")
print("="*45)

palabra = random.choice(PALABRAS)
letras_adivinadas = set()
letras_intentadas = set()
errores = 0
MAX_ERRORES = 6
gano = False

while errores < MAX_ERRORES:
    print(DIBUJOS[errores])

    estado = " ".join(c if c in letras_adivinadas else "_ " for c in palabra)
    print(f"\nPalabra: {estado}")
    print(f"Letras usadas: {' '.join(sorted(letras_intentadas)) or '(ninguna)'}")
    print(f"Errores: {errores} de {MAX_ERRORES} errores")

    if set(palabra) <= letras_adivinadas:
        gano = True
        break

    letra = input("\nElige una letra: ").lower().strip()

    if len(letra) != 1 or not letra.isalpha():
        print(" -> tiene que ser una sola letra")
        continue

    if letra in letras_intentadas:
        print(f" -> Ya intentaste '{letra}'")
        continue

    letras_intentadas.add(letra)

    if letra in palabra:
        letras_adivinadas.add(letra)
        ocurrencie = palabra.count(letra)
        print(f" -> ¡Bien! la letra '{letra}' aparece {ocurrencie} vez(es)")
    else:
        errores += 1
        print(f" -> La Leta '{letra}' no está en la palabra")

print("\n" + "="*45)
if gano:
    print("*** ¡GANASTE! ***")
    print(f"La palabra era: {palabra.upper()}")
    print(f"Te quedaron {MAX_ERRORES - errores} errores disponibles")

else:
    print(DIBUJOS[errores])
    print("\n*** TE AH"
          "++++++++++++++++++ORCASTE :( ***")
    print(f"La palabra era: {palabra.upper()}")
print("="*45)

# 🖤🖤️❤️❤️❤️