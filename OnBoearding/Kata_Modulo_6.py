#Kata_Modulo_6

planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

def ejercicio_1 ():
    #Crear y usar listas
    print ("\nActualmente hay {} planetas en el sistema solar\n".format(len(planets)))
    planets.append('Pluton')

    print ("""
    Se agrega un elemento mas a la lista
    Quedando un total de {} elementos en la lista
    El elemento agregado es: {}
    """.format(len(planets),planets[8] ))    

def ejercicio_2 ():
    #Trabajando con datos de una lista
    planets.pop()
    name = input("Ingresa el nombre de un planeta, iniciando con una letra mayuscula: ")

    search = planets.index(name)
    print("Los planetas mas cercanos al sol con referencia a '{}' son: ".format(name),planets[:search])
    print ("Los planetas mas alejados con referencia a '{}' son: ".format(name), planets[search+1:])

ejercicio_1()
ejercicio_2()