numeros = [12,4,1,7,1]

def mayor_5(n):
    return n > 5

mayores = list(filter(mayor_5, numeros))
print(mayores)

print("CON EXPRESIONES LAMBDA")
mayores2 = list(filter( lambda n : n > 5, numeros))
print(mayores2)


print("MAP CON DICCIONARIOS")
edades = {'Ana': 20, 'Juan': 15, 'Maria': 30}
# Duplicar las edades
resultado = filter(lambda k: edades[k] > 18, edades)
print(list(resultado))

edades = {'Ana': [20, "Madrid"], 'Juan': [15, "Barcelona"], 'Maria': [30, "Sevilla"]}
# Duplicar las edades
resultado = filter(lambda k: edades[k][0] > 18 and edades[k][1]== "Madrid", edades)
print(list(resultado))


edades = {'Ana': {"Edad" : 20, "Ciudad": "Madrid"},
          'Juan': {"Edad" :15, "Ciudad": "Barcelona"},
         'Maria': {"Edad" : 30, "Ciudad": "Sevilla"}
          }
# Duplicar las edades
print("MAYORES 18 y DE MADRID")
resultado = filter(lambda k: edades[k]["Edad"] > 18 and edades[k]["Ciudad"]== "Madrid", edades)
claves = list(resultado)
for nombre in claves:
    print(nombre,edades[nombre]["Edad"])
    
