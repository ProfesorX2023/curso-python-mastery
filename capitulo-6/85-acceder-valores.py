usuario = {"nombre":"Luis","edad":30,"pais":"Guatemala"}

print(usuario["nombre"])
print(usuario["edad"])
#print(usuario["telefono"])

print(usuario.get("telefono"))
print(usuario.get("pais"))
print(usuario.get("telefono","N/A"))