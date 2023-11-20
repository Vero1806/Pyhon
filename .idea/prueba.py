

'''
Ejercicio09
Vamos a crear un registro de eventos con un diccionario donde se registre el código del evento
y después la fecha y hora, el tipo de evento (que solo acepte los valores normal o crítico), y el nombre).
Después, mostrar un pequeño menú que permita al usuario:
 - Mostrar todos los eventos ordenados por fecha
 - Mostrar todos los eventos críticos
 - Buscar un evento: pedir el código por pantalla, imprimir toda la información y preguntarle
 al usuario si quiere además imprimir todos los eventos de ese día
'''
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
    eleccion = int(input(" "))

    if eleccion == 1:
        for clave, valor in eventos.items():


    if eleccion == 2:
        for clave, valor in eventos.items():
            if valor[2] == False:  # La posición 2 de la tupla contiene el valor booleano
                fecha, hora, es_critico, descripcion = valor
                print("Códogo =",clave)
                print("Fecha =", fecha.strftime('%Y-%m-%d'))
                print("Hora =", hora.strftime('%H:%M'))
                print("Es crítico =", valor[2])
                print("Descripción =", descripcion)
                print()










'''
if tipo != "critico" or tipo != "normal":
    print("valo introducido para tipo de evento no valido")
    break
'''