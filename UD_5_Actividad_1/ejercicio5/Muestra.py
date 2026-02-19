from datetime import date


class Muestra:
    def __init__(self, temperatura:float, fecha=date.today()):
        self.temperatura = temperatura
        self.fecha = fecha

    def __str__(self):
        return f'Tº {self.temperatura} de {self.fecha}'

    def get_temperatura(self):
        return self.temperatura

    def get_fecha(self):
        return self.fecha