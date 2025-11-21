"""
Ejercicio 3) Escribe el código de una función que devuelve la potencia de un número,
recibirá dos números enteros (base y exponente) y devolverá la potencia.
Calcula la potencia usando un bucle (sin usar operadores de potencia)
"""
from UD_3_Actividad_Funciones.Utilidades import *

def calcular_potencia(base, exponente):
    potencia = 1
    for _ in range(exponente):
        potencia *= base

    return potencia if exponente >= 0 else 1 / potencia
    """ Comprobamos si en exponente es negativo
    if exponente < 0:
        return 1 / potencia
    else:
        return potencia
    """

base = pedir_entero("Dime la base")
exponente = pedir_entero("Dime la exponente")
print(f"Potencia de {base} elevado a {exponente} = {calcular_potencia(base, exponente)}")