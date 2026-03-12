class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def precio_con_impuestos(self):
        return self.precio
    def __str__(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Precio: {self.precio} Precion con impuestos: {self.precio_con_impuestos():.2f}"

'''
▪ Subclases: Coche, Moto, Camion
□ Cada subclase hereda de Vehiculo y sobrescribe precio_con_impuestos (). Por ejemplo: Coche: 5% del precio, Moto: 3% del precio y Camión: 7% del precio
□ Método __str__() para mostrar la información del vehículo (marca, modelo, precio, y precio con impuestos).
'''
class Coche(Vehiculo):
    def __init__(self, marca, modelo, precio):
        Vehiculo.__init__(self, marca, modelo, precio)
    def precio_con_impuestos(self):
        return self.precio * 1.05
    def __str__(self):
        return "Coche " + super().__str__()

class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio):
        Vehiculo.__init__(self, marca, modelo, precio)
    def precio_con_impuestos(self):
        return self.precio * 1.03
    def __str__(self):
        return "Moto " + super().__str__()

class Camion(Vehiculo):
    def __init__(self, marca, modelo, precio):
        Vehiculo.__init__(self, marca, modelo, precio)
    def precio_con_impuestos(self):
        return self.precio * 1.07
    def __str__(self):
        return "Camion " + super().__str__()

'''
▪ Clase Flota
□ atributo:_Lista de vehículos
□ Métodos:
o	agregar_vehiculo(vehiculo):  añade un vehículo a la lista
o	mostrar_precio_con_impuestos(): recorre la lista y llama a precio_con_impuestos() de cada Vehiculo
o	valor_total_flota(): devuelve la suma de los precios de todos los vehículos
o	mostrar_flota(): imprime todos los vehículos con su información completa
o	mostrar_solo_coches(): muestra sólo los coches
o	buscar_por_marca(marca): devuelve lista de vehículos que coinciden con la marca
'''
class Flota:
    def __init__(self):
        self.vehiculos = []
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_precio_con_impuestos(self):
        print("PRECIO CON IMPUESTOS")
        print("====================")
        for v in self.vehiculos:
            print(v.precio_con_impuestos())

    def valor_total_flota(self):
        '''
        total = 0
        for v in self.vehiculos:
            total += v.precio_con_impuestos()
        return total
        '''
        return sum(v.precio_con_impuestos() for v in self.vehiculos)

    def mostrar_flota(self):
        print("FLOTA")
        print("=====")
        for v in self.vehiculos:
            print(v)

    def mostrar_solo_coches(self):
        print("LISTADO DE COCHES")
        print("=================")
        for v in self.vehiculos:
            if isinstance(v, Coche):
                print(v)

    def buscar_por_marca(self, marca):
        '''
        lista_marca = []
        for v in self.vehiculos:
            if v.marca.lower() == marca.lower():
                lista_marca.append(v)
        return lista_marca
        '''
        return [v for v in self.vehiculos  if v.marca.lower() == marca.lower() ]


# Creamos objeto de tipo flota
flota = Flota()
# Agregamos vehículos
flota.agregar_vehiculo(Moto("Yamaha","Modelo1",15000))
flota.agregar_vehiculo(Coche("Seat","Leon",16000))
flota.agregar_vehiculo(Camion("Seat","Modelo3", 30000))
# Llamamos al resto de los metodos
flota.mostrar_flota()
flota.mostrar_solo_coches()
flota.mostrar_precio_con_impuestos()
flota.buscar_por_marca("Seat")
print(f"Valor total: {flota.valor_total_flota()}")
