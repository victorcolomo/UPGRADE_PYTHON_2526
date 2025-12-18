numeros = [12,4,1,7,1]

def sumar_2(n):
    return n + 2

#map devuelve un objeto iterable, no es una lista
resultado = map(sumar_2, numeros)
for numero in resultado:
    print(numero)

resultado2 = list(map(sumar_2, numeros))
print(resultado2)
print(resultado2[0])

# Map con expresiones lambda
print("MAP CON EXPRESIONES LAMBDA")
numeros = list(map( lambda n : n+2 , numeros))
print(numeros)

print("MAP CON DICCIONARIOS")
edades = {'Ana': 20, 'Juan': 25, 'Maria': 30}
# Duplicar las edades
resultado = map(lambda k: [k, edades[k]+1], edades)
print(list(resultado))