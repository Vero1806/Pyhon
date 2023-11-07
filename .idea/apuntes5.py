dicionario = {'uno':1, 'dos':2} #clave : valor

a=dict(one=1,two=2)

b={}

len(dicionario)
dicionario['dos'] #me devolvera 2 porque es el valor asociado

del(dicionario['dos']) #borrara elemento y clave

'dos' in dicionario #devuevle true o false

a=dicionario.copy #copia el interior y no se elimina si ilimino cosa de la variable dicionario

dicionario.clear() #borra el interior

a.update(dicionario) #concadena a y diccionario
a.get('uno') #devuelve 1. igual que dicionario['dos']

aux = a.pop('dos') #borra el 2 de la lista, lo muestra y lo guarda como valor INT en la variable aux

a.items() #devuelven dict_items con los indices y los valores del dicionario

claves = a.keys() #claves del diccionario

valores = a.values() #valores del diccionario

a.setdefault ('ocho',8) #añade la clave y el valor en el dicionario si la clave ya existe no lo mete

try:
    num = int(input("Ingrea un número: "))
    resul = 10/num
except ZeroDivisionError or Exception: #excepcion multiple
    print("Division por cero")
except ValueError:
    print("Division por cero")
else: #excepcion no definida
    print("el resultao es erroneo")
finally:
    print("el resultado es ", resul)
