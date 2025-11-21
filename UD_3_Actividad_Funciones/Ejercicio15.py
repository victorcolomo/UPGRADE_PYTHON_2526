"""
Ejercicio 15) Cread una función que calcule el precio total de un artículo tras aplicarle el IVA,
la función recibe dos parámetros: uno el valor sobre el que se calcula y el otro el porcentaje a aplicar.
 Si no se indica el porcentaje de IVA se entiende que es el 21% (es un parámetro por defecto u omisión).
 En el cuerpo de la función debes comprobar si el IVA está comprendido entre 0 y 100, si no es así se debe
 aplicar el 21%
"""

def calcular_precio_final(precio, iva=21):
    if iva <= 0 or iva > 100:
        iva = 21
    return precio + (precio * iva / 100)

final = calcular_precio_final(100,10000)
print(f"El precio final es {final}")



