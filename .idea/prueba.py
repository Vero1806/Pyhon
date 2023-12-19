class DNI:
    def __init__(self, numero):
        self.__numero = numero
        self.__letra = self.calcular_letra()

    def calcular_letra(self):
        letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
        indice_letra = int(self.__numero) % 23
        letra = letras_dni[indice_letra]
        return letra

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def letra(self):
        return self.__letra

    @letra.setter
    def letra(self, letra):
        self.__letra = letra


class Persona:
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
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad


class Notas:
    def __init__(self):
        self.__notas = {}

    def add_notas(self, asignatura, nota):
        self.__notas[asignatura] = nota

    def mod_notas(self, asignatura, nueva_nota):
        if asignatura in self.__notas:
            self.__notas[asignatura] = nueva_nota

    def del_notas(self, asignatura):
        if asignatura in self.__notas:
            del self.__notas[asignatura]

    def calcular_media(self):
        if not self.__notas:
            return 0
        return sum(self.__notas.values()) / len(self.__notas)


class Alumno(Persona, Notas):
    def __init__(self, dni, nombre, edad):
        Persona.__init__(self, dni, nombre, edad)
        Notas.__init__(self)


# Ejemplo de uso
dni_alumno = DNI("12345678")
alumno = Alumno(dni_alumno, "Juan Perez", 20)

# Agregar notas
alumno.add_notas("Matematicas", 8.5)
alumno.add_notas("Historia", 7.0)
alumno.add_notas("Ciencias", 9.2)

# Modificar nota
alumno.mod_notas("Historia", 8.0)

# Mostrar información del alumno
print(f"Nombre: {alumno.nombre}")
print(f"DNI: {alumno.dni.numero}-{alumno.dni.letra}")
print(f"Edad: {alumno.edad}")
print(f"Notas: {alumno.calcular_media()}")
