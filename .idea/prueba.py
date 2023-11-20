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