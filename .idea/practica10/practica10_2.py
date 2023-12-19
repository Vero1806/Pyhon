# Vamos a realizar la clase DNI donde vamos a guardar el número de DNI (lo vamos a
# guardar en una cadena de longitud 8) y la letra correspondiente.
#  Vamos a crear el constructor, que recibe el número de DNI y calcula
# automáticamente la letra.
#  Crearemos también los métodos setters y getters.

class DNI ():
    def __init__(self, numero):
        self.__numero = numero
        self.__letra = self.calcularLetra()

    @property
    def numero (self):
        return self.__numero

    @numero.setter
    def numero (self, numero):
        self.__numero = numero

    @property
    def letra (self):
        return self.__letra

    @letra.setter
    def letra (self, letra):
        self.__letra = letra

    def calcularLetra(self):
        letrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
        indiceLetra = int(self.__numero) % 23
        letra = letrasDNI[indiceLetra]
        return letra


    # def dniCompleto(self):
    #     return str(self.numero)+str(self.letra)


# A continuación creamos la clase Persona. Una persona tendrá un DNI, un nombre y
# una edad.
#  Creamos el constructor.
#  Crearemos también los métodos seters y getters.

class Persona ():
    def __init__(self, dni, nombre, edad):
        self.__dni = dni
        self.__nombre = nombre
        self.__edad = edad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre (self, nombre):
        self.__nombre

    @property
    def edad (self):
        return self.__edad

    @edad.setter
    def edad (self, edad):
        self.__edad


# La clase Notas nos permite guardar una serie de notas por asignatura.
#  Creamos el constructor, teniendo en cuenta que la estructura de datos que
# vamos a utilizar para guardar asignaturas y notas será un diccionario.
#  Creamos métodos para gestionar las notas: addnotas, modnotas, delnotas
#  Creamos un método que nos devuelve la media de las notas guardadas

class Notas ():
    def __init__(self):
        self.__notas = {}

    def addNotas (self, asignatura, notas):
        self.__notas[asignatura] = notas

    def modNotas(self, asignatura, nuevaNota):
        if asignatura in self.__notas:
            self.__notas[asignatura] = nuevaNota

    def delNotas(self, asignatura):
        if asignatura in self.__notas:
            del self.__notas[asignatura]

    def calcularMedia(self):
        return round(sum(self.__notas.values()) / len(self.__notas),2)

# La clase Alumno se hereda de las clases anteriores: Persona y Notas.
class Alumno(Persona, Notas):
    def __init__(self, dni, nombre, edad):
        Persona.__init__(self, dni, nombre, edad)
        Notas.__init__(self)


# Ejemplo de uso
dniAlumno = DNI("12345678")
alumno = Alumno(dniAlumno, "Juan Perez", 20)

# Agregar notas
alumno.addNotas("Matematicas", 8.5)
alumno.addNotas("Historia", 7.0)
alumno.addNotas("Ciencias", 9.2)
alumno.addNotas("Ingles", 6.0)

# Modificar nota
alumno.modNotas("Historia", 8.0)
alumno.delNotas("Matematicas")

# Mostrar información del alumno
print(f"Nombre: {alumno.nombre}")
print(f"DNI: {alumno.dni.numero}-{alumno.dni.letra}")
print(f"Edad: {alumno.edad}")
print(f"Notas Media: {alumno.calcularMedia()}")