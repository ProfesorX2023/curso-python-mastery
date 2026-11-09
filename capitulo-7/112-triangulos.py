lado_1 = int(input("Digite el primer lado: "))
lado_2 = int(input("Digite el segundo lado: "))
lado_3 = int(input("Digite el tercer lado: "))

if lado_1 <= (lado_2+lado_3) and lado_2 <= (lado_3+lado_1) and lado_3 <= (lado_1+lado_2):
    print("✅ Perfecto!, tenemos un triángulo!")
    if lado_1 == lado_2 == lado_3:
        print("Triángulo equilatero")
    elif lado_1 != lado_2 != lado_3:
        print("Triangulo escaleno")
    else:
        print("Triangulo isoceles")
else:
    print("🤔❌, parece que los lados no correponden a un triángulo")