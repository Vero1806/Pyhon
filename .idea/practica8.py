#1 Realizar un esquema con los 5 módulos (distintos a los que hemos visto aquí)
# que son más usados/útiles en python,
# explica para qué se usan y
# las funciones principales para familiarizarnos con ellos

# import collections
    #Es un módulo que mejoras las funciones de las tuplas y listas sumando más funcionalidades. Por ejemplo:
        #.appendleft() // agrega un valor a la derecha en una lista
        #.popleft() // borra un valor a la derecha de la lista
        #.Counter() // cuenta la cantidad de elementos dentro de una lista
        #.defaultdict() // especifica un valor predeterminado para nuevas clases cuando trabajamos con diccionarios
        #.OrderedDict() // mantiene el orden de la inserción de las claves en los diccionarios.

#import requests

#2 Calculadora de fracciones
#Usando el módulo Fractions, crea un programa que permita hacer
# las operaciones básicas con fracciones,
# escribiéndolas en la notación que solemos usar cuando las escribimos

import fractions


while True:
    print("-------Menú de Calculadora de Fracciones--------")
    print("Qué operacion quieres realizar")
    print("1. Sumar fracciones")
    print("2. Restar fracciones")
    print("3. Multiplicar fracciones")
    print("4. Dividir fracciones")
    print("0. Salir")
    eleccion = int(input(" "))


    try:
        if eleccion == 0:
            print("Hasta la próxima.")
            exit()

        if eleccion not in range(0,5):
            print("Error. Esa opción no es valida")
            continue
        else:

            print("Fracción 1")
            fraccion1 = fractions.Fraction(input("Dime el dominador y el denominador separado por 1 barra . Ej: 2/3 "))
            print("Fracción 2")
            fraccion2 = fractions.Fraction(input("Dime el dominador y el denominador separado por 1 barra . Ej: 3/4 "))

            if eleccion == 1:
                suma = fraccion1+fraccion2
                print("la suma de", fraccion1, "y", fraccion2, "es:", suma)


            if eleccion == 2:
                resta = fraccion1-fraccion2
                print("la resta de", fraccion1, "y", fraccion2, "es:", resta)

            if eleccion == 3:
                multi = fraccion1*fraccion2
                print("la multiplicación de", fraccion1, "y", fraccion2, "es:", multi)


            if eleccion == 4:
                div = fraccion1/fraccion2
                print("la división de", fraccion1, "y", fraccion2, "es:", div)





    except ZeroDivisionError as e:
        print("Estas intentado dividir por 0. Error:", e)
        continue
    except ValueError as e:
        print("El valor introducido no es correcto. Error =", e)
        continue

    while True:
        continuar = input("¿Desea continuar operado? Si o No ")
        continuarMayus = continuar.upper()
        if continuarMayus == "SI":
            break
        if continuarMayus == "NO":
            print("Hasta la próxima")
            exit()
        else:
            print("El valor intrudido no es correcto. Responda Si o No")


#3: Formatear una Fecha
#Escribe un programa que tome la fecha actual y
# pida al usuario en qué formato quiere imprimirla y
# se la devuelva en el mismo, utilizando el formato datetime.

import datetime

fechaCompleta = datetime.datetime.now()
print(fechaCompleta)


while True:
    print("-------Menú de formato de Fechas--------")
    print("¿En qué formato quieres mostrar la fecha?")
    print("1. Solo fecha")
    print("2. Solo hora")
    print("3. Fecha y hora")
    print("4. Hora formato am/pm")
    print("0. Salir")
    eleccion = int(input(" "))

    try:
        if eleccion == 0:
            print("Hasta la próxima.")
            exit()

        if eleccion not in range(0,5):
            print("Error. Esa opción no es valida")
            continue
        else:

            if eleccion == 1:
                print(fechaCompleta.strftime("Hoy es %d de %B del año %Y"))

            if eleccion == 2:
                print(fechaCompleta.strftime("%H:%M:%S"))

            if eleccion == 3:
                print(fechaCompleta.strftime("%d-%m-%Y %H:%M:%S"))

            if eleccion == 4:
                print(fechaCompleta.strftime("Son las %I:%M:%S %p"))


    except ValueError as e:
        print("El valor introducido no es correcto. Error =", e)
        continue


#4: Tamaño de los archivos. Vamos a crear un programa que solicite al usuario una extensión de archivo (por ejemplo, ".txt", ".pdf", ".jpg"),
# entonces debe buscar todos los archivos con esa extensión haya en un directorio específico utilizando el módulo os y
# calcular el tamaño total ocupado por esos archivos. Si terminamos, añadir funcionalidad
# a este programa para calcular espacios en el disco, explorando las diferentes opciones del módulo OS.

