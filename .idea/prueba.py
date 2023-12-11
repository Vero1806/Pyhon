import csv


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