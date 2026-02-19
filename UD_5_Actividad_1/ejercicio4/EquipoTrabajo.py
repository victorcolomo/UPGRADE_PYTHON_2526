class EquipoTrabajo():

    def __init__(self, nombre_equipo):
        self.__nombre = nombre_equipo
        self.empleados = []

    def add_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(str(empleado))