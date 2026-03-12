import json

usuarios = [
    {
        "nombre": "Ana",
        "apellido": "Perez",
        "notas" : [5,7,8]
    },
    {
        "nombre": "Juan",
        "apellido": "Gomez",
        "notas": [8,2,3]
    }
]
# Guardamos la lista de usuarios en el archivo JSON
with open("datos.json","w",encoding="utf-8") as jsonfile:
    json.dump(usuarios,jsonfile,indent=4)

# Leemos el fichero json
with open("datos.json","r",encoding="utf-8") as jsonfile:
    # Load convertimos una lista de diccionarios
    datos = json.load(jsonfile)

for usuario in datos:
    print(usuario["nombre"])
    print(usuario["notas"][0])
