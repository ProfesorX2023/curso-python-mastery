persona = ("Luis",30,"Guatemala","Desarrollador")

print(persona[0])
print(persona[-1])
print(persona[1:3])
print(len(persona))

#persona[0] = "Maria" -> Esto no se puede hacer

nueva_persona = ("Maria",) + persona[1:]
print(nueva_persona)