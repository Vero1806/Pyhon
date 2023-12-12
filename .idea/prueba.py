#4) Crear un programa que pida al usuario los apellidos de un alumno y
# devuelva todas sus notas ordenadas de mayor a menor y la calificación media
import csv
import tkinter as tk
#from tkinter import messagebox


def obtenerNotasYMedia(apellido):
    # Inicializar lista para almacenar las notas del alumno
    notas = []

    with open('datos.csv', mode="r", encoding='utf-8') as archivo:
        lectorCsv = csv.DictReader(archivo, delimiter=';')

        for fila in lectorCsv:
            if fila['Apellidos'].lower() == apellido.lower():
                nota = float(fila['Nota'])
                notas.append(nota)

    if not notas:
        return None  # No se encontró al alumno

    # Calcular la calificación media
    media = sum(notas) / len(notas)

    # Ordenar las notas de mayor a menor
    notasOrdenadas = sorted(notas, reverse=True) #notasOrdenadas = sorted(notas)[::-1]

    return notasOrdenadas, media

def mostrar_resultados():
    apellidoUsuario = entrada_apellido.get()
    notasAlumno, mediaAlumno = obtenerNotasYMedia(apellidoUsuario)

    if notasAlumno is not None:
        resultados = f"Notas del alumno {apellidoUsuario}: {notasAlumno}\nCalificación media: {mediaAlumno}"
        labelResultado.config(text=f"Resultados {resultados}")
    else:
        labelResultado.config(text=f"Error. No se encontró al alumno con el apellido {apellidoUsuario}.")

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Consulta de Notas")

# Crear elementos de la interfaz
etiqueta_apellido = tk.Label(ventana, text="Ingrese el apellido del alumno:")
etiqueta_apellido.pack()
labelResultado = tk.Label(ventana, text="")

entrada_apellido = tk.Entry(ventana)
entrada_apellido.pack()

boton_consultar = tk.Button(ventana, text="Consultar", command=mostrar_resultados)
boton_consultar.pack()
labelResultado.pack()
# Iniciar el bucle de eventos de Tkinter
ventana.mainloop()