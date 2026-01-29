
# Ejercicio 1) Tienes una lista de números y quieres sumar 5 a cada número. Usa la función map()
print("EJERCICIO 1")
print("===========")
numeros = [1,2,3,4,5]
resultado1 = list(map( lambda x : x + 5, numeros))
print(resultado1)

# Ejercicio 2) Dada una lista de números con decimales, queremos una nueva lista con cada número
# redondeado al entero más cercano. Utiliza la función map()
print("EJERCICIO 2")
print("===========")
decimales = [10.345, 12.789, 6, 3.1416]
resultado2 = list(map( lambda x : round(x,2), decimales ) )
print(resultado2)

# Ejercicio 4) Dada una lista de palabras, usa map() para crear una nueva lista con la longitud de cada palabra.
print("EJERCICIO 4")
print("===========")
palabras = ["hola mundo","Fin"]
resultado3 = list(map(len , palabras))
print(resultado3)

# Ejercicio 5) Dada una lista de números, usa filter() para eliminar los números negativos.
print("EJERCICIO 4")
print("===========")
numeros = [-1,-2,3,-4,5]
resultado4 = list(filter(lambda x : x > 0, numeros))
print(resultado4)


# Ejercicio 9) En un inventario representado como un diccionario, cada producto tiene una cantidad
# disponible como valor. Crea una función propia que determine si un producto no tiene stock
# y utiliza filter() sobre los pares (producto, cantidad) del diccionario para encontrar solo
# los productos cuya cantidad sea 0. Finalmente, imprime los nombres de los productos sin stock.

print("EJERCICIO 9")
print("===========")
inventario = {
    'pan': 10,
    'peras': 0,
    'platanos' : 0,
    'leche' : 4
}

productosSinStock = list(filter( lambda item: item[1] == 0 , inventario.items()))
nombresSinStock = list(map(lambda item: item[0], productosSinStock))
print(nombresSinStock)
