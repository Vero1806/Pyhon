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
