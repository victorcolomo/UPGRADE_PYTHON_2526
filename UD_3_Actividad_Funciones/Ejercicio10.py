"""
Ejercicio 10) Una factoría es aquel número cuya suma de los factoriales de sus dígitos es
igual al propio número. Por ejemplo:
145 = 1! + 4! + 5! = 145
40585 = 4! + 0! + 5! + 8! + 5! = 40585
Usa funciones para determinar si un número es una factoría

"""
from UD_3_Actividad_Funciones import Utilidades


def es_factoria(numero):
    valor_inicial = numero
    suma_factoriales = 0
    while numero > 0:
        digito = numero % 10
        # Por cada digito calculamos el factorial
        suma_factoriales += factorial(digito)
        numero = numero // 10

    # Para saber si un numero es factoria comparamos si suma_factoriales == numero
    return suma_factoriales == valor_inicial


def factorial(numero):
    resultado = 1
    for n in range(2,numero+1):
        resultado *= n
    return resultado

def es_factoria2(numero):
    valor_inicial = numero
    suma_factoriales = 0
    for digito in str(numero):
        suma_factoriales += factorial(int(digito))

    # Para saber si un numero es factoria comparamos si suma_factoriales == numero
    return suma_factoriales == valor_inicial

n = Utilidades.pedir_entero_positivo("Dime un numero")
if es_factoria2(n):
    print(f"{n} es factoria")
else:
    print(f"{n} no es factoria")

