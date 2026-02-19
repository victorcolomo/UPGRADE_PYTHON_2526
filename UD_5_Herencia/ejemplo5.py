from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadradro(Figura):
    def __init__(self,lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

# No se puede declarar un método de la una clase abstracta
# f = Figura()
cuadrado = Cuadradro(10)
print(cuadrado.area())
