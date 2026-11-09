import json

#Diccionario a string JSON
usuario = {"nombre":"Luis","edad":30,"activo":True}
texto_json = json.dumps(usuario, indent=2)
print(texto_json)

#string JSON a Diccionario

crudo = '{"nombre":"Maria","edad":25}'
parsed = json.loads(crudo)
print(parsed)

with open("datos.json","w") as f:
    json.dump(usuario,f,indent=3)

with open("datos.json","r") as f:
    cargado = json.load(f)

print(cargado)