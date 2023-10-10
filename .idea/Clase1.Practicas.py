#Ejercicio 1
#Escribir un programa que pregunte al usuario su nombre, y luego lo salude.
nombre = input("¿Cual es tú nombre?")
print("Hola", nombre)


#Ejercicio 2
#Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float (input("¿Cual es la base del rectangulo?"))
altura = float (input("¿Y su altura?"))

print("El perimetro es", base, "+", base, "+", altura, "+", altura, "=", (base*2+altura*2))
print("Y el area es", base, "x", altura, "=", (base*altura))

#Ejercicio 3
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cateto1 = float (input("¿Cual es el primer cateto?"))
cateto2 = float (input("¿Y el segundo?"))

resultado = (cateto1**2) + (cateto2**2)
newResultado = resultado**0.5

print("la raiz cuadrada de la suma de los cuadrados de los catetos ", cateto1, "y", cateto2, "es igual a", newResultado)

#Ejercicio 4
#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

while True:
    num1 = float (input("¿Cual es el primer número?"))
    num2 = float (input("¿Y el segundo?"))
    if num2 == 0 :
        print("Número no valido. No se puede dividir por 0")
    if num2 != 0 :
        break


print("la suma de", num1, "y", num2, "es", num1+num2)
print("la resta de", num1, "y", num2, "es", num1-num2)
print("la división de", num1, "y", num2, "es", num1/num2)
print("la multiplicación de", num1, "y", num2, "es", num1*num2)


#Ejercicio 5
#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. La fórmula para la conversión es: C = (F-32)*5/9

fahren = float (input("¿Cuantos grados Fahrenheit quieres convertir a Cersius?"))

cels = round((fahren-32)*5/9)

print(fahren, "grados Fahrenheit aproximadamente unos", cels, "grados Cersius")


#Ejercicio 6
#Calcular la media de tres números pedidos por teclado.

n1 = float (input("¿Cual es el primer número?"))
n2 = float (input("¿Y el segundo?"))
n3 = float (input("¿Y el tercero"))

print ("La media de", n1, "," , n2, "y" , n3, "es igual a", (n1+n2+n3)/2)

#Ejercicio 7
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = int (input("¿Cuantos minutos quieres pasar a horas?"))

horas = int(minutos/60)
newMinitos = minutos%60


print(minutos, "minutos es igual a", horas, "horas y", newMinitos, "minutos")

#Ejercicio 8
#Dado un número de dos cifras, diseña un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

while True:
    vertido: str = input("¿Introduce un número de 2 cifras?")
    if len(vertido) != 2:
        print ("Número no valido")
    if len(vertido) == 2:
        break
invertido = vertido[1] + vertido [0]
print(invertido)

#Ejercicio 9
#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.


a = int (input("Introduce la variable A "))
b = int (input("Introduce la variable B "))
print("Has introducido que A =", a, "y B =", b )
c = a
a = b
b = c
print("Ahora: A =", a, "y B =", b )

#Ejercicio 10
#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un
#algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y
#mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.


while True:
    v1 = float (input("Introduce la velocidad del vehículo 1 en Km/h "))
    v2 = float (input("Introduce la velocidad de vehículo 2 en Km/h "))
    dist = float (input("¿Qué distancia hay entre ellos en Km? "))
    if v2 > v1 and dist != 0.0:
        tiempoDeci = dist / (v2-v1)
        tiempoMinut = int(tiempoDeci*360)
        print("El vehiculo 1 tardara en alcanzar al 2", tiempoMinut, "minutos")
        break
    elif dist == 0:
        print("El vehiculo 1 y el vehículo 2 están en el mismo lugar")
        break
    else:
        print ("Datos erroneos. El vehículo 1 tiene que ser más lento que el vehículo 2")



#Ejercicio 11
#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El
#tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.


horas= int (input("Introduce las hora a la que sale el ciclista de la ciudad A"))
minutos= int (input("En que minuto?"))
segundos= int (input("En que segundo?"))
disTiempo= int (input("A cuantos segundos está la ciudad B?"))

sg = disTiempo+segundos
mint = int(sg/60+minutos)

if sg>60 and mint<60: # calculo si los minutos no llegan a sumar una hora
    mint = int(sg/60+minutos)
    sg = int (sg%60)
    print(" El ciclista llegará a la ciudad B a las", horas, "y ", mint, "minutos y ", sg, "segundos")

if mint>60: # calculo de horas
    mint = int(sg/60+minutos)
    sg = int (sg%60)
    hor = int(mint/60+horas)
    mint = int(mint%60)
    print(" El ciclista llegará a la ciudad B a las", hor, "y ", mint, "minutos y ", sg, "segundos")

else:
    print(" El ciclista llegará a la ciudad B a las", horas, "y ", minutos, "minutos y ", sg, "segundos")


#Ejercicio 12
#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Cual es tu nombre?")
apellido1 = input("Cual es tu primer apellido?")
apellido2 = input("Cual es tu segundo apellido?")

iniciales = nombre[0]+ "." + apellido1[0] + "." + apellido2[0]+ "."

print("Tus iniciales son", iniciales.upper())

#Ejercicio 13
#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que:
#por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en
#blanco 0. Imprime el resultado obtenido por el estudiante.


#Opción 1:
correctas = int(input("¿Cuantas respuestas a acertado? "))
incorrectas = int(input("¿Cuantas respuestas a fallado? "))
#blanco = int(input("¿Cuantas respuestas a dejado en blanco? ")) No es necesario

print("El alumno a optenido ", correctas*5-incorrectas, "puntos")

#Opción 2:
pregunta=1
notafinal = 0
for preguta in range (10):
    respuesta = input ("Esta correcta la pregunta número "+str(pregunta)+" ? S, N o B ")
    if respuesta == "S":
        notafinal = notafinal +5
    if  respuesta == "N":
        notafinal = notafinal -1
    if  respuesta == "B":
        notafinal = notafinal
    pregunta = pregunta+1

print ("El alumno a optenido", notafinal, "puntos en el examen")


#Ejercicio 14
#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
#después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20
#céntimos o 10 céntimos).

dosEuros = int(input("Cuantas monedas de 2 € tienes? "))
unEuro = int(input("Cuantas monedas de 1 € tienes? "))
cincuentaCentimos = int(input("Cuantas monedas de 0.50 € tienes? "))
veinteCentimos = int(input("Cuantas monedas de 0.20 € tienes? "))
diezCentimos = int(input("Cuantas monedas de 0.10 € tienes? "))

centimosTotales = int (cincuentaCentimos*50+veinteCentimos*20+diezCentimos*10)%100
centimosAeuros = int((cincuentaCentimos*50+veinteCentimos*20+diezCentimos*10)/100)

EurosTotales = dosEuros*2+unEuro+centimosAeuros

print("Tienes", EurosTotales, "Euros con", centimosTotales, "céntimos")