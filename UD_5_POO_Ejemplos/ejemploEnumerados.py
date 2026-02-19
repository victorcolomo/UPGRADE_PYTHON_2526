# enumerado TipoVivienda: Piso, Dúplex o Chalet

from enum import Enum

class TipoVivienda(Enum):
    PISO = "Piso"
    DUPLEX = "Dúplex"
    CHALET = "Chalet"

class TipoViviendaValor(Enum):
    PISO = ("Piso",100000)
    DUPLEX = ("Dúplex", 150000)
    CHALET = ("Chalet", 200000)

class TipoViviendaCampos(Enum):
    PISO = ("Piso",100000)
    DUPLEX = ("Dúplex", 150000)
    CHALET = ("Chalet", 200000)

    def __init__(self,nombre, precio):
        self.nombre = nombre
        self.precio = precio

vivienda = TipoViviendaCampos.PISO

print(vivienda)
print(vivienda.nombre)
print(vivienda.precio)