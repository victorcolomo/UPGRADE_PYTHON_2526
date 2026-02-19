
# Clase padre: Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print("Hola soy una persona")

# Clase Hija: Estudante
class Estudiante(Persona):
    # No añadimos nada, hereda todo del padre
    pass


estudiante = Estudiante("Pedro")
estudiante.saludar()

print(isinstance(estudiante, Estudiante))
print(isinstance(estudiante, Persona))