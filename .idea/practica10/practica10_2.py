# Vamos a realizar la clase DNI donde vamos a guardar el número de DNI (lo vamos a
# guardar en una cadena de longitud 8) y la letra correspondiente.
#  Vamos a crear el constructor, que recibe el número de DNI y calcula
# automáticamente la letra.
#  Crearemos también los métodos setters y getters.

class DNI ():
    def __init__(self, numero):
        self.__numero = numero

        letrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
        indiceLetra = self.__numero % 23
        letra = letrasDNI[indiceLetra]
        self.__letra = letra

    @property
    def numero (self):
        return self.__numero

    @numero.setter
    def numero (self, numero):
        self.__numero = numero

    @property
    def DNIcompleto(self):
        return self.__numero+self.__letra


# A continuación creamos la clase Persona. Una persona tendrá un DNI, un nombre y
# una edad.
#  Creamos el constructor.
#  Crearemos también los métodos seters y getters.

class Persona (DNI):
    def __init__(self, dni, nombre, edad):
        super().__init__(dni.DNIcompleto)
        self.__nombre = nombre
        self.__edad = edad

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
        self__notas = {}

    def addNotas (self, asignatura, notas):
        self.__notas[asignatura] = notas

    def modNotas(self, asignatura, nuevaNota):
        if asignatura in self.__notas:
            self.__notas[asignatura] = nuevaNota

    def delNotas(self, asignatura):
        if asignatura in self.__notas:
            del self.__notas[asignatura]

    def calcular_media(self):
        return sum(self.__notas.values()) / len(self.__notas)

# La clase Alumno se hereda de las clases anteriores: Persona y Notas.
class Alumno(Persona, Notas):
    def __init__(self, dni, nombre, edad):
        super().__init__(dni, nombre, edad)



# Ejemplo de uso
numero_dni = 12345678
dni_alumno = DNI(numero_dni)
alumno = Alumno(dni_alumno, "Juan Perez", 20)

# Agregar notas
alumno.add_notas("Matematicas", 8.5)
alumno.add_notas("Historia", 7.0)
alumno.add_notas("Ciencias", 9.2)

# Modificar nota
alumno.mod_notas("Historia", 8.0)

# Mostrar información del alumno
print(f"Nombre: {alumno.nombre}")
print(f"DNI: {alumno.dni_completo}")
print(f"Edad: {alumno.edad}")
print(f"Notas: {alumno.calcular_media()}")