'''
▪ Crea la clase abstracta Figura con métodos abstractos: dibujar() y mostrar_datos()
▪ Crea las subclases: Rectangulo y Cuadrado, define los atributos necesarios y que ue implementan los métodos:
□ Método dibujar() muestra la figura con * según dimensiones
▪ Crear objetos y probar los métodos
'''

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def dibujar(self):
        pass
    @abstractmethod
    def mostrar_datos(self):
        pass

class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def dibujar(self):
        '''
        for _ in range(self.lado):
            for _ in range(self.lado):
                print("*",end="")
            print()
        '''
        for _ in range(self.lado):
            print("*" * self.lado)

    def mostrar_datos(self):
        print(f"Cuadrado con lado {self.lado}")

class Rectangulo(Figura):
    def __init__(self, base,altura):
        self.base = base
        self.altura = altura

    def dibujar(self):
        for _ in range(self.altura):
            print("*" * self.base)
    def mostrar_datos(self):
        print(f"Rectángulo con base {self.base} y altura {self.altura}")

cuadrado = Cuadrado(3)
cuadrado.mostrar_datos()
cuadrado.dibujar()

rectangulo = Rectangulo(3,2)
rectangulo.mostrar_datos()
rectangulo.dibujar()