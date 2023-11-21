'''
1)
Elaborar unn algoritmo que actúe como un generador de contraseñas aleatorio.
El usuario podrá elegir entre las siguientes características de la contraseña:
- Longitud: podrá elegir cualquier valor que esté entre 6 y 20
- Si contiene: mayúsculas y/o números y/o símbolos
'''

import random
import string

print("----------Menú del Generador de contraseñas ----------")
longitud = int(input("1. logitud de la contraseña: "
                     "introduce la cantidad de digitos que va a tener (de 6 a 20 caracteres) "))
mayusculas = input("2. ¿Le ponemos mayusculas a la contraseña? Si o No ")
numeros = input("3. ¿Le ponemos números a la contraseña? Si o No ")
simbolos = input("4. ¿Le ponemos simbolos a la contraseña? Si o No ")

may_mayus=mayusculas.upper()
num_mayus=numeros.upper()
sim_mayus=simbolos.upper()

if longitud>5 and longitud<21 and may_mayus == "SI" and num_mayus == "NO" and sim_mayus == "NO":

    letras = string.ascii_letters
    mayus_minima = random.choice(string.ascii_uppercase) #Elige una letra y la pone en mayuscula

    contra_letras = ''.join(random.choice(letras) for _ in range(longitud-1))
    contra_mayus_minus = contra_letras+mayus_minima
    # Genera una cadena aleatoria de la longitud seleccionada
    print(contra_mayus_minus)

if longitud>5 and longitud<21 and may_mayus == "NO" and num_mayus == "SI" and sim_mayus == "NO":
    numero_aleatorio = random.randint(10000000000000000000,99999999999999999999)
    contra_num = str(numero_aleatorio)[:longitud] # Convierte el número a cadena y acota la longitud a 3 dígitos
    print(contra_num)

if longitud>5 and longitud<21 and may_mayus == "NO" and num_mayus == "NO" and sim_mayus == "SI":
    numero_aleatorio = random.randint(10000000000000000000,99999999999999999999)
    contra_num = str(numero_aleatorio)[:longitud-2]
    lista_simbolos = ["!","@","#","$","%","&","*"]
    simbolo_aleatorio1 = random.choice(lista_simbolos)
    simbolo_aleatorio2 = random.choice(lista_simbolos)
    contra_simbolos = simbolo_aleatorio1 + contra_num + simbolo_aleatorio2
    print(contra_simbolos)
'''
2)
Desarrollar un algoritmo que haga la función del sombrero seleccionador de Harry Potter. El sombrero realizará 3 preguntas al candidato y cada pregunta tendrá 4 respuestas posibles.
El candidato elegirá una respuesta a esas tres preguntas y en función de las respuestas, el algoritmo elegirá a qué casa pertenece (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
'''