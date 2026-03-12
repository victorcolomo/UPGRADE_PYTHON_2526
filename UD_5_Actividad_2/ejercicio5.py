'''
Ejercicio 5) Herencia múltiple
▪ Crea dos clases: Terrestre con método moverse() que imprime “Anda” y Acuatico con moverse() que imprime “Nada”.
▪ Crea una clase Cocodrilo que herede de ambas clases.
▪ Sobrescribe moverse() en Cocodrilo para llamar al método de ambas clases usando super() de forma controlada.
▪ Comprueba el orden de ejecución y usa Cocodrilo.__mro__ para visualizar el MRO.
'''
class Terreste:
    def moverse(self):
        print('Anda')

class Acuatico:
    def moverse(self):
        print('Nada')

class Cocodrilo(Terreste, Acuatico):
    def moverse(self):
        Terreste.moverse(self)
        Acuatico.moverse(self)

c = Cocodrilo()
print(Cocodrilo.__mro__)
c.moverse()
