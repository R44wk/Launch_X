# Ejercicio 1 Creacion de un bucle "while"

new_planet = ' '
planets = []

print ("\n\tEjercicio 1: Uso de ciclos while en Python\n")

while new_planet.capitalize() != 'Done':
    new_planet = input("-> Ingresa un nombre de planeta o 'done' si has terminado de ingresar datos-[~$]: ")
    if new_planet == '':
        print("\n\tNo ingresaste datos! Intentalo de nuevo\n")            
    else:            
        planets.append(new_planet)
planets.pop()
    #print (planets)
# Ejercicio 1 Creacion de un bucle "while"
print ("\n\tEjercicio 2: Creacion de un ciclo \"for\"\n")

print("\nLos datos ingresados son: \n")
for i in planets:
    print("- ",i)