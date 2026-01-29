
class Conductor:
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni

    def __str__(self):
        # Para que no nos de error tenemos que convertir los datos en una sola cadena de texto
        return f"CONDUCTOR {self.__nombre} DNI {self.__dni}"