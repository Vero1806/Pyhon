# Función Login: Recibe un nombre de usuario y una contraseña, y devuelve un
# valor lógico: verdadero si se ha introducido el nombre y la contraseña adecuadas (usuario1,asdf).
# Además devuelve el numero de internos
# Parámetros de entrada: nombre y contraseña, y el número de intentos actual
# Datos devueltos: Valor lógico indicando si ha hecho login, e intentos



def login(usuario,contra,contador):

    if usuario == "usuario1" and contra == "asdf" and contador < 4:
        return (True,contador+1)
    else:
       return (False,contador+1)


# Crear un programa principal donde se pida un nombre de usuario y una contraseña
# y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.


veces = 0

while True:
    user = input("Introduce el usuario ")
    cont = input("Introduce la contraseña ")

    acierta, veces = login(user,cont,veces) # acierta, veces = True,contador+1 or False,contador+1 lo que esta antes del igual la devolución, lo que esta dentro de los parentesis (lo que le introduzco a la función)
    if acierta:
        print("La contraseña es correcta")
        break
    else:
        print("Contraseña incorrecta. Intentos =", veces)

        if veces == 3:
            print("Has fallado", contador, "veces. El usuario se ha bloqueado")
            break




