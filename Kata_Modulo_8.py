print ("\n\tEjercicio 1 Creacion de un diccionario de python\n")

planet = {
    "name": 'Mars',
    'moons': 2
    }
print ("Planet:", planet.get("name"), "\tMoons:", planet.get("moons"))

planet.update({"circunferencia (Km)": {"polar":6752, "equatoria":6792}})

#print (planet)
print ("\nPLaneta:",planet["name"], "Circunferencia polar:",planet["circunferencia (Km)"]["polar"])

print ("\n\tEjercicio 2 Programacion dinamica con diccionarios\n")

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planet_moons.values()
planets = len(planet_moons)

#print (moons)
#print (planets)

total = 0
for i in moons:
    total = i+total

print ("\nEl promedio de lunas en el sistema solar es de: {:1.1f}\n".format(total/planets))
