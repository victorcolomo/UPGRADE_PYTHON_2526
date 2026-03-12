'''
Ejercicio 1) Archivo de texto: guardar una lista de nombres en un archivo
▪ Escribe un programa en Python que haga lo siguiente:
□ Pida al usuario que introduzca una serie de nombres uno a uno.
□ La introducción de nombres terminará cuando el usuario escriba la palabra FIN.
□ Todos los nombres introducidos deben almacenarse en una lista.
□ Finalmente, el programa deberá crear un archivo de texto llamado nombres.txt y guardar cada nombre
en una línea distinta.
▪ Nota:
□ Si el archivo ya existe, debe sobrescribirse.
□ El archivo debe quedar en la misma carpeta que el programa.
'''
# Definimos la lista de nombres vacío
nombres = []
while True:
    nombre =input("Ingrese nombre: ")
    # Condición de salida
    if nombre.upper() == "FIN":
        break
    nombres.append(nombre)

# Recorremos la lista de nombres y lo añadimos en el fichero
with open("nombres.txt", "w",encoding="utf-8") as archivo:
    for nombre in nombres:
        # Tenemos que incluir el salto de línea
        archivo.write(nombre+"\n")
