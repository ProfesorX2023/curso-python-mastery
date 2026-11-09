agenda = {
    "Luis":"+502 4766-0639",
    "María":"+502 5555-1234",
    "Pedro":"+502 4444-5678",
    "Ana":"+502 3333-9999"
}

nombre = input("Ingrese su nombre: ").strip().title()
telefono = agenda.get(nombre,"❌ No encontrado")
print(f"✅ {nombre}: {telefono}")

nuevo_nombre = input("Ingrese su nombre: ").strip().title()
nuevo_telefono = input("Ingrese su telefono: ").strip()
agenda[nuevo_nombre] = nuevo_telefono

print("\n💻 Agenda completa: ")
for n, t in sorted(agenda.items()):
    print(f"✅ {n}: {t}")