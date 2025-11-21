"""
EJERCICIO 7) Escribe el código de una función que dibuje en pantalla un rectángulo de
dimensiones dadas con un símbolo que se le especifica. Por ejemplo, la llamada al
procedimiento dibujar_rectangulo(3,5,’#’) produciría la siguiente salida:
    #####
    #####
    #####
"""

def dibujar_rectangulo(filas, columnas, simbolo):
    for _ in range(filas):
        for _ in range(columnas):
            print(simbolo,end="")
        print()

def dibujar_rectangulo2(filas, columnas, simbolo):
    for _ in range(filas):
        print(simbolo * columnas)


dibujar_rectangulo2(3,5,"#")