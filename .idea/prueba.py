#4) Crear un programa que pida al usuario los apellidos de un alumno y
# devuelva todas sus notas ordenadas de mayor a menor y la calificación media
import csv

def obtenerNotasYMedia(apellido, archivoCsv):
    # Inicializar listas para almacenar las notas del alumno
    notas = []

    with open(archivoCsv,mode="r",encoding='utf-8') as archivo:
        lectorCsv = csv.DictReader(archivo, delimiter=';')


        for fila in lectorCsv:
            if fila['Apellidos'].lower() == apellido.lower():
                nota = (fila['Nota'])
                notaFload = float(nota)
                notas.append(nota)

        print(notas)

    if not notas:
        return None, None  # No se encontró al alumno

    # Calcular la calificación media
    media = sum(notas) / len(notas)

    # Ordenar las notas de mayor a menor
    notasOrdenadas = sorted(notas, reverse=True)

    return notasOrdenadas, media

# Solicitar al usuario el apellido del alumno
apellidoUsuario = input("Ingrese el apellido del alumno: ")

# Especificar el nombre del archivo CSV
archivoCsv = 'datos.csv'  # Reemplazar con el nombre real de tu archivo

# Obtener las notas y la calificación media
notasAlumno, mediaAlumno = obtenerNotasYMedia(apellidoUsuario, archivoCsv)

# Mostrar los resultados
if notasAlumno is not None:
    print(f"Notas del alumno {apellidoUsuario}: {notasAlumno}")
    print(f"Calificación media: {mediaAlumno}")
else:
    print(f"No se encontró al alumno con el apellido {apellidoUsuario}.")