ciudades = [
    ("Guatemala", 14.6349, -90.5069),
    ("Antigua", 14.5586, -90.7339),
    ("Quetzaltenango", 14.8347, -91.5181),
    ("Coban", 15.4730, -90.3779)
]

print(f"{'CIUDAD':<20}{'LAT':>10}{'LON':>10}")
print("-" * 40)
for nombre, lat, lon in ciudades:
    print(f"{nombre:<20}{lat:>10.2f}{lon:>10.2f}")