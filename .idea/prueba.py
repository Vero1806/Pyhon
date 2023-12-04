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