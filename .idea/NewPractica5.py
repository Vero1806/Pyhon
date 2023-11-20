
'''
Ejercicio 1: Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Que buen día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
'''

npalabras = {} #Diccionario con el numero de veces que se repiten las palabras y las palabras

fras = input("Escribe la oración")

frase = fras.lower() #ponemos todas las letras en minuscula

frasecortada = frase.split() #Separa la cadena por espacios

for palabra in frasecortada:

    if palabra in npalabras:
        npalabras[palabra] += 1 #Suma el contador si la palabra se repite
    else:
        npalabras[palabra] = 1 #Si no pone un 1 y ya


print(npalabras)

'''
Ejercicio2: Tenemos guardado en un diccionario los códigos morse corespondientes a cada caracter. Escribir un programa que lea una palabra y la muestre usando el código morse.
'''

codigo = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
}	

palabra = input("Introduce una palabra para leer en morse ")

mayus=palabra.upper()

#print(mayus)

for clave in mayus:
   if clave in codigo.keys():
       print(codigo[clave], end=" ")



#Ejercicio3: Basado en el ejercicio anterior: ahora nos pide un código morse donde cada letra está separada por espacios y nos da la cadena correspondiente.


codigo = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
}

palabra = input("Introduce el codigo morse de una palabra separado por espacios. ")

letras=palabra.split()

#print(letras)
cadena = " "

for valor in letras:
    for key,morse in codigo.items():
        if morse==valor:
            cadena = cadena + (key)


print(cadena)

'''
Ejercicio4: Supongamos un diccionario que contiene como clave el nombre de una persona y como valor una lista con todos sus "gustos". Hagamos un programa que agregue "gustos" a la persona:
Si la persona no existe, la agrega al diccionario
Si la persona existe y el gusto existe en su lista, no tiene ningún efecto.
Si la persona existe y el gusto no existe en su lista, agrega el gusto a la lista.
Se deja de pedir personas cuando introducimos el carácter "*".
'''


agenda = {'Pepe': ['patinar', 'nadar', 'fiesta'],
          'Juan': ['pizza', 'cine', 'tele']}

# print(agenda['Pepe']) comprobación

persona = ""

while persona != "*":

    persona = input("Para que persona de la lista ")

    if persona == "*":
        break

    gusto = input("Dime que gusto quieres agregar ")

    gustopersona = agenda.setdefault(persona, []) #variable lista que crea nombre y gusto y la introduce en agenda

    #print(type(gustopersona))

    if gusto in gustopersona:
        print(persona, "ya tiene el gusto", gusto, "en su lista")

    else:
        gustopersona.append(gusto)
        print("Se ha agregado el gusto", gusto, "a", persona)
        print(gustopersona)


print(agenda)

'''
Ejercicio5: Vamos a crear una lista de números y pedirle al usuario que ingrese un índice y nosotros mostraremos
el valor del índice mostrado manejando las excepciones pertinentes
'''

lista = [1,2,3,4,5,6,7,8,9,10]

try:
    indice = int(input("dime la posicion del valor que quieras ver "))
    print(lista[indice])
except IndexError:
    print("Error. La tabla es más pequeña que el número", indice)
except ValueError:
    print("Error: los indices de una lista no tienen decimales")


'''
Ejercicio6: Vamos a pedir al usuario que introduzca un número y vamos a intentar dividir 10 por el número introducido manejando 
las distintas excepciones que se pueden producir
'''

num = int(input("Introduce un número como divisor"))

try:
    resultado = 10 / num
    print(resultado)
except ValueError as e:
    print("El número ", num, "no es un entero. Error:", e)
except ZeroDivisionError as e:
    print("No se puede dividir entre cero. Error:", e)

'''
Ejercicio7: Vamos a crear un diccionario (pidiendo los valores por pantalla hasta introducir *) donde las claves son los nombres de los vinos y el valor una lista con la información sobre la denominación de origen, añada y precio. Después, hagamos un programa en que, dado el diccionario de vinos y una lista con un rango de precios [menorPrecio, mayorPrecio], nos devuelva una lista de los nombres, ordenados alfabéticamente de los vinos que estén en este rango de precios.
'''
vinos =  {}
lista = []
#print(vinos)
nombre=""
origen=""
añada=""
precio=""

print("Vamos a introducir los vinos en el diccionario. La ejecucion se parara cuando introduzcas *")
try:
    while True :
        nombre = input("Introduce el nombre del vino ")
        if nombre == "*":
            break
        origen = input("Introduce la denominación de origen ")
        if origen == "*":
            break
        añadastring = input("Introduce el año de fabricación del vino ")
        if añadastring == "*":
            break
        preciostring = input("Introduce el precio del vino.(Separa los decimales con .) ")
        if preciostring == "*":
            break

        añada = int(añadastring)
        precio = float(preciostring)

        listadatos = [origen,añada,precio]

        datos = vinos.setdefault(nombre, listadatos)

        if nombre in vinos:
            print("El vino ", nombre, "ya esta en la lista")

        else:
            listadatos.append(datos)
            print("Se han agregado los datos", listadatos, "al vino", nombre)


    print(vinos)

except ValueError as e:
    print("No has introducido un valor valido en la añada o en el precio. Error =", e)



print("Ahora vamos a buscar los vinos en el rango de precios que prefieras")
menorPrecio = float(input("Introduce la cantidad mínima que quieras gastarte.(Separa los decimales con .)"))
mayorPrecio = float(input("Introduce la cantidad máxima que quieras gastarte.(Separa los decimales con .)"))


for nombre, datos_lista in vinos.items():
    for datos in datos_lista:
        precio_vino = datos[2]
        if menorPrecio <= precio_vino <= mayorPrecio:
            nombres.append(nombre)

print(nombres.sort)


'''
Ejercicio08: Vamos a crear un programa que lea por teclado las temperaturas mínimas de los 3 primeros meses del año de distintas ciudades, de la forma dic = {'Londres': [3.4, 6.3, 10.5], 'Oslo': [-3.8, -5.0, 4.2], 'Rennes': [2.5, 3.1, 12.3]} y una vez obtenido el carácter de salida * nos devuelva:
- El valor medio de las temperaturas de cada ciudad (redondear a 2 decimales).
- El valor mínimo de las temperaturas de cada ciudad
- Una lista con la ciudad con la temperatura más baja y su valor
'''

'''
Ejercicio09
Vamos a crear un registro de eventos con un diccionario donde se registre el código del evento y después la fecha y hora, el tipo de evento (que solo acepte los valores normal o crítico), y el nombre). Después, mostrar un pequeño menú que permita al usuario:
 - Mostrar todos los eventos ordenados por fecha
 - Mostrar todos los eventos críticos
 - Buscar un evento: pedir el código por pantalla, imprimir toda la información y preguntarle al usuario si quiere además imprimir todos los eventos de ese día 
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

    #if eleccion == 1:
    # for clave, valor in eventos.items():


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
Ejercicio10
Pon un ejemplo para el que veas útil el empleo de diccionarios.
'''