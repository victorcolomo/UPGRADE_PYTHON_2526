'''
Diseña una clase Libro que represente libros de una biblioteca.
▪ Tiene como atributos: título, autor, número de páginas y prestado (True/False)
▪ Métodos:
□ prestar(): marca el libro como prestado si no lo está.
□ devolver(): marca el libro como disponible.
□ mostrar_informacion(): muestra toda la información del libro.
'''
class Libro:

    def __init__(self, titulo, autor, num_paginas=0):
        self.__titulo = titulo
        self.__autor = autor
        self.__num_paginas = num_paginas
        self.__prestado = False

    def get_prestado(self):
        return self.__prestado

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            return True
        else:
            return False

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            return True
        else:
            return False

    def mostrar_informacion(self):
        estado = "Prestado" if self.__prestado else "Devuelto"
        print(f'Titulo {self.__titulo} Autor: {self.__autor} Paginas: {self.__num_paginas} Estado: {estado}')


    def __str__(self):
        estado = "Prestado" if self.__prestado else "Devuelto"
        return f'Titulo {self.__titulo} Autor: {self.__autor} Paginas: {self.__num_paginas} Estado: {estado}'
