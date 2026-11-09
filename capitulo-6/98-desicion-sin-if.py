#Preguntar una edad
#Decidir: (No utilizaremos if ni for)
#Puede beber
#puede entrar
#Tiene entrada gratis
#A una discoteca
#18 pueden beber, puede entrar
#30 no pueden entrar a discotecas
#20 y 25 tienen entrada gratis
#Flujo: preguntar edad -> Escribir las tres respuestas
#edad >= 18 - True o False -> print

edad = int(input("Ingrese su edad: "))

puede_beber = edad >=18
puede_entrar = edad>=18 and edad<30
entrada_gratis = edad == 20 or edad == 25
respuestas = {True:"Si",False:"No"}

print(f"Puede beber? {respuestas[puede_beber]}")
print(f"Puede Entrar? {respuestas[puede_entrar]}")
print(f"Tiene entrada grátis? {respuestas[entrada_gratis]}")