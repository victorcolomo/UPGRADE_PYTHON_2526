'''
□ Crea al menos 3 objetos Libro distintos y almacénalos en una lista
□ Presta uno de ellos.
□ Muestra la información de todos los libros.
□ Muestra la información de los libros disponible
'''

from Libro import *

libro1 = Libro("100 años de soledad","Marquez",325)
libro2 = Libro("Titulo 2","Pepe")
libro3 = Libro("Titulo 3","Ana",220)

libro2.prestar()

print("TODOS LOS LIBROS")
biblioteca = [libro1,libro2,libro3]
for libro in biblioteca:
    #print(str(libro))
    libro.mostrar_informacion()

print("LOS LIBROS DISPONIBLE")
for libro in biblioteca:
    if libro.get_prestado():
        libro.mostrar_informacion()
