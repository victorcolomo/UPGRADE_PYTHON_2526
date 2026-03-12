'''
Ejercicio 6) Vectores con operadores matemáticos
▪ Crea una clase Vector con atributos x e y.
▪ Sobrescribe los métodos:
□ __add__ para sumar dos vectores.
□ __sub__ para restar vectores.
□ __mul__ para multiplicación por escalar.
▪ Crea varios vectores y realiza operaciones combinadas (suma, resta, multiplicación).
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __str__(self):
        return f"Vectores: {self.x}, {self.y}"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)