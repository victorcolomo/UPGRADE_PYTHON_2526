notas = {"Juan" : 7, "Ana" : 8, "Pepe" : 9}
notas["Victor"] = 10  # Añadimos elemento

if "Ana" in notas:
    notas["Ana"] = 9 # Modificamos valor
else:
    print("No existe")

if "Ana" in notas:
    notas.pop("Ana")

# Solo mostrar las claves
print("SOLO CLAVES")
for clave in notas.keys():
    print(clave)

# Solo mostrar las valores
print("SOLO VALORES")
for valor in notas.values():
    print(valor)

# Recorremos claves y valores
print("CLAVES Y  VALORES")
for clave, valor in notas.items():
    print(f"{clave} = {valor}")