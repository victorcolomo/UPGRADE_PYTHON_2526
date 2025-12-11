import email

import Utilidades

def add_contacto(contactos):
    nombre = Utilidades.pedir_texto("Ingrese el nombre del contacto: ")
    telefono = Utilidades.pedir_entero("Ingrese el telefono del contacto: ")
    email = Utilidades.pedir_texto("Ingrese el email del contacto: ")
    if existe_contacto(contactos,email):
        print("El contacto ya existe")
    else:
        contactos.append([nombre,telefono,email])
        print("Añadimos contacto")

def existe_contacto(contactos, email):
    for contacto in contactos:
        if email == contacto[2]:
            return True
    return False

def posicion_contacto(contactos, email):
    posicion = 0
    for contacto in contactos:
        if email == contacto[2]:
            return posicion
        posicion += 1
    return -1

def buscar_contacto(contactos):
    email = Utilidades.pedir_texto("Ingrese el email del contacto: ")
    posicion = posicion_contacto(contactos, email)
    if posicion != -1:
        print(f"{'Nombre':<20} {'Telefono':<15} {'Email':<20}")
        print("-" * 55)
        print(f"{contactos[posicion][0]:<20} {contactos[posicion][1]:<15} {contactos[posicion][2]:<20}")
    else:
        print("No existe contacto")

def eliminar_contacto(contactos):
    email = Utilidades.pedir_texto("Ingrese el email del contacto: ")
    posicion = posicion_contacto(contactos, email)
    if posicion != -1:
        contactos.pop(posicion)
        print("Eliminado contacto")
    else:
        print("No existe contacto")

def mostrar_todos(contactos):
    if len(contactos) == 0:
        print("No hay contactos")
    else:
        print(f"{'Nombre':<20} {'Telefono':<15} {'Email':<20}")
        print("-"*55)
        for c in contactos:
            print(f"{c[0]:<20} {c[1]:<15} {c[2]:<20}")