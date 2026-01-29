
from Coche import *

c1 = Coche("Seat","León",2500)
c2 = Coche("Seat","Arona")

c1.mostrar()
print("------------")
c2.mostrar()
print("------------")

c1.set_Marca("Ford")
print(c1.get_Marca())

c1.modelo = "Focus"
print(c1.modelo)