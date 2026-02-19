class VehiculoCombustion:
    km_litro = 15
    def __init__(self, deposito_litros):
        print("Inicializando el vehiculo combustion")
        self.deposito_litros = deposito_litros
    # Devuelve los km que podemos recorrer
    def autonomia(self):
        return self.deposito_litros * VehiculoCombustion.km_litro # por cada litro podemos recorrer 5 km
    def repostorar(self):
        self.deposito_litros += self.km_litro

class VehiculoElectrico:
    km_kwh = 5
    def __init__(self, bateria_kwh):
        print("Inicializando el vehiculo electrico")
        self.bateria_kwh = bateria_kwh
    def autonomia(self):
        return self.bateria_kwh * VehiculoElectrico.km_kwh  # por cada litro podemos recorrer 5 km
    def repostorar(self):
        self.bateria_kwh += self.bateria_kwh

class HibridoEnchufable(VehiculoCombustion, VehiculoElectrico):
    def __init__(self, deposito_litros, bateria_kwh):
        #super().__init__(deposito_litros)
        VehiculoCombustion.__init__(self, deposito_litros)
        VehiculoElectrico.__init__(self, bateria_kwh)
    # Sobreescribimos el metodo autonomia
    def autonomia(self):
        return self.bateria_kwh + self.deposito_litros

print(HibridoEnchufable.__mro__)
hibrido = HibridoEnchufable(100, 10)
print(hibrido.autonomia())
print(isinstance(hibrido, HibridoEnchufable))
print(isinstance(hibrido, VehiculoCombustion))
print(isinstance(hibrido, VehiculoElectrico))