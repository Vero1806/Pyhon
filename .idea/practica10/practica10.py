class Autor:
    def __init__(self,nombreAutor, paisAutor):
        self.__nombreAutor = nombreAutor
        self.__paisAutor = paisAutor

    @property
    def nombreAutor(self):
        return self.__nombreAutor

    @nombreAutor.setter
    def nombreAutor(self,nombreAutorNuevo):
        self.__nombreAutor=nombreAutorNuevo

    @property
    def paisAutor(self):
        return __nombreAutor

    @paisAutor.setter
    def paisAutor(self,paisAutorNuevo):
        self.__paisAutor=paisAutorNuevo

        ###

    def mostrarAutor(self):
        return print(self.__nombreAutor,self.__paisAutor)



class Libro:
    def __init__(self,titulo,autor,anio):

        self.__titulo = titulo
        super().__init__(nombreAutor, paisAutor)
        self.__anio = anio


    @property
    def titulo(self):
        return __titulo

    @titulo.setter
    def titulo(self,tituloNuevo):
        self.__titulo=tituloNuevo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    @property
    def anio(self):
        return __anio

    @anio.setter
    def anio(self,anioNuevo):
        self.__anio=anioNuevo

    def mostrarLibro(self):
        return print(self.__titulo,self.__autor,self.__anio)

autorPedro = Autor("Pedro López", "España")
autorAlex = Autor("Alejandro Gonzalez", "México")


libroViaje = Libro ("Viaje al centro del mundo", autorPedro,1998)
libroSol = Libro ("Un Sol en el centro de la Tierra", autorAlex,1945)

print(autorPedro)
print(autorAlex)

print("")

autorPedro.mostrarAutor()
autorAlex.mostrarAutor()
libroViaje.mostrarLibro()
libroSol.mostrarLibro()


