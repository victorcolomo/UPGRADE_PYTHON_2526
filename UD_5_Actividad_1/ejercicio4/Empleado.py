class Empleado:
    def __init__(self, nombre, puesto):
        self.__nombre = nombre
        self.__puesto = puesto

    def __str__(self):
        return f'Nombre {self.__nombre} Puesto: {self.__puesto}'