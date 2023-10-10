# Ejercicio 1: Escribe un programa que tome una cadena de texto ingresada por el usuario y muestre su longitud.
cadena = input("Escribe una cadena? ")

print(len(cadena))

# Ejercicio 2: Crea un programa que cuente la cantidad de vocales (a, e, i, o, u) en una cadena de texto.
cadenainicial = input("introduce una cadena ")

cadena = cadenainicial.lower()

a = cadena.count("a")
e = cadena.count("e")
i = cadena.count("i")
o = cadena.count("o")
u = cadena.count("u")

a1 = cadena.count("á")
e1 = cadena.count("é")
i1 = cadena.count("í")
o1 = cadena.count("ó")
u1 = cadena.count("ú")

u2 = cadena.count("ü")

print("Tu cadena tiene " ,(a+e+i+o+u) , " vocales")

# Ejercicio 3: Desarrolla un programa que tome una cadena de texto y muestre su reverso.
cadena = input("Dime una cadena para darle la vueta ")

print (cadena[::-1])

# Ejercicio 4: Escribe un programa que verifique si una cadena es un palíndromo.
palindromoinicial = input ("Escribe una cadena que del derecho y del revés sea igual ")

palindromo = palindromoinicial.lower()

prueba = palindromo[::-1]
#acortación de una función mayor. los 2 primeros puntos es el inicio, los 2 siguientes el final y el -1 el paso en negativo para darle la vuelta. https://aprendermarketing.es/3-formas-de-invertir-una-cadena-en-python/

if palindromo == prueba:
    print("La palabra", palindromo , "es un palíndromo")
else:
    print("La palabra", palindromo, "al darle la vuelta da", prueba, "por lo que no es un palíndromo")

# Ejercicio 5: Crea un programa que cuente la cantidad de palabras en una frase ingresada por el usuario.

frase = (input ("Dame una frase"))
varible=frase.split() #convierte en list de palabras separadas

print("Tu frase tiene" , len(varible), "palabras")
#len cuenta los elementos de la lista

# Ejercicio 6: Desarrolla un programa que muestre los números pares e impares en un rango específico especificado por un númmero de inicio y otro de fin
# Ejercicio 6: Desarrolla un programa que muestre los números pares e impares en un rango específico especificado por un númmero de inicio y otro de fin

numero1 = int(input ("Dame un número de inicio "))
numero2 = int(input ("Dame un número de final "))
pares = list()
impares = list()

num = list(range(numero1, numero2+1)) #crea un lista con los números
#print (num) #comprobación
for num in num:
    if num%2 == 0:
        pares.append(num) #añade a la lista el num que pasa por el for
        #print(num , "es par")
    if num%2 != 0:
        impares.append(num)
        #print(num , "es impar")

# Ejercicio 7: Crea una calculadora básica que realice operaciones de suma, resta, multiplicación y división.

while True:
    numero1 = int(input("primer número "))

    operacion = int(input ("Que operación quieres hacer? "
                           "1 - suma"
                           "2- resta"
                           "3- multiplicación "
                           "4-división "))

    if operacion == 1:
        numero2 = int(input ("segundo número "))
        print("la suma es" , numero1+numero2)
        break
    if operacion == 2:
        numero2 = int(input ("segundo número "))
        print("la resta es" , numero1-numero2)
        break
    if operacion == 3:
        numero2 = int(input ("segundo número "))
        print("la multiplicación es" , numero1*numero2)
        break
    if operacion == 4:
        numero2 = int(input ("segundo número "))
        print("la división es" , numero1/numero2)
        break
    else: print ("operación no valida")
# Ejercicio 8: Crea un programa que devuelva la tabla de multiplicar (del 1 al 10) de un número introducido por el usuario

# Ejercicio 9: Crea un juego de adivinanza de números donde el programa orienta al jugador diciéndole mayor o menor. Dispondrá de 5 intentos para adivinar
# y recibirá diferentes mensajes según si acierta a la primera o en el último intento o si directamente no acierta

# Ejercicio 10: Crea un programa que valide si la contraseña es segura (al menos 8 caracteres, contener letras mayúsculas y minúsculas, y al menos un número)
# y que de solo tres oportunidades para lograrlo

# BOLA EXTRA: Programa el juego del ahorcado