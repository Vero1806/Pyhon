'''
Ejercicio08: Vamos a crear un programa que lea por teclado las temperaturas mínimas de los 3 primeros
meses del año de distintas ciudades, de la forma dic = {'Londres': [3.4, 6.3, 10.5],
'Oslo': [-3.8, -5.0, 4.2], 'Rennes': [2.5, 3.1, 12.3]} y una vez obtenido el carácter de salida * nos devuelva:
- El valor medio de las temperaturas de cada ciudad (redondear a 2 decimales).
- El valor mínimo de las temperaturas de cada ciudad
- Una lista con la ciudad con la temperatura más baja y su valor
'''
temperaturas = {}

while True:
    ciudad = input("Introduce la ciudad de las temperaturas que vamos a comparar ")
    if nombre == "*":
        break
    valor1 = float(input("Temperatura minima de enero "))
    if nombre == "*":
        break
    valor2 = float(input("Temperatura mínima de febrero "))
    if nombre == "*":
        break
    valor3 = float(input("Temperatura mínima de marzo "))
    if nombre == "*":
        break

temperaturas[ciudad]=(valor1,valor2,valor3)

print(temperaturas)