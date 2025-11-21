
"""
Ejercicio 4) Crea una función que pida al usuario un número entero y valide que
realmente lo es. La función debe recibir como parámetro un mensaje que se mostrará
al usuario, y devolverá el número introducido una vez validado.
"""
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("El valor no es entero")

def pedir_entero_rango(mensaje, min=0, max=10):
    while True:
        try:
            valor = int(input(mensaje))
            if max >= valor >= min:
                return valor
            else:
               print(f"El valor debe estar entre {min} y {max}")
        except ValueError:
            print("El valor no es entero")

def pedir_entero_positivo(mensaje, min=0):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= min:
                return valor
            else:
               print(f"El valor debe estar entre {min}")
        except ValueError:
            print("El valor no es entero")