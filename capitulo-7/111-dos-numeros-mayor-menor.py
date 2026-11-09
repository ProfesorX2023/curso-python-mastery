numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

resultado = f"{numero1} mayor que numero {numero2}" if numero1 > numero2 else  f"{numero1} menor que numero {numero2}" if numero1 < numero2 else f"{numero1} igual a {numero2}"
print(resultado)