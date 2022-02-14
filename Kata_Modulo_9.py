print ("\n\tEjercicio 1: Uso de funciones en Python")
def fuel(tank1, tank2, tank3):

    promedio = ((tank1+tank2+tank3)/3)

    return """\n\tInfomre de combustible
    
    - Tank_1: {0}
    - Tank_2: {1}
    - Tank_3: {2}
    - Promedio: {3}
    """.format(tank1,tank2,tank3,promedio)

print(fuel(10,20,100))

print ('-'*40)

def promedio(tank1,tank2,tank3):
    p= (tank1+tank2+tank3)/3
    return p

def report(tank1,tank2,tank3):
    return """\n\tInfomre de combustible
    
    - Tank_1: {0}
    - Tank_2: {1}
    - Tank_3: {2}
    - Promedio: {3}
    """.format(tank1,tank2,tank3,promedio(tank1,tank2,tank3))

print(report(50,60,90))

print ('-'*40)

print("\n\tEjercicio 2 trabajo de argumentos de palabra clave")

def report(launch, time, destino, tank1, tank2):
    return """
    \tReporte
    Lanzamiento: {}
    Tiempo de llegada: {}
    Destino: {}
    Nivel de combustible Tanque 1: {}%
    Nivel de combustible tanque 2: {}%
    """.format(launch,time,destino, tank1, tank2)

print (report("10:20","20 Hrs","Marte",20,100))
print ('-'*40)

def informe(destino, *time, **tank):
    return """
    \t Reporte New
    Lanzamiento: {1} en horas
    Destino: {0}
    Fuel: {2} %
    """.format(destino,sum(time),sum(tank.values()))

print (informe("Marte", 5,10,10,10, Tank_A=80, Tank_B=100))
print ('-'*40)

def informe_2(destino, *time, **tank):
    print( """
    \t Reporte New
    Lanzamiento: {1} en horas
    Destino: {0}
    Fuel: {2} %
    """.format(destino,sum(time),sum(tank.values())))
    for i, b in tank.items():
        print (i, "-",b,"%")
print (informe_2("Marte", 5,10,10,10, Tank_A=80, Tank_B=100, Tank_C=100))

