class Autor:
    def __init__(self, nombreAutor, paisAutor):
        self.__nombreAutor = nombreAutor
        self.__paisAutor = paisAutor

    @property
    def nombreAutor(self):
        return self.__nombreAutor

    @nombreAutor.setter
    def nombreAutor(self, nombreAutor):
        self.__nombreAutor = nombreAutor

    @property
    def paisAutor(self):
        return self.__paisAutor

    @paisAutor.setter
    def paisAutor(self, paisAutor):
        self.__paisAutor = paisAutor


class Libro(Autor):
    def __init__(self, titulo, autor, anio):
        self.__titulo = titulo
        super().__init__(autor.nombreAutor, autor.paisAutor)
        self.__anio = anio

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        self.__anio = anio


class Biblioteca(Libro):
    def __init__(self):
        super().__init__("", Autor("", ""), "")
        self.__libros = []

    def agregarLibro(self, libro):
        self.__libros.append(libro)

    def listarLibros(self):
        for libro in self.__libros:
            print("Título", libro.titulo, "autor", libro.nombreAutor, "país", libro.paisAutor, "año", libro.anio)

    def buscarLibroAutor(self, autor):
        librosEncontrados = []
        for libro in self.__libros:
            if libro.nombreAutor.lower() == autor.lower():
                librosEncontrados.append(libro)
        return librosEncontrados

    def buscarLibroTitulo(self, titulo):
        librosLocalizados = []
        for libro in self.__libros:
            if libro.titulo.lower() == titulo.lower():
                librosLocalizados.append(libro)
        return librosLocalizados


autorPedro = Autor("Pedro Lopez", "España")
autorAlex = Autor("Alejandro Gonzalez", "México")

libroViaje = Libro("Viaje al centro del mundo", autorPedro, 1998)
libroMar = Libro("Viaje submarino", autorPedro, 1999)
libroSol = Libro("Un Sol en el centro de la Tierra", autorAlex, 1945)
libroTon = Libro("Ton Rider", autorAlex, 1955)

biblioteca = Biblioteca()
biblioteca.agregarLibro(libroViaje)
biblioteca.agregarLibro(libroMar)
biblioteca.agregarLibro(libroSol)
biblioteca.agregarLibro(libroTon)

print("Listado de libros")
biblioteca.listarLibros()

print("")

autorBuscar = input("Dime el autor del que quieras buscar los libros ")
print("Los libros del autor", autorBuscar, "son: ")
buscar = biblioteca.buscarLibroAutor(autorBuscar)
for libro in buscar:
    print("Título", libro.titulo, "año", libro.anio)

tituloBuscar = input("Dime el título del libro que quieras buscar ")
print("Los libros con título", tituloBuscar, "son: ")
buscar = biblioteca.buscarLibroTitulo(tituloBuscar)
for libro in buscar:
    print("Autor", libro.nombreAutor, "año", libro.anio)