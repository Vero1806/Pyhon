
# Función Convertir_A_Segundos: Recibe una cantidad de horas, minutos y segundos
# y calcula a cuantos segundos corresponde.
# Parámetros de entrada: hora, minutos y segundos
# Dato devuelto: Segundos totales

def Convertir_A_Segundos (horas,minutos,segundos):
    horas_segundos = horas*3600
    minutos_segundos = minutos*60
    segundos_totales = horas_segundos+minutos_segundos+segundos
    return segundos_totales


# Función Convertir_A_HMS: Recibe una cantidad de segundos y debe calcular a
# que hora, minutos y segundos corresponde
# Parámetros de entrada: segundos
# Valores de salida: hora,minutos y segundos

def Covertir_a_HMS (segundos2):
    horas2 = round(segundos2/3600)
    minutos2 = round((segundos2%3600)/60)
    segundos_finales = minutos2%60
    return (horas2,minutos2,segundos_finales)


# Escribe un programa principal con un menú donde se pueda elegir la opción de
# convertir a segundos, convertir a horas,minutos y segundos o salir del programa.

while True:
    print("-----Menú de calculadora de horas -------")
    print("1. Convertir una hora concreta a segundos ")
    print("2. Convertir segundos a una hora concreta ")
    print("0. Salir")
    opcion = int(input(""))

    if opcion == 1:
        h1 = int(input("Dime el número de horas "))
        m1 = int(input("Dime el número de minutos "))
        s1 = int(input("Dime el número de segundos "))

        segund = Convertir_A_Segundos(h1,m1,s1)

        print(h1, "horas,", m1, "minutos y", s1, "son igual a ", segund,"segundos en total ")

    if opcion == 2:
        s2 = int(input("Dime los segundos totales para pasarlos a horas, minutos y segundos "))

        hour,minut,secon = Covertir_a_HMS(s2)

        print(s2,"segundos son", hour, "horas,", minut, "minutos y", secon, "segundos ")

    if opcion == 0:
        print("Fin del programa")
        break



