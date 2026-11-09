edad = int(input("Digite su edad: "))

if edad >= 18:
    pais = input("PAIS (GT/US/EU)").upper().strip()
    if pais == "GT":
        print("Eres elegible para votar en Guatemala")
    elif pais == "US":
        print("Eres elegible para votar en USA")
    elif pais == "EU":
        print("Eres elegible para votar en la Unión Europea")
    else:
        print("Revisa las leyes de tu pais")
else:
    print("Aun no puede votar")