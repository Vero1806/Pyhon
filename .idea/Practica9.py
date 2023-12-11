'''
1) Con la ayuda de ChatGPT, elaborar un esquema con el funcionamiento y las características principales del módulo TKINTER
para la elaboración de interfaces gráficas. Realizar una interfaz gráfica para cualquiera de los programas desarrollados
con anterioridad que sea personalizada por cada uno y en la que aparezcan convenientemente comentados todas las explicaciones
sobre qué hace cada cosa y qué personalizaciones hemos incluido
'''
import tkinter as tk
import datetime

def mostrar_solo_fecha():
    fechaCompleta = datetime.datetime.now()
    label_resultado.config(text=fechaCompleta.strftime("Hoy es %d de %B del año %Y"))

def mostrar_solo_hora():
    fechaCompleta = datetime.datetime.now()
    label_resultado.config(text=fechaCompleta.strftime("%H:%M:%S"))

def mostrar_fecha_y_hora():
    fechaCompleta = datetime.datetime.now()
    label_resultado.config(text=fechaCompleta.strftime("%d-%m-%Y %H:%M:%S"))

def mostrar_hora_am_pm():
    fechaCompleta = datetime.datetime.now()
    label_resultado.config(text=fechaCompleta.strftime("Son las %I:%M:%S %p"))

# Crear la ventana
ventana = tk.Tk()
ventana.title("Primera ventana de Vero en Python")

# Crear widgets
label_menu1 = tk.Label(ventana, text="-------Menú de formato de Fechas--------")
label_menu2 = tk.Label(ventana, text="¿En qué formato quieres mostrar la fecha?")
label_resultado = tk.Label(ventana, text="")

# Crear botones
boton1 = tk.Button(ventana, text="1. Solo fecha", command=mostrar_solo_fecha)
boton2 = tk.Button(ventana, text="2. Solo hora", command=mostrar_solo_hora)
boton3 = tk.Button(ventana, text="3. Fecha y hora", command=mostrar_fecha_y_hora)
boton4 = tk.Button(ventana, text="4. Hora formato am/pm", command=mostrar_hora_am_pm)

# Posicionar widgets
label_menu1.pack()
label_menu2.pack()

# Posicionar botones a la izquierda
boton1.pack()
boton2.pack()
boton3.pack()
boton4.pack()

label_resultado.pack()

# Iniciar el bucle de la ventana
ventana.mainloop()

'''
#Crear un fichero csv del estilo con suficientes registros para realizar los siguientes algoritmos :
"Nombre";"Apellidos";"Curso";"Asignatura";"Nota" \
                                          "José Luis";"Pineda Requena";"2ºDAM";"HLC";9.5
'''

'''
2) Escribir en un fichero nuevo llamado aprobados.csv con el mismo formato en el que aparezcan solo los que han aprobado
'''

#Escribir en un fichero nuevo llamado aprobados.csv con el mismo formato en el que aparezcan solo los que han aprobado

import csv

notasAprobadas = []

with open("datos.csv",mode="r",encoding='utf-8') as datosAbierto:
    lectorCsv = csv.DictReader(datosAbierto, delimiter=";")

    #for fila in lector_csv:
    #    print(fila)
    for fila in lectorCsv:
        nota = (fila['Nota'])
        notaFload = float(nota)
        if notaFload > 5:
            notasAprobadas.append(fila)
            #print(fila)


with open ("aprobados.csv",mode="w",encoding='utf-8', newline="") as aprobadosAbierto:
    campos = ["Nombre","Apellidos","Curso","Asignatura","Nota"]
    escribir = csv.DictWriter(aprobadosAbierto, fieldnames=campos, delimiter=';')

    # Escribir el encabezado
    escribir.writeheader()

    # Escribir las filas seleccionadas
    escribir.writerows(notasAprobadas)


#Volver a abrir el archivo en modo lectura para que imprima lo que ha copiado
with open ("aprobados.csv",mode="r",encoding='utf-8') as aprobadosAbierto:
    leer = csv.DictReader(aprobadosAbierto, delimiter=';')
    for fila in leer:
        print(fila)

print("Filas seleccionadas guardadas en 'aprobados.csv'.")

'''
3) Crear un nuevo fichero en el que se exporte la nota media de cada alumno: "Nombre";"Apellidos";"NotaMedia"
'''

# Crear un diccionario para almacenar las notas de cada alumno
notasAlumno = {}

# Abrir el archivo CSV con los datos de los estudiantes
with open("datos.csv", mode="r", encoding="utf-8") as datosAbierto:
    lector_csv = csv.DictReader(datosAbierto, delimiter=";")

    # Recorrer cada fila del archivo CSV
    for fila in lector_csv:
        # Obtener los detalles del estudiante
        nombre = fila["Nombre"]
        apellidos = fila["Apellidos"]
        nota = float(fila["Nota"])

        # Calcular la nota media del estudiante
        if (nombre, apellidos) not in notasAlumno:
            notasAlumno[(nombre, apellidos)] = {"notas": [], "notaMedia": 0.0}

        notasAlumno[(nombre, apellidos)]["notas"].append(nota)

# Calcular la nota media de cada estudiante
for estudiante, info in notasAlumno.items():
    notas = info["notas"]
    notaMedia = sum(notas) / len(notas)
    info["notaMedia"] = round(notaMedia, 2)

# Crear un nuevo archivo CSV con la nota media de cada estudiante
with open("notaMediaEstudiantes.csv", mode="w", encoding="utf-8", newline="") as notasMediasArchivo:
    campos = ["Nombre", "Apellidos", "NotaMedia"]
    escritor_csv = csv.DictWriter(notasMediasArchivo, fieldnames=campos, delimiter=";")

    # Escribir el encabezado
    escritor_csv.writeheader()

    # Escribir la nota media de cada estudiante
    for estudiante, info in notasAlumno.items():
        nombre, apellidos = estudiante
        notaMedia = info["notaMedia"]
        escritor_csv.writerow({"Nombre": nombre, "Apellidos": apellidos, "NotaMedia": notaMedia})

with open("notaMediaEstudiantes.csv", mode="r", encoding="utf-8") as notasMediasArchivo:
    leer = csv.DictReader(notasMediasArchivo, delimiter=';')
    for fila in leer:
        print(fila)

print("Nota media de cada estudiante guardada en 'notaMediaEstudiantes.csv'.")
'''
4) Crear un programa que pida al usuario los apellidos de un alumno y devuelva todas sus notas ordenadas de mayor a menor y la calificación media
'''



'''
5) Crear una interfaz gráfica para el apartado 4)
'''
