<<<<<<< Updated upstream
import collections

nums = [1, 2, 3]
# creating deque collection from the list
deque = collections.deque(nums)

print(deque)

# adding an element at the end
deque.append(4)

print(deque)

# adding element at the starting
deque.appendleft(0)

print(deque)

# removing the element at the end
deque.pop()

print(deque)

# removing element at the starting


print(deque)


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
=======
import datetime
import time

eventos = {"EV14.2": (datetime.datetime(2024,2,20), datetime.time(12,00), True, "Eleciones"),
           "EV12.1": (datetime.datetime(2024,1,15), datetime.time(16,00), False, "Clase online"),
           "EV16.3": (datetime.datetime(2024,3,16), datetime.time(20,00), False, "Reunión")}

print(eventos)

while True:
    print("----------Menú----------")
    print("1. Eventos ordenados por fechas")
    print("2. Todos los eventos crítcos")
    print("3. Buscar un evento por su códgo")
    print("0 = Salir ")
    eleccion = int(input(""))

    if eleccion == 1:
        # eventos_ordenados = {clave: eventos[clave] for clave in sorted(eventos)} #ordena eventos por clave
        eventos_ordenados = {clave: fecha for clave, fecha in sorted(eventos.items(), key=lambda item: item[1][0])}
        # formula que cambia la primera sentencia para que el valor de ordenación sea la fecha
        for clave, valor in eventos_ordenados.items():
            fecha, hora, es_critico, descripcion = valor
            print("Códogo =",clave)
            print("Fecha =", fecha.strftime('%Y-%m-%d'))
            print("Hora =", hora.strftime('%H:%M'))
            print("Es crítico =", valor[2])
            print("Descripción =", descripcion)
            print()


    if eleccion == 2:
        for clave, valor in eventos.items(): #recorre el diccionario con clave y valor
            if valor[2] == True:  # La posición 2 de la tupla contiene el valor booleano
                fecha, hora, es_critico, descripcion = valor
                #asignamos lo que esta dentro de diccionario a valor para recorrerlo e imprimirlo
                print("Códogo =",clave)
                print("Fecha =", fecha.strftime('%Y-%m-%d'))
                print("Hora =", hora.strftime('%H:%M'))
                print("Es crítico =", valor[2])
                print("Descripción =", descripcion)
                print()

    if eleccion == 3:
        cod = input("Introduce el código del evento que quieras ver")
        if cod in eventos.keys():
            fecha, hora, es_critico, descripcion = eventos[cod]
            print("Códogo =",cod)
            print("Fecha =", fecha.strftime('%Y-%m-%d'))
            print("Hora =", hora.strftime('%H:%M'))
            print("Es crítico =", es_critico)
            print("Descripción =", descripcion)
            print()
        else:
            print("El código", cod, "no existe")

    if eleccion == 0:
        print("Fin del programa")
        break
>>>>>>> Stashed changes
