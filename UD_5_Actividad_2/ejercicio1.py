# Creamos el tipo enumerado TipoVivienda
from enum import Enum

class TipoVivienda(Enum):
    PISO = "Piso"
    DUPLEX = "Dúplex"
    CHALET = "Chalet"


# Clase Vivienda
class Vivienda():
    # Constructor
    def __init__(self, tipo=None, num_habitaciones=0, metros_cuadrados=0.0, precio=0.0, ciudad="", barrio=""):
        self.tipo = tipo
        self.num_habitaciones = num_habitaciones
        self.metros_cuadradados = metros_cuadrados
        self.precio = precio
        self.ciudad = ciudad
        self.barrio = barrio

    # Get y set de precio
    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    # comision(): devuelve el 3% del precio
    def comision(self):
        return self.precio * 0.03

    # __str__(): devuelve una cadena con todos los datos incluyendo la comisión
    def __str__(self):
        return (f"Tipo: {self.tipo.value}, num_habitaciones: {self.num_habitaciones} ,"
                f"metros cuadradados: {self.metros_cuadradados} , precio: {self.precio} , "
                f"ciudad: {self.ciudad}, barrio: {self.barrio}")


class Casa(Vivienda):
    def __init__(self, tipo=None, num_habitaciones=0, metros_cuadrados=0.0, precio=0.0, ciudad="", barrio="",
                 parcela=0.0, piscina=False):
        # Llamar al constructor del padre
        super().__init__(tipo,num_habitaciones,metros_cuadrados,precio,ciudad,barrio)
        self.parcela = parcela
        self.piscina = piscina

    def __str__(self):
        return super().__str__() + f" Parcela {self.parcela} Piscina {self.piscina}"




'''
▪ Subclase Piso que añade:
□ atributo: exterior (bool)
□ Sobrescribir comision() de modo que si los metros cuadrados > 100 sea 3.5%
'''



class Piso(Vivienda):
    def __init__(self, tipo=None, num_habitaciones=0, metros_cuadrados=0.0, precio=0.0, ciudad="", barrio="",
                 exterior=False):
        # Llamar al constructor del padre
        super().__init__(tipo,num_habitaciones,metros_cuadrados,precio,ciudad,barrio)
        self.exterior = exterior

    def comision(self):
        '''
        if  self.metros_cuadradados > 100:
            return self.precio * 0.035
        else:
            return super().comision()
        '''
        return self.precio * 0.035 if self.metros_cuadradados > 100 else super().comision()

casa1 = Casa(TipoVivienda.CHALET, 3, 120,225000, "Madrid",
             "Hortaleza", 140, True)
print(casa1)
print(f"Comision {casa1.comision()}")

piso1 = Piso(TipoVivienda.DUPLEX,4,200,330000, "Barcelona","Centro",False)
print(piso1)
print(f"Comision {piso1.comision()}")