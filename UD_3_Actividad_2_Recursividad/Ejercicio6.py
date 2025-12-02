# Ejercicio 6) Función que recibe un número entero positivo y lo convierta a binario
# utilizando recursividad.

def convertir_binario(n):
    if n < 2:
        print(n,end="")
    else:
        convertir_binario(n // 2)
        print(n % 2, end="")

numero = int(input("Ingresa un numero: "))
convertir_binario(numero)