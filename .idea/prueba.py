'''
Ejercicio7: Vamos a crear un diccionario (pidiendo los valores por pantalla hasta introducir *)
donde las claves son los nombres de los vinos y el valor una lista con la información sobre la denominación de origen,
añada y precio.
Después, hagamos un programa en que, dado el diccionario de vinos y
una lista con un rango de precios [menorPrecio, mayorPrecio], nos devuelva una lista de los nombres, ordenados
alfabéticamente de los vinos que estén en este rango de precios.
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

