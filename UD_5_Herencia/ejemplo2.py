
# Clase padre: Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print("Hola soy una persona")

# Clase Hija: Estudante
class Estudiante(Persona):
    # Sobreescribir: deber tener el mismo nombre y
    # la misma (mismos parámetros)
    def saludar(self):
        print("Hola soy un estudiante")

estudiante = Estudiante("Pedro")
estudiante.saludar()

print(Estudiante.__mro__)
