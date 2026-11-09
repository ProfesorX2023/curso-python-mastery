notas = [85,45,72,90,55,78,60,92,38,70]

promedio = sum(notas) / len(notas)
mas_alta = max(notas)
mas_baja = min(notas)
aprobados = [n for n in notas if n>=60]
reprobados = [n for n in notas if n <60]

print(f"✅Notas: {notas}")
print(f"✅Promedio: {promedio:.2f}")
print(f"✅Mas alta: {mas_alta}")
print(f"✅Mas Baja: {mas_baja}")
print(f"✅Cantidad de Notas: {len(notas)}")
print(f"✅Aprobados: {len(aprobados)}: {aprobados}")
print(f"✅Reprobados: {len(reprobados)}: {reprobados}")