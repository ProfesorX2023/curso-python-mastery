estudiantes =[
    {"nombre":"Luis", "nota":85, "aprobado": True},
    {"nombre":"María", "nota":92, "aprobado": True},
    {"nombre":"Pedro", "nota":55, "aprobado": False},
    {"nombre":"Ana", "nota":78, "aprobado": True},
]

for estudiante in estudiantes:
    estado = "✅" if estudiante["aprobado"] else "❌"
    print(f"{estado} {estudiante['nombre']:<10}{estudiante["nota"]:>5}")

aprobado = [e for e in estudiantes if e["aprobado"]]
print(f"\nAprobados: {len(aprobado)}")

promedio = sum(est["nota"] for est in estudiantes) / len(estudiantes)
print(f"Promedio: {promedio}")