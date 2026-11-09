#CONTROL DE DECIMALES {:.Nf}
#CONTROL DE PORCENTAJE {:.%f}
#CONTROL DE MILES {:,}
PI = 3.14159265389793

print(f"PI con 2 decimales es: {PI:.2f}")
print(f"PI con 4 decimales es: {PI:.4f}")
print(f"PI con 0 decimales es: {PI:.0f}")

precio = 1500
print(f"Precio: Q.{precio:.2f}")

descuento = 0.15
print(f"Descuento: {descuento:.0%}")
print(f"Descuento: {descuento:.2%}")

poblacion = 1700000000
deuda_total = 1500000

print(f"Poblacion: {poblacion:,}")
print(f"Deuda: {deuda_total:,.2f}")
