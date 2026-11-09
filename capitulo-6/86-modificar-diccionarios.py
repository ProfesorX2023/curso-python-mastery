usuario = {"nombre":"Luis","edad":30,"pais":"Guatemala"}

usuario["telefono"] = "25681234"
print(usuario)

usuario["edad"] = 31
print(usuario)

usuario.update({"telefono":"+502 4766 0639", "edad":32})
print(usuario)