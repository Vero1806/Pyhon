'''
Ejercicio4: Supongamos un diccionario que contiene como clave el nombre de una persona y como valor una lista con todos sus "gustos". Hagamos un programa que agregue "gustos" a la persona:
Si la persona no existe, la agrega al diccionario
Si la persona existe y el gusto existe en su lista, no tiene ningún efecto.
Si la persona existe y el gusto no existe en su lista, agrega el gusto a la lista.
Se deja de pedir personas cuando introducimos el carácter "*".
'''

agenda = {'Pepe':['patinar', 'nadar', 'fiesta'],
          'Juan':['pizza', 'cine', 'tele']}


#print(person['Pepe']) comprobación

persona = " "

while persona != "*":

    persona = input("Para que persona de la lista ")


    gusto = input("Dime que gusto quieres agregar ")



    if persona in agenda:
        agenda[persona].append(gusto)
        print("Se ha agregado el gusto", gusto, "a", persona,".")
        print(agenda)
    else:
        print(persona, "no se encuentra en la agenda.")
        print(agenda)


print(agenda)

