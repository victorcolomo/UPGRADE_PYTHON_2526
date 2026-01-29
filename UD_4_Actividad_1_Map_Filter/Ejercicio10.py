'''
Ejercicio 10) Crea un programa que gestione un diccionario de productos, donde la clave sea el código de barras y el valor sea otro diccionario con nombre, precio, stock y categoría. Implementa un menú que permita:
1. Aplicar el IVA (21%) a todos los productos y mostrar el precio con IVA.
2. Mostrar los productos con stock bajo (<10 unidades).
3. Ordenar los productos por precio y, en caso de empate, por nombre.
4. Salir del programa.
# Diccionario de productos
'''
# Diccionario con los productos
productos = {
    '123456': {'nombre': 'Manzanas', 'precio': 0.9, 'stock': 20, 'categoria': 'Fruta'},
    '234567': {'nombre': 'Leche', 'precio': 0.9, 'stock': 5, 'categoria': 'Lácteo'},
    '345678': {'nombre': 'Pan', 'precio': 1.0, 'stock': 8, 'categoria': 'Panadería'},
    '456789': {'nombre': 'Huevos', 'precio': 2.5, 'stock': 12, 'categoria': 'Lácteo'},
    '567890': {'nombre': 'Platanos', 'precio': 1.8, 'stock': 3, 'categoria': 'Fruta'},
}

# Constante para el IVA
IVA = 0.21

def aplicarIVA():

    precioConIVA = map( lambda item: item[1]['nombre'] + "->"
                                     + str(round(item[1]['precio'] * (1 + IVA),2) ) , productos.items())

    for p in precioConIVA:
        print(p)

def mostrarStockBajo():
    stockBajo = filter(lambda item : item[1]['stock'] < 10 , productos.items())
    for codigo, datos  in stockBajo:
        print(datos['nombre'] + " - > "+str(datos['stock']))


# Ordenar los productos por precio y, en caso de empate, por nombre.
def ordenarProductos():
    productosOrdenados = sorted(productos.items(),
                                key=lambda item: (item[1]['precio'] ,item[1]['nombre'] ))

    for codigo, datos in productosOrdenados:
        print(datos['nombre'] + " - > "+str(datos['precio']) + " - > "+str(datos['stock']))


def menu():
    while True:
        print("\n---MENU ---")
        print("1. Aplicar el IVA (21%) a todos los productos y mostrar el precio con IVA.")
        print("2. Mostrar los productos con stock bajo (<10 unidades).")
        print("3. Ordenar los productos por precio y, en caso de empate, por nombre.")
        print("4. Salir del programa.")

        opcion = input("Dime una opción:")

        if opcion == "1":
            aplicarIVA()
        elif opcion == "2":
            mostrarStockBajo()
        elif opcion == "3":
            ordenarProductos()
        elif opcion == "4":
            break
        else:
            print("Opcion no valida")




menu()

