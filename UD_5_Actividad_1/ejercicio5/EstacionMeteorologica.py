from datetime import date

from Muestra import Muestra


class EstacionMeteorologica:

    def __init__(self):
        self.muestras = []

    def add_muestra(self, temperatura,fecha=date.today()):
        self.muestras.append(Muestra(temperatura,fecha))