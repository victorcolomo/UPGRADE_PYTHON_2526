'''
▪ Crea una clase Persona con atributos nombre y edad.
▪ Implementa:
□ __str__ para mostrar “Nombre: X, Edad: Y años”.
□ __eq__ para comparar si dos personas son iguales por nombre y edad.
□ __lt__ para comparar edades.
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    def __eq__(self, other):
        return isinstance(other, Persona) and self.nombre == other.nombre and self.edad == other.edad

    def __lt__(self, other):
        #return type(other) == type(self) and self.edad < other.edad
        return isinstance(other, Persona) and self.edad < other.edad

p1 = Persona("Pepe", 20)
p2 = Persona("Pepe", 20)
p3 = Persona("Ana", 18)
print(type(12))
print(type(p1) == type(p2))
print(p1)
print(p1 == p2)
print(p3 < p1)