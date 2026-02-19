
from Empleado import *
from EquipoTrabajo import *

empleado1 = Empleado("Ana","Frontend")
empleado2 = Empleado("Juna","Backend")

equipo = EquipoTrabajo("Desarrollo")
equipo.add_empleado(empleado1)
equipo.add_empleado(empleado2)

equipo.mostrar_empleados()

del equipo

print(str(empleado1))