
class Coche:
    # Atributos de clase
    vendidos=0
    # Constructor __init__(self,....)
    # En los métodos de instancia, self es obligatorio al primer parametro
    # Visibilidad
    # atributo -> publico
    # __atributo -> private
    def __init__(self, marca, modelo, km=0):
        self.__marca = marca  # self es lo mismo que this en java
        self.__modelo = modelo
        self.__km = km
        self.__cantidad = 0
        Coche.vendidos += 1

    # Metodos
    def mostrar(self):
        print("Vendidos",Coche.vendidos)
        print(self.__marca, self.__modelo, "KM",self.__km, "Cantidad",self.__cantidad)

    # Getter y setter en foma java
    def get_Marca(self):
        return self.__marca

    def set_Marca(self, marca):
        self.__marca = marca

    # Fomato python
    @property
    def modelo(self):           # equivalente a get_modelo
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):   # equivalente a set_modelo
        self.__modelo = modelo


    def __del__(self):
        print("Objeto coche eliminado")

