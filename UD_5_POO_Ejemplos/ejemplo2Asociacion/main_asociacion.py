from Conductor import Conductor
from UD_5_POO_Ejemplos.ejemplo2Asociacion.Coche import Coche

# def __init__(self, marca, modelo, conductor, km=0):
conductor= Conductor("Pepe","12312A")
coche1 = Coche("Ferrario","A5",conductor)


coche1.mostrar()