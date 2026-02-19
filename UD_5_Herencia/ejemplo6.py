class Persona():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Nombre: {self.name} - Edad {self.age}"

    # Para poder ordenar objetos de tipo Persona, tenemos que
    # que definir una funcion para el operador < , para que que
    # se pueda comparar objetos
    def __lt__(self, other):
        if self.age == other.age:
            return self.name < other.name
        else:
            return self.age < other.age

personas = [
    Persona('John', 25),
    Persona('Peter', 22),
    Persona('Jane', 22),
]

Persona('John', 25) <   Persona('Peter', 22)

personas.sort()

for p in personas:
    print(p)