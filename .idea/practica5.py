
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


agenda = {'Pepe':['patinar', 'nadar', 'fiesta'],
          'Juan':['pizza', 'cine', 'tele']}


#print(person['Pepe']) comprobación

persona = " "

while persona != "*":

    persona = input("Para que persona de la lista ")


    gusto = input("Dime que gusto quieres agregar ")



    if persona in agenda:
        agenda[persona].append(gusto)
        print("Se ha agregado el gusto", gusto, "a", persona,".")
        print(agenda)
    else:
        print(persona, "no se encuentra en la agenda.")
        print(agenda)


print(agenda)



'''
Ejercicio5: Vamos a crear una lista de números y pedirle al usuario que ingrese un índice y nosotros mostraremos 
el valor del índice mostrado manejando las excepciones pertinentes
'''


'''
Ejercicio6: Vamos a pedir al usuario que introduzca un número y vamos a intentar dividir 10 por el número introducido manejando 
las distintas excepciones que se pueden producir
'''

'''
Ejercicio7: Vamos a crear un diccionario (pidiendo los valores por pantalla hasta introducir *) donde las claves son los nombres de los vinos y el valor una lista con la información sobre la denominación de origen, añada y precio. Después, hagamos un programa en que, dado el diccionario de vinos y una lista con un rango de precios [menorPrecio, mayorPrecio], nos devuelva una lista de los nombres, ordenados alfabéticamente de los vinos que estén en este rango de precios.
'''

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

'''
Ejercicio10
Pon un ejemplo para el que veas útil el empleo de diccionarios.
'''