#Filtro
pares = [n for n in range(21) if n %  2 == 0]
print(pares)

nombre = ["luis","maría","pedro"]

#transoformación
capitalizados = [n.title() for n in nombre]
print(capitalizados)

#filtrado y transformación
notas = [60,72,85,90,55,78]
aprobados = [n for n in notas if n >= 60]
print(aprobados)

expresiones = ["5+2*6","10*9-20","-50+6*1+10"]
resultados = [eval(n) for n in expresiones if eval(n) < 0]
print(resultados)

aprobados = ["Aprobado" if n >= 60 else "Repdobado" for n in notas]
print(aprobados)