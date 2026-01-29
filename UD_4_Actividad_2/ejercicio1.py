import numpy as np
'''
Crea dos arrays de Numpy de tamaño 5, llenos de números enteros. 
Luego, calcula la suma de ambos arrays elemento por elemento y muestra el resultado.
'''
lista = [1,4,5,6]
a = np.array(lista)
b = np.array([7,8,9,10])

suma = a + b
print(suma)


'''
Crea un array de Numpy de tamaño 6 con valores enteros de tu elección. Luego, 
multiplica cada elemento del array por 3 y muestra el resultado.
'''
c = np.array([1,2,3,4,5,6])
multiplicacion = c * 3
print(multiplicacion)


'''
Crea un array de Numpy con 10 números enteros de tu elección. Calcula el promedio de los elementos y muestra el resultado.
Numpy permite calcular el promedio de los elementos de un array con la función np.mean() de forma rápida y eficiente, algo que con listas requeriría escribir más código.

'''
d = np.array([1,2,3,4,5,6,7,8,9,10])
promedio = np.mean(d)
print(promedio)


'''
Ejercicio 4) Filtrar elementos mayores a un valor dado
Crea un array de Numpy con 8 números enteros. Luego, crea un nuevo array que solo contenga 
los elementos mayores a 5 y muéstralo.
Con Numpy, puedes aplicar filtros de manera muy rápida usando operaciones de comparación 
en una sola línea. Filtrar listas de esta forma requeriría escribir bucles y condicionales adicionales
'''
e = np.array([1,20,3,4,5,6,7,8])
mayores5 = e[e>5]
print(mayores5)