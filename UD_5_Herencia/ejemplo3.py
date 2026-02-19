
# Clase padre: Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print(f"Nombre: {self.nombre}")

# Clase Hija: Estudante
class Estudiante(Persona):
    def __init__(self, nombre, curso):
        super().__init__(nombre)  #Llamada al constructor del padre
        self.curso = curso

    # Sobreescribir: deber tener el mismo nombre y
    # la misma (mismos parámetros)
    def saludar(self):
        # Llamos al método saludar del padre
        super().saludar()
        print(f"Nombre: {self.curso}")

estudiante = Estudiante("Pedro","2ºDAM")
estudiante.saludar()

print(Estudiante.__mro__)