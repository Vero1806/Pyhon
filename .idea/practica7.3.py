# Función Intercambiar: Recibe dos números como parámetros de entrada y
#  devuelve los números ordenador de mayor a menor
# Parámetros de entrada: dos números
# Datos de salida: dos números

def Intercambiar (n1,n2):
    if n1 > n2:
        return n1,n2
    if n2 > n1:
        return n2,n1


# Función CalcularMCD: Recibe dos números y devuelve el MCD utilizando el método
# de Euclides. El método de Euclides es el siguiente:
#  * Se divide el número mayor entre el menor.
#  * Si la división es exacta, el divisor es el MCD.
#  * Si la división no es exacta, dividimos el divisor entre el resto obtenido y
# se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
# Parámetros de entrada: dos números
# Dato devuelto: El MCD

def CalcularMCD (num1, num2):
   n1, n2 = Intercambiar(num1,num2)
   resto = n1%n2

   if resto == 0:
       return n2

   if resto != 0:

    while resto != 0:
        n1 = n2 #Divisor para a ser dividendo
        n2 = resto #Resto pasa a ser divisor
        resto = n1 % n2 #repetimos operación
    return n2 #Para cuando resto = 0 el divisor que tengamos en ese momento sera MCD


# print(CalcularMCD(39,150)) #Prueba


# Función LeerFracion: Lee por teclado una fracción (numerador y denominador)
#  y lo devuelve como parámetro de entrada y salida.
# Esta función usa SimplificarFraccion para simplificar la fracción leída.
# Datos devueltos: numerador y denominador

def LeerFracion():
  num1 = int(input("Introduce el numerador de la fracción. Debe ser un número entero "))
  num2 = int(input("Introduce el denominador de la fracción. Debe ser un número entero "))
  n1, n2 = SimplificarFracion(num1,num2)
  return n1,n2


# Función SimplificarFracion: Recibe una fracción (numerador y denominador)
#  y lo devuelve la fracción simplificada como parámetro ed entrada y salida.
# Para simplificar hay que dividir numerador y dominador por el MCD del numerador
# y denominador.
# Datos devueltos: numerador y denominador

def SimplificarFracion (n1,n2):
    mcd = CalcularMCD(n1,n2)
    num1 = n1/mcd
    num2 = n2/mcd
    return num1,num2


# print(LeerFraccion()) #comprobación
# print(SimplificarFracion(39,150)) #comprobación


# Función EscribirFracion: Recibe una fracción (numerador y denominador)
#  y lo muestra por pantalla. Muestra numerador partido por denominador. Si el
# denominador es 1 sólo muestra el numerador.
# Parámetros de entrada: numerador y denominador

def EscribirFracion(numerador, denominador):

    if denominador == 1:
        return print(numerador)
    else:
        return print(numerador,"/",denominador)


#print(EscribirFracion(15,1)) #Esta es la función de presentación para el menú


# Función SumarFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es la suma de la primera y la segunda.
# La suma de dos fracciones es otra fracción cuyo `numerador=n1*d2+d1*n2`
# y `denominador=d1*d2`.
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado

def SumarFracciones (numerador1, denominador1, numerador2, denominador2):
    newnumerador = (numerador1*denominador2)+(denominador1*numerador2)
    newdenominador = denominador1*denominador2
    resulnumerador,resuldenominador = SimplificarFracion(newnumerador,newdenominador)

    return resulnumerador,resuldenominador

#print(SumarFracciones(13,20,3,4)) #Resultado antes de simplificar 112/80 después 7/5
#print(SumarFracciones(3,4,5,7)) #Resultado 41/28

# Función RestarFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es la resta de la primera y la segunda.
# La resta de dos fracciones es otra fracción cuyo `numerador=n1*d2-d1*n2`
# y `denominador=d1*d2`.
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado
def RestarFracciones (numerador1, denominador1, numerador2, denominador2):
    newnumerador = (numerador1*denominador2)-(denominador1*numerador2)
    newdenominador = denominador1*denominador2
    resulnumerador,resuldenominador = SimplificarFracion(newnumerador,newdenominador)

    return resulnumerador,resuldenominador

#print(RestarFracciones(5,6,2,3)) #resultado 1/6


# Función MultiplicarFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es el producto de la primera y la segunda.
# La multiplicación de dos fracciones es otra fracción cuyo `numerador=n1*n2`
# y `denominador=d1*d2`
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado

def MiltiplicarFracciones (numerador1, denominador1, numerador2, denominador2):
    newnumerador = numerador1*numerador2
    newdenominador = denominador1*denominador2
    resulnumerador,resuldenominador = SimplificarFracion(newnumerador,newdenominador)

    return resulnumerador,resuldenominador

#print(MiltiplicarFracciones(10,9,6,15)) #resultado 4/9


# Función DividirFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es la división de la primera y la segunda.
# La resta de dos fracciones es otra fracción cuyo `numerador=n1*d2`
# y `denominador=d1*n2`
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado

def DividirFracciones (numerador1, denominador1, numerador2, denominador2):
    newnumerador = numerador1*denominador2
    newdenominador = denominador1*numerador2
    resulnumerador,resuldenominador = SimplificarFracion(newnumerador,newdenominador)

    return resulnumerador,resuldenominador

#print(DividirFracciones(2,3,5,6)) #resultado 4/5

# Crear un programa que utilizando las funciones anteriores muestre un menú para
# operar con fracciones.

#meter en el menú un try excepcion para ZeroDivisionError