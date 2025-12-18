
numeros = [12,4,1,7,1]
numeros_ordenados = sorted(numeros)
print("ORDEN ASCENDENTE")
print(numeros_ordenados)

print("ORDEN DESCENDENTE")
numeros_ordenados = sorted(numeros, reverse=True)
print(numeros_ordenados)

nombres = ["pepe","juan","ana","eva"]
nombres_ordenados = sorted(nombres)
print("ORDEN ALFABETICO")
print(nombres_ordenados)

print("ORDEN POR TAMAÑO")
nombres_ordenados_size = sorted(nombres, key=lambda c : len(c))
print(nombres_ordenados_size)

print("DICCIONARIO ORDENADO POR CAMPOS")
alumnos = { 'Ana': [20, 1.65],
            'Juan': [25, 1.80],
            'Maria': [20, 1.70],
            'Pedro': [25, 1.75] }
alumnos_ordenados = sorted(alumnos, key = lambda k : (alumnos[k][0] , -alumnos[k][1]) )
print(alumnos_ordenados)