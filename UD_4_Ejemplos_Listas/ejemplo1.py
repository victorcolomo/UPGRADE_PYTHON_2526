
# Declaramos lista
lista = [ 1, 5, "ana" , 12.7 , "ana" ]
print(lista)
# Modifica valor
lista[-1]= "pepe"
# inserta elementos
lista.append(23)
lista.insert(1,"Eva")
lista.append("ana")
print(lista)
# busqueda de elementos
print("Ana en la lista " , lista.count("ana"))
print("Posicion Ana en la lista " , lista.index("ana",lista.index("ana")+1))

print("CONTENIDO DE LA LISTA")
for x in lista:
    print(x)

# eliminar elementos
''' lista.pop()
lista.pop(0)
lista.remove("ana")
print(lista)
lista.clear()
print(lista)
'''
print("Tamaño: " , len(lista))
if "ana" in lista:
    print("Esta en la lista")
else:
    print("No esta en la lista")
