#Ejercicio1
# Crea una lista e inicalizala con 5 cadenas de caracteres leídas por teclado.
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra
# sus elementos  por la pantalla.

c1 = input ("Dame el primer valor de la lista \n")
c2 = input ("Dame el segundo valor de la lista \n")
c3 = input ("Dame el tercer valor de la lista \n")
c4 = input ("Dame el cuarto valor de la lista \n")
c5 = input ("Dame el quinto valor de la lista \n")

lista = [c1,c2,c3,c4,c5]
print("La lista has introducido es \n" , lista)
#listainversa = lista [::-1]
lista.reverse()

print("Y ahora la invertimos \n" , lista)


#Ejercicio2
# Escribe un programa que multiplique todos los números en una lista y muestre el resultado.

lista2 = [1,2,3,4,5]
mul = 1

for i in lista2: # forma con bucle
    mul = mul*i
    print(mul)

multiplicacion = lista2 [0] * lista2 [1]* lista2 [2]* lista2 [3]* lista2 [4] #comprobación

print(multiplicacion, "y tambien", mul )

#Ejercicio3
# Programa que declare una lista y la vaya llenando de números hasta que
# introduzcamos un número negativo. Entonces se debe imprimir el vector
# (sólo los elementos introducidos).

lista3 = []

while (True):
    i = int(input("Introduce un valor a la lista \n"))
    lista3.append(i)

    if (i < 0):
        break

#print(lista3) comprobación

lista3.reverse() #da la vuelta e elimina el último valor que será el negativo
lista3.pop(0)
lista3.reverse()

print(lista3)


#Ejercicio4
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un
# alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas,
# la nota media, la nota más alta que ha sacado y la menor.

notas = []

while len(notas) < 5 :
    nota = int(input ("Dime que nota deseas introducir \n"))

    if nota not in range(1,11):
        print("esa nota no es valida")

    else:
        notas.append(nota)



suma = 0
for i in notas: # forma con bucle
    suma = suma+i
media = suma/5

print("Todas las notas", notas)
print("Nota media", media)
print("Nota máxima", max(notas))


#Ejercicio5
# Hacer un programa que inicialice una lista de números con valores aleatorios
# (10 valores), y posterior ordene los elementos de menor a mayor.
import random

valoresrandom= []

for numero in range (10):
    numero = random.randint(1,100)
    valoresrandom.append(numero)

#print(valoresrandom) comprobación

valoresrandom.sort()
print(valoresrandom)


#Ejercicio6
# Crea un programa que pida un número al usuario un número de mes
# (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30)
# y el nombre del mes. Para simplificarlo vamos
# a suponer que febrero tiene 28 días.

numero = int(input("Dame el numero del mes del mes que quieras mirar los días "))

matrizmeses = [['Enero',31],['Febrero',28],['Marzo',31],['Abril',30],['Mayo',31],['Junio',30],['Julio',31],['Agosto',31],['Septiembre',30],['Octubre',31],['Noviembre',30],['Dicembre',31]]

print(matrizmeses[numero-1])

#Ejercicio7
# Crear un programa que añada números a una lista hasta que introducimos un número negativo.
# A continuación debe crear una nueva lista igual que la anterior pero eliminando los
# números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

lista7 = []

while (True):
    i = int(input("Introduce un valor a la lista \n"))
    lista7.append(i)

    if (i < 0):
        break

#print(lista7) #comprobación

lista7.reverse() #da la vuelta e elimina el último valor que será el negativo
lista7.pop(0)
lista7.reverse()

#print(lista7) #comprobación

printlista = set(lista7) #set() es una coleccion de objetos únicos. Por lo que, al transformarla elimina los duplicarlos

print(printlista)


#Ejercicio8
# Queremos guardar los nombres y la edades de los alumnos de un curso.
# Realiza un programa que introduzca el nombre y la edad de cada alumno.
# El proceso de lectura de datos terminará cuando se introduzca como nombre
# un asterisco (*) Al finalizar se mostrar  los siguientes datos:
#  * Todos lo alumnos mayores de edad.
#  * Los alumnos mayores (los que tienen más edad)


#Ejercicio9
# Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol.
# Para ello vamos a utilizar dos tablas:
#
# * Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de
# los equipos de cada partido. El número de partidos de que se compone la jornada también lo pediremos
# * Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos
# columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna
#  de la tabla anterior, y en la segunda los goles del otro equipo.
#
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.


#Ejercicio10
# Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
# * Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# * Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
# * Eliminar: Me pide una cadena, y la elimina de la lista.
# * Mostrar: Muestra la lista de cadenas
# * Terminar

palabras = []

while (True) :
    palabra = input ("Dime que palabra quieres introducir \n Si dices NO dejaremos de añadir palabras a la lista")

    if palabra == "NO":
        break
    else:
        notas.append(nota)

print(palabras, "\n")
eleccion = int(input("Elige una de estas 3 opciones para operar con la lista \n 1.Contar \n 2.Modificar \n 3.Eliminar"))

if eleccion == 1:
    contar = input("Dime la cadena que quieres contar")
    print("El numero de veces que aparece la palabra", contar, "en la lista es", palabras.count(contar))

#if eleccion == 2:

#if eleccion == 3:


