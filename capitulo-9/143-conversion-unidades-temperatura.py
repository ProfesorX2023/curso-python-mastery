# Crea dos funciones: una que convierte de Celcius a Fehrenheit
# otra que haga lo inverso

# fahrenheit a celcius -> return

# celcius a fahrenheit -> return

# print para mostrar ambos o dos prints

# input que reciba en una variable: grados = float(input(...
# llamar a funcion con la variable como parametro

def temperaturas(celcius):
    return f"su temperatura ingresada en celcius equivale a: {celcius * 1.8 + 32} grados de farenheit"

cel = temperaturas(int(input("ingrese su temperatura en celcius: ")))

def temperaturas2(farenheit):
     return f"su temperatura ingresada en farenheit equivale a: {(farenheit - 32)*5/9} grados de celcius"

far = temperaturas2(int(input("ingrese su temperatura en farenheit: ")))



print("farenheit: ", far)
print("celcius: ", cel)