'''
▪ Tienes que:
□ Crear varios dispositivos.
□ Mostrar la información de cada uno.
□ Mostrar el total de dispositivos creados.

'''

from Dispositivo import *

dispositivo1 = Dispositivo("Iphone14","Telefono")
dispositivo2 = Dispositivo("Oppo","Telefono")
dispositivo3 = Dispositivo("Ipad","Tablet")

dispositivo1.mostrar_info()
dispositivo2.mostrar_info()
dispositivo3.mostrar_info()

Dispositivo.mostrar_total()