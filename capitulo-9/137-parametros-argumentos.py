def saludar(nombre): # Parametro
    print(f"Hola, {nombre}, bienvenido")

saludar("Luis") # Argumento
saludar("María")

def calcular_imc(peso_kg, altura_m):
    imc = peso_kg / (altura_m ** 2)
    print(f" IMC: {imc:.2f}")

calcular_imc(70, 1.75)
calcular_imc(82, 1.80)