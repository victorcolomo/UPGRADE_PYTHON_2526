'''
Diseña una clase Dispositivo para representar dispositivos electrónicos.
▪ Atributos de clase: total_dispositivos (contador común a todos los objetos).
▪ Atributos de instancia: nombre y tipo
▪ Métodos:
□ Constructor que incremente el contador de dispositivos.
□ mostrar_info(): muestra nombre y tipo.
□ mostrar_total() (método de clase): muestra el número total de dispositivos creados.

'''
class Dispositivo:
    # Atributos de clase
    total_dispositivos = 0

    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo
        Dispositivo.total_dispositivos += 1

    def mostrar_info(self):
        print(f'Nombre: {self.__nombre} tipo: {self.__tipo}')

    @classmethod
    def mostrar_total(cls):
        print(f'Total de dispositivos creados.{cls.total_dispositivos}')