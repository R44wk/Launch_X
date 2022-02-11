"""
Kata_Modulo_5

Ejercicio 1 Utilizar operadores aritmeticos
Escenario: Crear un programa para calcular la distancia entre planetas
Imagina que estás creando un programa para calcular la distancia entre planetas. 
El programa permite a un usuario ingresar las distancias de dos planetas desde el sol, y calcula la distancia entre esos dos planetas.
Además, deseas proporcionar la distancia tanto en millas como en kilómetros."""

def ej_1():
    tierra = 149597870 # in km
    jupiter = 778547200

    dif = jupiter-tierra
    print("""La distancia que hay entre la Tierra y jupiter es de: 
    -> {1} Millas
    -> {0} Kms  """
    .format(dif,dif*0.621,))

def ej_2():
    """
Ejercicio 2 convierte strings en numeros y valor absoluto
Para crear nuestra aplicación, queremos leer la distancia del sol para dos planetas, 
y luego mostrar la distancia entre los planetas. Haremos esto usando input para leer los valores,
int para convertir a entero y luego abs para convertir el resultado en su valor absoluto.

"""

    planetA = int(input("\nIngresa la distancia del planeta 1 (Kms): "))
    planetB = int(input("\nIngresa la distancia del planeta 2 (Kms): "))

    distancia = abs(planetB-planetA)

    print ("\nLa distancia entre los dos planetas es: {} Kms".format(distancia))
    print ("\nLa distancia entre los dos planetas es: {} Millas\n".format(distancia*.621))

ej_1()
ej_2()